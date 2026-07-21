import type { Metadata } from "next";
import Link from "next/link";
import NavLanding from "../components/NavLanding";
import BuscadorOpec from "./BuscadorOpec";
import meta from "@/data/opec-meta.json";
import { formatOpecDate } from "@/lib/opec";
import "../landing.css";
import "./buscador-opec.css";

export const metadata: Metadata = {
  title: "Buscador inteligente de convocatorias 2026 | OPEC y vacantes",
  description:
    "Consulta en un solo buscador las vacantes ESE 2, EREON 2026 y Procuraduría. Filtra por convocatoria o describe tu perfil para encontrar empleos afines.",
  keywords: [
    "buscador inteligente OPEC",
    "convocatorias empleo público 2026",
    "vacantes Procuraduría 2026",
    "EREON 2026",
    "convocatoria ESE 2026",
  ],
  alternates: { canonical: "/buscador-opec" },
  openGraph: {
    title: "Buscador inteligente de convocatorias — Ascenso Público",
    description: `Explora ${meta.totalOpec.toLocaleString("es-CO")} empleos consolidados y encuentra los que mejor se ajustan a tu perfil.`,
    url: "/buscador-opec",
    type: "website",
  },
};

const number = (value: number) => value.toLocaleString("es-CO");
const updatedDate = formatOpecDate(meta.fechaActualizacion);

export default function BuscadorOpecPage() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    name: "Buscador inteligente de convocatorias 2026",
    applicationCategory: "BusinessApplication",
    operatingSystem: "Web",
    offers: { "@type": "Offer", price: "0", priceCurrency: "COP" },
    description: metadata.description,
    provider: { "@type": "Organization", name: "Ascenso Público", url: "https://ascensopublico.com" },
  };

  return (
    <>
      <NavLanding />
      <main className="opec-page">
        <section className="opec-hero">
          <div className="opec-hero-orb opec-orb-one" aria-hidden="true" />
          <div className="opec-hero-orb opec-orb-two" aria-hidden="true" />
          <div className="wrap opec-hero-inner">
            <div className="opec-breadcrumb"><Link href="/">Inicio</Link><span>›</span><strong>Buscador OPEC</strong></div>
            <div className="opec-hero-grid">
              <div className="opec-hero-copy">
                <span className="opec-hero-tag"><i /> Herramienta gratuita · 3 convocatorias</span>
                <h1>Encuentra la vacante que <span>sí encaja contigo</span></h1>
                <p>Consulta en un solo lugar las convocatorias ESE 2, EREON 2026 y Procuraduría. Elige una convocatoria y aplica filtros, o describe tu formación y experiencia para recibir coincidencias inteligentes.</p>
                <div className="opec-hero-actions">
                  <a href="#explorar" className="btn btn-oro">Explorar vacantes <span aria-hidden="true">↓</span></a>
                  <button type="button" className="opec-hero-tip" tabIndex={-1}><span>✓</span> No necesitas registrarte</button>
                </div>
              </div>
              <div className="opec-hero-preview" aria-hidden="true">
                <div className="opec-preview-glow" />
                <div className="opec-preview-card">
                  <div className="opec-preview-search"><span>⌕</span> Enfermería sin experiencia</div>
                  <div className="opec-preview-result">
                    <div><span>Asistencial</span><b>OPEC 193509</b></div>
                    <h3>Auxiliar área salud</h3>
                    <p>E.S.E. Hospital Universitario de La Samaritana</p>
                    <div className="opec-preview-info"><span>⌖ Bogotá D.C.</span><span>$1.643.220</span></div>
                    <strong>✓ No requiere experiencia</strong>
                  </div>
                </div>
                <div className="opec-preview-badge"><b>{number(meta.sinExperiencia)}</b><span>OPEC abiertas<br/>sin experiencia</span></div>
              </div>
            </div>

            <div className="opec-stats" aria-label="Resumen del consolidado">
              <div><strong>{number(meta.totalOpec)}</strong><span>Empleos consolidados</span></div>
              <div><strong>{number(meta.totalVacantes)}</strong><span>Vacantes publicadas</span></div>
              <div><strong>{number(meta.totalConvocatorias)}</strong><span>Convocatorias integradas</span></div>
              <div><strong>{number(meta.departamentos)}</strong><span>Departamentos</span></div>
            </div>
          </div>
        </section>

        <section className="opec-explorer" id="explorar">
          <div className="wrap">
            <div className="opec-explorer-intro">
              <div>
                <span className="eyebrow">Explorador de oportunidades</span>
                <h2>Tu próxima oportunidad puede estar aquí</h2>
              </div>
              <p>Usa el cuadro inteligente para describir tu perfil o cambia a búsqueda con filtros para elegir convocatoria, ubicación, estudios, salario y experiencia.</p>
            </div>
            <BuscadorOpec />
          </div>
        </section>

        <section className="opec-guide-section">
          <div className="wrap">
            <div className="opec-guide-head">
              <span className="eyebrow c">Simple y directo</span>
              <h2>De la búsqueda a tu inscripción</h2>
              <p>Ascenso Público te ayuda a identificar oportunidades; la inscripción siempre se realiza en SIMO.</p>
            </div>
            <div className="opec-guide-grid">
              <article><span>01</span><div><h3>Elige cómo quieres buscar</h3><p>Selecciona una convocatoria y filtros, o describe tu perfil en lenguaje natural.</p></div></article>
              <article><span>02</span><div><h3>Compara las coincidencias</h3><p>Revisa convocatoria, OPEC o código, estudios, experiencia y nivel de afinidad.</p></div></article>
              <article><span>03</span><div><h3>Confirma en el canal oficial</h3><p>Copia la referencia y verifica requisitos, fechas y disponibilidad antes de inscribirte.</p></div></article>
            </div>
          </div>
        </section>

        <section className="opec-disclaimer-section">
          <div className="wrap">
            <div className="opec-disclaimer">
              <div className="opec-disclaimer-icon" aria-hidden="true">i</div>
              <div>
                <h2>Información importante</h2>
                <p>Este buscador es una herramienta informativa e independiente creada por Ascenso Público. Los requisitos mostrados provienen de los consolidados de ESE 2, EREON 2026 y Procuraduría, actualizados el <strong>{updatedDate}</strong>. La afinidad inteligente es orientativa y no reemplaza la verificación de requisitos mínimos. Antes de pagar derechos de participación, confirma la información, fechas y disponibilidad en los canales oficiales de cada convocatoria y, cuando corresponda, en <a href="https://simo.cnsc.gov.co/" target="_blank" rel="noopener noreferrer">SIMO</a>.</p>
              </div>
            </div>
          </div>
        </section>

        <section className="opec-final-cta">
          <div className="wrap opec-final-cta-inner">
            <div><span>Ya encontraste tu OPEC</span><h2>Ahora prepárate específicamente para ese cargo</h2><p>Creamos una ruta de 21 días a partir de las funciones y competencias reales de tu empleo.</p></div>
            <Link href="/comprar" className="btn btn-oro">Crear mi ruta personalizada <span aria-hidden="true">→</span></Link>
          </div>
        </section>
      </main>

      <footer className="opec-footer">
        <div className="wrap opec-footer-inner">
          <Link href="/" className="brand" aria-label="Ascenso Público - inicio">
            <span className="brand-logo">
              <svg viewBox="0 0 100 100" width="24" height="24" aria-hidden="true">
                <circle cx="26" cy="74" r="3.4" fill="#0A2A5E" opacity=".45" />
                <circle cx="34" cy="70" r="4.2" fill="#0A2A5E" opacity=".72" />
                <path d="M36 66 C48 62 58 54 72 34" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round" />
                <path d="M61 32 L75 30 L73 45" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </span>
            <span><span className="brand-name">Ascenso Público</span><small>Tu ruta hacia el empleo público</small></span>
          </Link>
          <div className="opec-footer-links"><Link href="/">Inicio</Link><Link href="/simulacro">Simulacros</Link><Link href="/comprar">Curso personalizado</Link><Link href="/privacidad">Privacidad</Link></div>
          <p>© {new Date().getFullYear()} Ascenso Público. Herramienta independiente, no afiliada a la CNSC.</p>
        </div>
      </footer>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }} />
    </>
  );
}
