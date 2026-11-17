import type { Metadata } from "next";
import Link from "next/link";
import NavLanding from "../components/NavLanding";
import FormCompra from "./FormCompra";
import { PRODUCTOS, SIM_DIAS_ACCESO, SIM_INTENTOS } from "@/lib/simulacroPago";
import { waUrl, WA_MENSAJES, CORREO_CONTACTO } from "@/lib/contacto";
import "../landing.css";
import "./simulacro-completo.css";

export const metadata: Metadata = {
  title: "Simulacro completo por cargo · 100 preguntas",
  description:
    "Simulacro completo de 100 preguntas con el formato de la prueba escrita del concurso: cronómetro, explicación de cada opción e informe por competencia. $39.000, y se te descuenta si luego compras el curso.",
  alternates: { canonical: "/simulacro-completo" },
};

const QUE_TRAE = [
  {
    ic: "📝",
    t: "100 preguntas con el formato oficial",
    d: "Caso, enunciado y tres opciones de respuesta, como en la Prueba de Juicio Situacional de la CNSC. No es una muestra: es la prueba completa de principio a fin.",
  },
  {
    ic: "⏱",
    t: "Cronómetro y una sola sesión",
    d: "Se presenta como el examen real: tiempo corriendo, sin ver aciertos sobre la marcha y sin poder devolverte al final. Aquí es donde aparece el nervio que te hace fallar el día de la prueba.",
  },
  {
    ic: "🔍",
    t: "Las tres opciones explicadas",
    d: "Al terminar ves por qué la correcta lo es y por qué las otras dos, que también suenan razonables, no responden lo que el caso pregunta.",
  },
  {
    ic: "📊",
    t: "Informe por competencia",
    d: "Tu puntaje desagregado por eje temático, los temas que dominas, los que te están costando y en qué orden estudiarlos.",
  },
];

export default function SimulacroCompletoPage() {
  return (
    <>
      <NavLanding />

      <section className="simc-hero">
        <div className="wrap simc-hero-grid">
          <div>
            <span className="kick">Simulacro completo · por convocatoria y nivel</span>
            <h1>
              Mide tu puntaje real <span className="hl">antes del examen</span>
            </h1>
            <p className="sub">
              100 preguntas con el formato oficial de la prueba escrita: un caso, un enunciado y tres
              opciones. Cronometradas y en una sola sesión. Al terminar sabes tu puntaje, qué competencia
              te está costando y qué estudiar primero.
            </p>
            <div className="simc-precio-hero">
              <span className="simc-num">$39.000</span>
              <div>
                <b>Pago único</b>
                <small>
                  {SIM_INTENTOS} intentos · {SIM_DIAS_ACCESO} días de acceso
                </small>
              </div>
            </div>
            <p className="simc-descuento">
              🎁 Si después compras el curso, <strong>te descontamos los $39.000 completos</strong> durante los{" "}
              {SIM_DIAS_ACCESO} días siguientes.
            </p>
            <a href="#comprar" className="btn btn-oro">
              Quiero presentarlo
            </a>
            <p className="simc-gratis-link">
              ¿Primero quieres probar? <Link href="/simulacro">Haz el simulacro gratis de 20 preguntas</Link>.
            </p>
          </div>

          <div className="simc-shot" aria-hidden="true">
            <div className="simc-ventana">
              <div className="simc-ventana-bar">
                <span>Simulacro en curso</span>
                <span className="simc-chip">⏱ 48:12</span>
                <span className="simc-chip">✍️ 37 / 100</span>
              </div>
              <div className="simc-ventana-prog">
                <i />
              </div>
              <div className="simc-ventana-body">
                <span className="simc-tag">Caso 38 · Derecho disciplinario</span>
                <p className="simc-caso">
                  Durante una indagación previa usted advierte que el término para resolver venció hace
                  dos semanas y que el expediente sigue sin decisión de fondo…
                </p>
                <div className="simc-op">A. Archivar de inmediato por vencimiento del término</div>
                <div className="simc-op sel">B. Informar al superior y dejar constancia en el expediente</div>
                <div className="simc-op">C. Continuar la actuación sin dejar registro</div>
                <div className="simc-op">D. Remitir el caso a otra dependencia</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="sec">
        <div className="wrap">
          <span className="eyebrow c" style={{ display: "block", textAlign: "center" }}>
            Qué recibes
          </span>
          <h2 className="center">Lo que un simulacro serio tiene que darte</h2>
          <div className="simc-trae">
            {QUE_TRAE.map((x) => (
              <article key={x.t} className="simc-trae-item">
                <span className="simc-trae-ic">{x.ic}</span>
                <h3>{x.t}</h3>
                <p>{x.d}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="sec sec-alt">
        <div className="wrap simc-compra-grid">
          <div className="simc-compra-copy">
            <span className="eyebrow">Cómo lo recibes</span>
            <h2>Sin usuario, sin contraseña</h2>
            <p className="lead">
              Pagas, y el acceso te llega al correo como un enlace propio. Lo abres desde el celular o el
              computador, sin crear cuenta ni recordar claves.
            </p>
            <ol className="simc-pasos">
              <li>
                <b>Eliges tu simulacro</b> y dejas tu nombre, correo y celular.
              </li>
              <li>
                <b>Pagas $39.000</b> con PSE, Nequi, Bancolombia o tarjeta en la pasarela de Wompi.
              </li>
              <li>
                <b>Recibes tu enlace</b> en pantalla y en el correo, apenas se aprueba el pago.
              </li>
              <li>
                <b>Lo presentas cuando quieras</b>, dentro de los {SIM_DIAS_ACCESO} días, hasta {SIM_INTENTOS} veces.
              </li>
            </ol>
            <p className="simc-ayuda">
              ¿Pagaste y no te llegó? Escríbenos por{" "}
              <a href={waUrl(WA_MENSAJES.simulacroPago)} target="_blank" rel="noopener">
                WhatsApp
              </a>{" "}
              o a <a href={`mailto:${CORREO_CONTACTO}`}>{CORREO_CONTACTO}</a> y te reenviamos el enlace.
            </p>
          </div>

          <FormCompra productos={PRODUCTOS} />
        </div>
      </section>

      <section className="sec">
        <div className="wrap">
          <span className="eyebrow">Preguntas frecuentes</span>
          <h2>Antes de comprarlo</h2>
          <div className="faq" style={{ marginTop: 28 }}>
            <details open>
              <summary>¿En qué se diferencia del simulacro gratis?</summary>
              <div className="ans">
                El gratis son 20 casos para que midas tu criterio. Este son <strong>100</strong>, con cronómetro,
                en una sola sesión y con un informe por competencia. El gratis te dice si vas bien; este te dice
                qué puntaje sacarías y qué estudiar.
              </div>
            </details>
            <details>
              <summary>¿Las preguntas son las del examen real?</summary>
              <div className="ans">
                No, y desconfía de quien te diga que sí: las preguntas de la CNSC son reservadas. Las nuestras se
                construyen con los <strong>ejes temáticos publicados en el acuerdo de la convocatoria</strong> y
                con el formato real de juicio situacional.
              </div>
            </details>
            <details>
              <summary>¿Cuántas veces puedo presentarlo?</summary>
              <div className="ans">
                {SIM_INTENTOS} intentos durante {SIM_DIAS_ACCESO} días. La recomendación es presentarlo una vez
                ahora, estudiar lo que salga flojo y repetirlo cerca de la fecha del examen.
              </div>
            </details>
            <details>
              <summary>¿Y si después quiero el curso completo?</summary>
              <div className="ans">
                Te descontamos los <strong>$39.000 completos</strong> del valor del curso si lo compras dentro de
                los {SIM_DIAS_ACCESO} días. Solo recuérdanoslo por WhatsApp.
              </div>
            </details>
            <details>
              <summary>¿Puedo pagarlo por WhatsApp?</summary>
              <div className="ans">
                Sí. Si no te sientes cómodo pagando en línea, escríbenos y coordinamos el pago contigo.
              </div>
            </details>
          </div>
        </div>
      </section>
    </>
  );
}
