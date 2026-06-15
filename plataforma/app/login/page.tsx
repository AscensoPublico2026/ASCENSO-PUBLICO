"use client";

import { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { createClient } from "@/lib/supabase/client";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [pw, setPw] = useState("");
  const [err, setErr] = useState("");
  const [loading, setLoading] = useState(false);
  const [modo, setModo] = useState<"login" | "recuperar">("login");
  const [enviado, setEnviado] = useState(false);
  const router = useRouter();
  const searchParams = useSearchParams();
  const next = searchParams.get("next") || "/perfil";

  async function onLogin(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setErr("");
    const supabase = createClient();
    const { error } = await supabase.auth.signInWithPassword({ email, password: pw });
    if (error) {
      setErr("Correo o contraseña incorrectos. ¿Ya activaste tu cuenta?");
      setLoading(false);
      return;
    }
    router.push(next);
  }

  async function onRecuperar(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setErr("");
    const supabase = createClient();
    const { error } = await supabase.auth.resetPasswordForEmail(email, {
      redirectTo: `${window.location.origin}/reset-password`,
    });
    if (error) {
      setErr("No pudimos enviar el correo. Verifica tu dirección.");
      setLoading(false);
      return;
    }
    setEnviado(true);
    setLoading(false);
  }

  const input: React.CSSProperties = {
    width: "100%", padding: "12px 14px", borderRadius: 12, border: "1px solid var(--gris-borde)",
    fontFamily: "inherit", fontSize: ".95rem", marginTop: 6, background: "#fff",
  };

  return (
    <main style={{ maxWidth: 420, margin: "0 auto", padding: "70px 22px" }}>
      {/* Logo */}
      <div style={{ textAlign: "center", marginBottom: 28 }}>
        <Link href="/" style={{ display: "inline-flex", alignItems: "center", gap: 10 }}>
          <span style={{
            width: 42, height: 42, borderRadius: 11,
            background: "linear-gradient(135deg, #F6C56B, #E8A33D)",
            display: "flex", alignItems: "center", justifyContent: "center",
            boxShadow: "0 5px 14px rgba(232,163,61,.4)",
          }}>
            <svg viewBox="0 0 100 100" width={24} height={24}>
              <circle cx="26" cy="74" r="3.4" fill="#0A2A5E" opacity={0.45}/>
              <circle cx="34" cy="70" r="4.2" fill="#0A2A5E" opacity={0.72}/>
              <path d="M36 66 C48 62 58 54 72 34" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round"/>
              <path d="M61 32 L75 30 L73 45" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </span>
          <span style={{ fontWeight: 800, fontSize: "1.15rem", color: "var(--azul)" }}>Ascenso Público</span>
        </Link>
      </div>

      {modo === "login" ? (
        <>
          <h1 style={{ fontSize: "1.8rem", textAlign: "center", marginBottom: 8 }}>Inicia sesión</h1>
          <p style={{ color: "var(--texto-suave)", textAlign: "center", marginBottom: 24 }}>Accede a tu curso personalizado.</p>

          <form onSubmit={onLogin}>
            <label style={{ fontWeight: 700, fontSize: ".9rem", color: "var(--azul)" }}>Correo
              <input style={input} type="email" value={email} onChange={(e) => setEmail(e.target.value)} required placeholder="tucorreo@ejemplo.com" />
            </label>
            <label style={{ fontWeight: 700, fontSize: ".9rem", color: "var(--azul)", display: "block", marginTop: 16 }}>Contraseña
              <input style={input} type="password" value={pw} onChange={(e) => setPw(e.target.value)} required placeholder="Tu contraseña" />
            </label>

            {err && <p style={{ color: "#b00", fontSize: ".85rem", marginTop: 10 }}>{err}</p>}

            <button type="submit" disabled={loading} className="btn btn-oro" style={{ width: "100%", padding: 14, marginTop: 20 }}>
              {loading ? "Entrando…" : "Entrar"}
            </button>
          </form>

          {/* Olvidé mi contraseña */}
          <button
            onClick={() => { setModo("recuperar"); setErr(""); }}
            style={{ display: "block", margin: "16px auto 0", background: "none", border: "none", color: "var(--azul)", fontWeight: 600, fontSize: ".88rem", cursor: "pointer", fontFamily: "inherit" }}
          >
            ¿Olvidaste tu contraseña?
          </button>

          {/* Ayuda extra */}
          <div style={{ marginTop: 28, padding: "16px 18px", background: "#FDF4E3", borderRadius: 12, fontSize: ".84rem", color: "#B8600A" }}>
            <strong>¿Acabas de comprar?</strong> Si aún no has creado tu contraseña, revisa tu correo o vuelve al enlace que te dio Wompi después del pago.
          </div>
        </>
      ) : (
        <>
          <h1 style={{ fontSize: "1.8rem", textAlign: "center", marginBottom: 8 }}>Recuperar contraseña</h1>
          <p style={{ color: "var(--texto-suave)", textAlign: "center", marginBottom: 24 }}>
            Te enviaremos un enlace a tu correo para crear una contraseña nueva.
          </p>

          {enviado ? (
            <div style={{ textAlign: "center", padding: 24, background: "var(--verde-suave)", borderRadius: 14, color: "var(--verde)" }}>
              <div style={{ fontSize: "2rem", marginBottom: 8 }}>📧</div>
              <p style={{ fontWeight: 700 }}>¡Correo enviado!</p>
              <p style={{ fontSize: ".88rem", marginTop: 8, color: "var(--texto-suave)" }}>
                Revisa tu bandeja de entrada (y spam) y sigue el enlace para crear tu nueva contraseña.
              </p>
            </div>
          ) : (
            <form onSubmit={onRecuperar}>
              <label style={{ fontWeight: 700, fontSize: ".9rem", color: "var(--azul)" }}>Correo
                <input style={input} type="email" value={email} onChange={(e) => setEmail(e.target.value)} required placeholder="tucorreo@ejemplo.com" />
              </label>
              {err && <p style={{ color: "#b00", fontSize: ".85rem", marginTop: 10 }}>{err}</p>}
              <button type="submit" disabled={loading} className="btn btn-oro" style={{ width: "100%", padding: 14, marginTop: 20 }}>
                {loading ? "Enviando…" : "Enviar enlace de recuperación"}
              </button>
            </form>
          )}

          <button
            onClick={() => { setModo("login"); setErr(""); setEnviado(false); }}
            style={{ display: "block", margin: "16px auto 0", background: "none", border: "none", color: "var(--azul)", fontWeight: 600, fontSize: ".88rem", cursor: "pointer", fontFamily: "inherit" }}
          >
            ← Volver a iniciar sesión
          </button>
        </>
      )}
    </main>
  );
}
