"use client";

import { useEffect, useState } from "react";

/**
 * Contador compacto para la TARJETA del curso en /perfil.
 * Muestra el tiempo restante hasta que el curso quede disponible (deadline 12h).
 * No contiene enlaces (es seguro dentro de un <Link>/<a>).
 */
export default function ContadorMini({ deadline }: { deadline: string }) {
  const target = new Date(deadline).getTime();
  const [diff, setDiff] = useState<number>(target - Date.now());

  useEffect(() => {
    const t = setInterval(() => setDiff(target - Date.now()), 1000);
    return () => clearInterval(t);
  }, [target]);

  const pill: React.CSSProperties = {
    display: "inline-flex", alignItems: "center", gap: 6,
    background: "rgba(255,255,255,.16)", color: "#fff",
    fontSize: ".74rem", fontWeight: 800, padding: "5px 11px", borderRadius: 14,
    border: "1px solid rgba(255,255,255,.25)", whiteSpace: "nowrap",
  };

  if (diff <= 0) {
    return <span style={pill}>⏰ Disponible muy pronto</span>;
  }

  const h = Math.floor(diff / 3600000);
  const m = Math.floor((diff % 3600000) / 60000);
  const s = Math.floor((diff % 60000) / 1000);
  const texto = h > 0 ? `${h}h ${m}m` : `${m}m ${s}s`;

  return <span style={pill}>⏳ Disponible en {texto}</span>;
}
