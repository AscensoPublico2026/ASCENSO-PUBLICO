"use server";

import { createAdminClient } from "@/lib/supabase/server";
import { correoResultadoSimulacro } from "@/lib/email";
import { evaluarSimulacro } from "@/lib/simulacro/evaluar";
import { preguntasDeNivel, esNivelValido, nombreNivel } from "@/lib/simulacro/preguntas";

const TERMINOS_VERSION = "2026-06";

export interface GuardarLeadInput {
  nivel: string;
  correo: string;
  whatsapp?: string;
  respuestas: number[];
  aceptaMarketing: boolean;
  userAgent?: string;
}

export async function guardarLeadSimulacro(input: GuardarLeadInput) {
  if (!esNivelValido(input.nivel)) {
    return { ok: false, error: "Nivel inválido." };
  }
  const correo = (input.correo || "").trim().toLowerCase();
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(correo)) {
    return { ok: false, error: "Ingresa un correo válido." };
  }

  const preguntas = preguntasDeNivel(input.nivel);
  const resultado = evaluarSimulacro(preguntas, input.respuestas || []);

  try {
    const supabase = createAdminClient();
    await supabase.from("leads_simulacro").insert({
      nivel: input.nivel,
      correo,
      whatsapp: input.whatsapp?.trim() || null,
      puntaje: resultado.porcentaje,
      correctas: resultado.correctas,
      total: resultado.total,
      temas_debiles: resultado.temasAReforzar.map((t) => t.tema),
      acepta_marketing: !!input.aceptaMarketing,
      consentimiento_fecha: input.aceptaMarketing ? new Date().toISOString() : null,
      terminos_version: TERMINOS_VERSION,
      user_agent: input.userAgent || null,
    });
  } catch (e) {
    console.error("[simulacro] error guardando lead:", e);
    // No bloqueamos al usuario por un fallo de guardado; igual ve su resultado.
  }

  try {
    await correoResultadoSimulacro(correo, {
      nivel: nombreNivel(input.nivel),
      porcentaje: resultado.porcentaje,
      correctas: resultado.correctas,
      total: resultado.total,
      temasAReforzar: resultado.temasAReforzar.map((t) => ({ tema: t.tema, guia: t.guia.titulo })),
      temasDominados: resultado.temasDominados.map((t) => ({ tema: t.tema })),
    });
  } catch (e) {
    console.error("[simulacro] error enviando correo:", e);
  }

  return { ok: true };
}
