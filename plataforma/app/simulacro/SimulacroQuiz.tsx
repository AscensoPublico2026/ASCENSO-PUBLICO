"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import type { PreguntaSimulacro } from "@/lib/simulacro/preguntas";
import { evaluarSimulacro } from "@/lib/simulacro/evaluar";
import { guardarLeadSimulacro } from "./actions";

type Fase = "quiz" | "lead" | "result";

export default function SimulacroQuiz({
  nivel,
  nivelNombre,
  preguntas,
}: {
  nivel: string;
  nivelNombre: string;
  preguntas: PreguntaSimulacro[];
}) {
  const [fase, setFase] = useState<Fase>("quiz");
  const [idx, setIdx] = useState(0);
  const [resp, setResp] = useState<number[]>(() => Array(preguntas.length).fill(-1));
  const [correo, setCorreo] = useState("");
  const [whatsapp, setWhatsapp] = useState("");
  const [marketing, setMarketing] = useState(false);
  const [enviando, setEnviando] = useState(false);
  const [error, setError] = useState("");

  const p = preguntas[idx];
  const total = preguntas.length;
  const esUltima = idx === total - 1;
  const resultado = useMemo(() => evaluarSimulacro(preguntas, resp), [preguntas, resp]);

  function elegir(opt: number) {
    setResp((prev) => {
      const c = [...prev];
      c[idx] = opt;
      return c;
    });
  }

  function siguiente() {
    if (resp[idx] < 0) return;
    if (!esUltima) setIdx(idx + 1);
    else setFase("lead");
  }

  async function enviarLead(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(correo.trim())) {
      setError("Ingresa un correo válido para enviarte tu resultado.");
      return;
    }
    setEnviando(true);
    try {
      await guardarLeadSimulacro({
        nivel,
        correo: correo.trim(),
        whatsapp: whatsapp.trim() || undefined,
        respuestas: resp,
        aceptaMarketing: marketing,
        userAgent: typeof navigator !== "undefined" ? navigator.userAgent : "",
      });
    } catch {
      /* mostramos resultado igual */
    }
    setEnviando(false);
    setFase("result");
  }

  // ---------- FASE QUIZ ----------
  if (fase === "quiz") {
    const progreso = Math.round((idx / total) * 100);
    return (
      <main className="sim-page">
        <header className="sim-top">
          <Link href="/simulacro" className="sim-brand">
            <span className="sim-brand-logo">↗</span>
            <span>Simulacro · {nivelNombre}</span>
          </Link>
          <span className="sim-contador">{idx + 1} / {total}</span>
        </header>

        <div className="sim-quiz wrap">
          <div className="sim-bar"><i style={{ width: `${progreso}%` }} /></div>

          <div className="sim-q-card">
            <span className="sim-q-tema">{p.tema}</span>
            <h2 className="sim-q-enunciado">{p.enunciado}</h2>

            <div className="sim-opciones">
              {p.opciones.map((op, i) => (
                <button
                  key={i}
                  className={`sim-opcion${resp[idx] === i ? " sel" : ""}`}
                  onClick={() => elegir(i)}
                  type="button"
                >
                  <span className="sim-letra">{"ABCD"[i]}</span>
                  <span>{op}</span>
                </button>
              ))}
            </div>
          </div>

          <div className="sim-nav">
            <button
              className="btn btn-ghost-dark"
              onClick={() => setIdx(Math.max(0, idx - 1))}
              disabled={idx === 0}
              type="button"
            >
              ← Anterior
            </button>
            <button
              className="btn btn-azul"
              onClick={siguiente}
              disabled={resp[idx] < 0}
              type="button"
            >
              {esUltima ? "Ver mi resultado →" : "Siguiente →"}
            </button>
          </div>
          <p className="sim-hint center">Responde todas. La retroalimentación aparece al final.</p>
        </div>
      </main>
    );
  }

  // ---------- FASE LEAD ----------
  if (fase === "lead") {
    return (
      <main className="sim-page">
        <header className="sim-top">
          <span className="sim-brand"><span className="sim-brand-logo">↗</span><span>Ascenso Público</span></span>
        </header>
        <div className="sim-lead wrap">
          <div className="sim-lead-card">
            <span className="sim-check-big">✅</span>
            <h2>¡Terminaste el simulacro!</h2>
            <p>Déjanos tu correo y te mostramos tu resultado + el plan de qué estudiar (también te lo enviamos).</p>

            <form onSubmit={enviarLead} className="sim-form">
              <label>
                Correo electrónico *
                <input
                  type="email"
                  value={correo}
                  onChange={(e) => setCorreo(e.target.value)}
                  placeholder="tucorreo@ejemplo.com"
                  required
                />
              </label>
              <label>
                WhatsApp (opcional)
                <input
                  type="tel"
                  value={whatsapp}
                  onChange={(e) => setWhatsapp(e.target.value)}
                  placeholder="300 000 0000"
                />
              </label>

              <label className="sim-consent">
                <input type="checkbox" checked={marketing} onChange={(e) => setMarketing(e.target.checked)} />
                <span>
                  Autorizo a Ascenso Público a enviarme información sobre cursos, descuentos y
                  convocatorias, y el tratamiento de mis datos según la{" "}
                  <Link href="/privacidad" target="_blank">Política de Privacidad</Link> y los{" "}
                  <Link href="/terminos" target="_blank">Términos</Link>.
                </span>
              </label>

              {error && <p className="sim-error">{error}</p>}

              <button className="btn btn-oro sim-form-btn" type="submit" disabled={enviando}>
                {enviando ? "Calculando…" : "Ver mi resultado →"}
              </button>
              <p className="sim-mini">Tu resultado es gratis. No compartimos tu correo con terceros.</p>
            </form>
          </div>
        </div>
      </main>
    );
  }

  // ---------- FASE RESULTADO ----------
  const r = resultado;
  return (
    <main className="sim-page">
      <header className="sim-top">
        <Link href="/" className="sim-brand"><span className="sim-brand-logo">↗</span><span>Ascenso Público</span></Link>
        <Link href="/comprar" className="btn btn-oro sim-top-cta">Quiero mi curso</Link>
      </header>

      <div className="sim-result wrap">
        <div className="sim-score-card">
          <div className={`sim-score-num ${r.porcentaje >= 80 ? "alto" : r.porcentaje >= 50 ? "medio" : "bajo"}`}>
            {r.porcentaje}%
          </div>
          <div className="sim-score-sub">{r.correctas} de {r.total} correctas · Nivel {nivelNombre}</div>
          <p className="sim-score-msg">{r.mensaje}</p>
        </div>

        {r.temasAReforzar.length > 0 && (
          <section className="sim-bloque">
            <h3>📌 Refuerza estos temas</h3>
            <div className="sim-temas">
              {r.temasAReforzar.map((t) => (
                <div className="sim-tema-row reforzar" key={t.tema}>
                  <div>
                    <strong>{t.tema}</strong>
                    <span className="sim-tema-guia">Estudia la guía: {t.guia.titulo}</span>
                  </div>
                  <span className="sim-tema-score">{t.correctas}/{t.total}</span>
                </div>
              ))}
            </div>
          </section>
        )}

        {r.temasDominados.length > 0 && (
          <section className="sim-bloque">
            <h3>✅ Ya dominas</h3>
            <div className="sim-temas">
              {r.temasDominados.map((t) => (
                <div className="sim-tema-row dominado" key={t.tema}>
                  <strong>{t.tema}</strong>
                  <span className="sim-tema-score">{t.correctas}/{t.total}</span>
                </div>
              ))}
            </div>
          </section>
        )}

        <section className="sim-cta-final">
          <h3>Prepárate por TU cargo, no en general</h3>
          <p>
            La CNSC te evalúa según tu cargo específico. Con Ascenso Público estudias exactamente
            estos temas — y los de tu manual de funciones — en un plan de 21 días con simulacro final.
          </p>
          <div className="sim-cta-btns">
            <Link href="/comprar" className="btn btn-oro">Quiero mi curso personalizado →</Link>
            <Link href="/simulacro" className="btn btn-ghost-dark">Probar otro nivel</Link>
          </div>
        </section>

        <details className="sim-review">
          <summary>Ver las respuestas correctas</summary>
          <div className="sim-review-list">
            {preguntas.map((q, i) => {
              const ok = resp[i] === q.correcta;
              return (
                <div className={`sim-review-item ${ok ? "ok" : "bad"}`} key={q.id}>
                  <p className="sim-review-q">{i + 1}. {q.enunciado}</p>
                  <p className="sim-review-correct">✔ {q.opciones[q.correcta]}</p>
                  <p className="sim-review-exp">{q.explicacion}</p>
                </div>
              );
            })}
          </div>
        </details>

        <p className="sim-mini center">Te enviamos este resultado a {correo}. Revisa tu bandeja (y spam).</p>
      </div>
    </main>
  );
}
