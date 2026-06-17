import Link from "next/link";
import { redirect, notFound } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { toTitleCase } from "@/lib/format";
import Contador from "../Contador";

export const dynamic = "force-dynamic";

// Módulos del currículo (estilo plataforma de aprendizaje). El orden define
// cómo se muestran al estudiante. Cada guía se clasifica con moduloKey().
type ModuloDef = { key: string; icon: string; titulo: string; desc: string };
const MODULOS: ModuloDef[] = [
  { key: "introduccion", icon: "🚀", titulo: "Introducción", desc: "Empieza aquí: cómo funciona tu curso y tu entidad." },
  { key: "generales", icon: "🏛️", titulo: "Conocimientos Generales", desc: "El Estado, la función pública y el marco institucional." },
  { key: "nivel", icon: "🎯", titulo: "Competencias por Nivel", desc: "Competencias comportamentales propias de tu nivel." },
  { key: "funcional", icon: "🧩", titulo: "Funciones del Cargo", desc: "El conocimiento técnico específico de tu empleo." },
  { key: "bonus", icon: "🎁", titulo: "Material Bonus", desc: "Contenido extra para reforzar. Opcional, pero recomendado." },
  { key: "simulacro", icon: "📝", titulo: "Simulacro Final", desc: "Pon a prueba todo lo que aprendiste, como en la prueba real." },
];

function moduloKey(g: any): string {
  if (g.tipo === "simulacro") return "simulacro";
  if (g.tipo === "bonus") return "bonus";
  if (g.tipo === "funcional") return "funcional";
  if (g.tipo === "nivel") return "nivel";
  // INTRO-00 y "Conoce tu Entidad" (ENT-) van a Introducción; el resto de
  // generales (GEN-) quedan en Conocimientos Generales.
  if (/(^|\/)(INTRO|ENT)-/i.test(g.archivo_path || "") || g.dia === 1) return "introduccion";
  return "generales";
}


export default async function CursoDetallePage({ params }: { params: { cursoId: string } }) {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  // Obtener el curso con su convocatoria
  const { data: curso } = await supabase
    .from("cursos")
    .select("*, convocatorias(nombre, imagen_url, entidad)")
    .eq("id", params.cursoId)
    .eq("usuario_id", user.id)
    .single();

  if (!curso) notFound();

  // Obtener las guías del curso
  const { data: guias } = await supabase
    .from("guias_curso")
    .select("*")
    .eq("curso_id", curso.id)
    .order("orden", { ascending: true });

  const cargoNombre = toTitleCase(curso.cargo_nombre || "Curso personalizado");
  const convNombre = curso.convocatorias?.nombre || "";
  const imagenUrl = curso.convocatorias?.imagen_url || null;

  // Desbloqueo del simulacro: solo se activa cuando TODAS las guías del PLAN
  // con archivo disponible (generales/nivel/funcionales) ya fueron leídas.
  // El bonus NO es obligatorio para desbloquear; el simulacro tampoco se cuenta.
  const guiasRequeridas = (guias || []).filter((g: any) => g.tipo !== "simulacro" && g.tipo !== "bonus" && g.archivo_path);
  const requeridasLeidas = guiasRequeridas.filter((g: any) => g.leida).length;
  const simulacroDesbloqueado = guiasRequeridas.length > 0 && requeridasLeidas === guiasRequeridas.length;
  const faltanSimulacro = guiasRequeridas.length - requeridasLeidas;

  // Agrupar guías en MÓDULOS (estilo currículo) y ordenarlas dentro de cada uno.
  const porModulo: Record<string, any[]> = {};
  (guias || []).forEach((g: any) => {
    const k = moduloKey(g);
    (porModulo[k] = porModulo[k] || []).push(g);
  });
  Object.values(porModulo).forEach((arr) =>
    arr.sort((a: any, b: any) => (a.orden ?? a.dia ?? 0) - (b.orden ?? b.dia ?? 0))
  );
  // Módulo abierto por defecto: el primero que tenga guías por leer.
  const moduloAbierto =
    (MODULOS.find((m) => (porModulo[m.key] || []).some((g: any) => g.archivo_path && !g.leida)) ||
      MODULOS.find((m) => (porModulo[m.key] || []).length > 0) ||
      { key: "" }).key;

  // Calcular progreso EN VIVO: % de guías (con archivo disponible) que ya fueron leídas.
  // Solo cuentan las guías que tienen archivo (las funcionales/simulacro pendientes no penalizan).
  const guiasDisponibles = (guias || []).filter((g: any) => g.archivo_path);
  const guiasLeidas = guiasDisponibles.filter((g: any) => g.leida).length;
  const progresoPct = guiasDisponibles.length > 0
    ? Math.round((guiasLeidas / guiasDisponibles.length) * 100)
    : 0;

  // Sincronizar el campo del curso (para que aparezca igual en la lista de /perfil)
  if (curso.estado === "listo" && progresoPct !== curso.progreso_pct) {
    await supabase.from("cursos").update({ progreso_pct: progresoPct }).eq("id", curso.id);
  }

  return (
    <main style={{ maxWidth: 800, margin: "0 auto", padding: "40px 22px 80px" }}>
      {/* Back link */}
      <Link href="/perfil" style={{ color: "var(--texto-suave)", fontSize: ".88rem", display: "inline-flex", alignItems: "center", gap: 6 }}>
        ← Mis cursos
      </Link>

      {/* Hero mini del curso */}
      <div style={{
        position: "relative",
        borderRadius: 18,
        overflow: "hidden",
        marginTop: 16,
        height: 160,
        display: "flex",
        alignItems: "flex-end",
        background: "linear-gradient(135deg, #0A2A5E, #1A4A8A)",
      }}>
        {imagenUrl && (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={imagenUrl} alt={convNombre} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", opacity: 0.5 }} />
        )}
        <div style={{ position: "absolute", inset: 0, background: "linear-gradient(to top, rgba(10,42,94,.9), rgba(10,42,94,.3))" }} />
        <div style={{ position: "relative", zIndex: 2, padding: "20px 24px" }}>
          {curso.opec && (
            <span style={{ display: "inline-block", background: "linear-gradient(135deg, #E8A33D, #F6C56B)", color: "#0A2A5E", fontWeight: 800, fontSize: ".7rem", padding: "3px 9px", borderRadius: 6, marginBottom: 6 }}>
              OPEC {curso.opec}
            </span>
          )}
          <h1 style={{ color: "#fff", fontSize: "1.4rem", margin: 0 }}>{cargoNombre}</h1>
          {convNombre && <p style={{ color: "rgba(255,255,255,.7)", fontSize: ".85rem", margin: "2px 0 0" }}>{convNombre}</p>}
        </div>
      </div>

      {/* Estado del curso */}
      {curso.estado === "en_preparacion" && (
        <div style={{
          background: "#FDF4E3",
          border: "1px solid #F0DCB0",
          borderRadius: 14,
          padding: "20px 24px",
          marginTop: 20,
        }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 12 }}>
            <span style={{ fontSize: "1.2rem" }}>⏳</span>
            <span style={{ fontWeight: 800, color: "#B8600A", fontSize: ".82rem", textTransform: "uppercase" }}>Curso en preparación</span>
          </div>
          <p style={{ color: "var(--texto-suave)", margin: "0 0 14px" }}>
            Estamos armando tu ruta personalizada. Estará lista en máximo:
          </p>
          {curso.preparacion_deadline && <Contador deadline={curso.preparacion_deadline} />}
        </div>
      )}

      {/* Biblioteca de guías */}
      {curso.estado === "listo" && (() => {
        // Verificar si el deadline ya pasó (si existe)
        const deadlinePasado = !curso.preparacion_deadline || new Date(curso.preparacion_deadline).getTime() <= Date.now();

        if (!deadlinePasado) {
          // Curso listo pero aún no pasan las 12h — mostrar contador
          return (
            <div style={{
              background: "var(--verde-suave)",
              border: "1px solid #c3e6d3",
              borderRadius: 14,
              padding: "20px 24px",
              marginTop: 20,
            }}>
              <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 12 }}>
                <span style={{ fontSize: "1.2rem" }}>✅</span>
                <span style={{ fontWeight: 800, color: "var(--verde)", fontSize: ".82rem", textTransform: "uppercase" }}>Tu curso está casi listo</span>
              </div>
              <p style={{ color: "var(--texto-suave)", margin: "0 0 14px" }}>
                Tu ruta de estudio ya fue preparada. Estará disponible en:
              </p>
              <Contador deadline={curso.preparacion_deadline} />
            </div>
          );
        }

        // Deadline pasado → mostrar guías
        return (
          <div style={{ marginTop: 24 }}>
          {/* Progreso */}
          <div style={{ background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 16, padding: "20px 22px", marginBottom: 26, boxShadow: "0 2px 12px rgba(10,42,94,.05)" }}>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: 12, marginBottom: 12, flexWrap: "wrap" }}>
              <div>
                <h2 style={{ fontSize: "1.1rem", margin: 0 }}>Tu ruta de estudio</h2>
                <p style={{ fontSize: ".84rem", color: "var(--texto-suave)", margin: "3px 0 0" }}>
                  {guiasLeidas} de {guiasDisponibles.length} guías completadas
                </p>
              </div>
              <span style={{ fontSize: "1.7rem", fontWeight: 800, color: "var(--azul)" }}>{progresoPct}%</span>
            </div>
            <div style={{ height: 10, borderRadius: 6, background: "var(--gris-borde)", overflow: "hidden" }}>
              <div style={{ height: "100%", width: `${progresoPct}%`, background: "linear-gradient(90deg, #E8A33D, #F6C56B)", borderRadius: 6, transition: "width .4s ease" }} />
            </div>
          </div>

          {/* Módulos del currículo (acordeón) */}
          {MODULOS.map((m) => {
            const gs = porModulo[m.key] || [];
            if (gs.length === 0) return null;
            // Simulacro bloqueado: tarjeta de bloqueo en vez del módulo.
            if (m.key === "simulacro" && !simulacroDesbloqueado) {
              return <SimulacroBloqueado key={m.key} faltan={faltanSimulacro} total={guiasRequeridas.length} />;
            }
            const total = gs.filter((g: any) => g.archivo_path).length;
            const leidas = gs.filter((g: any) => g.archivo_path && g.leida).length;
            return (
              <ModuloGuias
                key={m.key}
                modulo={m}
                guias={gs}
                total={total}
                leidas={leidas}
                abierto={m.key === moduloAbierto}
              />
            );
          })}

          {/* Si no hay guías aún */}
          {(!guias || guias.length === 0) && (
            <p style={{ color: "var(--texto-suave)", textAlign: "center", padding: 30 }}>
              Pronto verás aquí tus guías por día. Estamos terminando de armar tu ruta.
            </p>
          )}
        </div>
        );
      })()}

      {/* Vencimiento */}
      {curso.fecha_vencimiento && (
        <p style={{ color: "var(--texto-suave)", fontSize: ".8rem", marginTop: 24, textAlign: "center" }}>
          Acceso válido hasta {new Date(curso.fecha_vencimiento).toLocaleDateString("es-CO")}.
        </p>
      )}
    </main>
  );
}

const TIPO_LABEL: Record<string, string> = {
  general: "Conocimiento general",
  nivel: "Competencias por nivel",
  funcional: "Funciones del cargo",
  bonus: "Material extra",
  simulacro: "Evaluación final",
};

function FilaGuia({ g }: { g: any }) {
  const dispo = !!g.archivo_path;
  return (
    <Link
      href={`/guia/${g.id}`}
      className="guia-row"
      style={{
        display: "flex",
        alignItems: "center",
        gap: 14,
        background: "#fff",
        border: `1px solid ${g.leida ? "#c3e6d3" : "var(--gris-borde)"}`,
        borderRadius: 14,
        padding: "13px 16px",
        textDecoration: "none",
        color: "inherit",
      }}
    >
      {g.dia != null ? (
        <span style={{
          width: 46, height: 46, borderRadius: 12, flexShrink: 0,
          background: g.leida ? "var(--verde)" : "linear-gradient(135deg, #0A2A5E, #1A4A8A)",
          color: "#fff", display: "flex", flexDirection: "column",
          alignItems: "center", justifyContent: "center", lineHeight: 1,
        }}>
          <span style={{ fontSize: ".5rem", fontWeight: 700, letterSpacing: ".08em", opacity: .85 }}>DÍA</span>
          <span style={{ fontSize: "1.15rem", fontWeight: 800 }}>{g.dia}</span>
        </span>
      ) : (
        <span style={{
          width: 46, height: 46, borderRadius: 12, flexShrink: 0,
          background: "linear-gradient(135deg, #E8A33D, #F6C56B)", color: "#0A2A5E",
          display: "flex", alignItems: "center", justifyContent: "center", fontSize: "1.3rem", fontWeight: 800,
        }}>★</span>
      )}

      <div style={{ flex: 1, minWidth: 0 }}>
        <span style={{ fontWeight: 700, fontSize: ".95rem", color: "var(--azul)", display: "block" }}>{g.titulo}</span>
        {g.tipo && (
          <span style={{ display: "block", fontSize: ".74rem", color: "var(--texto-suave)", marginTop: 2 }}>
            {TIPO_LABEL[g.tipo] || g.tipo}
          </span>
        )}
      </div>

      {g.leida ? (
        <span style={{ color: "var(--verde)", fontSize: ".8rem", fontWeight: 700, whiteSpace: "nowrap" }}>✓ Completada</span>
      ) : dispo ? (
        <span style={{ color: "#fff", background: "linear-gradient(135deg, #0A2A5E, #1A4A8A)", fontSize: ".78rem", fontWeight: 700, padding: "7px 14px", borderRadius: 20, whiteSpace: "nowrap" }}>Comenzar →</span>
      ) : (
        <span style={{ color: "var(--texto-suave)", fontSize: ".76rem", fontWeight: 600, whiteSpace: "nowrap" }}>Próximamente</span>
      )}
    </Link>
  );
}

function ModuloGuias({ modulo, guias, total, leidas, abierto }: {
  modulo: ModuloDef; guias: any[]; total: number; leidas: number; abierto: boolean;
}) {
  const completo = total > 0 && leidas === total;
  const pct = total > 0 ? Math.round((leidas / total) * 100) : 0;
  return (
    <details className="modulo" open={abierto}>
      <summary className="modulo-sum">
        <span className="modulo-ic">{completo ? "✅" : modulo.icon}</span>
        <span style={{ flex: 1, minWidth: 0 }}>
          <span className="modulo-tit">{modulo.titulo}</span>
          <span className="modulo-desc">{modulo.desc}</span>
        </span>
        {total > 0 && (
          <span className="modulo-meta">
            <span className="modulo-bar"><span style={{ width: `${pct}%` }} /></span>
            <span className="modulo-cont" style={completo ? { color: "var(--verde)", borderColor: "#c3e6d3", background: "var(--verde-suave)" } : undefined}>
              {leidas}/{total}
            </span>
          </span>
        )}
      </summary>
      <div className="modulo-body">
        {guias.map((g: any) => <FilaGuia key={g.id} g={g} />)}
      </div>
    </details>
  );
}

function SimulacroBloqueado({ faltan, total }: { faltan: number; total: number }) {
  const completadas = total - faltan;
  const pct = total > 0 ? Math.round((completadas / total) * 100) : 0;
  return (
    <div style={{ marginBottom: 28 }}>
      <h3 style={{ fontSize: ".95rem", color: "var(--azul)", marginBottom: 12, paddingBottom: 8, borderBottom: "1px solid var(--gris-borde)" }}>
        📝 Simulacro Final
      </h3>
      <div style={{
        background: "var(--gris-bg, #F2F0EA)",
        border: "1px dashed var(--gris-borde)",
        borderRadius: 12,
        padding: "20px 18px",
        textAlign: "center",
      }}>
        <div style={{ fontSize: "1.8rem", marginBottom: 8 }}>🔒</div>
        <p style={{ fontWeight: 700, color: "var(--azul)", margin: "0 0 6px", fontSize: ".95rem" }}>
          Simulacro bloqueado
        </p>
        <p style={{ color: "var(--texto-suave)", margin: "0 0 14px", fontSize: ".86rem", lineHeight: 1.5 }}>
          El simulacro final se desbloquea cuando completes <strong>todas las guías</strong> de tu plan de estudio.
          {faltan > 0 && (
            <> Te {faltan === 1 ? "falta" : "faltan"} <strong>{faltan}</strong> {faltan === 1 ? "guía" : "guías"} por leer.</>
          )}
        </p>
        <div style={{ display: "flex", alignItems: "center", gap: 10, justifyContent: "center" }}>
          <div style={{ width: 140, height: 8, borderRadius: 4, background: "var(--gris-borde)", overflow: "hidden" }}>
            <div style={{ height: "100%", width: `${pct}%`, background: "linear-gradient(90deg, #E8A33D, #F6C56B)", borderRadius: 4 }} />
          </div>
          <span style={{ fontSize: ".8rem", fontWeight: 700, color: "var(--azul)" }}>{completadas}/{total}</span>
        </div>
      </div>
    </div>
  );
}
