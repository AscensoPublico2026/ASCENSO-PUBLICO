import Link from "next/link";
import { requireAdmin } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import FormCrearCliente from "./FormCrearCliente";

export const dynamic = "force-dynamic";

export default async function CrearClientePage() {
  await requireAdmin();
  const supabase = createClient();
  const { data: convocatorias } = await supabase
    .from("convocatorias")
    .select("id, nombre, entidad")
    .eq("activa", true)
    .order("orden", { ascending: true });

  return (
    <main style={{ maxWidth: 680, margin: "0 auto", padding: "40px 22px" }}>
      <Link href="/admin" style={{ color: "var(--texto-suave)", fontSize: ".9rem" }}>← Panel</Link>
      <h1 style={{ fontSize: "1.7rem", margin: "12px 0 8px" }}>Crear cliente manual</h1>
      <p style={{ color: "var(--texto-suave)", marginBottom: 28, fontSize: ".92rem" }}>
        Crea un perfil y curso sin pasar por la pasarela de pagos.
        Ideal para pagos por transferencia, consignación o efectivo.
      </p>
      <FormCrearCliente convocatorias={convocatorias || []} />
    </main>
  );
}
