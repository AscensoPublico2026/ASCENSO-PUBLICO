import { redirect, notFound } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

/**
 * Visor de guía: muestra el HTML embebido a través de /api/guia/[id].
 * El middleware ya protege esta ruta, pero mantenemos la verificación por seguridad.
 */
export default async function GuiaPage({ params }: { params: { id: string } }) {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  // Obtener datos de la guía y del curso (para el link de regreso)
  const { data: guia } = await supabase
    .from("guias_curso")
    .select("id, titulo, archivo_path, dia, tipo, curso_id")
    .eq("id", params.id)
    .single();

  if (!guia) notFound();

  // Si no tiene archivo, mostrar un aviso (guía aún no cargada por admin)
  if (!guia.archivo_path) {
    return (
      <main style={{ maxWidth: 620, margin: "0 auto", padding: "60px 22px", textAlign: "center" }}>
        <div style={{ fontSize: "2.4rem", marginBottom: 12 }}>📝</div>
        <h1 style={{ fontSize: "1.4rem", marginBottom: 8 }}>{guia.titulo}</h1>
        <p style={{ color: "var(--texto-suave)", marginBottom: 24 }}>
          Esta guía aún está siendo preparada por nuestro equipo. Estará disponible pronto.
        </p>
        <a href={`/perfil/${guia.curso_id}`} style={{ color: "var(--azul)", fontWeight: 700 }}>← Volver a mi curso</a>
      </main>
    );
  }

  // Tipo de badge
  const tipoLabel: Record<string, string> = {
    general: "Conocimiento general",
    nivel: "Competencias por nivel",
    funcional: "Funciones del cargo",
    bonus: "Material bonus",
    simulacro: "Evaluación",
  };

  return (
    <main style={{ height: "100vh", display: "flex", flexDirection: "column" }}>
      {/* Header del visor */}
      <div style={{
        padding: "12px 20px",
        borderBottom: "1px solid var(--gris-borde)",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        background: "#fff",
        boxShadow: "0 2px 8px rgba(0,0,0,.04)",
        flexShrink: 0,
      }}>
        <a
          href={`/perfil/${guia.curso_id}`}
          style={{ color: "var(--azul)", fontWeight: 700, fontSize: ".9rem", display: "flex", alignItems: "center", gap: 6 }}
        >
          ← Mi curso
        </a>

        <div style={{ textAlign: "center", flex: 1, padding: "0 16px" }}>
          <strong style={{ color: "var(--azul)", fontSize: ".92rem", display: "block" }}>
            {guia.titulo}
          </strong>
          <span style={{ fontSize: ".72rem", color: "var(--texto-suave)" }}>
            {guia.dia != null && `Día ${guia.dia}`}
            {guia.dia != null && guia.tipo && " · "}
            {guia.tipo && (tipoLabel[guia.tipo] || guia.tipo)}
          </span>
        </div>

        <div style={{ width: 80 }}>{/* Spacer para centrar el título */}</div>
      </div>

      {/* Iframe con la guía */}
      <iframe
        src={`/api/guia/${params.id}`}
        style={{ flex: 1, width: "100%", border: "none" }}
        title={guia.titulo}
      />
    </main>
  );
}
