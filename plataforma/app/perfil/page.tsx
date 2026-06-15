import Link from "next/link";
import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import Contador from "./Contador";
import LogoutButton from "./LogoutButton";

export const dynamic = "force-dynamic";

export default async function PerfilPage() {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  const { data: cursos } = await supabase
    .from("cursos")
    .select("*, convocatorias(nombre)")
    .eq("usuario_id", user.id)
    .order("created_at", { ascending: false });

  const curso: any = cursos?.[0];
  const nombre = (user.user_metadata as any)?.nombre || user.email;

  return (
    <main style={{ maxWidth: 760, margin: "0 auto", padding: "40px 22px" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 28 }}>
        <div>
          <div style={{ color: "var(--texto-suave)", fontSize: ".85rem" }}>Hola,</div>
          <strong style={{ color: "var(--azul)", fontSize: "1.1rem" }}>{nombre}</strong>
        </div>
        <LogoutButton />
      </div>

      {!curso ? (
        <div style={{ border: "1.5px dashed var(--gris-borde)", borderRadius: 14, padding: 30, textAlign: "center", color: "var(--texto-suave)" }}>
          Aún no encontramos un curso asociado a tu cuenta. Si ya pagaste, escríbenos por WhatsApp.
        </div>
      ) : (
        <div style={{ background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 18, padding: 30, boxShadow: "var(--sombra)" }}>
          <div style={{ color: "var(--texto-suave)", fontSize: ".85rem" }}>Tu curso</div>
          <h1 style={{ fontSize: "1.5rem", margin: "4px 0 4px" }}>
            {curso.cargo_nombre || "Curso personalizado"}{curso.convocatorias?.nombre ? ` — ${curso.convocatorias.nombre}` : ""}
          </h1>

          {curso.estado === "en_preparacion" && (
            <div style={{ marginTop: 18 }}>
              <span style={{ display: "inline-block", background: "var(--oro-suave,#FDF4E3)", color: "#B8600A", fontWeight: 800, fontSize: ".78rem", padding: "5px 12px", borderRadius: 20, textTransform: "uppercase" }}>Curso en preparación</span>
              <p style={{ color: "var(--texto-suave)", margin: "16px 0" }}>Estamos armando tu ruta personalizada. Estará lista en máximo:</p>
              {curso.preparacion_deadline && <Contador deadline={curso.preparacion_deadline} />}
            </div>
          )}

          {curso.estado === "listo" && (
            <div style={{ marginTop: 18 }}>
              <span style={{ display: "inline-block", background: "var(--verde-suave)", color: "var(--verde)", fontWeight: 800, fontSize: ".78rem", padding: "5px 12px", borderRadius: 20, textTransform: "uppercase" }}>Curso listo</span>
              <h2 style={{ fontSize: "1.1rem", margin: "18px 0 10px" }}>Tu biblioteca</h2>
              <Guias cursoId={curso.id} />
            </div>
          )}

          {curso.fecha_vencimiento && (
            <p style={{ color: "var(--texto-suave)", fontSize: ".8rem", marginTop: 20 }}>
              Acceso válido hasta {new Date(curso.fecha_vencimiento).toLocaleDateString("es-CO")}.
            </p>
          )}
        </div>
      )}
    </main>
  );
}

async function Guias({ cursoId }: { cursoId: string }) {
  const supabase = createClient();
  const { data: guias } = await supabase
    .from("guias_curso")
    .select("*")
    .eq("curso_id", cursoId)
    .order("orden", { ascending: true });

  if (!guias || guias.length === 0) {
    return <p style={{ color: "var(--texto-suave)" }}>Pronto verás aquí tus guías por día.</p>;
  }

  return (
    <div style={{ display: "grid", gap: 10 }}>
      {guias.map((g: any) => (
        <Link key={g.id} href={`/guia/${g.id}`} style={{ display: "flex", alignItems: "center", gap: 12, background: "var(--crema)", border: "1px solid var(--gris-borde)", borderRadius: 12, padding: "12px 16px" }}>
          {g.dia != null && <span style={{ width: 34, height: 34, borderRadius: 8, background: "var(--azul)", color: "#fff", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 800, fontSize: ".8rem" }}>D{g.dia}</span>}
          <span style={{ fontWeight: 600 }}>{g.titulo}</span>
        </Link>
      ))}
    </div>
  );
}
