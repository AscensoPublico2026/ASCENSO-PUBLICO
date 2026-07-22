"use client";

import { crearCompra } from "./actions";
import { useState, useEffect } from "react";
import Link from "next/link";
import ContadorCupos from "../components/ContadorCupos";
import { trackEvent } from "@/lib/analytics";
import { createClient } from "@/lib/supabase/client";

// Componente principal (ahora completamente cliente)
export default function ComprarPage({ searchParams }: { searchParams?: { conv?: string; error?: string } }) {
  const [convocatorias, setConvocatorias] = useState<{ id: string; nombre: string }[]>([]);
  const [usuarioLogueado, setUsuarioLogueado] = useState<{ correo: string; celular: string } | null>(null);
  const [loading, setLoading] = useState(true);

  const [mostrarPassword, setMostrarPassword] = useState(false);
  const [mostrarConfirm, setMostrarConfirm] = useState(false);
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errorPassword, setErrorPassword] = useState("");

  // Cargar datos al montar
  useEffect(() => {
    async function loadData() {
      try {
        const supabase = createClient();
        
        // Cargar convocatorias
        const { data: convData } = await supabase
          .from("convocatorias")
          .select("id,nombre")
          .eq("activa", true)
          .order("orden");
        setConvocatorias(convData || []);

        // Verificar si hay usuario logueado
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const { data: profile } = await supabase
            .from("profiles")
            .select("correo, celular")
            .eq("id", user.id)
            .single();
          setUsuarioLogueado({
            correo: profile?.correo || user.email || "",
            celular: profile?.celular || "",
          });
        }
      } catch (error) {
        console.error("Error cargando datos:", error);
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, []);

  // Validar que las contraseñas coincidan
  useEffect(() => {
    if (confirmPassword && password !== confirmPassword) {
      setErrorPassword("Las contraseñas no coinciden");
    } else {
      setErrorPassword("");
    }
  }, [password, confirmPassword]);

  const inputStyle: React.CSSProperties = {
    width: "100%", padding: "12px 14px", borderRadius: 12, border: "1px solid var(--gris-borde)",
    fontFamily: "inherit", fontSize: ".95rem", marginTop: 6, background: "#fff",
  };
  const label: React.CSSProperties = { fontWeight: 700, fontSize: ".9rem", color: "var(--azul)", display: "block", marginTop: 16 };

  const passwordContainerStyle: React.CSSProperties = {
    position: "relative",
    display: "flex",
    alignItems: "center",
  };

  const toggleButtonStyle: React.CSSProperties = {
    position: "absolute",
    right: "12px",
    background: "none",
    border: "none",
    cursor: "pointer",
    fontSize: ".85rem",
    color: "var(--azul)",
    padding: "4px 8px",
    userSelect: "none",
  };

  if (loading) {
    return (
      <main style={{ maxWidth: 620, margin: "0 auto", padding: "48px 22px", textAlign: "center" }}>
        <p style={{ color: "var(--texto-suave)" }}>Cargando...</p>
      </main>
    );
  }

  return (
    <main style={{ maxWidth: 620, margin: "0 auto", padding: "48px 22px" }}>
      <Link href="/" style={{ color: "var(--texto-suave)", fontSize: ".88rem" }}>← Volver al inicio</Link>

      <h1 style={{ fontSize: "1.9rem", marginBottom: 6, marginTop: 16 }}>Adquiere tu curso personalizado</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 8 }}>
        Completa tus datos y sube tu manual de funciones. Después realizas el pago seguro con Wompi.
      </p>
      <p style={{ color: "var(--azul)", fontWeight: 800, marginBottom: 24 }}>Precio: $300.000 COP · pago único</p>

      <ContadorCupos />

      {searchParams?.error && (
        <div style={{ background: "#fdecec", border: "1px solid #f5b5b5", borderRadius: 12, padding: "12px 16px", marginBottom: 12, fontSize: ".88rem", color: "#b00020" }}>
          <strong>No se pudo procesar la compra.</strong> {searchParams.error}
        </div>
      )}

      {usuarioLogueado && (
        <div style={{ background: "var(--verde-suave)", border: "1px solid #c3e6d3", borderRadius: 12, padding: "12px 16px", marginBottom: 8, fontSize: ".85rem", color: "var(--verde)" }}>
          ✓ Estás comprando con tu cuenta (<strong>{usuarioLogueado.correo}</strong>). Tu nuevo curso se sumará a tu perfil. Usa el mismo correo para que quede vinculado.
        </div>
      )}

      <form
        action={crearCompra}
        onSubmit={(event) => {
          const data = new FormData(event.currentTarget);
          trackEvent("checkout_form_submitted", {
            level: String(data.get("nivel") || ""),
            convocatoria_id: String(data.get("convocatoria_id") || ""),
          });
        }}
      >
        {/* Nombres y Apellidos separados - OBLIGATORIOS */}
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14 }}>
          <label style={label}>Nombres *
            <input style={inputStyle} type="text" name="nombres" required placeholder="Ej: Julio César" />
          </label>
          <label style={label}>Apellidos *
            <input style={inputStyle} type="text" name="apellidos" required placeholder="Ej: Deávila Pérez" />
          </label>
        </div>

        <label style={label}>Correo *
          <input style={inputStyle} type="email" name="correo" required placeholder="tucorreo@ejemplo.com" defaultValue={usuarioLogueado?.correo || ""} />
        </label>
        <label style={label}>Celular (WhatsApp)
          <input style={inputStyle} type="tel" name="celular" placeholder="Ej: 315 197 2091" defaultValue={usuarioLogueado?.celular || ""} />
        </label>
        <label style={label}>Convocatoria *
          <select style={inputStyle} name="convocatoria_id" defaultValue={searchParams?.conv || ""} required>
            <option value="">Selecciona tu convocatoria</option>
            {convocatorias.map((c) => (<option key={c.id} value={c.id}>{c.nombre}</option>))}
          </select>
        </label>
        <label style={label}>Número de OPEC *
          <input style={inputStyle} type="text" name="opec" required placeholder="Ej: 48521" />
        </label>
        <label style={label}>Nombre del cargo *
          <input style={inputStyle} type="text" name="cargo" required placeholder="Ej: Técnico Administrativo" />
        </label>
        <label style={label}>Nivel del cargo *
          <select style={inputStyle} name="nivel" defaultValue="" required>
            <option value="" disabled>Selecciona</option>
            <option value="asistencial">Asistencial</option>
            <option value="tecnico">Técnico</option>
            <option value="profesional">Profesional</option>
          </select>
        </label>
        <label style={label}>Manual de funciones (PDF) *
          <input style={inputStyle} type="file" name="manual" accept=".pdf,application/pdf" required />
          <span style={{ fontSize: ".78rem", color: "var(--texto-suave)", marginTop: 4, display: "block" }}>
            Descárgalo de la página de la CNSC → SIMO → tu OPEC → &quot;Manual de funciones&quot;.
          </span>
        </label>

        {/* Campos de contraseña */}
        <div style={{ background: "var(--crema)", border: "1px solid #e8dcc4", borderRadius: 12, padding: "16px 18px", marginTop: 20 }}>
          <p style={{ fontSize: ".88rem", color: "var(--azul)", fontWeight: 600, marginBottom: 12 }}>
            🔐 Crea tu contraseña de acceso
          </p>
          <label style={label}>Contraseña *
            <div style={passwordContainerStyle}>
              <input 
                style={{...inputStyle, paddingRight: "70px"}} 
                type={mostrarPassword ? "text" : "password"}
                name="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                minLength={6}
                required 
                placeholder="Mínimo 6 caracteres" 
              />
              <button
                type="button"
                style={toggleButtonStyle}
                onClick={() => setMostrarPassword(!mostrarPassword)}
              >
                {mostrarPassword ? "Ocultar" : "Mostrar"}
              </button>
            </div>
          </label>
          <label style={label}>Confirma tu contraseña *
            <div style={passwordContainerStyle}>
              <input 
                style={{...inputStyle, paddingRight: "70px", borderColor: errorPassword ? "#d00" : "var(--gris-borde)"}} 
                type={mostrarConfirm ? "text" : "password"}
                name="confirmPassword"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                minLength={6}
                required 
                placeholder="Repite la contraseña" 
              />
              <button
                type="button"
                style={toggleButtonStyle}
                onClick={() => setMostrarConfirm(!mostrarConfirm)}
              >
                {mostrarConfirm ? "Ocultar" : "Mostrar"}
              </button>
            </div>
            {errorPassword && (
              <span style={{ fontSize: ".78rem", color: "#d00", marginTop: 4, display: "block" }}>
                {errorPassword}
              </span>
            )}
          </label>
          <p style={{ fontSize: ".75rem", color: "var(--texto-suave)", marginTop: 8 }}>
            Usarás esta contraseña para acceder a tu curso después del pago.
          </p>
        </div>

        <label style={{ display: "flex", gap: 10, alignItems: "flex-start", marginTop: 20, fontSize: ".88rem", color: "var(--texto-suave)" }}>
          <input type="checkbox" name="consentimiento" required style={{ marginTop: 3 }} />
          <span>Autorizo el tratamiento de mis datos personales conforme a la Ley 1581 de 2012 y la <Link href="/privacidad" style={{ color: "var(--azul)", textDecoration: "underline" }}>política de privacidad</Link>.</span>
        </label>

        <button type="submit" disabled={!!errorPassword} className="btn btn-oro" style={{ width: "100%", padding: 15, marginTop: 24, opacity: errorPassword ? 0.5 : 1, cursor: errorPassword ? "not-allowed" : "pointer" }}>
          Continuar al pago seguro →
        </button>
        <p style={{ fontSize: ".8rem", color: "var(--texto-suave)", textAlign: "center", marginTop: 12 }}>
          Pago seguro con Wompi · PSE, Nequi y tarjetas
        </p>
      </form>
    </main>
  );
}
