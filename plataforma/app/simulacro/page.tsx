import Link from "next/link";
import type { Metadata } from "next";
import { NIVELES, preguntasDeNivel } from "@/lib/simulacro/preguntas";
import "../landing.css";
import "./simulacro.css";

export const metadata: Metadata = {
  title: "Simulacro CNSC gratis por nivel | Ascenso Público",
  description:
    "Mide tu conocimiento para la prueba escrita de la CNSC con un simulacro gratis según tu nivel (asistencial, técnico o profesional). Recibe retroalimentación y descubre qué estudiar.",
};

const DESC: Record<string, string> = {
  asistencial: "Estado, atención al ciudadano y competencias del nivel asistencial.",
  tecnico: "Marco institucional, procesos técnicos y competencias del nivel técnico.",
  profesional: "Función pública, gestión y competencias del nivel profesional.",
};

export default function SimulacroIndex() {
  return (
    <main className="sim-page">
      <header className="sim-top">
        <Link href="/" className="sim-brand">
          <span className="sim-brand-logo">↗</span>
          <span>Ascenso Público</span>
        </Link>
        <Link href="/comprar" className="btn btn-oro sim-top-cta">Quiero mi curso</Link>
      </header>

      <section className="sim-hero">
        <div className="wrap center">
          <span className="eyebrow c">Simulacro gratis · CNSC</span>
          <h1 className="sim-h1">Descubre qué tan listo estás para tu prueba</h1>
          <p className="sim-lead">
            Responde un simulacro <strong>gratis</strong> según tu nivel y recibe una
            <strong> retroalimentación</strong> que te dice exactamente qué temas dominas y
            cuáles reforzar. Sin costo, sin compromiso.
          </p>
        </div>
      </section>

      <section className="wrap sim-niveles">
        <div className="grid grid-3">
          {NIVELES.map((n) => {
            const total = preguntasDeNivel(n.id).length;
            return (
              <div className="card sim-nivel-card" key={n.id}>
                <span className="sim-nivel-emoji">{n.emoji}</span>
                <h3>Nivel {n.nombre}</h3>
                <p>{DESC[n.id]}</p>
                <div className="sim-nivel-meta">{total} preguntas · ~10 min</div>
                <Link href={`/simulacro/${n.id}`} className="btn btn-azul sim-nivel-btn">
                  Empezar simulacro →
                </Link>
              </div>
            );
          })}
        </div>
        <p className="sim-nota center">
          Mide conocimiento del Estado y temas básicos de la prueba escrita. Al finalizar,
          te enviamos tu resultado por correo.
        </p>
      </section>
    </main>
  );
}
