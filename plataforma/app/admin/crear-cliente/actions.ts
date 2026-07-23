"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";
import { cargarGuiasAutomaticas, copiarPlanDesdeOPEC } from "@/lib/autocargarGuias";

const VIGENCIA_DIAS = 90;
// Contraseña genérica fija para todos los clientes creados manualmente.
// El estudiante la puede cambiar desde su perfil cuando quiera.
const PASSWORD_GENERICA = "nuevoestudiante2026";

export type CrearClienteResult = {
  ok: boolean;
  error?: string;
  userId?: string;
  cursoId?: string;
  correo?: string;
};

/**
 * Crea un usuario (Auth + profile) y un curso con guías auto-cargadas,
 * sin requerir pago por pasarela. Para cobros por transferencia / consignación.
 */
export async function crearClienteManual(
  _prev: CrearClienteResult | null,
  formData: FormData
): Promise<CrearClienteResult> {
  await requireAdmin();

  const nombre         = String(formData.get("nombre")         || "").trim();
  const correo         = String(formData.get("correo")         || "").trim().toLowerCase();
  const celular        = String(formData.get("celular")        || "").trim();
  const convocatoria_id = String(formData.get("convocatoria_id") || "").trim() || null;
  const opec           = String(formData.get("opec")           || "").trim() || null;
  const cargo_nombre   = String(formData.get("cargo_nombre")   || "").trim() || null;
  const nivel          = String(formData.get("nivel")          || "").trim().toLowerCase() || null;

  if (!nombre)  return { ok: false, error: "El nombre es obligatorio." };
  if (!correo)  return { ok: false, error: "El correo es obligatorio." };
  if (!nivel)   return { ok: false, error: "El nivel es obligatorio." };

  const supabase = createAdminClient();

  try {
    // 1. Crear o recuperar usuario en Auth
    let userId: string | null = null;
    const { data: list } = await supabase.auth.admin.listUsers();
    const existente = list?.users?.find(
      (u: any) => (u.email || "").toLowerCase() === correo
    );

    if (existente) {
      userId = existente.id;
      await supabase.auth.admin.updateUserById(existente.id, {
        password: PASSWORD_GENERICA,
        user_metadata: { nombre },
      });
    } else {
      const { data: created, error: createErr } = await supabase.auth.admin.createUser({
        email: correo,
        password: PASSWORD_GENERICA,
        email_confirm: true,
        user_metadata: { nombre },
      });
      if (createErr) return { ok: false, error: "Error al crear usuario: " + createErr.message };
      userId = created?.user?.id ?? null;
    }
    if (!userId) return { ok: false, error: "No se pudo obtener el ID del usuario." };

    // 2. Upsert profile
    const { error: profErr } = await supabase.from("profiles").upsert(
      { id: userId, nombre, correo, celular: celular || null, rol: "estudiante" },
      { onConflict: "id" }
    );
    if (profErr) return { ok: false, error: "Error al crear perfil: " + profErr.message };

    // 3. Verificar duplicado por OPEC
    if (opec) {
      const { data: dup } = await supabase
        .from("cursos").select("id")
        .eq("usuario_id", userId).eq("opec", opec).maybeSingle();
      if (dup) return { ok: false, error: `Este usuario ya tiene un curso para el OPEC ${opec}.` };
    }

    // 4. Crear el curso (deadline 24h, vigencia 90 días)
    const ahora    = new Date();
    const deadline = new Date(ahora.getTime() + 24 * 3600 * 1000);
    const vence    = new Date(ahora.getTime() + VIGENCIA_DIAS * 86400 * 1000);

    const { data: curso, error: cursoErr } = await supabase
      .from("cursos")
      .insert({
        usuario_id: userId,
        convocatoria_id,
        opec,
        cargo_nombre,
        nivel,
        estado: "en_preparacion",
        fecha_compra: ahora.toISOString(),
        preparacion_deadline: deadline.toISOString(),
        fecha_vencimiento: vence.toISOString(),
      })
      .select("id").single();

    if (cursoErr || !curso) {
      return { ok: false, error: "Error al crear curso: " + (cursoErr?.message || "sin respuesta") };
    }
    const cursoId = curso.id;

    // 5. Auto-cargar guías (copia plan OPEC existente o carga base por nivel)
    let copiadoPlan = false;
    if (opec) {
      try { copiadoPlan = await copiarPlanDesdeOPEC(supabase, cursoId, opec); } catch { /* ok */ }
    }
    if (!copiadoPlan && nivel) {
      try { await cargarGuiasAutomaticas(supabase, cursoId, nivel); } catch { /* ok */ }
    }

    // 6. Registrar pago manual como aprobado
    const referencia = `MANUAL-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
    await supabase.from("pagos").insert({
      usuario_id: userId,
      curso_id: cursoId,
      referencia,
      monto: 30000000, // $300.000 COP en centavos
      estado: "aprobado",
    });

    revalidatePath("/admin");
    revalidatePath("/admin/cursos");
    revalidatePath("/admin/usuarios");
    revalidatePath("/admin/pagos");

    return { ok: true, userId, cursoId, correo };
  } catch (e: any) {
    return { ok: false, error: "Error inesperado: " + e.message };
  }
}
