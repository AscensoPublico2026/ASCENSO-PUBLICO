/**
 * Componente que muestra el contador de cupos vendidos.
 * Se usa en la landing (sección precio) y en la página de compra.
 * 
 * Props:
 * - vendidos: número de pagos aprobados (cursos vendidos)
 * - total: cupos totales del lanzamiento (default: 100)
 */
export default function ContadorCupos({ vendidos, total = 100 }: { vendidos: number; total?: number }) {
  const restantes = Math.max(0, total - vendidos);
  const porcentaje = Math.min(100, Math.round((vendidos / total) * 100));

  return (
    <div style={{
      background: "linear-gradient(135deg, #0A2A5E, #1A4A8A)",
      borderRadius: 14,
      padding: "16px 20px",
      marginTop: 18,
      marginBottom: 18,
      color: "#fff",
    }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 10 }}>
        <span style={{ fontSize: ".82rem", fontWeight: 600, color: "rgba(255,255,255,.8)" }}>
          🔥 Precio de lanzamiento — cupos limitados
        </span>
        <span style={{ fontSize: ".78rem", fontWeight: 800, color: "#F6C56B" }}>
          {restantes > 0 ? `Quedan ${restantes}` : "¡Agotados!"}
        </span>
      </div>

      {/* Barra de progreso */}
      <div style={{ height: 8, borderRadius: 4, background: "rgba(255,255,255,.2)", overflow: "hidden" }}>
        <div style={{
          height: "100%",
          width: `${porcentaje}%`,
          background: "linear-gradient(90deg, #E8A33D, #F6C56B)",
          borderRadius: 4,
          transition: "width .5s ease",
        }} />
      </div>

      <div style={{ display: "flex", justifyContent: "space-between", marginTop: 8, fontSize: ".78rem" }}>
        <span style={{ color: "rgba(255,255,255,.7)" }}>
          <strong style={{ color: "#F6C56B" }}>{vendidos}</strong> cursos vendidos
        </span>
        <span style={{ color: "rgba(255,255,255,.7)" }}>
          de <strong>{total}</strong> del lanzamiento
        </span>
      </div>
    </div>
  );
}
