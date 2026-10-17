"use client";

import { useEffect, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { marcarGuiaTerminada } from "./actions";

/**
 * Botón "✓ Terminé esta guía" (cursos con desbloqueo secuencial).
 * Se activa tras `minutos` con la guía abierta; al pulsarlo guarda el avance
 * y lleva a la siguiente guía, que queda desbloqueada.
 */
export default function BotonTerminar({ guiaId, cursoId, yaTerminada, minutos }: {
  guiaId: string; cursoId: string; yaTerminada: boolean; minutos: number;
}) {
  const router = useRouter();
  const [restante, setRestante] = useState(yaTerminada ? 0 : minutos * 60);
  const [hecha, setHecha] = useState(yaTerminada);
  const [siguienteId, setSiguienteId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [pendiente, startTransition] = useTransition();

  function terminar() {
    setError(null);
    startTransition(async () => {
      const r = await marcarGuiaTerminada(guiaId);
      if (!r.ok) { setError(r.error || "No se pudo guardar."); return; }
      setSiguienteId(r.siguienteId ?? null);
      setHecha(true);
    });
  }

  // El botón "✅ Finalizar Día N" al final de cada guía avisa con postMessage
  // (GUIA_COMPLETADA): llegar al final y confirmar también la marca como terminada.
  useEffect(() => {
    if (hecha) return;
    const onMsg = (e: MessageEvent) => {
      if (e.origin !== window.location.origin) return;
      if (e.data && e.data.type === "GUIA_COMPLETADA") terminar();
    };
    window.addEventListener("message", onMsg);
    return () => window.removeEventListener("message", onMsg);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [hecha]);

  useEffect(() => {
    if (hecha || restante <= 0) return;
    const t = setInterval(() => setRestante((s) => Math.max(0, s - 1)), 1000);
    return () => clearInterval(t);
  }, [hecha, restante]);

  const base: React.CSSProperties = {
    border: "none", borderRadius: 20, padding: "8px 14px", fontWeight: 800,
    fontSize: ".8rem", whiteSpace: "nowrap", fontFamily: "inherit",
  };

  if (hecha) {
    return (
      <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
        <span style={{ color: "var(--verde)", fontWeight: 800, fontSize: ".8rem", whiteSpace: "nowrap" }}>✓ Terminada</span>
        <button
          style={{ ...base, cursor: "pointer", color: "#fff", background: "linear-gradient(135deg, #0A2A5E, #1A4A8A)" }}
          onClick={() => router.push(siguienteId ? `/guia/${siguienteId}` : `/perfil/${cursoId}`)}
        >
          {siguienteId ? "Siguiente guía →" : "Volver a mi curso"}
        </button>
      </div>
    );
  }

  const listo = restante <= 0;
  const mm = Math.floor(restante / 60), ss = String(restante % 60).padStart(2, "0");
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "flex-end", gap: 3 }}>
      <button
        disabled={!listo || pendiente}
        title={listo ? "Marca la guía como terminada para desbloquear la siguiente" : "Estudia la guía completa antes de marcarla"}
        style={{
          ...base,
          cursor: listo && !pendiente ? "pointer" : "not-allowed",
          color: listo ? "#0A2A5E" : "var(--texto-suave)",
          background: listo ? "linear-gradient(135deg, #E8A33D, #F6C56B)" : "var(--gris-borde)",
        }}
        onClick={terminar}
      >
        {pendiente ? "Guardando…" : listo ? "✓ Terminé esta guía" : `✓ Terminé (en ${mm}:${ss})`}
      </button>
      {error && <span style={{ color: "#B42318", fontSize: ".72rem" }}>{error}</span>}
    </div>
  );
}
