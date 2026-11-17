import Link from "next/link";
import { waUrl } from "@/lib/contacto";

type Convocatoria = {
  id: string;
  nombre: string;
  entidad: string | null;
  estado: string;
  etiqueta: string | null;
  vacantes: string | null;
  fecha_prueba_aprox: string | null;
  imagen_url: string | null;
  tema?: string | null;
};

/** Orden de aparición: primero donde todavía hay prueba por delante. */
const PESO_ESTADO: Record<string, number> = { abiertas: 0, proxima: 1, cerradas: 2 };

/**
 * Concursos que la gente ya busca pero que todavía no tienen OPEC ni manual de
 * funciones publicados. En cuanto los publiquen podemos armar el curso, así que
 * el botón invita a dejar el dato y no a esperar.
 */
const PROXIMAMENTE = [
  {
    nombre: "Corporaciones Autónomas Regionales (CAR)",
    entidad: "CNSC · 33 corporaciones ambientales",
    vacantes: "1.832",
    fecha: "Inscripciones aplazadas · nueva fecha por confirmar (se espera en 2027)",
    imagen: "/fotos/territorial-uapa.jpg",
    mensaje: "Hola, quiero el curso para el concurso de las CAR. Mi cargo es:",
  },
];

export default function ConvocatoriasGrid({ convocatorias }: { convocatorias: Convocatoria[] }) {
  const ordenadas = [...convocatorias].sort(
    (a, b) => (PESO_ESTADO[a.estado] ?? 1) - (PESO_ESTADO[b.estado] ?? 1)
  );

  if (ordenadas.length === 0) {
    return (
      <div style={{ gridColumn: "1/-1", textAlign: "center", color: "var(--texto-suave)", padding: 34, border: "1.5px dashed var(--gris-borde)", borderRadius: 14, background: "var(--blanco)" }}>
        Pronto publicaremos las convocatorias activas. Escríbenos para avisarte cuando abra la tuya.
      </div>
    );
  }

  return (
    <div className="conv-grid">
      {ordenadas.map((c) => {
        const cerrada = c.estado === "cerradas";
        return (
          <div key={c.id} className={`conv${cerrada ? " conv-cerrada" : ""}`}>
            <div className="conv-media">
              {c.imagen_url && (
                // eslint-disable-next-line @next/next/no-img-element
                <img src={c.imagen_url} alt={c.nombre} loading="lazy" />
              )}
              {c.etiqueta && <span className={`estado ${c.estado}`}>{c.etiqueta}</span>}
            </div>
            <div className="conv-body">
              <h3>{c.nombre}</h3>
              {c.entidad && <div className="ent">{c.entidad}</div>}
              {c.vacantes && <div className="vac">🪑 {c.vacantes} vacantes</div>}
              {c.fecha_prueba_aprox && (
                <div className="fecha">
                  <span className="fecha-label">📅 Qué sigue</span>
                  {c.fecha_prueba_aprox}
                </div>
              )}
              <Link
                href={c.tema === "docente" ? "/docentes" : `/convocatorias/${c.id}`}
                className={`btn ${cerrada ? "btn-ghost-conv" : "btn-azul"} conv-btn`}
                style={{ padding: "11px 18px", fontSize: ".88rem", marginTop: 6 }}
              >
                {cerrada ? "Ver estado" : "Prepararme para este concurso"}
              </Link>
            </div>
          </div>
        );
      })}
      {PROXIMAMENTE.map((p) => (
        <div key={p.nombre} className="conv conv-proximamente">
          <div className="conv-media">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={p.imagen} alt={p.nombre} loading="lazy" />
            <span className="estado proxima">Apenas publiquen la OPEC</span>
          </div>
          <div className="conv-body">
            <h3>{p.nombre}</h3>
            <div className="ent">{p.entidad}</div>
            <div className="vac">🪑 {p.vacantes} vacantes</div>
            <div className="fecha">
              <span className="fecha-label">📅 Qué sigue</span>
              {p.fecha}
            </div>
            <a
              href={waUrl(p.mensaje)}
              target="_blank"
              rel="noopener"
              className="btn btn-ghost-conv conv-btn"
              style={{ padding: "11px 18px", fontSize: ".88rem", marginTop: 6 }}
              data-analytics-event="whatsapp_clicked"
              data-analytics-placement="conv_proximamente"
            >
              💬 Escribirnos por WhatsApp
            </a>
          </div>
        </div>
      ))}
    </div>
  );
}
