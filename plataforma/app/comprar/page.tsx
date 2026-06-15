import { crearCompra } from "./actions";
import { createClient } from "@/lib/supabase/server";
import Link from "next/link";
import ContadorCupos from "../components/ContadorCupos";

export const dynamic = "force-dynamic";

const CUPOS_LANZAMIENTO = 100;

export default async function ComprarPage({ searchParams }: { searchParams: { conv?: string } }) {
  let convocatorias: { id: string; nombre: string }[] = [];
  let cursosVendidos = 0;
  try {
    const supabase = createClient();
    const { data } = await supabase.from("convocatorias").select("id,nombre").eq("activa", true).order("orden");
    convocatorias = data || [];
    const { count } = await supabase.from("pagos").select("*", { count: "exact", head: true }).eq("estado", "aprobado");
    cursosVendidos = count || 0;
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
      <Link href="/" style={{ color: "var(--texto-suave)", fontSize: ".88rem" }}>← Volver al inicio</Link>

      <h1 style={{ fontSize: "1.9rem", marginBottom: 6, marginTop: 16 }}>Adquiere tu curso personalizado</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 8 }}>
        Completa tus datos y sube tu manual de funciones. Después realizas el pago seguro con Wompi.
      </p>
      <p style={{ color: "var(--azul)", fontWeight: 800, marginBottom: 24 }}>Precio: $300.000 COP · pago único</p>

      <ContadorCupos vendidos={cursosVendidos} total={CUPOS_LANZAMIENTO} />

      <form action={crearCompra}>
        {/* Nombres y Apellidos separados - OBLIGATORIOS */}
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14 }}>
          <label style={label}>Nombres *
            <input style={inputStyle} type="text" name="nombres" required placeholder="Ej: Julio César" />
          </label>
          <label style={label}>Apellidos *
            <input style={inputStyle} type="text" name="apellidos" required placeholder="Ej: Deávila Pérez" />
          </label>
        </div>

        <label style={label}>Correo *
          <input style={inputStyle} type="email" name="correo" required placeholder="tucorreo@ejemplo.com" />
        </label>
        <label style={label}>Celular (WhatsApp)
          <input style={inputStyle} type="tel" name="celular" placeholder="Ej: 315 197 2091" />
        </label>
        <label style={label}>Convocatoria *
          <select style={inputStyle} name="convocatoria_id" defaultValue={searchParams?.conv || ""} required>
            <option value="">Selecciona tu convocatoria</option>
            {convocatorias.map((c) => (<option key={c.id} value={c.id}>{c.nombre}</option>))}
          </select>
        </label>
        <label style={label}>Número de OPEC *
          <input style={inputStyle} type="text" name="opec" required placeholder="Ej: 48521" />
        </label>
        <label style={label}>Nombre del cargo *
          <input style={inputStyle} type="text" name="cargo" required placeholder="Ej: Técnico Administrativo" />
        </label>
        <label style={label}>Nivel del cargo *
          <select style={inputStyle} name="nivel" defaultValue="" required>
            <option value="" disabled>Selecciona</option>
            <option value="asistencial">Asistencial</option>
            <option value="tecnico">Técnico</option>
            <option value="profesional">Profesional</option>
          </select>
        </label>
        <label style={label}>Manual de funciones (PDF) *
          <input style={inputStyle} type="file" name="manual" accept=".pdf,application/pdf" required />
          <span style={{ fontSize: ".78rem", color: "var(--texto-suave)", marginTop: 4, display: "block" }}>
            Descárgalo de la página de la CNSC → SIMO → tu OPEC → &quot;Manual de funciones&quot;.
          </span>
        </label>

        <label style={{ display: "flex", gap: 10, alignItems: "flex-start", marginTop: 20, fontSize: ".88rem", color: "var(--texto-suave)" }}>
          <input type="checkbox" name="consentimiento" required style={{ marginTop: 3 }} />
          <span>Autorizo el tratamiento de mis datos personales conforme a la Ley 1581 de 2012 y la <Link href="/privacidad" style={{ color: "var(--azul)", textDecoration: "underline" }}>política de privacidad</Link>.</span>
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
