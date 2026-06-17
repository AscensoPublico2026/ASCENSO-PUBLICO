# 🔄 CONTINUIDAD DEL PROYECTO — Ascenso Público

> **Para retomar en una nueva sesión de Kiro:** conecta este repositorio y pídele a Kiro:
> *"Lee CONTINUIDAD.md y continuemos donde quedamos."*
>
> ⭐ **`CONTINUIDAD.md` es el ÚNICO documento de ESTADO al día y la fuente de verdad.** Si cualquier otro archivo (README, ARQUITECTURA, etc.) parece contradecirlo, **manda este**.

_Última actualización: 17 de junio de 2026 — **SIM-001 creado y CONGELADO como plantilla oficial de simulacros, + MOTOR de simulacros data-driven construido.** Simulacro final de 50 preguntas tipo CNSC (juicio situacional) para INDERVALLE Técnico Operativo 314-03 (Almacén): contexto + dilema + 4 opciones + modo examen real (responder todo → presentar → resultados con revisión pregunta por pregunta y guía de refuerzo). Ya existe `simulacro/motor/` + `simulacro/bancos/` (molde + bancos reutilizables + receta por curso + builder con validación), igual al motor de guías. **Próximo paso: armar simulacros de nuevos cursos eligiendo bancos + escribiendo solo las funcionales del cargo.**_

---

## 0. ESTADO ACTUAL (resumen para arrancar rápido)

- **Plataforma:** 100% en producción en https://ascensopublico.com. Todo mergeado en `main`.
- **Contenido de guías:** **31 guías publicadas** en la biblioteca, todas con el estándar profundo del motor:
  - INTRO-00 + Generales (GEN-01/02/03) + 12 por nivel (ASI/TEC/PRO) + 12 funcionales (FUN-*) + 2 bonus (BON-01 Estrategia CNSC, BON-02 Ofimática) + **ENT-IDV-01 (Conoce tu Entidad: INDERVALLE)**.
- **Flujo de armado de cursos:** el admin ya **asigna guías por código** desde desplegables (no sube HTML a mano). El panel del curso está **ordenado por el plan** (Día 1 + Conoce tu Entidad → generales/nivel → 12 funcionales → simulacro).
- **Prueba de compra y correos:** funcionando. Correo al cliente ✅, aviso de compra al admin a `ascensopublico@gmail.com` ✅, y **recuperación de contraseña** con marca (SMTP Resend + plantilla en español + fix del flujo PKCE) ✅. Único pendiente opcional: registro **DMARC** para mejorar entregabilidad (ver §9.7).
- **✅ SIMULACRO `SIM-001` CREADO Y CONGELADO** como **plantilla oficial de todos los simulacros** (igual que se hizo con las guías y con "Conoce tu Entidad"). Archivo: `simulacro/SIM-001.html`.
  - **50 preguntas** de juicio situacional tipo CNSC para el cargo de prueba (INDERVALLE, Técnico Operativo 314-03, Almacén).
  - **Distribución:** 6 Generales + 6 Nivel Técnico + **32 Funcionales Almacén (FUN-ALM-01 a 07)** + 5 Otras Funcionales (DOC/MIPG/OFI/PRO/ATC) + 1 Ofimática (BON-02).
  - **Formato CNSC:** contexto (Caso) + párrafo de dilema que incita la decisión + 4 opciones plausibles. Pregunta integrada, NO académica.
  - **Modo examen real:** se responde todo sin ver aciertos → botón "Presentar examen" → resultados con puntaje, %, **revisión pregunta por pregunta** (tu respuesta vs. correcta + explicación breve) y **guía de refuerzo** que remite a la guía del curso donde estudiar cada tema fallado.
  - Opciones barajadas en cada intento; incluye una pregunta de cálculo (promedio ponderado) tipo MBE.
  - **Diseño congelado:** Inter + Crimson Pro, marca navy/gold, único y profesional (no copia de las guías funcionales).
- **✅ MOTOR DE SIMULACROS con BANCOS reutilizables** (`simulacro/motor/` + `simulacro/bancos/`): molde congelado `base-simulacro.html` + **bancos de preguntas reutilizables** + receta por curso en `contenido/<CODIGO>.json` + `construir_simulacro.py` (ensambla bancos + funcionales del cargo, con validación) + `construir_todos.py`.
  - **Bancos:** `generales` (todos los cargos/niveles), `nivel-asistencial`/`nivel-tecnico`/`nivel-profesional` (por nivel; ASI y PRO son semillas vacías por llenar), `ofimatica`, `funcionales-comunes` (DOC/MIPG/OFI/PRO/ATC).
  - **Receta SIM-001:** ensambla `generales(6) + nivel-tecnico(6) + ofimatica(1) + funcionales-comunes(5)` reutilizables **+ 32 funcionales del cargo (FUN-ALM)** = 50.
- **➡️ PRÓXIMO PASO sugerido:** para un curso nuevo, copiar una receta, elegir los bancos según el nivel del cargo y escribir SOLO las `funcionales` del cargo; luego `python3 motor/construir_simulacro.py contenido/<CODIGO>.json`. Si es de nivel Asistencial o Profesional, primero llenar el banco de ese nivel (una sola vez).

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
ARQUITECTURA-PLATAFORMA.md · ESTANDAR-TECNICO.md · PLANTILLA-GUIA.md   (CONTINUIDAD.md = fuente de verdad del estado; PROYECTO-MAESTRO.md y PLAN-PROYECTO.md se eliminaron por estar desactualizados)
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

### 9.7 Correos y recuperación de contraseña (estado y config)
- ✅ **Custom SMTP con Resend** en Supabase (Auth → SMTP): host `smtp.resend.com`, puerto 465, **usuario `resend`**, password = API key `re_...`, remitente `noreply@ascensopublico.com` ("Ascenso Público"). Todos los correos de Auth salen con la marca.
- ✅ **Plantilla "Reset Password"** personalizada (HTML de marca, en español) en Supabase → Auth → Email Templates.
- ✅ **URL Configuration** (Supabase → Auth): Site URL `https://ascensopublico.com`; Redirect URLs `https://ascensopublico.com/reset-password` y `/**`. (Sin esto el enlace caía a la home.)
- ✅ **Fix de código `/reset-password`** (mergeado, PR #78): canjea el `?code=` del flujo PKCE de Supabase (`exchangeCodeForSession`); antes se quedaba en "Verificando…". El disparo está en `app/login/page.tsx` (`resetPasswordForEmail` con `redirectTo` a `/reset-password`).
- ✅ **Aviso de compra al admin** llega a `ascensopublico@gmail.com` (`ADMIN_EMAIL` en Vercel).
- ⏳ **Pendiente (config, opcional):** (a) **DMARC** en Cloudflare (TXT `_dmarc` = `v=DMARC1; p=none; rua=mailto:ascensopublico@gmail.com`) para mejorar entregabilidad/evitar spam; (b) uniformar las otras plantillas de Auth (Confirm signup / Magic Link) con la misma marca; (c) verificar que todas las cuentas externas (GitHub, Vercel, Supabase, Resend, Cloudflare, dominio, Wompi) estén bajo `ascensopublico@gmail.com`.
- ℹ️ Si en el correo aparece un enlace crudo al final, es una segunda `{{ .ConfirmationURL }}` sobrante en la plantilla; debe haber solo una (la del botón).

## 10. Cómo quedó esta sesión
- ✅ **BON-02 (Ofimática)** creada (basada en `referencias/ofimatica-banco-preguntas.md`) y auto-cargada como bonus.
- ✅ **Asignación de guías por código** + **panel del curso reordenado** por el plan (Día 1/Entidad → generales/nivel → funcionales → simulacro) + seed de las 31 publicadas + `scripts/sync-biblioteca.sh`.
- ✅ **`generador-plan-estudio.md` v3** (tabla con Estado + fichas de contenido listas para pegar → portable a cualquier IA).
- ✅ **Plan de estudio generado** para el cargo de prueba (INDERVALLE Téc. Operativo 314-03, Almacén): las 12 funcionales YA existían (este fue el cargo modelo); solo faltan crear **ENT-IDV-01** (hecha) y **SIM-001** (próximo).
- ✅ **ENT-IDV-01 "Conoce tu Entidad: INDERVALLE"** creada, generalizada y publicada (molde de todas las ENT-*).
- ✅ **Limpieza** del repo (sin HTML huérfanos en la raíz).
- ✅ **Correos y recuperación de contraseña** resueltos de punta a punta: Custom SMTP con Resend, plantilla de marca en español, Site/Redirect URLs, fix del flujo PKCE en `/reset-password` (mergeado) y aviso de compra al admin a `ascensopublico@gmail.com`. Detalle y pendientes en §9.7.

**Todo está mergeado en `main` y desplegado.** ➡️ **PRÓXIMO PASO (nueva sesión): crear el SIMULACRO `SIM-001` y congelar su diseño como plantilla.** Luego, si el usuario da luz verde, construir la "Biblioteca por OPEC" (§9.4).
