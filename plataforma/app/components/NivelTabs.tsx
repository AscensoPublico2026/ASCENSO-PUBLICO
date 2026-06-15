"use client";

import { useState } from "react";

const RUTAS: Record<string, { titulo: string; dias: [string, string][] }> = {
  asistencial: {
    titulo: "Ruta nivel Asistencial",
    dias: [
      ["D1", "Estado, función pública y atención al ciudadano"],
      ["D5", "Competencias comportamentales del nivel asistencial"],
      ["D9", "Funciones de apoyo y manejo documental de tu cargo"],
      ["D14", "Simulacro situacional: atención y colaboración"],
      ["D21", "Simulacro integral final enfocado en tu OPEC"],
    ],
  },
  tecnico: {
    titulo: "Ruta nivel Técnico",
    dias: [
      ["D1", "Estado, función pública y marco institucional"],
      ["D5", "Competencias del nivel técnico"],
      ["D9", "Funciones técnicas reales de tu empleo"],
      ["D14", "Simulacro situacional: desempeño y trabajo colaborativo"],
      ["D21", "Simulacro integral final enfocado en tu OPEC"],
    ],
  },
  profesional: {
    titulo: "Ruta nivel Profesional",
    dias: [
      ["D1", "Estado, función pública y relación con el ciudadano"],
      ["D5", "Competencias del nivel profesional"],
      ["D9", "Alcance y funciones del cargo profesional"],
      ["D14", "Simulacro situacional: gestión y cumplimiento"],
      ["D21", "Simulacro integral final enfocado en tu OPEC"],
    ],
  },
};

export default function NivelTabs() {
  const [nivel, setNivel] = useState("asistencial");
  const ruta = RUTAS[nivel];

  return (
    <div>
      <div className="nivel-tabs" role="tablist" aria-label="Nivel del cargo">
        {(["asistencial", "tecnico", "profesional"] as const).map((n) => (
          <button
            key={n}
            className={`nivel-tab${nivel === n ? " active" : ""}`}
            role="tab"
            aria-selected={nivel === n}
            onClick={() => setNivel(n)}
          >
            {n.charAt(0).toUpperCase() + n.slice(1)}
          </button>
        ))}
      </div>
      <div className="ruta-card">
        <div className="rc-head">{ruta.titulo}</div>
        <div className="rc-sub">Plan personalizado · 21 días</div>
        {ruta.dias.map(([dia, desc]) => (
          <div className="mk-row" key={dia}>
            <span className="mk-day">{dia}</span>
            <p>{desc}</p>
          </div>
        ))}
      </div>
      <p className="ruta-ejemplo" style={{ marginTop: 14 }}>
        Ejemplo ilustrativo · tu ruta real se arma con tu OPEC y tu manual de funciones
      </p>
    </div>
  );
}
