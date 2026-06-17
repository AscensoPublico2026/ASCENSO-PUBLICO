import { getTransaction } from "@/lib/wompiApi";
import { procesarReferencia } from "@/lib/procesarPago";
import { createAdminClient } from "@/lib/supabase/server";
import ActivarForm from "./ActivarForm";
import { waUrl, WA_MENSAJES } from "@/lib/contacto";

export const dynamic = "force-dynamic";

// Wompi redirige aquí tras el pago (redirect-url), añadiendo ?id=<transaction_id>.
export default async function ActivarPage({ searchParams }: { searchParams: { id?: string; ref?: string } }) {
  const id = searchParams?.id;
  let referencia = searchParams?.ref || "";
  let aprobado = false;
  let email = "";

  // 1) Vía normal: preguntar el estado de la transacción a la API de Wompi.
  if (id) {
    const tx = await getTransaction(id);
    if (tx) {
      referencia = tx.reference;
      aprobado = tx.status === "APPROVED";
    }
  }

  // 2) Respaldo: si la API no confirmó (p. ej. llave privada de otro entorno),
  //    pero el WEBHOOK ya procesó el pago, lo encontramos por el id de transacción
  //    o por la referencia en nuestra tabla de pagos (ya marcado como aprobado).
  if (!aprobado) {
    try {
      const supabase = createAdminClient();
      let q = supabase.from("pagos").select("referencia").eq("estado", "aprobado");
      q = id ? q.eq("wompi_transaction_id", id) : q.eq("referencia", referencia);
      const { data: pagoOk } = await q.maybeSingle();
      if (pagoOk?.referencia) {
        referencia = pagoOk.referencia;
        aprobado = true;
      }
    } catch {
      /* ignore */
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
        {/* Auto-recarga cada 6s por si el pago aún está procesándose (ej. Nequi). */}
        <meta httpEquiv="refresh" content="6" />
        <h1 style={{ fontSize: "1.6rem" }}>Estamos confirmando tu pago…</h1>
        <p style={{ color: "var(--texto-suave)", marginTop: 12 }}>
          Si acabas de pagar, espera unos segundos (esta página se actualiza sola). Si el problema persiste,{" "}
          <a href={waUrl(WA_MENSAJES.soporte)} target="_blank" rel="noopener" style={{ color: "var(--azul)", fontWeight: 700 }}>escríbenos por WhatsApp</a> y lo resolvemos.
        </p>
      </main>
    );
  }

  return <ActivarForm referencia={referencia} email={email} />;
}
