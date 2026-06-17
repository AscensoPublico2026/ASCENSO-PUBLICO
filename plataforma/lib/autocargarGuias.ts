/**
 * Auto-carga de guías al confirmar pago.
 * 
 * Regla de asignación (basada en biblioteca/biblioteca.json):
 * - Introducción (INTRO-00): Día 1 → siempre
 * - Generales (GEN-01, GEN-02, GEN-03): Días 2-4 → siempre
 * - Por Nivel (ASI/TEC/PRO según curso.nivel): Días 5-8 → según nivel
 * - Bonus (BON-01, BON-02): sin día fijo → siempre (sección bonus)
 * - Funcionales (Días 9-20): NO se auto-cargan (admin las sube personalizadas)
 * - Simulacro Final (Día 21): NO se auto-carga (admin la sube personalizada)
 * - INTRO-01 "Conoce tu Entidad": NO se auto-carga (bajo-demanda, admin la crea)
 */

import { SupabaseClient } from "@supabase/supabase-js";

// Definición de las guías que se auto-cargan según el nivel
const GUIAS_SIEMPRE = [
  { codigo: "INTRO-00", dia: 1, titulo: "Presentación del Curso y la CNSC", tipo: "general", orden: 1 },
  { codigo: "GEN-01", dia: 2, titulo: "Estado y Función Pública", tipo: "general", orden: 2 },
  { codigo: "GEN-02", dia: 3, titulo: "Relación Estado-Ciudadano", tipo: "general", orden: 3 },
  { codigo: "GEN-03", dia: 4, titulo: "Marco Institucional", tipo: "general", orden: 4 },
];

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

// Mapeo de código → archivo en storage (bucket 'guias')
const ARCHIVOS: Record<string, string> = {
  "INTRO-00": "guias/INTRO-00-presentacion-curso.html",
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
 */
export async function cargarGuiasAutomaticas(
  supabase: SupabaseClient,
  cursoId: string,
  nivel: string
): Promise<void> {
  // Normalizar nivel
  const nivelNorm = (nivel || "").toLowerCase().trim();

  // Construir la lista de guías a insertar
  const guiasNivel = GUIAS_POR_NIVEL[nivelNorm] || [];
  const todasLasGuias = [...GUIAS_SIEMPRE, ...guiasNivel, ...GUIAS_BONUS];

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
