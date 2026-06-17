import { createClient } from "@/lib/supabase/server";
import { crearConvocatoria, toggleConvocatoria, eliminarConvocatoria } from "./actions";

export const dynamic = "force-dynamic";

// Imágenes ya cargadas en /public/fotos (para el desplegable de "elegir existente").
const IMAGENES_DISPONIBLES = [
  "nacional.jpg", "territorial12.jpg", "territorial-uapa.jpg",
  "dian.jpg", "procuraduria.jpg", "ese.jpg", "hero.jpg",
];

export default async function AdminConvocatorias() {
  const supabase = createClient();
  const { data: convs } = await supabase.from("convocatorias").select("*").order("orden");

  const input: React.CSSProperties = { width: "100%", padding: "10px 12px", borderRadius: 10, border: "1px solid var(--gris-borde)", fontFamily: "inherit", fontSize: ".88rem" };
  const box: React.CSSProperties = { background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 14, padding: 22, boxShadow: "0 4px 20px rgba(10,42,94,.06)" };

  return (
    <div style={{ padding: "40px 28px", maxWidth: 960 }}>
      <h1 style={{ fontSize: "1.7rem", margin: "0 0 20px" }}>Convocatorias</h1>

      <div style={{ ...box, marginBottom: 24 }}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Agregar nueva convocatoria</h2>
        <form action={crearConvocatoria} style={{ display: "grid", gap: 10, gridTemplateColumns: "1fr 1fr" }}>
          <input style={input} name="nombre" placeholder="Nombre *" required />
          <input style={input} name="entidad" placeholder="Entidad" />
          <select style={input} name="estado" defaultValue="proxima">
            <option value="abiertas">Inscripciones abiertas</option>
            <option value="proxima">Prueba próxima / pendiente</option>
            <option value="cerradas">Inscripciones cerradas</option>
          </select>
          <input style={input} name="etiqueta" placeholder="Etiqueta (ej. Prueba escrita pendiente)" />
          <input style={input} name="vacantes" placeholder="Vacantes (ej. 1.665)" />
          <input style={input} name="fecha_prueba_aprox" placeholder="Fecha de pruebas (texto)" />

          {/* Imagen — opción A: elegir una ya cargada */}
          <div>
            <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>IMAGEN — elegir una ya cargada</label>
            <select style={input} name="imagen_existente" defaultValue="">
              <option value="">— Selecciona una imagen existente —</option>
              {IMAGENES_DISPONIBLES.map((f) => (
                <option key={f} value={`/fotos/${f}`}>{f}</option>
              ))}
            </select>
          </div>
          {/* Imagen — opción B: subir una nueva */}
          <div>
            <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>IMAGEN — o subir una nueva</label>
            <input style={input} type="file" name="imagen_file" accept="image/*" />
          </div>
          {/* Imagen — opción C: pegar una URL */}
          <input style={{ ...input, gridColumn: "1/-1" }} name="imagen_url" placeholder="…o pega una URL de imagen (opcional, ej. /fotos/nacional.jpg)" />

          <select style={input} name="tema" defaultValue="nacional">
            <option value="nacional">Nacional</option>
            <option value="territorial">Territorial</option>
            <option value="impuestos">Impuestos</option>
            <option value="justicia">Justicia</option>
            <option value="salud">Salud</option>
          </select>
          <input style={input} type="number" name="orden" placeholder="Orden" />
          <p style={{ gridColumn: "1/-1", color: "var(--texto-suave)", fontSize: ".74rem", margin: 0 }}>
            💡 Puedes elegir una imagen ya cargada, subir una nueva, o pegar una URL. Si subes una, queda guardada en el sistema y disponible por su enlace.
          </p>
          <button className="btn btn-oro" style={{ gridColumn: "1/-1", padding: 12 }}>Agregar convocatoria</button>
        </form>
      </div>

      <h2 style={{ fontSize: "1.05rem", marginBottom: 14 }}>Existentes ({convs?.length || 0})</h2>
      {(!convs || convs.length === 0) ? (
        <p style={{ color: "var(--texto-suave)" }}>Aún no hay convocatorias.</p>
      ) : (
        <div style={{ display: "grid", gap: 12 }}>
          {convs.map((c: any) => (
            <div key={c.id} style={{ ...box, display: "flex", alignItems: "center", gap: 14 }}>
              {c.imagen_url && (
                <img src={c.imagen_url} alt="" style={{ width: 50, height: 50, borderRadius: 8, objectFit: "cover", flexShrink: 0 }} />
              )}
              <div style={{ flex: 1 }}>
                <strong>{c.nombre}</strong>
                {!c.activa && <span style={{ color: "#b00", fontSize: ".75rem", marginLeft: 8 }}>(inactiva)</span>}
                <div style={{ color: "var(--texto-suave)", fontSize: ".82rem" }}>{c.entidad} · {c.etiqueta || c.estado}</div>
              </div>
              <form action={toggleConvocatoria.bind(null, c.id, c.activa)}>
                <button style={{ background: "none", border: "1px solid var(--gris-borde)", borderRadius: 8, padding: "6px 12px", cursor: "pointer", fontFamily: "inherit", fontSize: ".82rem" }}>
                  {c.activa ? "Desactivar" : "Activar"}
                </button>
              </form>
              <form action={eliminarConvocatoria.bind(null, c.id)}>
                <button style={{ background: "none", border: "none", color: "#b00", cursor: "pointer", fontSize: ".82rem" }}>Eliminar</button>
              </form>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
