import Link from "next/link";
import { requireAdmin } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

export default async function AdminHome() {
  await requireAdmin();
  const supabase = createClient();
  const { count: cursos } = await supabase.from("cursos").select("*", { count: "exact", head: true });
  const { count: convs } = await supabase.from("convocatorias").select("*", { count: "exact", head: true });

  const card: React.CSSProperties = { background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 16, padding: 26, boxShadow: "var(--sombra)", display: "block" };

  return (
    <main style={{ maxWidth: 880, margin: "0 auto", padding: "48px 22px" }}>
      <h1 style={{ fontSize: "1.9rem", marginBottom: 24 }}>Panel de administración</h1>
      <div style={{ display: "grid", gap: 18, gridTemplateColumns: "repeat(auto-fit,minmax(240px,1fr))" }}>
        <Link href="/admin/cursos" style={card}>
          <div style={{ fontSize: "2rem", fontFamily: "'Source Serif 4',serif", color: "var(--azul)" }}>{cursos ?? 0}</div>
          <div style={{ fontWeight: 700, marginTop: 6 }}>Cursos / Clientes →</div>
          <div style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>Ver clientes, subir guías y habilitar acceso.</div>
        </Link>
        <Link href="/admin/convocatorias" style={card}>
          <div style={{ fontSize: "2rem", fontFamily: "'Source Serif 4',serif", color: "var(--azul)" }}>{convs ?? 0}</div>
          <div style={{ fontWeight: 700, marginTop: 6 }}>Convocatorias →</div>
          <div style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>Agregar, editar y activar/desactivar.</div>
        </Link>
      </div>
    </main>
  );
}
