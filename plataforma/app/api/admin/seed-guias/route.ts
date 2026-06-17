import { NextResponse } from "next/server";
import { createClient, createAdminClient } from "@/lib/supabase/server";
import { archivosSeed } from "@/lib/catalogoGuias";
import { SITE_URL } from "@/lib/site";

/**
 * API Route: /api/admin/seed-guias
 * 
 * Sube las guías HTML al bucket 'guias' de Supabase Storage.
 * Solo se puede ejecutar como admin (verifica sesión + rol).
 * 
 * USO: visita https://ascensopublico.com/api/admin/seed-guias
 * (debes estar logueado como admin)
 * 
 * La lista de guías se deriva del catálogo (biblioteca.json): todas las
 * guías publicadas que tienen archivo. Los HTML se leen desde
 * /public/seed-guias/ (embebidos en el deploy) y se suben al bucket
 * 'guias' con la ruta guias/NOMBRE.html. Es idempotente (upsert).
 */

const GUIAS = archivosSeed();

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
  const siteUrl = SITE_URL;

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
