"use server";

import { createAdminClient } from "@/lib/supabase/server";

// Define la contraseña del cliente tras un pago aprobado.
export async function definirPassword(referencia: string, password: string) {
  if (!password || password.length < 6) {
    return { ok: false, error: "La contraseña debe tener al menos 6 caracteres." };
  }
  const supabase = createAdminClient();
  const { data: pago } = await supabase
    .from("pagos")
    .select("usuario_id,estado")
    .eq("referencia", referencia)
    .single();

  if (!pago || pago.estado !== "aprobado" || !pago.usuario_id) {
    return { ok: false, error: "El pago aún no está confirmado. Espera unos segundos y reintenta." };
  }

  const { error } = await supabase.auth.admin.updateUserById(pago.usuario_id, { password });
  if (error) return { ok: false, error: error.message };
  return { ok: true };
}
