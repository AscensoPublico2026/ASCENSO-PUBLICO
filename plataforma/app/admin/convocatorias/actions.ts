"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";

export async function crearConvocatoria(formData: FormData) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("convocatorias").insert({
    nombre: String(formData.get("nombre") || "").trim(),
    entidad: String(formData.get("entidad") || "").trim() || null,
    estado: String(formData.get("estado") || "proxima"),
    etiqueta: String(formData.get("etiqueta") || "").trim() || null,
    vacantes: String(formData.get("vacantes") || "").trim() || null,
    fecha_prueba_aprox: String(formData.get("fecha_prueba_aprox") || "").trim() || null,
    imagen_url: String(formData.get("imagen_url") || "").trim() || null,
    tema: String(formData.get("tema") || "nacional"),
    orden: Number(formData.get("orden") || 0) || 0,
    activa: true,
  });
  revalidatePath("/admin/convocatorias");
  revalidatePath("/");
}

export async function editarConvocatoria(id: string, formData: FormData) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("convocatorias").update({
    nombre: String(formData.get("nombre") || "").trim(),
    entidad: String(formData.get("entidad") || "").trim() || null,
    estado: String(formData.get("estado") || "proxima"),
    etiqueta: String(formData.get("etiqueta") || "").trim() || null,
    vacantes: String(formData.get("vacantes") || "").trim() || null,
    fecha_prueba_aprox: String(formData.get("fecha_prueba_aprox") || "").trim() || null,
    imagen_url: String(formData.get("imagen_url") || "").trim() || null,
    tema: String(formData.get("tema") || "nacional"),
    orden: Number(formData.get("orden") || 0) || 0,
  }).eq("id", id);
  revalidatePath("/admin/convocatorias");
  revalidatePath("/");
}

export async function toggleConvocatoria(id: string, activa: boolean) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("convocatorias").update({ activa: !activa }).eq("id", id);
  revalidatePath("/admin/convocatorias");
  revalidatePath("/");
}

export async function eliminarConvocatoria(id: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("convocatorias").delete().eq("id", id);
  revalidatePath("/admin/convocatorias");
  revalidatePath("/");
}
