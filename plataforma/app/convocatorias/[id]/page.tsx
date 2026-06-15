import Link from "next/link";
import { createClient } from "@/lib/supabase/server";
import { notFound } from "next/navigation";

export const dynamic = "force-dynamic";

export default async function ConvocatoriaDetalle({ params }: { params: { id: string } }) {
  const supabase = createClient();
  const { data: conv } = await supabase
    .from("convocatorias")
    .select("*")
    .eq("id", params.id)
    .single();

  if (!conv) notFound();

  const estadoColor: Record<string, { bg: string; color: string }> = {
    abiertas: { bg: "var(--verde-suave)", color: "var(--verde)" },
    proxima: { bg: "#FDF4E3", color: "#B8600A" },
    cerradas: { bg: "#EAF1FB", color: "var(--azul)" },
  };
  const sc = estadoColor[conv.estado] || estadoColor.proxima;

  return (
    <main style={{ maxWidth: 840, margin: "0 auto", padding: "40px 22px 80px" }}>
      {/* Breadcrumb */}
      <Link href="/#convocatorias" style={{ color: "var(--texto-suave)", fontSize: ".88rem", display: "inline-flex", alignItems: "center", gap: 6 }}>
        ← Volver a convocatorias
      </Link>

      {/* Hero de la convocatoria */}
      <div style={{
        position: "relative",
        borderRadius: 20,
        overflow: "hidden",
        marginTop: 20,
        height: 220,
        background: "linear-gradient(135deg, #0A2A5E, #1A4A8A)",
        display: "flex",
        alignItems: "flex-end",
      }}>
        {conv.imagen_url && (
          // eslint-disable-next-line @next/next/no-img-element
          <img
            src={conv.imagen_url}
            alt={conv.nombre}
            style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", opacity: 0.7 }}
          />
        )}
        <div style={{
          position: "relative",
          zIndex: 2,
          padding: "24px 28px",
          background: "linear-gradient(transparent, rgba(10,42,94,.85))",
          width: "100%",
        }}>
          {conv.etiqueta && (
            <span style={{
              display: "inline-block",
              fontSize: ".72rem",
              fontWeight: 800,
              textTransform: "uppercase",
              letterSpacing: ".04em",
              padding: "5px 12px",
              borderRadius: 20,
              background: sc.bg,
              color: sc.color,
              marginBottom: 8,
            }}>
              {conv.etiqueta}
            </span>
          )}
          <h1 style={{ color: "#fff", fontSize: "clamp(1.5rem, 3.5vw, 2.2rem)", margin: 0 }}>
            {conv.nombre}
          </h1>
        </div>
      </div>

      {/* Contenido principal */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "1fr 320px",
        gap: 28,
        marginTop: 28,
      }}>
        {/* Info */}
        <div style={{ background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 16, padding: 28, boxShadow: "var(--sombra)" }}>
          <h2 style={{ fontSize: "1.2rem", marginBottom: 16 }}>Información de la convocatoria</h2>

          <div style={{ display: "grid", gap: 14 }}>
            {conv.entidad && (
              <div>
                <div style={{ fontSize: ".78rem", fontWeight: 700, color: "var(--texto-suave)", textTransform: "uppercase", letterSpacing: ".05em" }}>Entidad</div>
                <div style={{ fontWeight: 600, marginTop: 4 }}>{conv.entidad}</div>
              </div>
            )}
            {conv.vacantes && (
              <div>
                <div style={{ fontSize: ".78rem", fontWeight: 700, color: "var(--texto-suave)", textTransform: "uppercase", letterSpacing: ".05em" }}>Vacantes</div>
                <div style={{ fontWeight: 600, marginTop: 4, color: "var(--verde)" }}>🪑 {conv.vacantes}</div>
              </div>
            )}
            {conv.fecha_prueba_aprox && (
              <div>
                <div style={{ fontSize: ".78rem", fontWeight: 700, color: "var(--texto-suave)", textTransform: "uppercase", letterSpacing: ".05em" }}>Estado / Fechas</div>
                <div style={{ fontWeight: 600, marginTop: 4, color: "var(--azul)" }}>{conv.fecha_prueba_aprox}</div>
              </div>
            )}
          </div>

          <hr style={{ border: "none", borderTop: "1px solid var(--gris-borde)", margin: "22px 0" }} />

          <h3 style={{ fontSize: "1rem", marginBottom: 10 }}>¿Qué preparamos para esta convocatoria?</h3>
          <ul style={{ listStyle: "none", padding: 0, display: "grid", gap: 10 }}>
            <li style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span style={{ width: 22, height: 22, borderRadius: "50%", background: "var(--verde-suave)", color: "var(--verde)", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 800, fontSize: ".7rem", flexShrink: 0 }}>✓</span>
              Plan de 21 días personalizado por tu cargo (OPEC + manual de funciones)
            </li>
            <li style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span style={{ width: 22, height: 22, borderRadius: "50%", background: "var(--verde-suave)", color: "var(--verde)", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 800, fontSize: ".7rem", flexShrink: 0 }}>✓</span>
              Guías de conocimiento general + competencias por nivel + funcionales
            </li>
            <li style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span style={{ width: 22, height: 22, borderRadius: "50%", background: "var(--verde-suave)", color: "var(--verde)", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 800, fontSize: ".7rem", flexShrink: 0 }}>✓</span>
              Simulacros de juicio situacional tipo CNSC con retroalimentación
            </li>
            <li style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span style={{ width: 22, height: 22, borderRadius: "50%", background: "var(--verde-suave)", color: "var(--verde)", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 800, fontSize: ".7rem", flexShrink: 0 }}>✓</span>
              Guía de estrategia CNSC + simulacro integral final
            </li>
          </ul>
        </div>

        {/* Sidebar — Tarjeta de compra */}
        <div style={{
          background: "#fff",
          border: "2px solid var(--oro, #E8A33D)",
          borderRadius: 18,
          padding: 26,
          boxShadow: "0 10px 36px rgba(10,42,94,.12)",
          height: "fit-content",
          position: "sticky",
          top: 90,
        }}>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: ".78rem", fontWeight: 700, color: "var(--ambar, #B8600A)", textTransform: "uppercase", letterSpacing: ".08em", marginBottom: 6 }}>
              Precio de lanzamiento
            </div>
            <div style={{ fontFamily: "'Source Serif 4',serif", fontSize: "2.4rem", color: "var(--azul)", fontWeight: 700 }}>
              $300.000 <span style={{ fontSize: ".9rem", color: "var(--texto-suave)", fontWeight: 600 }}>COP</span>
            </div>
            <p style={{ fontSize: ".85rem", color: "var(--texto-suave)", margin: "6px 0 18px" }}>Pago único · acceso completo</p>
          </div>

          <Link
            href={`/comprar?conv=${conv.id}`}
            className="btn btn-oro"
            style={{ width: "100%", padding: "14px 20px", fontSize: ".95rem", textAlign: "center" }}
          >
            Comprar mi curso →
          </Link>

          <p style={{ fontSize: ".78rem", color: "var(--texto-suave)", textAlign: "center", marginTop: 12 }}>
            Pago seguro con Wompi · PSE, Nequi y tarjetas
          </p>

          <div style={{
            display: "flex",
            alignItems: "center",
            gap: 10,
            marginTop: 16,
            background: "var(--verde-suave)",
            borderRadius: 10,
            padding: "10px 14px",
            color: "var(--verde)",
            fontWeight: 600,
            fontSize: ".82rem",
          }}>
            <span>🛡️</span>
            <span>Tu ruta lista en máximo 12 horas</span>
          </div>
        </div>
      </div>

      {/* Responsive: sidebar debajo en mobile */}
      <style>{`
        @media(max-width: 768px) {
          main > div:last-of-type {
            grid-template-columns: 1fr !important;
          }
        }
      `}</style>
    </main>
  );
}
