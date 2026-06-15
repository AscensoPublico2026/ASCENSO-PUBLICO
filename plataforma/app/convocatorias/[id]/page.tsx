import Link from "next/link";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

export default async function ConvocatoriaDetalle({ params }: { params: { id: string } }) {
  let conv: any = null;
  try {
    const supabase = createClient();
    const { data } = await supabase.from("convocatorias").select("*").eq("id", params.id).single();
    conv = data;
  } catch {
    conv = null;
  }

  if (!conv) {
    return (
      <main style={{ maxWidth: 720, margin: "0 auto", padding: "60px 22px", textAlign: "center" }}>
        <h1 style={{ fontSize: "1.6rem" }}>Convocatoria no encontrada</h1>
        <p style={{ color: "var(--texto-suave)", marginTop: 10 }}>
          <Link href="/convocatorias" style={{ color: "var(--azul)", textDecoration: "underline" }}>Ver todas las convocatorias</Link>
        </p>
      </main>
    );
  }

  return (
    <main style={{ maxWidth: 760, margin: "0 auto", padding: "56px 22px" }}>
      <Link href="/convocatorias" style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>← Convocatorias</Link>
      {conv.etiqueta && (
        <div style={{ marginTop: 16 }}>
          <span style={{ fontSize: ".72rem", fontWeight: 800, textTransform: "uppercase", color: "var(--verde)", background: "var(--verde-suave)", padding: "5px 12px", borderRadius: 20 }}>{conv.etiqueta}</span>
        </div>
      )}
      <h1 style={{ fontSize: "2rem", margin: "12px 0 8px" }}>{conv.nombre}</h1>
      {conv.entidad && <p style={{ color: "var(--texto-suave)" }}>{conv.entidad}</p>}

      <div style={{ background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 16, padding: 26, marginTop: 24, boxShadow: "var(--sombra)" }}>
        {conv.vacantes && <p style={{ marginBottom: 8 }}><strong>Vacantes:</strong> {conv.vacantes}</p>}
        {conv.fecha_prueba_aprox && <p style={{ marginBottom: 8 }}><strong>Pruebas:</strong> {conv.fecha_prueba_aprox}</p>}
        <p style={{ color: "var(--texto-suave)", marginTop: 12 }}>
          Prepárate específicamente para tu cargo en esta convocatoria: analizamos tu OPEC y tu manual de
          funciones y te entregamos un plan de 21 días con guías y simulacros tipo CNSC.
        </p>
        <Link href={`/comprar?conv=${conv.id}`} className="btn btn-oro" style={{ marginTop: 20, padding: "14px 28px", display: "inline-flex" }}>
          Adquirir ahora — $300.000
        </Link>
      </div>
    </main>
  );
}
