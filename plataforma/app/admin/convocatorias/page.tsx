import { createClient } from "@/lib/supabase/server";
import { crearConvocatoria, toggleConvocatoria, eliminarConvocatoria } from "./actions";

export const dynamic = "force-dynamic";

export default async function AdminConvocatorias() {
  const supabase = createClient();
  const { data: convs } = await supabase.from("convocatorias").select("*").order("orden");

  const input: React.CSSProperties = { width: "100%", padding: "10px 12px", borderRadius: 10, border: "1px solid var(--gris-borde)", fontFamily: "inherit", fontSize: ".88rem" };
  const box: React.CSSProperties = { background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 14, padding: 22, boxShadow: "0 4px 20px rgba(10,42,94,.06)" };

  return (
    <div style={{ padding: "40px 28px", maxWidth: 960 }}>
      <h1 style={{ fontSize: "1.7rem", margin: "0 0 20px" }}>Convocatorias</h1>

      {/* Formulario para agregar */}
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
          <input style={input} name="imagen_url" placeholder="URL de imagen (ej. /fotos/nacional.jpg)" />
          <select style={input} name="tema" defaultValue="nacional">
            <option value="nacional">Nacional</option>
            <option value="territorial">Territorial</option>
            <option value="impuestos">Impuestos</option>
            <option value="justicia">Justicia</option>
            <option value="salud">Salud</option>
          </select>
          <input style={input} type="number" name="orden" placeholder="Orden (posición)" />
          <div>{/* spacer */}</div>
          <button className="btn btn-oro" style={{ gridColumn: "1/-1", padding: 12 }}>Agregar convocatoria</button>
        </form>
      </div>

      {/* Listado existente */}
      <h2 style={{ fontSize: "1.05rem", marginBottom: 14 }}>Convocatorias existentes ({convs?.length || 0})</h2>
      {(!convs || convs.length === 0) ? (
        <p style={{ color: "var(--texto-suave)" }}>Aún no hay convocatorias.</p>
      ) : (
        <div style={{ display: "grid", gap: 12 }}>
          {convs.map((c: any) => (
            <div key={c.id} style={{ ...box, display: "flex", alignItems: "center", gap: 14 }}>
              {/* Thumbnail */}
              {c.imagen_url && (
                // eslint-disable-next-line @next/next/no-img-element
                <img src={c.imagen_url} alt="" style={{ width: 56, height: 56, borderRadius: 10, objectFit: "cover", flexShrink: 0 }} />
              )}
              <div style={{ flex: 1 }}>
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <strong>{c.nombre}</strong>
                  {!c.activa && <span style={{ background: "#fee", color: "#b00", fontSize: ".7rem", fontWeight: 700, padding: "2px 8px", borderRadius: 8 }}>INACTIVA</span>}
                  <span style={{ fontSize: ".72rem", color: "var(--texto-suave)", marginLeft: "auto" }}>Orden: {c.orden}</span>
                </div>
                <div style={{ color: "var(--texto-suave)", fontSize: ".82rem", marginTop: 2 }}>
                  {c.entidad} · {c.etiqueta || c.estado}{c.vacantes ? ` · ${c.vacantes} vacantes` : ""}
                </div>
              </div>
              <div style={{ display: "flex", gap: 8, flexShrink: 0 }}>
                <form action={toggleConvocatoria.bind(null, c.id, c.activa)}>
                  <button style={{ background: "none", border: "1px solid var(--gris-borde)", borderRadius: 8, padding: "6px 12px", cursor: "pointer", fontFamily: "inherit", fontSize: ".82rem" }}>
                    {c.activa ? "Desactivar" : "Activar"}
                  </button>
                </form>
                <form action={eliminarConvocatoria.bind(null, c.id)}>
                  <button style={{ background: "none", border: "none", color: "#b00", cursor: "pointer", fontSize: ".82rem", fontWeight: 700 }}>Eliminar</button>
                </form>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
