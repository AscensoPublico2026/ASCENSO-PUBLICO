/**
 * Motor de evaluación del simulacro gratis.
 * La retroalimentación se calcula AL FINAL (después de responder todas).
 */
import { PreguntaSimulacro, GuiaRef } from "./preguntas";

export interface ResultadoTema {
  tema: string;
  guia: GuiaRef;
  correctas: number;
  total: number;
  /** "dominado" | "regular" | "reforzar" */
  estado: "dominado" | "regular" | "reforzar";
}

export interface ResultadoSimulacro {
  total: number;
  correctas: number;
  porcentaje: number; // 0-100
  temas: ResultadoTema[];
  temasAReforzar: ResultadoTema[];
  temasDominados: ResultadoTema[];
  /** Mensaje global según el desempeño. */
  mensaje: string;
}

/**
 * @param preguntas  preguntas presentadas (en el orden mostrado)
 * @param respuestas índice elegido por el usuario para cada pregunta (-1 si no respondió)
 */
export function evaluarSimulacro(
  preguntas: PreguntaSimulacro[],
  respuestas: number[]
): ResultadoSimulacro {
  const total = preguntas.length;
  let correctas = 0;

  const acc = new Map<string, ResultadoTema>();

  preguntas.forEach((p, i) => {
    const ok = respuestas[i] === p.correcta;
    if (ok) correctas++;

    const key = p.tema;
    const t = acc.get(key) ?? {
      tema: p.tema,
      guia: p.guia,
      correctas: 0,
      total: 0,
      estado: "regular" as const,
    };
    t.total += 1;
    if (ok) t.correctas += 1;
    acc.set(key, t);
  });

  const temas = Array.from(acc.values()).map((t) => {
    const ratio = t.total > 0 ? t.correctas / t.total : 0;
    t.estado = ratio >= 0.8 ? "dominado" : ratio >= 0.5 ? "regular" : "reforzar";
    return t;
  });

  const porcentaje = total > 0 ? Math.round((correctas / total) * 100) : 0;

  const temasAReforzar = temas
    .filter((t) => t.estado !== "dominado")
    .sort((a, b) => a.correctas / a.total - b.correctas / b.total);
  const temasDominados = temas.filter((t) => t.estado === "dominado");

  let mensaje: string;
  if (porcentaje >= 80) {
    mensaje =
      "¡Excelente base! Vas muy bien. Pule los detalles de tu cargo específico y llegas listo a la prueba.";
  } else if (porcentaje >= 50) {
    mensaje =
      "Buen punto de partida. Tienes bases, pero hay temas clave por reforzar para subir tu puntaje.";
  } else {
    mensaje =
      "Tienes mucho por ganar. La buena noticia: ya sabes EXACTAMENTE qué estudiar. Enfócate en los temas marcados.";
  }

  return {
    total,
    correctas,
    porcentaje,
    temas,
    temasAReforzar,
    temasDominados,
    mensaje,
  };
}
