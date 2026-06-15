import Link from "next/link";

type Convocatoria = {
  id: string;
  nombre: string;
  entidad: string | null;
  estado: string;
  etiqueta: string | null;
  vacantes: string | null;
  fecha_prueba_aprox: string | null;
  imagen_url: string | null;
};

export default function ConvocatoriasGrid({ convocatorias }: { convocatorias: Convocatoria[] }) {
  if (convocatorias.length === 0) {
    return (
      <div style={{ gridColumn: "1/-1", textAlign: "center", color: "var(--texto-suave)", padding: 34, border: "1.5px dashed var(--gris-borde)", borderRadius: 14, background: "var(--blanco)" }}>
        Pronto publicaremos las convocatorias activas. Escríbenos para avisarte cuando abra la tuya.
      </div>
    );
  }

  return (
    <div className="conv-grid">
      {convocatorias.map((c) => (
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
            <Link href={`/convocatorias/${c.id}`} className="btn btn-azul conv-btn" style={{ padding: "11px 18px", fontSize: ".88rem", marginTop: 6 }}>
              Conocer convocatoria
            </Link>
          </div>
        </div>
      ))}
    </div>
  );
}
