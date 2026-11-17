import type { Metadata } from "next";
import Link from "next/link";
import { createAdminClient } from "@/lib/supabase/server";
import { producto } from "@/lib/simulacroPago";
import { cargarBanco, type PreguntaPublica } from "@/lib/bancoSimulacroPago";
import { waUrl, WA_MENSAJES, CORREO_CONTACTO } from "@/lib/contacto";
import ExamenPago from "./ExamenPago";
import NavLanding from "../../components/NavLanding";
import "../../landing.css";
import "../simulacro-completo.css";
import "./examen.css";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Simulacro completo",
  robots: { index: false, follow: false },
};

export default async function AccesoSimulacro({ params }: { params: { token: string } }) {
  const wa = waUrl(WA_MENSAJES.simulacroPago);
  const supabase = createAdminClient();

  const { data: compra } = await supabase
    .from("compras_simulacro")
    .select("*")
    .eq("token", params.token)
    .maybeSingle();

  if (!compra) {
    return (
      <Aviso ic="🔑" titulo="Este enlace no es válido">
        <p>
          Puede que esté incompleto o que se haya copiado mal. Busca el correo que te enviamos al comprar: ahí
          está el enlace original.
        </p>
        <Ayuda wa={wa} />
      </Aviso>
    );
  }

  if (compra.estado !== "aprobado") {
    return (
      <Aviso ic="⏳" titulo="Tu pago todavía no se confirma">
        <p>
          Apenas el banco confirme la transacción, este mismo enlace se activa. Si ya te hicieron el cobro,
          escríbenos y lo verificamos de una vez.
        </p>
        <Ayuda wa={wa} />
      </Aviso>
    );
  }

  if (compra.expira_en && new Date(compra.expira_en) < new Date()) {
    return (
      <Aviso ic="📅" titulo="Tu acceso venció">
        <p>
          Este simulacro estuvo disponible 30 días. Si necesitas presentarlo otra vez, escríbenos: te lo
          reactivamos.
        </p>
        <Ayuda wa={wa} />
      </Aviso>
    );
  }

  if ((compra.intentos_usados ?? 0) >= (compra.max_intentos ?? 2)) {
    return (
      <Aviso ic="✅" titulo="Ya usaste tus intentos">
        <p>
          Presentaste este simulacro {compra.intentos_usados} veces
          {compra.ultimo_puntaje != null ? `, y tu último puntaje fue ${Math.round(Number(compra.ultimo_puntaje))}%` : ""}.
          Si quieres un intento adicional o prefieres pasar al curso completo, escríbenos.
        </p>
        <Link href="/" className="btn btn-oro" style={{ width: "100%", padding: 14 }}>
          Ver el curso personalizado
        </Link>
        <Ayuda wa={wa} />
      </Aviso>
    );
  }

  const prod = producto(compra.producto);
  const banco = await cargarBanco(compra.producto);

  if (!banco || banco.length === 0) {
    return (
      <Aviso ic="🛠️" titulo="Estamos terminando este simulacro">
        <p>
          Tu acceso quedó registrado, pero el banco de preguntas de tu convocatoria todavía no está publicado.
          Escríbenos y te avisamos apenas esté (o te devolvemos el pago, lo que prefieras).
        </p>
        <Ayuda wa={wa} />
      </Aviso>
    );
  }

  // Al cliente no le mandamos ni la respuesta correcta ni las explicaciones:
  // la calificación se hace en el servidor cuando presenta el examen.
  const publicas: PreguntaPublica[] = banco.map((p, i) => ({
    i,
    tema: p.tema,
    refT: p.refT,
    nivel: p.nivel,
    ctx: p.ctx,
    q: p.q,
    ops: p.ops,
  }));

  return (
    <ExamenPago
      token={params.token}
      nombre={(compra.nombre || "").trim().split(/\s+/)[0] || ""}
      titulo={prod?.nombre || compra.producto_nombre || "Simulacro completo"}
      convocatoria={prod?.convocatoria || ""}
      nivel={prod?.nivel || ""}
      minutos={prod?.minutos || 150}
      intentoNumero={(compra.intentos_usados ?? 0) + 1}
      maxIntentos={compra.max_intentos ?? 2}
      preguntas={publicas}
    />
  );
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

function Aviso({ ic, titulo, children }: { ic: string; titulo: string; children: React.ReactNode }) {
  return (
    <>
      <NavLanding />
      <section className="sec sec-alt" style={{ minHeight: "70vh" }}>
        <div className="wrap">
          <div className="simc-estado">
            <span className="simc-ic">{ic}</span>
            <h1>{titulo}</h1>
            {children}
          </div>
        </div>
      </section>
    </>
  );
}
