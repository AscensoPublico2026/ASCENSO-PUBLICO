import "server-only";

import crypto from "crypto";

const VERSION = "v1";
const ALGORITHM = "aes-256-gcm";

function encryptionKey(): Buffer {
  const raw = process.env.DOCUMENT_ENCRYPTION_KEY?.trim();
  if (!raw) {
    throw new Error("Falta configurar DOCUMENT_ENCRYPTION_KEY para proteger la cédula.");
  }

  if (/^[a-f0-9]{64}$/i.test(raw)) return Buffer.from(raw, "hex");

  const decoded = Buffer.from(raw, "base64");
  if (decoded.length === 32) return decoded;

  throw new Error("DOCUMENT_ENCRYPTION_KEY debe contener 32 bytes en hexadecimal o Base64.");
}

export function normalizeCedula(value: string): string {
  return value.replace(/[^0-9]/g, "");
}

export function isValidCedula(value: string): boolean {
  return /^\d{5,12}$/.test(value) && !/^0+$/.test(value);
}

export function encryptCedula(value: string): string {
  const normalized = normalizeCedula(value);
  if (!isValidCedula(normalized)) {
    throw new Error("Ingresa un número de cédula válido, de 5 a 12 dígitos.");
  }

  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv(ALGORITHM, encryptionKey(), iv);
  const encrypted = Buffer.concat([cipher.update(normalized, "utf8"), cipher.final()]);
  const authTag = cipher.getAuthTag();

  return [VERSION, iv.toString("base64url"), authTag.toString("base64url"), encrypted.toString("base64url")].join(":");
}

export function decryptCedula(payload: string | null | undefined): string | null {
  if (!payload) return null;
  try {
    const [version, ivValue, tagValue, encryptedValue] = payload.split(":");
    if (version !== VERSION || !ivValue || !tagValue || !encryptedValue) {
      console.error("[cedula] Formato cifrado inválido; verifica la versión del dato.");
      return null;
    }

    const decipher = crypto.createDecipheriv(ALGORITHM, encryptionKey(), Buffer.from(ivValue, "base64url"));
    decipher.setAuthTag(Buffer.from(tagValue, "base64url"));
    return Buffer.concat([
      decipher.update(Buffer.from(encryptedValue, "base64url")),
      decipher.final(),
    ]).toString("utf8");
  } catch {
    // Alerta operativa sin incluir el payload ni ningún dato personal.
    console.error("[cedula] No se pudo descifrar la identificación; verifica DOCUMENT_ENCRYPTION_KEY.");
    return null;
  }
}

export function maskCedula(last4: string | null | undefined): string {
  return last4 ? `•••• ${last4}` : "—";
}
