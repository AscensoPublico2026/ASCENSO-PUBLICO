import Link from "next/link";
import type { Metadata } from "next";
import "../landing.css";
import "../simulacro/simulacro.css";
import { waUrl, WA_MENSAJES } from "@/lib/contacto";

export const metadata: Metadata = {
  title: "Guías y simulacros gratis para concursos de mérito",
  description:
    "Guías de estudio gratis sobre el Estado, la función pública, la relación Estado-ciudadano y el marco institucional, más los simulacros gratis de la Procuraduría 2026 y del Concurso Docente.",
};

const GUIAS = [
  {
    href: "/guias-gratis/como-funciona-un-concurso-cnsc.html",
    emoji: "🧭",
    titulo: "Cómo funciona un concurso de la CNSC",
    desc: "Qué evalúa cada prueba, cómo piensa la CNSC, los errores que más eliminan y cómo detectar los distractores.",
  },
  {
    href: "/guias-gratis/estado-y-funcion-publica.html",
    emoji: "🏛️",
    titulo: "Estado y Función Pública",
    desc: "Fines del Estado, principios de la función administrativa, deberes y prohibiciones del servidor, mérito y carrera.",
  },
  {
    href: "/guias-gratis/relacion-estado-ciudadano.html",
    emoji: "🤝",
    titulo: "Relación Estado-Ciudadano",
    desc: "Derecho de petición y sus términos, transparencia y acceso a la información, protección de datos y atención al ciudadano.",
  },
  {
    href: "/guias-gratis/marco-institucional.html",
    emoji: "⚖️",
    titulo: "Marco Institucional",
    desc: "Ramas del poder público, órganos autónomos y de control, control interno y cómo se organiza la administración.",
  },
];

const SIMULACROS = [
  { href: "/simulacro-gratis/procuraduria.html", emoji: "⚖️", titulo: "Procuraduría · Núcleo común", desc: "Estructura y funciones de la PGN, disciplinario y mecanismos de protección.", nuevo: true },
  { href: "/simulacro-gratis/procuraduria-operativo.html", emoji: "🧰", titulo: "Procuraduría · Operativo", desc: "Auxiliares y oficinistas: atención al ciudadano y alcance del cargo.", nuevo: true },
  { href: "/simulacro-gratis/procuraduria-tecnico.html", emoji: "🛠️", titulo: "Procuraduría · Técnico", desc: "Sustanciadores y técnicos: procedimiento y calidad de la información.", nuevo: true },
  { href: "/simulacro-gratis/procuraduria-profesional.html", emoji: "🎓", titulo: "Procuraduría · Profesional", desc: "Profesional y asesor: conceptos, conflicto de interés y liderazgo.", nuevo: true },
  { href: "/simulacro-gratis/docente.html", emoji: "👩‍🏫", titulo: "Concurso Docente 2026", desc: "Lectura crítica, razonamiento, pedagogía y casos de aula.", nuevo: true },
];

export default function GuiasGratis() {
  return (
    <main className="sim-page">
      <header className="sim-top">
        <Link href="/" className="sim-brand">
          <span className="sim-brand-logo">↗</span>
          <span>Ascenso Público</span>
        </Link>
        <a href={waUrl(WA_MENSAJES.precio)} target="_blank" rel="noopener" className="btn btn-oro sim-top-cta" data-analytics-event="whatsapp_clicked" data-analytics-placement="guias_gratis_top">
          Quiero mi curso
        </a>
      </header>

      <section className="sim-hero">
        <div className="wrap center">
          <span className="eyebrow c">Material gratis · concursos de mérito</span>
          <h1 className="sim-h1">Empieza a estudiar hoy, gratis</h1>
          <p className="sim-lead">
            Las guías generales que evalúan casi todas las convocatorias y cinco simulacros tipo caso,
            con la explicación de cada respuesta. Sin registro para leer.
          </p>
        </div>
      </section>

      <section className="wrap sim-niveles">
        <h2 className="center" style={{ color: "var(--azul)", marginBottom: 8 }}>📚 Guías de estudio gratis</h2>
        <p className="center" style={{ color: "var(--texto-suave)", maxWidth: 620, margin: "0 auto 26px" }}>
          Son las mismas guías generales de nuestra ruta de 21 días: con ejemplos, casos y autoevaluación.
        </p>
        <div className="grid grid-4">
          {GUIAS.map((g) => (
            <div className="card sim-nivel-card" key={g.href}>
              <span className="sim-nivel-emoji">{g.emoji}</span>
              <h3>{g.titulo}</h3>
              <p>{g.desc}</p>
              <div className="sim-nivel-meta">Guía completa · lectura de 60–90 min</div>
              <a href={g.href} className="btn btn-azul sim-nivel-btn" data-analytics-event="cta_click" data-analytics-placement="guias_gratis_abrir">
                Abrir guía →
              </a>
            </div>
          ))}
        </div>

        <h2 className="center" style={{ color: "var(--azul)", margin: "56px 0 8px" }}>📝 Simulacros gratis</h2>
        <p className="center" style={{ color: "var(--texto-suave)", maxWidth: 620, margin: "0 auto 26px" }}>
          20 casos cada uno. Al final ves tu puntaje, la explicación de cada opción y qué temas reforzar.
        </p>
        <div className="guias-sim-grid">
          {SIMULACROS.map((s) => (
            <a key={s.href} href={s.href} className="guias-sim-card" data-analytics-event="cta_click" data-analytics-placement="guias_gratis_simulacro">
              {s.nuevo && <span className="sim-promo-nuevo">NUEVO</span>}
              <span className="sim-nivel-emoji">{s.emoji}</span>
              <strong>{s.titulo}</strong>
              <span>{s.desc}</span>
              <span className="guias-sim-go">Empezar →</span>
            </a>
          ))}
        </div>

        <div className="guias-cta">
          <h2>¿Y lo específico de tu cargo?</h2>
          <p>
            Las guías gratis cubren lo general. La prueba funcional evalúa las funciones de <b>tu</b> empleo.
            En el curso armamos tu ruta de 21 días con tu OPEC y tu manual de funciones.
          </p>
          <div style={{ display: "flex", gap: 12, justifyContent: "center", flexWrap: "wrap" }}>
            <a href={waUrl(WA_MENSAJES.precio)} target="_blank" rel="noopener" className="btn btn-oro" data-analytics-event="whatsapp_clicked" data-analytics-placement="guias_gratis_comprar">Quiero mi curso personalizado</a>
            <Link href="/#como" className="btn-ghost-dark">Ver cómo funciona</Link>
          </div>
        </div>
      </section>
    </main>
  );
}
