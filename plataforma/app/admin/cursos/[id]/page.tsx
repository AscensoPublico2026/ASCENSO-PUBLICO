import Link from "next/link";
import { notFound } from "next/navigation";
import { requireAdmin } from "@/lib/auth";
import { createClient, createAdminClient } from "@/lib/supabase/server";
import { toTitleCase } from "@/lib/format";
import { subirGuia, habilitarCurso, eliminarGuia } from "./actions";

export const dynamic = "force-dynamic";

export default async function AdminCursoDetalle({ params }: { params: { id: string } }) {
  await requireAdmin();
  const supabase = createClient();
  const { data: curso } = await supabase
    .from("cursos")
    .select("*, profiles(nombre,correo,celular), convocatorias(nombre)")
    .eq("id", params.id)
    .single();
  if (!curso) notFound();

  const admin = createAdminClient();
  let manualUrl: string | null = null;
  if (curso.manual_pdf_path) {
    const { data } = await admin.storage.from("manuales").createSignedUrl(curso.manual_pdf_path, 1800);
    manualUrl = data?.signedUrl ?? null;
  }

  const { data: guias } = await supabase.from("guias_curso").select("*").eq("curso_id", params.id).order("orden");

  const estadoColor: Record<string, { label: string; bg: string; color: string }> = {
    en_preparacion: { label: "En preparación", bg: "#FDF4E3", color: "#B8600A" },
    listo: { label: "Listo", bg: "var(--verde-suave)", color: "var(--verde)" },
    vencido: { label: "Vencido", bg: "#f5f5f5", color: "#888" },
  };
  const badge = estadoColor[curso.estado] || estadoColor.en_preparacion;

  const input: React.CSSProperties = { width: "100%", padding: "10px 12px", borderRadius: 10, border: "1px solid var(--gris-borde)", fontFamily: "inherit", fontSize: ".88rem" };
  const box: React.CSSProperties = { background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 14, padding: 22, boxShadow: "0 4px 20px rgba(10,42,94,.06)", marginBottom: 20 };

  // Separar guías auto-cargadas vs manuales
  const guiasAuto = (guias || []).filter((g: any) => ["general", "nivel", "bonus"].includes(g.tipo));
  const guiasManuales = (guias || []).filter((g: any) => ["funcional", "simulacro"].includes(g.tipo));

  return (
    <div style={{ padding: "40px 28px", maxWidth: 880 }}>
      <Link href="/admin/cursos" style={{ color: "var(--texto-suave)", fontSize: ".88rem" }}>← Todos los cursos</Link>

      {/* Header del curso */}
      <div style={{ display: "flex", alignItems: "center", gap: 14, margin: "16px 0 24px" }}>
        <h1 style={{ fontSize: "1.5rem", margin: 0 }}>
          {toTitleCase(curso.cargo_nombre || "Curso")}
          {curso.convocatorias?.nombre ? <span style={{ fontWeight: 400, fontSize: "1rem", color: "var(--texto-suave)" }}> — {curso.convocatorias.nombre}</span> : ""}
        </h1>
        <span style={{ fontSize: ".72rem", fontWeight: 800, padding: "4px 10px", borderRadius: 12, background: badge.bg, color: badge.color }}>
          {badge.label}
        </span>
      </div>

      {/* Datos del cliente */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 12 }}>👤 Datos del cliente</h2>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "8px 20px" }}>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)", textTransform: "uppercase" }}>Nombre</span><br/><strong>{curso.profiles?.nombre || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)", textTransform: "uppercase" }}>Correo</span><br/><strong>{curso.profiles?.correo || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)", textTransform: "uppercase" }}>Celular</span><br/><strong>{curso.profiles?.celular || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)", textTransform: "uppercase" }}>OPEC</span><br/><strong>{curso.opec || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)", textTransform: "uppercase" }}>Nivel</span><br/><strong>{curso.nivel || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)", textTransform: "uppercase" }}>Fecha compra</span><br/><strong>{curso.fecha_compra ? new Date(curso.fecha_compra).toLocaleDateString("es-CO") : "-"}</strong></div>
        </div>
        {manualUrl && (
          <a href={manualUrl} target="_blank" rel="noopener" style={{ display: "inline-flex", alignItems: "center", gap: 8, marginTop: 14, color: "var(--azul)", fontWeight: 700, fontSize: ".9rem" }}>
            📄 Ver manual de funciones (PDF)
          </a>
        )}
      </div>

      {/* Acciones rápidas */}
      {curso.estado !== "listo" && (
        <div style={{ ...box, background: "#FDF4E3", border: "1px solid #F0DCB0" }}>
          <h2 style={{ fontSize: "1rem", marginBottom: 8, color: "#B8600A" }}>⚡ Acción pendiente</h2>
          <p style={{ color: "var(--texto-suave)", fontSize: ".88rem", marginBottom: 14 }}>
            Cuando hayas revisado y subido las guías funcionales, habilita el acceso del estudiante:
          </p>
          <form action={habilitarCurso.bind(null, curso.id)}>
            <button className="btn btn-oro" style={{ padding: "10px 20px" }}>✅ Habilitar acceso (marcar curso como listo)</button>
          </form>
        </div>
      )}

      {/* Guías auto-cargadas */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 12 }}>📚 Guías auto-cargadas ({guiasAuto.length})</h2>
        <p style={{ color: "var(--texto-suave)", fontSize: ".82rem", marginBottom: 12 }}>
          Estas guías se asignaron automáticamente al confirmar el pago (Intro + Generales + Nivel + Bonus).
        </p>
        {guiasAuto.length === 0 ? (
          <p style={{ color: "var(--texto-suave)", fontSize: ".85rem" }}>No hay guías auto-cargadas.</p>
        ) : (
          <div style={{ display: "grid", gap: 6 }}>
            {guiasAuto.map((g: any) => (
              <div key={g.id} style={{ display: "flex", alignItems: "center", gap: 10, padding: "8px 12px", background: "var(--crema)", borderRadius: 8 }}>
                {g.dia != null && <span style={{ fontSize: ".78rem", fontWeight: 800, color: "var(--azul)" }}>D{g.dia}</span>}
                <span style={{ fontSize: ".88rem", flex: 1 }}>{g.titulo}</span>
                <span style={{ fontSize: ".72rem", color: "var(--texto-suave)" }}>{g.tipo}</span>
                {g.archivo_path ? (
                  <span style={{ fontSize: ".72rem", color: "var(--verde)" }}>✓ con archivo</span>
                ) : (
                  <span style={{ fontSize: ".72rem", color: "#B8600A" }}>⚠ sin archivo</span>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Guías manuales (funcionales + simulacro) */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 12 }}>📝 Guías funcionales y simulacro ({guiasManuales.length})</h2>
        <p style={{ color: "var(--texto-suave)", fontSize: ".82rem", marginBottom: 12 }}>
          Estas guías las subes tú manualmente (personalizadas por el cargo del cliente).
        </p>
        {guiasManuales.length > 0 && (
          <div style={{ display: "grid", gap: 6, marginBottom: 16 }}>
            {guiasManuales.map((g: any) => (
              <div key={g.id} style={{ display: "flex", alignItems: "center", gap: 10, padding: "8px 12px", background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 8 }}>
                {g.dia != null && <span style={{ fontSize: ".78rem", fontWeight: 800, color: "var(--azul)" }}>D{g.dia}</span>}
                <span style={{ fontSize: ".88rem", flex: 1 }}>{g.titulo}</span>
                <span style={{ fontSize: ".72rem", color: "var(--texto-suave)" }}>{g.tipo}</span>
                <form action={eliminarGuia.bind(null, curso.id, g.id)}>
                  <button style={{ background: "none", border: "none", color: "#b00", cursor: "pointer", fontSize: ".78rem" }}>Eliminar</button>
                </form>
              </div>
            ))}
          </div>
        )}

        {/* Formulario de subida */}
        <h3 style={{ fontSize: ".92rem", margin: "14px 0 10px", color: "var(--azul)" }}>Subir nueva guía</h3>
        <form action={subirGuia.bind(null, curso.id)} style={{ display: "grid", gap: 10, gridTemplateColumns: "1fr 1fr" }}>
          <input style={input} type="text" name="titulo" placeholder="Título de la guía *" required />
          <input style={input} type="number" name="dia" placeholder="Día (ej. 9)" />
          <select style={input} name="tipo" defaultValue="funcional">
            <option value="funcional">Funcional</option>
            <option value="simulacro">Simulacro</option>
          </select>
          <input style={input} type="number" name="orden" placeholder="Orden (ej. 9)" />
          <input style={{ ...input, gridColumn: "1/-1" }} type="file" name="archivo" accept=".html,text/html" required />
          <button className="btn btn-oro" style={{ gridColumn: "1/-1", padding: 12 }}>Subir guía</button>
        </form>
      </div>
    </div>
  );
}
