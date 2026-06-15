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
      contentType: archivo.type || "text/html",
      upsert: true,
    });
    if (error) throw new Error("No se pudo subir la guía: " + error.message);
  }

  await supabase.from("guias_curso").insert({ curso_id: cursoId, titulo, dia, tipo, orden, archivo_path });
  revalidatePath(`/admin/cursos/${cursoId}`);
}

// Marca el curso como "listo" (habilita el acceso del estudiante a sus guías).
export async function habilitarCurso(cursoId: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("cursos").update({ estado: "listo", progreso_pct: 100 }).eq("id", cursoId);
  revalidatePath(`/admin/cursos/${cursoId}`);
}

// Elimina una guía.
export async function eliminarGuia(cursoId: string, guiaId: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("guias_curso").delete().eq("id", guiaId);
  revalidatePath(`/admin/cursos/${cursoId}`);
}
