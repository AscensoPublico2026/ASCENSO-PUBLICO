import { NextResponse } from "next/server";
import { createClient, createAdminClient } from "@/lib/supabase/server";

/**
 * API Route: /api/admin/seed-guias
 * 
 * Sube las 17 guías HTML al bucket 'guias' de Supabase Storage.
 * Solo se puede ejecutar como admin (verifica sesión + rol).
 * 
 * USO: visita https://ascenso-publico.vercel.app/api/admin/seed-guias
 * (debes estar logueado como admin)
 * 
 * Las guías se leen desde /public/seed-guias/ (embebidas en el deploy)
 * y se suben al bucket 'guias' con la ruta guias/NOMBRE.html
 */

const GUIAS = [
  "INTRO-00-presentacion-curso.html",
  "GEN-01-estado-funcion-publica.html",
  "GEN-02-relacion-estado-ciudadano.html",
  "GEN-03-marco-institucional.html",
  "ASI-COM-01-cumplimiento-desarrollo-laboral.html",
  "ASI-COM-02-atencion-colaboracion.html",
  "ASI-ESP-01-competencias-nivel-asistencial.html",
  "ASI-ESP-02-alcance-cargo-asistencial.html",
  "TEC-COM-01-desempeno-cumplimiento.html",
  "TEC-COM-02-usuarios-trabajo-colaborativo.html",
  "TEC-ESP-01-competencias-nivel-tecnico.html",
  "TEC-ESP-02-alcance-cargo-tecnico.html",
  "PRO-COM-01-gestion-cumplimiento.html",
  "PRO-COM-02-servicio-articulacion.html",
  "PRO-ESP-01-competencias-nivel-profesional.html",
  "PRO-ESP-02-alcance-cargo-profesional.html",
  "BON-01-estrategia-cnsc.html",
];

export async function GET() {
  // Verificar que es admin
  try {
    const supabase = createClient();
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      return NextResponse.json({ error: "No autorizado. Inicia sesión primero." }, { status: 401 });
    }
    const { data: profile } = await supabase.from("profiles").select("rol").eq("id", user.id).single();
    if (!profile || profile.rol !== "admin") {
      return NextResponse.json({ error: "Solo admin puede ejecutar esto." }, { status: 403 });
    }
  } catch {
    return NextResponse.json({ error: "Error verificando autorización." }, { status: 500 });
  }

  // Subir guías
  const admin = createAdminClient();
  const results: { file: string; status: "ok" | "error"; message?: string }[] = [];
  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || "https://ascenso-publico.vercel.app";

  for (const filename of GUIAS) {
    const storagePath = `guias/${filename}`;

    try {
      // Leer el archivo desde public/seed-guias/ (servido por Next.js)
      const res = await fetch(`${siteUrl}/seed-guias/${filename}`);
      if (!res.ok) {
        results.push({ file: filename, status: "error", message: `Fetch failed: ${res.status}` });
        continue;
      }

      const content = await res.arrayBuffer();

      const { error } = await admin.storage
        .from("guias")
        .upload(storagePath, content, {
          contentType: "text/html; charset=utf-8",
          upsert: true,
        });

      if (error) {
        results.push({ file: filename, status: "error", message: error.message });
      } else {
        results.push({ file: filename, status: "ok" });
      }
    } catch (e: any) {
      results.push({ file: filename, status: "error", message: e.message || "Unknown error" });
    }
  }

  const ok = results.filter((r) => r.status === "ok").length;
  const fail = results.filter((r) => r.status === "error").length;

  return NextResponse.json({
    message: `Subidas: ${ok}/${GUIAS.length}. Errores: ${fail}.`,
    results,
  });
}
