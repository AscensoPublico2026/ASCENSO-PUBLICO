const RESEND_URL = "https://api.resend.com/emails";
import { SITE_URL } from "@/lib/site";

// Remitente del dominio verificado en Resend (ascensopublico.com).
// "noreply@" es la dirección de origen; no necesita ser un buzón real.
const FROM = "Ascenso Público <noreply@ascensopublico.com>";

// URL base del sitio (para logos e imágenes en los correos)
const SITE = SITE_URL;
const LOGO_URL = `${SITE}/brand/logo-gold-256.png`;
const WHATSAPP = "573151972091";

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

/**
 * Plantilla base de correo con la marca de Ascenso Público.
 * Encabezado navy con logo dorado + contenido + footer.
 */
function plantilla(opts: { titulo: string; cuerpo: string; cta?: { texto: string; url: string } }): string {
  const { titulo, cuerpo, cta } = opts;
  return `
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#F2F0EA;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F2F0EA;padding:24px 0;">
    <tr>
      <td align="center">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(10,42,94,.10);">
          <!-- Encabezado -->
          <tr>
            <td align="center" style="background:linear-gradient(135deg,#0A2A5E,#1A4A8A);padding:32px 24px;">
              <img src="${LOGO_URL}" alt="Ascenso Público" width="64" height="64" style="display:block;border:0;margin-bottom:12px;">
              <div style="color:#ffffff;font-size:20px;font-weight:800;letter-spacing:.3px;">Ascenso Público</div>
              <div style="color:#F6C56B;font-size:13px;margin-top:4px;">Tu ruta hacia el empleo público</div>
            </td>
          </tr>
          <!-- Contenido -->
          <tr>
            <td style="padding:32px 32px 24px;">
              <h1 style="color:#0A2A5E;font-size:22px;margin:0 0 16px;font-weight:800;">${titulo}</h1>
              <div style="color:#2A3441;font-size:15px;line-height:1.7;">
                ${cuerpo}
              </div>
              ${cta ? `
              <table role="presentation" cellpadding="0" cellspacing="0" style="margin:28px 0 8px;">
                <tr>
                  <td align="center" style="border-radius:12px;background:linear-gradient(135deg,#E8A33D,#F6C56B);">
                    <a href="${cta.url}" target="_blank" style="display:inline-block;padding:14px 32px;color:#0A2A5E;font-size:15px;font-weight:800;text-decoration:none;">${cta.texto}</a>
                  </td>
                </tr>
              </table>` : ""}
            </td>
          </tr>
          <!-- Footer -->
          <tr>
            <td style="background:#0A2A5E;padding:24px 32px;text-align:center;">
              <div style="color:rgba(255,255,255,.85);font-size:13px;line-height:1.6;">
                ¿Tienes dudas? Escríbenos por
                <a href="https://wa.me/${WHATSAPP}" target="_blank" style="color:#F6C56B;font-weight:700;text-decoration:none;">WhatsApp</a>
              </div>
              <div style="color:rgba(255,255,255,.5);font-size:11px;margin-top:12px;">
                © ${new Date().getFullYear()} Ascenso Público · Preparación para concursos de mérito CNSC.<br>
                No afiliado a la CNSC. Material de preparación independiente.
              </div>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`;
}

export async function correoConfirmacionCliente(to: string, nombre: string) {
  const url = `${SITE}/perfil`;
  const primerNombre = (nombre || "").split(" ")[0] || "";
  const html = plantilla({
    titulo: `¡Bienvenido${primerNombre ? `, ${primerNombre}` : ""}! 🎉`,
    cuerpo: `
      <p style="margin:0 0 14px;">Recibimos tu pago correctamente. ¡Gracias por confiar en nosotros para preparar tu ascenso!</p>
      <p style="margin:0 0 14px;">Tu curso personalizado está <strong style="color:#0A2A5E;">en preparación</strong>. Nuestro equipo está armando tu ruta de estudio enfocada en tu cargo, y estará disponible en tu perfil en un máximo de <strong>12 horas</strong>.</p>
      <p style="margin:0;">Mientras tanto, ya puedes ingresar a tu perfil y ver el avance:</p>
    `,
    cta: { texto: "Ir a mi perfil →", url },
  });
  await enviar(to, "¡Bienvenido a Ascenso Público! Tu curso está en preparación", html);
}

export async function correoAvisoAdmin(datos: any) {
  const admin = process.env.ADMIN_EMAIL;
  if (!admin) return;
  const html = plantilla({
    titulo: "🔔 Nueva compra recibida",
    cuerpo: `
      <p style="margin:0 0 16px;">Un nuevo cliente compró un curso. Estos son sus datos:</p>
      <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background:#FBF9F4;border-radius:12px;padding:8px;">
        <tr><td style="padding:8px 14px;color:#5B6675;font-size:13px;width:120px;">Nombre</td><td style="padding:8px 14px;color:#0A2A5E;font-size:14px;font-weight:600;">${datos.nombre || "-"}</td></tr>
        <tr><td style="padding:8px 14px;color:#5B6675;font-size:13px;">Correo</td><td style="padding:8px 14px;color:#0A2A5E;font-size:14px;font-weight:600;">${datos.correo || "-"}</td></tr>
        <tr><td style="padding:8px 14px;color:#5B6675;font-size:13px;">Celular</td><td style="padding:8px 14px;color:#0A2A5E;font-size:14px;font-weight:600;">${datos.celular || "-"}</td></tr>
        <tr><td style="padding:8px 14px;color:#5B6675;font-size:13px;">OPEC</td><td style="padding:8px 14px;color:#0A2A5E;font-size:14px;font-weight:600;">${datos.opec || "-"}</td></tr>
        <tr><td style="padding:8px 14px;color:#5B6675;font-size:13px;">Cargo</td><td style="padding:8px 14px;color:#0A2A5E;font-size:14px;font-weight:600;">${datos.cargo_nombre || "-"}</td></tr>
        <tr><td style="padding:8px 14px;color:#5B6675;font-size:13px;">Nivel</td><td style="padding:8px 14px;color:#0A2A5E;font-size:14px;font-weight:600;">${datos.nivel || "-"}</td></tr>
        <tr><td style="padding:8px 14px;color:#5B6675;font-size:13px;">Referencia</td><td style="padding:8px 14px;color:#0A2A5E;font-size:13px;">${datos.referencia || "-"}</td></tr>
      </table>
      <p style="margin:16px 0 0;font-size:13px;color:#5B6675;">El manual de funciones está en el panel de administración, listo para que armes su ruta.</p>
    `,
    cta: { texto: "Ir al panel admin →", url: `${SITE}/admin/cursos` },
  });
  await enviar(admin, "🔔 Nueva compra — Ascenso Público", html);
}
