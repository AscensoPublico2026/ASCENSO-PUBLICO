/**
 * Banco de preguntas del SIMULACRO GRATIS.
 *
 * Se basa en las guías FIJAS del curso (Generales + Por Nivel):
 *   - GEN-01 Estado y Función Pública
 *   - GEN-02 Relación Estado-Ciudadano
 *   - GEN-03 Marco Institucional
 *   - <NIVEL>-COM-01/02  (competencias comportamentales del nivel)
 *   - <NIVEL>-ESP-01/02  (competencias específicas / alcance del cargo)
 *
 * Cada pregunta lleva su `guia` para que la retroalimentación final diga
 * exactamente qué guía reforzar (conecta con el producto).
 *
 * ⚠️ CONTENIDO BORRADOR: las preguntas marcadas con `borrador: true` son
 * ejemplos para que el equipo las COMPLETE hasta 20 por nivel y las VERIFIQUE
 * contra el contenido real de cada guía y la norma vigente antes de publicar.
 */

export type NivelSimulacro = "asistencial" | "tecnico" | "profesional";

export interface GuiaRef {
  codigo: string;
  titulo: string;
}

export interface PreguntaSimulacro {
  id: string;
  /** Tema para agrupar la retroalimentación. */
  tema: string;
  /** Guía real que se debe reforzar si falla. */
  guia: GuiaRef;
  enunciado: string;
  /** 4 opciones. */
  opciones: string[];
  /** Índice (0-3) de la opción correcta. */
  correcta: number;
  explicacion: string;
  /** true mientras sea ejemplo sin verificar. */
  borrador?: boolean;
}

export const NIVELES: { id: NivelSimulacro; nombre: string; emoji: string }[] = [
  { id: "asistencial", nombre: "Asistencial", emoji: "🧰" },
  { id: "tecnico", nombre: "Técnico", emoji: "🛠️" },
  { id: "profesional", nombre: "Profesional", emoji: "🎓" },
];

// Guías generales (comunes a los 3 niveles)
const GEN_01: GuiaRef = { codigo: "GEN-01", titulo: "Estado y Función Pública" };
const GEN_02: GuiaRef = { codigo: "GEN-02", titulo: "Relación Estado-Ciudadano" };
const GEN_03: GuiaRef = { codigo: "GEN-03", titulo: "Marco Institucional" };

/** Preguntas GENERALES (se incluyen en los 3 niveles). */
const GENERALES: PreguntaSimulacro[] = [
  {
    id: "gen-209",
    tema: "Estado y Función Pública",
    guia: GEN_01,
    enunciado:
      "Según el art. 209 de la Constitución, ¿con fundamento en qué principios se desarrolla la función administrativa?",
    opciones: [
      "Igualdad, moralidad, eficacia, economía, celeridad, imparcialidad y publicidad",
      "Solo legalidad y jerarquía",
      "Libre competencia y autonomía de la voluntad",
      "Reserva, confidencialidad y discrecionalidad",
    ],
    correcta: 0,
    explicacion:
      "El art. 209 C.P. establece que la función administrativa está al servicio del interés general y se rige por los principios de igualdad, moralidad, eficacia, economía, celeridad, imparcialidad y publicidad.",
    borrador: true,
  },
  {
    id: "gen-ramas",
    tema: "Estado y Función Pública",
    guia: GEN_01,
    enunciado: "Las ramas del poder público en Colombia (art. 113 C.P.) son:",
    opciones: [
      "Legislativa, ejecutiva y judicial",
      "Nacional, departamental y municipal",
      "Central, descentralizada y autónoma",
      "Civil, militar y de control",
    ],
    correcta: 0,
    explicacion:
      "El art. 113 C.P. señala que son ramas del poder público la legislativa, la ejecutiva y la judicial (además de los órganos autónomos e independientes).",
    borrador: true,
  },
  {
    id: "gen-dp-general",
    tema: "Relación Estado-Ciudadano",
    guia: GEN_02,
    enunciado:
      "Como regla general, ¿en cuántos días HÁBILES debe resolverse un derecho de petición (Ley 1755 de 2015)?",
    opciones: ["15 días hábiles", "10 días hábiles", "30 días hábiles", "5 días hábiles"],
    correcta: 0,
    explicacion:
      "La regla general es 15 días hábiles. Casos especiales: documentos e información (10 días) y consultas (30 días).",
    borrador: true,
  },
  {
    id: "gen-dp-docs",
    tema: "Relación Estado-Ciudadano",
    guia: GEN_02,
    enunciado:
      "Una petición de DOCUMENTOS E INFORMACIÓN debe resolverse, salvo norma especial, en:",
    opciones: ["10 días hábiles", "15 días hábiles", "30 días hábiles", "3 días hábiles"],
    correcta: 0,
    explicacion:
      "La Ley 1755 de 2015 fija un término especial de 10 días hábiles para peticiones de documentos e información.",
    borrador: true,
  },
  {
    id: "gen-cnsc",
    tema: "Marco Institucional",
    guia: GEN_03,
    enunciado: "¿Cuál es la función principal de la CNSC?",
    opciones: [
      "Administrar y vigilar la carrera administrativa",
      "Nombrar directamente a los servidores públicos",
      "Sancionar penalmente a los funcionarios",
      "Fijar los salarios del sector privado",
    ],
    correcta: 0,
    explicacion:
      "La CNSC es el órgano autónomo responsable de la administración y vigilancia de las carreras de los servidores públicos (art. 130 C.P.).",
    borrador: true,
  },
  {
    id: "gen-merito",
    tema: "Marco Institucional",
    guia: GEN_03,
    enunciado:
      "El ingreso a los cargos de carrera administrativa se hace, por regla general, mediante:",
    opciones: [
      "Concurso público de méritos",
      "Libre nombramiento del jefe",
      "Recomendación política",
      "Antigüedad en la entidad",
    ],
    correcta: 0,
    explicacion:
      "El ingreso y ascenso en los empleos de carrera se rige por el mérito, mediante concurso público (art. 125 C.P.).",
    borrador: true,
  },
];

/** Preguntas POR NIVEL. */
const POR_NIVEL: Record<NivelSimulacro, PreguntaSimulacro[]> = {
  asistencial: [
    {
      id: "asi-alcance",
      tema: "Alcance del cargo Asistencial",
      guia: { codigo: "ASI-ESP-02", titulo: "Alcance del Cargo Asistencial" },
      enunciado: "Los empleos del nivel ASISTENCIAL se caracterizan por:",
      opciones: [
        "Actividades de apoyo y de simple ejecución, complementarias de otros niveles",
        "Formular políticas públicas de la entidad",
        "Dirigir y coordinar áreas misionales",
        "Asesorar jurídicamente al representante legal",
      ],
      correcta: 0,
      explicacion:
        "El nivel asistencial agrupa empleos con funciones de apoyo y actividades complementarias o de simple ejecución (Decreto 1083 de 2015).",
      borrador: true,
    },
    {
      id: "asi-atencion",
      tema: "Atención y colaboración (Asistencial)",
      guia: { codigo: "ASI-COM-02", titulo: "Atención y Colaboración en el Servicio Público (Nivel Asistencial)" },
      enunciado:
        "Un ciudadano llega molesto por una demora que no dependió de ti. ¿Cuál es la actuación más adecuada?",
      opciones: [
        "Escuchar con calma, orientarlo y darle una ruta de solución",
        "Responderle en el mismo tono para hacerte respetar",
        "Ignorarlo hasta que se calme",
        "Pedirle que regrese otro día",
      ],
      correcta: 0,
      explicacion:
        "La competencia de orientación al usuario y autocontrol exige mantener la calma, escuchar y orientar hacia una solución.",
      borrador: true,
    },
    {
      id: "asi-comp",
      tema: "Competencias del Nivel Asistencial",
      guia: { codigo: "ASI-ESP-01", titulo: "Competencias del Nivel Asistencial" },
      enunciado:
        "¿Cuál es una competencia comportamental COMÚN a todos los servidores (Decreto 815 de 2018)?",
      opciones: [
        "Orientación al usuario y al ciudadano",
        "Visión estratégica",
        "Liderazgo de grupos de trabajo",
        "Toma de decisiones de política",
      ],
      correcta: 0,
      explicacion:
        "Entre las competencias comunes están: aprendizaje continuo, orientación a resultados, orientación al usuario y al ciudadano, compromiso con la organización, trabajo en equipo y adaptación al cambio.",
      borrador: true,
    },
  ],
  tecnico: [
    {
      id: "tec-alcance",
      tema: "Alcance del cargo Técnico",
      guia: { codigo: "TEC-ESP-02", titulo: "Alcance del Cargo Técnico" },
      enunciado: "Los empleos del nivel TÉCNICO se caracterizan por:",
      opciones: [
        "Desarrollar procesos y aplicar conocimientos técnicos o tecnológicos propios del área",
        "Definir las políticas generales de la entidad",
        "Ejercer la representación legal",
        "Realizar únicamente labores de aseo y mensajería",
      ],
      correcta: 0,
      explicacion:
        "El nivel técnico comprende empleos con funciones que exigen el desarrollo de procesos y la aplicación de conocimientos técnicos o tecnológicos (Decreto 1083 de 2015).",
      borrador: true,
    },
    {
      id: "tec-comp",
      tema: "Competencias del Nivel Técnico",
      guia: { codigo: "TEC-ESP-01", titulo: "Competencias del Nivel Técnico" },
      enunciado:
        "En la prueba de competencias, la 'confiabilidad técnica' se refiere a:",
      opciones: [
        "Aplicar de forma correcta y consistente los conocimientos de tu área",
        "Dirigir equipos de alto nivel",
        "Diseñar la política pública sectorial",
        "Representar judicialmente a la entidad",
      ],
      correcta: 0,
      explicacion:
        "La confiabilidad técnica implica dominar y aplicar de manera correcta y consistente los conocimientos técnicos del empleo. (Verificar redacción con la guía.)",
      borrador: true,
    },
  ],
  profesional: [
    {
      id: "pro-alcance",
      tema: "Alcance del cargo Profesional",
      guia: { codigo: "PRO-ESP-02", titulo: "Alcance del Cargo Profesional" },
      enunciado: "Los empleos del nivel PROFESIONAL se caracterizan por:",
      opciones: [
        "Aplicar conocimientos propios de una profesión para actividades de coordinación, análisis y ejecución",
        "Realizar tareas de simple ejecución",
        "Únicamente vigilar la carrera administrativa",
        "Ejercer control fiscal",
      ],
      correcta: 0,
      explicacion:
        "El nivel profesional agrupa empleos cuya naturaleza demanda la aplicación de los conocimientos propios de una profesión (Decreto 1083 de 2015).",
      borrador: true,
    },
    {
      id: "pro-comp",
      tema: "Competencias del Nivel Profesional",
      guia: { codigo: "PRO-ESP-01", titulo: "Competencias del Nivel Profesional" },
      enunciado:
        "¿Cuál de estas suele evaluarse como competencia del nivel profesional?",
      opciones: [
        "Aprendizaje continuo y experticia profesional",
        "Predominio de actividades manuales",
        "Funciones exclusivamente de mensajería",
        "Ninguna competencia comportamental",
      ],
      correcta: 0,
      explicacion:
        "En el nivel profesional se evalúan competencias como aprendizaje continuo, experticia profesional, trabajo en equipo y creatividad e innovación. (Verificar con la guía.)",
      borrador: true,
    },
  ],
};

/** Devuelve las preguntas del simulacro de un nivel (Generales + del nivel). */
export function preguntasDeNivel(nivel: NivelSimulacro): PreguntaSimulacro[] {
  return [...GENERALES, ...POR_NIVEL[nivel]];
}

export function nombreNivel(nivel: NivelSimulacro): string {
  return NIVELES.find((n) => n.id === nivel)?.nombre ?? nivel;
}

export function esNivelValido(v: string): v is NivelSimulacro {
  return v === "asistencial" || v === "tecnico" || v === "profesional";
}
