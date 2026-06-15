import Link from "next/link";
import { notFound } from "next/navigation";
import { requireAdmin } from "@/lib/auth";
import { createClient, createAdminClient } from "@/lib/supabase/server";
import { subirGuia, habilitarCurso, eliminarGuia } from "./actions";

export const dynamic = "force-dynamic";

export default async function AdminCursoDetalle({ params }: { params: { id: string } }) {
  await requireAdmin();
  const supabase = createClient();
  const { data: curso } = await supabase
    .from("cursos")
    .select("*, profiles(nombre,correo,celular), convocatorias(nombre)")
    .eq("id", params.id)
    .single();
  if (!curso) notFound();

  const admin = createAdminClient();
  let manualUrl: string | null = null;
  if (curso.manual_pdf_path) {
    const { data } = await admin.storage.from("manuales").createSignedUrl(curso.manual_pdf_path, 1800);
    manualUrl = data?.signedUrl ?? null;
  }

  const { data: guias } = await supabase.from("guias_curso").select("*").eq("curso_id", params.id).order("orden");

  const input: React.CSSProperties = { padding: "10px 12px", borderRadius: 10, border: "1px solid var(--gris-borde)", fontFamily: "inherit", fontSize: ".9rem" };
  const box: React.CSSProperties = { background: "#fff", border: "1px solid var(--gris-borde)", borderRadius: 14, padding: 22, boxShadow: "var(--sombra)", marginTop: 18 };

  return (
    <main style={{ maxWidth: 820, margin: "0 auto", padding: "40px 22px" }}>
      <Link href="/admin/cursos" style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>← Cursos</Link>
      <h1 style={{ fontSize: "1.6rem", margin: "12px 0 4px" }}>{curso.cargo_nombre || "Curso"} {curso.convocatorias?.nombre ? `— ${curso.convocatorias.nombre}` : ""}</h1>

      <div style={box}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 10 }}>Datos del cliente</h2>
        <p><strong>Nombre:</strong> {curso.profiles?.nombre || "-"}</p>
        <p><strong>Correo:</strong> {curso.profiles?.correo || "-"}</p>
        <p><strong>Celular:</strong> {curso.profiles?.celular || "-"}</p>
        <p><strong>OPEC:</strong> {curso.opec || "-"} · <strong>Nivel:</strong> {curso.nivel || "-"}</p>
        <p><strong>Estado:</strong> {curso.estado}</p>
        {manualUrl && <p style={{ marginTop: 8 }}><a href={manualUrl} target="_blank" rel="noopener" style={{ color: "var(--azul)", fontWeight: 700 }}>📄 Ver manual de funciones</a></p>}
        {curso.estado !== "listo" && (
          <form action={habilitarCurso.bind(null, curso.id)} style={{ marginTop: 14 }}>
            <button className="btn btn-oro" style={{ padding: "10px 20px" }}>✅ Habilitar acceso (marcar listo)</button>
          </form>
        )}
      </div>

      <div style={box}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 10 }}>Guías del curso</h2>
        {(!guias || guias.length === 0) ? <p style={{ color: "var(--texto-suave)" }}>Aún no hay guías.</p> : (
          <div style={{ display: "grid", gap: 8 }}>
            {guias.map((g: any) => (
              <div key={g.id} style={{ display: "flex", alignItems: "center", gap: 10, padding: "8px 0", borderBottom: "1px solid var(--gris-borde)" }}>
                <span style={{ fontWeight: 700 }}>{g.dia != null ? `D${g.dia} · ` : ""}{g.titulo}</span>
                <span style={{ color: "var(--texto-suave)", fontSize: ".8rem" }}>({g.tipo})</span>
                <form action={eliminarGuia.bind(null, curso.id, g.id)} style={{ marginLeft: "auto" }}>
                  <button style={{ background: "none", border: "none", color: "#b00", cursor: "pointer" }}>Eliminar</button>
                </form>
              </div>
            ))}
          </div>
        )}

        <h3 style={{ fontSize: ".95rem", margin: "18px 0 8px" }}>Subir nueva guía (HTML)</h3>
        <form action={subirGuia.bind(null, curso.id)} style={{ display: "grid", gap: 10, gridTemplateColumns: "1fr 1fr" }}>
          <input style={input} type="text" name="titulo" placeholder="Título de la guía" required />
          <input style={input} type="number" name="dia" placeholder="Día (ej. 1)" />
          <select style={input} name="tipo" defaultValue="general">
            <option value="general">General</option>
            <option value="nivel">Por nivel</option>
            <option value="funcional">Funcional</option>
            <option value="bonus">Bonus</option>
            <option value="simulacro">Simulacro</option>
          </select>
          <input style={input} type="number" name="orden" placeholder="Orden (ej. 1)" />
          <input style={{ ...input, gridColumn: "1/-1" }} type="file" name="archivo" accept=".html,text/html" required />
          <button className="btn btn-oro" style={{ gridColumn: "1/-1", padding: 12 }}>Subir guía</button>
        </form>
      </div>
    </main>
  );
}
