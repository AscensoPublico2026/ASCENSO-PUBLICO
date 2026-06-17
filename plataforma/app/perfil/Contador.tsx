"use client";

import { useEffect, useState } from "react";
import { waUrl, WA_MENSAJES } from "@/lib/contacto";

function pad(n: number) {
  return (n < 10 ? "0" : "") + n;
}

export default function Contador({ deadline }: { deadline: string }) {
  const target = new Date(deadline).getTime();
  const [diff, setDiff] = useState<number>(target - Date.now());

  useEffect(() => {
    const t = setInterval(() => setDiff(target - Date.now()), 1000);
    return () => clearInterval(t);
  }, [target]);

  if (diff <= 0) {
    return (
      <div style={{ background: "var(--verde-suave)", color: "var(--verde)", borderRadius: 12, padding: 16, fontWeight: 700 }}>
        ⏰ Tu ruta debería estar lista. Si aún no la ves, <a href={waUrl(WA_MENSAJES.soporte)} target="_blank" rel="noopener" style={{ color: "var(--verde)", fontWeight: 800, textDecoration: "underline" }}>escríbenos por WhatsApp</a> y la activamos.
      </div>
    );
  }

  const h = Math.floor(diff / 3600000);
  const m = Math.floor((diff % 3600000) / 60000);
  const s = Math.floor((diff % 60000) / 1000);
  const box: React.CSSProperties = { background: "var(--azul)", color: "#fff", borderRadius: 14, padding: "16px 12px", minWidth: 78, textAlign: "center" };

  return (
    <div>
      <div style={{ display: "flex", gap: 10, justifyContent: "center" }}>
        <div style={box}><div style={{ fontFamily: "'Source Serif 4',serif", fontSize: "2.2rem" }}>{pad(h)}</div><div style={{ fontSize: ".7rem", opacity: .7 }}>HORAS</div></div>
        <div style={box}><div style={{ fontFamily: "'Source Serif 4',serif", fontSize: "2.2rem" }}>{pad(m)}</div><div style={{ fontSize: ".7rem", opacity: .7 }}>MIN</div></div>
        <div style={box}><div style={{ fontFamily: "'Source Serif 4',serif", fontSize: "2.2rem" }}>{pad(s)}</div><div style={{ fontSize: ".7rem", opacity: .7 }}>SEG</div></div>
      </div>
    </div>
  );
}
