import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase/server";

/**
 * DEBUG/ADMIN: Reprocesa una referencia de pago manualmente.
 * Ejecuta el flujo de procesarReferencia paso a paso y captura errores.
 * 
 * Uso: /api/admin/reprocesar?ref=AP-1781566912576-929e825378c2
 */
export async function GET(req: NextRequest) {
  const ref = req.nextUrl.searchParams.get("ref");
  if (!ref) return NextResponse.json({ error: "Falta ?ref=" });

  const supabase = createAdminClient();
  const log: any = {};

  try {
    // 1. Buscar preregistro
    const { data: pre, error: preErr } = await supabase.from("preregistros").select("*").eq("referencia", ref).single();
    log.preregistro = pre ? { encontrado: true, correo: pre.correo, nivel: pre.nivel } : { encontrado: false, error: preErr?.message };
    if (!pre) return NextResponse.json({ log, resultado: "No hay preregistro con esa referencia" });

    // 2. Buscar pago
    const { data: pago } = await supabase.from("pagos").select("*").eq("referencia", ref).single();
    log.pago = pago ? { estado: pago.estado, usuario_id: pago.usuario_id, curso_id: pago.curso_id } : { encontrado: false };

    // 3. Listar usuarios para ver si el correo ya existe
    const { data: list } = await supabase.auth.admin.listUsers();
    const existente = list?.users?.find((u: any) => (u.email || "").toLowerCase() === (pre.correo || "").toLowerCase());
    log.usuario_auth_existente = existente ? { existe: true, id: existente.id } : { existe: false };

    // 4. Intentar crear usuario
    let userId: string | null = null;
    if (existente) {
      userId = existente.id;
      log.accion_usuario = "Usuario ya existía en Auth, se reutiliza";
    } else {
      const { data: created, error: createErr } = await supabase.auth.admin.createUser({
        email: pre.correo,
        password: crypto.randomUUID(),
        email_confirm: true,
        user_metadata: { nombre: pre.nombre },
      });
      if (createErr) {
        log.accion_usuario = "ERROR al crear: " + createErr.message;
        return NextResponse.json({ log, resultado: "Falló createUser" });
      }
      userId = created?.user?.id ?? null;
      log.accion_usuario = "Usuario creado: " + userId;
    }

    if (!userId) return NextResponse.json({ log, resultado: "No se obtuvo userId" });

    // 5. Asegurar profile
    const { error: profErr } = await supabase.from("profiles").upsert({
      id: userId,
      nombre: pre.nombre,
      correo: pre.correo,
      celular: pre.celular,
      rol: "estudiante",
    }, { onConflict: "id" });
    log.profile = profErr ? "ERROR: " + profErr.message : "OK";

    // 6. Verificar si ya hay curso
    const { data: cursoExistente } = await supabase.from("cursos").select("id").eq("usuario_id", userId).maybeSingle();
    let cursoId: string;

    if (cursoExistente) {
      cursoId = cursoExistente.id;
      log.curso = "Ya existía: " + cursoId;
    } else {
      // 7. Crear curso
      const ahora = new Date();
      const deadline = new Date(ahora.getTime() + 12 * 3600 * 1000);
      const { data: curso, error: cursoErr } = await supabase
        .from("cursos")
        .insert({
          usuario_id: userId,
          convocatoria_id: pre.convocatoria_id,
          opec: pre.opec,
          cargo_nombre: pre.cargo_nombre,
          nivel: pre.nivel,
          manual_pdf_path: pre.manual_pdf_path,
          estado: "en_preparacion",
          fecha_compra: ahora.toISOString(),
          preparacion_deadline: deadline.toISOString(),
        })
        .select("id")
        .single();
      if (cursoErr) {
        log.curso = "ERROR: " + cursoErr.message;
        return NextResponse.json({ log, resultado: "Falló crear curso" });
      }
      cursoId = curso!.id;
      log.curso = "Creado: " + cursoId;

      // 8. Auto-cargar guías
      try {
        const { cargarGuiasAutomaticas } = await import("@/lib/autocargarGuias");
        await cargarGuiasAutomaticas(supabase, cursoId, pre.nivel);
        log.guias = "Auto-cargadas OK";
      } catch (e: any) {
        log.guias = "ERROR: " + e.message;
      }
    }

    // 9. Actualizar pago
    const { error: pagoErr } = await supabase
      .from("pagos")
      .update({ estado: "aprobado", usuario_id: userId, curso_id: cursoId })
      .eq("referencia", ref);
    log.actualizar_pago = pagoErr ? "ERROR: " + pagoErr.message : "OK - estado aprobado";

    // 10. Marcar preregistro procesado
    await supabase.from("preregistros").update({ procesado: true }).eq("referencia", ref);

    return NextResponse.json({ log, resultado: "✅ COMPLETADO - ahora puedes ir a /activar y crear contraseña", userId, cursoId });
  } catch (e: any) {
    log.error_fatal = e.message;
    return NextResponse.json({ log, resultado: "Excepción: " + e.message });
  }
}
