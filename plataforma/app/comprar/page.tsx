import type { Metadata } from "next";
import Link from "next/link";
import NavLanding from "../components/NavLanding";
import ContadorCupos from "../components/ContadorCupos";
import { waUrl, WA_MENSAJES, CORREO_CONTACTO } from "@/lib/contacto";
import "../landing.css";

export const metadata: Metadata = {
  title: "Pedir mi curso personalizado",
  description:
    "Cuéntanos tu convocatoria y tu cargo por WhatsApp. Te confirmamos el precio de tu nivel, revisamos tu OPEC y armamos tu ruta de estudio en 24 horas.",
  alternates: { canonical: "/comprar" },
};

const NIVELES = [
  { nivel: "Operativo y administrativo", precio: "$190.000", cargos: "Auxiliares, citadores y oficinistas" },
  { nivel: "Técnico", precio: "$240.000", cargos: "Sustanciadores, técnicos y tecnólogos" },
  { nivel: "Profesional", precio: "$290.000", cargos: "Profesional universitario y equivalentes" },
  { nivel: "Asesor y ejecutivo", precio: "$390.000", cargos: "Asesores y cargos de dirección" },
];

const PASOS = [
  "Nos escribes con tu convocatoria y el nombre de tu cargo.",
  "Verificamos tu OPEC y el manual de funciones. Si no sabes dónde están, te enseñamos a descargarlos.",
  "Te confirmamos el precio exacto de tu nivel y te enviamos el enlace de pago seguro de Wompi.",
  "En máximo 24 horas tienes tu ruta de 21 días lista en tu perfil.",
];

export default function ComprarPage() {
  const wa = waUrl(WA_MENSAJES.precio);

  return (
    <>
      <NavLanding />

      <section className="sec sec-alt">
        <div className="wrap" style={{ maxWidth: 760 }}>
          <span className="eyebrow">Tu curso personalizado</span>
          <h1 style={{ fontFamily: "'Source Serif 4',serif", color: "var(--azul)", fontSize: "clamp(1.7rem,4vw,2.3rem)", margin: "6px 0 12px", lineHeight: 1.2 }}>
            Cuéntanos tu cargo y te armamos la ruta
          </h1>
          <p className="lead" style={{ margin: "0 0 26px" }}>
            El curso se arma con <strong>tu OPEC y tu manual de funciones</strong>, así que empieza con una
            conversación, no con un formulario. Te responde una persona.
          </p>

          <a
            href={wa}
            target="_blank"
            rel="noopener"
            className="btn btn-oro"
            data-analytics-event="whatsapp_clicked"
            data-analytics-placement="comprar_principal"
            style={{ padding: "15px 32px", fontSize: "1rem" }}
          >
            💬 Escribir por WhatsApp
          </a>

          <p style={{ fontSize: ".86rem", color: "var(--texto-suave)", marginTop: 12 }}>
            ¿Prefieres correo? <a href={`mailto:${CORREO_CONTACTO}`} style={{ color: "var(--azul)", fontWeight: 700 }}>{CORREO_CONTACTO}</a>
          </p>

          <div style={{ marginTop: 34 }}>
            <ContadorCupos />
          </div>
        </div>
      </section>

      <section className="sec">
        <div className="wrap" style={{ maxWidth: 760 }}>
          <h2 style={{ color: "var(--azul)", fontSize: "1.3rem", marginBottom: 6 }}>Precio según el nivel del empleo</h2>
          <p style={{ color: "var(--texto-suave)", fontSize: ".93rem", marginBottom: 20 }}>
            Como los derechos de participación del concurso, el valor cambia según el nivel del cargo al que
            aspiras. Pago único, sin mensualidades.
          </p>

          <div className="precio-grid">
            {NIVELES.map((n) => (
              <div key={n.nivel} className="precio-nivel">
                <span className="precio-nivel-tag">{n.nivel}</span>
                <div className="precio-nivel-num">{n.precio}</div>
                <p>{n.cargos}</p>
              </div>
            ))}
          </div>

          <h2 style={{ color: "var(--azul)", fontSize: "1.3rem", margin: "34px 0 14px" }}>Cómo funciona</h2>
          <ol style={{ paddingLeft: 20, color: "var(--texto)", lineHeight: 1.65 }}>
            {PASOS.map((p) => (
              <li key={p} style={{ marginBottom: 8 }}>{p}</li>
            ))}
          </ol>

          <div style={{ display: "flex", gap: 12, flexWrap: "wrap", marginTop: 26 }}>
            <a href={wa} target="_blank" rel="noopener" className="btn btn-oro" data-analytics-event="whatsapp_clicked" data-analytics-placement="comprar_final">
              Pedir mi curso
            </a>
            <Link href="/simulacro" className="btn btn-ghost-conv" style={{ padding: "13px 22px" }}>
              Probar un simulacro gratis
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
