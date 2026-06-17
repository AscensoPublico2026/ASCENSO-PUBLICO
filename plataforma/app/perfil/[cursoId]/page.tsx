import Link from "next/link";
import { redirect, notFound } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { toTitleCase } from "@/lib/format";
import Contador from "../Contador";

export const dynamic = "force-dynamic";

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

  // Agrupar guías por tipo/sección
  const guiasPlan = (guias || []).filter((g: any) => g.tipo !== "bonus" && g.tipo !== "simulacro");
  const guiasBonus = (guias || []).filter((g: any) => g.tipo === "bonus");
  const guiasSimulacro = (guias || []).filter((g: any) => g.tipo === "simulacro");

  // Desbloqueo del simulacro: solo se activa cuando TODAS las guías con archivo
  // disponible (plan + bonus, excepto el propio simulacro) ya fueron leídas.
  const guiasRequeridas = (guias || []).filter((g: any) => g.tipo !== "simulacro" && g.archivo_path);
  const requeridasLeidas = guiasRequeridas.filter((g: any) => g.leida).length;
  const simulacroDesbloqueado = guiasRequeridas.length > 0 && requeridasLeidas === guiasRequeridas.length;
  const faltanSimulacro = guiasRequeridas.length - requeridasLeidas;

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
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 20 }}>
            <h2 style={{ fontSize: "1.15rem", margin: 0 }}>Tu biblioteca</h2>
            <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <div style={{ width: 120, height: 8, borderRadius: 4, background: "var(--gris-borde)", overflow: "hidden" }}>
                <div style={{ height: "100%", width: `${progresoPct}%`, background: "linear-gradient(90deg, #E8A33D, #F6C56B)", borderRadius: 4 }} />
              </div>
              <span style={{ fontSize: ".82rem", fontWeight: 700, color: "var(--azul)" }}>{progresoPct}%</span>
            </div>
          </div>

          {/* Sección: Plan de estudio */}
          {guiasPlan.length > 0 && (
            <SeccionGuias titulo="📘 Plan de estudio" guias={guiasPlan} />
          )}

          {/* Sección: Bonus */}
          {guiasBonus.length > 0 && (
            <SeccionGuias titulo="🎁 Bonus" guias={guiasBonus} />
          )}

          {/* Sección: Simulacro Final (se desbloquea al completar todas las guías) */}
          {guiasSimulacro.length > 0 && (
            simulacroDesbloqueado
              ? <SeccionGuias titulo="📝 Simulacro Final" guias={guiasSimulacro} />
              : <SimulacroBloqueado faltan={faltanSimulacro} total={guiasRequeridas.length} />
          )}

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

function SeccionGuias({ titulo, guias }: { titulo: string; guias: any[] }) {
  return (
    <div style={{ marginBottom: 28 }}>
      <h3 style={{ fontSize: ".95rem", color: "var(--azul)", marginBottom: 12, paddingBottom: 8, borderBottom: "1px solid var(--gris-borde)" }}>
        {titulo}
      </h3>
      <div style={{ display: "grid", gap: 8 }}>
        {guias.map((g: any) => (
          <Link
            key={g.id}
            href={`/guia/${g.id}`}
            style={{
              display: "flex",
              alignItems: "center",
              gap: 12,
              background: "#fff",
              border: "1px solid var(--gris-borde)",
              borderRadius: 12,
              padding: "12px 16px",
              transition: "transform .15s, box-shadow .15s",
              textDecoration: "none",
              color: "inherit",
            }}
          >
            {g.dia != null ? (
              <span style={{
                width: 36,
                height: 36,
                borderRadius: 9,
                background: "var(--azul)",
                color: "#fff",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontWeight: 800,
                fontSize: ".78rem",
                flexShrink: 0,
              }}>
                D{g.dia}
              </span>
            ) : (
              <span style={{
                width: 36,
                height: 36,
                borderRadius: 9,
                background: "linear-gradient(135deg, #E8A33D, #F6C56B)",
                color: "#0A2A5E",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontWeight: 800,
                fontSize: ".9rem",
                flexShrink: 0,
              }}>
                ★
              </span>
            )}
            <div style={{ flex: 1 }}>
              <span style={{ fontWeight: 600, fontSize: ".92rem" }}>{g.titulo}</span>
              {g.tipo && (
                <span style={{ display: "block", fontSize: ".72rem", color: "var(--texto-suave)", marginTop: 2 }}>
                  {g.tipo === "general" && "Conocimiento general"}
                  {g.tipo === "nivel" && "Competencias por nivel"}
                  {g.tipo === "funcional" && "Funciones del cargo"}
                  {g.tipo === "bonus" && "Material extra"}
                  {g.tipo === "simulacro" && "Evaluación"}
                </span>
              )}
            </div>
            {g.leida ? (
              <span style={{ color: "var(--verde)", fontSize: ".8rem", fontWeight: 700, display: "flex", alignItems: "center", gap: 4 }}>
                ✓ Leída
              </span>
            ) : (
              <span style={{ color: "var(--azul)", fontSize: ".85rem", fontWeight: 600 }}>→</span>
            )}
          </Link>
        ))}
      </div>
    </div>
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
