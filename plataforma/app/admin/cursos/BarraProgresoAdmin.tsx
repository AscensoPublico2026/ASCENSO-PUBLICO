/**
 * Barra de progreso del ESTUDIANTE para el PANEL ADMIN.
 * Muestra cuántas guías (con archivo) ya marcó como leídas el estudiante,
 * sobre el total de guías asignadas a su curso. Es un componente de
 * presentación puro (sin estado ni reloj) — el cálculo del % se hace en el
 * servidor a partir de guias_curso (mismo criterio que usa /perfil).
 *
 * Props:
 * - leidas: cantidad de guías con archivo_path marcadas como leida=true.
 * - total: cantidad total de guías con archivo_path asignadas al curso.
 * - compact: versión reducida para tablas (lista de cursos).
 */
export default function BarraProgresoAdmin({
  leidas,
  total,
  compact = false,
}: {
  leidas: number;
  total: number;
  compact?: boolean;
}) {
  const pct = total > 0 ? Math.round((leidas / total) * 100) : 0;

  if (total === 0) {
    return <span style={{ fontSize: ".78rem", color: "var(--texto-suave)" }}>Sin guías asignadas</span>;
  }

  // Color según avance: rojo/gris si apenas empieza, oro a mitad, verde si va bien.
  let color = "#8A94A3";
  if (pct >= 100) color = "#1A7A4A";
  else if (pct >= 50) color = "#E8A33D";
  else if (pct > 0) color = "#B8600A";

  return (
    <div style={{ minWidth: compact ? 120 : 180 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: 4 }}>
        <span style={{ fontSize: ".72rem", fontWeight: 700, color }}>
          📚 {leidas}/{total} guías
        </span>
        {!compact && (
          <span style={{ fontSize: ".68rem", color: "var(--texto-suave)" }}>{pct}% avanzado</span>
        )}
      </div>
      <div style={{
        height: compact ? 6 : 8,
        borderRadius: 4,
        background: "#EDEAE2",
        overflow: "hidden",
        border: "1px solid var(--gris-borde)",
      }}>
        <div style={{
          height: "100%",
          width: `${pct}%`,
          background: "linear-gradient(90deg, #E8A33D, #F6C56B)",
          borderRadius: 4,
        }} />
      </div>
    </div>
  );
}
