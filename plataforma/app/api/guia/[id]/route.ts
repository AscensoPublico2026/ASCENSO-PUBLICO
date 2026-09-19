import { NextRequest, NextResponse } from "next/server";
import { createClient, createAdminClient } from "@/lib/supabase/server";
import { SITE_URL } from "@/lib/site";

export const dynamic = "force-dynamic";

// Sirve el HTML de una guía con el Content-Type correcto (text/html; charset=utf-8)
// para que el navegador la RENDERICE (no muestre el código) y respete los acentos.
// La RLS de guias_curso limita el acceso a guías de cursos propios (o admin).
export async function GET(_req: NextRequest, { params }: { params: { id: string } }) {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return new NextResponse("No autorizado", { status: 401 });

  const { data: guia } = await supabase
    .from("guias_curso")
    .select("archivo_path")
    .eq("id", params.id)
    .single();
  if (!guia?.archivo_path) return new NextResponse("No encontrado", { status: 404 });

  const admin = createAdminClient();
  let html: string | null = null;

  // Normalizar la ruta del bucket: los HTML se guardan bajo "guias/<basename>",
  // sin importar si el archivo_path del curso dice "guias/..." o "simulacro/..."
  // (los simulacros se registran con carpeta "simulacro/"). Así el simulacro se
  // encuentra igual que cualquier guía.
  const basename = guia.archivo_path.replace(/^(guias|simulacro)\//, "");
  const rutaBucket = `guias/${basename}`;

  // 1) Intentar servir desde el bucket (caso normal). Probamos la ruta
  //    normalizada y, por compatibilidad, la ruta original tal cual.
  let blob = (await admin.storage.from("guias").download(rutaBucket)).data;
  if (!blob && rutaBucket !== guia.archivo_path) {
    blob = (await admin.storage.from("guias").download(guia.archivo_path)).data;
  }
  if (blob) {
    html = await blob.text();
  } else {
    // 2) Auto-sanación: el HTML aún no está en el bucket (guía recién publicada).
    //    Lo tomamos de public/seed-guias/ (incluido en el deploy), lo subimos al
    //    bucket bajo la ruta normalizada y lo servimos. Así una guía nueva
    //    funciona SOLA, sin tener que correr /api/admin/seed-guias a mano.
    try {
      const res = await fetch(`${SITE_URL}/seed-guias/${basename}`);
      if (res.ok) {
        const content = await res.arrayBuffer();
        await admin.storage.from("guias").upload(rutaBucket, content, {
          contentType: "text/html; charset=utf-8",
          upsert: true,
        });
        html = Buffer.from(content).toString("utf-8");
      }
    } catch {
      // Si falla, caemos al 404 de abajo.
    }
  }

  if (html == null) return new NextResponse("No disponible", { status: 404 });

  return new NextResponse(html, {
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "private, no-store",
    },
  });
}
