import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

// Exige sesión de administrador; si no, redirige.
export async function requireAdmin() {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");
  const { data: profile } = await supabase.from("profiles").select("rol").eq("id", user.id).single();
  if (!profile || profile.rol !== "admin") redirect("/perfil");
  return user;
}
