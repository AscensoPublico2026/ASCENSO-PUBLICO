import Link from "next/link";
import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { toTitleCase } from "@/lib/format";
import LogoutButton from "./LogoutButton";
import CambiarPassword from "./CambiarPassword";
import { waUrl, WA_MENSAJES } from "@/lib/contacto";

export const dynamic = "force-dynamic";

export default async function PerfilPage() {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  // Traer todos los cursos del usuario con datos de convocatoria
  const { data: cursos } = await supabase
    .from("cursos")
    .select("*, convocatorias(nombre, imagen_url, entidad)")
    .eq("usuario_id", user.id)
    .order("created_at", { ascending: false });

  const nombre = toTitleCase((user.user_metadata as any)?.nombre || user.email || "");

  // Verificar si es admin para mostrar botón de panel
  const { data: profile } = await supabase.from("profiles").select("rol").eq("id", user.id).single();
  const isAdmin = profile?.rol === "admin";

  // Progreso EN VIVO por curso: % de guías con archivo que ya fueron leídas.
  // No dependemos del valor guardado (curso.progreso_pct), que puede quedar
  // desactualizado; lo calculamos desde guias_curso (que el alumno sí puede leer).
  const progresoPorCurso: Record<string, number> = {};
  const cursoIds = (cursos || []).map((c: any) => c.id);
  if (cursoIds.length > 0) {
    const { data: gs } = await supabase
      .from("guias_curso")
      .select("curso_id, archivo_path, leida")
      .in("curso_id", cursoIds);
    for (const id of cursoIds) {
      const disp = (gs || []).filter((g: any) => g.curso_id === id && g.archivo_path);
      const leidas = disp.filter((g: any) => g.leida).length;
      progresoPorCurso[id] = disp.length > 0 ? Math.round((leidas / disp.length) * 100) : 0;
    }
  }

  return (
    <main style={{ maxWidth: 860, margin: "0 auto", padding: "40px 22px 80px" }}>
      {/* Header del perfil */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 32 }}>
        <div>
          <div style={{ color: "var(--texto-suave)", fontSize: ".82rem" }}>Bienvenido,</div>
          <h1 style={{ fontSize: "1.4rem", margin: 0 }}>{nombre}</h1>
        </div>
        <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
          {isAdmin && (
            <a href="/admin" style={{ background: "linear-gradient(135deg, #E8A33D, #F6C56B)", color: "#0A2A5E", fontWeight: 800, fontSize: ".82rem", padding: "8px 14px", borderRadius: 10, textDecoration: "none" }}>
              ⚙️ Panel admin
            </a>
          )}
          <LogoutButton />
        </div>
      </div>

      {/* Cambiar contraseña */}
      <CambiarPassword />

      {/* Multi-curso: grid de tarjetas */}
      {!cursos || cursos.length === 0 ? (
        <EmptyState />
      ) : cursos.length === 1 ? (
        <>
          <CursoCard curso={cursos[0]} progresoPct={progresoPorCurso[cursos[0].id] ?? 0} expanded />
          <ComprarOtroCurso />
        </>
      ) : (
        <>
          <h2 style={{ fontSize: "1.1rem", color: "var(--texto-suave)", marginBottom: 18 }}>
            Tus cursos ({cursos.length})
          </h2>
          <div style={{ display: "grid", gap: 20, gridTemplateColumns: "repeat(auto-fit, minmax(340px, 1fr))" }}>
            {cursos.map((curso: any) => (
              <CursoCard key={curso.id} curso={curso} progresoPct={progresoPorCurso[curso.id] ?? 0} />
            ))}
          </div>
          <ComprarOtroCurso />
        </>
      )}
    </main>
  );
}

function ComprarOtroCurso() {
  return (
    <div style={{
      marginTop: 24,
      border: "1.5px dashed var(--gris-borde)",
      borderRadius: 16,
      padding: "24px 28px",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      gap: 16,
      flexWrap: "wrap",
      background: "#fff",
    }}>
      <div>
        <h3 style={{ fontSize: "1rem", margin: "0 0 4px" }}>¿Aplicas a otra convocatoria?</h3>
        <p style={{ color: "var(--texto-suave)", fontSize: ".88rem", margin: 0 }}>
          Puedes preparar otro cargo con su propio plan personalizado.
        </p>
      </div>
      <Link href="/comprar" className="btn btn-oro" style={{ padding: "11px 22px", whiteSpace: "nowrap" }}>
        + Comprar otro curso
      </Link>
    </div>
  );
}

function EmptyState() {
  return (
    <div style={{
      border: "1.5px dashed var(--gris-borde)",
      borderRadius: 18,
      padding: "48px 30px",
      textAlign: "center",
    }}>
      <div style={{ fontSize: "2.4rem", marginBottom: 12 }}>📚</div>
      <h2 style={{ fontSize: "1.2rem", marginBottom: 8 }}>Aún no tienes cursos</h2>
      <p style={{ color: "var(--texto-suave)", marginBottom: 20 }}>
        Cuando compres tu curso personalizado aparecerá aquí con tu ruta de estudio.
      </p>
      <Link href="/comprar" className="btn btn-oro" style={{ padding: "12px 24px" }}>
        Comprar mi curso
      </Link>
      <p style={{ color: "var(--texto-suave)", fontSize: ".82rem", marginTop: 14 }}>
        ¿Ya pagaste y no ves tu curso? <a href={waUrl(WA_MENSAJES.soporte)} target="_blank" rel="noopener" style={{ color: "var(--azul)", fontWeight: 700 }}>Escríbenos por WhatsApp</a>
      </p>
    </div>
  );
}

function CursoCard({ curso, progresoPct, expanded }: { curso: any; progresoPct?: number; expanded?: boolean }) {
  const imagenUrl = curso.convocatorias?.imagen_url || null;
  const convNombre = curso.convocatorias?.nombre || "";
  const cargoNombre = toTitleCase(curso.cargo_nombre || "Curso personalizado");
  const opec = curso.opec || "";
  const pct = progresoPct ?? curso.progreso_pct ?? 0;

  const estadoBadge: Record<string, { label: string; bg: string; color: string }> = {
    en_preparacion: { label: "En preparación", bg: "#FDF4E3", color: "#B8600A" },
    listo: { label: "Curso listo", bg: "var(--verde-suave)", color: "var(--verde)" },
    vencido: { label: "Vencido", bg: "#F5F5F5", color: "#888" },
  };
  const badge = estadoBadge[curso.estado] || estadoBadge.en_preparacion;

  return (
    <Link
      href={`/perfil/${curso.id}`}
      style={{ textDecoration: "none", color: "inherit", display: "block" }}
    >
      <div style={{
        position: "relative",
        borderRadius: 20,
        overflow: "hidden",
        boxShadow: "0 8px 32px rgba(10,42,94,.12)",
        transition: "transform .2s, box-shadow .2s",
        cursor: "pointer",
        minHeight: expanded ? 240 : 200,
        display: "flex",
        flexDirection: "column",
        justifyContent: "flex-end",
      }}
        className="curso-card-hover"
      >
        {/* Imagen de fondo */}
        <div style={{
          position: "absolute",
          inset: 0,
          background: "linear-gradient(135deg, #0A2A5E, #1A4A8A)",
        }}>
          {imagenUrl && (
            // eslint-disable-next-line @next/next/no-img-element
            <img
              src={imagenUrl}
              alt={convNombre}
              style={{ width: "100%", height: "100%", objectFit: "cover", opacity: 0.55 }}
            />
          )}
        </div>

        {/* Overlay gradiente */}
        <div style={{
          position: "absolute",
          inset: 0,
          background: "linear-gradient(to top, rgba(10,42,94,.92) 0%, rgba(10,42,94,.6) 50%, rgba(10,42,94,.3) 100%)",
        }} />

        {/* Contenido */}
        <div style={{ position: "relative", zIndex: 2, padding: expanded ? "28px 28px" : "22px 24px" }}>
          {/* OPEC Badge */}
          {opec && (
            <span style={{
              display: "inline-block",
              background: "linear-gradient(135deg, #E8A33D, #F6C56B)",
              color: "#0A2A5E",
              fontWeight: 800,
              fontSize: ".72rem",
              letterSpacing: ".04em",
              padding: "4px 10px",
              borderRadius: 8,
              marginBottom: 10,
            }}>
              OPEC {opec}
            </span>
          )}

          {/* Cargo (Title Case, grande) */}
          <h2 style={{
            color: "#fff",
            fontSize: expanded ? "1.5rem" : "1.2rem",
            fontWeight: 800,
            margin: "0 0 4px",
            lineHeight: 1.2,
          }}>
            {cargoNombre}
          </h2>

          {/* Convocatoria (subtítulo) */}
          {convNombre && (
            <p style={{
              color: "rgba(255,255,255,.75)",
              fontSize: ".88rem",
              margin: "0 0 12px",
            }}>
              {convNombre}
            </p>
          )}

          {/* Footer: estado + progreso */}
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: 12 }}>
            <span style={{
              display: "inline-block",
              fontSize: ".7rem",
              fontWeight: 800,
              textTransform: "uppercase",
              letterSpacing: ".04em",
              padding: "4px 10px",
              borderRadius: 14,
              background: badge.bg,
              color: badge.color,
            }}>
              {badge.label}
            </span>

            {curso.estado === "listo" && (
              <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                <div style={{
                  width: 80,
                  height: 6,
                  borderRadius: 3,
                  background: "rgba(255,255,255,.25)",
                  overflow: "hidden",
                }}>
                  <div style={{
                    height: "100%",
                    width: `${pct}%`,
                    background: "linear-gradient(90deg, #E8A33D, #F6C56B)",
                    borderRadius: 3,
                  }} />
                </div>
                <span style={{ color: "rgba(255,255,255,.7)", fontSize: ".72rem", fontWeight: 600 }}>
                  {pct}%
                </span>
              </div>
            )}
          </div>

          {/* Vencimiento */}
          {curso.fecha_vencimiento && (
            <p style={{ color: "rgba(255,255,255,.5)", fontSize: ".72rem", marginTop: 8 }}>
              Acceso hasta {new Date(curso.fecha_vencimiento).toLocaleDateString("es-CO")}
            </p>
          )}
        </div>
      </div>
    </Link>
  );
}
