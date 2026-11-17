import Link from "next/link";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";
import { SIM_PRECIO } from "@/lib/simulacroPago";
import { SITE_URL } from "@/lib/site";
import { reenviarAcceso, anadirIntento } from "./actions";

export const dynamic = "force-dynamic";

function fecha(v?: string | null) {
  if (!v) return "—";
  return new Date(v).toLocaleString("es-CO", { dateStyle: "medium", timeStyle: "short" });
}

const COLOR: Record<string, string> = {
  aprobado: "var(--verde)",
  pendiente: "var(--ambar)",
  rechazado: "#9B2226",
};

export default async function AdminSimulacros() {
  await requireAdmin();
  const supabase = createAdminClient();

  const { data: compras } = await supabase
    .from("compras_simulacro")
    .select("*")
    .order("creado_en", { ascending: false })
    .limit(300);

  const lista = compras || [];
  const aprobadas = lista.filter((c) => c.estado === "aprobado");
  const presentados = aprobadas.filter((c) => (c.intentos_usados ?? 0) > 0);
  const puntajes = presentados.map((c) => Number(c.ultimo_puntaje || 0));
  const promedio = puntajes.length ? Math.round(puntajes.reduce((a, b) => a + b, 0) / puntajes.length) : null;

  const th: React.CSSProperties = { textAlign: "left", padding: "10px 12px", borderBottom: "2px solid var(--gris-borde)", fontSize: ".78rem", color: "var(--texto-suave)", textTransform: "uppercase" };
  const td: React.CSSProperties = { padding: "10px 12px", borderBottom: "1px solid var(--gris-borde)", fontSize: ".88rem", verticalAlign: "top" };

  return (
    <main style={{ maxWidth: 1180, margin: "0 auto", padding: "40px 22px" }}>
      <Link href="/admin" style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>← Panel</Link>
      <h1 style={{ fontSize: "1.7rem", margin: "12px 0 6px" }}>Simulacros de pago</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 22, fontSize: ".9rem" }}>
        Compras del simulacro completo de ${SIM_PRECIO.toLocaleString("es-CO")}. El acceso va por enlace con token, sin cuenta de usuario.
      </p>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(170px,1fr))", gap: 12, marginBottom: 26 }}>
        {[
          { t: "Compras aprobadas", v: aprobadas.length },
          { t: "Ingresos", v: "$" + (aprobadas.length * SIM_PRECIO).toLocaleString("es-CO") },
          { t: "Ya lo presentaron", v: `${presentados.length} de ${aprobadas.length}` },
          { t: "Puntaje promedio", v: promedio == null ? "—" : promedio + "%" },
          { t: "Pendientes de pago", v: lista.filter((c) => c.estado === "pendiente").length },
        ].map((k) => (
          <div key={k.t} style={{ background: "var(--blanco)", border: "1px solid var(--gris-borde)", borderRadius: 12, padding: "14px 16px" }}>
            <div style={{ fontSize: ".74rem", color: "var(--texto-suave)", textTransform: "uppercase", letterSpacing: ".04em" }}>{k.t}</div>
            <div style={{ fontSize: "1.45rem", fontWeight: 800, color: "var(--azul)" }}>{k.v}</div>
          </div>
        ))}
      </div>

      {lista.length === 0 ? (
        <p style={{ color: "var(--texto-suave)" }}>Todavía no hay compras del simulacro completo.</p>
      ) : (
        <div style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", background: "var(--blanco)", borderRadius: 12 }}>
            <thead>
              <tr>
                <th style={th}>Comprador</th>
                <th style={th}>Simulacro</th>
                <th style={th}>Estado</th>
                <th style={th}>Intentos</th>
                <th style={th}>Puntaje</th>
                <th style={th}>Compra</th>
                <th style={th}>Acceso</th>
              </tr>
            </thead>
            <tbody>
              {lista.map((c) => (
                <tr key={c.id}>
                  <td style={td}>
                    <strong>{c.nombre}</strong>
                    <br />
                    <a href={`mailto:${c.correo}`} style={{ color: "var(--azul)" }}>{c.correo}</a>
                    <br />
                    {c.celular && (
                      <a href={`https://wa.me/57${c.celular}`} target="_blank" rel="noopener" style={{ color: "var(--verde)", fontSize: ".84rem" }}>
                        WhatsApp {c.celular}
                      </a>
                    )}
                  </td>
                  <td style={td}>
                    {c.producto_nombre || c.producto}
                    <br />
                    <code style={{ fontSize: ".74rem", color: "var(--texto-suave)" }}>{c.referencia}</code>
                  </td>
                  <td style={{ ...td, color: COLOR[c.estado] || "var(--texto)", fontWeight: 700 }}>
                    {c.estado}
                    {c.metodo_pago && <div style={{ fontWeight: 400, fontSize: ".78rem", color: "var(--texto-suave)" }}>{c.metodo_pago}</div>}
                  </td>
                  <td style={td}>
                    {c.intentos_usados ?? 0} de {c.max_intentos ?? 2}
                  </td>
                  <td style={td}>{c.ultimo_puntaje == null ? "—" : Math.round(Number(c.ultimo_puntaje)) + "%"}</td>
                  <td style={td}>
                    {fecha(c.creado_en)}
                    {c.expira_en && <div style={{ fontSize: ".78rem", color: "var(--texto-suave)" }}>vence {fecha(c.expira_en)}</div>}
                  </td>
                  <td style={td}>
                    {c.estado === "aprobado" ? (
                      <>
                        <input
                          readOnly
                          value={`${SITE_URL}/simulacro-completo/${c.token}`}
                          onFocus={(e) => e.currentTarget.select()}
                          style={{ width: 210, fontSize: ".72rem", padding: "5px 7px", border: "1px solid var(--gris-borde)", borderRadius: 7 }}
                        />
                        <div style={{ display: "flex", gap: 8, marginTop: 7 }}>
                          <form action={reenviarAcceso}>
                            <input type="hidden" name="id" value={c.id} />
                            <button type="submit" style={{ fontSize: ".76rem", border: "1px solid var(--gris-borde)", borderRadius: 7, padding: "4px 9px", background: "#fff", cursor: "pointer" }}>
                              Reenviar correo
                            </button>
                          </form>
                          <form action={anadirIntento}>
                            <input type="hidden" name="id" value={c.id} />
                            <button type="submit" style={{ fontSize: ".76rem", border: "1px solid var(--gris-borde)", borderRadius: 7, padding: "4px 9px", background: "#fff", cursor: "pointer" }}>
                              +1 intento
                            </button>
                          </form>
                        </div>
                      </>
                    ) : (
                      <span style={{ color: "var(--texto-suave)", fontSize: ".82rem" }}>Sin pago confirmado</span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </main>
  );
}
