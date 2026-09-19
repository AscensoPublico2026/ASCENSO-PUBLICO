"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";
import { getGuiaCatalogo } from "@/lib/catalogoGuias";
import { copiarPlanDesdeOPEC, PLANES_PLANTILLA } from "@/lib/autocargarGuias";
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
 * "Armar plan completo desde una plantilla" — Inserta de una sola vez TODAS
 * las guías de un plan predefinido (ver PLANES_PLANTILLA en autocargarGuias.ts),
 * resolviendo cada guía por su CÓDIGO contra el catálogo (biblioteca.json). Así
 * el admin arma un curso completo (Días 1 a 21) con un clic, sin subir HTML ni
 * teclear guía por guía. Es idempotente: no duplica las que ya estén asignadas
 * (compara por archivo_path) y omite con aviso las que no estén publicadas.
 *
 * @returns objeto con conteos {insertadas, omitidas, faltantes[]} — se usa para
 *          mostrar un resumen al admin.
 */
export async function armarPlanPlantilla(cursoId: string, planId: string) {
  await requireAdmin();
  const plan = PLANES_PLANTILLA[planId];
  if (!plan) throw new Error(`No existe la plantilla de plan "${planId}".`);

  const supabase = createAdminClient();

  // Guías ya asignadas al curso (para no duplicar).
  const { data: yaTiene } = await supabase
    .from("guias_curso")
    .select("archivo_path")
    .eq("curso_id", cursoId);
  const existentes = new Set((yaTiene || []).map((g: any) => g.archivo_path).filter(Boolean));

  const registros: any[] = [];
  const faltantes: string[] = [];
  let omitidas = 0;

  for (const item of plan.guias) {
    const guia = getGuiaCatalogo(item.codigo);
    // La guía debe existir en el catálogo y tener su HTML publicado en el bucket.
    if (!guia || !guia.archivoPath || guia.estado !== "publicada") {
      faltantes.push(item.codigo);
      continue;
    }
    if (existentes.has(guia.archivoPath)) {
      omitidas++;
      continue;
    }
    registros.push({
      curso_id: cursoId,
      titulo: guia.titulo,
      dia: item.dia,
      tipo: guia.tipo,
      orden: item.orden ?? item.dia ?? 0,
      archivo_path: guia.archivoPath,
    });
  }

  if (registros.length > 0) {
    const { error } = await supabase.from("guias_curso").insert(registros);
    if (error) throw new Error("No se pudo armar el plan: " + error.message);
  }

  revalidatePath(`/admin/cursos/${cursoId}`);
  return { insertadas: registros.length, omitidas, faltantes };
}

/**
 * Wrapper con firma `(formData) => Promise<void>` para usar directamente como
 * `action` de un <form> (Next exige que la action del form no devuelva datos).
 * Delega en `armarPlanPlantilla`. El planId se pasa por bind() o por el form.
 */
export async function armarPlanPlantillaForm(cursoId: string, planId: string, _formData: FormData): Promise<void> {
  await armarPlanPlantilla(cursoId, planId);
}

/**
 * "Rehacer plan (limpiar y armar)" — Deja el curso EXACTAMENTE con el plan de
 * la plantilla:
 *  1) ELIMINA del curso toda guía cuyo archivo_path NO pertenezca al plan
 *     (p. ej. las genéricas CNSC que la auto-carga insertó por error).
 *  2) INSERTA las guías del plan que falten (idempotente, sin duplicar).
 *
 * Resuelve el caso típico: un curso PGN al que se le auto-cargaron las guías
 * genéricas (INTRO-00 CNSC, GEN-01/02/03, ASI-COM/ESP) y hay que sustituirlas
 * por las -PGN-AUX correctas del cargo. Un solo clic deja el plan limpio.
 *
 * @returns {eliminadas, insertadas, conservadas, faltantes[]}
 */
export async function rehacerPlanPlantilla(cursoId: string, planId: string) {
  await requireAdmin();
  const plan = PLANES_PLANTILLA[planId];
  if (!plan) throw new Error(`No existe la plantilla de plan "${planId}".`);

  const supabase = createAdminClient();

  // Resolver las rutas (archivo_path) que SÍ pertenecen al plan.
  const rutasPlan = new Set<string>();
  const faltantes: string[] = [];
  for (const item of plan.guias) {
    const g = getGuiaCatalogo(item.codigo);
    if (g && g.archivoPath && g.estado === "publicada") rutasPlan.add(g.archivoPath);
    else faltantes.push(item.codigo);
  }

  // Guías actuales del curso.
  const { data: actuales } = await supabase
    .from("guias_curso")
    .select("id, archivo_path")
    .eq("curso_id", cursoId);

  // 1) Eliminar las que NO están en el plan (incluye las de archivo_path null/vacío).
  const aEliminar = (actuales || []).filter(
    (g: any) => !(g.archivo_path && rutasPlan.has(g.archivo_path))
  );
  let eliminadas = 0;
  if (aEliminar.length > 0) {
    const ids = aEliminar.map((g: any) => g.id);
    const { error } = await supabase.from("guias_curso").delete().in("id", ids);
    if (error) throw new Error("No se pudieron eliminar las guías sobrantes: " + error.message);
    eliminadas = ids.length;
  }

  // 2) Insertar las del plan que falten (comparando por archivo_path ya presente).
  const restantes = (actuales || []).filter(
    (g: any) => g.archivo_path && rutasPlan.has(g.archivo_path)
  );
  const yaPresentes = new Set(restantes.map((g: any) => g.archivo_path));
  const registros: any[] = [];
  for (const item of plan.guias) {
    const g = getGuiaCatalogo(item.codigo);
    if (!g || !g.archivoPath || g.estado !== "publicada") continue;
    if (yaPresentes.has(g.archivoPath)) continue;
    registros.push({
      curso_id: cursoId,
      titulo: g.titulo,
      dia: item.dia,
      tipo: g.tipo,
      orden: item.orden ?? item.dia ?? 0,
      archivo_path: g.archivoPath,
    });
  }
  if (registros.length > 0) {
    const { error } = await supabase.from("guias_curso").insert(registros);
    if (error) throw new Error("No se pudo armar el plan: " + error.message);
  }

  revalidatePath(`/admin/cursos/${cursoId}`);
  return { eliminadas, insertadas: registros.length, conservadas: restantes.length, faltantes };
}

/** Wrapper `(formData)=>Promise<void>` para usar rehacerPlanPlantilla en un <form>. */
export async function rehacerPlanPlantillaForm(cursoId: string, planId: string, _formData: FormData): Promise<void> {
  await rehacerPlanPlantilla(cursoId, planId);
}
