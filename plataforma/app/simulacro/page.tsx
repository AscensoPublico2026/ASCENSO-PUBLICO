import Link from "next/link";
import type { Metadata } from "next";
import "../landing.css";
import "./simulacro.css";
import { waUrl, WA_MENSAJES } from "@/lib/contacto";

export const metadata: Metadata = {
  title: "Simulacros gratis por convocatoria",
  description:
    "Simulacros gratis para la prueba escrita de tu concurso: Procuraduría 2026 en sus cuatro versiones y Concurso Docente. 20 casos tipo juicio situacional, puntaje al instante y guía de qué reforzar.",
};

const GRUPOS = [
  {
    id: "procuraduria",
    titulo: "Procuraduría General de la Nación 2026",
    sub: "«Mérito Construyendo Excelencia». Núcleo común del concurso y, además, uno por cada nivel de la convocatoria.",
    simulacros: [
      { id: "procuraduria", nombre: "Procuraduría · Núcleo común", emoji: "⚖️", desc: "Estructura y funciones de la PGN, derecho disciplinario, mecanismos de protección de derechos y derecho de petición." },
      { id: "procuraduria-operativo", nombre: "Procuraduría · Operativo y administrativo", emoji: "🧰", desc: "Auxiliares, citadores y oficinistas: núcleo común más atención al ciudadano, gestión documental y alcance del cargo." },
      { id: "procuraduria-tecnico", nombre: "Procuraduría · Técnico", emoji: "🛠️", desc: "Sustanciadores, técnicos y tecnólogos: núcleo común más procedimiento, calidad de la información y seguridad." },
      { id: "procuraduria-profesional", nombre: "Procuraduría · Profesional y asesor", emoji: "🎓", desc: "Profesional universitario, asesor y ejecutivo: núcleo común más conceptos técnicos, conflicto de interés e independencia de criterio." },
    ],
  },
  {
    id: "docente",
    titulo: "Concurso Docente 2026",
    sub: "Prueba de aptitudes y competencias básicas.",
    simulacros: [
      { id: "docente", nombre: "Docente de aula", emoji: "👩‍🏫", desc: "Lectura crítica, razonamiento cuantitativo, competencias pedagógicas, normatividad y casos de aula." },
    ],
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
        <a href={waUrl(WA_MENSAJES.precio)} target="_blank" rel="noopener" className="btn btn-oro sim-top-cta" data-analytics-event="whatsapp_clicked" data-analytics-placement="simulacro_index_buy">Quiero mi curso</a>
      </header>

      <section className="sim-hero">
        <div className="wrap center">
          <span className="eyebrow c">Simulacros gratis · por convocatoria</span>
          <h1 className="sim-h1">Descubre qué tan listo estás para tu prueba</h1>
          <p className="sim-lead">
            Elige <strong>tu concurso</strong> y responde 20 casos con el formato real de la prueba.
            Al terminar ves tu puntaje, la explicación de cada opción y qué temas debes reforzar.
            Sin costo, sin registro.
          </p>
        </div>
      </section>

      <section className="wrap sim-niveles">
        {GRUPOS.map((g) => (
          <div className="sim-grupo" key={g.id}>
            <h2 className="sim-grupo-t">{g.titulo}</h2>
            <p className="sim-grupo-s">{g.sub}</p>
            <div className="grid grid-3">
              {g.simulacros.map((n) => (
                <div className="card sim-nivel-card" key={n.id}>
                  <span className="sim-nivel-emoji">{n.emoji}</span>
                  <h3>{n.nombre}</h3>
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
          </div>
        ))}

        <div className="sim-pago-band">
          <div>
            <span className="sim-pago-tag">¿Ya hiciste el gratis?</span>
            <h2>Simulacro completo de 100 preguntas</h2>
            <p>
              Con cronómetro, en una sola sesión y con informe por competencia. $39.000, y te lo
              descontamos si después compras el curso.
            </p>
          </div>
          <Link href="/simulacro-completo" className="btn btn-oro" data-analytics-event="cta_click" data-analytics-placement="simulacro_index_pago">
            Ver el simulacro completo →
          </Link>
        </div>

        <p className="sim-nota center">
          Todos los simulacros son gratis y sin registro. Al finalizar te enviamos tu resultado y los
          temas que debes reforzar.
        </p>
      </section>
    </main>
  );
}
