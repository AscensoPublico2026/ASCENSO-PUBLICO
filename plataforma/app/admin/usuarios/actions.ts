"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";
import { correoCredencialesCliente } from "@/lib/email";

// Misma contraseña genérica usada en la creación manual de clientes
// (admin/crear-cliente/actions.ts). Se centraliza aquí para reenviarla.
const PASSWORD_GENERICA = "nuevoestudiante2026";

/**
 * Actualiza el nombre visible de un usuario (en profiles y en Auth).
 * Útil para que el admin ponga/corrija su propio nombre o el de un cliente.
 */
export async function actualizarNombreUsuario(userId: string, formData: FormData) {
  await requireAdmin();
  const nombre = String(formData.get("nombre") || "").trim();
  if (!nombre) throw new Error("El nombre no puede estar vacío.");
  const supabase = createAdminClient();
  await supabase.from("profiles").update({ nombre }).eq("id", userId);
  try { await supabase.auth.admin.updateUserById(userId, { user_metadata: { nombre } }); } catch { /* ignore */ }
  revalidatePath("/admin/usuarios");
}

/**
 * Elimina un usuario y todos sus datos asociados (cursos, guías, pagos).
 * NO permite eliminar admins.
 */
export async function eliminarUsuario(userId: string) {
  await requireAdmin();
  const supabase = createAdminClient();

  // Verificar que no sea admin
  const { data: profile } = await supabase.from("profiles").select("rol").eq("id", userId).single();
  if (profile?.rol === "admin") {
    throw new Error("No se puede eliminar un administrador.");
  }

  // Eliminar cursos (cascade elimina guias_curso)
  await supabase.from("cursos").delete().eq("usuario_id", userId);

  // Eliminar pagos
  await supabase.from("pagos").delete().eq("usuario_id", userId);

  // Eliminar profile
  await supabase.from("profiles").delete().eq("id", userId);

  // Eliminar usuario de Auth
  await supabase.auth.admin.deleteUser(userId);

  revalidatePath("/admin/usuarios");
}

/**
 * Inhabilita un usuario (elimina su sesión pero mantiene los datos).
 * El usuario no podrá iniciar sesión hasta que se le reactive.
 */
export async function inhabilitarUsuario(userId: string) {
  await requireAdmin();
  const supabase = createAdminClient();

  // Verificar que no sea admin
  const { data: profile } = await supabase.from("profiles").select("rol").eq("id", userId).single();
  if (profile?.rol === "admin") {
    throw new Error("No se puede inhabilitar un administrador.");
  }

  // Banear al usuario en Auth (no puede iniciar sesión)
  await supabase.auth.admin.updateUserById(userId, { ban_duration: "876000h" }); // ~100 años

  revalidatePath("/admin/usuarios");
}

/**
 * Rehabilita un usuario previamente inhabilitado.
 */
export async function rehabilitarUsuario(userId: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.auth.admin.updateUserById(userId, { ban_duration: "none" });
  revalidatePath("/admin/usuarios");
}

/**
 * Reenvía el correo de credenciales (usuario + contraseña genérica) a un
 * cliente, sin crear ni tocar su curso. Además RESETEA su contraseña a la
 * genérica ("nuevoestudiante2026"), para que el correo que recibe siempre
 * sea válido para iniciar sesión (si el cliente ya la había cambiado por su
 * cuenta, esto la reemplaza de nuevo por la genérica).
 */
export async function reenviarCredenciales(userId: string) {
  await requireAdmin();
  const supabase = createAdminClient();

  const { data: profile, error } = await supabase
    .from("profiles")
    .select("correo, nombre")
    .eq("id", userId)
    .single();
  if (error || !profile?.correo) throw new Error("No se encontró el correo de este usuario.");

  await supabase.auth.admin.updateUserById(userId, { password: PASSWORD_GENERICA });
  await correoCredencialesCliente(profile.correo, profile.nombre || "", PASSWORD_GENERICA);

  revalidatePath("/admin/usuarios");
}
