import { NextRequest, NextResponse } from "next/server";

/**
 * DEBUG: Envía un correo de prueba con Resend y muestra la respuesta COMPLETA.
 * Uso: /api/admin/test-email?to=tucorreo@gmail.com
 * 
 * Permite diagnosticar por qué no llegan los correos (API key, FROM, dominio, etc.)
 */
export async function GET(req: NextRequest) {
  const to = req.nextUrl.searchParams.get("to");
  if (!to) return NextResponse.json({ error: "Falta ?to=correo@ejemplo.com" });

  const key = process.env.RESEND_API_KEY;
  const FROM = "Ascenso Público <noreply@ascensopublico.com>";

  const diagnostico: any = {
    tiene_api_key: !!key,
    api_key_prefijo: key ? key.substring(0, 6) + "..." : "NO CONFIGURADA",
    from: FROM,
    to,
    admin_email: process.env.ADMIN_EMAIL || "NO CONFIGURADA",
  };

  if (!key) {
    return NextResponse.json({ diagnostico, error: "RESEND_API_KEY no está configurada en Vercel" });
  }

  try {
    const res = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        from: FROM,
        to,
        subject: "Prueba de correo — Ascenso Público",
        html: "<p>Este es un correo de prueba. Si lo recibes, la configuración de Resend funciona correctamente. ✅</p>",
      }),
    });

    const httpStatus = res.status;
    const body = await res.json();

    return NextResponse.json({
      diagnostico,
      resultado_resend: {
        http_status: httpStatus,
        respuesta: body,
        exito: httpStatus >= 200 && httpStatus < 300,
      },
      interpretacion: httpStatus >= 200 && httpStatus < 300
        ? "✅ Correo enviado correctamente. Revisa tu bandeja (y spam)."
        : "❌ Resend rechazó el envío. Revisa el campo 'respuesta' para ver el motivo.",
    });
  } catch (e: any) {
    return NextResponse.json({ diagnostico, error: "Excepción: " + e.message });
  }
}
