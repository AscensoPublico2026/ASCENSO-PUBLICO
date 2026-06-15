"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";

// Sube una guía (HTML) al curso y la registra.
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
 * cuando se cumplan las 12h desde la compra (preparacion_deadline).
 * Si ya pasaron las 12h, se ve inmediatamente.
 */
export async function marcarCursoListo(cursoId: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("cursos").update({ estado: "listo" }).eq("id", cursoId);
  revalidatePath(`/admin/cursos/${cursoId}`);
}

/**
 * "Habilitar ahora" — Acceso inmediato (casos especiales, amigos, etc).
 * Pone el curso en estado "listo" Y elimina el deadline (el cliente lo ve ya).
 */
export async function habilitarCursoAhora(cursoId: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("cursos").update({
    estado: "listo",
    preparacion_deadline: new Date().toISOString(), // deadline = ahora = ya pasó
  }).eq("id", cursoId);
  revalidatePath(`/admin/cursos/${cursoId}`);
}

// Elimina una guía.
export async function eliminarGuia(cursoId: string, guiaId: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("guias_curso").delete().eq("id", guiaId);
  revalidatePath(`/admin/cursos/${cursoId}`);
}
