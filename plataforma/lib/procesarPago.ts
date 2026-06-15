import crypto from "crypto";
import { createAdminClient } from "@/lib/supabase/server";
import { correoConfirmacionCliente, correoAvisoAdmin } from "@/lib/email";

const VIGENCIA_DIAS = 90; // acceso al curso (ARQUITECTURA §17: 60–90 días)

// IDEMPOTENTE: dada una referencia con pago aprobado, asegura que existan el
// usuario (Auth) y su curso (estado en_preparacion, deadline +12h). La pueden
// llamar tanto el webhook como la página /activar sin duplicar nada.
export async function procesarReferencia(referencia: string, transactionId?: string) {
  const supabase = createAdminClient();

  const { data: pre } = await supabase.from("preregistros").select("*").eq("referencia", referencia).single();
  if (!pre) return null;

  // ¿Ya estaba procesado?
  const { data: pago } = await supabase.from("pagos").select("*").eq("referencia", referencia).single();
  if (pago?.usuario_id && pago?.curso_id) {
    return { userId: pago.usuario_id, cursoId: pago.curso_id, email: pre.correo, yaProcesado: true };
  }

  // Crear o recuperar el usuario de Auth
  let userId: string | null = null;
  const tempPassword = crypto.randomUUID(); // temporal; el cliente define la suya en /activar
  const { data: created } = await supabase.auth.admin.createUser({
    email: pre.correo,
    password: tempPassword,
    email_confirm: true,
    user_metadata: { nombre: pre.nombre },
  });
  if (created?.user) {
    userId = created.user.id;
  } else {
    const { data: list } = await supabase.auth.admin.listUsers();
    const found = list?.users?.find((u: any) => (u.email || "").toLowerCase() === (pre.correo || "").toLowerCase());
    userId = found?.id ?? null;
  }
  if (!userId) throw new Error("No se pudo crear/obtener el usuario");

  // Completar el profile
  await supabase.from("profiles").update({ celular: pre.celular, nombre: pre.nombre }).eq("id", userId);

  // Crear el curso
  const ahora = new Date();
  const deadline = new Date(ahora.getTime() + 12 * 3600 * 1000);
  const vence = new Date(ahora.getTime() + VIGENCIA_DIAS * 86400 * 1000);
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
      fecha_vencimiento: vence.toISOString(),
    })
    .select("id")
    .single();

  const cursoId = curso?.id ?? null;

  await supabase
    .from("pagos")
    .update({ estado: "aprobado", usuario_id: userId, curso_id: cursoId, wompi_transaction_id: transactionId ?? null })
    .eq("referencia", referencia);

  await supabase.from("preregistros").update({ procesado: true }).eq("referencia", referencia);

  // Correos (no bloquean el flujo si fallan)
  try {
    await correoConfirmacionCliente(pre.correo, pre.nombre);
    await correoAvisoAdmin({ ...pre, referencia });
  } catch {
    /* ignore */
  }

  return { userId, cursoId, email: pre.correo, yaProcesado: false };
}
