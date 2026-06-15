import { NextRequest, NextResponse } from "next/server";

/**
 * DEBUG: Consulta una transacción de Wompi directamente.
 * Uso: /api/admin/debug-tx?id=12116952-1781566986-41494
 * 
 * Esto permite ver exactamente qué responde la API de Wompi
 * para diagnosticar por qué /activar no la encuentra.
 * 
 * ELIMINAR DESPUÉS DE DEBUGGEAR.
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
    const body = await res.text();

    return NextResponse.json({
      wompi_url: url,
      http_status: status,
      response: body ? JSON.parse(body) : null,
      env_check: {
        has_private_key: !!process.env.WOMPI_PRIVATE_KEY,
        public_key_prefix: pub.substring(0, 12) + "...",
        base_url: base,
      },
    });
  } catch (e: any) {
    return NextResponse.json({ error: e.message, wompi_url: url });
  }
}
