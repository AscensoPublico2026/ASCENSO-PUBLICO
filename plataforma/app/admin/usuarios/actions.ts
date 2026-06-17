"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";

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
