# 🔄 CONTINUIDAD DEL PROYECTO — Ascenso Público

> **Para retomar en una nueva sesión de Kiro:** conecta este repositorio y pídele a Kiro:
> *"Lee CONTINUIDAD.md y ARQUITECTURA-PLATAFORMA.md y continuemos donde quedamos."*

_Última actualización: 16 de junio de 2026._

---

## 1. Qué es el proyecto
**Ascenso Público**: preparación **personalizada por el CARGO específico** (no solo por nivel) para los concursos de méritos de la **CNSC** (Colombia). Plan de 21 días + guías + simulacros tipo CNSC, a partir del OPEC y el **manual de funciones** del aspirante.

**La plataforma está 100% DESPLEGADA y funcionando en producción:** https://ascensopublico.com

## 2. Repositorio
- **GitHub:** `ascensopublico2026/ASCENSO-PUBLICO`
- **Rama principal:** `main` (todo el trabajo está mergeado ahí).
- **La app Next.js está en la subcarpeta `/plataforma`** (Vercel usa Root Directory = `plataforma`).

## 3. Stack y despliegue (TODO EN PRODUCCIÓN)
- **Next.js 14** (App Router) + TypeScript — carpeta `/plataforma`
- **Supabase** (BD + Auth + Storage) — proyecto `tkxcijdqnivqhmjemvlu`
- **Vercel** — plan **Hobby** por ahora (pasar a Pro $20/mes al vender formalmente). Root = `plataforma`
- **Wompi** (sandbox) para pagos
- **Resend** para correos (dominio verificado)
- **Dominio propio:** https://ascensopublico.com (SSL activo, DNS gestionado en **Cloudflare**)
- `next.config.mjs` ignora errores de TS/ESLint en build

## 4. Estructura del repo
```
plataforma/                · App Next.js (CORE, en producción)
  ├─ app/                  · landing (/), comprar, convocatorias, activar, login,
  │                          reset-password, perfil, perfil/[cursoId], guia/[id],
  │                          admin/*, api/webhooks/wompi, api/admin/*
  ├─ app/components/       · NavLanding, NivelTabs, ConvocatoriasGrid, ContadorCupos, ScrollReveal
  ├─ lib/                  · supabase, wompi, wompiApi, email, auth, format,
  │                          procesarPago, autocargarGuias
  ├─ supabase/             · schema.sql, seed-convocatorias.sql, migracion-progreso.sql
  ├─ public/               · fotos/ (convocatorias+fundador), brand/ (logos), seed-guias/ (17 guías)
  └─ SETUP.md, DESPLIEGUE.md
brand/                     · logos originales + brand/fotos (respaldo)
guias/                     · 17 guías HTML originales (fuente/respaldo)
biblioteca/biblioteca.json · fuente de verdad del catálogo de guías
prompts/                   · plantillas para automatización futura (generador guías/plan)
ARQUITECTURA-PLATAFORMA.md · PROYECTO-MAESTRO.md · PLAN-PROYECTO.md · ESTANDAR-TECNICO.md · PLANTILLA-GUIA.md
```

## 5. LO QUE YA ESTÁ HECHO Y FUNCIONANDO ✅

### Landing (`/`)
Migrada a Next.js. Convocatorias dinámicas desde Supabase, animaciones de scroll (ScrollReveal), responsive móvil, SEO + Open Graph + favicon + sitemap + robots. Hero, fundador (Julio César Deávila), nivel interactivo, FAQ, política de datos, WhatsApp flotante.

### Compra (`/comprar`)
Formulario con **Nombres + Apellidos separados** (normalización Title Case vía `lib/format.ts`), OPEC/cargo/nivel obligatorios, **contador de cupos** (100 de lanzamiento), pre-llena datos si el usuario está logueado (multi-curso). Sube manual PDF a Storage privado.

### Flujo de pago
`/comprar` → Wompi → **webhook** (`/api/webhooks/wompi`) → `procesarReferencia()` crea usuario + curso + auto-carga guías. Redirect a `/activar` (crear contraseña). `procesarReferencia` es **robusto ante usuarios residuales** (busca por email, evita duplicados por opec).

### Auto-carga de guías (`lib/autocargarGuias.ts`)
Al comprar se cargan automáticamente: **Intro (INTRO-00) + Generales (GEN-01/02/03) + las del Nivel** (ASI/TEC/PRO según `curso.nivel`) **+ Bonus (BON-01)**. Las **funcionales** (días 9-20) y el **simulacro** las sube el admin manualmente.

### Portal del estudiante (`/perfil`)
Multi-curso con **tarjetas hero** (imagen convocatoria + overlay navy + OPEC badge dorado + cargo en Title Case). `/perfil/[cursoId]` muestra la biblioteca por secciones (Plan / Bonus / Simulacro). **Progreso EN VIVO** (guías leídas / total; columna `leida` en `guias_curso`). Botones "Cambiar contraseña", "Comprar otro curso" y "Panel admin" (solo si rol=admin).

### Visor de guías (`/guia/[id]`)
Iframe que carga `/api/guia/[id]` (sirve el HTML desde Storage privado con URL firmada). Marca la guía como leída al abrir y recalcula el progreso.

### Panel admin (`/admin`)
Layout con sidebar (Dashboard, Cursos, Convocatorias, Usuarios).
- **`/admin/cursos/[id]`**: datos del cliente + manual PDF + guías auto-cargadas vs funcionales + subir guías + **dos botones**: "Curso listo" (se habilita a las 12h de la compra) y "Habilitar ahora" (acceso inmediato, para casos especiales).
- **`/admin/convocatorias`**: CRUD con campo `imagen_url`.
- **`/admin/usuarios`**: listar + eliminar usuarios (no admins).

### Auth
`/login` (con "¿Olvidaste tu contraseña?"), `/reset-password`, `middleware.ts` protege `/perfil` `/guia` `/admin` (excluye `/api/`).

### Correos (`lib/email.ts`)
Plantilla HTML profesional con **logo dorado + colores de marca** (encabezado navy, botón CTA, footer con WhatsApp). Confirmación al cliente + aviso al admin. Remitente `noreply@ascensopublico.com`.

### Endpoints admin útiles (se mantienen)
- `/api/admin/seed-guias` — sube las 17 guías HTML al bucket `guias` (solo admin, idempotente).
- `/api/admin/reprocesar?ref=XXX` — reprocesa un pago manualmente (herramienta de emergencia).

## 6. Datos / convenciones (NO cambiar sin avisar)
- **Tablas Supabase:** `profiles`, `convocatorias`, `preregistros`, `cursos`, `guias_curso`, `pagos`.
- **Guías:** las 17 HTML viven en `/guias` (repo) y en bucket privado `guias` de Storage. `biblioteca/biblioteca.json` es la fuente de verdad del catálogo.
- **Fotos:** `/plataforma/public/fotos`. **Logos:** `/plataforma/public/brand`.
- **Marca:** navy `#0A2A5E` · crema `#FBF9F4` · oro `#E8A33D`. Tipos: Source Serif 4 + Plus Jakarta Sans.
- **Contacto:** WhatsApp **573151972091** · correo **ascensopublico@gmail.com**.
- **Precio:** $300.000 COP, pago único. **Cupos de lanzamiento:** 100.
- **Niveles:** `asistencial` | `tecnico` | `profesional`.
- **Fundador:** Julio César Deávila.

## 7. Flujo de trabajo (IMPORTANTE)
- Trabajar en **ramas** y hacer push; el usuario mergea desde GitHub.
- ⚠️ Si la herramienta de **crear PR falla** ("No provider found"), mergear **directo a main** con git (el usuario lo autoriza expresamente).
- Tras cambiar variables en **Vercel**, recordar **redesplegar**.
- ⚠️ Vercel a veces solo toma el primer commit de una rama si se pushea **después** de abrir el PR: **verificar siempre** que los cambios lleguen a `main` (revisar el contenido en main, no solo el log).
- 🌐 El sandbox de Kiro tiene red **INTEGRATIONS_ONLY** (sin acceso directo a Supabase/Wompi): Kiro escribe/sube código; el usuario configura paneles externos.
- 🚫 Nada de testimonios/fotos/cifras inventadas. Solo datos reales.
- 🔒 Nunca exponer secretos (`service_role`, llaves privadas) en el repo.

## 8. Variables de entorno en Vercel (ya configuradas)
`NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`,
`NEXT_PUBLIC_WOMPI_PUBLIC_KEY`, `WOMPI_PRIVATE_KEY`, `WOMPI_INTEGRITY_SECRET`, `WOMPI_EVENTS_SECRET`,
`RESEND_API_KEY`, `ADMIN_EMAIL`, `NEXT_PUBLIC_SITE_URL` (=https://ascensopublico.com),
`NEXT_PUBLIC_WOMPI_REDIRECT_URL` (=https://ascensopublico.com/activar), `PRECIO_COP` (=300000).

## 9. PENDIENTES / ROADMAP (en pausa hasta que el usuario lo pida)
- **TESTIMONIOS:** tabla + admin + sección en landing. En pausa hasta tener reseñas reales (mantener oculto hasta que el usuario avise).
- **SIMULACRO FINAL:** módulo interactivo tipo CNSC (juicio situacional, repetible). Se construye **al final**, cuando un cargo tenga TODO el contenido (generales + nivel + funcionales). Es la pieza estrella.
- **AUTOMATIZACIÓN (Fase 3):** al comprar → IA lee el manual de funciones → genera el plan de estudio → reutiliza guías de la biblioteca que coincidan **100%** (mismo nivel + mismo tema) → genera las faltantes con las plantillas/políticas → las deja en estado "pendiente de revisión" → el admin revisa y publica. Requiere API de IA (costo por uso).
- **CHATBOT** de dudas sencillas en el portal del estudiante. Muy a futuro.
- **Vercel Pro** ($20/mes) cuando se venda formalmente (uso comercial). Correo profesional (`contacto@`) opcional.

## 10. Cómo quedó esta conversación
Sesión dedicada a: migrar landing a Next.js, rediseño del portal del estudiante (multi-curso, tarjetas hero, progreso), panel admin completo, login + recuperar contraseña, auto-carga de guías, contador de cupos, doble habilitación de curso, **conexión del dominio propio `ascensopublico.com`** (Vercel + Cloudflare), **correos profesionales con Resend** (dominio verificado), SEO + Open Graph + 404, responsive móvil, animaciones de scroll, y **limpieza** del repo (eliminada landing vieja, scripts duplicados y docs de investigación).

**Todo está mergeado en `main` y desplegado.** El siguiente módulo lo define el usuario (probablemente: contenido de guías funcionales de un cargo real, o el simulacro cuando haya contenido completo).
