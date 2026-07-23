import crypto from "crypto";
import { analyticsEventKey, trackServerEvent } from "@/lib/analytics-server";
import { createAdminClient } from "@/lib/supabase/server";
import { correoConfirmacionCliente, correoAvisoAdmin } from "@/lib/email";
import { cargarGuiasAutomaticas } from "@/lib/autocargarGuias";


// IDEMPOTENTE: dada una referencia con pago aprobado, asegura que existan el
// usuario (Auth) y su curso (estado en_preparacion, deadline +24h). La pueden
// llamar tanto el webhook como la página /activar sin duplicar nada.
export async function procesarReferencia(referencia: string, transactionId?: string) {
  const supabase = createAdminClient();

  const { data: pre } = await supabase.from("preregistros").select("*").eq("referencia", referencia).single();
  if (!pre) return null;

  // ¿Ya estaba procesado? (pago con usuario y curso asignados)
  const { data: pago } = await supabase.from("pagos").select("*").eq("referencia", referencia).single();
  if (pago?.usuario_id && pago?.curso_id) {
    await trackServerEvent("purchase_completed", {
      level: pre.nivel || "",
      convocatoria_id: pre.convocatoria_id || "",
      value: Number(pago.monto || 0) / 100,
      currency: "COP",
    }, { eventKey: analyticsEventKey("purchase", referencia) });
    return { userId: pago.usuario_id, cursoId: pago.curso_id, email: pre.correo, yaProcesado: true };
  }

  // ---- Crear o recuperar el usuario de Auth (robusto ante usuarios residuales) ----
  let userId: string | null = null;

  // 1. Buscar si el correo YA existe en Auth (evita el error "email already exists")
  const { data: list } = await supabase.auth.admin.listUsers();
  const existente = list?.users?.find(
    (u: any) => (u.email || "").toLowerCase() === (pre.correo || "").toLowerCase()
  );

  if (existente) {
    userId = existente.id;
    // Si el usuario ya existe, actualizar su contraseña con la nueva del preregistro
    if (pre.password) {
      await supabase.auth.admin.updateUserById(existente.id, { password: pre.password });
    }
  } else {
    // 2. No existe → crear nuevo con la contraseña que el cliente eligió en /comprar
    const userPassword = pre.password || crypto.randomUUID(); // fallback por si el campo no existe aún
    const { data: created, error: createErr } = await supabase.auth.admin.createUser({
      email: pre.correo,
      password: userPassword,
      email_confirm: true,
      user_metadata: { nombre: pre.nombre },
    });
    if (createErr) throw new Error("No se pudo crear el usuario: " + createErr.message);
    userId = created?.user?.id ?? null;
  }

  if (!userId) throw new Error("No se pudo crear/obtener el usuario");

  // ---- Asegurar el profile (upsert por si el trigger no corrió) ----
  await supabase.from("profiles").upsert({
    id: userId,
    nombre: pre.nombre,
    correo: pre.correo,
    celular: pre.celular,
  }, { onConflict: "id" });

  // ---- Crear el curso (solo si no existe uno para esta misma compra) ----
  let cursoId: string | null = null;

  // Verificar si ya hay un curso de esta misma compra (mismo usuario + opec) para evitar duplicados
  const { data: cursoExistente } = await supabase
    .from("cursos")
    .select("id")
    .eq("usuario_id", userId)
    .eq("opec", pre.opec)
    .maybeSingle();

  if (cursoExistente) {
    cursoId = cursoExistente.id;
  } else {
    const ahora = new Date();
    const deadline = new Date(ahora.getTime() + 24 * 3600 * 1000);
    const { data: curso } = await supabase
      .from("cursos")
      .insert({
        usuario_id: userId,
        convocatoria_id: pre.convocatoria_id,
        opec: pre.opec,
        cargo_nombre: pre.cargo_nombre,
        nivel: pre.nivel,
        manual_pdf_path: pre.manual_pdf_path,
        estado: "en_preparacion",
        fecha_compra: ahora.toISOString(),
        preparacion_deadline: deadline.toISOString(),
      })
      .select("id")
      .single();

    cursoId = curso?.id ?? null;

    // Auto-cargar guías (Intro + Generales + Nivel + Bonus) al crear el curso
    if (cursoId && pre.nivel) {
      try {
        await cargarGuiasAutomaticas(supabase, cursoId, pre.nivel);
      } catch (err) {
        console.error("[procesarReferencia] Error en auto-carga de guías:", err);
      }
    }
  }

  // ---- Actualizar el pago como aprobado ----
  await supabase
    .from("pagos")
    .update({ estado: "aprobado", usuario_id: userId, curso_id: cursoId, wompi_transaction_id: transactionId ?? null })
    .eq("referencia", referencia);

  await supabase.from("preregistros").update({ procesado: true }).eq("referencia", referencia);

  await trackServerEvent("purchase_completed", {
    level: pre.nivel || "",
    convocatoria_id: pre.convocatoria_id || "",
    value: Number(pago?.monto || 0) / 100,
    currency: "COP",
  }, {
    eventKey: analyticsEventKey("purchase", referencia),
  });

  // ---- Correos (no bloquean el flujo si fallan) ----
  try {
    await correoConfirmacionCliente(pre.correo, pre.nombre);
    await correoAvisoAdmin({
      nombre: pre.nombre,
      correo: pre.correo,
      celular: pre.celular,
      opec: pre.opec,
      cargo_nombre: pre.cargo_nombre,
      nivel: pre.nivel,
      referencia,
    });
  } catch {
    /* ignore */
  }

  return { userId, cursoId, email: pre.correo, yaProcesado: false };
}
