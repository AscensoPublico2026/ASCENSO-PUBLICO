# 🔄 CONTINUIDAD DEL PROYECTO — Ascenso Público

> **Para retomar en una nueva sesión de Kiro:** conecta este repositorio y pídele a Kiro:
> *"Lee CONTINUIDAD.md y ARQUITECTURA-PLATAFORMA.md y continuemos donde quedamos."*

_Última actualización: 16 de junio de 2026 — cierre de sesión tras BON-02, automatización de asignación de guías por código, reorden del panel y guía "Conoce tu Entidad" (ENT-IDV-01). **Próximo paso: crear el SIMULACRO (SIM-001).**_

---

## 0. ESTADO ACTUAL (resumen para arrancar rápido)

- **Plataforma:** 100% en producción en https://ascensopublico.com. Todo mergeado en `main`.
- **Contenido de guías:** **31 guías publicadas** en la biblioteca, todas con el estándar profundo del motor:
  - INTRO-00 + Generales (GEN-01/02/03) + 12 por nivel (ASI/TEC/PRO) + 12 funcionales (FUN-*) + 2 bonus (BON-01 Estrategia CNSC, BON-02 Ofimática) + **ENT-IDV-01 (Conoce tu Entidad: INDERVALLE)**.
- **Flujo de armado de cursos:** el admin ya **asigna guías por código** desde desplegables (no sube HTML a mano). El panel del curso está **ordenado por el plan** (Día 1 + Conoce tu Entidad → generales/nivel → 12 funcionales → simulacro).
- **Prueba de compra:** hecha desde un perfil de prueba. Correos funcionan (al cliente ✅). **PENDIENTE (acción del usuario):** el aviso al admin llega a `cesardeavilamartinez@gmail.com`; hay que cambiar la variable `ADMIN_EMAIL` en Vercel a `ascensopublico@gmail.com` y **redesplegar** (es solo configuración, el código está bien).
- **➡️ PRÓXIMO PASO (se hará en una nueva sesión): crear el SIMULACRO `SIM-001`** para el cargo de prueba (INDERVALLE, Técnico Operativo 314-03, Almacén), hacer pruebas de cómo se ve y **definir su diseño/estructura como plantilla de TODOS los simulacros** (igual que se hizo con las guías y con "Conoce tu Entidad").

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
  ├─ lib/                  · supabase, wompi, wompiApi, email, auth, format, procesarPago,
  │                          autocargarGuias, catalogoGuias (+ biblioteca.json copia)
  ├─ supabase/             · schema.sql, seed-convocatorias.sql, migracion-progreso.sql
  ├─ public/               · fotos/, brand/, seed-guias/ (31 guías publicadas, HTML servido estático)
  └─ SETUP.md, DESPLIEGUE.md
brand/                     · logos originales + brand/fotos (respaldo)
guias/                     · 31 guías HTML codificadas (INTRO, GEN, nivel, 12 FUN-*, BON-01/02, ENT-IDV-01)
biblioteca/biblioteca.json · FUENTE DE VERDAD del catálogo (se copia a plataforma/lib/ con scripts/sync-biblioteca.sh)
motor/                     · motor data-driven: base-guia.html + construir_guia.py + contenido/*.json (genera el HTML de las guías)
referencias/               · insumos de contenido (ej. ofimatica-banco-preguntas.md para BON-02)
prompts/                   · generador-plan-estudio.md (v3) + generador-guias.md (v2.1) — prompts portables a cualquier IA
scripts/                   · sync-biblioteca.sh (copia catálogo + HTML a la plataforma), utilidades
ARQUITECTURA-PLATAFORMA.md · PROYECTO-MAESTRO.md · PLAN-PROYECTO.md · ESTANDAR-TECNICO.md · PLANTILLA-GUIA.md
```

## 5. LO QUE YA ESTÁ HECHO Y FUNCIONANDO ✅

### Landing (`/`)
Migrada a Next.js. Convocatorias dinámicas desde Supabase, ScrollReveal, responsive, SEO + Open Graph + favicon + sitemap + robots. Hero, fundador (Julio César Deávila), nivel interactivo, FAQ, política de datos, WhatsApp flotante.

### Compra (`/comprar`) y pago
Formulario con Nombres+Apellidos separados (Title Case vía `lib/format.ts`), OPEC/cargo/nivel obligatorios, contador de cupos (100), pre-llena si está logueado (multi-curso), sube manual PDF a Storage. Flujo: `/comprar` → Wompi → webhook (`/api/webhooks/wompi`) → `procesarReferencia()` crea usuario + curso + auto-carga guías → `/activar`. Robusto ante usuarios residuales.

### Auto-carga de guías (`lib/autocargarGuias.ts`)
Al comprar se cargan automáticamente: **INTRO-00 + Generales (GEN-01/02/03) + las del Nivel** (ASI/TEC/PRO según `curso.nivel`) **+ Bonus (BON-01, BON-02)**. Las **funcionales, el simulacro y "Conoce tu Entidad"** NO se auto-cargan: las asigna el admin por código (ver abajo).

### Asignar guías de la biblioteca por código (`lib/catalogoGuias.ts`)
El admin, en `/admin/cursos/[id]`, asigna guías publicadas **por código** desde desplegables (sin subir HTML); la guía queda cargada referenciando el HTML que ya vive en el bucket `guias`. Helpers del catálogo: `guiasFuncionalesAsignables`, `guiasSimulacroAsignables`, `guiasEntidadAsignables`, `esRutaEntidad`.
- Fuente de verdad: `biblioteca/biblioteca.json` → copia en `plataforma/lib/biblioteca.json`.
- **Al agregar/crear una guía nueva:** correr `scripts/sync-biblioteca.sh` (copia catálogo + HTML a la plataforma) y visitar `/api/admin/seed-guias` (admin) para subir el HTML al bucket (idempotente; sube TODAS las publicadas, 31 hoy).

### Panel admin del curso ordenado por el plan (`/admin/cursos/[id]`)
Secciones en orden: **📅 Día 1 (Presentación + desplegable "Conoce tu Entidad" → solo guías ENT-*)** · **📚 Generales y por nivel (auto)** · **📝 Guías funcionales (x/12, desplegable)** · **🎯 Simulacro (desplegable)** · **⬆️ Subir HTML personalizado (fallback)**. Más: datos del cliente, manual PDF, y botones "Curso listo" (12h) / "Habilitar ahora".

### Portal del estudiante (`/perfil`, `/perfil/[cursoId]`)
Multi-curso con tarjetas hero; biblioteca por secciones (Plan / Bonus / Simulacro); progreso EN VIVO (columna `leida` en `guias_curso`). Visor `/guia/[id]` (iframe → `/api/guia/[id]` con URL firmada), marca leída al abrir.

### Auth y correos
`/login` (+ recuperar contraseña), `/reset-password`, `middleware.ts` protege `/perfil` `/guia` `/admin`. Correos (`lib/email.ts`) con plantilla de marca: confirmación al cliente (✅ funciona) + aviso al admin (a `ADMIN_EMAIL`). Remitente `noreply@ascensopublico.com`.

### Endpoints admin
- `/api/admin/seed-guias` — sube TODAS las guías publicadas (derivadas del catálogo) al bucket `guias`.
- `/api/admin/reprocesar?ref=XXX` — reprocesa un pago manualmente.


## 6. Datos / convenciones (NO cambiar sin avisar)
- **Tablas Supabase:** `profiles`, `convocatorias`, `preregistros`, `cursos`, `guias_curso`, `pagos`. Enum `tipo_guia`: `general | nivel | funcional | bonus | simulacro`.
- **Guías:** las 31 publicadas viven en `/guias` (repo), se copian a `plataforma/public/seed-guias/` y se suben al bucket privado `guias`. `biblioteca/biblioteca.json` es la fuente de verdad (copia en `plataforma/lib/biblioteca.json`).
- **Fotos:** `/plataforma/public/fotos`. **Logos:** `/plataforma/public/brand`.
- **Marca:** navy `#0A2A5E` · crema `#FBF9F4` · oro `#E8A33D`. Tipos: Source Serif 4 + Plus Jakarta Sans.
- **Contacto:** WhatsApp **573151972091** · correo **ascensopublico@gmail.com**.
- **Precio:** $300.000 COP, pago único. **Cupos de lanzamiento:** 100.
- **Niveles:** `asistencial` | `tecnico` | `profesional`. **Fundador:** Julio César Deávila.

## 7. Flujo de trabajo (IMPORTANTE)
- Trabajar en **ramas** y hacer push; el usuario mergea desde GitHub. **Preferencia del usuario:** enviarle el **link directo** para mergear (`.../pull/new/<rama>`), sin pasos intermedios.
- ⚠️ La herramienta de **crear PR falla** ("No provider found") — es esperado: pasar el link directo de la rama y el usuario crea/mergea el PR.
- Para **previsualizar una guía renderizada** sin merge: ponerla en `plataforma/public/seed-guias/` y usar la URL de **Preview de Vercel** + `/seed-guias/NOMBRE.html` (se sirve estática). En producción: `https://ascensopublico.com/seed-guias/NOMBRE.html`.
- Tras cambiar variables en **Vercel**, recordar **redesplegar**.
- 🌐 El sandbox de Kiro tiene red **OPEN_INTERNET** pero **sin acceso directo a Supabase/Wompi/Vercel**: Kiro escribe/sube código; el usuario configura paneles externos.
- 🛠️ **Truco de git en el sandbox:** el clon es *shallow* y `git fetch` directo falla (auth solo por las herramientas MCP de GitHub: `pull_repository`, `push_to_remote`). Para mergear ramas localmente puede tocar `git replace --graft` por el borde shallow (ya resuelto antes).
- 🚫 Nada de testimonios/fotos/cifras inventadas. Solo datos reales. 🔒 Nunca exponer secretos en el repo.

## 8. Variables de entorno en Vercel (ya configuradas)
`NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`,
`NEXT_PUBLIC_WOMPI_PUBLIC_KEY`, `WOMPI_PRIVATE_KEY`, `WOMPI_INTEGRITY_SECRET`, `WOMPI_EVENTS_SECRET`,
`RESEND_API_KEY`, **`ADMIN_EMAIL`** (⚠️ revisar: debe ser `ascensopublico@gmail.com`), `NEXT_PUBLIC_SITE_URL` (=https://ascensopublico.com),
`NEXT_PUBLIC_WOMPI_REDIRECT_URL` (=https://ascensopublico.com/activar), `PRECIO_COP` (=300000).

## 9. IDEAS, PROPUESTAS Y DECISIONES (contexto conceptual — leer antes de continuar)

### 9.1 Portabilidad: el proyecto NO depende de ninguna IA en particular ✅ (decisión clave)
El "cómo se hacen las cosas" vive en **documentos + el motor**, no en el asistente. Para no quedar amarrado a Kiro:
- **`prompts/generador-plan-estudio.md` (v3):** recibe OPEC + manual de funciones y devuelve (1) la **tabla del plan de 21 días** con columna **Estado** (✅ Reusar / 🆕 Crear) y (2) **fichas de contenido** por cada guía a crear, en el formato exacto que espera el generador de guías (temario expandido: subtemas, normas a citar, ejemplos por entidad, qué evalúa la CNSC).
- **`prompts/generador-guias.md` (v2.1, documento vivo con changelog):** recibe la ficha de una guía y devuelve el HTML completo con el estándar.
- **`motor/`:** el diseño está **congelado en código** (`base-guia.html` + `construir_guia.py`); la IA solo rellena un JSON de contenido (`motor/contenido/CODIGO.json`) y el script genera el HTML. Así el diseño NUNCA se rompe al cambiar de IA.
- **Flujo portable completo:** plan → fichas → generar cada guía → guardar en `guias/` → registrar en `biblioteca.json` → `scripts/sync-biblioteca.sh` → `/api/admin/seed-guias` → asignar por código en el panel.

### 9.2 "Conoce tu Entidad" (ENT-*) — PLANTILLA DEFINIDA ✅
`ENT-IDV-01` (INDERVALLE) es el **molde oficial** de todas las guías de entidad. Decisión del usuario: es una **bienvenida institucional GENERAL y rica en información de la entidad**, NO interactiva (sin quiz/trampas/comparaciones), y **sirve para cualquier nivel/cargo de esa entidad** (no menciona OPEC ni cargo). Secciones: Bienvenida · Identidad · Qué hace · En detalle · Marco legal · Organización (misional + apoyo) · Para tu prueba · Cierre. Diseño con la marca (navy/crema/oro). Para otra entidad: reemplazar solo los textos, mantener estructura/estilo.

### 9.3 SIMULACRO (SIM-*) — PRÓXIMO PASO 🔜
- Es la **pieza estrella**. Se construye cuando el cargo ya tiene todo el contenido (generales + nivel + funcionales). Tipo **juicio situacional** (igual estándar que el simulacro de las funcionales: contexto largo + enunciado + 4 opciones plausibles, feedback por opción, puntaje + temas a reforzar, repetible, opciones barajadas).
- **Se generará a partir del contenido de las guías del plan** del cliente (sabemos qué cubre cada guía).
- **Es único por OPEC, pero se GUARDA para reutilizar:** si llega otra compra de la misma OPEC, no se rehace — se carga el ya creado.
- En la nueva sesión: crear `SIM-001` para el cargo de prueba, **probar cómo se ve, ajustar y CONGELAR su diseño/estructura como plantilla de todos los simulacros**.

### 9.4 "Biblioteca por OPEC" — PROPUESTA (Fase 2, requiere luz verde + migración del usuario)
Idea del usuario: que al recibir una compra de una **OPEC ya trabajada antes**, el curso se arme **solo** (sin volver a crear ni asignar guía por guía). Diseño propuesto por Kiro:
- **2 tablas nuevas en Supabase:** `plantillas_opec` (opec, nivel, cargo, created_at) y `plantillas_opec_guias` (opec, titulo, dia, tipo, orden, archivo_path).
- **Botón "Guardar como plantilla de esta OPEC"** (guarda la "receta" del curso armado) y **"Cargar plantilla de la OPEC"** (arma el curso de una).
- **Flujo:** OPEC nueva → se arma manual y se guarda como plantilla; OPEC repetida → se carga todo y el admin solo aprueba/habilita.
- **Decisiones pendientes con el usuario:** (a) ¿clave por OPEC (recomendado) o por cargo+nivel?; (b) ¿aplicar plantilla **automático** al comprar o **avisar** antes? Requiere que el usuario aplique la migración SQL en Supabase.

### 9.5 AUTOMATIZACIÓN total (Fase 3, futuro)
Al comprar → IA lee el manual → genera el plan (con `generador-plan-estudio.md`) → reutiliza guías 100% coincidentes → genera las faltantes (con `generador-guias.md` + motor) → quedan "pendiente de revisión" → admin publica. Requiere API de IA (costo por uso).

### 9.6 Otros pendientes (en pausa)
- **TESTIMONIOS:** tabla + admin + sección landing. Oculto hasta tener reseñas reales.
- **CHATBOT** de dudas en el portal. Muy a futuro.
- **Vercel Pro** ($20/mes) al vender formalmente. Correo profesional (`contacto@`) opcional.

### 9.7 Pendientes de CONFIGURACIÓN (acción del usuario en paneles externos)
- **Correos de Auth (Supabase) sin marca:** el correo de "recuperar contraseña" llega con marca/datos de **Supabase** (no de Ascenso Público) porque usa el SMTP y las plantillas por defecto de Supabase. **Fix (en el dashboard de Supabase):**
  1. Auth → **SMTP Settings** → habilitar **Custom SMTP** con Resend: host `smtp.resend.com`, puerto 465 (o 587), usuario `resend`, contraseña = `RESEND_API_KEY`, **sender** `noreply@ascensopublico.com`, nombre "Ascenso Público".
  2. Auth → **Email Templates** → personalizar "Reset Password" (y Confirm signup, Magic Link) con la marca y textos en español.
  Así TODOS los correos de auth saldrán de Ascenso Público. (No requiere cambio de código.)
- **`ADMIN_EMAIL` en Vercel** = `ascensopublico@gmail.com` + **redeploy** (el aviso de compra está saliendo a otro correo).
- **Todas las cuentas bajo `ascensopublico@gmail.com`:** verificar/migrar la titularidad o notificaciones de GitHub, Vercel, Supabase, Resend, Cloudflare, registrador del dominio y Wompi a ese correo. (Acción del usuario en cada panel.)
- **Orden del portal del estudiante:** confirmado **Plan → 🎁 Bonus → 📝 Simulacro Final** (los bonus van ANTES del simulacro; el simulacro cierra como gran final). Para enriquecer bonus: agregar más `BON-*` (se auto-cargan y se ordenan por `orden`).

## 10. Cómo quedó esta sesión
- ✅ **BON-02 (Ofimática)** creada (basada en `referencias/ofimatica-banco-preguntas.md`) y auto-cargada como bonus.
- ✅ **Asignación de guías por código** + **panel del curso reordenado** por el plan (Día 1/Entidad → generales/nivel → funcionales → simulacro) + seed de las 31 publicadas + `scripts/sync-biblioteca.sh`.
- ✅ **`generador-plan-estudio.md` v3** (tabla con Estado + fichas de contenido listas para pegar → portable a cualquier IA).
- ✅ **Plan de estudio generado** para el cargo de prueba (INDERVALLE Téc. Operativo 314-03, Almacén): las 12 funcionales YA existían (este fue el cargo modelo); solo faltan crear **ENT-IDV-01** (hecha) y **SIM-001** (próximo).
- ✅ **ENT-IDV-01 "Conoce tu Entidad: INDERVALLE"** creada, generalizada y publicada (molde de todas las ENT-*).
- ✅ **Limpieza** del repo (sin HTML huérfanos en la raíz).
- ⚠️ Pendiente del usuario: corregir `ADMIN_EMAIL` en Vercel (aviso de compra debe ir a `ascensopublico@gmail.com`) y redesplegar.

**Todo está mergeado en `main` y desplegado.** ➡️ **PRÓXIMO PASO (nueva sesión): crear el SIMULACRO `SIM-001` y congelar su diseño como plantilla.** Luego, si el usuario da luz verde, construir la "Biblioteca por OPEC" (§9.4).
