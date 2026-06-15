import { redirect, notFound } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

// Visor de guía: muestra el HTML embebido a través de /api/guia/[id],
// que lo sirve con el Content-Type correcto para que se renderice bien.
export default async function GuiaPage({ params }: { params: { id: string } }) {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  const { data: guia } = await supabase
    .from("guias_curso")
    .select("titulo,archivo_path")
    .eq("id", params.id)
    .single();
  if (!guia?.archivo_path) notFound();

  return (
    <main style={{ height: "100vh", display: "flex", flexDirection: "column" }}>
      <div style={{ padding: "10px 16px", borderBottom: "1px solid var(--gris-borde)", display: "flex", justifyContent: "space-between", alignItems: "center", background: "#fff" }}>
        <a href="/perfil" style={{ color: "var(--azul)", fontWeight: 700 }}>← Mi perfil</a>
        <strong style={{ color: "var(--azul)" }}>{guia.titulo}</strong>
      </div>
      <iframe src={`/api/guia/${params.id}`} style={{ flex: 1, width: "100%", border: "none" }} title={guia.titulo} />
    </main>
  );
}
