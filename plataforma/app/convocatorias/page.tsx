import Link from "next/link";
import { createClient } from "@/lib/supabase/server";
import "../landing.css";

export const dynamic = "force-dynamic";

type Conv = {
  id: string;
  nombre: string;
  entidad: string | null;
  etiqueta: string | null;
  vacantes: string | null;
  fecha_prueba_aprox: string | null;
  estado: string;
  imagen_url: string | null;
};

export default async function ConvocatoriasPage() {
  let convs: Conv[] = [];
  try {
    const supabase = createClient();
    const { data } = await supabase
      .from("convocatorias")
      .select("id, nombre, entidad, estado, etiqueta, vacantes, fecha_prueba_aprox, imagen_url")
      .eq("activa", true)
      .order("orden");
    convs = (data as Conv[]) || [];
  } catch {
    convs = [];
  }

  return (
    <main style={{ maxWidth: 1080, margin: "0 auto", padding: "56px 22px" }}>
      <Link href="/" style={{ color: "var(--texto-suave)", fontSize: ".88rem" }}>← Volver al inicio</Link>
      <h1 style={{ fontSize: "2rem", marginBottom: 8, marginTop: 16 }}>Convocatorias disponibles</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 32 }}>
        Elige tu concurso y prepárate específicamente para tu cargo. ¿No ves la tuya? Escríbenos.
      </p>

      {convs.length === 0 ? (
        <div style={{ border: "1.5px dashed var(--gris-borde)", borderRadius: 14, padding: 30, textAlign: "center", color: "var(--texto-suave)" }}>
          Aún no hay convocatorias publicadas. Se cargan desde el panel de administración.
        </div>
      ) : (
        <div className="conv-grid">
          {convs.map((c) => (
            <div key={c.id} className="conv">
              <div className="conv-media">
                {c.imagen_url && (
                  // eslint-disable-next-line @next/next/no-img-element
                  <img src={c.imagen_url} alt={c.nombre} loading="lazy" />
                )}
                {c.etiqueta && (
                  <span className={`estado ${c.estado}`}>{c.etiqueta}</span>
                )}
              </div>
              <div className="conv-body">
                <h3>{c.nombre}</h3>
                {c.entidad && <div className="ent">{c.entidad}</div>}
                {c.vacantes && <div className="vac">🪑 {c.vacantes} vacantes</div>}
                {c.fecha_prueba_aprox && <div className="fecha">{c.fecha_prueba_aprox}</div>}
                <Link
                  href={`/convocatorias/${c.id}`}
                  className="btn btn-azul conv-btn"
                  style={{ padding: "11px 18px", fontSize: ".88rem", marginTop: 10 }}
                >
                  Conocer convocatoria
                </Link>
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}
