import Link from "next/link";

export const metadata = {
  title: "Página no encontrada",
};

export default function NotFound() {
  return (
    <main style={{
      minHeight: "80vh",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      textAlign: "center",
      padding: "60px 22px",
      maxWidth: 560,
      margin: "0 auto",
    }}>
      {/* Logo */}
      <span style={{
        width: 64, height: 64, borderRadius: 16,
        background: "linear-gradient(135deg, #F6C56B, #E8A33D)",
        display: "flex", alignItems: "center", justifyContent: "center",
        boxShadow: "0 8px 20px rgba(232,163,61,.4)",
        marginBottom: 24,
      }}>
        <svg viewBox="0 0 100 100" width={34} height={34} aria-hidden="true">
          <circle cx="26" cy="74" r="3.4" fill="#0A2A5E" opacity={0.45}/>
          <circle cx="34" cy="70" r="4.2" fill="#0A2A5E" opacity={0.72}/>
          <path d="M36 66 C48 62 58 54 72 34" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round"/>
          <path d="M61 32 L75 30 L73 45" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
      </span>

      <div style={{ fontFamily: "'Source Serif 4', serif", fontSize: "4rem", fontWeight: 700, color: "var(--azul, #0A2A5E)", lineHeight: 1 }}>
        404
      </div>
      <h1 style={{ fontSize: "1.4rem", margin: "12px 0 8px", color: "var(--azul, #0A2A5E)" }}>
        Página no encontrada
      </h1>
      <p style={{ color: "var(--texto-suave, #5B6675)", marginBottom: 28, lineHeight: 1.6 }}>
        La página que buscas no existe o fue movida. Verifica el enlace o vuelve al inicio.
      </p>

      <div style={{ display: "flex", gap: 12, flexWrap: "wrap", justifyContent: "center" }}>
        <Link href="/" className="btn btn-oro" style={{ padding: "12px 24px" }}>
          Ir al inicio
        </Link>
        <Link href="/perfil" className="btn" style={{ padding: "12px 24px", background: "#fff", border: "1px solid var(--gris-borde, #E6E2D8)", color: "var(--azul, #0A2A5E)", fontWeight: 700, borderRadius: 12 }}>
          Mi perfil
        </Link>
      </div>

      <p style={{ color: "var(--texto-suave, #5B6675)", fontSize: ".84rem", marginTop: 28 }}>
        ¿Necesitas ayuda? <a href="https://wa.me/573151972091" target="_blank" rel="noopener" style={{ color: "var(--azul, #0A2A5E)", fontWeight: 700 }}>Escríbenos por WhatsApp</a>
      </p>
    </main>
  );
}
