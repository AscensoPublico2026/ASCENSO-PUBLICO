import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";
import {
  CUPOS_TOTALES_LANZAMIENTO,
  CUPOS_VENDIDOS_LANZAMIENTO,
} from "@/lib/cupos";

export const dynamic = "force-dynamic";

export async function GET() {
  let vendidos = CUPOS_VENDIDOS_LANZAMIENTO;
  let total = CUPOS_TOTALES_LANZAMIENTO;

  try {
    // Esta lectura usa la clave pública y queda sujeta a la política RLS de solo lectura.
    const supabase = createClient();
    const { data } = await supabase
      .from("configuracion_cupos")
      .select("vendidos,total")
      .eq("id", 1)
      .maybeSingle();

    if (
      data && Number.isInteger(data.vendidos) && Number.isInteger(data.total) &&
      data.vendidos >= 0 && data.total > 0 && data.vendidos <= data.total
    ) {
      vendidos = data.vendidos;
      total = data.total;
    }
  } catch {
    // Si la migración aún no se aplicó o Supabase no está disponible,
    // mantenemos el último valor seguro compilado (177/200).
  }

  return NextResponse.json(
    { vendidos, total },
    { headers: { "Cache-Control": "no-store, max-age=0" } },
  );
}
