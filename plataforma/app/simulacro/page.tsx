import Link from "next/link";
import type { Metadata } from "next";
import "../landing.css";
import "./simulacro.css";

export const metadata: Metadata = {
  title: "Simulacro CNSC gratis por nivel | Ascenso Público",
  description:
    "Mide tu conocimiento para la prueba escrita de la CNSC con un simulacro gratis según tu nivel (asistencial, técnico o profesional). 20 preguntas tipo CNSC, retroalimentación y guía de qué estudiar.",
};

const NIVELES = [
  {
    id: "asistencial",
    nombre: "Asistencial",
    emoji: "🧰",
    desc: "Estado, atención al ciudadano y competencias del nivel asistencial.",
  },
  {
    id: "tecnico",
    nombre: "Técnico",
    emoji: "🛠️",
    desc: "Marco institucional, procesos técnicos y competencias del nivel técnico.",
  },
  {
    id: "profesional",
    nombre: "Profesional",
    emoji: "🎓",
    desc: "Función pública, gestión y competencias del nivel profesional.",
  },
];

export default function SimulacroIndex() {
  return (
    <main className="sim-page">
      <header className="sim-top">
        <Link href="/" className="sim-brand">
          <span className="sim-brand-logo">↗</span>
          <span>Ascenso Público</span>
        </Link>
        <Link href="/comprar" className="btn btn-oro sim-top-cta" data-analytics-event="cta_click" data-analytics-placement="simulacro_index_buy">Quiero mi curso</Link>
      </header>

      <section className="sim-hero">
        <div className="wrap center">
          <span className="eyebrow c">Simulacro gratis · CNSC</span>
          <h1 className="sim-h1">Descubre qué tan listo estás para tu prueba</h1>
          <p className="sim-lead">
            Responde un simulacro <strong>gratis</strong> de 20 preguntas tipo CNSC según tu
            nivel y recibe una <strong>retroalimentación</strong> que te dice exactamente qué
            temas dominas y cuáles reforzar. Sin costo, sin compromiso.
          </p>
        </div>
      </section>

      <section className="wrap sim-niveles">
        <div className="grid grid-3">
          {NIVELES.map((n) => (
            <div className="card sim-nivel-card" key={n.id}>
              <span className="sim-nivel-emoji">{n.emoji}</span>
              <h3>Nivel {n.nombre}</h3>
              <p>{n.desc}</p>
              <div className="sim-nivel-meta">20 preguntas · ~30 min</div>
              <a
                href={`/simulacro-gratis/${n.id}.html`}
                className="btn btn-azul sim-nivel-btn"
                data-analytics-event="cta_click"
                data-analytics-placement="simulacro_index_start"
                data-analytics-level={n.id}
              >
                Empezar simulacro →
              </a>
            </div>
          ))}
        </div>
        <p className="sim-nota center">
          Mide tu conocimiento del Estado y los temas base de la prueba escrita. Al finalizar,
          te enviamos tu resultado por correo.
        </p>
      </section>
    </main>
  );
}
