import type { Metadata } from "next";
import Link from "next/link";
import NavLanding from "../components/NavLanding";
import BuscadorOpec from "./BuscadorOpec";
import meta from "@/data/opec-meta.json";
import { formatOpecDate } from "@/lib/opec";
import "../landing.css";
import "./buscador-opec.css";

export const metadata: Metadata = {
  title: "Buscador OPEC ESE 2026 | Vacantes por salario y experiencia",
  description:
    "Encuentra tu vacante en la convocatoria Empresas Sociales del Estado 2026. Filtra OPEC por departamento, municipio, nivel, salario y experiencia.",
  keywords: [
    "buscador OPEC ESE 2026",
    "vacantes Empresas Sociales del Estado",
    "empleos CNSC sin experiencia",
    "oferta pública SIMO",
    "convocatoria ESE 2026",
  ],
  alternates: { canonical: "/buscador-opec" },
  openGraph: {
    title: "Buscador OPEC ESE 2026 — Ascenso Público",
    description: `Explora ${meta.totalOpec.toLocaleString("es-CO")} OPEC y encuentra la vacante que mejor se ajusta a tu perfil.`,
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
    name: "Buscador OPEC ESE 2026",
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
                <span className="opec-hero-tag"><i /> Herramienta gratuita · ESE 2026</span>
                <h1>Encuentra la OPEC que <span>sí encaja contigo</span></h1>
                <p>Compara las vacantes de Empresas Sociales del Estado en un solo lugar. Filtra por ubicación, estudios, salario y experiencia para descubrir dónde tienes una oportunidad real.</p>
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
              <div><strong>{number(meta.totalOpec)}</strong><span>OPEC consolidadas</span></div>
              <div><strong>{number(meta.totalVacantes)}</strong><span>Vacantes disponibles</span></div>
              <div><strong>{number(meta.entidades)}</strong><span>Entidades E.S.E.</span></div>
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
              <p>Escribe una profesión, cargo, ciudad, entidad o número de OPEC. Puedes combinar todos los filtros.</p>
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
              <article><span>01</span><div><h3>Filtra según tu perfil</h3><p>Combina ubicación, nivel, salario, estudios y experiencia.</p></div></article>
              <article><span>02</span><div><h3>Revisa los requisitos</h3><p>Abre la ficha y confirma que tus estudios y experiencia coincidan.</p></div></article>
              <article><span>03</span><div><h3>Copia la OPEC y ve a SIMO</h3><p>Busca el número en la plataforma oficial y completa allí tu inscripción.</p></div></article>
            </div>
          </div>
        </section>

        <section className="opec-disclaimer-section">
          <div className="wrap">
            <div className="opec-disclaimer">
              <div className="opec-disclaimer-icon" aria-hidden="true">i</div>
              <div>
                <h2>Información importante</h2>
                <p>Este buscador es una herramienta informativa e independiente creada por Ascenso Público. Los requisitos mostrados provienen del consolidado de empleos SIMO y fueron actualizados el <strong>{updatedDate}</strong>. Antes de pagar derechos de participación, confirma la información, fechas y disponibilidad directamente en <a href="https://simo.cnsc.gov.co/" target="_blank" rel="noopener noreferrer">SIMO</a> y en los canales oficiales de la CNSC.</p>
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
