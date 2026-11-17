import type { Metadata } from "next";
import Link from "next/link";
import NavLanding from "../../components/NavLanding";
import { getTransaction } from "@/lib/wompiApi";
import { procesarCompraSimulacro } from "@/lib/procesarSimulacro";
import { createAdminClient } from "@/lib/supabase/server";
import { waUrl, WA_MENSAJES, CORREO_CONTACTO } from "@/lib/contacto";
import { SITE_URL } from "@/lib/site";
import "../../landing.css";
import "../simulacro-completo.css";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Tu simulacro completo",
  robots: { index: false, follow: false },
};

type Props = { searchParams: { id?: string; intento?: string } };

export default async function GraciasPage({ searchParams }: Props) {
  const id = searchParams.id;
  const intento = Number(searchParams.intento || 0);
  const wa = waUrl(WA_MENSAJES.simulacroPago);

  if (!id) {
    return (
      <Marco>
        <span className="simc-ic">🤔</span>
        <h1>No encontramos la transacción</h1>
        <p>
          Si acabas de pagar, revisa tu correo: ahí te llega el enlace de acceso. Si no te llegó, escríbenos y te
          lo reenviamos.
        </p>
        <Ayuda wa={wa} />
      </Marco>
    );
  }

  const tx = await getTransaction(id);
  const estado: string = tx?.status || "DESCONOCIDO";
  const referencia: string = tx?.reference || "";

  // Pago aprobado: marcamos la compra (idempotente) y entregamos el enlace.
  if (estado === "APPROVED" && referencia.startsWith("SIM-")) {
    const compra = await procesarCompraSimulacro(referencia, tx.id, tx?.payment_method_type);
    if (compra?.token) {
      const url = `${SITE_URL}/simulacro-completo/${compra.token}`;
      return (
        <Marco>
          <span className="simc-ic">✅</span>
          <h1>¡Listo, {primerNombre(compra.nombre)}! Tu pago fue aprobado</h1>
          <p>
            Este es tu acceso al <strong>{compra.producto_nombre}</strong>. También te lo enviamos a{" "}
            <strong>{compra.correo}</strong>, así que puedes cerrar esta página sin perderlo.
          </p>
          <code className="simc-enlace">{url}</code>
          <Link href={`/simulacro-completo/${compra.token}`} className="btn btn-oro" style={{ width: "100%", padding: 15 }}>
            Presentar mi simulacro ahora
          </Link>
          <p style={{ marginTop: 16, fontSize: ".85rem" }}>
            Tienes 2 intentos durante 30 días. Preséntalo de una sola sentada, con tiempo y sin interrupciones.
          </p>
          <Ayuda wa={wa} />
        </Marco>
      );
    }
  }

  // PSE puede quedar en trámite varios minutos: refrescamos solos.
  if (estado === "PENDING") {
    return (
      <Marco refrescarA={intento < 40 ? `/simulacro-completo/gracias?id=${encodeURIComponent(id)}&intento=${intento + 1}` : undefined}>
        <span className="simc-ic">⏳</span>
        <h1>Estamos confirmando tu pago</h1>
        <p>
          Los pagos por PSE pueden tardar unos minutos en confirmarse. Deja esta página abierta: se actualiza
          sola. Apenas el banco confirme, te mostramos el enlace y te lo enviamos al correo.
        </p>
        <p style={{ fontSize: ".85rem" }}>
          Si cierras la página no pasa nada: <strong>el enlace igual te llega al correo</strong>.
        </p>
        <Ayuda wa={wa} />
      </Marco>
    );
  }

  if (estado === "DECLINED" || estado === "ERROR" || estado === "VOIDED") {
    await marcarRechazada(referencia);
    return (
      <Marco>
        <span className="simc-ic">⚠️</span>
        <h1>El pago no se completó</h1>
        <p>
          Tu banco no aprobó la transacción, así que <strong>no se te cobró nada</strong>. Puedes intentarlo de
          nuevo con otro medio de pago o coordinarlo con nosotros por WhatsApp.
        </p>
        <Link href="/simulacro-completo#comprar" className="btn btn-oro" style={{ width: "100%", padding: 15 }}>
          Intentar de nuevo
        </Link>
        <Ayuda wa={wa} />
      </Marco>
    );
  }

  return (
    <Marco>
      <span className="simc-ic">🔎</span>
      <h1>No pudimos leer el estado del pago</h1>
      <p>
        Si el cobro se hizo, el enlace te llega igual al correo apenas lo confirmemos. Escríbenos con tu nombre y
        te lo verificamos de una vez.
      </p>
      <Ayuda wa={wa} />
    </Marco>
  );
}

function primerNombre(n?: string) {
  return (n || "").trim().split(/\s+/)[0] || "";
}

async function marcarRechazada(referencia: string) {
  if (!referencia.startsWith("SIM-")) return;
  try {
    const supabase = createAdminClient();
    await supabase
      .from("compras_simulacro")
      .update({ estado: "rechazado" })
      .eq("referencia", referencia)
      .eq("estado", "pendiente");
  } catch {
    /* no bloquea la vista */
  }
}

function Ayuda({ wa }: { wa: string }) {
  return (
    <p style={{ marginTop: 18, fontSize: ".86rem" }}>
      ¿Necesitas ayuda?{" "}
      <a href={wa} target="_blank" rel="noopener" style={{ color: "var(--verde)", fontWeight: 700 }}>
        Escríbenos por WhatsApp
      </a>{" "}
      o a <a href={`mailto:${CORREO_CONTACTO}`}>{CORREO_CONTACTO}</a>.
    </p>
  );
}

function Marco({ children, refrescarA }: { children: React.ReactNode; refrescarA?: string }) {
  return (
    <>
      {refrescarA && <meta httpEquiv="refresh" content={`6;url=${refrescarA}`} />}
      <NavLanding />
      <section className="sec sec-alt" style={{ minHeight: "70vh" }}>
        <div className="wrap">
          <div className="simc-estado">{children}</div>
        </div>
      </section>
    </>
  );
}
