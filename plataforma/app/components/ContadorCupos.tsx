import {
  CUPOS_TOTALES_LANZAMIENTO,
  CUPOS_VENDIDOS_LANZAMIENTO,
} from "@/lib/cupos";

/**
 * Contador compartido entre la landing y la página de compra.
 * Las cifras oficiales se mantienen en lib/cupos.ts para que ambas vistas
 * siempre muestren el mismo estado de la campaña.
 */
export default function ContadorCupos() {
  const vendidos = Math.min(CUPOS_TOTALES_LANZAMIENTO, CUPOS_VENDIDOS_LANZAMIENTO);
  const restantes = Math.max(0, CUPOS_TOTALES_LANZAMIENTO - vendidos);
  const porcentaje = Math.min(100, Math.round((vendidos / CUPOS_TOTALES_LANZAMIENTO) * 100));

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

      <div style={{ display: "flex", alignItems: "baseline", gap: 8, marginBottom: 8 }}>
        <span style={{ fontSize: "1.5rem", fontWeight: 900, color: "#F6C56B", lineHeight: 1 }}>
          {vendidos}/{CUPOS_TOTALES_LANZAMIENTO}
        </span>
        <span style={{ fontSize: ".82rem", fontWeight: 700, color: "rgba(255,255,255,.85)" }}>
          cupos vendidos
        </span>
      </div>

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
        {restantes > 0 ? (
          <>Ya hay <strong style={{ color: "#F6C56B" }}>{vendidos}</strong> aspirantes preparándose · asegura el tuyo antes de que se agoten.</>
        ) : (
          <>Los <strong style={{ color: "#F6C56B" }}>{CUPOS_TOTALES_LANZAMIENTO}</strong> cupos del precio de lanzamiento se han agotado. ¡Gracias por la confianza!</>
        )}
      </div>
    </div>
  );
}
