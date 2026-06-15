import crypto from "crypto";

// Genera una referencia única para la transacción.
export function generarReferencia(prefix = "AP"): string {
  const rand = crypto.randomBytes(6).toString("hex");
  return `${prefix}-${Date.now()}-${rand}`;
}

// Firma de integridad de Wompi: SHA256( reference + amountInCents + currency + secret ).
export function firmaIntegridad(reference: string, amountInCents: number, currency = "COP"): string {
  const secret = process.env.WOMPI_INTEGRITY_SECRET || "";
  const cadena = `${reference}${amountInCents}${currency}${secret}`;
  return crypto.createHash("sha256").update(cadena).digest("hex");
}

// Construye la URL del Web Checkout de Wompi.
// Nota: la llave "signature:integrity" debe quedar literal (no URL-encoded).
export function urlCheckout(opts: { reference: string; amountInCents: number; currency?: string; signature: string }): string {
  const currency = opts.currency ?? "COP";
  const redirect = process.env.NEXT_PUBLIC_WOMPI_REDIRECT_URL
    || `${process.env.NEXT_PUBLIC_SITE_URL || ""}/preparacion`;
  const q = [
    `public-key=${encodeURIComponent(process.env.NEXT_PUBLIC_WOMPI_PUBLIC_KEY || "")}`,
    `currency=${currency}`,
    `amount-in-cents=${opts.amountInCents}`,
    `reference=${encodeURIComponent(opts.reference)}`,
    `signature:integrity=${opts.signature}`,
    `redirect-url=${encodeURIComponent(redirect)}`,
  ].join("&");
  return `https://checkout.wompi.co/p/?${q}`;
}
