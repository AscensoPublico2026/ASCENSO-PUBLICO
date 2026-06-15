import Link from "next/link";
import { requireAdmin } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { crearConvocatoria, toggleConvocatoria, eliminarConvocatoria } from "./actions";

export const dynamic = "force-dynamic";

export default async function AdminConvocatorias() {
  await requireAdmin();
  const supabase = createClient();
  const { data: convs } = await supabase.from("convocatorias").select("*").order("orden");

  const input: React.CSSProperties = { padding: "10px 12px", borderRadius: 10, border: "1px solid var(--gris-borde)", fontFamily: "inherit", fontSize: ".9rem" };
  const box: React.CSSProperties = { background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 14, padding: 22, boxShadow: "var(--sombra)" };

  return (
    <main style={{ maxWidth: 920, margin: "0 auto", padding: "40px 22px" }}>
      <Link href="/admin" style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>← Panel</Link>
      <h1 style={{ fontSize: "1.7rem", margin: "12px 0 20px" }}>Convocatorias</h1>

      <div style={{ ...box, marginBottom: 24 }}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Agregar convocatoria</h2>
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
          <select style={input} name="tema" defaultValue="nacional">
            <option value="nacional">Nacional</option>
            <option value="territorial">Territorial</option>
            <option value="impuestos">Impuestos</option>
            <option value="justicia">Justicia</option>
            <option value="salud">Salud</option>
          </select>
          <input style={input} type="number" name="orden" placeholder="Orden" />
          <button className="btn btn-oro" style={{ gridColumn: "1/-1", padding: 12 }}>Agregar</button>
        </form>
      </div>

      {(!convs || convs.length === 0) ? <p style={{ color: "var(--texto-suave)" }}>Aún no hay convocatorias.</p> : (
        <div style={{ display: "grid", gap: 12 }}>
          {convs.map((c: any) => (
            <div key={c.id} style={{ ...box, display: "flex", alignItems: "center", gap: 12 }}>
              <div style={{ flex: 1 }}>
                <strong>{c.nombre}</strong> {!c.activa && <span style={{ color: "#b00", fontSize: ".8rem" }}>(inactiva)</span>}
                <div style={{ color: "var(--texto-suave)", fontSize: ".85rem" }}>{c.entidad} · {c.etiqueta || c.estado}{c.vacantes ? ` · ${c.vacantes} vacantes` : ""}</div>
              </div>
              <form action={toggleConvocatoria.bind(null, c.id, c.activa)}>
                <button style={{ background: "none", border: "1px solid var(--gris-borde)", borderRadius: 8, padding: "6px 12px", cursor: "pointer", fontFamily: "inherit" }}>{c.activa ? "Desactivar" : "Activar"}</button>
              </form>
              <form action={eliminarConvocatoria.bind(null, c.id)}>
                <button style={{ background: "none", border: "none", color: "#b00", cursor: "pointer" }}>Eliminar</button>
              </form>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}
