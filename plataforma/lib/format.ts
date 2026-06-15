/**
 * Utilidades de normalización de texto para Ascenso Público.
 * Regla: el usuario escribe como quiera, el sistema lo organiza bonito.
 */

/**
 * Convierte texto a Title Case (primera letra de cada palabra en mayúscula).
 * Maneja tildes y caracteres especiales del español.
 * Ejemplo: "JULIO CESAR" → "Julio Cesar", "juan pablo" → "Juan Pablo"
 */
export function toTitleCase(text: string): string {
  if (!text) return "";
  return text
    .trim()
    .toLowerCase()
    .replace(/(?:^|\s)\S/g, (match) => match.toUpperCase());
}

/**
 * Normaliza nombre completo (nombres + apellidos) para mostrar.
 * Ejemplo: toDisplayName("julio cesar", "deavila perez") → "Julio Cesar Deávila Perez"
 */
export function toDisplayName(nombres: string, apellidos: string): string {
  const n = toTitleCase(nombres);
  const a = toTitleCase(apellidos);
  return [n, a].filter(Boolean).join(" ");
}

/**
 * Normaliza el nombre del cargo para mostrar en tarjetas y perfil.
 * Ejemplo: "TECNICO ADMINISTRATIVO" → "Técnico Administrativo"
 */
export function normalizeCargo(cargo: string): string {
  return toTitleCase(cargo);
}
