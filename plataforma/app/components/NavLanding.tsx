"use client";

import { useState } from "react";
import Link from "next/link";

export default function NavLanding() {
  const [open, setOpen] = useState(false);

  return (
    <header className="nav">
      <div className="nav-in">
        <Link href="/" className="brand" aria-label="Ascenso Público - inicio">
          <span className="brand-logo">
            <svg viewBox="0 0 100 100" width={26} height={26} aria-hidden="true">
              <circle cx="26" cy="74" r="3.4" fill="#0A2A5E" opacity={0.45}/>
              <circle cx="34" cy="70" r="4.2" fill="#0A2A5E" opacity={0.72}/>
              <path d="M36 66 C48 62 58 54 72 34" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round"/>
              <path d="M61 32 L75 30 L73 45" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </span>
          <span>
            <span className="brand-name">Ascenso Público</span><br/>
            <span className="brand-slogan">Tu ruta hacia el empleo público</span>
          </span>
        </Link>

        <nav className="nav-links">
          <Link href="/#problema">El problema</Link>
          <Link href="/#como">Cómo funciona</Link>
          <Link href="/buscador-opec" className="nav-destacado nav-opec">Buscador OPEC <span>NUEVO</span></Link>
          <Link href="/#simulacro">Simulacro gratis</Link>
          <Link href="/#incluye">Qué incluye</Link>
          <Link href="/#convocatorias">Convocatorias</Link>
          <Link href="/#precio">Precio</Link>
          <Link href="/login" className="btn btn-azul nav-cta desktop">Iniciar sesión</Link>
          <Link href="/comprar" className="btn btn-oro nav-cta desktop">Quiero mi curso</Link>
        </nav>

        <button
          className="nav-toggle"
          aria-label={open ? "Cerrar menú" : "Abrir menú"}
          aria-expanded={open}
          onClick={() => setOpen(!open)}
        >
          <span/><span/><span/>
        </button>
      </div>

      {open && (
        <nav className="mobile-menu open" aria-label="Menú de navegación móvil">
          <Link href="/#problema" onClick={() => setOpen(false)}>El problema</Link>
          <Link href="/#como" onClick={() => setOpen(false)}>Cómo funciona</Link>
          <Link href="/buscador-opec" className="nav-destacado nav-opec" onClick={() => setOpen(false)}>Buscador OPEC <span>NUEVO</span></Link>
          <Link href="/#simulacro" onClick={() => setOpen(false)}>Simulacro gratis</Link>
          <Link href="/#incluye" onClick={() => setOpen(false)}>Qué incluye</Link>
          <Link href="/#convocatorias" onClick={() => setOpen(false)}>Convocatorias</Link>
          <Link href="/#precio" onClick={() => setOpen(false)}>Precio</Link>
          <Link href="/login" onClick={() => setOpen(false)} style={{ color: "var(--azul)", fontWeight: 800 }}>Iniciar sesión</Link>
          <Link href="/comprar" onClick={() => setOpen(false)} style={{ color: "var(--oro)", fontWeight: 800 }}>Comprar mi curso</Link>
        </nav>
      )}
    </header>
  );
}
