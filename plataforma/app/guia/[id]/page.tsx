import { redirect, notFound } from "next/navigation";
import { createClient, createAdminClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

// Visor de guía embebida. La RLS limita guias_curso a las de cursos del propio
// usuario; la URL firmada (temporal) se genera en el servidor con service role.
export default async function GuiaPage({ params }: { params: { id: string } }) {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  const { data: guia } = await supabase
    .from("guias_curso")
    .select("id,titulo,archivo_path")
    .eq("id", params.id)
    .single();

  if (!guia || !guia.archivo_path) notFound();

  const admin = createAdminClient();
  const { data: signed } = await admin.storage.from("guias").createSignedUrl(guia.archivo_path, 60 * 30);
  if (!signed?.signedUrl) notFound();

  return (
    <main style={{ height: "100vh", display: "flex", flexDirection: "column" }}>
      <div style={{ padding: "10px 16px", borderBottom: "1px solid var(--gris-borde)", display: "flex", justifyContent: "space-between", alignItems: "center", background: "#fff" }}>
        <a href="/perfil" style={{ color: "var(--azul)", fontWeight: 700 }}>← Mi perfil</a>
        <strong style={{ color: "var(--azul)" }}>{guia.titulo}</strong>
      </div>
      <iframe src={signed.signedUrl} style={{ flex: 1, width: "100%", border: "none" }} title={guia.titulo} />
    </main>
  );
}
