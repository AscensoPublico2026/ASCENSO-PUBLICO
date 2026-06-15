import { NextRequest, NextResponse } from "next/server";
import { createClient, createAdminClient } from "@/lib/supabase/server";

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
  const { data: blob, error } = await admin.storage.from("guias").download(guia.archivo_path);
  if (error || !blob) return new NextResponse("No disponible", { status: 404 });

  const html = await blob.text();
  return new NextResponse(html, {
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "private, no-store",
    },
  });
}
