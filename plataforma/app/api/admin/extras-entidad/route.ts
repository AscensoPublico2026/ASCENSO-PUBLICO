import { NextResponse } from "next/server";
import { createClient, createAdminClient } from "@/lib/supabase/server";
import { asegurarExtrasEntidad, actualizarNivelDIAN } from "@/lib/autocargarGuias";

/**
 * API Route: /api/admin/extras-entidad
 *
 * Agrega a los cursos CNSC ya existentes las guías adicionales de su entidad
 * (DIAN: ponderaciones y puntaje en el Día 1 + estrategia de tiempo e integridad
 * como bonus) y, en los cursos DIAN, cambia las comportamentales genéricas de la
 * CNSC (Días 5-8) por el set DIAN de su nivel. Idempotente: no duplica. Solo admin.
 *
 * USO: visita /api/admin/extras-entidad estando logueado como admin.
 * Recuerda correr antes /api/admin/seed-guias para subir los HTML nuevos.
 */
export async function GET() {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: "No autorizado." }, { status: 401 });
  const { data: profile } = await supabase.from("profiles").select("rol").eq("id", user.id).single();
  if (!profile || profile.rol !== "admin") return NextResponse.json({ error: "Solo admin." }, { status: 403 });

  const admin = createAdminClient();
  const { data: cursos, error } = await admin.from("cursos").select("id, cargo_nombre, opec");
  if (error) return NextResponse.json({ error: error.message }, { status: 500 });

  const detalle: any[] = [];
  let total = 0;
  for (const c of cursos || []) {
    const n = (await asegurarExtrasEntidad(admin, c.id)) + (await actualizarNivelDIAN(admin, c.id));
    if (n > 0) { detalle.push({ curso: c.id, cargo: c.cargo_nombre, opec: c.opec, guias_agregadas: n }); total += n; }
  }
  return NextResponse.json({ ok: true, cursos_revisados: cursos?.length || 0, cursos_actualizados: detalle.length, guias_insertadas: total, detalle });
}
