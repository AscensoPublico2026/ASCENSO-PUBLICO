"use server";

import { redirect } from "next/navigation";
import { analyticsEventKey, trackServerEvent } from "@/lib/analytics-server";
import { createAdminClient } from "@/lib/supabase/server";
import { generarReferencia, firmaIntegridad, urlCheckout } from "@/lib/wompi";
import { encryptCedula, isValidCedula, normalizeCedula } from "@/lib/cedula";
import { toTitleCase } from "@/lib/format";

// Server Action: recibe el formulario de compra, normaliza los textos,
// valida la contraseña, sube el PDF, guarda el pre-registro, crea el pago pendiente y redirige al checkout de Wompi.
export async function crearCompra(formData: FormData) {
  // Campos obligatorios con normalización Title Case
  const nombres = toTitleCase(String(formData.get("nombres") || "").trim());
  const apellidos = toTitleCase(String(formData.get("apellidos") || "").trim());
  const nombre = `${nombres} ${apellidos}`.trim(); // nombre completo normalizado
  const correo = String(formData.get("correo") || "").trim().toLowerCase();
  const celular = String(formData.get("celular") || "").trim();
  const cedulaInput = String(formData.get("cedula") || "").trim();
  const cedula = normalizeCedula(cedulaInput);
  const convocatoria_id = String(formData.get("convocatoria_id") || "").trim() || null;
  const opec = String(formData.get("opec") || "").trim();
  const cargo = toTitleCase(String(formData.get("cargo") || "").trim()); // Normalizado
  const nivel = String(formData.get("nivel") || "").trim();
  const consentimiento = formData.get("consentimiento") === "on";
  const manual = formData.get("manual") as File | null;
  
  // Contraseña (nuevo campo obligatorio)
  const password = String(formData.get("password") || "").trim();
  const confirmPassword = String(formData.get("confirmPassword") || "").trim();

  if (!nombres || !apellidos || !correo || !cedula || !consentimiento) {
    throw new Error("Faltan datos obligatorios o no aceptaste el tratamiento de datos.");
  }

  if (!/^[0-9.\s-]+$/.test(cedulaInput) || cedulaInput.length > 20 || !isValidCedula(cedula)) {
    throw new Error("Ingresa un número de cédula válido, de 5 a 12 dígitos.");
  }
  const cedulaEncrypted = encryptCedula(cedula);
  const cedulaLast4 = cedula.slice(-4);

  // Validar contraseña
  if (!password || password.length < 6) {
    throw new Error("La contraseña debe tener al menos 6 caracteres.");
  }

  if (password !== confirmPassword) {
    throw new Error("Las contraseñas no coinciden.");
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

  // Guardar pre-registro con nombres normalizados Y la contraseña
  const { error: insErr } = await supabase.from("preregistros").insert({
    referencia, nombre, correo, celular,
    cedula_encrypted: cedulaEncrypted,
    cedula_last4: cedulaLast4,
    convocatoria_id, opec, cargo_nombre: cargo, nivel, manual_pdf_path, consentimiento,
    password, // ← contraseña elegida por el cliente ANTES del pago
  });
  if (insErr) {
    // Evita dejar manuales huérfanos si falta la migración o falla el preregistro.
    if (manual_pdf_path) {
      await supabase.storage.from("manuales").remove([manual_pdf_path]);
    }
    throw new Error("No se pudo guardar el registro: " + insErr.message);
  }

  // Pago pendiente + firma + redirección a Wompi
  const monto = Number(process.env.PRECIO_COP || "300000") * 100; // a centavos
  const { error: pagoError } = await supabase
    .from("pagos")
    .insert({ referencia, monto, estado: "pendiente" });
  if (pagoError) throw new Error("No se pudo iniciar el pago: " + pagoError.message);

  await trackServerEvent("checkout_started", {
    level: nivel,
    convocatoria_id: convocatoria_id || "",
    value: monto / 100,
    currency: "COP",
  }, { eventKey: analyticsEventKey("checkout", referencia) });

  const signature = firmaIntegridad(referencia, monto, "COP");
  const url = urlCheckout({ reference: referencia, amountInCents: monto, signature });
  redirect(url);
}
