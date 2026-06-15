export default function Home() {
  return (
    <main style={{ maxWidth: 760, margin: "0 auto", padding: "90px 22px", textAlign: "center" }}>
      <h1 style={{ fontSize: "2.2rem", marginBottom: 12 }}>Ascenso Público — Plataforma</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 8 }}>
        Preparación personalizada para concursos de la CNSC.
      </p>
      <p style={{ color: "var(--texto-suave)", marginBottom: 28 }}>
        🚧 Plataforma en construcción: compra + perfil del estudiante + panel de administración.
      </p>
      <a className="btn btn-oro" href="/comprar">Quiero mi curso</a>
      <p style={{ color: "var(--texto-suave)", fontSize: ".85rem", marginTop: 30 }}>
        Configuración y despliegue: ver <code>SETUP.md</code>.
      </p>
    </main>
  );
}
