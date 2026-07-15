import { createServerClient, type CookieOptions } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

/**
 * Middleware de autenticación para Ascenso Público.
 * Protege las rutas /perfil/* y /guia/* — si no hay sesión, redirige a /login.
 */
export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // No interceptar rutas de API (se protegen internamente)
  if (pathname.startsWith("/api/")) {
    return NextResponse.next();
  }

  // Solo proteger rutas que requieren sesión
  const protectedPaths = ["/perfil", "/guia", "/admin"];
  const isProtected = protectedPaths.some((p) => pathname.startsWith(p));

  if (!isProtected) {
    return NextResponse.next();
  }

  // Crear response base
  const response = NextResponse.next({ request });

  try {
    const supabase = createServerClient(
      process.env.NEXT_PUBLIC_SUPABASE_URL!,
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
      {
        cookies: {
          getAll() {
            return request.cookies.getAll();
          },
          setAll(cookiesToSet: { name: string; value: string; options: CookieOptions }[]) {
            cookiesToSet.forEach(({ name, value, options }) => {
              response.cookies.set(name, value, options);
            });
          },
        },
      }
    );

    const { data: { user } } = await supabase.auth.getUser();

    if (!user) {
      const loginUrl = new URL("/login", request.url);
      loginUrl.searchParams.set("next", pathname);
      return NextResponse.redirect(loginUrl);
    }
  } catch {
    // Si falla la verificación de auth, redirigir a login
    const loginUrl = new URL("/login", request.url);
    return NextResponse.redirect(loginUrl);
  }

  return response;
}

export const config = {
  matcher: ["/perfil/:path*", "/guia/:path*", "/admin/:path*"],
};
