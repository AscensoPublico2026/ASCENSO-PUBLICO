"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { createClient } from "@/lib/supabase/client";

export default function ResetPasswordPage() {
  const [pw, setPw] = useState("");
  const [pwConfirm, setPwConfirm] = useState("");
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");
  const [done, setDone] = useState(false);
  const [sessionReady, setSessionReady] = useState(false);
  const router = useRouter();

  useEffect(() => {
    // Supabase inyecta los tokens en el hash de la URL al redirigir desde el correo.
    // El cliente de Supabase los detecta automáticamente y establece la sesión.
    const supabase = createClient();
    supabase.auth.onAuthStateChange((event) => {
      if (event === "PASSWORD_RECOVERY") {
        setSessionReady(true);
      }
    });
    // También verificar si ya hay sesión (por si el evento ya pasó)
    supabase.auth.getUser().then(({ data }) => {
      if (data.user) setSessionReady(true);
    });
  }, []);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setErr("");

    if (pw.length < 6) {
      setErr("La contraseña debe tener al menos 6 caracteres.");
      return;
    }
    if (pw !== pwConfirm) {
      setErr("Las contraseñas no coinciden.");
      return;
    }

    setLoading(true);
    const supabase = createClient();
    const { error } = await supabase.auth.updateUser({ password: pw });

    if (error) {
      setErr("No se pudo actualizar la contraseña: " + error.message);
      setLoading(false);
      return;
    }

    setDone(true);
    setTimeout(() => router.push("/perfil"), 2000);
  }

  const input: React.CSSProperties = {
    width: "100%", padding: "12px 14px", borderRadius: 12, border: "1px solid var(--gris-borde)",
    fontFamily: "inherit", fontSize: ".95rem", marginTop: 6, background: "#fff",
  };

  if (!sessionReady) {
    return (
      <main style={{ maxWidth: 420, margin: "0 auto", padding: "70px 22px", textAlign: "center" }}>
        <h1 style={{ fontSize: "1.6rem", marginBottom: 12 }}>Verificando enlace…</h1>
        <p style={{ color: "var(--texto-suave)" }}>
          Si el enlace es válido, podrás crear tu nueva contraseña en un momento.
        </p>
        <p style={{ color: "var(--texto-suave)", marginTop: 16, fontSize: ".85rem" }}>
          ¿No funciona? <Link href="/login" style={{ color: "var(--azul)", fontWeight: 700 }}>Volver a login</Link> y solicita otro enlace.
        </p>
      </main>
    );
  }

  if (done) {
    return (
      <main style={{ maxWidth: 420, margin: "0 auto", padding: "70px 22px", textAlign: "center" }}>
        <div style={{ width: 60, height: 60, borderRadius: "50%", background: "var(--verde-suave)", color: "var(--verde)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "1.8rem", margin: "0 auto 16px" }}>✓</div>
        <h1 style={{ fontSize: "1.6rem" }}>¡Contraseña actualizada!</h1>
        <p style={{ color: "var(--texto-suave)", marginTop: 10 }}>Redirigiendo a tu perfil…</p>
      </main>
    );
  }

  return (
    <main style={{ maxWidth: 420, margin: "0 auto", padding: "70px 22px" }}>
      <h1 style={{ fontSize: "1.8rem", textAlign: "center", marginBottom: 8 }}>Nueva contraseña</h1>
      <p style={{ color: "var(--texto-suave)", textAlign: "center", marginBottom: 24 }}>
        Crea una nueva contraseña para tu cuenta.
      </p>

      <form onSubmit={onSubmit}>
        <label style={{ fontWeight: 700, fontSize: ".9rem", color: "var(--azul)" }}>Nueva contraseña
          <input style={input} type="password" value={pw} onChange={(e) => setPw(e.target.value)} required minLength={6} placeholder="Mínimo 6 caracteres" />
        </label>
        <label style={{ fontWeight: 700, fontSize: ".9rem", color: "var(--azul)", display: "block", marginTop: 16 }}>Confirmar contraseña
          <input style={input} type="password" value={pwConfirm} onChange={(e) => setPwConfirm(e.target.value)} required minLength={6} placeholder="Repite tu contraseña" />
        </label>

        {err && <p style={{ color: "#b00", fontSize: ".85rem", marginTop: 10 }}>{err}</p>}

        <button type="submit" disabled={loading} className="btn btn-oro" style={{ width: "100%", padding: 14, marginTop: 20 }}>
          {loading ? "Guardando…" : "Guardar nueva contraseña"}
        </button>
      </form>
    </main>
  );
}
