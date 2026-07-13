"use client";

import { useEffect, useState } from "react";

/**
 * Barra de tiempo para el PANEL ADMIN.
 * Muestra cuánto tiempo lleva corriendo (y cuánto falta) el plazo de 24h de
 * preparación de un curso, con una barra que se va VACIANDO a medida que pasa
 * el tiempo (igual concepto que el contador que ve el cliente en /perfil,
 * pero pensado para que el admin controle sus tiempos de entrega).
 *
 * Props:
 * - fechaCompra: ISO string de cuándo se compró el curso (inicio del plazo).
 * - deadline: ISO string del preparacion_deadline (fechaCompra + 24h).
 * - listo: si el curso ya está en estado "listo" (deja de tener sentido el plazo).
 */
export default function BarraTiempoAdmin({
  fechaCompra,
  deadline,
  listo,
  compact = false,
}: {
  fechaCompra: string | null;
  deadline: string | null;
  listo: boolean;
  compact?: boolean;
}) {
  const inicio = fechaCompra ? new Date(fechaCompra).getTime() : null;
  const fin = deadline ? new Date(deadline).getTime() : null;
  const [ahora, setAhora] = useState(Date.now());

  useEffect(() => {
    if (listo) return; // no hace falta seguir el reloj si ya está listo
    const t = setInterval(() => setAhora(Date.now()), 1000);
    return () => clearInterval(t);
  }, [listo]);

  if (!inicio || !fin) {
    return (
      <span style={{ fontSize: ".78rem", color: "var(--texto-suave)" }}>Sin fecha de compra</span>
    );
  }

  const totalMs = fin - inicio;
  const transcurridoMs = Math.min(totalMs, Math.max(0, ahora - inicio));
  const restanteMs = Math.max(0, fin - ahora);
  const pctTranscurrido = totalMs > 0 ? Math.min(100, Math.round((transcurridoMs / totalMs) * 100)) : 100;
  const vencido = restanteMs <= 0;

  const h = Math.floor(restanteMs / 3600000);
  const m = Math.floor((restanteMs % 3600000) / 60000);
  const s = Math.floor((restanteMs % 60000) / 1000);
  const textoRestante = vencido ? "Plazo cumplido" : h > 0 ? `${h}h ${m}m restantes` : `${m}m ${s}s restantes`;

  // Color según urgencia: verde si queda mucho, oro si va quedando poco, rojo si se venció.
  let color = "#1A7A4A"; // verde
  if (!listo) {
    if (vencido) color = "#B00020";
    else if (pctTranscurrido >= 75) color = "#E8A33D";
  } else {
    color = "#1A7A4A";
  }

  if (listo) {
    return (
      <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
        <span style={{ fontSize: ".78rem", fontWeight: 700, color: "#1A7A4A" }}>✅ Curso listo</span>
      </div>
    );
  }

  return (
    <div style={{ minWidth: compact ? 120 : 180 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: 4 }}>
        <span style={{ fontSize: ".72rem", fontWeight: 700, color }}>
          {vencido ? "⏰" : "⏳"} {textoRestante}
        </span>
        {!compact && (
          <span style={{ fontSize: ".68rem", color: "var(--texto-suave)" }}>{pctTranscurrido}% del plazo</span>
        )}
      </div>
      <div style={{
        height: compact ? 6 : 8,
        borderRadius: 4,
        background: "#EDEAE2",
        overflow: "hidden",
        border: "1px solid var(--gris-borde)",
      }}>
        <div style={{
          height: "100%",
          width: `${pctTranscurrido}%`,
          background: vencido
            ? "linear-gradient(90deg, #D0334A, #B00020)"
            : "linear-gradient(90deg, #0A2A5E, #1A4A8A)",
          borderRadius: 4,
          transition: "width 1s linear",
        }} />
      </div>
    </div>
  );
}
