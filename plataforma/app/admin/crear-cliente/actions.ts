"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";
import { cargarGuiasAutomaticas, copiarPlanDesdeOPEC } from "@/lib/autocargarGuias";

export type CrearClienteResult = {
  ok: boolean;
  error?: string;
  userId?: string;
  cursoId?: string;
};

/**
 * Crea un usuario (Auth + profile) y un curso con guías auto-cargadas.
 * Flujo equivalente a procesarReferencia pero sin requerir pago/preregistro.
 * Para casos donde el pago se hace por transferencia/consignación/efectivo.
 */
export async function crearClienteManual(
  _prev: CrearClienteResult | null,
  formData: FormData
): Promise<CrearClienteResult> {
  await requireAdmin();

  // --- Extraer campos ---
  const nombre = String(formData.get("nombre") || "").trim();
  const correo = String(formData.get("correo") || "").trim().toLowerCase();
  const celular = String(formData.get("celular") || "").trim();
  const password = String(formData.get("password") || "").trim();
  const convocatoria_id = String(formData.get("convocatoria_id") || "").trim() || null;
  const opec = String(formData.get("opec") || "").trim() || null;
  const cargo_nombre = String(formData.get("cargo_nombre") || "").trim() || null;
  const nivel = String(formData.get("nivel") || "").trim().toLowerCase() || null;

  // --- Validaciones básicas ---
  if (!nombre) return { ok: false, error: "El nombre es obligatorio." };
  if (!correo) return { ok: false, error: "El correo es obligatorio." };
  if (!password || password.length < 6) return { ok: false, error: "La contraseña debe tener al menos 6 caracteres." };
  if (!nivel) return { ok: false, error: "El nivel es obligatorio (asistencial, técnico o profesional)." };

  const supabase = createAdminClient();

  try {
    // --- 1. Crear o recuperar usuario en Auth ---
    let userId: string | null = null;

    // Buscar si el correo ya existe en Auth
    const { data: list } = await supabase.auth.admin.listUsers();
    const existente = list?.users?.find(
      (u: any) => (u.email || "").toLowerCase() === correo
    );

    if (existente) {
      userId = existente.id;
      // Actualizar contraseña con la nueva proporcionada
      await supabase.auth.admin.updateUserById(existente.id, {
        password,
        user_metadata: { nombre },
      });
    } else {
      // Crear nuevo usuario
      const { data: created, error: createErr } = await supabase.auth.admin.createUser({
        email: correo,
        password,
        email_confirm: true,
        user_metadata: { nombre },
      });
      if (createErr) {
        return { ok: false, error: "Error al crear usuario: " + createErr.message };
      }
      userId = created?.user?.id ?? null;
    }

    if (!userId) return { ok: false, error: "No se pudo obtener el ID del usuario." };

    // --- 2. Asegurar profile ---
    const { error: profErr } = await supabase.from("profiles").upsert(
      {
        id: userId,
        nombre,
        correo,
        celular: celular || null,
        rol: "estudiante",
      },
      { onConflict: "id" }
    );
    if (profErr) return { ok: false, error: "Error al crear perfil: " + profErr.message };

    // --- 3. Verificar si ya tiene curso del mismo OPEC ---
    if (opec) {
      const { data: cursoExistente } = await supabase
        .from("cursos")
        .select("id")
        .eq("usuario_id", userId)
        .eq("opec", opec)
        .maybeSingle();
      if (cursoExistente) {
        return { ok: false, error: `Este usuario ya tiene un curso para el OPEC ${opec}. ID: ${cursoExistente.id}` };
      }
    }

    // --- 4. Crear el curso ---
    const VIGENCIA_DIAS = 90;
    const ahora = new Date();
    const deadline = new Date(ahora.getTime() + 24 * 3600 * 1000); // +24h
    const vence = new Date(ahora.getTime() + VIGENCIA_DIAS * 86400 * 1000);

    const { data: curso, error: cursoErr } = await supabase
      .from("cursos")
      .insert({
        usuario_id: userId,
        convocatoria_id: convocatoria_id,
        opec,
        cargo_nombre,
        nivel,
        estado: "en_preparacion",
        fecha_compra: ahora.toISOString(),
        preparacion_deadline: deadline.toISOString(),
        fecha_vencimiento: vence.toISOString(),
      })
      .select("id")
      .single();

    if (cursoErr || !curso) {
      return { ok: false, error: "Error al crear curso: " + (cursoErr?.message || "sin respuesta") };
    }

    const cursoId = curso.id;

    // --- 5. Auto-cargar guías ---
    // Primero intentar copiar plan de otro curso del mismo OPEC
    let copiadoPlan = false;
    if (opec) {
      try {
        copiadoPlan = await copiarPlanDesdeOPEC(supabase, cursoId, opec);
      } catch { /* ignore */ }
    }

    // Si no había plan previo, cargar las guías base según nivel
    if (!copiadoPlan && nivel) {
      try {
        await cargarGuiasAutomaticas(supabase, cursoId, nivel);
      } catch (err: any) {
        console.error("[crearClienteManual] Error en auto-carga de guías:", err);
      }
    }

    // --- 6. Crear registro de pago como "aprobado" (pago manual/externo) ---
    const referencia = `MANUAL-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
    await supabase.from("pagos").insert({
      usuario_id: userId,
      curso_id: cursoId,
      referencia,
      monto: 30000000, // $300.000 COP en centavos
      estado: "aprobado",
    });

    // --- Revalidar rutas admin ---
    revalidatePath("/admin");
    revalidatePath("/admin/cursos");
    revalidatePath("/admin/usuarios");
    revalidatePath("/admin/pagos");

    return { ok: true, userId, cursoId };
  } catch (e: any) {
    return { ok: false, error: "Error inesperado: " + e.message };
  }
}
