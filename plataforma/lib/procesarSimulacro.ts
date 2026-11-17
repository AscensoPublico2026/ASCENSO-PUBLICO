import { createAdminClient } from "@/lib/supabase/server";
import { analyticsEventKey, trackServerEvent } from "@/lib/analytics-server";
import { correoSimulacroPagoListo } from "@/lib/email";
import { SIM_DIAS_ACCESO } from "@/lib/simulacroPago";

/**
 * Marca como aprobada una compra del simulacro completo y manda el correo con
 * el enlace de acceso. Es idempotente: la llaman el webhook de Wompi y la
 * página de gracias, y solo la primera deja huella.
 */
export async function procesarCompraSimulacro(referencia: string, transactionId?: string, metodo?: string) {
  const supabase = createAdminClient();

  const { data: compra } = await supabase
    .from("compras_simulacro")
    .select("*")
    .eq("referencia", referencia)
    .maybeSingle();

  if (!compra) return null;
  if (compra.estado === "aprobado") return compra;

  const expira = new Date();
  expira.setDate(expira.getDate() + SIM_DIAS_ACCESO);

  const { data: actualizada } = await supabase
    .from("compras_simulacro")
    .update({
      estado: "aprobado",
      pagado_en: new Date().toISOString(),
      expira_en: expira.toISOString(),
      wompi_transaction_id: transactionId ?? compra.wompi_transaction_id,
      metodo_pago: metodo ?? compra.metodo_pago,
    })
    .eq("id", compra.id)
    .select("*")
    .single();

  const final = actualizada ?? compra;

  try {
    await correoSimulacroPagoListo(final.correo, final.nombre, final.token, final.producto_nombre || "Simulacro completo");
  } catch (e) {
    console.error("No se pudo enviar el correo del simulacro de pago:", e);
  }

  await trackServerEvent(
    "purchase_completed",
    {
      level: final.producto || "",
      value: Number(final.monto_centavos || 0) / 100,
      currency: "COP",
      product: "simulacro_completo",
    },
    { eventKey: analyticsEventKey("purchase", referencia) }
  );

  return final;
}
