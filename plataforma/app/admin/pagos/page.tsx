import Link from "next/link";
import { requireAdmin } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { toTitleCase } from "@/lib/format";

export const dynamic = "force-dynamic";

function fmtCOP(centavosOmonto: number) {
  // monto se guarda en pesos (PRECIO_COP). Mostramos en COP.
  return new Intl.NumberFormat("es-CO", { style: "currency", currency: "COP", maximumFractionDigits: 0 }).format(centavosOmonto || 0);
}

export default async function AdminPagos() {
  await requireAdmin();
  const supabase = createClient();

  const { data: pagos } = await supabase
    .from("pagos")
    .select("referencia, monto, estado, usuario_id, curso_id, wompi_transaction_id")
    .eq("estado", "aprobado")
    .order("referencia", { ascending: false });

  // Traer datos de cliente y curso para relacionarlos.
  const userIds = Array.from(new Set((pagos || []).map((p: any) => p.usuario_id).filter(Boolean)));
  const cursoIds = Array.from(new Set((pagos || []).map((p: any) => p.curso_id).filter(Boolean)));

  const profilesMap: Record<string, any> = {};
  const cursosMap: Record<string, any> = {};
  if (userIds.length) {
    const { data } = await supabase.from("profiles").select("id,nombre,correo,celular").in("id", userIds);
    (data || []).forEach((p: any) => { profilesMap[p.id] = p; });
  }
  if (cursoIds.length) {
    const { data } = await supabase.from("cursos").select("id,cargo_nombre,opec,nivel").in("id", cursoIds);
    (data || []).forEach((c: any) => { cursosMap[c.id] = c; });
  }

  const th: React.CSSProperties = { textAlign: "left", padding: "10px 12px", borderBottom: "2px solid var(--gris-borde)", fontSize: ".8rem", color: "var(--texto-suave)", textTransform: "uppercase" };
  const td: React.CSSProperties = { padding: "10px 12px", borderBottom: "1px solid var(--gris-borde)", fontSize: ".9rem", verticalAlign: "top" };

  return (
    <main style={{ maxWidth: 1000, margin: "0 auto", padding: "40px 22px" }}>
      <Link href="/admin" style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>← Panel</Link>
      <h1 style={{ fontSize: "1.7rem", margin: "12px 0 6px" }}>Pagos aprobados ({pagos?.length ?? 0})</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 20, fontSize: ".9rem" }}>
        Cada pago aprobado relacionado con su cliente y curso. Haz clic en "Ver curso" para gestionarlo.
      </p>

      {(!pagos || pagos.length === 0) ? (
        <p style={{ color: "var(--texto-suave)" }}>Aún no hay pagos aprobados.</p>
      ) : (
        <div style={{ overflowX: "auto", background: "#fff", borderRadius: 14, border: "1px solid var(--gris-borde)" }}>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead><tr>
              <th style={th}>Cliente</th>
              <th style={th}>Cargo / OPEC</th>
              <th style={th}>Monto</th>
              <th style={th}>Referencia</th>
              <th style={th}></th>
            </tr></thead>
            <tbody>
              {pagos.map((p: any) => {
                const cli = profilesMap[p.usuario_id];
                const cur = cursosMap[p.curso_id];
                return (
                  <tr key={p.referencia}>
                    <td style={td}>
                      <strong>{cli?.nombre ? toTitleCase(cli.nombre) : "—"}</strong><br />
                      <span style={{ color: "var(--texto-suave)", fontSize: ".8rem" }}>{cli?.correo || "—"}{cli?.celular ? ` · ${cli.celular}` : ""}</span>
                    </td>
                    <td style={td}>
                      {cur?.cargo_nombre ? toTitleCase(cur.cargo_nombre) : "—"}<br />
                      <span style={{ color: "var(--texto-suave)", fontSize: ".8rem" }}>OPEC {cur?.opec || "—"} · {cur?.nivel || "—"}</span>
                    </td>
                    <td style={td}>{fmtCOP(p.monto)}</td>
                    <td style={td}><span style={{ fontSize: ".74rem", color: "var(--texto-suave)", wordBreak: "break-all" }}>{p.referencia}</span></td>
                    <td style={td}>
                      {p.curso_id ? (
                        <Link href={`/admin/cursos/${p.curso_id}`} style={{ color: "var(--azul)", fontWeight: 700, whiteSpace: "nowrap" }}>Ver curso →</Link>
                      ) : <span style={{ color: "var(--texto-suave)", fontSize: ".8rem" }}>sin curso</span>}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      <p style={{ color: "var(--texto-suave)", fontSize: ".82rem", marginTop: 16 }}>
        💡 Si ves un pago repetido del mismo cliente con la misma OPEC, puede ser una compra de prueba. El curso no se duplica (se reutiliza por usuario+OPEC), pero el registro de pago sí queda.
      </p>
    </main>
  );
}
