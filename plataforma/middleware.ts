import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

/**
 * Middleware de autenticación para Ascenso Público.
 * Protege las rutas /perfil/* y /guia/* — si no hay sesión, redirige a /login.
 * Las rutas públicas (/, /comprar, /login, /activar, /convocatorias, etc.) no se protegen.
 */
export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // Rutas protegidas (requieren sesión)
  const protectedPaths = ["/perfil", "/guia"];
  const isProtected = protectedPaths.some((p) => pathname.startsWith(p));

  if (!isProtected) {
    return NextResponse.next();
  }

  // Crear cliente de Supabase con las cookies del request
  let response = NextResponse.next({ request });

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return request.cookies.getAll();
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) => {
            request.cookies.set(name, value);
            response.cookies.set(name, value, options);
          });
        },
      },
    }
  );

  // Verificar sesión
  const { data: { user } } = await supabase.auth.getUser();

  if (!user) {
    // Redirigir a login con la URL de retorno
    const loginUrl = new URL("/login", request.url);
    loginUrl.searchParams.set("next", pathname);
    return NextResponse.redirect(loginUrl);
  }

  return response;
}

export const config = {
  matcher: ["/perfil/:path*", "/guia/:path*"],
};
