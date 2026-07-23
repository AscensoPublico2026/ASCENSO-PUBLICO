import Link from "next/link";
import { redirect, notFound } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { toTitleCase } from "@/lib/format";
import { waUrl, WA_MENSAJES } from "@/lib/contacto";
import Contador from "../Contador";

export const dynamic = "force-dynamic";

// Módulos del currículo (estilo plataforma de aprendizaje). El orden define
// cómo se muestran al estudiante. Cada guía se clasifica con moduloKey().
type ModuloDef = { key: string; icon: string; titulo: string; desc: string; intro: string };
const MODULOS: ModuloDef[] = [
  { key: "introduccion", icon: "🚀", titulo: "Introducción", desc: "Empieza aquí: cómo funciona tu curso y tu entidad.",
    intro: "Aquí arranca tu preparación. Conocerás cómo funciona la CNSC, cómo aprovechar al máximo el curso y la entidad a la que aspiras, para llegar con contexto al resto del plan." },
  { key: "generales", icon: "🏛️", titulo: "Conocimientos Generales", desc: "El Estado, la función pública y el marco institucional.",
    intro: "En estas guías encontrarás los fundamentos del Estado colombiano: qué es el Estado y la función pública, la relación entre el Estado y el ciudadano, y el marco institucional. Son la base común que la CNSC evalúa en cualquier cargo." },
  { key: "nivel", icon: "🎯", titulo: "Competencias por Nivel", desc: "Competencias comportamentales propias de tu nivel.",
    intro: "Aquí estudiarás las competencias comportamentales propias de tu nivel: cómo se espera que actúes, te relaciones y cumplas en tu cargo. La CNSC las evalúa con casos de juicio situacional." },
  { key: "funcional", icon: "🧩", titulo: "Funciones del Cargo", desc: "El conocimiento técnico específico de tu empleo.",
    intro: "El corazón de tu preparación: el conocimiento técnico específico de tu empleo. Dominarás las funciones reales del cargo, sus procedimientos y la normatividad que las rige." },
  { key: "bonus", icon: "🎁", titulo: "Material Bonus", desc: "Contenido extra para reforzar. Opcional, pero recomendado.",
    intro: "Material extra para potenciar tu preparación: estrategia para presentar la prueba y manejo de herramientas ofimáticas. Es opcional, pero te da una ventaja real el día del examen." },
  { key: "simulacro", icon: "📝", titulo: "Simulacro Final", desc: "Pon a prueba todo lo que aprendiste, como en la prueba real.",
    intro: "La prueba final: integra todo tu plan en preguntas tipo CNSC (juicio situacional). Mide tu nivel real, te muestra las respuestas correctas y te dice qué temas reforzar antes del examen." },
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

// Rango de días que cubre un módulo (ej. "Días 2–4", "Día 1") o null si no aplica.
function rangoDias(gs: any[]): string | null {
  const dias = gs.map((g) => g.dia).filter((d) => d != null) as number[];
  if (!dias.length) return null;
  const min = Math.min(...dias), max = Math.max(...dias);
  return min === max ? `Día ${min}` : `Días ${min}–${max}`;
}

const ESTADO_LABEL: Record<string, string> = { completo: "Completado", encurso: "En curso", pendiente: "Pendiente" };
function estadoModulo(total: number, leidas: number): "completo" | "encurso" | "pendiente" {
  if (total > 0 && leidas === total) return "completo";
  if (leidas > 0) return "encurso";
  return "pendiente";
}


export default async function CursoDetallePage({ params }: { params: { cursoId: string } }) {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  // ¿Es admin? El admin puede previsualizar cualquier curso (no solo los suyos).
  const { data: perfil } = await supabase.from("profiles").select("rol").eq("id", user.id).single();
  const esAdmin = perfil?.rol === "admin";

  // Obtener el curso con su convocatoria. El estudiante solo ve los suyos; el admin, cualquiera.
  let cursoQuery = supabase
    .from("cursos")
    .select("*, convocatorias(nombre, imagen_url, entidad)")
    .eq("id", params.cursoId);
  if (!esAdmin) cursoQuery = cursoQuery.eq("usuario_id", user.id);
  const { data: curso } = await cursoQuery.single();

  if (!curso) notFound();

  // Modo vista previa: admin revisando un curso que no es suyo (antes de habilitarlo).
  const esPreview = esAdmin && curso.usuario_id !== user.id;

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
  const simulacroDesbloqueado = esPreview || (guiasRequeridas.length > 0 && requeridasLeidas === guiasRequeridas.length);
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

  // Módulos que tienen guías (para numerarlos secuencialmente sin huecos).
  const modulosVisibles = MODULOS.filter((m) => (porModulo[m.key] || []).length > 0);
  // Próxima guía a estudiar (primera disponible y no leída, en orden de módulos).
  let proximaGuia: any = null;
  for (const m of MODULOS) {
    if (m.key === "simulacro" && !simulacroDesbloqueado) continue;
    const next = (porModulo[m.key] || []).find((g: any) => g.archivo_path && !g.leida);
    if (next) { proximaGuia = next; break; }
  }

  // Calcular progreso EN VIVO: % de guías (con archivo disponible) que ya fueron leídas.
  // Solo cuentan las guías que tienen archivo (las funcionales/simulacro pendientes no penalizan).
  const guiasDisponibles = (guias || []).filter((g: any) => g.archivo_path);
  const guiasLeidas = guiasDisponibles.filter((g: any) => g.leida).length;
  const progresoPct = guiasDisponibles.length > 0
    ? Math.round((guiasLeidas / guiasDisponibles.length) * 100)
    : 0;

  // Sincronizar el campo del curso (para que aparezca igual en la lista de /perfil)
  if (!esPreview && curso.estado === "listo" && progresoPct !== curso.progreso_pct) {
    await supabase.from("cursos").update({ progreso_pct: progresoPct }).eq("id", curso.id);
  }

  return (
    <main style={{ maxWidth: 800, margin: "0 auto", padding: "40px 22px 80px" }}>
      {/* Back link */}
      <Link href={esPreview ? `/admin/cursos/${curso.id}` : "/perfil"} style={{ color: "var(--texto-suave)", fontSize: ".88rem", display: "inline-flex", alignItems: "center", gap: 6 }}>
        ← {esPreview ? "Volver al panel del curso" : "Mis cursos"}
      </Link>

      {/* Banner de vista previa (admin) */}
      {esPreview && (
        <div style={{ marginTop: 14, background: "#FDF4E3", border: "1px solid #F0DCB0", borderRadius: 12, padding: "12px 16px", display: "flex", alignItems: "center", gap: 10 }}>
          <span style={{ fontSize: "1.2rem" }}>👁️</span>
          <span style={{ fontSize: ".86rem", color: "#B8600A" }}>
            <strong>Vista previa (admin).</strong> Estás viendo el curso tal como lo verá el estudiante. Aquí no se marca el progreso y el simulacro se muestra desbloqueado para que lo revises.
          </span>
        </div>
      )}

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
      {curso.estado === "en_preparacion" && !esPreview && (
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

          {/* Ficha de datos del curso */}
          <DatosCurso curso={curso} convNombre={convNombre} cargoNombre={cargoNombre} />
        </div>
      )}

      {/* Biblioteca de guías */}
      {(curso.estado === "listo" || esPreview) && (() => {
        // Verificar si el deadline ya pasó (si existe)
        const deadlinePasado = !curso.preparacion_deadline || new Date(curso.preparacion_deadline).getTime() <= Date.now();

        if (!esPreview && !deadlinePasado) {
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
              {/* Ficha de datos del curso */}
              <DatosCurso curso={curso} convNombre={convNombre} cargoNombre={cargoNombre} />
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
            <p style={{ display: "flex", alignItems: "center", gap: 8, margin: "14px 0 0", fontSize: ".82rem", color: "var(--texto-suave)", background: "var(--crema)", borderRadius: 10, padding: "10px 12px" }}>
              <span style={{ fontSize: "1rem" }}>⏱️</span>
              <span>Dedica <strong style={{ color: "var(--azul)" }}>60 a 90 minutos al día</strong>: una guía por sesión. Estudia de lunes a viernes y descansa los fines de semana: una guía por día hasta tu simulacro final.</span>
            </p>
          </div>

          {/* Continúa donde quedaste */}
          {proximaGuia && <ContinuarBanner guia={proximaGuia} />}

          {/* Módulos del currículo (acordeón) */}
          {modulosVisibles.map((m, idx) => {
            const gs = porModulo[m.key] || [];
            // Simulacro bloqueado: tarjeta de bloqueo en vez del módulo.
            if (m.key === "simulacro" && !simulacroDesbloqueado) {
              return <SimulacroBloqueado key={m.key} numero={idx + 1} faltan={faltanSimulacro} total={guiasRequeridas.length} />;
            }
            const total = gs.filter((g: any) => g.archivo_path).length;
            const leidas = gs.filter((g: any) => g.archivo_path && g.leida).length;
            return (
              <ModuloGuias
                key={m.key}
                numero={idx + 1}
                modulo={m}
                guias={gs}
                total={total}
                leidas={leidas}
                rango={rangoDias(gs)}
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

      {/* Botón flotante de WhatsApp: dudas / asistencia sobre el curso */}
      {!esPreview && (
        <a
          href={waUrl(WA_MENSAJES.soporte)}
          target="_blank"
          rel="noopener"
          aria-label="¿Dudas? Escríbenos por WhatsApp"
          style={{
            position: "fixed", right: 18, bottom: 18, zIndex: 200,
            display: "inline-flex", alignItems: "center", gap: 9,
            background: "#25D366", color: "#fff", fontWeight: 800, fontSize: ".9rem",
            padding: "13px 18px", borderRadius: 30, textDecoration: "none",
            boxShadow: "0 10px 26px rgba(37,211,102,.45)",
          }}
        >
          <svg width={22} height={22} viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15h-.01c-1.52 0-3.01-.41-4.3-1.18l-.31-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.37c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.82 2.42a8.18 8.18 0 0 1 2.41 5.82c0 4.54-3.69 8.23-8.23 8.23z"/></svg>
          <span>¿Dudas?</span>
        </a>
      )}
    </main>
  );
}

// ---------- Ficha de datos del curso (visible mientras espera las 24h) ----------
function DatosCurso({ curso, convNombre, cargoNombre }: { curso: any; convNombre: string; cargoNombre: string }) {
  const filas: { icon: string; label: string; value: string }[] = [];

  if (curso.opec) filas.push({ icon: "🔢", label: "N.° de inscripción (OPEC)", value: curso.opec });
  if (cargoNombre) filas.push({ icon: "💼", label: "Cargo", value: cargoNombre });
  if (convNombre) filas.push({ icon: "📋", label: "Convocatoria", value: convNombre });
  if (curso.nivel) filas.push({ icon: "🎯", label: "Nivel", value: curso.nivel.charAt(0).toUpperCase() + curso.nivel.slice(1) });
  if (curso.fecha_vencimiento) filas.push({ icon: "📅", label: "Acceso válido hasta", value: new Date(curso.fecha_vencimiento).toLocaleDateString("es-CO", { year: "numeric", month: "long", day: "numeric" }) });

  if (filas.length === 0) return null;

  return (
    <div style={{
      marginTop: 18,
      background: "rgba(255,255,255,.7)",
      border: "1px solid #F0DCB0",
      borderRadius: 12,
      overflow: "hidden",
    }}>
      <div style={{ padding: "10px 16px", borderBottom: "1px solid #F0DCB0", display: "flex", alignItems: "center", gap: 7 }}>
        <span style={{ fontSize: ".72rem", fontWeight: 800, textTransform: "uppercase", letterSpacing: ".06em", color: "#B8600A" }}>
          📄 Datos de tu inscripción
        </span>
      </div>
      {filas.map((f, i) => (
        <div key={f.label} style={{
          display: "flex",
          alignItems: "center",
          gap: 12,
          padding: "10px 16px",
          borderBottom: i < filas.length - 1 ? "1px solid #FEF3C7" : "none",
          background: i % 2 === 0 ? "transparent" : "rgba(254,243,199,.35)",
        }}>
          <span style={{ fontSize: "1rem", flexShrink: 0 }}>{f.icon}</span>
          <span style={{ fontSize: ".8rem", color: "#92400E", minWidth: 180, flexShrink: 0 }}>{f.label}</span>
          <span style={{ fontSize: ".88rem", fontWeight: 700, color: "#0A2A5E" }}>{f.value}</span>
        </div>
      ))}
    </div>
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

function ModuloGuias({ numero, modulo, guias, total, leidas, rango, abierto }: {
  numero: number; modulo: ModuloDef; guias: any[]; total: number; leidas: number; rango: string | null; abierto: boolean;
}) {
  const estado = estadoModulo(total, leidas);
  const pct = total > 0 ? Math.round((leidas / total) * 100) : 0;
  return (
    <details className="modulo" open={abierto}>
      <summary className="modulo-sum">
        <span className={`modulo-num ${estado}`}>{estado === "completo" ? "✓" : numero}</span>
        <span style={{ flex: 1, minWidth: 0 }}>
          <span className="modulo-tit">{modulo.icon} {modulo.titulo}</span>
          <span className="modulo-chips">
            {rango && <span className="chip chip-dia">📅 {rango}</span>}
            <span className="chip">📖 {total} {total === 1 ? "guía" : "guías"}</span>
            <span className={`chip estado-${estado}`}>{ESTADO_LABEL[estado]}</span>
          </span>
        </span>
        <span className="modulo-prog">
          <span className="modulo-bar"><span style={{ width: `${pct}%` }} /></span>
          <span className="modulo-cont">{leidas}/{total}</span>
        </span>
      </summary>
      <div className="modulo-body">
        <p className="modulo-intro"><span className="modulo-intro-ic">💡</span>{modulo.intro}</p>
        {guias.map((g: any) => <FilaGuia key={g.id} g={g} />)}
      </div>
    </details>
  );
}

function ContinuarBanner({ guia }: { guia: any }) {
  return (
    <Link href={`/guia/${guia.id}`} className="continuar">
      <div style={{ minWidth: 0 }}>
        <span className="continuar-label">▶ Continúa donde quedaste</span>
        <span className="continuar-title">
          {guia.dia != null ? `Día ${guia.dia} · ` : ""}{guia.titulo}
        </span>
      </div>
      <span className="continuar-btn">Continuar →</span>
    </Link>
  );
}

function SimulacroBloqueado({ numero, faltan, total }: { numero: number; faltan: number; total: number }) {
  const completadas = total - faltan;
  const pct = total > 0 ? Math.round((completadas / total) * 100) : 0;
  return (
    <div className="modulo modulo-locked">
      <div className="modulo-sum" style={{ cursor: "default" }}>
        <span className="modulo-num locked">🔒</span>
        <span style={{ flex: 1, minWidth: 0 }}>
          <span className="modulo-tit">📝 Simulacro Final</span>
          <span className="modulo-chips">
            <span className="chip chip-dia">📅 Día 21</span>
            <span className="chip estado-bloqueado">Bloqueado</span>
          </span>
        </span>
        <span className="modulo-prog">
          <span className="modulo-bar"><span style={{ width: `${pct}%` }} /></span>
          <span className="modulo-cont">{completadas}/{total}</span>
        </span>
      </div>
      <div className="modulo-body" style={{ paddingTop: 4 }}>
        <p className="modulo-intro"><span className="modulo-intro-ic">💡</span>La prueba final: integra todo tu plan en preguntas tipo CNSC. Mide tu nivel real y te dice qué reforzar antes del examen.</p>
        <div style={{ background: "var(--crema)", border: "1px dashed var(--gris-borde)", borderRadius: 12, padding: "16px 18px", textAlign: "center" }}>
          <p style={{ color: "var(--texto-suave)", margin: 0, fontSize: ".88rem", lineHeight: 1.55 }}>
            Se desbloquea cuando completes <strong>todas las guías de tu plan</strong>.
            {faltan > 0 && (
              <> Te {faltan === 1 ? "falta" : "faltan"} <strong>{faltan}</strong> {faltan === 1 ? "guía" : "guías"} por leer.</>
            )}
          </p>
        </div>
      </div>
    </div>
  );
}
