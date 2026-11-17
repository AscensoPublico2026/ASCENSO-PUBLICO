import Link from "next/link";
import type { Metadata } from "next";
import "../landing.css";
import "../simulacro/simulacro.css";
import { waUrl } from "@/lib/contacto";

export const metadata: Metadata = {
  title: "Concurso Docente 2026: fechas, pruebas y simulacro gratis",
  description:
    "Todo sobre el concurso de docentes y directivos docentes 2026 de la CNSC: más de 31.000 vacantes, fechas de inscripción, las cuatro pruebas y su ponderación, y un simulacro gratis de 20 preguntas.",
};

const ETAPAS = [
  {
    n: "01",
    t: "Aptitudes y competencias básicas",
    car: "Eliminatoria",
    peso: "55 %",
    d: "Es la prueba que decide quién sigue. Evalúa lectura crítica, razonamiento cuantitativo, competencias pedagógicas y del área, y competencias blandas. Mínimo 60/100 para docentes y 70/100 para directivos docentes.",
  },
  { n: "02", t: "Prueba psicotécnica", car: "Clasificatoria", peso: "5 % docentes · 10 % directivos", d: "El mismo día de la escrita. Valora actitudes, motivaciones e intereses frente a las funciones del cargo, con casos de aula tipo juicio situacional." },
  { n: "03", t: "Valoración de antecedentes", car: "Clasificatoria", peso: "30 % docentes · 25 % directivos", d: "Puntúa la formación y la experiencia que superan el requisito mínimo del empleo. Se prepara desde hoy, reuniendo y certificando tus soportes." },
  { n: "04", t: "Entrevista", car: "Clasificatoria", peso: "10 %", d: "Diálogo estructurado sobre las competencias comportamentales del cargo, calificado de 0 a 100." },
];

export default function Docentes() {
  return (
    <main className="sim-page">
      <header className="sim-top">
        <Link href="/" className="sim-brand">
          <span className="sim-brand-logo">↗</span>
          <span>Ascenso Público</span>
        </Link>
        <a
          href="/simulacro-gratis/docente.html"
          className="btn btn-oro sim-top-cta"
          data-analytics-event="cta_click"
          data-analytics-placement="docentes_top_simulacro"
        >
          Simulacro gratis
        </a>
      </header>

      <section className="sim-hero">
        <div className="wrap center">
          <span className="eyebrow c">Concurso docente y directivos docentes 2026</span>
          <h1 className="sim-h1">El concurso más grande del país ya empezó</h1>
          <p className="sim-lead">
            Más de 31.000 vacantes en instituciones educativas oficiales. Las inscripciones para las
            vacantes reservadas a personas con discapacidad van del <b>23 de noviembre de 2026 al 15 de
            enero de 2027</b>; las de población general se esperan a comienzos de 2027 y la prueba
            escrita, en el segundo semestre de 2027.
          </p>
          <div className="doc-hero-cta">
            <a href="/simulacro-gratis/docente.html" className="btn btn-oro" data-analytics-event="cta_click" data-analytics-placement="docentes_hero_simulacro">
              Hacer el simulacro gratis
            </a>
            <a
              href={waUrl("Hola, quiero que me avisen cuando abra la preparación para el concurso docente 2026.")}
              target="_blank"
              rel="noopener"
              className="btn btn-wa"
              data-analytics-event="whatsapp_clicked"
              data-analytics-placement="docentes_hero_wa"
            >
              🔔 Avísame cuando abra el curso
            </a>
          </div>
          <p className="doc-nota-fechas">
            Fechas tomadas de los comunicados de la CNSC. Las que aún no son oficiales están marcadas como previstas.
          </p>
        </div>
      </section>

      <section className="wrap doc-sec">
        <h2>Las cuatro pruebas y cuánto pesa cada una</h2>
        <p className="doc-lead">
          Todo se juega en la primera: si no alcanzas el mínimo en aptitudes y competencias básicas,
          el resto del proceso ya no aplica.
        </p>
        <div className="doc-etapas">
          {ETAPAS.map((e) => (
            <article key={e.n} className={`doc-etapa${e.car === "Eliminatoria" ? " elim" : ""}`}>
              <span className="doc-etapa-n">{e.n}</span>
              <div>
                <div className="doc-etapa-head">
                  <h3>{e.t}</h3>
                  <span className={`doc-chip${e.car === "Eliminatoria" ? " rojo" : ""}`}>{e.car}</span>
                  <span className="doc-chip peso">{e.peso}</span>
                </div>
                <p>{e.d}</p>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="doc-band">
        <div className="wrap">
          <h2>Empieza por saber dónde estás parado</h2>
          <p>
            20 preguntas con el enfoque de la prueba eliminatoria: lectura crítica, razonamiento
            cuantitativo, pedagogía, normatividad, convivencia escolar y casos de aula. Al terminar
            ves tu puntaje, por qué cada opción es correcta o es trampa, y qué debes reforzar.
          </p>
          <a href="/simulacro-gratis/docente.html" className="btn btn-oro" data-analytics-event="cta_click" data-analytics-placement="docentes_band_simulacro">
            Empezar el simulacro gratis →
          </a>
        </div>
      </section>

      <section className="wrap doc-sec">
        <h2>Qué puedes hacer desde hoy</h2>
        <div className="doc-pasos">
          <div><span>1</span><h3>Revisa tu OPEC en SIMO</h3><p>Mira qué cargos puede ocupar tu profesión y en qué entidad territorial. No todos exigen experiencia.</p></div>
          <div><span>2</span><h3>Reúne tus soportes</h3><p>La valoración de antecedentes pesa 30 %. Certificados de estudio y experiencia que superen el requisito mínimo suman puntos.</p></div>
          <div><span>3</span><h3>Entrena con casos</h3><p>La prueba no pregunta definiciones: pone situaciones de aula. Practica con el simulacro y con las guías gratis.</p></div>
          <div><span>4</span><h3>No esperes la fecha del examen</h3><p>Quien empieza cuando sale la citación llega con semanas. Quien empieza hoy llega con meses.</p></div>
        </div>
        <div className="guias-cta">
          <h2>¿Quieres preparación completa para tu cargo?</h2>
          <p>
            Estamos armando la preparación del concurso docente por cargo y por área. Déjanos tu
            WhatsApp y te avisamos apenas abra, con precio de lanzamiento.
          </p>
          <div style={{ display: "flex", gap: 12, justifyContent: "center", flexWrap: "wrap" }}>
            <a
              href={waUrl("Hola, quiero que me avisen cuando abra la preparación para el concurso docente 2026. Mi cargo de interés es:")}
              target="_blank"
              rel="noopener"
              className="btn btn-oro"
              data-analytics-event="whatsapp_clicked"
              data-analytics-placement="docentes_cta_wa"
            >
              🔔 Avísame por WhatsApp
            </a>
            <Link href="/guias-gratis" className="btn-ghost-dark">Ver guías gratis</Link>
          </div>
        </div>
      </section>
    </main>
  );
}
