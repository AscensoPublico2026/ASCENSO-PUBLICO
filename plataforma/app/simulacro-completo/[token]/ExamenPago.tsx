"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { PreguntaPublica } from "@/lib/bancoSimulacroPago";
import { waUrl, WA_MENSAJES } from "@/lib/contacto";

type Detalle = PreguntaPublica & {
  correcta: number;
  marcada: number;
  acierto: boolean;
  expl: string[];
};

type Resultado = {
  correctas: number;
  total: number;
  porcentaje: number;
  segundos: number;
  competencias: { eje: string; bien: number; total: number; pct: number }[];
  detalle: Detalle[];
  intento: number;
  maxIntentos: number;
};

type Props = {
  token: string;
  nombre: string;
  titulo: string;
  convocatoria: string;
  nivel: string;
  minutos: number;
  intentoNumero: number;
  maxIntentos: number;
  preguntas: PreguntaPublica[];
};

const LETRAS = ["A", "B", "C", "D", "E"];

function reloj(seg: number): string {
  const s = Math.max(0, Math.floor(seg));
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const r = s % 60;
  const dd = (n: number) => String(n).padStart(2, "0");
  return h > 0 ? `${h}:${dd(m)}:${dd(r)}` : `${dd(m)}:${dd(r)}`;
}

export default function ExamenPago(props: Props) {
  const { token, preguntas, minutos } = props;
  const total = preguntas.length;
  const clave = `ap-sim-pago-${token}`;

  const [fase, setFase] = useState<"inicio" | "examen" | "resultado">("inicio");
  const [respuestas, setRespuestas] = useState<number[]>(() => Array(total).fill(-1));
  const [marcadas, setMarcadas] = useState<boolean[]>(() => Array(total).fill(false));
  const [actual, setActual] = useState(0);
  const [limite, setLimite] = useState<number | null>(null); // timestamp de cierre
  const [ahora, setAhora] = useState(() => Date.now());
  const [enviando, setEnviando] = useState(false);
  const [error, setError] = useState("");
  const [resultado, setResultado] = useState<Resultado | null>(null);
  const [confirmar, setConfirmar] = useState(false);
  const [revisarSolo, setRevisarSolo] = useState<"todas" | "falladas">("todas");
  const enviadoRef = useRef(false);

  // ---- Recuperar un intento a medio hacer (si refrescó o se le fue la señal) ----
  useEffect(() => {
    try {
      const crudo = localStorage.getItem(clave);
      if (!crudo) return;
      const g = JSON.parse(crudo);
      if (!Array.isArray(g?.respuestas) || g.respuestas.length !== total) return;
      if (typeof g.limite !== "number" || g.limite < Date.now()) return;
      setRespuestas(g.respuestas);
      setMarcadas(Array.isArray(g.marcadas) && g.marcadas.length === total ? g.marcadas : Array(total).fill(false));
      setActual(typeof g.actual === "number" ? g.actual : 0);
      setLimite(g.limite);
      setFase("examen");
    } catch {
      /* si el navegador no deja guardar, el examen funciona igual */
    }
  }, [clave, total]);

  // ---- Guardar el avance ----
  useEffect(() => {
    if (fase !== "examen" || limite == null) return;
    try {
      localStorage.setItem(clave, JSON.stringify({ respuestas, marcadas, actual, limite }));
    } catch {
      /* sin almacenamiento: seguimos en memoria */
    }
  }, [clave, fase, respuestas, marcadas, actual, limite]);

  // ---- Reloj ----
  useEffect(() => {
    if (fase !== "examen") return;
    const t = setInterval(() => setAhora(Date.now()), 1000);
    return () => clearInterval(t);
  }, [fase]);

  const restante = limite == null ? minutos * 60 : (limite - ahora) / 1000;
  const contestadas = respuestas.filter((r) => r >= 0).length;

  const enviar = useCallback(
    async (auto = false) => {
      if (enviadoRef.current) return;
      enviadoRef.current = true;
      setEnviando(true);
      setError("");
      try {
        const segundos = limite == null ? 0 : minutos * 60 - Math.max(0, (limite - Date.now()) / 1000);
        const res = await fetch("/api/simulacro-pago/calificar", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ token, respuestas, segundos: Math.round(segundos) }),
        });
        const json = await res.json();
        if (!res.ok) throw new Error(json?.error || "No pudimos calificar tu examen.");
        try {
          localStorage.removeItem(clave);
        } catch {
          /* da igual */
        }
        setResultado(json as Resultado);
        setFase("resultado");
        window.scrollTo({ top: 0 });
      } catch (e: unknown) {
        enviadoRef.current = false;
        setError(
          (e instanceof Error ? e.message : "") ||
            "No pudimos calificar tu examen. Revisa tu conexión e inténtalo otra vez."
        );
        if (auto) setConfirmar(false);
      } finally {
        setEnviando(false);
      }
    },
    [clave, limite, minutos, respuestas, token]
  );

  // ---- Cierre por tiempo ----
  useEffect(() => {
    if (fase === "examen" && limite != null && ahora >= limite && !enviadoRef.current) {
      void enviar(true);
    }
  }, [ahora, enviar, fase, limite]);

  // ---- Aviso al cerrar la pestaña con el examen abierto ----
  useEffect(() => {
    if (fase !== "examen") return;
    const h = (e: BeforeUnloadEvent) => {
      e.preventDefault();
      e.returnValue = "";
    };
    window.addEventListener("beforeunload", h);
    return () => window.removeEventListener("beforeunload", h);
  }, [fase]);

  const empezar = () => {
    setLimite(Date.now() + minutos * 60 * 1000);
    setFase("examen");
  };

  const responder = (opcion: number) => {
    setRespuestas((prev) => {
      const n = [...prev];
      n[actual] = opcion;
      return n;
    });
  };

  const p = preguntas[actual];
  const vistas = useMemo(
    () => (resultado && revisarSolo === "falladas" ? resultado.detalle.filter((d) => !d.acierto) : resultado?.detalle ?? []),
    [resultado, revisarSolo]
  );

  // ================= INICIO =================
  if (fase === "inicio") {
    return (
      <main className="ex-wrap">
        <div className="ex-inicio">
          <span className="ex-kick">{props.convocatoria}</span>
          <h1>{props.titulo}</h1>
          <p className="ex-sub">
            {props.nombre ? `${props.nombre}, este` : "Este"} es tu intento {props.intentoNumero} de{" "}
            {props.maxIntentos}. Preséntalo como el examen real: de una sola sentada, sin interrupciones y sin
            consultar material.
          </p>

          <div className="ex-datos">
            <div>
              <b>{total}</b>
              <span>preguntas</span>
            </div>
            <div>
              <b>{minutos}</b>
              <span>minutos</span>
            </div>
            <div>
              <b>1</b>
              <span>sola sesión</span>
            </div>
          </div>

          <ul className="ex-reglas">
            <li>El cronómetro arranca cuando pulses «Comenzar» y no se puede pausar.</li>
            <li>Puedes navegar entre preguntas y marcar las que quieras revisar al final.</li>
            <li>No verás si aciertas hasta que presentes el examen.</li>
            <li>Si se te cierra el navegador, tus respuestas quedan guardadas mientras dure el tiempo.</li>
            <li>Al terminar recibes tu puntaje, la explicación de cada opción y tu informe por competencia.</li>
          </ul>

          <button className="btn btn-oro ex-empezar" onClick={empezar}>
            Comenzar el simulacro
          </button>
          <p className="ex-nota">Asegúrate de tener {minutos} minutos libres antes de empezar.</p>
        </div>
      </main>
    );
  }

  // ================= RESULTADO =================
  if (fase === "resultado" && resultado) {
    const r = resultado;
    const color = r.porcentaje >= 70 ? "verde" : r.porcentaje >= 50 ? "ambar" : "rojo";
    return (
      <main className="ex-wrap">
        <div className="ex-res-head">
          <span className="ex-kick">{props.titulo}</span>
          <div className={`ex-score ${color}`}>
            <b>{r.porcentaje}%</b>
            <span>
              {r.correctas} de {r.total} correctas
            </span>
          </div>
          <p className="ex-res-tiempo">
            Tiempo empleado: <strong>{reloj(r.segundos)}</strong> · Intento {r.intento} de {r.maxIntentos}
          </p>
          <p className="ex-res-lectura">{lectura(r.porcentaje)}</p>
        </div>

        <section className="ex-comp">
          <h2>Tu informe por competencia</h2>
          <p className="ex-comp-sub">De menor a mayor dominio. Estudia de arriba hacia abajo.</p>
          {r.competencias.map((c) => (
            <div key={c.eje} className="ex-comp-fila">
              <div className="ex-comp-top">
                <span>{c.eje}</span>
                <b>
                  {c.bien}/{c.total}
                </b>
              </div>
              <div className="ex-comp-bar">
                <i
                  className={c.pct >= 70 ? "verde" : c.pct >= 50 ? "ambar" : "rojo"}
                  style={{ width: `${Math.max(3, c.pct)}%` }}
                />
              </div>
            </div>
          ))}
        </section>

        <section className="ex-revision">
          <div className="ex-revision-head">
            <h2>Revisión pregunta por pregunta</h2>
            <div className="ex-filtro">
              <button className={revisarSolo === "todas" ? "on" : ""} onClick={() => setRevisarSolo("todas")}>
                Todas ({r.total})
              </button>
              <button className={revisarSolo === "falladas" ? "on" : ""} onClick={() => setRevisarSolo("falladas")}>
                Solo las falladas ({r.total - r.correctas})
              </button>
            </div>
          </div>

          {vistas.map((d) => (
            <article key={d.i} className={`ex-rev ${d.acierto ? "bien" : "mal"}`}>
              <header>
                <span className="ex-rev-n">#{d.i + 1}</span>
                <span className="ex-rev-tema">{d.tema}</span>
                <span className={`ex-rev-estado ${d.acierto ? "bien" : "mal"}`}>
                  {d.acierto ? "Correcta" : d.marcada < 0 ? "Sin responder" : "Incorrecta"}
                </span>
              </header>
              <p className="ex-rev-ctx">{d.ctx}</p>
              <p className="ex-rev-q">{d.q}</p>
              {d.ops.map((o, k) => (
                <div
                  key={k}
                  className={`ex-rev-op${k === d.correcta ? " ok" : ""}${
                    k === d.marcada && k !== d.correcta ? " err" : ""
                  }`}
                >
                  <b>{LETRAS[k]}.</b>
                  <div>
                    <p>{o}</p>
                    <small>{d.expl[k]}</small>
                  </div>
                </div>
              ))}
            </article>
          ))}
        </section>

        <section className="ex-cierre">
          <h2>¿Y ahora qué estudias?</h2>
          <p>
            Empieza por <strong>{r.competencias[0]?.eje}</strong>
            {r.competencias[1] ? (
              <>
                {" "}
                y <strong>{r.competencias[1].eje}</strong>
              </>
            ) : null}
            . Si quieres que te armemos el plan completo con tu cargo y tu manual de funciones, te descontamos
            los $39.000 de este simulacro.
          </p>
          <a
            href={waUrl(WA_MENSAJES.precio)}
            target="_blank"
            rel="noopener"
            className="btn btn-oro"
            data-analytics-event="whatsapp_clicked"
            data-analytics-placement="simpago_resultado"
          >
            Quiero mi curso con el descuento
          </a>
        </section>
      </main>
    );
  }

  // ================= EXAMEN =================
  return (
    <main className="ex-wrap ex-modo">
      <div className={`ex-barra${restante <= 300 ? " urgente" : ""}`}>
        <div className="ex-barra-in">
          <span className="ex-barra-t">{props.titulo}</span>
          <span className="ex-chip">⏱ {reloj(restante)}</span>
          <span className="ex-chip">
            ✍️ {contestadas} / {total}
          </span>
          <button className="ex-terminar" onClick={() => setConfirmar(true)} disabled={enviando}>
            Presentar
          </button>
        </div>
        <div className="ex-barra-prog">
          <i style={{ width: `${(contestadas / total) * 100}%` }} />
        </div>
      </div>

      <div className="ex-cuerpo">
        <article className="ex-pregunta">
          <header className="ex-p-head">
            <span className="ex-p-n">
              Pregunta {actual + 1} <small>de {total}</small>
            </span>
            <span className="ex-p-eje">{p.refT}</span>
            <button
              className={`ex-marcar${marcadas[actual] ? " on" : ""}`}
              onClick={() =>
                setMarcadas((prev) => {
                  const n = [...prev];
                  n[actual] = !n[actual];
                  return n;
                })
              }
            >
              {marcadas[actual] ? "★ Marcada" : "☆ Marcar para revisar"}
            </button>
          </header>

          <p className="ex-ctx">{p.ctx}</p>
          <p className="ex-q">{p.q}</p>

          <div className="ex-ops">
            {p.ops.map((o, k) => (
              <button
                key={k}
                className={`ex-op${respuestas[actual] === k ? " sel" : ""}`}
                onClick={() => responder(k)}
              >
                <b>{LETRAS[k]}</b>
                <span>{o}</span>
              </button>
            ))}
          </div>

          <div className="ex-nav">
            <button onClick={() => setActual((a) => Math.max(0, a - 1))} disabled={actual === 0}>
              ← Anterior
            </button>
            {respuestas[actual] >= 0 && (
              <button className="ex-limpiar" onClick={() => responder(-1)}>
                Borrar respuesta
              </button>
            )}
            <button
              className="ex-sig"
              onClick={() => setActual((a) => Math.min(total - 1, a + 1))}
              disabled={actual === total - 1}
            >
              Siguiente →
            </button>
          </div>
        </article>

        <aside className="ex-mapa">
          <h3>Tus preguntas</h3>
          <div className="ex-mapa-grid">
            {preguntas.map((_, i) => (
              <button
                key={i}
                className={`ex-mini${respuestas[i] >= 0 ? " hecha" : ""}${marcadas[i] ? " marcada" : ""}${
                  i === actual ? " actual" : ""
                }`}
                onClick={() => setActual(i)}
                aria-label={`Ir a la pregunta ${i + 1}`}
              >
                {i + 1}
              </button>
            ))}
          </div>
          <ul className="ex-leyenda">
            <li>
              <i className="hecha" /> Respondida
            </li>
            <li>
              <i className="marcada" /> Marcada
            </li>
            <li>
              <i /> Sin responder
            </li>
          </ul>
        </aside>
      </div>

      {confirmar && (
        <div className="ex-modal" role="dialog" aria-modal="true">
          <div className="ex-modal-caja">
            <h3>¿Presentar el examen?</h3>
            {contestadas < total ? (
              <p>
                Te faltan <strong>{total - contestadas}</strong> preguntas por responder. Las que dejes en blanco
                cuentan como incorrectas.
              </p>
            ) : (
              <p>Respondiste las {total} preguntas. Después de presentar no podrás cambiar tus respuestas.</p>
            )}
            {error && <p className="ex-error">{error}</p>}
            <div className="ex-modal-btns">
              <button className="ex-volver" onClick={() => setConfirmar(false)} disabled={enviando}>
                Seguir respondiendo
              </button>
              <button className="btn btn-oro" onClick={() => void enviar()} disabled={enviando}>
                {enviando ? "Calificando…" : "Sí, presentar"}
              </button>
            </div>
          </div>
        </div>
      )}
    </main>
  );
}

function lectura(pct: number): string {
  if (pct >= 85) return "Estás en rango de puntaje alto. Mantén el ritmo y repasa solo lo que te quedó flojo.";
  if (pct >= 70) return "Vas bien: pasas el umbral, pero en un concurso lo que decide es la lista de elegibles, no el aprobado. Ahí es donde se gana.";
  if (pct >= 50) return "Tienes la base, pero todavía no alcanza para competir. Con un mes de estudio dirigido esto cambia.";
  return "Hoy no alcanzarías el puntaje. No es para desanimarte: es exactamente lo que necesitabas saber con tiempo.";
}
