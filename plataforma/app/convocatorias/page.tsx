import Link from "next/link";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

type Conv = {
  id: string; nombre: string; entidad: string | null; etiqueta: string | null;
  vacantes: string | null; fecha_prueba_aprox: string | null; estado: string;
};

export default async function ConvocatoriasPage() {
  let convs: Conv[] = [];
  try {
    const supabase = createClient();
    const { data } = await supabase.from("convocatorias").select("*").eq("activa", true).order("orden");
    convs = (data as Conv[]) || [];
  } catch {
    convs = [];
  }

  return (
    <main style={{ maxWidth: 1080, margin: "0 auto", padding: "56px 22px" }}>
      <h1 style={{ fontSize: "2rem", marginBottom: 8 }}>Convocatorias disponibles</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 32 }}>
        Elige tu concurso y prepárate específicamente para tu cargo. ¿No ves la tuya? Escríbenos.
      </p>

      {convs.length === 0 ? (
        <div style={{ border: "1.5px dashed var(--gris-borde)", borderRadius: 14, padding: 30, textAlign: "center", color: "var(--texto-suave)" }}>
          Aún no hay convocatorias publicadas. (Se cargan desde el panel de administración.)
        </div>
      ) : (
        <div style={{ display: "grid", gap: 18, gridTemplateColumns: "repeat(auto-fit,minmax(280px,1fr))" }}>
          {convs.map((c) => (
            <div key={c.id} style={{ background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 14, padding: 22, boxShadow: "var(--sombra)" }}>
              {c.etiqueta && <span style={{ fontSize: ".72rem", fontWeight: 800, textTransform: "uppercase", color: "var(--verde)", background: "var(--verde-suave)", padding: "5px 12px", borderRadius: 20 }}>{c.etiqueta}</span>}
              <h3 style={{ fontSize: "1.1rem", margin: "12px 0 6px" }}>{c.nombre}</h3>
              {c.entidad && <div style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>{c.entidad}</div>}
              {c.vacantes && <div style={{ color: "var(--verde)", fontWeight: 700, fontSize: ".85rem", marginTop: 6 }}>🪑 {c.vacantes} vacantes</div>}
              {c.fecha_prueba_aprox && <div style={{ color: "var(--azul)", fontWeight: 600, fontSize: ".85rem", marginTop: 6 }}>{c.fecha_prueba_aprox}</div>}
              <Link href={`/convocatorias/${c.id}`} className="btn btn-oro" style={{ marginTop: 14, padding: "11px 18px", fontSize: ".9rem", display: "inline-flex" }}>Ver detalles</Link>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}
