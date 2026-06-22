import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase/server";
import { correoResultadoSimulacro } from "@/lib/email";

export const dynamic = "force-dynamic";

const TERMINOS_VERSION = "2026-06";

const NOMBRE_NIVEL: Record<string, string> = {
  asistencial: "Asistencial",
  tecnico: "Técnico",
  profesional: "Profesional",
};

const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

interface Tema {
  tema: string;
  guia: string;
}

/**
 * Recibe el lead del SIMULACRO GRATIS (HTML estático) cuando el usuario presenta
 * el examen. Guarda el lead (service role) y envía el correo de resultado.
 * El cálculo del puntaje lo hace el HTML; aquí solo persistimos y notificamos.
 */
export async function POST(req: NextRequest) {
  let body: any;
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ ok: false, error: "JSON inválido" }, { status: 400 });
  }

  const nivelId = String(body?.nivel || "").toLowerCase();
  if (!NOMBRE_NIVEL[nivelId]) {
    return NextResponse.json({ ok: false, error: "Nivel inválido" }, { status: 400 });
  }

  const correo = String(body?.correo || "").trim().toLowerCase();
  if (!EMAIL_RE.test(correo)) {
    return NextResponse.json({ ok: false, error: "Correo inválido" }, { status: 400 });
  }

  const whatsapp = body?.whatsapp ? String(body.whatsapp).trim() : null;
  const aceptaMarketing = !!body?.aceptaMarketing;

  const total = Number.isFinite(body?.total) ? Math.max(0, Math.trunc(body.total)) : 0;
  const correctas = Number.isFinite(body?.correctas) ? Math.max(0, Math.trunc(body.correctas)) : 0;
  const porcentaje = Number.isFinite(body?.porcentaje)
    ? Math.min(100, Math.max(0, Math.trunc(body.porcentaje)))
    : 0;

  const temasAReforzar: Tema[] = Array.isArray(body?.temasAReforzar)
    ? body.temasAReforzar
        .filter((t: any) => t && t.tema)
        .map((t: any) => ({ tema: String(t.tema), guia: String(t.guia || "") }))
        .slice(0, 30)
    : [];
  const temasDominados: { tema: string }[] = Array.isArray(body?.temasDominados)
    ? body.temasDominados
        .filter((t: any) => t && t.tema)
        .map((t: any) => ({ tema: String(t.tema) }))
        .slice(0, 30)
    : [];

  // Guardar el lead (no bloqueamos al usuario si falla)
  try {
    const supabase = createAdminClient();
    await supabase.from("leads_simulacro").insert({
      nivel: nivelId,
      correo,
      whatsapp,
      puntaje: porcentaje,
      correctas,
      total,
      temas_debiles: temasAReforzar.map((t) => t.tema),
      acepta_marketing: aceptaMarketing,
      consentimiento_fecha: aceptaMarketing ? new Date().toISOString() : null,
      terminos_version: TERMINOS_VERSION,
      user_agent: req.headers.get("user-agent") || null,
    });
  } catch (e) {
    console.error("[simulacro] error guardando lead:", e);
  }

  // Enviar correo con el resultado (no bloqueamos al usuario si falla)
  try {
    await correoResultadoSimulacro(correo, {
      nivel: NOMBRE_NIVEL[nivelId],
      porcentaje,
      correctas,
      total,
      temasAReforzar,
      temasDominados,
    });
  } catch (e) {
    console.error("[simulacro] error enviando correo:", e);
  }

  return NextResponse.json({ ok: true });
}
