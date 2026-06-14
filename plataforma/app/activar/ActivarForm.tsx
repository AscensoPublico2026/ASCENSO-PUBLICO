"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { definirPassword } from "./actions";

export default function ActivarForm({ referencia, email }: { referencia: string; email: string }) {
  const [pw, setPw] = useState("");
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");
  const router = useRouter();

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setErr("");
    const res = await definirPassword(referencia, pw);
    if (!res.ok) {
      setErr(res.error || "Ocurrió un error.");
      setLoading(false);
      return;
    }
    const supabase = createClient();
    const { error } = await supabase.auth.signInWithPassword({ email, password: pw });
    if (error) {
      setErr("Tu contraseña quedó creada. Inicia sesión en /login.");
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
    <main style={{ maxWidth: 460, margin: "0 auto", padding: "60px 22px", textAlign: "center" }}>
      <div style={{ width: 60, height: 60, borderRadius: "50%", background: "var(--verde-suave)", color: "var(--verde)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "1.8rem", margin: "0 auto 16px" }}>✓</div>
      <h1 style={{ fontSize: "1.7rem" }}>¡Pago confirmado!</h1>
      <p style={{ color: "var(--texto-suave)", margin: "10px 0 24px" }}>
        Crea una contraseña para entrar a tu perfil y ver tu curso.
      </p>
      <form onSubmit={onSubmit} style={{ textAlign: "left" }}>
        <label style={{ fontWeight: 700, fontSize: ".9rem", color: "var(--azul)" }}>Correo
          <input style={{ ...input, background: "#f4f2ec" }} type="email" value={email} readOnly />
        </label>
        <label style={{ fontWeight: 700, fontSize: ".9rem", color: "var(--azul)", display: "block", marginTop: 16 }}>Crea tu contraseña
          <input style={input} type="password" value={pw} onChange={(e) => setPw(e.target.value)} minLength={6} required placeholder="Mínimo 6 caracteres" />
        </label>
        {err && <p style={{ color: "#b00", fontSize: ".85rem", marginTop: 10 }}>{err}</p>}
        <button type="submit" disabled={loading} className="btn btn-oro" style={{ width: "100%", padding: 14, marginTop: 20 }}>
          {loading ? "Creando…" : "Entrar a mi perfil →"}
        </button>
      </form>
    </main>
  );
}
