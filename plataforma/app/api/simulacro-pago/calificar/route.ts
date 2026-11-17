import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase/server";
import { cargarBanco } from "@/lib/bancoSimulacroPago";
import { correoResultadoSimulacroPago } from "@/lib/email";

export const dynamic = "force-dynamic";

/**
 * Califica el simulacro completo en el servidor. El navegador nunca recibe la
 * respuesta correcta antes de presentar, así que el banco no se puede leer
 * desde las herramientas del navegador.
 */
export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => null);
  const token = String(body?.token || "");
  const respuestas: unknown = body?.respuestas;
  const segundos = Number(body?.segundos || 0);

  if (!token || !Array.isArray(respuestas)) {
    return NextResponse.json({ error: "Petición incompleta." }, { status: 400 });
  }

  const supabase = createAdminClient();
  const { data: compra } = await supabase
    .from("compras_simulacro")
    .select("*")
    .eq("token", token)
    .maybeSingle();

  if (!compra || compra.estado !== "aprobado") {
    return NextResponse.json({ error: "Este acceso no está activo." }, { status: 403 });
  }
  if (compra.expira_en && new Date(compra.expira_en) < new Date()) {
    return NextResponse.json({ error: "Tu acceso venció." }, { status: 403 });
  }
  if ((compra.intentos_usados ?? 0) >= (compra.max_intentos ?? 2)) {
    return NextResponse.json({ error: "Ya usaste todos tus intentos." }, { status: 403 });
  }

  const banco = await cargarBanco(compra.producto);
  if (!banco || banco.length === 0) {
    return NextResponse.json({ error: "No encontramos el banco de preguntas." }, { status: 500 });
  }

  const elegidas = (respuestas as unknown[]).map((r) => (typeof r === "number" ? r : -1));

  let correctas = 0;
  const porEje = new Map<string, { bien: number; total: number }>();
  const detalle = banco.map((p, i) => {
    const marcada = elegidas[i] ?? -1;
    const acierto = marcada === p.correcta;
    if (acierto) correctas++;
    const eje = porEje.get(p.refT) || { bien: 0, total: 0 };
    eje.total++;
    if (acierto) eje.bien++;
    porEje.set(p.refT, eje);
    return {
      i,
      tema: p.tema,
      refT: p.refT,
      nivel: p.nivel,
      ctx: p.ctx,
      q: p.q,
      ops: p.ops,
      correcta: p.correcta,
      marcada,
      acierto,
      expl: p.expl,
    };
  });

  const total = banco.length;
  const porcentaje = Math.round((correctas / total) * 100);
  const competencias = [...porEje.entries()]
    .map(([refT, v]) => ({
      eje: refT,
      bien: v.bien,
      total: v.total,
      pct: Math.round((v.bien / v.total) * 100),
    }))
    .sort((a, b) => a.pct - b.pct);

  const intento = (compra.intentos_usados ?? 0) + 1;
  await supabase
    .from("compras_simulacro")
    .update({ intentos_usados: intento, ultimo_puntaje: porcentaje })
    .eq("id", compra.id);

  try {
    await correoResultadoSimulacroPago(compra.correo, compra.nombre, {
      titulo: compra.producto_nombre || "Simulacro completo",
      porcentaje,
      correctas,
      total,
      competencias: competencias.slice(0, 5),
      token,
    });
  } catch (e) {
    console.error("No se pudo enviar el resultado del simulacro de pago:", e);
  }

  return NextResponse.json({
    correctas,
    total,
    porcentaje,
    segundos,
    competencias,
    detalle,
    intento,
    maxIntentos: compra.max_intentos ?? 2,
  });
}
