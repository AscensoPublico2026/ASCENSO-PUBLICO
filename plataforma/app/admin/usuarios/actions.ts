"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";
import { correoCredencialesCliente, correoCursoListo } from "@/lib/email";

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

// Valida un correo electrónico de forma simple (hay algo antes y después de @, y un punto en el dominio).
function esCorreoValido(correo: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo);
}

/**
 * Actualiza el CORREO de un usuario. El correo vive en DOS lugares y ambos
 * deben quedar consistentes para que el usuario pueda iniciar sesión con el
 * nuevo correo:
 *   - profiles.correo  (lo que se muestra en la plataforma)
 *   - auth.users.email (la credencial real de inicio de sesión)
 * Se normaliza a minúsculas, igual que en el resto del sistema.
 */
export async function actualizarCorreoUsuario(userId: string, formData: FormData) {
  await requireAdmin();
  const correo = String(formData.get("correo") || "").trim().toLowerCase();
  if (!correo) throw new Error("El correo no puede estar vacío.");
  if (!esCorreoValido(correo)) throw new Error("El correo no tiene un formato válido.");
  const supabase = createAdminClient();

  // 1) Auth (login): confirmar el correo para que quede usable de inmediato.
  const { error: authErr } = await supabase.auth.admin.updateUserById(userId, {
    email: correo,
    email_confirm: true,
  });
  if (authErr) {
    // Caso típico: el correo ya está en uso por otra cuenta.
    throw new Error(`No se pudo actualizar el correo de acceso: ${authErr.message}`);
  }
  // 2) profiles (lo que ve la plataforma).
  await supabase.from("profiles").update({ correo }).eq("id", userId);

  revalidatePath("/admin/usuarios");
}

/**
 * Actualiza el CELULAR de un usuario (solo en profiles; Auth no lo usa para
 * el login en esta plataforma).
 */
export async function actualizarCelularUsuario(userId: string, formData: FormData) {
  await requireAdmin();
  const celular = String(formData.get("celular") || "").trim();
  const supabase = createAdminClient();
  await supabase.from("profiles").update({ celular: celular || null }).eq("id", userId);
  revalidatePath("/admin/usuarios");
}

/**
 * Edita TODOS los datos del perfil de una sola vez: nombre, correo y celular.
 * Mantiene la consistencia del correo entre profiles y Auth. Solo actualiza
 * el correo en Auth si realmente cambió, para no reenviar confirmaciones
 * innecesarias.
 */
export async function actualizarPerfilUsuario(userId: string, formData: FormData) {
  await requireAdmin();
  const nombre = String(formData.get("nombre") || "").trim();
  const correo = String(formData.get("correo") || "").trim().toLowerCase();
  const celular = String(formData.get("celular") || "").trim();
  if (!nombre) throw new Error("El nombre no puede estar vacío.");
  if (!correo) throw new Error("El correo no puede estar vacío.");
  if (!esCorreoValido(correo)) throw new Error("El correo no tiene un formato válido.");

  const supabase = createAdminClient();

  // ¿Cambió el correo respecto del actual? Solo tocar Auth si cambió.
  const { data: actual } = await supabase.from("profiles").select("correo").eq("id", userId).single();
  const correoCambio = (actual?.correo || "").trim().toLowerCase() !== correo;

  if (correoCambio) {
    const { error: authErr } = await supabase.auth.admin.updateUserById(userId, {
      email: correo,
      email_confirm: true,
    });
    if (authErr) throw new Error(`No se pudo actualizar el correo de acceso: ${authErr.message}`);
  }
  try { await supabase.auth.admin.updateUserById(userId, { user_metadata: { nombre } }); } catch { /* ignore */ }

  await supabase.from("profiles").update({ nombre, correo, celular: celular || null }).eq("id", userId);

  revalidatePath("/admin/usuarios");
}

/**
 * Reenvía al usuario la notificación de "tu curso ya está disponible" al
 * correo que tenga registrado en ese momento. Útil cuando se le corrigió el
 * correo (el primer aviso llegó a un correo equivocado) o cuando el cliente
 * dice que no le llegó. Fuerza el reenvío aunque el curso ya estuviera
 * disponible (a diferencia del aviso automático al habilitar el curso).
 */
export async function reenviarNotificacionCurso(userId: string) {
  await requireAdmin();
  const supabase = createAdminClient();

  const { data: profile, error } = await supabase
    .from("profiles")
    .select("correo, nombre")
    .eq("id", userId)
    .single();
  if (error || !profile?.correo) throw new Error("No se encontró el correo de este usuario.");

  // ¿Tiene ya un curso disponible? Si lo tiene, avisamos "disponible ahora".
  const { data: curso } = await supabase
    .from("cursos")
    .select("estado")
    .eq("usuario_id", userId)
    .order("created_at", { ascending: false })
    .limit(1)
    .maybeSingle();
  const disponibleAhora = curso?.estado === "disponible";

  await correoCursoListo(profile.correo, profile.nombre || "", disponibleAhora);

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
