import Link from "next/link";
import { requireAdmin } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

export default async function AdminCursos() {
  await requireAdmin();
  const supabase = createClient();
  const { data: cursos } = await supabase
    .from("cursos")
    .select("id,cargo_nombre,nivel,estado,opec,fecha_compra, profiles(nombre,correo), convocatorias(entidad,nombre)")
    .order("created_at", { ascending: false });

  const th: React.CSSProperties = { textAlign: "left", padding: "10px 12px", borderBottom: "2px solid var(--gris-borde)", fontSize: ".8rem", color: "var(--texto-suave)", textTransform: "uppercase" };
  const td: React.CSSProperties = { padding: "10px 12px", borderBottom: "1px solid var(--gris-borde)", fontSize: ".92rem" };

  return (
    <main style={{ maxWidth: 980, margin: "0 auto", padding: "40px 22px" }}>
      <Link href="/admin" style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>← Panel</Link>
      <h1 style={{ fontSize: "1.7rem", margin: "12px 0 20px" }}>Cursos / Clientes</h1>
      {(!cursos || cursos.length === 0) ? (
        <p style={{ color: "var(--texto-suave)" }}>Aún no hay cursos.</p>
      ) : (
        <div style={{ overflowX: "auto", background: "#fff", borderRadius: 14, border: "1px solid var(--gris-borde)" }}>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead><tr><th style={th}>Cliente</th><th style={th}>Cargo</th><th style={th}>OPEC</th><th style={th}>Entidad</th><th style={th}>Nivel</th><th style={th}>Estado</th><th style={th}></th></tr></thead>
            <tbody>
              {cursos.map((c: any) => (
                <tr key={c.id}>
                  <td style={td}>{c.profiles?.nombre || "-"}<br /><span style={{ color: "var(--texto-suave)", fontSize: ".8rem" }}>{c.profiles?.correo}</span></td>
                  <td style={td}>{c.cargo_nombre || "-"}</td>
                  <td style={td}>{c.opec || "-"}</td>
                  <td style={td}>{c.convocatorias?.entidad || c.convocatorias?.nombre || "-"}</td>
                  <td style={td}>{c.nivel || "-"}</td>
                  <td style={td}>{c.estado === "listo" ? "✅ Listo" : "⏳ En preparación"}</td>
                  <td style={td}><Link href={`/admin/cursos/${c.id}`} style={{ color: "var(--azul)", fontWeight: 700 }}>Gestionar →</Link></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </main>
  );
}
