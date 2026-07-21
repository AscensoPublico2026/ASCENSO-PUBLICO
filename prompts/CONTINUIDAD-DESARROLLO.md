# 🛠️ Continuidad — DESARROLLO Y MEJORAS de la plataforma

> **Cuándo usar este documento:** cuando vas a hacer **ajustes, arreglos, modificaciones,
> personalizaciones o mejoras** de la plataforma Ascenso Público (la web, el admin, los
> correos, la UX, etc.). Esta es la "sección de desarrollo" del proyecto.

---

## 🟢 PROMPT PARA PEGAR EN UNA SESIÓN NUEVA DE KIRO

Copia y pega esto al iniciar sesión (repo `ascensopublico2026/ASCENSO-PUBLICO` conectado):

```
Hola Kiro. Vamos a trabajar en MEJORAS / AJUSTES de la plataforma Ascenso Público.
Antes de tocar nada, lee:
1. CONTINUIDAD.md (estado y cambios recientes)
2. prompts/CONTINUIDAD-DESARROLLO.md (este flujo de trabajo)
3. ARQUITECTURA-PLATAFORMA.md y ESTANDAR-TECNICO.md si el cambio toca arquitectura.

Trabaja SIEMPRE en una rama nueva y al final dame el link de compare para mergear yo
(la herramienta de crear PR falla con "No provider found", así que pásame el link
https://github.com/ascensopublico2026/ASCENSO-PUBLICO/compare/main...NOMBRE_RAMA).

Lo que quiero ajustar/mejorar hoy es:
- (describe aquí el cambio)
```

---

## 🧭 Cómo trabajamos en esta sección (reglas del proyecto)

- **Stack:** Next.js 14 (App Router) + TypeScript en `/plataforma`; Supabase (BD/Auth/Storage); Vercel (Root = `plataforma`); Wompi (pagos, en **producción**); Resend (correos); dominio `https://ascensopublico.com` (Cloudflare).
- **Git:** ramas nuevas siempre; **nunca** push directo a `main`. Push con la herramienta `github_push_to_remote` (no `git push`). El usuario mergea desde GitHub con el **link de compare**.
- **Sandbox:** sin acceso directo a Supabase/Wompi/Vercel; Kiro escribe código, el usuario configura los paneles externos. Si `main` local se ve desactualizado, usar `pull_repository` antes de ramificar.
- **Marca:** navy `#0A2A5E` · crema `#FBF9F4` · oro `#E8A33D`. Tipos: Source Serif 4 + Plus Jakarta Sans.
- **Contacto/redes:** todo sale de `plataforma/lib/contacto.ts` (WhatsApp `573170905177`, `REDES`). No hardcodear.
- **Reglas de producto:** precio $300.000 (`PRECIO_COP`, en centavos al cobrar); cupos de lanzamiento 177/200 (centralizados en `plataforma/lib/cupos.ts`); plan 21 días (20 estudio L-V + simulacro); el simulacro se desbloquea al terminar las guías del plan (bonus no cuenta); habilitación del curso a 12h o "Habilitar ahora" (envía correo).
- **Verificación:** no se puede compilar localmente (sin node_modules/red). Validar leyendo el código con cuidado; el usuario prueba en producción tras desplegar.

## 📂 Mapa rápido de archivos (los que más se tocan)
- Landing: `plataforma/app/page.tsx` + `plataforma/app/landing.css` + `plataforma/app/components/*`.
- Compra/pago: `plataforma/app/comprar/*`, `plataforma/lib/wompi.ts`, `plataforma/lib/wompiApi.ts`, `plataforma/app/api/webhooks/wompi/route.ts`, `plataforma/lib/procesarPago.ts`, `plataforma/app/activar/*`.
- Estudiante: `plataforma/app/perfil/page.tsx`, `plataforma/app/perfil/[cursoId]/page.tsx`, `plataforma/app/guia/[id]/*`, `globals.css`.
- Admin: `plataforma/app/admin/**` (cursos, pagos, usuarios, convocatorias) + sus `actions.ts`.
- Correos: `plataforma/lib/email.ts`. Catálogo: `plataforma/lib/catalogoGuias.ts` + `lib/biblioteca.json`.

## ✅ Flujo de trabajo recomendado
1. Entender el pedido y leer SOLO los archivos relevantes (usar el context-gatherer si no se conoce la zona).
2. Rama nueva → cambios pequeños y verificables → commit claro → push.
3. **Documentar el cambio en CONTINUIDAD.md** (sección "CAMBIOS RECIENTES").
4. Entregar el **link de compare** y, si aplica, los pasos que el usuario debe hacer en paneles externos (Vercel/Supabase/Wompi).

## 🧪 Pruebas
- Checklist completo en `PRE-LANZAMIENTO-PRUEBAS.md` y la versión interactiva en `https://ascensopublico.com/checklist-pruebas.html`.

> Regla de oro: **cada cambio relevante se documenta en CONTINUIDAD.md** para no perder el hilo entre sesiones/cuentas.
