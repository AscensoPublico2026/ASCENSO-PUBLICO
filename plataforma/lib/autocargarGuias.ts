/**
 * Auto-carga de guías al confirmar pago.
 * 
 * Regla de asignación (basada en biblioteca/biblioteca.json):
 * - Introducción (INTRO-00 o INTRO-00-PGN según convocatoria): Día 1 → siempre
 * - Generales (GEN-01, GEN-02, GEN-03): Días 2-4 → siempre
 * - Por Nivel (ASI/TEC/PRO según curso.nivel): Días 5-8 → según nivel
 * - Bonus (BON-01, BON-02): sin día fijo → siempre (sección bonus)
 * - Funcionales (Días 9-20): NO se auto-cargan (admin las sube personalizadas)
 * - Simulacro Final (Día 21): NO se auto-carga (admin la sube personalizada)
 * - INTRO-01 "Conoce tu Entidad": NO se auto-carga (bajo-demanda, admin la asigna)
 */

import { SupabaseClient } from "@supabase/supabase-js";

// --- Convocatorias con régimen especial (NO son CNSC) ---
// Estas convocatorias usan INTRO-00-PGN en vez de INTRO-00.
// Agregar aquí futuros concursos de régimen especial (Contraloría, Defensoría, etc.)
const CONVOCATORIAS_PGN = ["procuraduria-2026"];

/** Determina si una convocatoria es de la PGN (régimen especial). */
function esPGN(convocatoriaId: string | null | undefined): boolean {
  if (!convocatoriaId) return false;
  const norm = convocatoriaId.toLowerCase().trim();
  return CONVOCATORIAS_PGN.includes(norm) || norm.includes("procuraduria");
}


/**
 * "Conoce tu entidad" (CNSC) según la convocatoria: busca por nombre/entidad.
 * Devuelve el código ENT-* de la biblioteca o null si esa entidad no tiene guía.
 */
const ENTIDADES_CNSC: Array<{ patron: RegExp; codigo: string; titulo: string }> = [
  { patron: /\bdian\b|impuestos y aduanas/i, codigo: "ENT-DIAN-01", titulo: "Conoce tu Entidad: DIAN" },
  { patron: /\burt\b|restituci[oó]n de tierras/i, codigo: "ENT-URT-01", titulo: "Conoce tu Entidad: Unidad de Restitución de Tierras (URT)" },
  { patron: /hospital|huh|hernando moncaleano/i, codigo: "ENT-HUH-01", titulo: "Conoce tu Entidad: Hospital Universitario Hernando Moncaleano Perdomo" },
  { patron: /indervalle|inderval/i, codigo: "ENT-IDV-01", titulo: "Conoce tu Entidad: INDERVALLE" },
];

export function entidadCNSCDeConvocatoria(texto: string): { codigo: string; titulo: string } | null {
  for (const e of ENTIDADES_CNSC) if (e.patron.test(texto)) return { codigo: e.codigo, titulo: e.titulo };
  return null;
}

/**
 * Guías ADICIONALES propias de una entidad CNSC (además de "Conoce tu entidad").
 * DIAN: ponderaciones y puntaje (Día 1) + estrategia de tiempo y prueba de integridad (bonus).
 */
export function extrasDeEntidad(codigoEntidad?: string | null): Array<{ codigo: string; dia: number | null; titulo: string; tipo: string; orden: number }> {
  if (codigoEntidad === "ENT-DIAN-01") {
    return [
      { codigo: "DIAN-PON-01", dia: 1, titulo: "Cómo se califica tu prueba: ponderaciones y puntaje", tipo: "general", orden: 2 },
      { codigo: "DIAN-EST-01", dia: null, titulo: "Estrategia de tiempo y manejo de la prueba escrita (Bonus)", tipo: "bonus", orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, titulo: "Código de Integridad y prueba de integridad (Bonus)", tipo: "bonus", orden: 103 },
    ];
  }
  return [];
}

/** Lee nombre/entidad de la convocatoria (por uuid) y dice si es PGN y cuál es su guía de entidad. */
export async function infoConvocatoria(supabase: SupabaseClient, convocatoriaId?: string | null) {
  let texto = (convocatoriaId || "").toString();
  if (convocatoriaId) {
    const { data } = await supabase.from("convocatorias").select("nombre, entidad").eq("id", convocatoriaId).maybeSingle();
    if (data) texto = `${(data as any).nombre || ""} ${(data as any).entidad || ""}`;
  }
  const esPgn = /procuradur/i.test(texto) || esPGN(convocatoriaId);
  return { texto, esPgn, entidad: esPgn ? null : entidadCNSCDeConvocatoria(texto) };
}

// Definición de las guías que se auto-cargan según el nivel
const GUIAS_GENERALES = [
  { codigo: "GEN-01", dia: 2, titulo: "Estado y Función Pública", tipo: "general", orden: 2 },
  { codigo: "GEN-02", dia: 3, titulo: "Relación Estado-Ciudadano", tipo: "general", orden: 3 },
  { codigo: "GEN-03", dia: 4, titulo: "Marco Institucional", tipo: "general", orden: 4 },
];

// Intro varía según el tipo de concurso
const INTRO_CNSC = { codigo: "INTRO-00", dia: 1, titulo: "Presentación del Curso y la CNSC", tipo: "general", orden: 1 };
const INTRO_PGN = { codigo: "INTRO-00-PGN", dia: 1, titulo: "Presentación del Curso y el Concurso de la Procuraduría", tipo: "general", orden: 1 };

const GUIAS_POR_NIVEL: Record<string, Array<{ codigo: string; dia: number; titulo: string; tipo: string; orden: number }>> = {
  asistencial: [
    { codigo: "ASI-COM-01", dia: 5, titulo: "Cumplimiento y Desarrollo Laboral (Nivel Asistencial)", tipo: "nivel", orden: 5 },
    { codigo: "ASI-COM-02", dia: 6, titulo: "Atención y Colaboración en el Servicio Público (Nivel Asistencial)", tipo: "nivel", orden: 6 },
    { codigo: "ASI-ESP-01", dia: 7, titulo: "Competencias del Nivel Asistencial", tipo: "nivel", orden: 7 },
    { codigo: "ASI-ESP-02", dia: 8, titulo: "Alcance del Cargo Asistencial", tipo: "nivel", orden: 8 },
  ],
  tecnico: [
    { codigo: "TEC-COM-01", dia: 5, titulo: "Desempeño Individual y Cumplimiento Institucional (Nivel Técnico)", tipo: "nivel", orden: 5 },
    { codigo: "TEC-COM-02", dia: 6, titulo: "Relación con Usuarios y Trabajo Colaborativo (Nivel Técnico)", tipo: "nivel", orden: 6 },
    { codigo: "TEC-ESP-01", dia: 7, titulo: "Competencias del Nivel Técnico", tipo: "nivel", orden: 7 },
    { codigo: "TEC-ESP-02", dia: 8, titulo: "Alcance del Cargo Técnico", tipo: "nivel", orden: 8 },
  ],
  profesional: [
    { codigo: "PRO-COM-01", dia: 5, titulo: "Gestión Profesional y Cumplimiento Institucional (Nivel Profesional)", tipo: "nivel", orden: 5 },
    { codigo: "PRO-COM-02", dia: 6, titulo: "Servicio al Ciudadano y Articulación Institucional (Nivel Profesional)", tipo: "nivel", orden: 6 },
    { codigo: "PRO-ESP-01", dia: 7, titulo: "Competencias del Nivel Profesional", tipo: "nivel", orden: 7 },
    { codigo: "PRO-ESP-02", dia: 8, titulo: "Alcance del Cargo Profesional", tipo: "nivel", orden: 8 },
  ],
};

// Comportamentales DIAN por nivel (Días 5-8). La DIAN usa su propio Diccionario de
// Competencias Comportamentales (Resolución 065 de 2024), distinto del marco general
// del Decreto 815 de 2018; por eso sus cursos cargan este set y no el genérico CNSC.
// Son guías genéricas por nivel (sirven para cualquier cargo de ese nivel en la DIAN):
// así solo hay que construir las funcionales (Días 9-20) y el simulacro de cada cargo.
const GUIAS_POR_NIVEL_DIAN: Record<string, Array<{ codigo: string; dia: number; titulo: string; tipo: string; orden: number }>> = {
  asistencial: [
    { codigo: "DIAN-NIV-ASI-01", dia: 5, titulo: "Comportamiento ético y adaptabilidad (nivel asistencial DIAN)", tipo: "nivel", orden: 5 },
    { codigo: "DIAN-NIV-ASI-02", dia: 6, titulo: "Comunicación efectiva y trabajo en equipo (nivel asistencial DIAN)", tipo: "nivel", orden: 6 },
    { codigo: "DIAN-NIV-ASI-03", dia: 7, titulo: "Orientación al logro y al usuario y al ciudadano (nivel asistencial DIAN)", tipo: "nivel", orden: 7 },
    { codigo: "DIAN-NIV-ASI-04", dia: 8, titulo: "Tu ficha, innovación, solución de problemas y cómo se evalúa (nivel asistencial DIAN)", tipo: "nivel", orden: 8 },
  ],
  tecnico: [
    { codigo: "DIAN-NIV-TEC-01", dia: 5, titulo: "Comportamiento ético y adaptabilidad (nivel técnico DIAN)", tipo: "nivel", orden: 5 },
    { codigo: "DIAN-NIV-TEC-02", dia: 6, titulo: "Comunicación efectiva y trabajo en equipo (nivel técnico DIAN)", tipo: "nivel", orden: 6 },
    { codigo: "DIAN-NIV-TEC-03", dia: 7, titulo: "Orientación al logro, al usuario y al ciudadano e innovación (nivel técnico DIAN)", tipo: "nivel", orden: 7 },
    { codigo: "DIAN-NIV-TEC-04", dia: 8, titulo: "Tu ficha, innovación, solución de problemas y cómo se evalúa (nivel técnico DIAN)", tipo: "nivel", orden: 8 },
  ],
  profesional: [
    { codigo: "DIAN-NIV-PRO-01", dia: 5, titulo: "Comportamiento ético y adaptabilidad (nivel profesional DIAN)", tipo: "nivel", orden: 5 },
    { codigo: "DIAN-NIV-PRO-02", dia: 6, titulo: "Comunicación efectiva y trabajo en equipo (nivel profesional DIAN)", tipo: "nivel", orden: 6 },
    { codigo: "DIAN-NIV-PRO-03", dia: 7, titulo: "Orientación al logro y al usuario y al ciudadano (nivel profesional DIAN)", tipo: "nivel", orden: 7 },
    { codigo: "DIAN-NIV-PRO-04", dia: 8, titulo: "Tu ficha, innovación, solución de problemas y cómo se evalúa (nivel profesional DIAN)", tipo: "nivel", orden: 8 },
  ],
};

/** Guías por nivel (Días 5-8) según la entidad: la DIAN tiene su propio set. */
export function guiasNivelPara(nivelNorm: string, codigoEntidad?: string | null) {
  if (codigoEntidad === "ENT-DIAN-01" && GUIAS_POR_NIVEL_DIAN[nivelNorm]) return GUIAS_POR_NIVEL_DIAN[nivelNorm];
  return GUIAS_POR_NIVEL[nivelNorm] || [];
}

const GUIAS_BONUS = [
  { codigo: "BON-01", dia: null, titulo: "Estrategia CNSC (Bonus)", tipo: "bonus", orden: 100 },
  { codigo: "BON-02", dia: null, titulo: "Ofimática (Bonus)", tipo: "bonus", orden: 101 },
];

/**
 * PLANTILLAS DE PLAN COMPLETO por cargo/curso.
 *
 * Cada plantilla lista, por CÓDIGO de la biblioteca, TODAS las guías de un plan
 * de estudio de 21 días (intro + entidad + generales + nivel + funcionales +
 * simulacro) con su día. El admin arma el curso completo con un clic desde el
 * panel (server action `armarPlanPlantilla`), que resuelve cada código contra
 * el catálogo (biblioteca.json) y lo inserta en `guias_curso` sin duplicar.
 *
 * Ventaja: no se hardcodean rutas ni títulos aquí (eso vive en biblioteca.json);
 * solo la correspondencia código→día del plan. Para un cargo nuevo, se agrega
 * una entrada aquí con la lista de códigos y sus días.
 */
export interface ItemPlanPlantilla { codigo: string; dia: number | null; orden?: number }
export interface PlanPlantilla {
  id: string;
  nombre: string;
  /** Duración del curso en días: 21 (regular, por defecto) o 15 (intensivo). */
  duracion?: 21 | 15;
  guias: ItemPlanPlantilla[];
}

export const PLANES_PLANTILLA: Record<string, PlanPlantilla> = {
  // Procuraduría General de la Nación — Auxiliar Administrativo (5AM-10), Convocatoria 242-2026.
  "pgn-auxiliar-administrativo": {
    id: "pgn-auxiliar-administrativo",
    nombre: "PGN · Auxiliar Administrativo (5AM-10) — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-AUX", dia: 1 },
      { codigo: "ENT-PGN-AUX-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-AUX", dia: 2 },
      { codigo: "GEN-02-PGN-AUX", dia: 3 },
      { codigo: "GEN-03-PGN-AUX", dia: 4 },
      { codigo: "ASI-PGN-AUX-01", dia: 5 },
      { codigo: "ASI-PGN-AUX-02", dia: 6 },
      { codigo: "ASI-PGN-AUX-03", dia: 7 },
      { codigo: "ASI-PGN-AUX-04", dia: 8 },
      { codigo: "FUN-GDOC-AUX-01", dia: 9 },
      { codigo: "FUN-GDOC-AUX-02", dia: 10 },
      { codigo: "FUN-OFI-AUX-01", dia: 11 },
      { codigo: "FUN-OFI-AUX-02", dia: 12 },
      { codigo: "FUN-ATC-AUX-01", dia: 13 },
      { codigo: "FUN-ALM-AUX-01", dia: 14 },
      { codigo: "FUN-ALM-AUX-02", dia: 15 },
      { codigo: "FUN-PGN-AUX-01", dia: 16 },
      { codigo: "FUN-GP-AUX-01", dia: 17 },
      { codigo: "FUN-MIPG-AUX-01", dia: 18 },
      { codigo: "FUN-TRANS-AUX-01", dia: 19 },
      { codigo: "FUN-CONST-AUX-01", dia: 20 },
      { codigo: "SIM-PGN-5AM10-001", dia: 21 },
    ],
  },

  // Procuraduría General de la Nación — Profesional Universitario (3PU-15), Convocatoria 112-2026.
  // Perfil financiero-contable · Dirección Nacional de Investigaciones Especiales.
  "pgn-profesional-3pu15": {
    id: "pgn-profesional-3pu15",
    nombre: "PGN · Profesional Universitario (3PU-15) — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-PU15", dia: 1 },
      { codigo: "ENT-PGN-PU-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-PU15", dia: 2 },
      { codigo: "GEN-02-PGN-PU15", dia: 3 },
      { codigo: "GEN-03-PGN-PU15", dia: 4 },
      { codigo: "FUN-PU15-COM-01", dia: 5 },
      { codigo: "FUN-PU15-COM-02", dia: 6 },
      { codigo: "FUN-PU15-COM-03", dia: 7 },
      { codigo: "FUN-PU15-COM-04", dia: 8 },
      { codigo: "FUN-PGN-PU15-01", dia: 9 },
      { codigo: "FUN-GP-PU15-01", dia: 10 },
      { codigo: "FUN-CONST-PU15-01", dia: 11 },
      { codigo: "FUN-DIS-PU15-01", dia: 12 },
      { codigo: "FUN-JUR-PU15-01", dia: 13 },
      { codigo: "FUN-CONT-PU15-01", dia: 14 },
      { codigo: "FUN-PPTO-PU15-01", dia: 15 },
      { codigo: "FUN-CPUB-PU15-01", dia: 16 },
      { codigo: "FUN-FINP-PU15-01", dia: 17 },
      { codigo: "FUN-PJUD-PU15-01", dia: 18 },
      { codigo: "FUN-ANTIC-PU15-01", dia: 19 },
      { codigo: "FUN-MIPG-PU15-01", dia: 20 },
      { codigo: "SIM-PGN-3PU15-001", dia: 21 },
    ],
  },
  "pgn-asesor-1as19": {
    id: "pgn-asesor-1as19",
    nombre: "PGN · Asesor (1AS-19) — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-1AS19", dia: 1 },
      { codigo: "ENT-PGN-PU-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-1AS19", dia: 2 },
      { codigo: "GEN-02-PGN-1AS19", dia: 3 },
      { codigo: "GEN-03-PGN-1AS19", dia: 4 },
      { codigo: "1AS19-COM-01", dia: 5 },
      { codigo: "1AS19-COM-02", dia: 6 },
      { codigo: "1AS19-COM-03", dia: 7 },
      { codigo: "1AS19-COM-04", dia: 8 },
      { codigo: "FUN-PGN-1AS19-01", dia: 9 },
      { codigo: "FUN-GP-1AS19-01", dia: 10 },
      { codigo: "FUN-CONST-1AS19-01", dia: 11 },
      { codigo: "FUN-DIS-1AS19-01", dia: 12 },
      { codigo: "FUN-DIS-1AS19-02", dia: 13 },
      { codigo: "FUN-JUR-1AS19-01", dia: 14 },
      { codigo: "FUN-PROB-1AS19-01", dia: 15 },
      { codigo: "FUN-CONT-1AS19-01", dia: 16 },
      { codigo: "FUN-ANTIC-1AS19-01", dia: 17 },
      { codigo: "FUN-OT-1AS19-01", dia: 18 },
      { codigo: "FUN-PREV-1AS19-01", dia: 19 },
      { codigo: "FUN-MIPG-1AS19-01", dia: 20 },
      { codigo: "SIM-PGN-1AS19-001", dia: 21 },
    ],
  },

  "pgn-asesor-1as19-nathaly": {
    id: "pgn-asesor-1as19-nathaly",
    nombre: "PGN · Asesor (1AS-19) Despacho Procurador General (Conv. 02-2026) — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-1AS19N", dia: 1 },
      { codigo: "ENT-PGN-PU-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-1AS19N", dia: 2 },
      { codigo: "GEN-02-PGN-1AS19N", dia: 3 },
      { codigo: "GEN-03-PGN-1AS19N", dia: 4 },
      { codigo: "1AS19N-COM-01", dia: 5 },
      { codigo: "1AS19N-COM-02", dia: 6 },
      { codigo: "1AS19N-COM-03", dia: 7 },
      { codigo: "1AS19N-COM-04", dia: 8 },
      { codigo: "FUN-PGN-1AS19N-01", dia: 9 },
      { codigo: "FUN-GP-1AS19N-01", dia: 10 },
      { codigo: "FUN-CONST-1AS19N-01", dia: 11 },
      { codigo: "FUN-LEG-1AS19N-01", dia: 12 },
      { codigo: "FUN-JUR-1AS19N-01", dia: 13 },
      { codigo: "FUN-MP-1AS19N-01", dia: 14 },
      { codigo: "FUN-PREV-1AS19N-01", dia: 15 },
      { codigo: "FUN-CONT-1AS19N-01", dia: 16 },
      { codigo: "FUN-ANTIC-1AS19N-01", dia: 17 },
      { codigo: "FUN-PLAN-1AS19N-01", dia: 18 },
      { codigo: "FUN-ELEC-1AS19N-01", dia: 19 },
      { codigo: "FUN-COOP-1AS19N-01", dia: 20 },
      { codigo: "SIM-PGN-1AS19N-001", dia: 21 },
    ],
  },
  "pgn-profesional-3pu17-valentina": {
    id: "pgn-profesional-3pu17-valentina",
    nombre: "PGN · Profesional Universitario (3PU-17) Funciones Mixtas (Conv. 144-2026) — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-3PU17V", dia: 1 },
      { codigo: "ENT-PGN-PU-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-3PU17V", dia: 2 },
      { codigo: "GEN-02-PGN-3PU17V", dia: 3 },
      { codigo: "GEN-03-PGN-3PU17V", dia: 4 },
      { codigo: "3PU17V-COM-01", dia: 5 },
      { codigo: "3PU17V-COM-02", dia: 6 },
      { codigo: "3PU17V-COM-03", dia: 7 },
      { codigo: "3PU17V-COM-04", dia: 8 },
      { codigo: "FUN-PGN-3PU17V-01", dia: 9 },
      { codigo: "FUN-GP-3PU17V-01", dia: 10 },
      { codigo: "FUN-CONST-3PU17V-01", dia: 11 },
      { codigo: "FUN-DIS-3PU17V-01", dia: 12 },
      { codigo: "FUN-DIS-3PU17V-02", dia: 13 },
      { codigo: "FUN-MP-3PU17V-01", dia: 14 },
      { codigo: "FUN-CONC-3PU17V-01", dia: 15 },
      { codigo: "FUN-JUR-3PU17V-01", dia: 16 },
      { codigo: "FUN-PROB-3PU17V-01", dia: 17 },
      { codigo: "FUN-CONT-3PU17V-01", dia: 18 },
      { codigo: "FUN-ANTIC-3PU17V-01", dia: 19 },
      { codigo: "FUN-PREV-3PU17V-01", dia: 20 },
      { codigo: "SIM-PGN-3PU17V-001", dia: 21 },
    ],
  },

  // Procuraduría General de la Nación — Secretario Procuraduría (4SP-13), Convocatoria 283-2026.
  // Nivel Técnico · apoyo secretarial (trámite, notificaciones, archivo) — Carolina Rueda Rodríguez.
  "pgn-secretario-4sp13": {
    id: "pgn-secretario-4sp13",
    nombre: "PGN · Secretario Procuraduría (4SP-13), Conv. 283-2026 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-4SP13", dia: 1 },
      { codigo: "ENT-PGN-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-4SP13", dia: 2 },
      { codigo: "GEN-02-PGN-4SP13", dia: 3 },
      { codigo: "GEN-03-PGN-4SP13", dia: 4 },
      { codigo: "4SP13-COM-01", dia: 5 },
      { codigo: "4SP13-COM-02", dia: 6 },
      { codigo: "4SP13-COM-03", dia: 7 },
      { codigo: "4SP13-COM-04", dia: 8 },
      { codigo: "FUN-PGN-TEC-01", dia: 9 },
      { codigo: "FUN-GP-TEC-01", dia: 10 },
      { codigo: "FUN-CONST-TEC-01", dia: 11 },
      { codigo: "FUN-MP-TEC-01", dia: 12 },
      { codigo: "FUN-DIS-TEC-01", dia: 13 },
      { codigo: "FUN-OFI-TEC-01", dia: 14 },
      { codigo: "FUN-OFI-TEC-02", dia: 15 },
      { codigo: "FUN-GDOC-TEC-01", dia: 16 },
      { codigo: "FUN-GDOC-TEC-02", dia: 17 },
      { codigo: "FUN-ATC-TEC-01", dia: 18 },
      { codigo: "FUN-MIPG-TEC-01", dia: 19 },
      { codigo: "FUN-TRANS-TEC-01", dia: 20 },
      { codigo: "SIM-PGN-4SP13-001", dia: 21 },
    ],
  },

  // Procuraduría General de la Nación — Secretario Procuraduría (4SP-12), Convocatoria 291-2026.
  // Nivel Técnico · apoyo secretarial (trámite, notificaciones, archivo) — Humberto José Jiménez Ramírez.
  // Mismo rol/nivel/competencias que "pgn-secretario-4sp13"; solo cambia código, convocatoria,
  // salario, plazas, dependencias iniciales y que este cargo NO exige experiencia.
  "pgn-secretario-4sp12": {
    id: "pgn-secretario-4sp12",
    nombre: "PGN · Secretario Procuraduría (4SP-12), Conv. 291-2026 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-4SP12", dia: 1 },
      { codigo: "ENT-PGN-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-4SP12", dia: 2 },
      { codigo: "GEN-02-PGN-4SP12", dia: 3 },
      { codigo: "GEN-03-PGN-4SP12", dia: 4 },
      { codigo: "4SP12-COM-01", dia: 5 },
      { codigo: "4SP12-COM-02", dia: 6 },
      { codigo: "4SP12-COM-03", dia: 7 },
      { codigo: "4SP12-COM-04", dia: 8 },
      { codigo: "FUN-PGN-TEC-01", dia: 9 },
      { codigo: "FUN-GP-TEC-01", dia: 10 },
      { codigo: "FUN-CONST-TEC-01", dia: 11 },
      { codigo: "FUN-MP-TEC-01", dia: 12 },
      { codigo: "FUN-DIS-TEC-01", dia: 13 },
      { codigo: "FUN-OFI-TEC-01", dia: 14 },
      { codigo: "FUN-OFI-TEC-02", dia: 15 },
      { codigo: "FUN-GDOC-TEC-01", dia: 16 },
      { codigo: "FUN-GDOC-TEC-02", dia: 17 },
      { codigo: "FUN-ATC-TEC-01", dia: 18 },
      { codigo: "FUN-MIPG-TEC-01", dia: 19 },
      { codigo: "FUN-TRANS-TEC-01", dia: 20 },
      { codigo: "SIM-PGN-4SP12-001", dia: 21 },
    ],
  },

  // Procuraduría General de la Nación — Sustanciador (4SU-11), Convocatoria 288-2026.
  // Nivel Técnico · apoya en la proyección de conceptos, providencias, solicitudes,
  // constancias y recursos bajo supervisión del jefe de despacho (NO decide ni firma) —
  // Yinit Yulieth Ursola Meza. A diferencia de Secretario Procuraduría (4SP-12/4SP-13),
  // este cargo SÍ redacta borradores sustantivos, por lo que ninguna guía se comparte
  // con esos cursos: las 21 piezas son propias de este plan (ver
  // referencias/_SPEC-CURSO-4SU11-YINIT.md).
  "pgn-sustanciador-4su11": {
    id: "pgn-sustanciador-4su11",
    nombre: "PGN · Sustanciador (4SU-11), Conv. 288-2026 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-4SU11", dia: 1 },
      { codigo: "ENT-PGN-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-4SU11", dia: 2 },
      { codigo: "GEN-02-PGN-4SU11", dia: 3 },
      { codigo: "GEN-03-PGN-4SU11", dia: 4 },
      { codigo: "4SU11-COM-01", dia: 5 },
      { codigo: "4SU11-COM-02", dia: 6 },
      { codigo: "4SU11-COM-03", dia: 7 },
      { codigo: "4SU11-COM-04", dia: 8 },
      { codigo: "FUN-SUS-4SU11-01", dia: 9 },
      { codigo: "FUN-SUS-4SU11-02", dia: 10 },
      { codigo: "FUN-SUS-4SU11-03", dia: 11 },
      { codigo: "FUN-JUR-4SU11-01", dia: 12 },
      { codigo: "FUN-JUR-4SU11-02", dia: 13 },
      { codigo: "FUN-CONC-4SU11-01", dia: 14 },
      { codigo: "FUN-DIS-4SU11-01", dia: 15 },
      { codigo: "FUN-DIS-4SU11-02", dia: 16 },
      { codigo: "FUN-MP-4SU11-01", dia: 17 },
      { codigo: "FUN-GDOC-4SU11-01", dia: 18 },
      { codigo: "FUN-OFI-4SU11-01", dia: 19 },
      { codigo: "FUN-ATC-4SU11-01", dia: 20 },
      { codigo: "SIM-PGN-4SU11-001", dia: 21 },
    ],
  },

  // Procuraduría General de la Nación — Citador (6CI-04), Convocatoria 90-2026.
  // Nivel Asistencial/Operativo · apoyo operativo puro de correspondencia,
  // notificación, diligencias externas y archivo básico (NO decide, NO firma,
  // NO administra inventarios/almacén de bienes) — Ingrid Vanessa Angulo Prado.
  // Competencias comportamentales distintas a todos los cargos previos
  // (Responsabilidad C, Organización C, Orientación al Usuario B, Cumplimiento D,
  // Gestión de Recursos D) y sin conocimientos esenciales comunes (ver
  // referencias/_SPEC-CURSO-6CI04-INGRID.md). Ninguna guía se comparte con el
  // curso de Auxiliar Administrativo (5AM-10): todas las piezas son propias.
  "pgn-citador-6ci04": {
    id: "pgn-citador-6ci04",
    nombre: "PGN · Citador (6CI-04), Conv. 90-2026 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-6CI04", dia: 1 },
      { codigo: "ENT-PGN-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-6CI04", dia: 2 },
      { codigo: "GEN-02-PGN-6CI04", dia: 3 },
      { codigo: "GEN-03-PGN-6CI04", dia: 4 },
      { codigo: "6CI04-COM-01", dia: 5 },
      { codigo: "6CI04-COM-02", dia: 6 },
      { codigo: "6CI04-COM-03", dia: 7 },
      { codigo: "6CI04-COM-04", dia: 8 },
      { codigo: "FUN-COR-6CI04-01", dia: 9 },
      { codigo: "FUN-DIL-6CI04-01", dia: 10 },
      { codigo: "FUN-NOT-6CI04-01", dia: 11 },
      { codigo: "FUN-COR-6CI04-02", dia: 12 },
      { codigo: "FUN-GDOC-6CI04-01", dia: 13 },
      { codigo: "FUN-GDOC-6CI04-02", dia: 14 },
      { codigo: "FUN-ENT-6CI04-01", dia: 15 },
      { codigo: "FUN-SIS-6CI04-01", dia: 16 },
      { codigo: "FUN-ATC-6CI04-01", dia: 17 },
      { codigo: "FUN-PGN-6CI04-01", dia: 18 },
      { codigo: "FUN-GDOC-6CI04-03", dia: 19 },
      { codigo: "FUN-OFI-6CI04-01", dia: 20 },
      { codigo: "SIM-PGN-6CI04-001", dia: 21 },
    ],
  },
  "pgn-tecnico-administrativo-4tm16": {
    id: "pgn-tecnico-administrativo-4tm16",
    nombre: "PGN · Técnico Administrativo (4TM-16), Conv. 245-2026 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00-PGN-4TM16", dia: 1 },
      { codigo: "ENT-PGN-01", dia: 1, orden: 1 },
      { codigo: "GEN-01-PGN-4TM16", dia: 2 },
      { codigo: "GEN-02-PGN-4TM16", dia: 3 },
      { codigo: "GEN-03-PGN-4TM16", dia: 4 },
      { codigo: "4TM16-COM-01", dia: 5 },
      { codigo: "4TM16-COM-02", dia: 6 },
      { codigo: "4TM16-COM-03", dia: 7 },
      { codigo: "4TM16-COM-04", dia: 8 },
      { codigo: "FUN-DOC-4TM16-01", dia: 9 },
      { codigo: "FUN-SIS-4TM16-01", dia: 10 },
      { codigo: "FUN-INF-4TM16-01", dia: 11 },
      { codigo: "FUN-CAP-4TM16-01", dia: 12 },
      { codigo: "FUN-PLAN-4TM16-01", dia: 13 },
      { codigo: "FUN-OFI-4TM16-01", dia: 14 },
      { codigo: "FUN-APO-4TM16-01", dia: 15 },
      { codigo: "FUN-ADM-4TM16-01", dia: 16 },
      { codigo: "FUN-SEG-4TM16-01", dia: 17 },
      { codigo: "FUN-DIS-4TM16-01", dia: 18 },
      { codigo: "FUN-ATC-4TM16-01", dia: 19 },
      { codigo: "FUN-PGN-4TM16-01", dia: 20 },
      { codigo: "SIM-PGN-4TM16-001", dia: 21 },
    ],
  },
  "dian-gestor-ii-aduanas": {
    id: "dian-gestor-ii-aduanas",
    nombre: "DIAN · Gestor II (302-02, operación aduanera), concurso DIAN 2676 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-ADU-COM-01", dia: 5 },
      { codigo: "DIAN-ADU-COM-02", dia: 6 },
      { codigo: "DIAN-ADU-COM-03", dia: 7 },
      { codigo: "DIAN-ADU-COM-04", dia: 8 },
      { codigo: "FUN-ADU-01", dia: 9 },
      { codigo: "FUN-ADU-02", dia: 10 },
      { codigo: "FUN-ADU-03", dia: 11 },
      { codigo: "FUN-ADU-04", dia: 12 },
      { codigo: "FUN-ADU-05", dia: 13 },
      { codigo: "FUN-ADU-06", dia: 14 },
      { codigo: "FUN-ADU-07", dia: 15 },
      { codigo: "FUN-ADU-08", dia: 16 },
      { codigo: "FUN-ADU-09", dia: 17 },
      { codigo: "FUN-ADU-JUR-01", dia: 18 },
      { codigo: "FUN-ADU-MIPG-01", dia: 19 },
      { codigo: "FUN-ADU-DOC-01", dia: 20 },
      { codigo: "SIM-DIAN-ADU-001", dia: 21 },
      { codigo: "BON-01", dia: null, orden: 100 },
      { codigo: "BON-02", dia: null, orden: 101 },
      { codigo: "DIAN-EST-01", dia: null, orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, orden: 103 },
    ],
  },
  // DIAN — Gestor I (301-01), Fiscalización y Liquidación, concurso DIAN 2676.
  // Eje del manual: determinación y control tributario, régimen cambiario,
  // fiscalización internacional y fiscalización aduanera + básicas (ver
  // referencias/_SPEC-CURSO-GESTOR1-ANDREA.md).
  "dian-gestor-i-fiscalizacion": {
    id: "dian-gestor-i-fiscalizacion",
    nombre: "DIAN · Gestor I (301-01, fiscalización y liquidación), concurso DIAN 2676 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-PRO-COM-01", dia: 5 },
      { codigo: "DIAN-PRO-COM-02", dia: 6 },
      { codigo: "DIAN-PRO-COM-03", dia: 7 },
      { codigo: "DIAN-PRO-COM-04", dia: 8 },
      { codigo: "FUN-DIAN-01", dia: 9 },
      { codigo: "FUN-DIAN-02", dia: 10 },
      { codigo: "FUN-DIAN-03", dia: 11 },
      { codigo: "FUN-DIAN-04", dia: 12 },
      { codigo: "FUN-DIAN-05", dia: 13 },
      { codigo: "FUN-DIAN-06", dia: 14 },
      { codigo: "FUN-DIAN-07", dia: 15 },
      { codigo: "FUN-DIAN-08", dia: 16 },
      { codigo: "FUN-DIAN-JUR-01", dia: 17 },
      { codigo: "FUN-MIPG-01", dia: 18 },
      { codigo: "FUN-DOC-01", dia: 19 },
      { codigo: "FUN-DIAN-09", dia: 20 },
      { codigo: "SIM-DIAN-001", dia: 21 },
      { codigo: "BON-01", dia: null, orden: 100 },
      { codigo: "BON-02", dia: null, orden: 101 },
      { codigo: "DIAN-EST-01", dia: null, orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, orden: 103 },
    ],
  },
  "dian-gestor-iii-recursos-administrativos": {
    id: "dian-gestor-iii-recursos-administrativos",
    nombre: "DIAN · Gestor III (303-03, Recursos Administrativos), concurso DIAN 2676, OPEC 236745 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-PRO-COM-01", dia: 5 },
      { codigo: "DIAN-PRO-COM-02", dia: 6 },
      { codigo: "DIAN-PRO-COM-03", dia: 7 },
      { codigo: "DIAN-PRO-COM-GIII-04", dia: 8 },
      { codigo: "FUN-RADM-01", dia: 9 },
      { codigo: "FUN-RADM-02", dia: 10 },
      { codigo: "FUN-RADM-03", dia: 11 },
      { codigo: "FUN-RADM-04", dia: 12 },
      { codigo: "FUN-RADM-05", dia: 13 },
      { codigo: "FUN-RADM-06", dia: 14 },
      { codigo: "FUN-RADM-07", dia: 15 },
      { codigo: "FUN-RADM-08", dia: 16 },
      { codigo: "FUN-RADM-09", dia: 17 },
      { codigo: "FUN-RADM-10", dia: 18 },
      { codigo: "FUN-RADM-11", dia: 19 },
      { codigo: "FUN-RADM-12", dia: 20 },
      { codigo: "SIM-DIAN-GIII-001", dia: 21 },
      { codigo: "DIAN-EST-01", dia: null, orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, orden: 103 },
    ],
  },
  // DIAN — Analista I (nivel Técnico), concurso DIAN 2676, OPEC 246932 — Syndy Carolina Perilla Moreno.
  // Eje del manual: GESTIÓN DE INFORMACIÓN y soporte técnico (NO fiscaliza, NO liquida,
  // NO decide de fondo, NO administra infraestructura). Comportamentales propias
  // -TEC-COM (nivel Técnico, reenfocadas del molde -PRO-COM del nivel Profesional,
  // con 0 fugas) y funcionales propias FUN-AINF (ver referencias/_SPEC-CURSO-DIAN-ANALISTA-I-SYNDY.md).
  "dian-analista-i": {
    id: "dian-analista-i",
    nombre: "DIAN · Analista I (Técnico, gestión de información), concurso DIAN 2676, OPEC 246932 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-TEC-COM-01", dia: 5 },
      { codigo: "DIAN-TEC-COM-02", dia: 6 },
      { codigo: "DIAN-TEC-COM-03", dia: 7 },
      { codigo: "DIAN-TEC-COM-04", dia: 8 },
      { codigo: "FUN-AINF-01", dia: 9 },
      { codigo: "FUN-AINF-02", dia: 10 },
      { codigo: "FUN-AINF-03", dia: 11 },
      { codigo: "FUN-AINF-04", dia: 12 },
      { codigo: "FUN-AINF-05", dia: 13 },
      { codigo: "FUN-AINF-06", dia: 14 },
      { codigo: "FUN-AINF-07", dia: 15 },
      { codigo: "FUN-AINF-08", dia: 16 },
      { codigo: "FUN-AINF-09", dia: 17 },
      { codigo: "FUN-AINF-10", dia: 18 },
      { codigo: "FUN-AINF-11", dia: 19 },
      { codigo: "FUN-AINF-12", dia: 20 },
      { codigo: "SIM-DIAN-AI-001", dia: 21 },
      { codigo: "BON-01", dia: null, orden: 100 },
      { codigo: "BON-02", dia: null, orden: 101 },
      { codigo: "DIAN-EST-01", dia: null, orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, orden: 103 },
    ],
  },

  // DIAN 2676 — Gestor I, Talento Humano (OPEC 236897).
  "dian-gestor-i-talento-humano-236897": {
    id: "dian-gestor-i-talento-humano-236897",
    nombre: "DIAN · Gestor I, Talento Humano (OPEC 236897) — plan personalizado de 21 días",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-GHI-COM-01", dia: 5 },
      { codigo: "DIAN-GHI-COM-02", dia: 6 },
      { codigo: "DIAN-GHI-COM-03", dia: 7 },
      { codigo: "DIAN-GHI-COM-04", dia: 8 },
      { codigo: "FUN-GHI-01", dia: 9 },
      { codigo: "FUN-GHI-02", dia: 10 },
      { codigo: "FUN-GHI-03", dia: 11 },
      { codigo: "FUN-GHI-04", dia: 12 },
      { codigo: "FUN-GHI-05", dia: 13 },
      { codigo: "FUN-GHI-06", dia: 14 },
      { codigo: "FUN-CONST-DIAN-GHI-01", dia: 15 },
      { codigo: "FUN-JUR-DIAN-GHI-01", dia: 16 },
      { codigo: "FUN-MIPG-DIAN-GHI-01", dia: 17 },
      { codigo: "FUN-GDOC-DIAN-GHI-01", dia: 18 },
      { codigo: "FUN-ATC-DIAN-GHI-01", dia: 19 },
      { codigo: "FUN-DIAN-GHI-INFO-01", dia: 20 },
      { codigo: "SIM-DIAN-GHI-001", dia: 21 },
    ],
  },
  // DIAN 2676 — Facilitador II, nivel asistencial (OPEC 236906).
  "dian-facilitador-ii-236906": {
    id: "dian-facilitador-ii-236906",
    nombre: "DIAN · Facilitador II (OPEC 236906) — plan personalizado de 21 días",
    guias: [
      { codigo: "INTRO-00-DIAN-FAC2", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01-DIAN-FAC2", dia: 2 },
      { codigo: "GEN-02-DIAN-FAC2", dia: 3 },
      { codigo: "GEN-03-DIAN-FAC2", dia: 4 },
      { codigo: "DIAN-ASI-COM-01", dia: 5 },
      { codigo: "DIAN-ASI-COM-02", dia: 6 },
      { codigo: "DIAN-ASI-COM-03", dia: 7 },
      { codigo: "DIAN-ASI-COM-04", dia: 8 },
      { codigo: "FUN-CONST-FAC2-01", dia: 9 },
      { codigo: "FUN-COR-FAC2-01", dia: 10 },
      { codigo: "FUN-GDOC-FAC2-01", dia: 11 },
      { codigo: "FUN-GDOC-FAC2-02", dia: 12 },
      { codigo: "FUN-GP-FAC2-01", dia: 13 },
      { codigo: "FUN-GDOC-FAC2-03", dia: 14 },
      { codigo: "FUN-COR-FAC2-02", dia: 15 },
      { codigo: "FUN-GP-FAC2-02", dia: 16 },
      { codigo: "FUN-DOC-FAC2-01", dia: 17 },
      { codigo: "FUN-CONST-FAC2-02", dia: 18 },
      { codigo: "FUN-COR-FAC2-03", dia: 19 },
      { codigo: "FUN-GDOC-FAC2-04", dia: 20 },
      { codigo: "SIM-DIAN-FAC2-001", dia: 21 },
    ],
  },

  // DIAN 2676 — Analista IV (204-04), nivel Técnico, Fiscalización y Liquidación (OPEC 236760)
  // Gloriela Paola Usuga. Mismas competencias funcionales que Gestor I 301-01 (determinación y
  // control tributario, régimen cambiario, fiscalización internacional y aduanera): reutiliza las
  // funcionales FUN-DIAN adaptadas al nivel técnico (-AIV) y comportamentales DIAN-AIV-COM.
  "dian-analista-iv-fiscalizacion-236760": {
    id: "dian-analista-iv-fiscalizacion-236760",
    nombre: "DIAN · Analista IV (204-04, fiscalización y liquidación), concurso DIAN 2676, OPEC 236760 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-AIV-COM-01", dia: 5 },
      { codigo: "DIAN-AIV-COM-02", dia: 6 },
      { codigo: "DIAN-AIV-COM-03", dia: 7 },
      { codigo: "DIAN-AIV-COM-04", dia: 8 },
      { codigo: "FUN-DIAN-01-AIV", dia: 9 },
      { codigo: "FUN-DIAN-02-AIV", dia: 10 },
      { codigo: "FUN-DIAN-03-AIV", dia: 11 },
      { codigo: "FUN-DIAN-04-AIV", dia: 12 },
      { codigo: "FUN-DIAN-05-AIV", dia: 13 },
      { codigo: "FUN-DIAN-06-AIV", dia: 14 },
      { codigo: "FUN-DIAN-07-AIV", dia: 15 },
      { codigo: "FUN-DIAN-08-AIV", dia: 16 },
      { codigo: "FUN-JUR-AIV-01", dia: 17 },
      { codigo: "FUN-MIPG-AIV-01", dia: 18 },
      { codigo: "FUN-DOC-AIV-01", dia: 19 },
      { codigo: "FUN-DIAN-09-AIV", dia: 20 },
      { codigo: "SIM-DIAN-AIV-001", dia: 21 },
      { codigo: "BON-01", dia: null, orden: 100 },
      { codigo: "BON-02", dia: null, orden: 101 },
      { codigo: "DIAN-EST-01", dia: null, orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, orden: 103 },
      { codigo: "BON-03", dia: null, orden: 104 },
    ],
  },
  "dian-analista-ii-fiscalizacion-236762": {
    id: "dian-analista-ii-fiscalizacion-236762",
    nombre: "DIAN · Analista II (202-02, fiscalización y liquidación), concurso DIAN 2676, OPEC 236762 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-AII-COM-01", dia: 5 },
      { codigo: "DIAN-AII-COM-02", dia: 6 },
      { codigo: "DIAN-AII-COM-03", dia: 7 },
      { codigo: "DIAN-AII-COM-04", dia: 1, orden: 3 },
      { codigo: "FUN-DIAN-01", dia: 8 },
      { codigo: "FUN-DIAN-02", dia: 9 },
      { codigo: "FUN-DIAN-03-AII", dia: 10 },
      { codigo: "FUN-AII-01", dia: 11 },
      { codigo: "FUN-DIAN-04", dia: 12 },
      { codigo: "FUN-DIAN-05-AII", dia: 13 },
      { codigo: "FUN-DIAN-06-AII", dia: 14 },
      { codigo: "FUN-DIAN-07-AII", dia: 15 },
      { codigo: "FUN-DIAN-08-AII", dia: 16 },
      { codigo: "FUN-JUR-AII-01", dia: 17 },
      { codigo: "FUN-MIPG-AII-01", dia: 18 },
      { codigo: "FUN-DOC-AII-01", dia: 19 },
      { codigo: "FUN-DIAN-09-AII", dia: 20 },
      { codigo: "SIM-DIAN-AII-001", dia: 21 },
      { codigo: "BON-01", dia: null, orden: 100 },
      { codigo: "BON-02", dia: null, orden: 101 },
      { codigo: "DIAN-EST-01", dia: null, orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, orden: 103 },
      { codigo: "BON-03", dia: null, orden: 104 },
      { codigo: "FUN-AII-02", dia: null, orden: 105 },
    ],
  },
  // DIAN — Gestor II (302-02), Administrativo y Financiero (recursos administrativos,
  // logística, compras y contratos), concurso DIAN 2676. Ver
  // referencias/_SPEC-CURSO-GESTOR2-ADMIN-EDWIN.md.
  "dian-gestor-ii-administrativo": {
    id: "dian-gestor-ii-administrativo",
    nombre: "DIAN · Gestor II (302-02, administrativo y financiero), concurso DIAN 2676 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-ADM-COM-01", dia: 5 },
      { codigo: "DIAN-ADM-COM-02", dia: 6 },
      { codigo: "DIAN-ADM-COM-03", dia: 7 },
      { codigo: "DIAN-ADM-COM-04", dia: 8 },
      { codigo: "FUN-ADM-01", dia: 9 },
      { codigo: "FUN-ADM-02", dia: 10 },
      { codigo: "FUN-ADM-03", dia: 11 },
      { codigo: "FUN-ADM-04", dia: 12 },
      { codigo: "FUN-ADM-05", dia: 13 },
      { codigo: "FUN-ADM-06", dia: 14 },
      { codigo: "FUN-ADM-12", dia: 15 },
      { codigo: "FUN-ADM-07", dia: 16 },
      { codigo: "FUN-ADM-09", dia: 17 },
      { codigo: "FUN-ADM-10", dia: 18 },
      { codigo: "FUN-ADM-11", dia: 19 },
      { codigo: "FUN-ADM-08", dia: 20 },
      { codigo: "SIM-DIAN-ADM-001", dia: 21 },
      { codigo: "BON-01", dia: null, orden: 100 },
      { codigo: "BON-02", dia: null, orden: 101 },
      { codigo: "DIAN-EST-01", dia: null, orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, orden: 103 },
    ],
  },
  // DIAN — Gestor II (302-02), Fiscalización y Liquidación, concurso DIAN 2676. Ver
  // referencias/_SPEC-CURSO-GESTOR2-FISCALIZACION-KAREN.md. Comparte las funcionales
  // FUN-DIAN-* con el plan del Gestor I.
  "dian-gestor-ii-fiscalizacion": {
    id: "dian-gestor-ii-fiscalizacion",
    nombre: "DIAN · Gestor II (302-02, fiscalización y liquidación), concurso DIAN 2676 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-FIS2-COM-01", dia: 5 },
      { codigo: "DIAN-FIS2-COM-02", dia: 6 },
      { codigo: "DIAN-FIS2-COM-03", dia: 7 },
      { codigo: "DIAN-FIS2-COM-04", dia: 1, orden: 3 },
      { codigo: "FUN-DIAN-01", dia: 8 },
      { codigo: "FUN-DIAN-02", dia: 9 },
      { codigo: "FUN-DIAN-03", dia: 10 },
      { codigo: "FUN-FIS2-01", dia: 11 },
      { codigo: "FUN-DIAN-04", dia: 12 },
      { codigo: "FUN-DIAN-05", dia: 13 },
      { codigo: "FUN-DIAN-06", dia: 14 },
      { codigo: "FUN-DIAN-07", dia: 15 },
      { codigo: "FUN-DIAN-08", dia: 16 },
      { codigo: "FUN-DIAN-JUR-01", dia: 17 },
      { codigo: "FUN-MIPG-01", dia: 18 },
      { codigo: "FUN-DOC-01", dia: 19 },
      { codigo: "FUN-DIAN-09", dia: 20 },
      { codigo: "SIM-DIAN-FIS2-001", dia: 21 },
      { codigo: "BON-01", dia: null, orden: 100 },
      { codigo: "BON-02", dia: null, orden: 101 },
      { codigo: "DIAN-EST-01", dia: null, orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, orden: 103 },
    ],
  },
  // DIAN 2676 — Gestor III, Control Interno (ficha PC-CI-3006), OPEC 236872 — Andrea Aroca.
  // Días 5-8: comportamentales genéricas DIAN nivel profesional (DIAN-NIV-PRO). Funcionales propias FUN-CI.
  "dian-gestor-iii-control-interno-236872": {
    id: "dian-gestor-iii-control-interno-236872",
    nombre: "DIAN · Gestor III (303-03, Control Interno), concurso DIAN 2676, OPEC 236872 — plan completo (21 días)",
    guias: [
      { codigo: "INTRO-00", dia: 1 },
      { codigo: "ENT-DIAN-01", dia: 1, orden: 1 },
      { codigo: "DIAN-PON-01", dia: 1, orden: 2 },
      { codigo: "GEN-01", dia: 2 },
      { codigo: "GEN-02", dia: 3 },
      { codigo: "GEN-03", dia: 4 },
      { codigo: "DIAN-NIV-PRO-01", dia: 5 },
      { codigo: "DIAN-NIV-PRO-02", dia: 6 },
      { codigo: "DIAN-NIV-PRO-03", dia: 7 },
      { codigo: "DIAN-NIV-PRO-04", dia: 8 },
      { codigo: "FUN-CI-01", dia: 9 },
      { codigo: "FUN-CI-02", dia: 10 },
      { codigo: "FUN-CI-03", dia: 11 },
      { codigo: "FUN-CI-04", dia: 12 },
      { codigo: "FUN-CI-05", dia: 13 },
      { codigo: "FUN-CI-06", dia: 14 },
      { codigo: "FUN-CI-07", dia: 15 },
      { codigo: "FUN-CI-08", dia: 16 },
      { codigo: "FUN-CI-09", dia: 17 },
      { codigo: "FUN-CI-10", dia: 18 },
      { codigo: "FUN-CI-11", dia: 19 },
      { codigo: "FUN-CI-12", dia: 20 },
      { codigo: "SIM-DIAN-CI-001", dia: 21 },
      { codigo: "BON-01", dia: null, orden: 100 },
      { codigo: "BON-02", dia: null, orden: 101 },
      { codigo: "DIAN-EST-01", dia: null, orden: 102 },
      { codigo: "DIAN-INT-01", dia: null, orden: 103 },
    ],
  },
  // DIAN 2676 — Analista I (201-01), Fiscalización y liquidación (ficha AT-FL-2013), OPEC 236764 — Adriana Marcela Bernal.
  // Curso INTENSIVO de 15 días. Días 1-7 transversales DIAN intensivos (INTENS-DIAN), 8-9 comportamentales técnico (INTENS-TEC),
  // 10-14 propias del cargo (INTENS-AIFL), 15 simulacro. Ver referencias/_SPEC-CURSO-INTENSIVO-ANALISTA1-FL-ADRIANA.md.
  "dian-analista-i-fiscalizacion-intensivo-236764": {
    id: "dian-analista-i-fiscalizacion-intensivo-236764",
    nombre: "DIAN · Analista I (201-01, fiscalización y liquidación), concurso DIAN 2676, OPEC 236764 — intensivo 15 días",
    duracion: 15,
    guias: [
      { codigo: "INTENS-DIAN-01", dia: 1 },
      { codigo: "INTENS-DIAN-02", dia: 2 },
      { codigo: "INTENS-DIAN-03", dia: 3 },
      { codigo: "INTENS-DIAN-04", dia: 4 },
      { codigo: "INTENS-DIAN-05", dia: 5 },
      { codigo: "INTENS-DIAN-06", dia: 6 },
      { codigo: "INTENS-DIAN-07", dia: 7 },
      { codigo: "INTENS-TEC-08", dia: 8 },
      { codigo: "INTENS-TEC-09", dia: 9 },
      { codigo: "INTENS-AIFL-10", dia: 10 },
      { codigo: "INTENS-AIFL-11", dia: 11 },
      { codigo: "INTENS-AIFL-12", dia: 12 },
      { codigo: "INTENS-AIFL-13", dia: 13 },
      { codigo: "INTENS-AIFL-14", dia: 14 },
      { codigo: "SIM-DIAN-AIFL-001", dia: 15 },
    ],
  },
  // DIAN 2676 — Gestor I (301-01), Fiscalización y liquidación (ficha AT-FL-3008), OPEC 236767 — intensivo de 15 días.
  // Días 1-7 transversales DIAN intensivos (INTENS-DIAN), 8-9 comportamentales nivel profesional (INTENS-PRO),
  // 10-14 propias del cargo (INTENS-GI, fusión de las guías del plan de 21 días), 15 simulacro del Gestor I.
  // Ver referencias/_SPEC-CURSO-INTENSIVO-GESTOR1-FL.md.
  "dian-gestor-i-fiscalizacion-intensivo-236767": {
    id: "dian-gestor-i-fiscalizacion-intensivo-236767",
    nombre: "DIAN · Gestor I (301-01, fiscalización y liquidación), concurso DIAN 2676, OPEC 236767 — intensivo 15 días",
    duracion: 15,
    guias: [
      { codigo: "INTENS-DIAN-01", dia: 1 },
      { codigo: "INTENS-DIAN-02", dia: 2 },
      { codigo: "INTENS-DIAN-03", dia: 3 },
      { codigo: "INTENS-DIAN-04", dia: 4 },
      { codigo: "INTENS-DIAN-05", dia: 5 },
      { codigo: "INTENS-DIAN-06", dia: 6 },
      { codigo: "INTENS-DIAN-07", dia: 7 },
      { codigo: "INTENS-PRO-08", dia: 8 },
      { codigo: "INTENS-PRO-09", dia: 9 },
      { codigo: "INTENS-GI-10", dia: 10 },
      { codigo: "INTENS-GI-11", dia: 11 },
      { codigo: "INTENS-GI-12", dia: 12 },
      { codigo: "INTENS-GI-13", dia: 13 },
      { codigo: "INTENS-GI-14", dia: 14 },
      { codigo: "SIM-DIAN-001", dia: 15 },
    ],
  },
};

// Mapeo de código → archivo en storage (bucket 'guias')
const ARCHIVOS: Record<string, string> = {
  "INTENS-DIAN-01": "guias/INTENS-DIAN-01-arranque-dian-prueba-metodo.html",
  "INTENS-DIAN-02": "guias/INTENS-DIAN-02-sistema-tributario-aduanero-cambiario.html",
  "INTENS-DIAN-03": "guias/INTENS-DIAN-03-constitucion-funcion-publica-integridad.html",
  "INTENS-DIAN-04": "guias/INTENS-DIAN-04-cpaca-pqrsf-servicio-ciudadano.html",
  "INTENS-DIAN-05": "guias/INTENS-DIAN-05-evasion-elusion-contrabando-transparencia.html",
  "INTENS-DIAN-06": "guias/INTENS-DIAN-06-gestion-documental-herramientas-informaticas.html",
  "INTENS-DIAN-07": "guias/INTENS-DIAN-07-mipg-modelo-integrado.html",
  "INTENS-TEC-08": "guias/INTENS-TEC-08-comportamiento-etico-adaptabilidad.html",
  "INTENS-TEC-09": "guias/INTENS-TEC-09-comunicacion-equipo-logro-usuario.html",
  "INTENS-AIFL-10": "guias/INTENS-AIFL-10-fiscalizacion-liquidacion-control-tributario.html",
  "INTENS-AIFL-11": "guias/INTENS-AIFL-11-fiscalizacion-aduanera-mercancias-cautelares.html",
  "INTENS-AIFL-12": "guias/INTENS-AIFL-12-regimen-cambiario-divisas.html",
  "INTENS-AIFL-13": "guias/INTENS-AIFL-13-fiscalizacion-internacional-gestion-documental.html",
  "INTENS-AIFL-14": "guias/INTENS-AIFL-14-alcance-cargo-repaso-likert.html",
  "SIM-DIAN-AIFL-001": "simulacro/SIM-DIAN-AIFL-001.html",
  "INTENS-PRO-08": "guias/INTENS-PRO-08-comportamiento-etico-adaptabilidad.html",
  "INTENS-PRO-09": "guias/INTENS-PRO-09-comunicacion-equipo-logro-usuario.html",
  "INTENS-GI-10": "guias/INTENS-GI-10-determinacion-control-fiscalizacion-liquidacion.html",
  "INTENS-GI-11": "guias/INTENS-GI-11-fiscalizacion-aduanera-cautelares-destruccion.html",
  "INTENS-GI-12": "guias/INTENS-GI-12-regimen-cambiario-dian.html",
  "INTENS-GI-13": "guias/INTENS-GI-13-fiscalizacion-internacional-laft-ros.html",
  "INTENS-GI-14": "guias/INTENS-GI-14-alcance-cargo-informes-repaso-likert.html",
  "FUN-CI-01": "guias/FUN-CI-01-funcion-control-interno-ley-87.html",
  "FUN-CI-02": "guias/FUN-CI-02-mipg-meci-lineas-defensa.html",
  "FUN-CI-03": "guias/FUN-CI-03-normas-globales-auditoria-interna.html",
  "FUN-CI-04": "guias/FUN-CI-04-plan-auditoria-pruebas-evidencia.html",
  "FUN-CI-05": "guias/FUN-CI-05-hallazgos-informes-de-ley.html",
  "FUN-CI-06": "guias/FUN-CI-06-planes-de-mejoramiento.html",
  "FUN-CI-07": "guias/FUN-CI-07-administracion-riesgo-diseno-controles.html",
  "FUN-CI-08": "guias/FUN-CI-08-indicadores-cultura-control-entes-externos.html",
  "FUN-CI-09": "guias/FUN-CI-09-constitucion-servidor-publico.html",
  "FUN-CI-10": "guias/FUN-CI-10-cpaca-pqrsf-servicio-ciudadano.html",
  "FUN-CI-11": "guias/FUN-CI-11-integridad-transparencia-evasion-contrabando.html",
  "FUN-CI-12": "guias/FUN-CI-12-herramientas-informaticas-gestion-documental.html",
  "SIM-DIAN-CI-001": "simulacro/SIM-DIAN-CI-001.html",
  "DIAN-FIS2-COM-01": "guias/DIAN-FIS2-COM-01-comportamiento-etico-adaptabilidad.html",
  "DIAN-FIS2-COM-02": "guias/DIAN-FIS2-COM-02-comunicacion-trabajo-equipo.html",
  "DIAN-FIS2-COM-03": "guias/DIAN-FIS2-COM-03-orientacion-logro-usuario.html",
  "DIAN-FIS2-COM-04": "guias/DIAN-FIS2-COM-04-alcance-cargo-gestor-ii.html",
  "FUN-FIS2-01": "guias/FUN-FIS2-01-precritica-denuncias-revision-expedientes.html",
  "SIM-DIAN-FIS2-001": "simulacro/SIM-DIAN-FIS2-001.html",
  "FUN-ADM-12": "guias/FUN-ADM-12-evasion-elusion-contrabando-transparencia.html",
  "FUN-ADM-09": "guias/FUN-ADM-09-cpaca-principios-procedimiento.html",
  "FUN-ADM-10": "guias/FUN-ADM-10-mipg-buen-gobierno-integridad.html",
  "FUN-ADM-11": "guias/FUN-ADM-11-documental-pqrsf-servicio-tic.html",
  "DIAN-ADM-COM-01": "guias/DIAN-ADM-COM-01-comportamiento-etico-adaptabilidad.html",
  "DIAN-ADM-COM-02": "guias/DIAN-ADM-COM-02-innovacion-solucion-problemas.html",
  "DIAN-ADM-COM-03": "guias/DIAN-ADM-COM-03-logro-usuario-comunicacion-equipo.html",
  "DIAN-ADM-COM-04": "guias/DIAN-ADM-COM-04-alcance-cargo-gestor-ii.html",
  "FUN-ADM-01": "guias/FUN-ADM-01-contratacion-publica-i.html",
  "FUN-ADM-02": "guias/FUN-ADM-02-contratacion-publica-ii.html",
  "FUN-ADM-03": "guias/FUN-ADM-03-custodia-disposicion-mercancias.html",
  "FUN-ADM-04": "guias/FUN-ADM-04-ingresos-almacenamiento-registro-mercancias.html",
  "FUN-ADM-05": "guias/FUN-ADM-05-infraestructura-servicios-generales.html",
  "FUN-ADM-06": "guias/FUN-ADM-06-siif-nacion-ingresos-egresos.html",
  "FUN-ADM-07": "guias/FUN-ADM-07-constitucion-politica.html",
  "FUN-ADM-08": "guias/FUN-ADM-08-notificacion-recursos-archivo.html",
  "SIM-DIAN-ADM-001": "simulacro/SIM-DIAN-ADM-001.html",
  "ENT-DIAN-01": "guias/ENT-DIAN-01-conoce-entidad-dian.html",
  "DIAN-PRO-COM-01": "guias/DIAN-PRO-COM-01-comportamiento-etico-adaptabilidad.html",
  "DIAN-PRO-COM-02": "guias/DIAN-PRO-COM-02-comunicacion-trabajo-equipo.html",
  "DIAN-PRO-COM-03": "guias/DIAN-PRO-COM-03-orientacion-logro-usuario.html",
  "DIAN-PRO-COM-GIII-04": "guias/DIAN-PRO-COM-GIII-04-alcance-cargo-gestor-iii.html",
  "FUN-RADM-01": "guias/FUN-RADM-01-generalidades-recursos-administrativos.html",
  "FUN-RADM-02": "guias/FUN-RADM-02-infraestructura-fisica-i.html",
  "FUN-RADM-03": "guias/FUN-RADM-03-infraestructura-fisica-ii.html",
  "FUN-RADM-04": "guias/FUN-RADM-04-administracion-bienes-muebles-inmuebles.html",
  "FUN-RADM-05": "guias/FUN-RADM-05-servicios-generales-parque-automotor.html",
  "FUN-RADM-06": "guias/FUN-RADM-06-contratacion-estatal-i.html",
  "FUN-RADM-07": "guias/FUN-RADM-07-contratacion-estatal-ii.html",
  "FUN-RADM-08": "guias/FUN-RADM-08-gestion-documental-archivo.html",
  "FUN-RADM-09": "guias/FUN-RADM-09-mipg-buen-gobierno-integridad.html",
  "FUN-RADM-10": "guias/FUN-RADM-10-transparencia-lucha-corrupcion.html",
  "FUN-RADM-11": "guias/FUN-RADM-11-herramientas-informaticas-informes-gestion.html",
  "FUN-RADM-12": "guias/FUN-RADM-12-repaso-integrador.html",
  "SIM-DIAN-GIII-001": "simulacro/SIM-DIAN-GIII-001.html",
  "SIM-DIAN-001": "simulacro/SIM-DIAN-001.html",
  "DIAN-ADU-COM-01": "guias/DIAN-ADU-COM-01-comportamiento-etico-adaptabilidad.html",
  "DIAN-ADU-COM-02": "guias/DIAN-ADU-COM-02-comunicacion-trabajo-equipo.html",
  "DIAN-ADU-COM-03": "guias/DIAN-ADU-COM-03-orientacion-logro-usuario.html",
  "DIAN-ADU-COM-04": "guias/DIAN-ADU-COM-04-alcance-cargo-gestor-ii.html",
  "FUN-ADU-01": "guias/FUN-ADU-01-generalidades-operacion-aduanera.html",
  "FUN-ADU-02": "guias/FUN-ADU-02-ingreso-mercancias-importacion.html",
  "FUN-ADU-03": "guias/FUN-ADU-03-salidas-mercancias-exportacion.html",
  "FUN-ADU-04": "guias/FUN-ADU-04-transito-aduanero-regimenes-especiales.html",
  "FUN-ADU-05": "guias/FUN-ADU-05-nomenclatura-arancelaria.html",
  "FUN-ADU-06": "guias/FUN-ADU-06-valoracion-mercancias.html",
  "FUN-ADU-07": "guias/FUN-ADU-07-origen-acuerdos-comerciales.html",
  "FUN-ADU-08": "guias/FUN-ADU-08-registro-aduanero-oea-garantias.html",
  "FUN-ADU-09": "guias/FUN-ADU-09-control-aduanero-contrabando-transparencia.html",
  "FUN-ADU-JUR-01": "guias/FUN-ADU-JUR-01-cpaca-procedimiento-administrativo.html",
  "FUN-ADU-MIPG-01": "guias/FUN-ADU-MIPG-01-mipg-buen-gobierno-integridad.html",
  "FUN-ADU-DOC-01": "guias/FUN-ADU-DOC-01-gestion-documental-pqrsf-servicio-tic.html",
  "SIM-DIAN-ADU-001": "simulacro/SIM-DIAN-ADU-001.html",
  "DIAN-PON-01": "guias/DIAN-PON-01-ponderaciones-puntaje-prueba.html",
  "DIAN-EST-01": "guias/DIAN-EST-01-estrategia-tiempo-prueba-escrita.html",
  "DIAN-INT-01": "guias/DIAN-INT-01-codigo-integridad-prueba-integridad.html",
  "ENT-URT-01": "guias/ENT-URT-01-conoce-entidad-urt-asuntos-etnicos.html",
  "ENT-HUH-01": "guias/ENT-HUH-01-conoce-entidad-huhmp.html",
  "ENT-IDV-01": "guias/ENT-IDV-01-conoce-entidad-indervalle.html",
  "INTRO-00-PGN-4SP13": "guias/INTRO-00-PGN-4SP13-presentacion-curso.html",
  "FUN-DIS-TEC-01": "guias/FUN-DIS-TEC-01-procedimiento-disciplinario-tramite-secretarial.html",
  "INTRO-00": "guias/INTRO-00-presentacion-curso.html",
  "INTRO-00-PGN": "guias/INTRO-00-PGN-presentacion-curso-pgn.html",
  "GEN-01": "guias/GEN-01-estado-funcion-publica.html",
  "GEN-02": "guias/GEN-02-relacion-estado-ciudadano.html",
  "GEN-03": "guias/GEN-03-marco-institucional.html",
  "ASI-COM-01": "guias/ASI-COM-01-cumplimiento-desarrollo-laboral.html",
  "ASI-COM-02": "guias/ASI-COM-02-atencion-colaboracion.html",
  "ASI-ESP-01": "guias/ASI-ESP-01-competencias-nivel-asistencial.html",
  "ASI-ESP-02": "guias/ASI-ESP-02-alcance-cargo-asistencial.html",
  "TEC-COM-01": "guias/TEC-COM-01-desempeno-cumplimiento.html",
  "TEC-COM-02": "guias/TEC-COM-02-usuarios-trabajo-colaborativo.html",
  "TEC-ESP-01": "guias/TEC-ESP-01-competencias-nivel-tecnico.html",
  "TEC-ESP-02": "guias/TEC-ESP-02-alcance-cargo-tecnico.html",
  "PRO-COM-01": "guias/PRO-COM-01-gestion-cumplimiento.html",
  "PRO-COM-02": "guias/PRO-COM-02-servicio-articulacion.html",
  "PRO-ESP-01": "guias/PRO-ESP-01-competencias-nivel-profesional.html",
  "PRO-ESP-02": "guias/PRO-ESP-02-alcance-cargo-profesional.html",
  "DIAN-NIV-ASI-01": "guias/DIAN-NIV-ASI-01-etica-adaptabilidad.html",
  "DIAN-NIV-ASI-02": "guias/DIAN-NIV-ASI-02-comunicacion-trabajo-equipo.html",
  "DIAN-NIV-ASI-03": "guias/DIAN-NIV-ASI-03-logro-usuario.html",
  "DIAN-NIV-ASI-04": "guias/DIAN-NIV-ASI-04-ficha-innovacion-problemas-evaluacion.html",
  "DIAN-NIV-TEC-01": "guias/DIAN-NIV-TEC-01-comportamiento-etico-adaptabilidad.html",
  "DIAN-NIV-TEC-02": "guias/DIAN-NIV-TEC-02-comunicacion-trabajo-equipo.html",
  "DIAN-NIV-TEC-03": "guias/DIAN-NIV-TEC-03-logro-usuario-innovacion.html",
  "DIAN-NIV-TEC-04": "guias/DIAN-NIV-TEC-04-ficha-innovacion-problemas-evaluacion.html",
  "DIAN-NIV-PRO-01": "guias/DIAN-NIV-PRO-01-comportamiento-etico-adaptabilidad.html",
  "DIAN-NIV-PRO-02": "guias/DIAN-NIV-PRO-02-comunicacion-trabajo-equipo.html",
  "DIAN-NIV-PRO-03": "guias/DIAN-NIV-PRO-03-logro-usuario.html",
  "DIAN-NIV-PRO-04": "guias/DIAN-NIV-PRO-04-ficha-innovacion-problemas-evaluacion.html",
  "BON-01": "guias/BON-01-estrategia-cnsc.html",
  "BON-02": "guias/BON-02-ofimatica.html",
};

/**
 * Auto-carga las guías correspondientes al curso recién creado.
 * Se llama desde procesarReferencia() después de crear el curso.
 * 
 * @param supabase - Cliente con service role (admin)
 * @param cursoId - ID del curso recién creado
 * @param nivel - Nivel del cargo (asistencial | tecnico | profesional)
 * @param convocatoriaId - ID de la convocatoria (opcional; si es PGN, carga INTRO-00-PGN)
 */
export async function cargarGuiasAutomaticas(
  supabase: SupabaseClient,
  cursoId: string,
  nivel: string,
  convocatoriaId?: string | null
): Promise<void> {
  // Normalizar nivel (quitar tildes para que "técnico" → "tecnico")
  const nivelNorm = (nivel || "").toLowerCase().trim()
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "");

  // GUARDA IDEMPOTENTE: si el curso ya tiene guías, NO volver a auto-cargar.
  // Evita el bug de duplicados cuando esta función se ejecuta más de una vez
  // sobre el mismo curso (p. ej. por un reproceso o un webhook reintentado).
  const { count: yaTiene } = await supabase
    .from("guias_curso")
    .select("id", { count: "exact", head: true })
    .eq("curso_id", cursoId);
  if ((yaTiene ?? 0) > 0) {
    console.warn(`[autocargarGuias] El curso ${cursoId} ya tiene ${yaTiene} guías; se omite la auto-carga (idempotente).`);
    return;
  }

  // Convocatoria: ¿PGN (régimen especial) o CNSC? y, si es CNSC, su "Conoce tu entidad".
  const infoConv = await infoConvocatoria(supabase, convocatoriaId);

  // PROCURADURÍA: no se auto-cargan guías genéricas. Cada cargo tiene su plan propio:
  // si ya existe, el admin usa "Limpiar y rehacer" con ese plan; si es nuevo, se construye.
  if (infoConv.esPgn) {
    console.warn(`[autocargarGuias] Curso ${cursoId} es de la Procuraduría: sin auto-carga (se arma con plan propio).`);
    return;
  }

  // --- PGN nivel asistencial: usar las guías propias -PGN-AUX (no las genéricas) ---
  // La Procuraduría (régimen especial) tiene guías reenfocadas al cargo Auxiliar
  // Administrativo. Si es PGN + asistencial, auto-cargamos las AUX correctas
  // (Días 1-8: intro + entidad + generales + competencias) resolviéndolas por
  // código contra el catálogo. Las funcionales y el simulacro las arma el admin
  // (o el botón "Armar plan completo").
  if (esPGN(convocatoriaId) && nivelNorm === "asistencial") {
    const CODIGOS_PGN_AUX: Array<{ codigo: string; dia: number; orden: number; tipo: string }> = [
      { codigo: "INTRO-00-PGN-AUX", dia: 1, orden: 0, tipo: "general" },
      { codigo: "ENT-PGN-AUX-01", dia: 1, orden: 1, tipo: "general" },
      { codigo: "GEN-01-PGN-AUX", dia: 2, orden: 2, tipo: "general" },
      { codigo: "GEN-02-PGN-AUX", dia: 3, orden: 3, tipo: "general" },
      { codigo: "GEN-03-PGN-AUX", dia: 4, orden: 4, tipo: "general" },
      { codigo: "ASI-PGN-AUX-01", dia: 5, orden: 5, tipo: "nivel" },
      { codigo: "ASI-PGN-AUX-02", dia: 6, orden: 6, tipo: "nivel" },
      { codigo: "ASI-PGN-AUX-03", dia: 7, orden: 7, tipo: "nivel" },
      { codigo: "ASI-PGN-AUX-04", dia: 8, orden: 8, tipo: "nivel" },
    ];
    const guia = (await import("./catalogoGuias")).getGuiaCatalogo;
    const registrosPGN = CODIGOS_PGN_AUX
      .map((c) => {
        const g = guia(c.codigo);
        if (!g || !g.archivoPath || g.estado !== "publicada") return null;
        return { curso_id: cursoId, dia: c.dia, titulo: g.titulo, tipo: c.tipo, orden: c.orden, archivo_path: g.archivoPath };
      })
      .filter(Boolean) as any[];
    if (registrosPGN.length > 0) {
      const { error } = await supabase.from("guias_curso").insert(registrosPGN);
      if (error) console.error("[autocargarGuias] Error al insertar guías PGN-AUX:", error.message);
    }
    return;
  }

  // Elegir la guía de introducción según tipo de concurso
  const intro = INTRO_CNSC;

  // Construir la lista de guías a insertar:
  // Día 1 = Introducción + "Conoce tu entidad" (si la convocatoria tiene), Días 2-4 generales,
  // Días 5-8 por nivel, + bonus.
  const guiasNivel = guiasNivelPara(nivelNorm, infoConv.entidad?.codigo);
  const entGuia = infoConv.entidad
    ? [{ codigo: infoConv.entidad.codigo, dia: 1, titulo: infoConv.entidad.titulo, tipo: "general", orden: 1 }]
    : [];
  if (!infoConv.entidad) console.warn(`[autocargarGuias] La convocatoria "${infoConv.texto}" no tiene guía "Conoce tu entidad" en la biblioteca.`);
  const extrasEnt = extrasDeEntidad(infoConv.entidad?.codigo);
  const todasLasGuias = [intro, ...entGuia, ...extrasEnt.filter((g) => g.dia === 1), ...GUIAS_GENERALES, ...guiasNivel, ...GUIAS_BONUS, ...extrasEnt.filter((g) => g.dia === null)];

  // Preparar los registros para guias_curso
  const registros = todasLasGuias.map((g) => ({
    curso_id: cursoId,
    dia: g.dia,
    titulo: g.titulo,
    tipo: g.tipo,
    orden: g.orden,
    archivo_path: ARCHIVOS[g.codigo] || null,
  }));

  // Insertar en batch (idempotente: si ya existen, no duplica gracias a que
  // este código solo se ejecuta una vez al crear el curso)
  if (registros.length > 0) {
    const { error } = await supabase.from("guias_curso").insert(registros);
    if (error) {
      console.error("[autocargarGuias] Error al insertar guías:", error.message);
    }
  }
}

/**
 * Reutilización del plan por OPEC.
 *
 * Si YA existe otro curso del MISMO OPEC con el plan armado (es decir, con
 * guías funcionales asignadas), copia TODAS sus guías al curso nuevo. Así, el
 * primer comprador de un OPEC se arma a mano una sola vez y todos los
 * siguientes del mismo OPEC quedan con el plan completo automáticamente
 * (funcionales + "Conoce tu Entidad" + simulacro + generales/nivel/bonus).
 *
 * No copia el progreso (leida/fecha_leida): el nuevo alumno empieza de cero.
 *
 * @returns true si copió un plan con funcionales; false si no había uno
 *          (en ese caso el llamador debe usar cargarGuiasAutomaticas).
 */
export async function copiarPlanDesdeOPEC(
  supabase: SupabaseClient,
  nuevoCursoId: string,
  opec: string | null
): Promise<boolean> {
  if (!opec) return false;

  // Otros cursos del mismo OPEC
  // Solo se copian planes de la MISMA modalidad (21 días o intensivo de 15):
  // un curso intensivo no debe heredar las guías del plan de 21 días ni al revés.
  const { data: cursosTodos } = await supabase
    .from("cursos")
    .select("*")
    .eq("opec", opec)
    .neq("id", nuevoCursoId);
  const { data: actual } = await supabase.from("cursos").select("*").eq("id", nuevoCursoId).maybeSingle();
  const modActual = String((actual as any)?.modalidad || "21");
  const cursos = (cursosTodos || []).filter((c: any) => String(c.modalidad || "21") === modActual);
  if (cursos.length === 0) return false;

  const ids = cursos.map((c: any) => c.id);
  const { data: guias } = await supabase
    .from("guias_curso")
    .select("curso_id, titulo, dia, tipo, orden, archivo_path")
    .in("curso_id", ids);
  if (!guias || guias.length === 0) return false;

  // Agrupar por curso y elegir el que tenga MÁS guías funcionales (plan más completo)
  const porCurso: Record<string, any[]> = {};
  guias.forEach((g: any) => {
    (porCurso[g.curso_id] = porCurso[g.curso_id] || []).push(g);
  });
  let mejor: any[] | null = null;
  let mejorFuncionales = 0;
  for (const arr of Object.values(porCurso)) {
    const nFunc = arr.filter((g: any) => g.tipo === "funcional").length;
    if (nFunc > mejorFuncionales) {
      mejorFuncionales = nFunc;
      mejor = arr;
    }
  }
  // Si ningún curso del OPEC tiene funcionales, no hay un "plan" que copiar.
  if (!mejor || mejorFuncionales === 0) return false;

  // Evitar duplicados: no copiar guías cuyo archivo ya esté en el curso destino
  // (p. ej. si ya tenía las genéricas auto-cargadas).
  const { data: yaTiene } = await supabase
    .from("guias_curso")
    .select("archivo_path")
    .eq("curso_id", nuevoCursoId);
  const existentes = new Set((yaTiene || []).map((g: any) => g.archivo_path).filter(Boolean));

  // Copiar las guías del mejor curso que falten en el destino (sin progreso).
  const registros = mejor
    .filter((g: any) => !(g.archivo_path && existentes.has(g.archivo_path)))
    .map((g: any) => ({
      curso_id: nuevoCursoId,
      titulo: g.titulo,
      dia: g.dia,
      tipo: g.tipo,
      orden: g.orden,
      archivo_path: g.archivo_path,
    }));
  if (registros.length === 0) return false;
  const { error } = await supabase.from("guias_curso").insert(registros);
  if (error) {
    console.error("[copiarPlanDesdeOPEC] Error al copiar el plan:", error.message);
    return false;
  }
  return true;
}


/**
 * Rutas (archivo_path) de las guías GENÉRICAS que la auto-carga histórica pudo
 * haber insertado en cursos que en realidad usan un plan propio (p. ej. PGN-AUX).
 * Son las versiones "viejas" comunes/CNSC que deben limpiarse cuando el curso
 * ya tiene su equivalente propio.
 */
const RUTAS_GENERICAS = new Set<string>([
  "guias/INTRO-00-presentacion-curso.html",
  "guias/GEN-01-estado-funcion-publica.html",
  "guias/GEN-02-relacion-estado-ciudadano.html",
  "guias/GEN-03-marco-institucional.html",
  "guias/ASI-COM-01-cumplimiento-desarrollo-laboral.html",
  "guias/ASI-COM-02-atencion-colaboracion.html",
  "guias/ASI-ESP-01-competencias-nivel-asistencial.html",
  "guias/ASI-ESP-02-alcance-cargo-asistencial.html",
  "guias/TEC-COM-01-desempeno-cumplimiento.html",
  "guias/TEC-COM-02-usuarios-trabajo-colaborativo.html",
  "guias/TEC-ESP-01-competencias-nivel-tecnico.html",
  "guias/TEC-ESP-02-alcance-cargo-tecnico.html",
  "guias/PRO-COM-01-gestion-cumplimiento.html",
  "guias/PRO-COM-02-servicio-articulacion.html",
  "guias/PRO-ESP-01-competencias-nivel-profesional.html",
  "guias/PRO-ESP-02-alcance-cargo-profesional.html",
]);

/**
 * AUTO-SANEAMIENTO de un curso: elimina las guías GENÉRICAS (comunes/CNSC) que
 * quedaron mezcladas cuando el curso ya tiene su plan PROPIO por entidad
 * (p. ej. las -PGN-AUX de la Procuraduría, o cualquier plan con "Conoce tu
 * Entidad" propia + generales/nivel específicas).
 *
 * Es CONSERVADOR: solo actúa si el curso tiene señales claras de un plan propio
 * (una guía "Conoce tu Entidad" ENT-… asignada, o alguna guía -PGN-AUX). En ese
 * caso, las genéricas de RUTAS_GENERICAS sobran (fueron auto-cargadas por error)
 * y se eliminan. Si el curso es legítimamente genérico (sin plan propio), NO
 * toca nada.
 *
 * Se puede llamar de forma idempotente en cada carga del perfil/preview: si no
 * hay nada que limpiar, no hace ninguna escritura.
 *
 * @returns número de guías eliminadas (0 si no había nada que sanear).
 */
export async function sanearGuiasGenericas(
  supabase: SupabaseClient,
  cursoId: string
): Promise<number> {
  const { data: guias } = await supabase
    .from("guias_curso")
    .select("id, archivo_path")
    .eq("curso_id", cursoId);
  if (!guias || guias.length === 0) return 0;

  // ¿El curso tiene un plan PROPIO? Señales: una guía de entidad (ENT-…) o
  // alguna guía con sufijo -AUX (plan reenfocado por cargo).
  // IMPORTANTE: solo aplica a cursos de la PROCURADURÍA (régimen especial). Los
  // cursos de CNSC también pueden tener una guía "Conoce tu entidad" (ENT-DIAN-01,
  // ENT-URT-01, ENT-HUH-01…) y NO deben perder sus guías genéricas Días 1-8.
  const tienePlanPropio = guias.some((g: any) => {
    const p = (g.archivo_path || "").toString();
    return /PGN/i.test(p) || /-AUX[-.]/i.test(p) || /-AUX\//i.test(p);
  });
  if (!tienePlanPropio) return 0; // curso CNSC / genérico legítimo: no tocar.

  // Eliminar las genéricas sobrantes.
  const aEliminar = guias.filter((g: any) => g.archivo_path && RUTAS_GENERICAS.has(g.archivo_path));
  if (aEliminar.length === 0) return 0;

  const ids = aEliminar.map((g: any) => g.id);
  const { error } = await supabase.from("guias_curso").delete().in("id", ids);
  if (error) {
    console.error("[sanearGuiasGenericas] Error al eliminar genéricas:", error.message);
    return 0;
  }
  return ids.length;
}

/**
 * AUTO-COMPLETADO del plan PGN Auxiliar Administrativo.
 *
 * Si el curso tiene señales claras de ser el plan PGN-AUX (alguna guía cuyo
 * archivo_path contenga "-PGN-AUX" o sea del set del plan), y le FALTAN guías
 * de ese plan, las inserta automáticamente desde la plantilla
 * `pgn-auxiliar-administrativo` (resolviendo cada código contra el catálogo).
 * Es idempotente: no duplica las que ya estén (compara por archivo_path).
 *
 * Esto garantiza que, aunque el curso se haya creado antes del arreglo (y le
 * falten las funcionales/simulacro), al abrir el perfil el plan quede completo
 * de forma automática, sin intervención del admin.
 *
 * @returns número de guías insertadas (0 si ya estaba completo o no aplica).
 */
export async function asegurarPlanPGNAuxiliar(
  supabase: SupabaseClient,
  cursoId: string
): Promise<number> {
  const { getGuiaCatalogo } = await import("./catalogoGuias");
  const plan = PLANES_PLANTILLA["pgn-auxiliar-administrativo"];
  if (!plan) return 0;

  const { data: guias } = await supabase
    .from("guias_curso")
    .select("archivo_path")
    .eq("curso_id", cursoId);
  if (!guias) return 0;

  const rutasActuales = new Set((guias as any[]).map((g) => g.archivo_path).filter(Boolean));

  // Rutas del plan (resueltas del catálogo).
  const rutasPlan: { codigo: string; ruta: string; item: ItemPlanPlantilla; titulo: string; tipo: string }[] = [];
  for (const item of plan.guias) {
    const g = getGuiaCatalogo(item.codigo);
    if (g && g.archivoPath && g.estado === "publicada") {
      rutasPlan.push({ codigo: item.codigo, ruta: g.archivoPath, item, titulo: g.titulo, tipo: g.tipo });
    }
  }

  // ¿El curso es del plan PGN-AUX? Señal: comparte al menos una ruta del plan.
  const esPlanPGN = rutasPlan.some((r) => rutasActuales.has(r.ruta));
  if (!esPlanPGN) return 0; // no es este plan: no tocar.

  // Insertar las que falten.
  const registros = rutasPlan
    .filter((r) => !rutasActuales.has(r.ruta))
    .map((r) => ({
      curso_id: cursoId,
      titulo: r.titulo,
      dia: r.item.dia,
      tipo: r.tipo,
      orden: r.item.orden ?? r.item.dia ?? 0,
      archivo_path: r.ruta,
    }));
  if (registros.length === 0) return 0;

  const { error } = await supabase.from("guias_curso").insert(registros);
  if (error) {
    console.error("[asegurarPlanPGNAuxiliar] Error al completar el plan:", error.message);
    return 0;
  }
  return registros.length;
}


/**
 * RESTAURACIÓN del bloque base de los cursos de CNSC (todo lo que NO es PGN).
 *
 * Los cursos de CNSC se crean con: INTRO-00 (Día 1), GEN-01..03 (Días 2-4), las 4
 * guías de su nivel (Días 5-8) y los bonus. Un saneamiento antiguo (que confundía
 * "Conoce tu entidad" de CNSC con un plan de Procuraduría) las borró de algunos
 * cursos. Esta función las repone, SIN duplicar, solo cuando al curso le falta
 * todo el bloque base (ni INTRO-00 ni GEN-01 presentes) y no es de Procuraduría.
 *
 * @returns número de guías insertadas (0 si no aplica o ya estaba completo).
 */
export async function restaurarBaseCNSC(
  supabase: SupabaseClient,
  cursoId: string
): Promise<number> {
  const { data: curso } = await supabase
    .from("cursos")
    .select("id, nivel, convocatorias(nombre, entidad)")
    .eq("id", cursoId)
    .single();
  if (!curso) return 0;

  const conv: any = Array.isArray((curso as any).convocatorias) ? (curso as any).convocatorias[0] : (curso as any).convocatorias;
  const textoConv = `${conv?.nombre || ""} ${conv?.entidad || ""}`.toLowerCase();
  if (/procuradur/.test(textoConv)) return 0; // PGN: otro plan propio.

  const { data: guias } = await supabase.from("guias_curso").select("archivo_path").eq("curso_id", cursoId);
  const rutas = new Set<string>(((guias as any[]) || []).map((g) => (g.archivo_path || "").toString()).filter(Boolean));
  if ([...rutas].some((r) => /PGN/i.test(r) || /-AUX[-.]/i.test(r))) return 0; // señales de plan PGN.
  // Plan personalizado CNSC (INTRO/GEN propios, p. ej. INTRO-00-DIAN-FAC2, GEN-01-DIAN-FAC2):
  // ya trae su bloque Días 1-4; no agregar las genéricas encima.
  if ([...rutas].some((r) => /(^|\/)(INTRO-00|GEN-0[1-3])-[A-Z]/.test(r))) return 0;

  // Curso INTENSIVO (plan propio de 15 días con guías INTENS-*): no lleva el bloque base
  // CNSC. Si por una restauración anterior quedaron mezcladas las guías base genéricas
  // (introducción, generales, competencias, bonus, extras de la entidad), se eliminan.
  if ([...rutas].some((r) => /(^|\/)INTENS-/.test(r))) {
    const nivelI = ((curso as any).nivel || "").toString().toLowerCase().trim()
      .normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    const entI = entidadCNSCDeConvocatoria(textoConv);
    const baseI = [INTRO_CNSC, ...(entI ? [{ codigo: entI.codigo }] : []), ...extrasDeEntidad(entI?.codigo),
      ...GUIAS_GENERALES, ...guiasNivelPara(nivelI, entI?.codigo), ...GUIAS_BONUS,
      ...Object.values(GUIAS_POR_NIVEL).flat(), ...Object.values(GUIAS_POR_NIVEL_DIAN).flat()];
    const rutasBase = new Set<string>(baseI.map((g: any) => ARCHIVOS[g.codigo]).filter(Boolean));
    const { data: filas } = await supabase.from("guias_curso").select("id, archivo_path").eq("curso_id", cursoId);
    const ids = ((filas as any[]) || []).filter((g) => g.archivo_path && rutasBase.has(g.archivo_path)).map((g) => g.id);
    if (ids.length > 0) {
      const { error } = await supabase.from("guias_curso").delete().in("id", ids);
      if (error) console.error("[restaurarBaseCNSC] Error al limpiar curso intensivo:", error.message);
    }
    return 0;
  }

  // Solo si falta TODO el bloque inicial (no tocar cursos donde el admin borró una guía suelta).
  if (rutas.has(ARCHIVOS["INTRO-00"]) || rutas.has(ARCHIVOS["GEN-01"])) return 0;

  const nivelNorm = ((curso as any).nivel || "").toString().toLowerCase().trim()
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  const ent = entidadCNSCDeConvocatoria(textoConv);
  const guiasNivel = guiasNivelPara(nivelNorm, ent?.codigo);
  const entGuia = ent ? [{ codigo: ent.codigo, dia: 1, titulo: ent.titulo, tipo: "general", orden: 1 }] : [];
  const extrasEnt = extrasDeEntidad(ent?.codigo);
  const base = [INTRO_CNSC, ...entGuia, ...extrasEnt.filter((g) => g.dia === 1), ...GUIAS_GENERALES, ...guiasNivel, ...GUIAS_BONUS, ...extrasEnt.filter((g) => g.dia === null)];

  const registros = base
    .filter((g) => ARCHIVOS[g.codigo] && !rutas.has(ARCHIVOS[g.codigo]))
    .map((g) => ({
      curso_id: cursoId,
      dia: g.dia,
      titulo: g.titulo,
      tipo: g.tipo,
      orden: g.orden,
      archivo_path: ARCHIVOS[g.codigo],
    }));
  if (registros.length === 0) return 0;

  const { error } = await supabase.from("guias_curso").insert(registros);
  if (error) {
    console.error("[restaurarBaseCNSC] Error al restaurar:", error.message);
    return 0;
  }
  return registros.length;
}


/**
 * Agrega a un curso CNSC las guías ADICIONALES de su entidad (hoy: DIAN →
 * ponderaciones/puntaje en el Día 1 + estrategia de tiempo e integridad como bonus),
 * sin duplicar. Se usa desde el endpoint admin para ponerse al día los cursos
 * DIAN ya existentes; los cursos nuevos las reciben al crearse.
 *
 * @returns número de guías insertadas.
 */
export async function asegurarExtrasEntidad(
  supabase: SupabaseClient,
  cursoId: string
): Promise<number> {
  const { data: curso } = await supabase
    .from("cursos")
    .select("id, convocatorias(nombre, entidad)")
    .eq("id", cursoId)
    .single();
  if (!curso) return 0;
  const conv: any = Array.isArray((curso as any).convocatorias) ? (curso as any).convocatorias[0] : (curso as any).convocatorias;
  const textoConv = `${conv?.nombre || ""} ${conv?.entidad || ""}`;
  if (/procuradur/i.test(textoConv)) return 0;
  const ent = entidadCNSCDeConvocatoria(textoConv);
  const extras = extrasDeEntidad(ent?.codigo);
  if (extras.length === 0) return 0;

  const { data: guias } = await supabase.from("guias_curso").select("archivo_path").eq("curso_id", cursoId);
  const rutas = new Set<string>(((guias as any[]) || []).map((g) => (g.archivo_path || "").toString()).filter(Boolean));
  if ([...rutas].some((r) => /(^|\/)INTENS-/.test(r))) return 0; // curso intensivo: plan cerrado.
  const registros = extras
    .filter((g) => ARCHIVOS[g.codigo] && !rutas.has(ARCHIVOS[g.codigo]))
    .map((g) => ({
      curso_id: cursoId,
      dia: g.dia,
      titulo: g.titulo,
      tipo: g.tipo,
      orden: g.orden,
      archivo_path: ARCHIVOS[g.codigo],
    }));
  if (registros.length === 0) return 0;
  const { error } = await supabase.from("guias_curso").insert(registros);
  if (error) {
    console.error("[asegurarExtrasEntidad] Error:", error.message);
    return 0;
  }
  return registros.length;
}


/**
 * Cursos DIAN que recibieron las comportamentales GENÉRICAS de la CNSC (ASI/TEC/PRO-COM,
 * -ESP) en los Días 5-8: se cambian por el set DIAN de su nivel (DIAN-NIV-*), que usa el
 * Diccionario de Competencias de la DIAN (Res. 065/2024). Actualiza las filas en su lugar
 * (mismo id), así no se pierde el progreso. No toca los cursos con comportamentales
 * propias por cargo (DIAN-PRO-COM, DIAN-ASI-COM, etc.). Idempotente.
 *
 * @returns número de guías actualizadas.
 */
export async function actualizarNivelDIAN(
  supabase: SupabaseClient,
  cursoId: string
): Promise<number> {
  const { data: curso } = await supabase
    .from("cursos")
    .select("id, nivel, convocatorias(nombre, entidad)")
    .eq("id", cursoId)
    .single();
  if (!curso) return 0;
  const conv: any = Array.isArray((curso as any).convocatorias) ? (curso as any).convocatorias[0] : (curso as any).convocatorias;
  const ent = entidadCNSCDeConvocatoria(`${conv?.nombre || ""} ${conv?.entidad || ""}`);
  if (ent?.codigo !== "ENT-DIAN-01") return 0;
  const nivelNorm = ((curso as any).nivel || "").toString().toLowerCase().trim()
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  const nuevas = GUIAS_POR_NIVEL_DIAN[nivelNorm];
  if (!nuevas) return 0;

  const viejas = new Set<string>(Object.values(GUIAS_POR_NIVEL).flat().map((g) => ARCHIVOS[g.codigo]).filter(Boolean));
  const { data: guias } = await supabase.from("guias_curso").select("id, dia, archivo_path").eq("curso_id", cursoId);
  const lista = (guias as any[]) || [];
  const rutas = new Set<string>(lista.map((g) => (g.archivo_path || "").toString()));
  let n = 0;
  for (const g of lista) {
    if (!g.archivo_path || !viejas.has(g.archivo_path)) continue;
    const nueva = nuevas.find((x) => x.dia === g.dia);
    if (!nueva || !ARCHIVOS[nueva.codigo] || rutas.has(ARCHIVOS[nueva.codigo])) continue;
    const { error } = await supabase
      .from("guias_curso")
      .update({ titulo: nueva.titulo, archivo_path: ARCHIVOS[nueva.codigo], tipo: nueva.tipo })
      .eq("id", g.id);
    if (error) { console.error("[actualizarNivelDIAN]", error.message); continue; }
    rutas.add(ARCHIVOS[nueva.codigo]);
    n++;
  }
  return n;
}
