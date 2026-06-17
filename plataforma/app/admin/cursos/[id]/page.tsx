import Link from "next/link";
import { notFound } from "next/navigation";
import { requireAdmin } from "@/lib/auth";
import { createClient, createAdminClient } from "@/lib/supabase/server";
import { toTitleCase } from "@/lib/format";
import { subirGuia, marcarCursoListo, habilitarCursoAhora, eliminarGuia, asignarGuiaDesdeBiblioteca, copiarPlanOPEC } from "./actions";
import { guiasFuncionalesAsignables, guiasSimulacroAsignables, guiasEntidadAsignables, esRutaEntidad } from "@/lib/catalogoGuias";

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

  const todas = (guias || []) as any[];
  const rutasAsignadas = new Set(todas.map((g) => g.archivo_path).filter(Boolean));

  // Día 1: Introducción (INTRO-00) y Conoce tu Entidad
  const intro = todas.find((g) => g.dia === 1 && g.tipo === "general") || todas.find((g) => /INTRO-00/.test(g.archivo_path || ""));
  const entidadAsignadas = todas.filter((g) => esRutaEntidad(g.archivo_path));

  // Generales y por nivel (auto), excluyendo la presentación del día 1
  const guiasAuto = todas
    .filter((g) => ["general", "nivel", "bonus"].includes(g.tipo) && g.id !== intro?.id && !esRutaEntidad(g.archivo_path))
    .sort((a, b) => (a.orden ?? 0) - (b.orden ?? 0));

  const guiasFuncionales = todas.filter((g) => g.tipo === "funcional").sort((a, b) => (a.orden ?? 0) - (b.orden ?? 0));
  const guiasSimulacro = todas.filter((g) => g.tipo === "simulacro");

  // Disponibles en la biblioteca (no asignadas aún a este curso)
  const dispEntidad = guiasEntidadAsignables().filter((g) => !rutasAsignadas.has(g.archivoPath));
  const dispFuncionales = guiasFuncionalesAsignables().filter((g) => !rutasAsignadas.has(g.archivoPath));
  const dispSimulacro = guiasSimulacroAsignables().filter((g) => !rutasAsignadas.has(g.archivoPath));

  // Desplegable reutilizable para asignar una guía de la biblioteca por código.
  const selector = (items: { codigo: string; titulo: string }[], placeholder: string) => (
    <form action={asignarGuiaDesdeBiblioteca.bind(null, curso.id)} style={{ display: "grid", gap: 10, gridTemplateColumns: "1fr 90px 90px auto", alignItems: "end" }}>
      <div>
        <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>GUÍA (código — título)</label>
        <select style={input} name="codigo" defaultValue="" required>
          <option value="" disabled>{placeholder}</option>
          {items.map((g) => (
            <option key={g.codigo} value={g.codigo}>{g.codigo} — {g.titulo}</option>
          ))}
        </select>
      </div>
      <div>
        <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>DÍA</label>
        <input style={input} type="number" name="dia" placeholder="–" min={1} />
      </div>
      <div>
        <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>ORDEN</label>
        <input style={input} type="number" name="orden" placeholder="–" min={0} />
      </div>
      <button className="btn btn-azul" style={{ padding: "10px 14px" }}>Cargar</button>
    </form>
  );

  const filaGuia = (g: any, conEliminar: boolean) => (
    <div key={g.id} style={{ display: "flex", alignItems: "center", gap: 10, padding: "8px 12px", background: "var(--crema)", borderRadius: 8 }}>
      {g.dia != null && <span style={{ fontWeight: 800, color: "var(--azul)", fontSize: ".78rem", minWidth: 26 }}>D{g.dia}</span>}
      <span style={{ flex: 1, fontSize: ".88rem" }}>{g.titulo}</span>
      <span style={{ fontSize: ".72rem", color: "var(--texto-suave)" }}>{g.tipo}</span>
      {conEliminar && (
        <form action={eliminarGuia.bind(null, curso.id, g.id)}>
          <button style={{ background: "none", border: "none", color: "#b00", cursor: "pointer", fontSize: ".78rem" }}>Eliminar</button>
        </form>
      )}
    </div>
  );

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

      {/* Previsualizar como estudiante (revisar antes de habilitar) */}
      <Link href={`/perfil/${curso.id}`} className="btn btn-azul" style={{ display: "flex", justifyContent: "center", padding: "13px 18px", textDecoration: "none" }}>
        👁️ Previsualizar el curso como lo verá el estudiante
      </Link>
      <p style={{ color: "var(--texto-suave)", fontSize: ".78rem", margin: "8px 0 18px", textAlign: "center" }}>
        Revisa las guías y el simulacro antes de dar "Curso listo" o "Habilitar ahora".
      </p>

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

      {/* Curso ya marcado listo: permitir habilitarlo de una vez aunque falten las 12h */}
      {curso.estado === "listo" && (() => {
        const dl = curso.preparacion_deadline ? new Date(curso.preparacion_deadline) : null;
        const pendiente = dl && dl.getTime() > Date.now();
        if (!pendiente) {
          return (
            <div style={{ ...box, background: "var(--verde-suave)", border: "1px solid #c3e6d3" }}>
              <p style={{ color: "var(--verde)", fontWeight: 700, margin: 0 }}>✅ Curso habilitado</p>
              <p style={{ color: "var(--texto-suave)", fontSize: ".88rem", margin: "6px 0 0" }}>
                El cliente ya puede ver y usar el curso.
              </p>
            </div>
          );
        }
        return (
          <div style={{ ...box, background: "var(--verde-suave)", border: "1px solid #c3e6d3" }}>
            <p style={{ color: "var(--verde)", fontWeight: 700, marginBottom: 6 }}>✅ Curso listo — programado</p>
            <p style={{ color: "var(--texto-suave)", fontSize: ".88rem", marginBottom: 14 }}>
              El cliente verá el curso automáticamente el <strong>{dl!.toLocaleString("es-CO")}</strong> (12h desde su compra).
              ¿Cambiaste de opinión? Puedes habilitarlo ya mismo:
            </p>
            <form action={habilitarCursoAhora.bind(null, curso.id)}>
              <button className="btn btn-azul" style={{ padding: "10px 18px", fontSize: ".88rem" }}>
                ⚡ Habilitar curso ahora
              </button>
            </form>
          </div>
        );
      })()}

      {/* DÍA 1 — Introducción y tu entidad */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 12 }}>📅 Día 1 · Introducción y tu entidad</h2>
        {intro ? filaGuia(intro, false) : (
          <p style={{ color: "var(--texto-suave)", fontSize: ".85rem" }}>La presentación (INTRO-00) se auto-carga al confirmar la compra.</p>
        )}

        <h3 style={{ fontSize: ".9rem", margin: "18px 0 8px" }}>🏛️ Conoce tu Entidad</h3>
        {entidadAsignadas.length > 0 && (
          <div style={{ display: "grid", gap: 6, marginBottom: 12 }}>
            {entidadAsignadas.map((g: any) => filaGuia(g, true))}
          </div>
        )}
        {dispEntidad.length > 0 ? (
          <>
            <p style={{ color: "var(--texto-suave)", fontSize: ".8rem", marginBottom: 10 }}>
              Elige la guía de entidad que corresponde a la OPEC del cliente.
            </p>
            {selector(dispEntidad, "Selecciona la guía de entidad…")}
          </>
        ) : (
          <p style={{ color: "var(--texto-suave)", fontSize: ".82rem" }}>
            {entidadAsignadas.length > 0
              ? "Ya está asignada la guía de entidad."
              : "Aún no hay guías “Conoce tu Entidad” en la biblioteca. Créala (con su código ENT-…), súbela a la biblioteca y aquí podrás seleccionarla. Mientras tanto puedes usar la subida manual de abajo."}
          </p>
        )}
      </div>

      {/* Generales y por nivel (auto) */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 10 }}>📚 Generales y por nivel — auto-cargadas ({guiasAuto.length})</h2>
        {guiasAuto.length === 0 ? (
          <p style={{ color: "var(--texto-suave)", fontSize: ".85rem" }}>No hay guías auto-cargadas todavía.</p>
        ) : (
          <div style={{ display: "grid", gap: 6 }}>{guiasAuto.map((g: any) => filaGuia(g, false))}</div>
        )}
      </div>

      {/* Funcionales */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 10 }}>📝 Guías funcionales ({guiasFuncionales.length}/12)</h2>
        <form action={copiarPlanOPEC.bind(null, curso.id)} style={{ marginBottom: 14, padding: "12px 14px", background: "var(--azul-suave, #EAF1FB)", border: "1px solid #C9DCF4", borderRadius: 10 }}>
          <button className="btn btn-azul" style={{ padding: "9px 16px", fontSize: ".82rem" }}>
            ⚡ Copiar plan de otro curso del mismo OPEC
          </button>
          <p style={{ color: "var(--texto-suave)", fontSize: ".74rem", marginTop: 6, marginBottom: 0 }}>
            Trae funcionales, "Conoce tu Entidad" y simulacro desde otro curso ya armado con el mismo OPEC (no duplica lo que ya esté). Ideal para cursos del mismo cargo.
          </p>
        </form>
        {guiasFuncionales.length > 0 && (
          <div style={{ display: "grid", gap: 6, marginBottom: 14 }}>{guiasFuncionales.map((g: any) => filaGuia(g, true))}</div>
        )}
        {dispFuncionales.length > 0 ? (
          <>
            <p style={{ color: "var(--texto-suave)", fontSize: ".8rem", marginBottom: 10 }}>
              Selecciona del plan de estudio e indica el día/orden. Queda cargada al instante.
            </p>
            {selector(dispFuncionales, "Selecciona una guía funcional…")}
          </>
        ) : (
          <p style={{ color: "var(--texto-suave)", fontSize: ".82rem" }}>Ya están asignadas todas las funcionales disponibles en la biblioteca.</p>
        )}
      </div>

      {/* Simulacro */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 10 }}>🎯 Simulacro final ({guiasSimulacro.length})</h2>
        {guiasSimulacro.length > 0 && (
          <div style={{ display: "grid", gap: 6, marginBottom: 14 }}>{guiasSimulacro.map((g: any) => filaGuia(g, true))}</div>
        )}
        {dispSimulacro.length > 0 ? (
          selector(dispSimulacro, "Selecciona el simulacro…")
        ) : (
          <p style={{ color: "var(--texto-suave)", fontSize: ".82rem" }}>
            {guiasSimulacro.length > 0
              ? "Simulacro ya asignado."
              : "El simulacro final es único por OPEC. Cuando lo crees y lo subas a la biblioteca, aparecerá aquí para seleccionarlo."}
          </p>
        )}
      </div>

      {/* Subir guía personalizada (fallback) */}
      <div style={box}>
        <h2 style={{ fontSize: "1rem", marginBottom: 6 }}>⬆️ Subir guía personalizada (HTML)</h2>
        <p style={{ color: "var(--texto-suave)", fontSize: ".8rem", marginBottom: 10 }}>
          Solo para guías que aún NO están en la biblioteca (ej. una “Conoce tu Entidad” nueva). Lo ideal es subirla a la biblioteca para reutilizarla; esto es el respaldo rápido.
        </p>
        <form action={subirGuia.bind(null, curso.id)} style={{ display: "grid", gap: 10, gridTemplateColumns: "1fr 1fr" }}>
          <input style={input} type="text" name="titulo" placeholder="Título *" required />
          <input style={input} type="number" name="dia" placeholder="Día (ej. 9)" />
          <select style={input} name="tipo" defaultValue="funcional">
            <option value="general">General / Entidad</option>
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
