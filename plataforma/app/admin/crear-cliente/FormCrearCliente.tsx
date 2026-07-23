"use client";

import { useFormState, useFormStatus } from "react-dom";
import { crearClienteManual, type CrearClienteResult } from "./actions";

type Conv = { id: string; nombre: string; entidad: string | null };

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button
      type="submit"
      disabled={pending}
      style={{
        width: "100%", marginTop: 20, padding: "16px",
        background: pending ? "#ccc" : "var(--azul, #0A2A5E)",
        color: "#fff", border: "none", borderRadius: 12,
        fontWeight: 800, fontSize: "1rem", fontFamily: "inherit",
        cursor: pending ? "not-allowed" : "pointer",
      }}
    >
      {pending ? "Creando..." : "✓ Crear perfil y curso"}
    </button>
  );
}

export default function FormCrearCliente({ convocatorias }: { convocatorias: Conv[] }) {
  const [state, formAction] = useFormState<CrearClienteResult | null, FormData>(
    crearClienteManual,
    null
  );

  const box: React.CSSProperties = {
    background: "#fff", border: "1px solid var(--gris-borde)",
    borderRadius: 14, padding: "28px 24px",
    boxShadow: "0 4px 20px rgba(10,42,94,.06)",
  };
  const inp: React.CSSProperties = {
    width: "100%", padding: "12px 14px", borderRadius: 10,
    border: "1px solid var(--gris-borde)", fontFamily: "inherit",
    fontSize: ".92rem", background: "var(--crema, #FBF9F4)",
  };
  const lbl: React.CSSProperties = {
    display: "block", fontWeight: 700, fontSize: ".85rem",
    marginBottom: 6, color: "var(--azul, #0A2A5E)",
  };

  // ── Pantalla de éxito ──────────────────────────────────────────────────────
  if (state?.ok) {
    return (
      <div style={box}>
        <div style={{ textAlign: "center", padding: "20px 0" }}>
          <div style={{ fontSize: "3rem", marginBottom: 12 }}>✅</div>
          <h2 style={{ fontSize: "1.3rem", color: "var(--azul)", marginBottom: 8 }}>
            Cliente creado exitosamente
          </h2>
          <p style={{ color: "var(--texto-suave)", fontSize: ".9rem", marginBottom: 20 }}>
            El estudiante ya puede ingresar con:
          </p>
          <div style={{
            background: "#EFF6FF", border: "1px solid #BFDBFE",
            borderRadius: 12, padding: "16px 20px", textAlign: "left",
            fontSize: ".88rem", marginBottom: 24,
          }}>
            <div style={{ marginBottom: 8 }}>
              <strong>📧 Correo:</strong> {state.correo}
            </div>
            <div>
              <strong>🔑 Contraseña:</strong>{" "}
              <code style={{
                background: "#DBEAFE", color: "#1E40AF",
                padding: "2px 8px", borderRadius: 5,
                fontFamily: "monospace", fontWeight: 700,
              }}>
                nuevoestudiante2026
              </code>
            </div>
          </div>
          <div style={{ display: "flex", gap: 12, justifyContent: "center", flexWrap: "wrap" }}>
            <a href="/admin/crear-cliente" style={{
              background: "var(--azul, #0A2A5E)", color: "#fff",
              padding: "12px 24px", borderRadius: 10, fontWeight: 700,
              fontSize: ".9rem", textDecoration: "none",
            }}>
              + Crear otro cliente
            </a>
            <a href={`/admin/cursos/${state.cursoId}`} style={{
              background: "transparent", color: "var(--azul, #0A2A5E)",
              padding: "12px 24px", borderRadius: 10, fontWeight: 700,
              fontSize: ".9rem", border: "1px solid var(--azul, #0A2A5E)",
              textDecoration: "none",
            }}>
              Gestionar curso →
            </a>
          </div>
        </div>
      </div>
    );
  }

  // ── Formulario ─────────────────────────────────────────────────────────────
  return (
    <form action={formAction}>
      <div style={box}>

        {/* Error */}
        {state?.error && (
          <div style={{
            background: "#FEF2F2", border: "1px solid #FECACA",
            borderRadius: 10, padding: "12px 16px", marginBottom: 20,
            color: "#991B1B", fontSize: ".88rem", fontWeight: 600,
          }}>
            ⚠️ {state.error}
          </div>
        )}

        {/* ─── Datos del cliente ─── */}
        <h2 style={{ fontSize: "1.05rem", color: "var(--azul)", marginBottom: 16, paddingBottom: 10, borderBottom: "1px solid var(--gris-borde)" }}>
          👤 Datos del cliente
        </h2>

        <div style={{ marginBottom: 18 }}>
          <label style={lbl}>Nombre completo *</label>
          <input name="nombre" type="text" required placeholder="Ej: María López Gómez" style={inp} />
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14, marginBottom: 18 }}>
          <div>
            <label style={lbl}>Correo electrónico *</label>
            <input name="correo" type="email" required placeholder="cliente@correo.com" style={inp} />
          </div>
          <div>
            <label style={lbl}>Celular</label>
            <input name="celular" type="tel" placeholder="300 123 4567" style={inp} />
          </div>
        </div>

        {/* Aviso contraseña genérica */}
        <div style={{
          background: "#EFF6FF", border: "1px solid #BFDBFE",
          borderRadius: 10, padding: "12px 16px", marginBottom: 20,
          display: "flex", alignItems: "flex-start", gap: 10,
        }}>
          <span style={{ fontSize: "1.1rem", flexShrink: 0 }}>🔑</span>
          <div style={{ fontSize: ".84rem", color: "#1E40AF" }}>
            <strong>Contraseña de acceso asignada automáticamente:</strong>{" "}
            <code style={{
              background: "#DBEAFE", padding: "2px 7px", borderRadius: 5,
              fontFamily: "monospace", fontWeight: 700, fontSize: ".9rem",
            }}>
              nuevoestudiante2026
            </code>
            <br />
            <span style={{ color: "#3B82F6", marginTop: 3, display: "block" }}>
              Compártela con tu cliente por WhatsApp. Puede cambiarla desde su perfil.
            </span>
          </div>
        </div>

        {/* ─── Datos del curso ─── */}
        <h2 style={{ fontSize: "1.05rem", color: "var(--azul)", marginTop: 8, marginBottom: 16, paddingBottom: 10, borderBottom: "1px solid var(--gris-borde)" }}>
          🎓 Datos del curso
        </h2>

        <div style={{ marginBottom: 18 }}>
          <label style={lbl}>Convocatoria</label>
          <select name="convocatoria_id" style={{ ...inp, cursor: "pointer" }}>
            <option value="">— Seleccionar convocatoria —</option>
            {convocatorias.map((c) => (
              <option key={c.id} value={c.id}>
                {c.nombre}{c.entidad ? ` (${c.entidad})` : ""}
              </option>
            ))}
          </select>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14, marginBottom: 18 }}>
          <div>
            <label style={lbl}>Número OPEC</label>
            <input name="opec" type="text" placeholder="Ej: 123456" style={inp} />
          </div>
          <div>
            <label style={lbl}>Nivel *</label>
            <select name="nivel" required style={{ ...inp, cursor: "pointer" }}>
              <option value="">— Seleccionar —</option>
              <option value="asistencial">Asistencial</option>
              <option value="tecnico">Técnico</option>
              <option value="profesional">Profesional</option>
            </select>
          </div>
        </div>

        <div style={{ marginBottom: 4 }}>
          <label style={lbl}>Nombre del cargo</label>
          <input name="cargo_nombre" type="text" placeholder="Ej: Técnico Operativo — Almacén" style={inp} />
        </div>
      </div>

      <SubmitButton />

      <p style={{ textAlign: "center", fontSize: ".8rem", color: "var(--texto-suave)", marginTop: 12 }}>
        Se creará el usuario, perfil, curso y se auto-cargarán las guías según el nivel.
        El pago se registra como aprobado (manual).
      </p>
    </form>
  );
}
