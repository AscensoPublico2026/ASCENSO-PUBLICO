"use server";

import { createAdminClient } from "@/lib/supabase/server";
import { firmaIntegridad, urlCheckout } from "@/lib/wompi";
import { SITE_URL } from "@/lib/site";
import {
  SIM_INTENTOS,
  SIM_PRECIO_CENTAVOS,
  generarReferenciaSimulacro,
  generarToken,
  producto,
} from "@/lib/simulacroPago";

export type EstadoCompra = { error?: string; url?: string };

const CORREO_OK = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

/**
 * Crea la compra del simulacro completo y devuelve la URL del checkout de
 * Wompi (PSE, Nequi, Bancolombia o tarjeta). No crea usuario: el acceso se
 * entrega después con un enlace que lleva el token.
 */
export async function iniciarCompraSimulacro(
  _prev: EstadoCompra,
  formData: FormData
): Promise<EstadoCompra> {
  const nombre = String(formData.get("nombre") || "").trim();
  const correo = String(formData.get("correo") || "").trim().toLowerCase();
  const celular = String(formData.get("celular") || "").replace(/\D/g, "");
  const productoId = String(formData.get("producto") || "").trim();

  if (nombre.length < 3) return { error: "Escribe tu nombre completo." };
  if (!CORREO_OK.test(correo)) return { error: "Revisa tu correo: ahí te llega el acceso." };
  if (celular.length < 10) return { error: "Escribe tu celular a 10 dígitos." };

  const prod = producto(productoId);
  if (!prod) return { error: "Elige el simulacro que quieres presentar." };
  if (!prod.disponible) {
    return { error: "Ese simulacro todavía no está disponible. Escríbenos por WhatsApp y te avisamos apenas salga." };
  }

  const referencia = generarReferenciaSimulacro();
  const token = generarToken();

  const supabase = createAdminClient();
  const { error } = await supabase.from("compras_simulacro").insert({
    referencia,
    token,
    nombre,
    correo,
    celular,
    producto: prod.id,
    producto_nombre: prod.nombre,
    monto_centavos: SIM_PRECIO_CENTAVOS,
    max_intentos: SIM_INTENTOS,
  });

  if (error) {
    console.error("No se pudo registrar la compra del simulacro:", error);
    return { error: "No pudimos iniciar el pago. Intenta de nuevo o escríbenos por WhatsApp." };
  }

  const firma = firmaIntegridad(referencia, SIM_PRECIO_CENTAVOS);
  const url = urlCheckout({
    reference: referencia,
    amountInCents: SIM_PRECIO_CENTAVOS,
    signature: firma,
    redirectUrl: `${SITE_URL}/simulacro-completo/gracias`,
  });

  return { url };
}
