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
export interface ItemPlanPlantilla { codigo: string; dia: number; orden?: number }
export interface PlanPlantilla { id: string; nombre: string; guias: ItemPlanPlantilla[] }

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
  // Proceso disciplinario (Dirección Nacional de Investigaciones Especiales) con énfasis financiero-contable.
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
      { codigo: "FUN-DISC-PU15-01", dia: 12 },
      { codigo: "FUN-DISC-PU15-02", dia: 13 },
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
};

// Mapeo de código → archivo en storage (bucket 'guias')
const ARCHIVOS: Record<string, string> = {
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
  const intro = esPGN(convocatoriaId) ? INTRO_PGN : INTRO_CNSC;

  // Construir la lista de guías a insertar
  const guiasNivel = GUIAS_POR_NIVEL[nivelNorm] || [];
  const todasLasGuias = [intro, ...GUIAS_GENERALES, ...guiasNivel, ...GUIAS_BONUS];

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
  const { data: cursos } = await supabase
    .from("cursos")
    .select("id")
    .eq("opec", opec)
    .neq("id", nuevoCursoId);
  if (!cursos || cursos.length === 0) return false;

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
  const tienePlanPropio = guias.some((g: any) => {
    const p = (g.archivo_path || "").toString();
    return /(^|\/)ENT-/i.test(p) || /-AUX[-.]/i.test(p) || /-AUX\//i.test(p) || p.includes("-PGN-AUX");
  });
  if (!tienePlanPropio) return 0; // curso genérico legítimo: no tocar.

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
