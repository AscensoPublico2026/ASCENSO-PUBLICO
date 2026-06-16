const RESEND_URL = "https://api.resend.com/emails";
// Remitente del dominio verificado en Resend (ascensopublico.com).
// "noreply@" es la dirección de origen; no necesita ser un buzón real.
const FROM = "Ascenso Público <noreply@ascensopublico.com>";

async function enviar(to: string | string[], subject: string, html: string) {
  const key = process.env.RESEND_API_KEY;
  if (!key) {
    console.error("[email] RESEND_API_KEY no configurada");
    return;
  }
  try {
    const res = await fetch(RESEND_URL, {
      method: "POST",
      headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({ from: FROM, to, subject, html }),
    });
    if (!res.ok) {
      const body = await res.text();
      console.error(`[email] Resend rechazó el envío (${res.status}):`, body);
    }
  } catch (e) {
    console.error("[email] Error enviando correo:", e);
  }
}

export async function correoConfirmacionCliente(to: string, nombre: string) {
  const url = `${process.env.NEXT_PUBLIC_SITE_URL || ""}/perfil`;
  await enviar(
    to,
    "¡Bienvenido a Ascenso Público! Tu curso está en preparación",
    `<p>Hola ${nombre || ""},</p>
     <p>Recibimos tu pago. Tu curso personalizado está <strong>en preparación</strong> y estará disponible en tu perfil en máximo <strong>12 horas</strong>.</p>
     <p>Entra a tu perfil: <a href="${url}">${url}</a></p>
     <p>— Ascenso Público</p>`
  );
}

export async function correoAvisoAdmin(datos: any) {
  const admin = process.env.ADMIN_EMAIL;
  if (!admin) return;
  await enviar(
    admin,
    "🔔 Nueva compra — Ascenso Público",
    `<p>Nueva compra recibida:</p>
     <ul>
       <li><strong>Nombre:</strong> ${datos.nombre || "-"}</li>
       <li><strong>Correo:</strong> ${datos.correo || "-"}</li>
       <li><strong>Celular:</strong> ${datos.celular || "-"}</li>
       <li><strong>OPEC:</strong> ${datos.opec || "-"}</li>
       <li><strong>Cargo:</strong> ${datos.cargo_nombre || "-"}</li>
       <li><strong>Nivel:</strong> ${datos.nivel || "-"}</li>
       <li><strong>Referencia:</strong> ${datos.referencia || "-"}</li>
     </ul>
     <p>El manual de funciones está en Supabase Storage (bucket <code>manuales</code>).</p>`
  );
}
