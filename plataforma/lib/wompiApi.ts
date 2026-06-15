import crypto from "crypto";

// Base de la API de Wompi según el entorno (sandbox vs producción), derivado de la llave pública.
export function wompiApiBase(): string {
  const pub = process.env.NEXT_PUBLIC_WOMPI_PUBLIC_KEY || "";
  return pub.startsWith("pub_prod")
    ? "https://production.wompi.co/v1"
    : "https://sandbox.wompi.co/v1";
}

// Consulta una transacción por id (usa la llave privada). Devuelve data o null.
export async function getTransaction(id: string): Promise<any | null> {
  try {
    const res = await fetch(`${wompiApiBase()}/transactions/${id}`, {
      headers: { Authorization: `Bearer ${process.env.WOMPI_PRIVATE_KEY || ""}` },
      cache: "no-store",
    });
    if (!res.ok) return null;
    const json = await res.json();
    return json?.data ?? null;
  } catch {
    return null;
  }
}

// Verifica la firma (checksum) de un evento de webhook de Wompi.
// checksum = SHA256( valores de signature.properties + timestamp + WOMPI_EVENTS_SECRET ).
export function verificarEvento(event: any): boolean {
  try {
    const props: string[] = event?.signature?.properties || [];
    const checksum: string = event?.signature?.checksum || "";
    const timestamp = event?.timestamp ?? "";
    const secret = process.env.WOMPI_EVENTS_SECRET || "";
    let concat = "";
    for (const path of props) {
      const val = path.split(".").reduce((acc: any, k: string) => (acc == null ? acc : acc[k]), event.data);
      concat += val ?? "";
    }
    concat += `${timestamp}${secret}`;
    const local = crypto.createHash("sha256").update(concat).digest("hex");
    return local.toLowerCase() === String(checksum).toLowerCase();
  } catch {
    return false;
  }
}
