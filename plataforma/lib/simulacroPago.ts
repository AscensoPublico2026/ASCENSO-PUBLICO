import crypto from "crypto";

/** Precio del simulacro completo, en pesos y en centavos (Wompi). */
export const SIM_PRECIO = 39000;
export const SIM_PRECIO_CENTAVOS = SIM_PRECIO * 100;

/** Días que dura el acceso y número de intentos incluidos. */
export const SIM_DIAS_ACCESO = 30;
export const SIM_INTENTOS = 2;

export type ProductoSimulacro = {
  id: string;
  convocatoria: string;
  nivel: string;
  nombre: string;
  descripcion: string;
  preguntas: number;
  minutos: number;
  disponible: boolean;
};

/**
 * Catálogo del simulacro completo, por convocatoria y por nivel dentro de la
 * convocatoria. Los que aún no tienen banco quedan con disponible:false y la
 * página los muestra como "próximamente" en lugar de cobrarlos.
 */
export const PRODUCTOS: ProductoSimulacro[] = [
  {
    id: "procuraduria-profesional",
    convocatoria: "Procuraduría General de la Nación 2026",
    nivel: "Profesional y asesor",
    nombre: "Simulacro completo · Procuraduría · Profesional y asesor",
    descripcion:
      "Profesional universitario, asesor y ejecutivo. Estructura y competencias de la PGN, derecho disciplinario, mecanismos de protección de derechos, contratación, conflicto de interés y juicio situacional del nivel.",
    preguntas: 100,
    minutos: 150,
    disponible: true,
  },
  {
    id: "procuraduria-tecnico",
    convocatoria: "Procuraduría General de la Nación 2026",
    nivel: "Técnico",
    nombre: "Simulacro completo · Procuraduría · Técnico",
    descripcion:
      "Sustanciadores, técnicos y tecnólogos. Núcleo común del concurso, procedimiento disciplinario, gestión documental, calidad de la información y juicio situacional del nivel.",
    preguntas: 100,
    minutos: 150,
    disponible: false,
  },
  {
    id: "procuraduria-operativo",
    convocatoria: "Procuraduría General de la Nación 2026",
    nivel: "Operativo y administrativo",
    nombre: "Simulacro completo · Procuraduría · Operativo y administrativo",
    descripcion:
      "Auxiliares, citadores y oficinistas. Núcleo común del concurso, atención al ciudadano, derecho de petición, gestión documental y juicio situacional del nivel.",
    preguntas: 100,
    minutos: 150,
    disponible: false,
  },
  {
    id: "docente",
    convocatoria: "Concurso Docente 2026",
    nivel: "Docente de aula",
    nombre: "Simulacro completo · Concurso Docente",
    descripcion:
      "Lectura crítica, razonamiento cuantitativo, competencias pedagógicas y casos de aula con el formato de la prueba de aptitudes y competencias básicas.",
    preguntas: 100,
    minutos: 150,
    disponible: false,
  },
];

export function producto(id: string): ProductoSimulacro | undefined {
  return PRODUCTOS.find((p) => p.id === id);
}

/** Token de acceso del comprador: va en el enlace, no se adivina. */
export function generarToken(): string {
  return crypto.randomBytes(24).toString("base64url");
}

/** Referencia de la compra. El prefijo SIM separa estas compras de las del curso. */
export function generarReferenciaSimulacro(): string {
  return `SIM-${Date.now()}-${crypto.randomBytes(5).toString("hex")}`;
}

export function pesos(n: number): string {
  return "$" + n.toLocaleString("es-CO");
}
