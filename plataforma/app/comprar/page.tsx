import { crearCompra } from "./actions";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

export default async function ComprarPage({ searchParams }: { searchParams: { conv?: string } }) {
  let convocatorias: { id: string; nombre: string }[] = [];
  try {
    const supabase = createClient();
    const { data } = await supabase.from("convocatorias").select("id,nombre").eq("activa", true).order("orden");
    convocatorias = data || [];
  } catch {
    convocatorias = [];
  }

  const inputStyle: React.CSSProperties = {
    width: "100%", padding: "12px 14px", borderRadius: 12, border: "1px solid var(--gris-borde)",
    fontFamily: "inherit", fontSize: ".95rem", marginTop: 6, background: "#fff",
  };
  const label: React.CSSProperties = { fontWeight: 700, fontSize: ".9rem", color: "var(--azul)", display: "block", marginTop: 16 };

  return (
    <main style={{ maxWidth: 620, margin: "0 auto", padding: "48px 22px" }}>
      <h1 style={{ fontSize: "1.9rem", marginBottom: 6 }}>Adquiere tu curso personalizado</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 8 }}>
        Completa tus datos y sube tu manual de funciones. Después realizas el pago seguro con Wompi.
      </p>
      <p style={{ color: "var(--azul)", fontWeight: 800, marginBottom: 24 }}>Precio: $300.000 COP · pago único</p>

      <form action={crearCompra}>
        <label style={label}>Nombre completo *
          <input style={inputStyle} type="text" name="nombre" required />
        </label>
        <label style={label}>Correo *
          <input style={inputStyle} type="email" name="correo" required />
        </label>
        <label style={label}>Celular (WhatsApp)
          <input style={inputStyle} type="tel" name="celular" />
        </label>
        <label style={label}>Convocatoria
          <select style={inputStyle} name="convocatoria_id" defaultValue={searchParams?.conv || ""}>
            <option value="">Selecciona tu convocatoria</option>
            {convocatorias.map((c) => (<option key={c.id} value={c.id}>{c.nombre}</option>))}
          </select>
        </label>
        <label style={label}>Número de OPEC
          <input style={inputStyle} type="text" name="opec" />
        </label>
        <label style={label}>Nombre del cargo
          <input style={inputStyle} type="text" name="cargo" />
        </label>
        <label style={label}>Nivel del cargo
          <select style={inputStyle} name="nivel" defaultValue="">
            <option value="">Selecciona</option>
            <option value="asistencial">Asistencial</option>
            <option value="tecnico">Técnico</option>
            <option value="profesional">Profesional</option>
          </select>
        </label>
        <label style={label}>Manual de funciones (PDF) *
          <input style={inputStyle} type="file" name="manual" accept=".pdf,application/pdf" required />
        </label>

        <label style={{ display: "flex", gap: 10, alignItems: "flex-start", marginTop: 20, fontSize: ".88rem", color: "var(--texto-suave)" }}>
          <input type="checkbox" name="consentimiento" required style={{ marginTop: 3 }} />
          <span>Autorizo el tratamiento de mis datos personales conforme a la Ley 1581 de 2012 y la <a href="/privacidad" style={{ color: "var(--azul)", textDecoration: "underline" }}>política de privacidad</a>.</span>
        </label>

        <button type="submit" className="btn btn-oro" style={{ width: "100%", padding: 15, marginTop: 24 }}>
          Continuar al pago seguro →
        </button>
        <p style={{ fontSize: ".8rem", color: "var(--texto-suave)", textAlign: "center", marginTop: 12 }}>
          Pago seguro con Wompi · PSE, Nequi y tarjetas
        </p>
      </form>
    </main>
  );
}
