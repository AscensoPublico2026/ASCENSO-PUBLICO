import Link from "next/link";
import { notFound } from "next/navigation";
import { requireAdmin } from "@/lib/auth";
import { createClient, createAdminClient } from "@/lib/supabase/server";
import { toTitleCase } from "@/lib/format";
import { subirGuia, marcarCursoListo, habilitarCursoAhora, eliminarGuia, asignarGuiaDesdeBiblioteca } from "./actions";
import { guiasAsignables } from "@/lib/catalogoGuias";

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

  const input: React.CSSProperties = { width: "100%", padding: "10px 12px", borderRadius: 10, border: "1px solid var(--gris-borde)", fontFamily: "inherit", fontSize: ".88rem" };
  const box: React.CSSProperties = { background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 14, padding: 22, boxShadow: "0 4px 20px rgba(10,42,94,.06)", marginBottom: 20 };

  const guiasAuto = (guias || []).filter((g: any) => ["general", "nivel", "bonus"].includes(g.tipo));
  const guiasManuales = (guias || []).filter((g: any) => ["funcional", "simulacro"].includes(g.tipo));

  // Guías de la biblioteca (funcional + simulacro) que AÚN no están asignadas a este curso.
  const rutasAsignadas = new Set((guias || []).map((g: any) => g.archivo_path).filter(Boolean));
  const disponiblesBiblioteca = guiasAsignables().filter((g) => !rutasAsignadas.has(g.archivoPath));

  return (
    <div style={{ padding: "40px 28px", maxWidth: 880 }}>
      <Link href="/admin/cursos" style={{ color: "var(--texto-suave)", fontSize: ".88rem" }}>← Todos los cursos</Link>
      <h1 style={{ fontSize: "1.5rem", margin: "16px 0 24px" }}>
        {toTitleCase(curso.cargo_nombre || "Curso")}
        {curso.convocatorias?.nombre ? <span style={{ fontWeight: 400, fontSize: "1rem", color: "var(--texto-suave)" }}> — {curso.convocatorias.nombre}</span> : ""}
      </h1>

      {/* Datos del cliente */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 12 }}>👤 Datos del cliente</h2>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "8px 20px" }}>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)" }}>NOMBRE</span><br/><strong>{curso.profiles?.nombre || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)" }}>CORREO</span><br/><strong>{curso.profiles?.correo || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)" }}>CELULAR</span><br/><strong>{curso.profiles?.celular || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)" }}>OPEC</span><br/><strong>{curso.opec || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)" }}>NIVEL</span><br/><strong>{curso.nivel || "-"}</strong></div>
          <div><span style={{ fontSize: ".75rem", color: "var(--texto-suave)" }}>ESTADO</span><br/><strong>{curso.estado}</strong></div>
        </div>
        {manualUrl && (
          <a href={manualUrl} target="_blank" rel="noopener" style={{ display: "inline-block", marginTop: 14, color: "var(--azul)", fontWeight: 700 }}>
            📄 Ver manual de funciones
          </a>
        )}
      </div>

      {/* Habilitar acceso */}
      {curso.estado !== "listo" && (
        <div style={{ ...box, background: "#FDF4E3", border: "1px solid #F0DCB0" }}>
          <p style={{ color: "#B8600A", fontWeight: 700, marginBottom: 10 }}>⚡ Curso en preparación</p>
          <p style={{ color: "var(--texto-suave)", fontSize: ".88rem", marginBottom: 14 }}>
            Cuando termines de subir las guías funcionales, tienes dos opciones:
          </p>
          <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
            <form action={marcarCursoListo.bind(null, curso.id)}>
              <button className="btn btn-oro" style={{ padding: "10px 18px", fontSize: ".88rem" }}>
                ✅ Curso listo (se habilita a las 12h)
              </button>
            </form>
            <form action={habilitarCursoAhora.bind(null, curso.id)}>
              <button className="btn btn-azul" style={{ padding: "10px 18px", fontSize: ".88rem" }}>
                ⚡ Habilitar ahora (acceso inmediato)
              </button>
            </form>
          </div>
          <p style={{ color: "var(--texto-suave)", fontSize: ".78rem", marginTop: 10 }}>
            <strong>Curso listo:</strong> el cliente verá el curso cuando se cumplan las 12h desde su compra.<br/>
            <strong>Habilitar ahora:</strong> el cliente ve el curso de inmediato (para amigos o casos especiales).
          </p>
        </div>
      )}

      {/* Guías auto-cargadas */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 10 }}>📚 Guías auto-cargadas ({guiasAuto.length})</h2>
        {guiasAuto.length === 0 ? (
          <p style={{ color: "var(--texto-suave)", fontSize: ".85rem" }}>No hay guías auto-cargadas.</p>
        ) : (
          <div style={{ display: "grid", gap: 6 }}>
            {guiasAuto.map((g: any) => (
              <div key={g.id} style={{ display: "flex", alignItems: "center", gap: 10, padding: "8px 12px", background: "var(--crema)", borderRadius: 8 }}>
                {g.dia != null && <span style={{ fontWeight: 800, color: "var(--azul)", fontSize: ".78rem" }}>D{g.dia}</span>}
                <span style={{ flex: 1, fontSize: ".88rem" }}>{g.titulo}</span>
                <span style={{ fontSize: ".72rem", color: "var(--texto-suave)" }}>{g.tipo}</span>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Guías funcionales/simulacro */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 10 }}>📝 Guías funcionales y simulacro ({guiasManuales.length})</h2>
        {guiasManuales.length > 0 && (
          <div style={{ display: "grid", gap: 6, marginBottom: 16 }}>
            {guiasManuales.map((g: any) => (
              <div key={g.id} style={{ display: "flex", alignItems: "center", gap: 10, padding: "8px 12px", border: "1px solid var(--gris-borde)", borderRadius: 8 }}>
                {g.dia != null && <span style={{ fontWeight: 800, color: "var(--azul)", fontSize: ".78rem" }}>D{g.dia}</span>}
                <span style={{ flex: 1, fontSize: ".88rem" }}>{g.titulo}</span>
                <form action={eliminarGuia.bind(null, curso.id, g.id)}>
                  <button style={{ background: "none", border: "none", color: "#b00", cursor: "pointer", fontSize: ".78rem" }}>Eliminar</button>
                </form>
              </div>
            ))}
          </div>
        )}

        <h3 style={{ fontSize: ".9rem", margin: "14px 0 10px" }}>➕ Asignar guía de la biblioteca</h3>
        <p style={{ color: "var(--texto-suave)", fontSize: ".8rem", marginBottom: 10 }}>
          Elige una guía ya creada (según el plan de estudio) y queda cargada al instante. No necesitas subir el HTML: ya vive en el sistema.
        </p>
        {disponiblesBiblioteca.length === 0 ? (
          <p style={{ color: "var(--texto-suave)", fontSize: ".82rem", padding: "8px 0" }}>
            No quedan guías de la biblioteca por asignar (ya están todas las funcionales/simulacro disponibles).
          </p>
        ) : (
          <form action={asignarGuiaDesdeBiblioteca.bind(null, curso.id)} style={{ display: "grid", gap: 10, gridTemplateColumns: "2fr 1fr 1fr", alignItems: "end" }}>
            <div style={{ gridColumn: "1/-1" }}>
              <label style={{ fontSize: ".72rem", color: "var(--texto-suave)" }}>GUÍA (código — título)</label>
              <select style={input} name="codigo" defaultValue="" required>
                <option value="" disabled>Selecciona del plan de estudio…</option>
                {disponiblesBiblioteca.map((g) => (
                  <option key={g.codigo} value={g.codigo}>
                    {g.codigo} — {g.titulo}{g.tipo === "simulacro" ? " (Simulacro)" : ""}
                  </option>
                ))}
              </select>
            </div>
            <div>
              <label style={{ fontSize: ".72rem", color: "var(--texto-suave)" }}>DÍA (opcional)</label>
              <input style={input} type="number" name="dia" placeholder="ej. 9" min={1} />
            </div>
            <div>
              <label style={{ fontSize: ".72rem", color: "var(--texto-suave)" }}>ORDEN (opcional)</label>
              <input style={input} type="number" name="orden" placeholder="ej. 9" min={0} />
            </div>
            <button className="btn btn-azul" style={{ padding: 12 }}>Asignar al curso</button>
          </form>
        )}

        <h3 style={{ fontSize: ".9rem", margin: "22px 0 10px", paddingTop: 16, borderTop: "1px solid var(--gris-borde)" }}>⬆️ Subir guía personalizada (HTML)</h3>
        <p style={{ color: "var(--texto-suave)", fontSize: ".8rem", marginBottom: 10 }}>
          Solo para guías que NO están en la biblioteca (ej. “Conoce tu Entidad”, personalizada por cliente).
        </p>
        <form action={subirGuia.bind(null, curso.id)} style={{ display: "grid", gap: 10, gridTemplateColumns: "1fr 1fr" }}>
          <input style={input} type="text" name="titulo" placeholder="Título *" required />
          <input style={input} type="number" name="dia" placeholder="Día (ej. 9)" />
          <select style={input} name="tipo" defaultValue="funcional">
            <option value="funcional">Funcional</option>
            <option value="simulacro">Simulacro</option>
          </select>
          <input style={input} type="number" name="orden" placeholder="Orden" />
          <input style={{ ...input, gridColumn: "1/-1" }} type="file" name="archivo" accept=".html,text/html" required />
          <button className="btn btn-oro" style={{ gridColumn: "1/-1", padding: 12 }}>Subir guía</button>
        </form>
      </div>
    </div>
  );
}
