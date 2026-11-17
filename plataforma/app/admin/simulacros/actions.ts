"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";
import { correoSimulacroPagoListo } from "@/lib/email";

/** Reenvía al comprador el correo con su enlace de acceso. */
export async function reenviarAcceso(formData: FormData) {
  await requireAdmin();
  const id = String(formData.get("id") || "");
  if (!id) return;

  const supabase = createAdminClient();
  const { data: c } = await supabase.from("compras_simulacro").select("*").eq("id", id).maybeSingle();
  if (!c || c.estado !== "aprobado") return;

  await correoSimulacroPagoListo(c.correo, c.nombre, c.token, c.producto_nombre || "Simulacro completo");
  revalidatePath("/admin/simulacros");
}

/** Concede un intento adicional (por fallas técnicas o cortesía comercial). */
export async function anadirIntento(formData: FormData) {
  await requireAdmin();
  const id = String(formData.get("id") || "");
  if (!id) return;

  const supabase = createAdminClient();
  const { data: c } = await supabase.from("compras_simulacro").select("max_intentos").eq("id", id).maybeSingle();
  if (!c) return;

  await supabase
    .from("compras_simulacro")
    .update({ max_intentos: (c.max_intentos ?? 2) + 1 })
    .eq("id", id);
  revalidatePath("/admin/simulacros");
}
