/**
 * URL canónica del sitio — FUENTE ÚNICA.
 *
 * Usa SIEMPRE `SITE_URL` en vez de hardcodear el dominio o repetir
 * `process.env.NEXT_PUBLIC_SITE_URL || "..."` por todo el código.
 * Así, si el dominio cambia, se ajusta en un solo lugar (o vía la variable
 * de entorno NEXT_PUBLIC_SITE_URL) y no quedan dominios viejos regados.
 */
export const SITE_URL = (
  process.env.NEXT_PUBLIC_SITE_URL || "https://ascensopublico.com"
).replace(/\/+$/, "");
