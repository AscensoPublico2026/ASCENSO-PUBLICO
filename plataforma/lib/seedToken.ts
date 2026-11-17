/**
 * Token interno para leer /public/seed-guias/ desde el propio servidor.
 *
 * Las guías HTML del curso se incluyen en el deploy dentro de public/seed-guias/
 * para poder subirlas al bucket privado `guias`. Sin protección, cualquiera podía
 * abrirlas en https://ascensopublico.com/seed-guias/<archivo>.html sin comprar.
 *
 * El middleware solo deja pasar las peticiones a /seed-guias/ que traen el header
 * `x-seed-token` con este valor. El token se deriva de SUPABASE_SERVICE_ROLE_KEY
 * (nunca se expone la llave) y funciona tanto en el runtime Edge como en Node.
 */
export const SEED_TOKEN_HEADER = "x-seed-token";

export async function seedToken(): Promise<string | null> {
  const secret = process.env.SEED_GUIAS_TOKEN || process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!secret) return null;
  const data = new TextEncoder().encode(`seed-guias:${secret}`);
  const digest = await globalThis.crypto.subtle.digest("SHA-256", data);
  return Array.from(new Uint8Array(digest))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

/** Headers para que el servidor lea un archivo de /seed-guias/. */
export async function seedFetchHeaders(): Promise<Record<string, string>> {
  const token = await seedToken();
  return token ? { [SEED_TOKEN_HEADER]: token } : {};
}
