import { createClient, createAdminClient } from "@/lib/supabase/server";
import { inhabilitarUsuario, eliminarUsuario } from "./actions";

export const dynamic = "force-dynamic";

export default async function AdminUsuarios() {
  const supabase = createClient();
  const { data: profiles } = await supabase
    .from("profiles")
    .select("id, nombre, correo, celular, rol, created_at")
    .order("created_at", { ascending: false });

  const box: React.CSSProperties = { background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 14, padding: 22, boxShadow: "0 4px 20px rgba(10,42,94,.06)" };

  return (
    <div style={{ padding: "40px 28px", maxWidth: 960 }}>
      <h1 style={{ fontSize: "1.7rem", margin: "0 0 8px" }}>Usuarios</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 24 }}>Gestiona los usuarios registrados en la plataforma.</p>

      {(!profiles || profiles.length === 0) ? (
        <p style={{ color: "var(--texto-suave)" }}>No hay usuarios registrados.</p>
      ) : (
        <div style={{ display: "grid", gap: 12 }}>
          {profiles.map((u: any) => (
            <div key={u.id} style={{ ...box, display: "flex", alignItems: "center", gap: 14 }}>
              {/* Avatar */}
              <div style={{
                width: 42, height: 42, borderRadius: "50%",
                background: u.rol === "admin" ? "linear-gradient(135deg, #E8A33D, #F6C56B)" : "var(--azul)",
                color: u.rol === "admin" ? "#0A2A5E" : "#fff",
                display: "flex", alignItems: "center", justifyContent: "center",
                fontWeight: 800, fontSize: ".85rem", flexShrink: 0,
              }}>
                {(u.nombre || u.correo || "?").charAt(0).toUpperCase()}
              </div>

              {/* Info */}
              <div style={{ flex: 1 }}>
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <strong style={{ fontSize: ".92rem" }}>{u.nombre || "Sin nombre"}</strong>
                  {u.rol === "admin" && (
                    <span style={{ fontSize: ".68rem", fontWeight: 800, background: "linear-gradient(135deg, #E8A33D, #F6C56B)", color: "#0A2A5E", padding: "2px 8px", borderRadius: 6 }}>ADMIN</span>
                  )}
                </div>
                <div style={{ color: "var(--texto-suave)", fontSize: ".82rem" }}>
                  {u.correo} {u.celular ? `· ${u.celular}` : ""}
                </div>
                <div style={{ color: "var(--texto-suave)", fontSize: ".72rem", marginTop: 2 }}>
                  Registrado: {new Date(u.created_at).toLocaleDateString("es-CO")}
                </div>
              </div>

              {/* Acciones (no permitir eliminar admins) */}
              {u.rol !== "admin" && (
                <div style={{ display: "flex", gap: 8, flexShrink: 0 }}>
                  <form action={eliminarUsuario.bind(null, u.id)}>
                    <button
                      style={{ background: "none", border: "1px solid #fcc", borderRadius: 8, padding: "6px 12px", cursor: "pointer", fontFamily: "inherit", fontSize: ".78rem", color: "#b00" }}
                    >
                      Eliminar
                    </button>
                  </form>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
