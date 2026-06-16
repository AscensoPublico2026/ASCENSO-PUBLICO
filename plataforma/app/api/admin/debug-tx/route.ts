import { NextRequest, NextResponse } from "next/server";

/**
 * DEBUG: Simula exactamente lo que hace /activar para encontrar el error.
 * Uso: /api/admin/debug-tx?id=12116952-1781566986-41494
 */
export async function GET(req: NextRequest) {
  const id = req.nextUrl.searchParams.get("id");
  if (!id) return NextResponse.json({ error: "Falta ?id=" });

  const pub = process.env.NEXT_PUBLIC_WOMPI_PUBLIC_KEY || "";
  const base = pub.startsWith("pub_prod")
    ? "https://production.wompi.co/v1"
    : "https://sandbox.wompi.co/v1";

  const url = `${base}/transactions/${id}`;

  try {
    const res = await fetch(url, {
      headers: { Authorization: `Bearer ${process.env.WOMPI_PRIVATE_KEY || ""}` },
      cache: "no-store",
    });

    const status = res.status;
    const json = await res.json();
    
    // Esto es lo que hace getTransaction:
    const txData = json?.data ?? null;

    // Esto es lo que hace /activar:
    const reference = txData?.reference ?? "NO REFERENCE";
    const txStatus = txData?.status ?? "NO STATUS";
    const aprobado = txStatus === "APPROVED";

    return NextResponse.json({
      paso1_fetch_url: url,
      paso2_http_status: status,
      paso3_json_keys: json ? Object.keys(json) : null,
      paso4_txData_exists: !!txData,
      paso5_txData_status: txStatus,
      paso6_txData_status_type: typeof txStatus,
      paso7_txData_status_length: txStatus?.length,
      paso8_reference: reference,
      paso9_aprobado: aprobado,
      paso10_comparison: `"${txStatus}" === "APPROVED" → ${txStatus === "APPROVED"}`,
      env_check: {
        has_private_key: !!process.env.WOMPI_PRIVATE_KEY,
        public_key_prefix: pub.substring(0, 15) + "...",
        base_url: base,
      },
    });
  } catch (e: any) {
    return NextResponse.json({ error: e.message, wompi_url: url });
  }
}
