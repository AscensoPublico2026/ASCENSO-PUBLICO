"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";

export async function crearConvocatoria(formData: FormData) {
  await requireAdmin();
  const supabase = createAdminClient();

  // Imagen: 3 opciones (en orden de prioridad)
  //  1) archivo subido  → se guarda en el bucket público "imagenes"
  //  2) URL escrita      → se usa tal cual
  //  3) imagen existente → una de /public/fotos elegida del desplegable
  let imagenUrl = String(formData.get("imagen_url") || "").trim() || null;
  const imagenExistente = String(formData.get("imagen_existente") || "").trim();
  const archivo = formData.get("imagen_file") as File | null;

  if (archivo && archivo.size > 0) {
    const ext = (archivo.name.split(".").pop() || "jpg").toLowerCase();
    const path = `convocatorias/${Date.now()}.${ext}`.replace(/\s+/g, "_");
    const bytes = Buffer.from(await archivo.arrayBuffer());
    const { error } = await supabase.storage.from("imagenes").upload(path, bytes, {
      contentType: archivo.type || "image/jpeg",
      upsert: true,
    });
    if (!error) {
      const { data } = supabase.storage.from("imagenes").getPublicUrl(path);
      imagenUrl = data?.publicUrl || imagenUrl;
    } else {
      console.error("[crearConvocatoria] No se pudo subir la imagen:", error.message);
    }
  } else if (!imagenUrl && imagenExistente) {
    imagenUrl = imagenExistente;
  }

  await supabase.from("convocatorias").insert({
    nombre: String(formData.get("nombre") || "").trim(),
    entidad: String(formData.get("entidad") || "").trim() || null,
    estado: String(formData.get("estado") || "proxima"),
    etiqueta: String(formData.get("etiqueta") || "").trim() || null,
    vacantes: String(formData.get("vacantes") || "").trim() || null,
    fecha_prueba_aprox: String(formData.get("fecha_prueba_aprox") || "").trim() || null,
    imagen_url: imagenUrl,
    tema: String(formData.get("tema") || "nacional"),
    orden: Number(formData.get("orden") || 0) || 0,
    activa: true,
  });
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

export async function editarConvocatoria(id: string, formData: FormData) {
  await requireAdmin();
  const supabase = createAdminClient();

  // Imagen: misma lógica que al crear (3 opciones en orden de prioridad)
  let imagenUrl = String(formData.get("imagen_url") || "").trim() || null;
  const imagenExistente = String(formData.get("imagen_existente") || "").trim();
  const archivo = formData.get("imagen_file") as File | null;
  const imagenActual = String(formData.get("imagen_actual") || "").trim() || null;

  if (archivo && archivo.size > 0) {
    const ext = (archivo.name.split(".").pop() || "jpg").toLowerCase();
    const path = `convocatorias/${Date.now()}.${ext}`.replace(/\s+/g, "_");
    const bytes = Buffer.from(await archivo.arrayBuffer());
    const { error } = await supabase.storage.from("imagenes").upload(path, bytes, {
      contentType: archivo.type || "image/jpeg",
      upsert: true,
    });
    if (!error) {
      const { data } = supabase.storage.from("imagenes").getPublicUrl(path);
      imagenUrl = data?.publicUrl || imagenUrl;
    } else {
      console.error("[editarConvocatoria] No se pudo subir la imagen:", error.message);
    }
  } else if (!imagenUrl && imagenExistente) {
    imagenUrl = imagenExistente;
  } else if (!imagenUrl) {
    // Mantener la imagen actual si no se eligió ninguna nueva
    imagenUrl = imagenActual;
  }

  await supabase.from("convocatorias").update({
    nombre: String(formData.get("nombre") || "").trim(),
    entidad: String(formData.get("entidad") || "").trim() || null,
    estado: String(formData.get("estado") || "proxima"),
    etiqueta: String(formData.get("etiqueta") || "").trim() || null,
    vacantes: String(formData.get("vacantes") || "").trim() || null,
    fecha_prueba_aprox: String(formData.get("fecha_prueba_aprox") || "").trim() || null,
    imagen_url: imagenUrl,
    tema: String(formData.get("tema") || "nacional"),
    orden: Number(formData.get("orden") || 0) || 0,
  }).eq("id", id);

  revalidatePath("/admin/convocatorias");
  revalidatePath("/");
}
