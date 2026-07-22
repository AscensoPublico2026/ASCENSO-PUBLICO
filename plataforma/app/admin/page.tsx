import Link from "next/link";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

export default async function AdminHome() {
  const supabase = createClient();

  const { count: totalCursos } = await supabase.from("cursos").select("*", { count: "exact", head: true });
  const { count: cursosListo } = await supabase.from("cursos").select("*", { count: "exact", head: true }).eq("estado", "listo");
  const { count: cursosPrep } = await supabase.from("cursos").select("*", { count: "exact", head: true }).eq("estado", "en_preparacion");
  const { count: totalConvs } = await supabase.from("convocatorias").select("*", { count: "exact", head: true }).eq("activa", true);
  const { count: totalPagos } = await supabase.from("pagos").select("*", { count: "exact", head: true }).eq("estado", "aprobado");

  const stat: React.CSSProperties = {
    background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 16,
    padding: "22px 20px", boxShadow: "0 4px 20px rgba(10,42,94,.06)",
  };

  return (
    <div style={{ padding: "40px 28px", maxWidth: 900 }}>
      <h1 style={{ fontSize: "1.7rem", marginBottom: 8 }}>Dashboard</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 28 }}>Resumen general de Ascenso Público.</p>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))", gap: 16, marginBottom: 32 }}>
        <div style={stat}>
          <div style={{ fontSize: "2rem", fontFamily: "'Source Serif 4',serif", color: "var(--azul)" }}>{totalCursos ?? 0}</div>
          <div style={{ fontSize: ".85rem", color: "var(--texto-suave)", marginTop: 4 }}>Cursos totales</div>
        </div>
        <div style={stat}>
          <div style={{ fontSize: "2rem", fontFamily: "'Source Serif 4',serif", color: "var(--verde, #1A7A4A)" }}>{cursosListo ?? 0}</div>
          <div style={{ fontSize: ".85rem", color: "var(--texto-suave)", marginTop: 4 }}>Cursos listos</div>
        </div>
        <div style={stat}>
          <div style={{ fontSize: "2rem", fontFamily: "'Source Serif 4',serif", color: "#B8600A" }}>{cursosPrep ?? 0}</div>
          <div style={{ fontSize: ".85rem", color: "var(--texto-suave)", marginTop: 4 }}>En preparación</div>
        </div>
        <div style={stat}>
          <div style={{ fontSize: "2rem", fontFamily: "'Source Serif 4',serif", color: "var(--azul)" }}>{totalConvs ?? 0}</div>
          <div style={{ fontSize: ".85rem", color: "var(--texto-suave)", marginTop: 4 }}>Convocatorias activas</div>
        </div>
        <Link href="/admin/pagos" style={{ ...stat, display: "block", textDecoration: "none" }}>
          <div style={{ fontSize: "2rem", fontFamily: "'Source Serif 4',serif", color: "var(--verde, #1A7A4A)" }}>{totalPagos ?? 0}</div>
          <div style={{ fontSize: ".85rem", color: "var(--texto-suave)", marginTop: 4 }}>Pagos aprobados</div>
          <div style={{ fontSize: ".75rem", color: "var(--azul)", fontWeight: 700, marginTop: 6 }}>Ver detalle →</div>
        </Link>
      </div>

      <h2 style={{ fontSize: "1.1rem", marginBottom: 14 }}>Acciones rápidas</h2>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 16 }}>
        <Link href="/admin/cursos" style={{ ...stat, display: "block", transition: "transform .15s" }}>
          <div style={{ fontSize: "1.2rem", marginBottom: 6 }}>🎓</div>
          <div style={{ fontWeight: 700, color: "var(--azul)" }}>Gestionar cursos</div>
          <div style={{ color: "var(--texto-suave)", fontSize: ".85rem", marginTop: 4 }}>Ver clientes, subir guías funcionales y habilitar acceso.</div>
          {(cursosPrep ?? 0) > 0 && (
            <div style={{ marginTop: 10, background: "#FDF4E3", color: "#B8600A", fontWeight: 700, fontSize: ".78rem", padding: "4px 10px", borderRadius: 8, display: "inline-block" }}>
              ⚠️ {cursosPrep} curso{(cursosPrep ?? 0) > 1 ? "s" : ""} pendiente{(cursosPrep ?? 0) > 1 ? "s" : ""} de preparar
            </div>
          )}
        </Link>
        <Link href="/admin/convocatorias" style={{ ...stat, display: "block", transition: "transform .15s" }}>
          <div style={{ fontSize: "1.2rem", marginBottom: 6 }}>📋</div>
          <div style={{ fontWeight: 700, color: "var(--azul)" }}>Gestionar convocatorias</div>
          <div style={{ color: "var(--texto-suave)", fontSize: ".85rem", marginTop: 4 }}>Agregar, editar, activar/desactivar convocatorias.</div>
        </Link>
        <Link href="/admin/configuracion" style={{ ...stat, display: "block", transition: "transform .15s" }}>
          <div style={{ fontSize: "1.2rem", marginBottom: 6 }}>⚙️</div>
          <div style={{ fontWeight: 700, color: "var(--azul)" }}>Actualizar cupos vendidos</div>
          <div style={{ color: "var(--texto-suave)", fontSize: ".85rem", marginTop: 4 }}>Cambia el contador público sin modificar el código.</div>
        </Link>
      </div>
    </div>
  );
}
