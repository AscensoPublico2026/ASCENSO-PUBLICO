import { getTransaction } from "@/lib/wompiApi";
import { procesarReferencia } from "@/lib/procesarPago";
import ActivarForm from "./ActivarForm";

export const dynamic = "force-dynamic";

// Wompi redirige aquí tras el pago (redirect-url), añadiendo ?id=<transaction_id>.
export default async function ActivarPage({ searchParams }: { searchParams: { id?: string; ref?: string } }) {
  const id = searchParams?.id;
  let referencia = searchParams?.ref || "";
  let aprobado = false;
  let email = "";

  if (id) {
    const tx = await getTransaction(id);
    if (tx) {
      referencia = tx.reference;
      aprobado = tx.status === "APPROVED";
    }
  }

  if (aprobado && referencia) {
    try {
      const r = await procesarReferencia(referencia, id);
      if (r) email = r.email;
    } catch {
      /* se reintenta al recargar */
    }
  }

  if (!aprobado) {
    return (
      <main style={{ maxWidth: 560, margin: "0 auto", padding: "70px 22px", textAlign: "center" }}>
        <h1 style={{ fontSize: "1.6rem" }}>Estamos confirmando tu pago…</h1>
        <p style={{ color: "var(--texto-suave)", marginTop: 12 }}>
          Si acabas de pagar, espera unos segundos y recarga esta página. Si el problema persiste,
          escríbenos por WhatsApp y lo resolvemos.
        </p>
      </main>
    );
  }

  return <ActivarForm referencia={referencia} email={email} />;
}
