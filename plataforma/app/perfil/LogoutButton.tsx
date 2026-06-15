"use client";

import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";

export default function LogoutButton() {
  const router = useRouter();
  async function salir() {
    const supabase = createClient();
    await supabase.auth.signOut();
    router.push("/login");
  }
  return (
    <button onClick={salir} style={{ background: "none", border: "1px solid var(--gris-borde)", borderRadius: 10, padding: "8px 16px", cursor: "pointer", fontFamily: "inherit", color: "var(--texto-suave)" }}>
      Cerrar sesión
    </button>
  );
}
