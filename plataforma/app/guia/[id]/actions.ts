"use server";

import { revalidatePath } from "next/cache";
import { createClient } from "@/lib/supabase/server";
import { calcularDesbloqueo, siguienteGuia } from "@/lib/desbloqueo";

/**
 * Marca una guía como TERMINADA (cursos con desbloqueo secuencial).
 * Valida en el servidor que la guía sea del estudiante y que no esté
 * bloqueada. Devuelve la siguiente guía del plan, que queda desbloqueada.
 */
export async function marcarGuiaTerminada(guiaId: string): Promise<{ ok: boolean; siguienteId?: string | null; error?: string }> {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return { ok: false, error: "Tu sesión expiró. Vuelve a iniciar sesión." };

  const { data: guia } = await supabase
    .from("guias_curso")
    .select("id, curso_id, leida")
    .eq("id", guiaId)
    .single();
  if (!guia) return { ok: false, error: "Guía no encontrada." };

  // Solo el dueño del curso marca su progreso (el admin no contamina el avance).
  const { data: curso } = await supabase
    .from("cursos")
    .select("id, usuario_id")
    .eq("id", guia.curso_id)
    .single();
  if (!curso || curso.usuario_id !== user.id) return { ok: false, error: "Esta guía no pertenece a tu curso." };

  const { data: todas } = await supabase
    .from("guias_curso")
    .select("id, leida, archivo_path, tipo, dia, orden")
    .eq("curso_id", guia.curso_id);

  const { bloqueadas } = calcularDesbloqueo(todas || []);
  if (bloqueadas.has(guia.id)) return { ok: false, error: "Primero termina la guía anterior." };

  if (!guia.leida) {
    const { error } = await supabase
      .from("guias_curso")
      .update({ leida: true, fecha_leida: new Date().toISOString() })
      .eq("id", guia.id);
    if (error) return { ok: false, error: "No pudimos guardar tu avance. Intenta de nuevo." };

    const total = (todas || []).filter((g: any) => g.archivo_path).length;
    const leidas = (todas || []).filter((g: any) => g.archivo_path && (g.leida || g.id === guia.id)).length;
    if (total > 0) {
      await supabase.from("cursos").update({ progreso_pct: Math.round((leidas / total) * 100) }).eq("id", guia.curso_id);
    }
  }

  revalidatePath(`/perfil/${guia.curso_id}`);
  const sig = siguienteGuia(todas || [], guia.id);
  return { ok: true, siguienteId: sig?.id ?? null };
}
