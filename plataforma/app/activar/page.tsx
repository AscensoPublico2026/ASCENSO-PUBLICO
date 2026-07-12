import { getTransaction } from "@/lib/wompiApi";
import { procesarReferencia } from "@/lib/procesarPago";
import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

// Wompi redirige aquí tras el pago (redirect-url), añadiendo ?id=<transaction_id>.
// Ya no hay formulario de contraseña: el usuario la definió ANTES del pago en /comprar.
// Esta página solo loguea al usuario automáticamente y lo redirige a /perfil.
export default async function ActivarPage({ searchParams }: { searchParams: { id?: string; ref?: string } }) {
  const id = searchParams?.id;
  let referencia = searchParams?.ref || "";
  let aprobado = false;
  let email = "";
  let password = "";

  if (id) {
    const tx = await getTransaction(id);
    if (tx) {
      referencia = tx.reference;
      aprobado = tx.status === "APPROVED";
    }
  }

  if (!aprobado) {
    return (
      <main style={{ maxWidth: 560, margin: "0 auto", padding: "70px 22px", textAlign: "center" }}>
        <h1 style={{ fontSize: "1.6rem" }}>Estamos confirmando tu pago…</h1>
        <p style={{ color: "var(--texto-suave)", marginTop: 12 }}>
          Si acabas de pagar, espera unos segundos y recarga esta página. Si el problema persiste,
          escríbenos por WhatsApp y lo resolvemos.
        </p>
      </main>
    );
  }

  // Pago aprobado → procesar y obtener datos
  if (referencia) {
    try {
      const r = await procesarReferencia(referencia, id);
      if (r) email = r.email;
      
      // Obtener la contraseña del preregistro para hacer login automático
      const { createAdminClient } = await import("@/lib/supabase/server");
      const adminClient = createAdminClient();
      const { data: pre } = await adminClient.from("preregistros").select("password").eq("referencia", referencia).single();
      password = pre?.password || "";
    } catch (err) {
      console.error("[/activar] Error procesando referencia:", err);
    }
  }

  // Si tenemos email Y password, intentar login automático
  if (email && password) {
    const supabase = createClient();
    const { error } = await supabase.auth.signInWithPassword({ email, password });
    
    if (!error) {
      // Login exitoso → redirigir a perfil
      redirect("/perfil");
    }
  }

  // Si llegamos aquí, algo falló → mostrar mensaje para ir a login manual
  return (
    <main style={{ maxWidth: 560, margin: "0 auto", padding: "70px 22px", textAlign: "center" }}>
      <div style={{ width: 60, height: 60, borderRadius: "50%", background: "var(--verde-suave)", color: "var(--verde)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "1.8rem", margin: "0 auto 16px" }}>✓</div>
      <h1 style={{ fontSize: "1.7rem" }}>¡Pago confirmado!</h1>
      <p style={{ color: "var(--texto-suave)", margin: "10px 0 24px" }}>
        Tu curso está listo. Inicia sesión con tu correo y la contraseña que creaste.
      </p>
      <a href="/login" className="btn btn-oro" style={{ display: "inline-block", padding: "12px 32px", textDecoration: "none" }}>
        Ir a iniciar sesión →
      </a>
    </main>
  );
}
