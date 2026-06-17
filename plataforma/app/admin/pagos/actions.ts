"use server";

import { revalidatePath } from "next/cache";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";

/**
 * Elimina el registro de un pago (y su preregistro asociado) por referencia.
 * Útil para limpiar pagos de PRUEBA que quedaron huérfanos tras borrar
 * perfiles/cursos. NO toca usuarios ni cursos.
 */
export async function eliminarPago(referencia: string) {
  await requireAdmin();
  const supabase = createAdminClient();
  await supabase.from("pagos").delete().eq("referencia", referencia);
  await supabase.from("preregistros").delete().eq("referencia", referencia);
  revalidatePath("/admin/pagos");
  revalidatePath("/admin");
}
