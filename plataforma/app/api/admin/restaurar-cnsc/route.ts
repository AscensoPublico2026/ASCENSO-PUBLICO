import { NextResponse } from "next/server";
import { createClient, createAdminClient } from "@/lib/supabase/server";
import { restaurarBaseCNSC } from "@/lib/autocargarGuias";

/**
 * API Route: /api/admin/restaurar-cnsc
 *
 * Repone el bloque base (INTRO-00, GEN-01..03, 4 guías de nivel y bonus) en TODOS
 * los cursos de CNSC (no Procuraduría) que lo perdieron. Idempotente: no duplica
 * y no toca los cursos que ya lo tienen. Solo admin.
 *
 * USO: visita /api/admin/restaurar-cnsc estando logueado como admin.
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
    const n = await restaurarBaseCNSC(admin, c.id);
    if (n > 0) { detalle.push({ curso: c.id, cargo: c.cargo_nombre, opec: c.opec, guias_restauradas: n }); total += n; }
  }
  return NextResponse.json({ ok: true, cursos_revisados: cursos?.length || 0, cursos_reparados: detalle.length, guias_insertadas: total, detalle });
}
