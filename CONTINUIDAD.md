# 🔄 CONTINUIDAD DEL PROYECTO — Ascenso Público

> **Para retomar en una nueva sesión de Kiro:** conecta este repositorio y pídele a Kiro:
> *"Lee CONTINUIDAD.md y ARQUITECTURA-PLATAFORMA.md y continuemos donde quedamos."*

_Última actualización: 15 de junio de 2026 (plataforma ya desplegada y funcionando)._

---

## 1. Qué es el proyecto
**Ascenso Público**: preparación **personalizada por el CARGO específico** para concursos de méritos de la **CNSC** (Colombia). Plan de 21 días + guías + simulacros, según el OPEC y el **manual de funciones** del aspirante.

Dos partes:
1. **Landing** (marketing) — ✅ en vivo (GitHub Pages).
2. **Plataforma** (portal del estudiante + compra + panel admin) — ✅ **DESPLEGADA Y FUNCIONANDO** en Vercel.

## 2. Repositorio y URLs
- **GitHub:** `ascensopublico2026/ASCENSO-PUBLICO` · rama principal: **`main`**.
- **Landing en vivo:** https://ascensopublico2026.github.io/ASCENSO-PUBLICO/landing/
- **Plataforma en vivo:** https://ascenso-publico.vercel.app
- Para conectar en la nueva sesión: setup del repo con `owner=ascensopublico2026`, `repo=ASCENSO-PUBLICO`.

## 3. Estado ACTUAL (¡importante!)
### ✅ La plataforma YA está desplegada y probada de punta a punta (en sandbox)
- **Stack:** Next.js (App Router) + Supabase (Auth/DB/Storage) + Vercel (Hobby) + Wompi (sandbox) + Resend.
- **Supabase:** proyecto creado, `schema.sql` ejecutado, buckets `manuales` y `guias` (privados). Admin = `ascensopublico@gmail.com` (rol admin).
- **Vercel:** proyecto `ascenso-publico` (Root Directory = `plataforma`, framework Next.js vía `vercel.json`). Las **12 variables de entorno** están configuradas EN VERCEL (no en el repo): Supabase, Wompi, Resend, ADMIN_EMAIL, PRECIO_COP, NEXT_PUBLIC_SITE_URL=https://ascenso-publico.vercel.app, NEXT_PUBLIC_WOMPI_REDIRECT_URL=.../activar.
- **Wompi:** cuenta en **sandbox/revisión**. Webhook configurado → `https://ascenso-publico.vercel.app/api/webhooks/wompi`.
- **Flujo probado OK:** /comprar (datos + PDF) → checkout Wompi (tarjeta prueba 4242…) → /activar (crear contraseña) → /perfil (curso "en preparación" + contador 12h) → admin sube guía + "Habilitar acceso" → estudiante ve la guía **renderizada** (se arregló sirviéndola vía `/api/guia/[id]` como text/html; charset=utf-8).

### ⚠️ Pendientes conocidos (no bloquean)
- **Resend:** plan gratis sin dominio → los correos al CLIENTE no salen aún (solo al correo de la cuenta). Falta verificar dominio (DNS).
- **Wompi:** pasar de sandbox a **producción** cuando Wompi active la cuenta (cambiar llaves `pub_prod`/`prv_prod`).
- **Landing:** ajustes finos menores.
- **Dominio propio** (opcional) + actualizar Open Graph.

## 4. 🎯 SIGUIENTE MÓDULO A CONSTRUIR (confirmado viable, NO construido aún)
**Rediseño del módulo de estudiante + auto-carga de guías.** Lo que se acordó:
1. **Multi-curso por perfil:** `/perfil` debe ser un **tablero con todos los cursos** del usuario (hoy solo muestra el último). Al hacer clic en un curso → **página de detalle** con su biblioteca por días.
2. **Tarjeta de curso:** muestra **OPEC**, **nombre del cargo** y la **imagen de la convocatoria** (reusar fotos de la landing). Decisión pendiente: el nombre del cargo se captura en compra/panel (recomendado) vs. extraer del PDF (frágil; opcional a futuro).
3. **Auto-carga de guías al comprar:** según el `nivel` del curso, asignar automáticamente desde un **catálogo de plantillas** (sembrado de `biblioteca/biblioteca.json`):
   - Generales/intro/bonus para todos: `INTRO-00`, `GEN-01/02/03`, `BON-01`.
   - Las del nivel (días 5–8): `ASI-*` / `TEC-*` / `PRO-*`.
   - Con su **día y orden** ya definidos (día 1 intro, 2–4 general, 5–8 nivel, 9–20 funcionales, 21 simulacro).
4. **El admin solo sube las guías NUEVAS/custom:** funcionales (días 9–20), simulacro final (día 21), INTRO-01 (entidad). Ya existe `subirGuia` en el panel.

**Para implementarlo se necesita:**
- Subir **una vez** las 17 guías de `guias/` a Supabase Storage (carpeta compartida de plantillas).
- Crear tabla `guias_plantilla` (sembrada desde `biblioteca.json`) + regla de auto-asignación por nivel en `lib/procesarPago.ts`.
- Rediseñar `app/perfil/page.tsx` (multi-curso) + nueva página de detalle de curso.

**Decisiones pendientes antes de construir:** (a) nombre del cargo manual vs. auto-PDF; (b) guías todas disponibles vs. desbloqueo por día; (c) confirmar reúso de imágenes de convocatoria de la landing.

## 5. Estructura del repo
```
landing/index.html · landing/preparacion.html   · Landing (GitHub Pages)
plataforma/                                      · App Next.js (la plataforma desplegada)
  ├─ app/ (comprar, convocatorias, activar, login, perfil, admin, api/webhooks, api/guia)
  ├─ lib/ (supabase, wompi, wompiApi, email, auth, procesarPago)
  ├─ supabase/schema.sql · SETUP.md · DESPLIEGUE.md · vercel.json · .env.example
brand/ (logos + brand/fotos)  ·  guias/ (17 guías HTML por nivel)  ·  biblioteca/ (biblioteca.json = catálogo)
docs/investigacion-competencia/  ·  prompts/  ·  scripts/
ARQUITECTURA-PLATAFORMA.md · PROYECTO-MAESTRO.md · PLAN-PROYECTO.md · ESTANDAR-TECNICO.md · PLANTILLA-GUIA.md
```

## 6. Datos clave (NO cambiar sin avisar)
- **Marca:** navy `#0A2A5E` · crema `#FBF9F4` · oro `#E8A33D`. Tipos: Source Serif 4 + Plus Jakarta Sans.
- **Contacto:** WhatsApp **+57 315 197 2091** · correo **ascensopublico@gmail.com**. **Precio:** $300.000 COP pago único.
- **Fundador:** Julio César Deávila.
- **Convención de guías** (en `guias/`): `INTRO-*`, `GEN-*`, `BON-*` (todos) · `ASI-*` (asistencial) · `TEC-*` (técnico) · `PRO-*` (profesional).

## 7. Reglas de trabajo (IMPORTANTES)
- 🚫 **Integridad:** nada de testimonios/fotos/cifras inventadas. Solo datos reales.
- 🖼️ Imágenes: comprimir (squoosh) antes de subir; nombres sin espacios.
- 🔒 Datos personales (Ley 1581) + nunca exponer secretos (`service_role`, llaves privadas, env). Las variables viven en Vercel, no en el repo.
- 🌐 El sandbox de Kiro **no tiene internet**: Kiro escribe/sube código; **instalar/desplegar lo hace el usuario** (Vercel/Supabase). Vercel **redespliega solo** al hacer merge a `main`.
- 🔀 Git: trabajar en ramas + merge a `main` (no `git push` directo; usar herramientas de push/PR).

## 8. Cómo dejamos esta conversación
Plataforma desplegada, probada de punta a punta en sandbox y con la guía renderizando bien. El usuario va a continuar desde **otra cuenta de Kiro**. El siguiente paso es **construir el rediseño del módulo de estudiante** (sección 4), tras confirmar las 3 decisiones pendientes.
