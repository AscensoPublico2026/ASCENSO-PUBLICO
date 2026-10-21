"use client";

import { useEffect, useRef, useState } from "react";
import { useFormState, useFormStatus } from "react-dom";
import { crearClienteManual, consultarPlanPorOpec, type CrearClienteResult, type PlanOpecInfo } from "./actions";

type Convocatoria = { id: string; nombre: string; entidad: string | null };

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button
      type="submit"
      disabled={pending}
      style={{
        width: "100%",
        marginTop: 20,
        padding: "16px",
        background: pending ? "#ccc" : "var(--azul, #0A2A5E)",
        color: "#fff",
        border: "none",
        borderRadius: 12,
        fontWeight: 800,
        fontSize: "1rem",
        fontFamily: "inherit",
        cursor: pending ? "not-allowed" : "pointer",
        transition: "background .2s, transform .1s",
      }}
    >
      {pending ? "Creando..." : "✓ Crear perfil y curso"}
    </button>
  );
}

export default function FormCrearCliente({ convocatorias }: { convocatorias: Convocatoria[] }) {
  const [state, formAction] = useFormState<CrearClienteResult | null, FormData>(
    crearClienteManual,
    null
  );

  // Aviso en vivo: ¿ya tenemos un curso armado para este OPEC?
  const [planOpec, setPlanOpec] = useState<PlanOpecInfo | null>(null);
  const [consultando, setConsultando] = useState(false);
  const timerOpec = useRef<ReturnType<typeof setTimeout> | null>(null);
  const opecRef = useRef("");
  const convRef = useRef("");
  // Modalidad del curso: "21" (regular) o "15" (intensivo).
  const [modalidad, setModalidad] = useState<"21" | "15">("21");
  const modRef = useRef<"21" | "15">("21");
  const alCambiarOpec = (valor: string, conv: string = convRef.current, mod: "21" | "15" = modRef.current) => {
    opecRef.current = valor;
    convRef.current = conv;
    modRef.current = mod;
    if (timerOpec.current) clearTimeout(timerOpec.current);
    const v = valor.trim();
    if (v.length < 2) { setPlanOpec(null); setConsultando(false); return; }
    setConsultando(true);
    timerOpec.current = setTimeout(async () => {
      try { setPlanOpec(await consultarPlanPorOpec(v, conv || null, mod)); }
      catch { setPlanOpec(null); }
      finally { setConsultando(false); }
    }, 500);
  };
  useEffect(() => () => { if (timerOpec.current) clearTimeout(timerOpec.current); }, []);

  const box: React.CSSProperties = {
    background: "#fff",
    border: "1px solid var(--gris-borde)",
    borderRadius: 14,
    padding: "28px 24px",
    boxShadow: "0 4px 20px rgba(10,42,94,.06)",
  };

  const inputStyle: React.CSSProperties = {
    width: "100%",
    padding: "12px 14px",
    borderRadius: 10,
    border: "1px solid var(--gris-borde)",
    fontFamily: "inherit",
    fontSize: ".92rem",
    background: "var(--crema, #FBF9F4)",
    transition: "border-color .2s",
  };

  const labelStyle: React.CSSProperties = {
    display: "block",
    fontWeight: 700,
    fontSize: ".85rem",
    marginBottom: 6,
    color: "var(--azul, #0A2A5E)",
  };

  const fieldGroup: React.CSSProperties = {
    marginBottom: 18,
  };

  // Si fue exitoso, mostrar confirmación
  if (state?.ok) {
    return (
      <div style={box}>
        <div style={{ textAlign: "center", padding: "20px 0" }}>
          <div style={{ fontSize: "3rem", marginBottom: 12 }}>✅</div>
          <h2 style={{ fontSize: "1.3rem", color: "var(--azul)", marginBottom: 8 }}>
            Cliente creado exitosamente
          </h2>
          <p style={{ color: "var(--texto-suave)", fontSize: ".9rem", marginBottom: 20 }}>
            El usuario ya puede iniciar sesión con su correo y la contraseña genérica.
          </p>
          <div style={{
            background: "var(--crema, #FBF9F4)",
            border: "1px solid var(--gris-borde)",
            borderRadius: 10,
            padding: "14px 18px",
            textAlign: "left",
            fontSize: ".85rem",
            marginBottom: 20,
          }}>
            <div style={{ marginBottom: 6 }}><strong>Correo:</strong> {state.correo}</div>
            <div style={{ marginBottom: 6 }}>
              <strong>Contraseña:</strong>{" "}
              <code style={{ background: "#DBEAFE", color: "#1E40AF", padding: "2px 8px", borderRadius: 5, fontFamily: "monospace", fontWeight: 700 }}>
                nuevoestudiante2026
              </code>
            </div>
            <div style={{ marginBottom: 6 }}><strong>ID Curso:</strong> {state.cursoId}</div>
            <div style={{ marginBottom: 4 }}>
              <strong>Modalidad:</strong> {state.modalidad === "15" ? "⚡ Intensivo de 15 días (arma el plan con «Armar plan completo» en el curso)" : "📅 Curso de 21 días"}
            </div>
            <div style={{ marginBottom: 4 }}>
              <strong>Guías cargadas:</strong> {state.guiasCargadas ?? 0}
              {state.planCopiado ? " — plan completo copiado de un curso ya existente para este OPEC ✅" : ""}
            </div>
          </div>
          <div style={{ display: "flex", gap: 12, justifyContent: "center", flexWrap: "wrap" }}>
            <a
              href="/admin/crear-cliente"
              style={{
                background: "var(--azul, #0A2A5E)",
                color: "#fff",
                padding: "12px 24px",
                borderRadius: 10,
                fontWeight: 700,
                fontSize: ".9rem",
                textDecoration: "none",
              }}
            >
              + Crear otro cliente
            </a>
            <a
              href={`/admin/cursos/${state.cursoId}`}
              style={{
                background: "transparent",
                color: "var(--azul, #0A2A5E)",
                padding: "12px 24px",
                borderRadius: 10,
                fontWeight: 700,
                fontSize: ".9rem",
                border: "1px solid var(--azul, #0A2A5E)",
                textDecoration: "none",
              }}
            >
              Gestionar curso →
            </a>
          </div>
        </div>
      </div>
    );
  }

  return (
    <form action={formAction}>
      <div style={box}>
        {/* Error message */}
        {state?.error && (
          <div style={{
            background: "#FEF2F2",
            border: "1px solid #FECACA",
            borderRadius: 10,
            padding: "12px 16px",
            marginBottom: 20,
            color: "#991B1B",
            fontSize: ".88rem",
            fontWeight: 600,
          }}>
            ⚠️ {state.error}
          </div>
        )}

        {/* Sección: Datos del cliente */}
        <h2 style={{ fontSize: "1.05rem", color: "var(--azul)", marginBottom: 16, paddingBottom: 10, borderBottom: "1px solid var(--gris-borde)" }}>
          👤 Datos del cliente
        </h2>

        <div style={fieldGroup}>
          <label htmlFor="nombre" style={labelStyle}>Nombre completo *</label>
          <input
            id="nombre"
            name="nombre"
            type="text"
            required
            placeholder="Ej: María López Gómez"
            style={inputStyle}
          />
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14, marginBottom: 18 }}>
          <div>
            <label htmlFor="correo" style={labelStyle}>Correo electrónico *</label>
            <input
              id="correo"
              name="correo"
              type="email"
              required
              placeholder="cliente@correo.com"
              style={inputStyle}
            />
          </div>
          <div>
            <label htmlFor="celular" style={labelStyle}>Celular</label>
            <input
              id="celular"
              name="celular"
              type="tel"
              placeholder="300 123 4567"
              style={inputStyle}
            />
          </div>
        </div>

        {/* Aviso contraseña genérica */}
        <div style={{
          background: "#EFF6FF",
          border: "1px solid #BFDBFE",
          borderRadius: 10,
          padding: "12px 16px",
          marginBottom: 18,
          display: "flex",
          alignItems: "flex-start",
          gap: 10,
        }}>
          <span style={{ fontSize: "1.1rem", flexShrink: 0 }}>🔑</span>
          <div style={{ fontSize: ".84rem", color: "#1E40AF" }}>
            <strong>Contraseña de acceso:</strong>{" "}
            <code style={{ background: "#DBEAFE", padding: "2px 7px", borderRadius: 5, fontFamily: "monospace", fontWeight: 700, fontSize: ".9rem" }}>
              nuevoestudiante2026
            </code>
            <br />
            <span style={{ color: "#3B82F6", marginTop: 2, display: "block" }}>
              Comparte este correo y contraseña con tu cliente por WhatsApp. El puede cambiarla desde su perfil cuando quiera.
            </span>
          </div>
        </div>

        <div style={fieldGroup}>
          <label htmlFor="password" style={labelStyle}>Contraseña de acceso *</label>
          <input
            id="password"
            name="password"
            type="text"
            required
            minLength={6}
            placeholder="Mínimo 6 caracteres"
            style={inputStyle}
          />
          <span style={{ fontSize: ".78rem", color: "var(--texto-suave)", marginTop: 4, display: "block" }}>
            El cliente usará esta contraseña para ingresar. Puedes compartírsela por WhatsApp.
          </span>
        </div>

        {/* Sección: Datos del curso */}
        <h2 style={{ fontSize: "1.05rem", color: "var(--azul)", marginTop: 28, marginBottom: 16, paddingBottom: 10, borderBottom: "1px solid var(--gris-borde)" }}>
          🎓 Datos del curso
        </h2>

        <div style={fieldGroup}>
          <label style={labelStyle}>Modalidad del curso *</label>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
            {([
              ["21", "📅 Curso de 21 días", "Plan completo y detallado: 20 guías + simulacro final."],
              ["15", "⚡ Curso intensivo de 15 días", "14 guías condensadas + simulacro general. Para quien tiene poco tiempo antes de la prueba."],
            ] as const).map(([val, tit, desc]) => (
              <label
                key={val}
                style={{
                  display: "block", cursor: "pointer", padding: "12px 14px", borderRadius: 12,
                  border: modalidad === val ? "2px solid var(--azul, #0A2A5E)" : "1px solid var(--gris-borde, #D9DEE7)",
                  background: modalidad === val ? "#EAF0FB" : "#fff",
                }}
              >
                <input
                  type="radio" name="modalidad" value={val} checked={modalidad === val}
                  onChange={() => { setModalidad(val); alCambiarOpec(opecRef.current, convRef.current, val); }}
                  style={{ marginRight: 8 }}
                />
                <strong>{tit}</strong>
                <div style={{ fontSize: ".8rem", color: "var(--texto-suave, #5B6675)", marginTop: 4 }}>{desc}</div>
              </label>
            ))}
          </div>
        </div>

        <div style={fieldGroup}>
          <label htmlFor="convocatoria_id" style={labelStyle}>Convocatoria</label>
          <select
            id="convocatoria_id"
            name="convocatoria_id"
            style={{ ...inputStyle, cursor: "pointer" }}
            onChange={(e) => alCambiarOpec(opecRef.current, e.target.value)}
          >
            <option value="">— Seleccionar convocatoria —</option>
            {convocatorias.map((c) => (
              <option key={c.id} value={c.id}>
                {c.nombre} {c.entidad ? `(${c.entidad})` : ""}
              </option>
            ))}
          </select>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14, marginBottom: 18 }}>
          <div>
            <label htmlFor="opec" style={labelStyle}>Número OPEC</label>
            <input
              id="opec"
              name="opec"
              type="text"
              placeholder="Ej: 123456"
              style={inputStyle}
              onChange={(e) => alCambiarOpec(e.target.value, convRef.current)}
              autoComplete="off"
            />
          </div>
          <div>
            <label htmlFor="nivel" style={labelStyle}>Nivel *</label>
            <select
              id="nivel"
              name="nivel"
              required
              style={{ ...inputStyle, cursor: "pointer" }}
            >
              <option value="">— Seleccionar —</option>
              <option value="asistencial">Asistencial</option>
              <option value="tecnico">Técnico</option>
              <option value="profesional">Profesional</option>
            </select>
          </div>
        </div>

        {consultando && (
          <div style={{ marginBottom: 18, fontSize: ".85rem", color: "var(--texto-suave, #5B6675)" }}>Buscando si ya tenemos un curso para este OPEC…</div>
        )}
        {!consultando && planOpec?.existe && (
          <div style={{ marginBottom: 18, padding: "14px 16px", borderRadius: 12, background: "#E8F6EE", border: "1px solid #BFE6CF", color: "#1A7A4A", fontSize: ".9rem", lineHeight: 1.5 }}>
            <strong>✅ Ya contamos con este curso.</strong>
            {planOpec.cargo ? <> {planOpec.cargo}{planOpec.convocatoria ? ` · ${planOpec.convocatoria}` : ""}.</> : null}
            {" "}Tiene {planOpec.totalGuias} guías ({planOpec.funcionales} funcionales{planOpec.tieneSimulacro ? " + simulacro" : ""}).
            Al crear el perfil se cargará <strong>completo automáticamente</strong>.
          </div>
        )}

        <div style={fieldGroup}>
          <label htmlFor="cargo_nombre" style={labelStyle}>Nombre del cargo</label>
          <input
            id="cargo_nombre"
            name="cargo_nombre"
            type="text"
            placeholder="Ej: Técnico Operativo — Almacén"
            style={inputStyle}
          />
        </div>
      </div>

      {/* Botón de envío */}
      <SubmitButton />

      <p style={{ textAlign: "center", fontSize: ".8rem", color: "var(--texto-suave)", marginTop: 12 }}>
        Se creará el usuario, perfil, curso y se auto-cargarán las guías del nivel seleccionado.
        El pago se registrará como aprobado (manual).
      </p>
    </form>
  );
}
