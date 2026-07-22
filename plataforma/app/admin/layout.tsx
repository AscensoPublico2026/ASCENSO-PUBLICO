import Link from "next/link";
import { requireAdmin } from "@/lib/auth";

export default async function AdminLayout({ children }: { children: React.ReactNode }) {
  await requireAdmin();

  return (
    <div style={{ display: "flex", minHeight: "100vh" }}>
      {/* Sidebar */}
      <aside style={{
        width: 240,
        background: "var(--azul, #0A2A5E)",
        color: "#fff",
        padding: "24px 0",
        flexShrink: 0,
        display: "flex",
        flexDirection: "column",
      }}>
        <div style={{ padding: "0 20px", marginBottom: 28 }}>
          <Link href="/admin" style={{ display: "flex", alignItems: "center", gap: 10, color: "#fff" }}>
            <span style={{
              width: 34, height: 34, borderRadius: 9,
              background: "linear-gradient(135deg, #F6C56B, #E8A33D)",
              display: "flex", alignItems: "center", justifyContent: "center",
            }}>
              <svg viewBox="0 0 100 100" width={18} height={18}>
                <circle cx="26" cy="74" r="3.4" fill="#0A2A5E" opacity={0.45}/>
                <circle cx="34" cy="70" r="4.2" fill="#0A2A5E" opacity={0.72}/>
                <path d="M36 66 C48 62 58 54 72 34" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round"/>
                <path d="M61 32 L75 30 L73 45" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </span>
            <span style={{ fontWeight: 800, fontSize: ".95rem" }}>Admin</span>
          </Link>
        </div>

        <nav style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          <NavItem href="/admin" icon="📊" label="Dashboard" />
          <NavItem href="/admin/analitica" icon="📈" label="Analítica" />
          <NavItem href="/admin/cursos" icon="🎓" label="Cursos / Clientes" />
          <NavItem href="/admin/convocatorias" icon="📋" label="Convocatorias" />
          <NavItem href="/admin/usuarios" icon="👥" label="Usuarios" />
        </nav>

        <div style={{ marginTop: "auto", padding: "20px" }}>
          <Link href="/perfil" style={{ color: "rgba(255,255,255,.6)", fontSize: ".82rem" }}>← Volver al perfil</Link>
          <br />
          <Link href="/" style={{ color: "rgba(255,255,255,.6)", fontSize: ".82rem" }}>← Ir a la landing</Link>
        </div>
      </aside>

      {/* Contenido principal */}
      <div style={{ flex: 1, background: "var(--crema, #FBF9F4)", minHeight: "100vh", overflow: "auto" }}>
        {children}
      </div>
    </div>
  );
}

function NavItem({ href, icon, label }: { href: string; icon: string; label: string }) {
  return (
    <Link
      href={href}
      style={{
        display: "flex",
        alignItems: "center",
        gap: 10,
        padding: "11px 20px",
        color: "rgba(255,255,255,.85)",
        fontSize: ".9rem",
        fontWeight: 600,
      }}
    >
      <span>{icon}</span>
      <span>{label}</span>
    </Link>
  );
}
