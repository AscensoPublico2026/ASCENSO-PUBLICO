"use client";

import { useState } from "react";
import { createClient } from "@/lib/supabase/client";

export default function CambiarPassword() {
  const [abierto, setAbierto] = useState(false);
  const [pw, setPw] = useState("");
  const [pwConfirm, setPwConfirm] = useState("");
  const [loading, setLoading] = useState(false);
  const [msg, setMsg] = useState<{ type: "ok" | "error"; text: string } | null>(null);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setMsg(null);

    if (pw.length < 6) {
      setMsg({ type: "error", text: "Mínimo 6 caracteres." });
      return;
    }
    if (pw !== pwConfirm) {
      setMsg({ type: "error", text: "Las contraseñas no coinciden." });
      return;
    }

    setLoading(true);
    const supabase = createClient();
    const { error } = await supabase.auth.updateUser({ password: pw });
    setLoading(false);

    if (error) {
      setMsg({ type: "error", text: "Error: " + error.message });
    } else {
      setMsg({ type: "ok", text: "¡Contraseña actualizada!" });
      setPw("");
      setPwConfirm("");
      setTimeout(() => { setAbierto(false); setMsg(null); }, 2000);
    }
  }

  const input: React.CSSProperties = {
    width: "100%", padding: "10px 12px", borderRadius: 10, border: "1px solid var(--gris-borde)",
    fontFamily: "inherit", fontSize: ".9rem", marginTop: 4,
  };

  if (!abierto) {
    return (
      <button
        onClick={() => setAbierto(true)}
        style={{ background: "none", border: "1px solid var(--gris-borde)", borderRadius: 10, padding: "8px 14px", cursor: "pointer", fontFamily: "inherit", fontSize: ".84rem", color: "var(--texto-suave)" }}
      >
        🔑 Cambiar contraseña
      </button>
    );
  }

  return (
    <div style={{ background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 14, padding: 20, marginTop: 16, boxShadow: "0 4px 16px rgba(0,0,0,.04)" }}>
      <h3 style={{ fontSize: ".95rem", marginBottom: 12 }}>Cambiar contraseña</h3>
      <form onSubmit={onSubmit} style={{ display: "grid", gap: 10 }}>
        <label style={{ fontSize: ".82rem", fontWeight: 600, color: "var(--azul)" }}>
          Nueva contraseña
          <input style={input} type="password" value={pw} onChange={(e) => setPw(e.target.value)} minLength={6} required placeholder="Mínimo 6 caracteres" />
        </label>
        <label style={{ fontSize: ".82rem", fontWeight: 600, color: "var(--azul)" }}>
          Confirmar
          <input style={input} type="password" value={pwConfirm} onChange={(e) => setPwConfirm(e.target.value)} minLength={6} required placeholder="Repite tu contraseña" />
        </label>

        {msg && (
          <p style={{ fontSize: ".82rem", color: msg.type === "ok" ? "var(--verde)" : "#b00" }}>{msg.text}</p>
        )}

        <div style={{ display: "flex", gap: 10 }}>
          <button type="submit" disabled={loading} className="btn btn-oro" style={{ padding: "8px 18px", fontSize: ".85rem" }}>
            {loading ? "Guardando..." : "Guardar"}
          </button>
          <button type="button" onClick={() => { setAbierto(false); setMsg(null); }} style={{ background: "none", border: "none", color: "var(--texto-suave)", cursor: "pointer", fontSize: ".84rem" }}>
            Cancelar
          </button>
        </div>
      </form>
    </div>
  );
}
