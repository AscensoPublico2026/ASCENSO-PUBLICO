// ============================================================
// Desbloqueo secuencial de guías
// ------------------------------------------------------------
// En los cursos marcados como "secuenciales", el estudiante ve el plan
// COMPLETO desde el primer día, pero cada guía se abre solo cuando
// TERMINA la anterior (botón "✓ Terminé esta guía" en el visor).
// En estos cursos abrir una guía ya NO la marca como leída.
//
// Los demás cursos siguen como siempre (todo abierto; la guía se marca
// leída al abrirla; solo el simulacro espera a que se lean todas).
//
// Un curso es secuencial si:
//   - su columna `desbloqueo_secuencial` es true (ver
//     supabase/migracion-desbloqueo-secuencial.sql), o
//   - su OPEC está en OPECS_SECUENCIALES (respaldo que funciona aunque la
//     migración aún no se haya aplicado).
// ============================================================

export const OPECS_SECUENCIALES = ["236897", "236906"];

// Minutos mínimos con la guía abierta antes de poder marcarla terminada.
export const MINUTOS_MINIMOS_GUIA = 10;

export function esCursoSecuencial(curso: any): boolean {
  if (!curso) return false;
  if (curso.desbloqueo_secuencial === true) return true;
  return OPECS_SECUENCIALES.includes(String(curso.opec || "").trim());
}

// Orden de los módulos del currículo (debe coincidir con /perfil/[cursoId]).
export const ORDEN_MODULOS = ["introduccion", "generales", "nivel", "funcional", "bonus", "simulacro"];

export function moduloKey(g: any): string {
  if (g.tipo === "simulacro") return "simulacro";
  if (g.tipo === "bonus") return "bonus";
  if (g.tipo === "funcional") return "funcional";
  if (g.tipo === "nivel") return "nivel";
  // INTRO-00 y "Conoce tu Entidad" (ENT-) van a Introducción; el resto de
  // generales (GEN-) quedan en Conocimientos Generales.
  if (/(^|\/)(INTRO|ENT)-/i.test(g.archivo_path || "") || g.dia === 1) return "introduccion";
  return "generales";
}

function ordenDentro(g: any): number {
  return g.orden ?? g.dia ?? 0;
}

/** Guías del plan en el orden en que el estudiante debe recorrerlas. */
export function secuenciaPlan(guias: any[]): any[] {
  return [...(guias || [])].sort((a, b) => {
    const ma = ORDEN_MODULOS.indexOf(moduloKey(a));
    const mb = ORDEN_MODULOS.indexOf(moduloKey(b));
    if (ma !== mb) return ma - mb;
    return ordenDentro(a) - ordenDentro(b);
  });
}

/**
 * Calcula qué guías están bloqueadas en un curso secuencial.
 * Regla: se recorre el plan en orden (sin bonus, que siempre está libre);
 * las guías ya terminadas están abiertas; la PRIMERA no terminada está
 * abierta (es la "actual"); todas las siguientes no terminadas, bloqueadas.
 * Las guías sin archivo no cuentan (se muestran "Próximamente").
 */
export function calcularDesbloqueo(guias: any[]): { bloqueadas: Set<string>; actual: any | null; anterior: Map<string, any> } {
  const bloqueadas = new Set<string>();
  const anterior = new Map<string, any>();
  let actual: any = null;
  let previa: any = null;
  for (const g of secuenciaPlan(guias)) {
    if (g.tipo === "bonus" || !g.archivo_path) continue;
    if (previa) anterior.set(g.id, previa);
    previa = g;
    if (g.leida) continue;
    if (!actual) { actual = g; continue; }
    bloqueadas.add(g.id);
  }
  return { bloqueadas, actual, anterior };
}

/** Siguiente guía del plan (con archivo, sin bonus) después de `guiaId`. */
export function siguienteGuia(guias: any[], guiaId: string): any | null {
  const seq = secuenciaPlan(guias).filter((g) => g.tipo !== "bonus" && g.archivo_path);
  const i = seq.findIndex((g) => g.id === guiaId);
  return i >= 0 && i + 1 < seq.length ? seq[i + 1] : null;
}
