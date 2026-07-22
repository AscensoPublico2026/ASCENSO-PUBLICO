import Link from "next/link";
import { requireAdmin } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { toTitleCase } from "@/lib/format";
import { eliminarPago } from "./actions";

export const dynamic = "force-dynamic";

// El monto se guarda en CENTAVOS (PRECIO_COP * 100). Para mostrar en COP, /100.
function fmtCOP(montoCentavos: number) {
  const pesos = (montoCentavos || 0) / 100;
  return new Intl.NumberFormat("es-CO", { style: "currency", currency: "COP", maximumFractionDigits: 0 }).format(pesos);
}

export default async function AdminPagos() {
  await requireAdmin();
  const supabase = createClient();

  const { data: pagos } = await supabase
    .from("pagos")
    .select("referencia, monto, estado, usuario_id, curso_id, wompi_transaction_id")
    .eq("estado", "aprobado")
    .order("referencia", { ascending: false });

  const refs = (pagos || []).map((p: any) => p.referencia);
  const userIds = Array.from(new Set((pagos || []).map((p: any) => p.usuario_id).filter(Boolean)));
  const cursoIds = Array.from(new Set((pagos || []).map((p: any) => p.curso_id).filter(Boolean)));

  const profilesMap: Record<string, any> = {};
  const cursosMap: Record<string, any> = {};
  const preMap: Record<string, any> = {};

  if (userIds.length) {
    const { data } = await supabase.from("profiles").select("id,nombre,correo,celular").in("id", userIds);
    (data || []).forEach((p: any) => { profilesMap[p.id] = p; });
  }
  if (cursoIds.length) {
    const { data } = await supabase.from("cursos").select("id,cargo_nombre,opec,nivel").in("id", cursoIds);
    (data || []).forEach((c: any) => { cursosMap[c.id] = c; });
  }
  // Respaldo: datos del preregistro (sirve aunque el pago no esté enlazado a usuario/curso)
  if (refs.length) {
    const { data } = await supabase.from("preregistros").select("referencia,nombre,correo,celular,opec,cargo_nombre,nivel").in("referencia", refs);
    (data || []).forEach((p: any) => { preMap[p.referencia] = p; });
  }

  const th: React.CSSProperties = { textAlign: "left", padding: "10px 12px", borderBottom: "2px solid var(--gris-borde)", fontSize: ".8rem", color: "var(--texto-suave)", textTransform: "uppercase" };
  const td: React.CSSProperties = { padding: "10px 12px", borderBottom: "1px solid var(--gris-borde)", fontSize: ".9rem", verticalAlign: "top" };

  return (
    <main style={{ maxWidth: 1040, margin: "0 auto", padding: "40px 22px" }}>
      <Link href="/admin" style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>← Panel</Link>
      <h1 style={{ fontSize: "1.7rem", margin: "12px 0 6px" }}>Pagos aprobados ({pagos?.length ?? 0})</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 20, fontSize: ".9rem" }}>
        Cada pago aprobado relacionado con su cliente y curso. Usa "Eliminar" para limpiar pagos de prueba.
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
              <th style={th}></th>
            </tr></thead>
            <tbody>
              {pagos.map((p: any) => {
                const cli = profilesMap[p.usuario_id];
                const cur = cursosMap[p.curso_id];
                const pre = preMap[p.referencia];
                const nombre = cli?.nombre || pre?.nombre;
                const correo = cli?.correo || pre?.correo;
                const celular = cli?.celular || pre?.celular;
                const cargo = cur?.cargo_nombre || pre?.cargo_nombre;
                const opec = cur?.opec || pre?.opec;
                const nivel = cur?.nivel || pre?.nivel;
                const huerfano = !p.usuario_id && !p.curso_id;
                return (
                  <tr key={p.referencia} style={huerfano ? { background: "rgba(214,69,69,.05)" } : undefined}>
                    <td style={td}>
                      <strong>{nombre ? toTitleCase(nombre) : "—"}</strong>
                      {huerfano && <span style={{ fontSize: ".68rem", color: "#b00", fontWeight: 700, marginLeft: 6 }}>(huérfano)</span>}
                      <br />
                      <span style={{ color: "var(--texto-suave)", fontSize: ".8rem" }}>{correo || "—"}{celular ? ` · ${celular}` : ""}</span>
                    </td>
                    <td style={td}>
                      {cargo ? toTitleCase(cargo) : "—"}<br />
                      <span style={{ color: "var(--texto-suave)", fontSize: ".8rem" }}>OPEC {opec || "—"} · {nivel || "—"}</span>
                    </td>
                    <td style={td}>{fmtCOP(p.monto)}</td>
                    <td style={td}><span style={{ fontSize: ".74rem", color: "var(--texto-suave)", wordBreak: "break-all" }}>{p.referencia}</span></td>
                    <td style={td}>
                      {p.curso_id ? (
                        <Link href={`/admin/cursos/${p.curso_id}`} style={{ color: "var(--azul)", fontWeight: 700, whiteSpace: "nowrap" }}>Ver curso →</Link>
                      ) : <span style={{ color: "var(--texto-suave)", fontSize: ".8rem" }}>sin curso</span>}
                    </td>
                    <td style={td}>
                      <form action={eliminarPago.bind(null, p.referencia)}>
                        <button style={{ background: "none", border: "1px solid #fcc", borderRadius: 8, padding: "6px 12px", cursor: "pointer", fontFamily: "inherit", fontSize: ".78rem", color: "#b00", whiteSpace: "nowrap" }}>
                          Eliminar
                        </button>
                      </form>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      <p style={{ color: "var(--texto-suave)", fontSize: ".82rem", marginTop: 16 }}>
        💡 Los pagos marcados como <strong style={{ color: "#b00" }}>(huérfano)</strong> son pagos sin cliente/curso asociado (por ejemplo, pruebas viejas o registros que quedaron tras borrar perfiles). Puedes eliminarlos sin afectar a ningún cliente.
      </p>
    </main>
  );
}
