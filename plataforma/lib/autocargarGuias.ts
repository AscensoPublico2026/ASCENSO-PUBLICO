/**
 * Auto-carga de guías al confirmar pago.
 * 
 * Regla de asignación (basada en biblioteca/biblioteca.json):
 * - Introducción (INTRO-00): Día 1 → siempre
 * - Generales (GEN-01, GEN-02, GEN-03): Días 2-4 → siempre
 * - Por Nivel (ASI/TEC/PRO según curso.nivel): Días 5-8 → según nivel
 * - Bonus (BON-01): sin día fijo → siempre (sección bonus)
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
