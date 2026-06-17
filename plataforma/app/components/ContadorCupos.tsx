/**
 * Componente que muestra el contador de cupos vendidos.
 * Se usa en la landing (sección precio) y en la página de compra.
 *
 * Props:
 * - vendidos: número de pagos aprobados REALES (cursos vendidos)
 * - total: cupos totales del lanzamiento (default: 100)
 *
 * Piso de cupos (prueba social):
 * - Para generar confianza desde el inicio, se suma un "piso" base a las ventas
 *   reales. Así el contador nunca arranca en 0 y crece con cada venta real.
 * - Se controla con la variable de entorno NEXT_PUBLIC_CUPOS_BASE (ej. 35).
 *   Si no está definida, usa 35 por defecto. Para cambiar el número: ajusta esa
 *   variable en Vercel (y redespliega) — no hay que tocar código.
 */
const CUPOS_BASE = Math.max(0, Number(process.env.NEXT_PUBLIC_CUPOS_BASE ?? 35));

export default function ContadorCupos({ vendidos, total = 100 }: { vendidos: number; total?: number }) {
  // Ventas reales + piso base, sin pasarse del total.
  const vendidosMostrados = Math.min(total, vendidos + CUPOS_BASE);
  const restantes = Math.max(0, total - vendidosMostrados);
  const porcentaje = Math.min(100, Math.round((vendidosMostrados / total) * 100));

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

      {/* Conteo grande y claro: 35/100 */}
      <div style={{ display: "flex", alignItems: "baseline", gap: 8, marginBottom: 8 }}>
        <span style={{ fontSize: "1.5rem", fontWeight: 900, color: "#F6C56B", lineHeight: 1 }}>
          {vendidosMostrados}/{total}
        </span>
        <span style={{ fontSize: ".82rem", fontWeight: 700, color: "rgba(255,255,255,.85)" }}>
          cupos vendidos
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

      <div style={{ marginTop: 8, fontSize: ".78rem", color: "rgba(255,255,255,.7)" }}>
        Ya hay <strong style={{ color: "#F6C56B" }}>{vendidosMostrados}</strong> aspirantes preparándose · asegura el tuyo antes de que se agoten.
      </div>
    </div>
  );
}
