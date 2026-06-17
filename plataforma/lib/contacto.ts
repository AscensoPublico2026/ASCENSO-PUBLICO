/**
 * Datos de contacto — FUENTE ÚNICA.
 *
 * Centraliza el WhatsApp (Business) y el correo para no repetir el número
 * por todo el código. Si cambia, se ajusta en un solo lugar.
 */
export const WHATSAPP_NUMERO = "573170905177"; // formato internacional, sin "+"
export const CORREO_CONTACTO = "ascensopublico@gmail.com";

/** Construye un enlace de WhatsApp (opcionalmente con mensaje prellenado). */
export function waUrl(mensaje?: string): string {
  const base = `https://wa.me/${WHATSAPP_NUMERO}`;
  return mensaje ? `${base}?text=${encodeURIComponent(mensaje)}` : base;
}

/** Mensajes prellenados reutilizables según el contexto del botón. */
export const WA_MENSAJES = {
  general: "Hola, quiero información del curso personalizado de Ascenso Público.",
  comprar: "Hola, quiero mi curso personalizado de Ascenso Público.",
  asesoria: "Hola, tengo una duda antes de comprar el curso de Ascenso Público.",
  soporte: "Hola, necesito ayuda con mi curso de Ascenso Público.",
  convocatoria: "Hola, quiero saber si mi convocatoria/cargo está disponible en Ascenso Público.",
};
