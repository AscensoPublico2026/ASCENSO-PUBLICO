"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireAdmin } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/server";

export async function actualizarCupos(formData: FormData) {
  const user = await requireAdmin();
  const vendidos = Number(formData.get("vendidos"));
  const total = Number(formData.get("total"));

  if (!Number.isInteger(vendidos) || vendidos < 0) {
    throw new Error("La cantidad de cursos vendidos debe ser un entero igual o mayor que cero.");
  }
  if (!Number.isInteger(total) || total <= 0) {
    throw new Error("El total de cupos debe ser un entero mayor que cero.");
  }
  if (vendidos > total) {
    throw new Error("Los cursos vendidos no pueden superar el total de cupos.");
  }

  const supabase = createAdminClient();
  const { error } = await supabase.from("configuracion_cupos").upsert({
    id: 1,
    vendidos,
    total,
    updated_at: new Date().toISOString(),
    updated_by: user.id,
  }, { onConflict: "id" });

  if (error) throw new Error("No se pudo actualizar el contador: " + error.message);

  revalidatePath("/");
  revalidatePath("/comprar");
  revalidatePath("/admin");
  revalidatePath("/admin/configuracion");
  redirect("/admin/configuracion?guardado=1");
}
