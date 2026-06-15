"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [pw, setPw] = useState("");
  const [err, setErr] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setErr("");
    const supabase = createClient();
    const { error } = await supabase.auth.signInWithPassword({ email, password: pw });
    if (error) {
      setErr("Correo o contraseña incorrectos.");
      setLoading(false);
      return;
    }
    router.push("/perfil");
  }

  const input: React.CSSProperties = {
    width: "100%", padding: "12px 14px", borderRadius: 12, border: "1px solid var(--gris-borde)",
    fontFamily: "inherit", fontSize: ".95rem", marginTop: 6,
  };

  return (
    <main style={{ maxWidth: 420, margin: "0 auto", padding: "70px 22px" }}>
      <h1 style={{ fontSize: "1.8rem", textAlign: "center", marginBottom: 8 }}>Inicia sesión</h1>
      <p style={{ color: "var(--texto-suave)", textAlign: "center", marginBottom: 24 }}>Accede a tu curso.</p>
      <form onSubmit={onSubmit}>
        <label style={{ fontWeight: 700, fontSize: ".9rem", color: "var(--azul)" }}>Correo
          <input style={input} type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>
        <label style={{ fontWeight: 700, fontSize: ".9rem", color: "var(--azul)", display: "block", marginTop: 16 }}>Contraseña
          <input style={input} type="password" value={pw} onChange={(e) => setPw(e.target.value)} required />
        </label>
        {err && <p style={{ color: "#b00", fontSize: ".85rem", marginTop: 10 }}>{err}</p>}
        <button type="submit" disabled={loading} className="btn btn-oro" style={{ width: "100%", padding: 14, marginTop: 20 }}>
          {loading ? "Entrando…" : "Entrar"}
        </button>
      </form>
    </main>
  );
}
