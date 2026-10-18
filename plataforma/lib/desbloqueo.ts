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

export const OPECS_SECUENCIALES = ["236897", "236906", "236760", "236740"];

// Guías que aparecen en el plan pero aún se están escribiendo. Se ven en la
// ruta como "🛠️ En preparación", no se pueden abrir ni marcar, y FRENAN la
// secuencia (y el simulacro). Al terminar una guía: reemplazar su HTML, sacarla
// de esta lista y desplegar (+ /api/admin/seed-guias para refrescar el bucket).
// Se compara por nombre de archivo (sin carpeta).
export const GUIAS_EN_PREPARACION = new Set<string>([
  // Clary y Dayana · Gestor I Talento Humano (236897) — simulacro Día 21
  "SIM-DIAN-GHI-001.html",
  // Paula · Facilitador II (236906) — funcionales Días 14-20 + simulacro
  "FUN-GDOC-FAC2-03-transferencia-y-trazabilidad-documental.html",
  "FUN-COR-FAC2-02-radicacion-y-comunicaciones-oficiales.html",
  "FUN-GP-FAC2-02-apoyo-actos-administrativos.html",
  "FUN-DOC-FAC2-01-control-expedientes.html",
  "FUN-CONST-FAC2-02-derechos-peticion-transparencia.html",
  "FUN-COR-FAC2-03-mensajeria-y-control-entregas.html",
  "FUN-GDOC-FAC2-04-conservacion-prestamo-consulta.html",
  "SIM-DIAN-FAC2-001.html",
  // Edwin · Gestor II administrativo y financiero (236740) — Días 6-8, 11, 12, 14-17, 19, 20
  "DIAN-ADM-COM-03-logro-usuario-comunicacion-equipo.html",
  "DIAN-ADM-COM-04-alcance-cargo-gestor-ii.html",
  "FUN-ADM-03-custodia-disposicion-mercancias.html",
  "FUN-ADM-04-ingresos-almacenamiento-registro-mercancias.html",
  "FUN-ADM-06-siif-nacion-ingresos-egresos.html",
  "FUN-ADM-07-constitucion-politica.html",
  "FUN-ADM-08-notificacion-recursos-archivo.html",
  "FUN-ADM-09-cpaca-principios-procedimiento.html",
  "FUN-ADM-11-documental-pqrsf-servicio-tic.html",
  "FUN-ADM-12-evasion-elusion-contrabando-transparencia.html",
]);

export function enPreparacion(g: any): boolean {
  const base = String(g?.archivo_path || "").split("/").pop() || "";
  return GUIAS_EN_PREPARACION.has(base);
}

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
 * Si la primera no terminada está EN PREPARACIÓN, no hay "actual": la ruta
 * queda "esperando" esa guía y todo lo posterior sigue bloqueado.
 * Las guías sin archivo no cuentan (se muestran "Próximamente").
 */
export function calcularDesbloqueo(guias: any[]): {
  bloqueadas: Set<string>; preparando: Set<string>; actual: any | null; esperando: any | null;
} {
  const bloqueadas = new Set<string>();
  const preparando = new Set<string>();
  let actual: any = null;   // guía abierta por estudiar
  let esperando: any = null; // guía en preparación que frena la ruta
  for (const g of secuenciaPlan(guias)) {
    if (g.tipo === "bonus" || !g.archivo_path) continue;
    const prep = enPreparacion(g);
    if (prep) preparando.add(g.id);
    if (g.leida && !prep) continue;
    if (!actual && !esperando) {
      if (prep) { esperando = g; bloqueadas.add(g.id); }
      else actual = g;
      continue;
    }
    bloqueadas.add(g.id);
  }
  return { bloqueadas, preparando, actual, esperando };
}

/** Siguiente guía del plan (con archivo, sin bonus) después de `guiaId`. */
export function siguienteGuia(guias: any[], guiaId: string): any | null {
  const seq = secuenciaPlan(guias).filter((g) => g.tipo !== "bonus" && g.archivo_path);
  const i = seq.findIndex((g) => g.id === guiaId);
  return i >= 0 && i + 1 < seq.length ? seq[i + 1] : null;
}
