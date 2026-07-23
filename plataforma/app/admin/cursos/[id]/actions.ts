"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";
import { getGuiaCatalogo } from "@/lib/catalogoGuias";
import { copiarPlanDesdeOPEC } from "@/lib/autocargarGuias";
import { correoCursoListo } from "@/lib/email";

// Formatea fecha/hora en español Colombia (para avisar cuándo estará disponible).
function fmtFechaHora(iso: string | null): string | undefined {
  if (!iso) return undefined;
  try {
    return new Date(iso).toLocaleString("es-CO", {
      day: "2-digit", month: "long", hour: "2-digit", minute: "2-digit", hour12: true,
    });
  } catch { return undefined; }
}

/**
 * Asigna una guía YA EXISTENTE de la biblioteca al curso, por su código.
 * No vuelve a subir el HTML: referencia el archivo que ya vive en el bucket
 * `guias` (subido vía /api/admin/seed-guias). Es la forma rápida de armar
 * el plan: el admin solo elige el código del plan de estudio.
 */
export async function asignarGuiaDesdeBiblioteca(cursoId: string, formData: FormData) {
  await requireAdmin();
  const codigo = String(formData.get("codigo") || "").trim();
  if (!codigo) throw new Error("Selecciona una guía de la biblioteca.");

  const guia = getGuiaCatalogo(codigo);
  if (!guia) throw new Error(`La guía "${codigo}" no existe en la biblioteca.`);
  if (!guia.archivoPath) throw new Error(`La guía "${codigo}" aún no tiene archivo publicado.`);

  // Día/orden: el admin puede ajustarlos según el plan del cliente; si no, se usa el sugerido.
  const diaForm = Number(formData.get("dia") || 0);
  const ordenForm = Number(formData.get("orden") || 0);
  const dia = diaForm > 0 ? diaForm : guia.diaSugerido;
  const orden = ordenForm > 0 ? ordenForm : (guia.diaSugerido ?? 0);

  const supabase = createAdminClient();

  // Evitar duplicados: si ya está esa guía (mismo archivo) en el curso, no la repite.
  const { data: existente } = await supabase
    .from("guias_curso")
    .select("id")
    .eq("curso_id", cursoId)
    .eq("archivo_path", guia.archivoPath)
    .maybeSingle();
  if (existente) throw new Error(`La guía "${codigo}" ya está asignada a este curso.`);

  await supabase.from("guias_curso").insert({
    curso_id: cursoId,
    titulo: guia.titulo,
    dia,
    tipo: guia.tipo,
    orden,
    archivo_path: guia.archivoPath,
  });
  revalidatePath(`/admin/cursos/${cursoId}`);
}

// Sube una guía (HTML) al curso y la registra.
// Se mantiene como fallback para guías PERSONALIZADAS (ej. "Conoce tu Entidad")
// que no están en la biblioteca reutilizable.
export async function subirGuia(cursoId: string, formData: FormData) {
  await requireAdmin();
  const titulo = String(formData.get("titulo") || "").trim();
  const dia = Number(formData.get("dia") || 0) || null;
  const tipo = String(formData.get("tipo") || "general");
  const orden = Number(formData.get("orden") || 0) || 0;
  const archivo = formData.get("archivo") as File | null;
  if (!titulo) throw new Error("Falta el título.");

  const supabase = createAdminClient();
  let archivo_path: string | null = null;
  if (archivo && archivo.size > 0) {
    archivo_path = `${cursoId}/${Date.now()}-${archivo.name}`.replace(/\s+/g, "_");
    const bytes = Buffer.from(await archivo.arrayBuffer());
    const { error } = await supabase.storage.from("guias").upload(archivo_path, bytes, {
      contentType: "text/html; charset=utf-8",
      upsert: true,
    });
    if (error) throw new Error("No se pudo subir la guía: " + error.message);
  }

  await supabase.from("guias_curso").insert({ curso_id: cursoId, titulo, dia, tipo, orden, archivo_path });
  revalidatePath(`/admin/cursos/${cursoId}`);
}

/**
 * "Curso listo" — Admin terminó de preparar el curso.
 * El curso pasa a estado "listo" pero el cliente SOLO lo verá
 * cuando se cumplan las 24h desde la compra (preparacion_deadline).
 * Si ya pasaron las 24h, se ve inmediatamente.
 */
export async function marcarCursoListo(cursoId: string) {
  await requireAdmin();
  const supabase = createAdminClient();

  // Estado previo para decidir si notificar (evita correos duplicados).
  const { data: prev } = await supabase
    .from("cursos")
    .select("estado, preparacion_deadline, profiles(correo, nombre)")
    .eq("id", cursoId)
    .single();

  const ahora = Date.now();
  const deadlineMs = (prev as any)?.preparacion_deadline ? new Date((prev as any).preparacion_deadline).getTime() : null;
  const yaEstabaDisponible = (prev as any)?.estado === "listo" && deadlineMs != null && deadlineMs <= ahora;

  await supabase.from("cursos").update({ estado: "listo" }).eq("id", cursoId);

  // Notifica al cliente que su curso quedó listo (solo si no estaba ya disponible).
  const correo = (prev as any)?.profiles?.correo;
  if (correo && !yaEstabaDisponible) {
    const disponibleAhora = deadlineMs == null || deadlineMs <= ahora;
    await correoCursoListo((prev as any).profiles.correo, (prev as any).profiles.nombre || "", disponibleAhora, fmtFechaHora((prev as any)?.preparacion_deadline));
  }

  revalidatePath(`/admin/cursos/${cursoId}`);
}

/**
 * "Habilitar ahora" — Acceso inmediato (casos especiales, amigos, etc).
 * Pone el curso en estado "listo" Y elimina el deadline (el cliente lo ve ya).
 */
export async function habilitarCursoAhora(cursoId: string) {
  await requireAdmin();
  const supabase = createAdminClient();

  const { data: prev } = await supabase
    .from("cursos")
    .select("estado, preparacion_deadline, profiles(correo, nombre)")
    .eq("id", cursoId)
    .single();

  const ahora = Date.now();
  const deadlineMs = (prev as any)?.preparacion_deadline ? new Date((prev as any).preparacion_deadline).getTime() : null;
  const yaEstabaDisponible = (prev as any)?.estado === "listo" && deadlineMs != null && deadlineMs <= ahora;

  await supabase.from("cursos").update({
    estado: "listo",
    preparacion_deadline: new Date().toISOString(), // deadline = ahora = ya pasó
  }).eq("id", cursoId);

  // Notifica al cliente que ya puede entrar (solo si antes no estaba disponible).
  const correo = (prev as any)?.profiles?.correo;
  if (correo && !yaEstabaDisponible) {
    await correoCursoListo((prev as any).profiles.correo, (prev as any).profiles.nombre || "", true);
  }

  revalidatePath(`/admin/cursos/${cursoId}`);
}

// Elimina una guía.
export async function eliminarGuia(cursoId: string, guiaId: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("guias_curso").delete().eq("id", guiaId);
  revalidatePath(`/admin/cursos/${cursoId}`);
}

/**
 * "Copiar plan del mismo OPEC" — trae las guías (funcionales, entidad,
 * simulacro, etc.) de otro curso ya armado con el mismo OPEC, sin duplicar
 * las que ya estén. Útil para cursos creados antes de la reutilización
 * automática o para rearmar uno rápido.
 */
export async function copiarPlanOPEC(cursoId: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  const { data: curso } = await supabase.from("cursos").select("opec").eq("id", cursoId).single();
  await copiarPlanDesdeOPEC(supabase, cursoId, curso?.opec ?? null);
  revalidatePath(`/admin/cursos/${cursoId}`);
}

/**
 * Guarda el número de inscripción CNSC del candidato.
 * El admin lo agrega cuando el cliente se lo informa por WhatsApp.
 * Queda visible en la ficha del perfil del estudiante.
 */
export async function actualizarNumeroInscripcion(cursoId: string, formData: FormData) {
  await requireAdmin();
  const numero_inscripcion = String(formData.get("numero_inscripcion") || "").trim() || null;
  const supabase = createAdminClient();
  await supabase.from("cursos").update({ numero_inscripcion }).eq("id", cursoId);
  revalidatePath(`/admin/cursos/${cursoId}`);
  revalidatePath(`/perfil/${cursoId}`);
}
