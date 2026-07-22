import Link from "next/link";
import { createClient } from "@/lib/supabase/server";
import {
  CUPOS_TOTALES_LANZAMIENTO,
  CUPOS_VENDIDOS_LANZAMIENTO,
} from "@/lib/cupos";
import { actualizarCupos } from "./actions";

export const dynamic = "force-dynamic";

export default async function ConfiguracionPage({ searchParams }: { searchParams?: { guardado?: string } }) {
  const supabase = createClient();
  const { data, error } = await supabase
    .from("configuracion_cupos")
    .select("vendidos,total,updated_at")
    .eq("id", 1)
    .maybeSingle();

  const vendidos = data?.vendidos ?? CUPOS_VENDIDOS_LANZAMIENTO;
  const total = data?.total ?? CUPOS_TOTALES_LANZAMIENTO;
  const restantes = Math.max(0, total - vendidos);
  const porcentaje = total > 0 ? Math.min(100, Math.round((vendidos / total) * 100)) : 0;

  const input: React.CSSProperties = {
    width: "100%", padding: "12px 14px", borderRadius: 10,
    border: "1px solid var(--gris-borde)", fontFamily: "inherit", fontSize: "1rem",
  };
  const card: React.CSSProperties = {
    background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 16,
    padding: 24, boxShadow: "0 4px 20px rgba(10,42,94,.06)",
  };

  return (
    <main style={{ padding: "40px 28px", maxWidth: 820 }}>
      <Link href="/admin" style={{ color: "var(--texto-suave)", fontSize: ".88rem" }}>← Panel principal</Link>
      <h1 style={{ fontSize: "1.7rem", margin: "14px 0 6px" }}>Configuración</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 24 }}>
        Modifica las cifras que se muestran en el contador de la landing y de la página de compra.
      </p>

      {searchParams?.guardado === "1" && (
        <div role="status" style={{ background: "#E8F6EE", border: "1px solid #BFE6CF", color: "#17653B", borderRadius: 12, padding: "12px 16px", marginBottom: 16, fontWeight: 700 }}>
          ✓ Contador actualizado correctamente. El cambio ya se refleja en la página pública.
        </div>
      )}

      {error && (
        <div style={{ background: "#FFF8E8", border: "1px solid #E8A33D", color: "#6A4A16", borderRadius: 12, padding: "12px 16px", marginBottom: 16, fontSize: ".88rem" }}>
          La tabla de configuración aún no está disponible. Ejecuta primero <code>plataforma/supabase/migracion-configuracion-cupos.sql</code>. Mientras tanto se muestra el valor de respaldo {CUPOS_VENDIDOS_LANZAMIENTO}/{CUPOS_TOTALES_LANZAMIENTO}.
        </div>
      )}

      <div style={{ display: "grid", gridTemplateColumns: "minmax(0, 1fr) minmax(240px, .8fr)", gap: 18, alignItems: "start" }}>
        <form action={actualizarCupos} style={card}>
          <h2 style={{ fontSize: "1.05rem", marginBottom: 16 }}>Cupos del precio de lanzamiento</h2>
          <label style={{ display: "block", fontWeight: 700, fontSize: ".88rem", marginBottom: 16 }}>
            Cursos vendidos
            <input style={{ ...input, marginTop: 6 }} type="number" name="vendidos" min={0} defaultValue={vendidos} required />
            <small style={{ display: "block", color: "var(--texto-suave)", fontWeight: 400, marginTop: 5 }}>Esta es la cifra principal que puedes actualizar cada vez que vendas más cursos.</small>
          </label>
          <label style={{ display: "block", fontWeight: 700, fontSize: ".88rem", marginBottom: 18 }}>
            Total de cupos
            <input style={{ ...input, marginTop: 6 }} type="number" name="total" min={1} defaultValue={total} required />
          </label>
          <button className="btn btn-oro" style={{ width: "100%", padding: 12 }}>Guardar contador</button>
        </form>

        <section style={{ ...card, background: "linear-gradient(135deg, #0A2A5E, #1A4A8A)", color: "#fff" }}>
          <div style={{ color: "rgba(255,255,255,.72)", fontSize: ".78rem", fontWeight: 700 }}>VISTA ACTUAL</div>
          <div style={{ fontSize: "2.2rem", color: "#F6C56B", fontWeight: 900, margin: "10px 0 3px" }}>{vendidos}/{total}</div>
          <div style={{ fontSize: ".85rem", color: "rgba(255,255,255,.85)" }}>cursos vendidos · quedan {restantes}</div>
          <div style={{ height: 9, borderRadius: 5, background: "rgba(255,255,255,.2)", overflow: "hidden", marginTop: 16 }}>
            <div style={{ width: `${porcentaje}%`, height: "100%", background: "linear-gradient(90deg,#E8A33D,#F6C56B)" }} />
          </div>
          <div style={{ textAlign: "right", fontSize: ".75rem", color: "rgba(255,255,255,.7)", marginTop: 6 }}>{porcentaje}%</div>
          {data?.updated_at && <div style={{ fontSize: ".7rem", color: "rgba(255,255,255,.55)", marginTop: 14 }}>Última actualización: {new Date(data.updated_at).toLocaleString("es-CO")}</div>}
        </section>
      </div>
    </main>
  );
}
