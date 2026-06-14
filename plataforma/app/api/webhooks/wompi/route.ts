import { NextRequest, NextResponse } from "next/server";
import { verificarEvento } from "@/lib/wompiApi";
import { procesarReferencia } from "@/lib/procesarPago";

// Webhook de Wompi. Configúralo en el dashboard de Wompi apuntando a:
//   https://TU-DOMINIO/api/webhooks/wompi
export async function POST(req: NextRequest) {
  const event = await req.json().catch(() => null);
  if (!event) return NextResponse.json({ ok: false }, { status: 400 });

  if (!verificarEvento(event)) {
    return NextResponse.json({ ok: false, error: "firma inválida" }, { status: 401 });
  }

  const tx = event?.data?.transaction;
  if (event?.event === "transaction.updated" && tx?.status === "APPROVED") {
    try {
      await procesarReferencia(tx.reference, tx.id);
    } catch (e) {
      // Respondemos 200 para que Wompi no reintente infinitamente; el error queda logueado.
      console.error("Error procesando pago aprobado:", e);
    }
  }
  return NextResponse.json({ ok: true });
}
