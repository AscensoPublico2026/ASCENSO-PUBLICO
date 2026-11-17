import fs from "fs/promises";
import path from "path";

export type PreguntaBanco = {
  tema: string;
  ref: string;
  refT: string;
  nivel: "basic" | "intermediate" | "advanced";
  ctx: string;
  q: string;
  ops: string[];
  correcta: number;
  expl: string[];
};

/** Lo que sí viaja al navegador: sin respuesta correcta ni explicaciones. */
export type PreguntaPublica = {
  i: number;
  tema: string;
  refT: string;
  nivel: string;
  ctx: string;
  q: string;
  ops: string[];
};

const cache = new Map<string, PreguntaBanco[]>();

/**
 * Carga el banco de preguntas de un simulacro de pago. Los bancos viven fuera
 * de /public para que no se puedan descargar sin haber pagado.
 */
export async function cargarBanco(productoId: string): Promise<PreguntaBanco[] | null> {
  if (!/^[a-z0-9-]+$/.test(productoId)) return null;
  const guardado = cache.get(productoId);
  if (guardado) return guardado;

  const archivo = path.join(process.cwd(), "data", "simulacros-pago", `${productoId}.json`);
  try {
    const crudo = await fs.readFile(archivo, "utf-8");
    const banco = JSON.parse(crudo) as PreguntaBanco[];
    if (!Array.isArray(banco)) return null;
    cache.set(productoId, banco);
    return banco;
  } catch {
    return null;
  }
}
