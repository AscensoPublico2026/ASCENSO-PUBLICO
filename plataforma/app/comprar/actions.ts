"use server";

import { redirect } from "next/navigation";
import { createAdminClient } from "@/lib/supabase/server";
import { generarReferencia, firmaIntegridad, urlCheckout } from "@/lib/wompi";

// Server Action: recibe el formulario de compra, sube el PDF, guarda el
// pre-registro, crea el pago pendiente y redirige al checkout de Wompi.
export async function crearCompra(formData: FormData) {
  const nombre = String(formData.get("nombre") || "").trim();
  const correo = String(formData.get("correo") || "").trim();
  const celular = String(formData.get("celular") || "").trim();
  const convocatoria_id = String(formData.get("convocatoria_id") || "").trim() || null;
  const opec = String(formData.get("opec") || "").trim();
  const cargo = String(formData.get("cargo") || "").trim();
  const nivel = String(formData.get("nivel") || "").trim();
  const consentimiento = formData.get("consentimiento") === "on";
  const manual = formData.get("manual") as File | null;

  if (!nombre || !correo || !consentimiento) {
    throw new Error("Faltan datos obligatorios o no aceptaste el tratamiento de datos.");
  }

  const supabase = createAdminClient();
  const referencia = generarReferencia();

  // Subir el manual de funciones (PDF) a Storage privado
  let manual_pdf_path: string | null = null;
  if (manual && manual.size > 0) {
    const ext = (manual.name.split(".").pop() || "pdf").toLowerCase();
    manual_pdf_path = `${referencia}.${ext}`;
    const bytes = Buffer.from(await manual.arrayBuffer());
    const { error: upErr } = await supabase.storage
      .from("manuales")
      .upload(manual_pdf_path, bytes, { contentType: manual.type || "application/pdf", upsert: true });
    if (upErr) throw new Error("No se pudo subir el manual: " + upErr.message);
  }

  // Guardar pre-registro (los datos quedan listos para crear el perfil cuando el pago se confirme)
  const { error: insErr } = await supabase.from("preregistros").insert({
    referencia, nombre, correo, celular, convocatoria_id,
    opec, cargo_nombre: cargo, nivel, manual_pdf_path, consentimiento,
  });
  if (insErr) throw new Error("No se pudo guardar el registro: " + insErr.message);

  // Pago pendiente + firma + redirección a Wompi
  const monto = Number(process.env.PRECIO_COP || "300000") * 100; // a centavos
  await supabase.from("pagos").insert({ referencia, monto, estado: "pendiente" });

  const signature = firmaIntegridad(referencia, monto, "COP");
  const url = urlCheckout({ reference: referencia, amountInCents: monto, signature });
  redirect(url);
}
