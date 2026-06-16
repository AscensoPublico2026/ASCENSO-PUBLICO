"use client";

import { useEffect } from "react";

/**
 * Anima los elementos de la landing al entrar al viewport (fade-in + slide-up).
 * No requiere editar el JSX: selecciona automáticamente los bloques animables
 * y les aplica la animación con un leve escalonado (stagger).
 */
export default function ScrollReveal() {
  useEffect(() => {
    // Respeta accesibilidad
    const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReduced) return;

    // Selectores de bloques que se animan al aparecer
    const selectores = [
      ".sec .eyebrow",
      ".sec > .wrap > h2",
      ".sec > .wrap > .lead",
      ".card",
      ".feat",
      ".paso",
      ".stat",
      ".conv",
      ".precio-card",
      ".founder",
      ".sol > div",
      ".lead-cap",
      ".nivel-tabs",
      ".ruta-card",
    ];

    const elementos = Array.from(
      document.querySelectorAll<HTMLElement>(selectores.join(","))
    );

    // Estado inicial (oculto)
    elementos.forEach((el) => el.classList.add("reveal-init"));

    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry, i) => {
          if (entry.isIntersecting) {
            const el = entry.target as HTMLElement;
            // Pequeño escalonado para grupos de tarjetas
            const delay = Math.min(i * 60, 240);
            setTimeout(() => el.classList.add("reveal-in"), delay);
            io.unobserve(el);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    elementos.forEach((el) => io.observe(el));

    return () => io.disconnect();
  }, []);

  return null;
}
