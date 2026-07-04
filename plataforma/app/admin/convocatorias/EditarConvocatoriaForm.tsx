"use client";

import { useState } from "react";
import { editarConvocatoria } from "./actions";

const IMAGENES_DISPONIBLES = [
  "nacional.jpg", "territorial12.jpg", "territorial-uapa.jpg",
  "dian.jpg", "procuraduria.jpg", "ese.jpg", "hero.jpg",
];

interface Convocatoria {
  id: string;
  nombre: string;
  entidad: string | null;
  estado: string;
  etiqueta: string | null;
  vacantes: string | null;
  fecha_prueba_aprox: string | null;
  imagen_url: string | null;
  tema: string | null;
  orden: number;
  activa: boolean;
}

export default function EditarConvocatoriaForm({ conv }: { conv: Convocatoria }) {
  const [abierto, setAbierto] = useState(false);

  const input: React.CSSProperties = {
    width: "100%", padding: "10px 12px", borderRadius: 10,
    border: "1px solid var(--gris-borde)", fontFamily: "inherit", fontSize: ".88rem",
  };

  if (!abierto) {
    return (
      <button
        onClick={() => setAbierto(true)}
        style={{
          background: "none", border: "1px solid var(--gris-borde)", borderRadius: 8,
          padding: "6px 12px", cursor: "pointer", fontFamily: "inherit", fontSize: ".82rem",
          color: "var(--azul)",
        }}
      >
        Editar
      </button>
    );
  }

  const editarConBind = editarConvocatoria.bind(null, conv.id);

  return (
    <div style={{ gridColumn: "1/-1", marginTop: 12, background: "#f8f6f1", border: "1px solid var(--gris-borde)", borderRadius: 12, padding: 18 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12 }}>
        <h3 style={{ fontSize: ".95rem", margin: 0, color: "var(--azul)" }}>Editar: {conv.nombre}</h3>
        <button
          onClick={() => setAbierto(false)}
          style={{ background: "none", border: "none", cursor: "pointer", fontSize: "1.1rem", color: "var(--texto-suave)" }}
        >
          ✕
        </button>
      </div>
      <form action={editarConBind} style={{ display: "grid", gap: 10, gridTemplateColumns: "1fr 1fr" }}>
        {/* Campo oculto para mantener la imagen actual */}
        <input type="hidden" name="imagen_actual" value={conv.imagen_url || ""} />

        <div>
          <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>Nombre *</label>
          <input style={input} name="nombre" defaultValue={conv.nombre} required />
        </div>
        <div>
          <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>Entidad</label>
          <input style={input} name="entidad" defaultValue={conv.entidad || ""} />
        </div>
        <div>
          <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>Estado</label>
          <select style={input} name="estado" defaultValue={conv.estado}>
            <option value="abiertas">Inscripciones abiertas</option>
            <option value="proxima">Prueba próxima / pendiente</option>
            <option value="cerradas">Inscripciones cerradas</option>
          </select>
        </div>
        <div>
          <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>Etiqueta</label>
          <input style={input} name="etiqueta" defaultValue={conv.etiqueta || ""} placeholder="Ej. Prueba escrita pendiente" />
        </div>
        <div>
          <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>Vacantes</label>
          <input style={input} name="vacantes" defaultValue={conv.vacantes || ""} placeholder="Ej. 1.665" />
        </div>
        <div>
          <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>Fecha de pruebas (texto)</label>
          <input style={input} name="fecha_prueba_aprox" defaultValue={conv.fecha_prueba_aprox || ""} placeholder="Ej. Agosto 2026" />
        </div>

        {/* Imagen actual */}
        {conv.imagen_url && (
          <div style={{ gridColumn: "1/-1", display: "flex", alignItems: "center", gap: 12, background: "#fff", borderRadius: 8, padding: "8px 12px", border: "1px solid var(--gris-borde)" }}>
            <img src={conv.imagen_url} alt="" style={{ width: 48, height: 48, borderRadius: 8, objectFit: "cover" }} />
            <span style={{ fontSize: ".8rem", color: "var(--texto-suave)" }}>Imagen actual: {conv.imagen_url}</span>
          </div>
        )}

        {/* Imagen — opción A: elegir una ya cargada */}
        <div>
          <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>IMAGEN — elegir una ya cargada</label>
          <select style={input} name="imagen_existente" defaultValue="">
            <option value="">— No cambiar / seleccionar —</option>
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
        <input style={{ ...input, gridColumn: "1/-1" }} name="imagen_url" placeholder="…o pega una URL de imagen (deja vacío para mantener la actual)" defaultValue="" />

        <div>
          <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>Tema (color tarjeta)</label>
          <select style={input} name="tema" defaultValue={conv.tema || "nacional"}>
            <option value="nacional">Nacional</option>
            <option value="territorial">Territorial</option>
            <option value="impuestos">Impuestos</option>
            <option value="justicia">Justicia</option>
            <option value="salud">Salud</option>
          </select>
        </div>
        <div>
          <label style={{ fontSize: ".7rem", color: "var(--texto-suave)" }}>Orden</label>
          <input style={input} type="number" name="orden" defaultValue={conv.orden || 0} />
        </div>

        <p style={{ gridColumn: "1/-1", color: "var(--texto-suave)", fontSize: ".74rem", margin: 0 }}>
          💡 Si no cambias la imagen, se mantiene la actual. Puedes elegir otra existente, subir una nueva, o pegar una URL.
        </p>

        <div style={{ gridColumn: "1/-1", display: "flex", gap: 10 }}>
          <button className="btn btn-oro" style={{ flex: 1, padding: 12 }}>Guardar cambios</button>
          <button
            type="button"
            onClick={() => setAbierto(false)}
            style={{ padding: "12px 20px", borderRadius: 10, border: "1px solid var(--gris-borde)", background: "#fff", cursor: "pointer", fontFamily: "inherit", fontSize: ".88rem" }}
          >
            Cancelar
          </button>
        </div>
      </form>
    </div>
  );
}
