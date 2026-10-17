"use server";

import { redirect } from "next/navigation";
import { analyticsEventKey, trackServerEvent } from "@/lib/analytics-server";
import { createAdminClient } from "@/lib/supabase/server";
import { generarReferencia, firmaIntegridad, urlCheckout } from "@/lib/wompi";
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
  const convocatoria_id = String(formData.get("convocatoria_id") || "").trim() || null;
  const opec = String(formData.get("opec") || "").trim();
  const cargo = toTitleCase(String(formData.get("cargo") || "").trim()); // Normalizado
  const nivel = String(formData.get("nivel") || "").trim();
  const consentimiento = formData.get("consentimiento") === "on";
  const manual = formData.get("manual") as File | null;
  
  // Contraseña (nuevo campo obligatorio)
  const password = String(formData.get("password") || "").trim();
  const confirmPassword = String(formData.get("confirmPassword") || "").trim();

  // URL de destino (checkout de Wompi). Se calcula dentro del try y la
  // redirección real se hace al final, fuera del try, para no capturar el
  // NEXT_REDIRECT interno de Next.js.
  let url: string;

  try {
    if (!nombres || !apellidos || !correo || !consentimiento) {
      throw new Error("Faltan datos obligatorios o no aceptaste el tratamiento de datos.");
    }

    // Validar contraseña
    if (!password || password.length < 6) {
      throw new Error("La contraseña debe tener al menos 6 caracteres.");
    }

    if (password !== confirmPassword) {
      throw new Error("Las contraseñas no coinciden.");
    }

    if (!convocatoria_id) {
      throw new Error("Selecciona una convocatoria.");
    }

    // Verificación explícita de configuración del servidor: si faltan las
    // variables de entorno, damos un mensaje claro en vez de un error críptico.
    if (!process.env.NEXT_PUBLIC_SUPABASE_URL || !process.env.SUPABASE_SERVICE_ROLE_KEY) {
      throw new Error("Configuración del servidor incompleta (Supabase). Contacta al administrador.");
    }

    const supabase = createAdminClient();
    const referencia = generarReferencia();

    // Precio según la convocatoria (fuente de verdad en el servidor; no se
    // confía en ningún valor enviado por el cliente). Cada convocatoria define
    // su propio precio_cop (ej. DIAN/CNSC 200.000, Procuraduría 300.000).
    const { data: conv, error: convErr } = await supabase
      .from("convocatorias")
      .select("precio_cop")
      .eq("id", convocatoria_id)
      .single();
    if (convErr || !conv) {
      throw new Error("La convocatoria seleccionada no es válida.");
    }
    const precioCop = Number(conv.precio_cop);
    if (!Number.isFinite(precioCop) || precioCop < 1000) {
      throw new Error("La convocatoria no tiene un precio válido configurado.");
    }

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
    // El monto sale del precio de la convocatoria, convertido a centavos.
    const monto = Math.round(precioCop * 100); // a centavos
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
    url = urlCheckout({ reference: referencia, amountInCents: monto, signature });
  } catch (e) {
    // En vez de romper con la pantalla genérica "server-side exception",
    // devolvemos al usuario al formulario mostrando el motivo real.
    const msg = e instanceof Error ? e.message : "Ocurrió un error inesperado. Inténtalo de nuevo.";
    console.error("[crearCompra] Error:", msg);
    redirect(`/comprar?error=${encodeURIComponent(msg)}`);
  }

  // Redirección al checkout (fuera del try para no capturar el NEXT_REDIRECT).
  redirect(url);
}
