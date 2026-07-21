# 🔄 CONTINUIDAD DEL PROYECTO — Ascenso Público

> **Para retomar en una nueva sesión de Kiro:** conecta este repositorio y pídele a Kiro:
> *"Lee CONTINUIDAD.md y continuemos donde quedamos."*
>
> ⭐ **`CONTINUIDAD.md` es el ÚNICO documento de ESTADO al día y la fuente de verdad.** Si cualquier otro archivo (README, ARQUITECTURA, etc.) parece contradecirlo, **manda este**.

_Última actualización: 22 de junio de 2026 — **Feature "Simulacro Gratis" (lead magnet) construida en rama `feature/simulacro-gratis` + LIMPIEZA del repositorio.** Ver "## CAMBIOS RECIENTES" abajo. **Próximo paso: verificar las preguntas borrador del simulacro gratis, aplicar la migración SQL, mergear; y seguir con contenido + marketing en TikTok para vender.**_

---

## 🆕 CAMBIOS RECIENTES (sesión 22 jun 2026)

**Feature "Simulacro Gratis" (imán de leads para TikTok) — en rama `feature/simulacro-gratis`, PENDIENTE de merge:**
- ✅ **3 simulacros gratis por nivel** (asistencial / técnico / profesional), **20 preguntas cada uno**, en el **mismo formato HTML congelado del SIM-001** (molde, "modo examen real", revisión pregunta por pregunta y guía de refuerzo).
- ✅ **Composición = solo guías GENERALES + guías del NIVEL** (10 + 10), **entidad-neutras** (no nombran ninguna entidad ni cargo). Sin ofimática ni funcionales.
- ✅ **Motor propio del gratis:** molde `simulacro/motor/base-simulacro-gratis.html` (con "puerta" de captura de correo integrada al diseño) + `simulacro/motor/construir_gratis.py` + bancos `simulacro/bancos/gratis-generales|gratis-asistencial|gratis-tecnico|gratis-profesional.json` + recetas `simulacro/contenido/SIM-GRATIS-ASI|TEC|PRO.json`. Regenerar con `cd simulacro && python3 motor/construir_gratis.py`. Salida estática: `plataforma/public/simulacro-gratis/{asistencial,tecnico,profesional}.html`.
- ✅ **Captura de lead con consentimiento** (correo requerido + WhatsApp opcional + casilla de marketing desmarcada, Ley 1581): API `plataforma/app/api/simulacro/lead/route.ts` → guarda en tabla **`leads_simulacro`** (service role) y envía `correoResultadoSimulacro` (en `lib/email.ts`).
- ✅ **Landing:** franja clara dorada "Empieza con tu simulacro gratis" arriba (tras la barra de confianza) + selector en `/simulacro` + enlace en el nav.
- ⚠️ **PENDIENTE para publicar:** (1) **verificar las 60 preguntas BORRADOR** (marcadas `"_verificar": true` en los bancos `gratis-*`), en especial las técnico-legales (derecho de petición, régimen disciplinario, órganos de control, datos personales); (2) **aplicar la migración** `plataforma/supabase/migracion-simulacro.sql` en Supabase (SQL Editor → Run); (3) **mergear** la rama a `main`.

**🧹 LIMPIEZA del repositorio (esta sesión):**
- Borrados los borradores/versiones viejas del simulacro: `SIM-001-demo-v2.html`, `SIM-001-v3.html`, `SIM-001-v4.html`, `SIM-001-v5.html` (queda solo el final `simulacro/SIM-001.html`).
- Borrados scripts de un solo uso: `simulacro/generar_demo.py`, `simulacro/generar_v3_completo.sh`.
- Borrado `DISENO-SIMULACRO-SIM-001.md` (diseño histórico superado; el diseño vivo está congelado en el molde + `simulacro/motor/README.md` + §9.3). Recuperable desde el historial de git si se necesita.
- Borrada la caché `simulacro/motor/__pycache__/`.

---

## 🆕 CAMBIOS RECIENTES (sesión 17 jun 2026 — tarde)

**Lanzamiento / pagos:**
- ✅ **Primera compra real validada de punta a punta** (Wompi en PRODUCCIÓN, `pub_prod_`/`prv_prod_`; `PRECIO_COP=300000`). Para pruebas baratas se baja `PRECIO_COP` temporalmente (ej. 2000) y se vuelve a 300000.
- ✅ **Vista de pagos** `/admin/pagos`: cada pago aprobado con su cliente/cargo/OPEC, monto correcto (el `monto` se guarda en **centavos** → se divide /100), respaldo por preregistro, marca **(huérfano)** y **botón Eliminar** (acción `eliminarPago`). El stat del dashboard enlaza aquí.
- ✅ **`/activar` robusto:** si `getTransaction` falla (p. ej. `WOMPI_PRIVATE_KEY` de otro entorno) pero el webhook ya procesó el pago, igual activa (busca el pago aprobado por `wompi_transaction_id`/referencia) y **se auto-recarga cada 6s**. ⚠️ Recordatorio: el webhook (URL de eventos en Wompi producción) debe apuntar a `https://ascensopublico.com/api/webhooks/wompi`.

**Notificaciones:**
- ✅ **Correo al cliente cuando se habilita el curso** (`correoCursoListo` en `lib/email.ts`), disparado en `marcarCursoListo` y `habilitarCursoAhora`. Si aún faltan las 12h, el correo indica la **hora exacta** de disponibilidad; si ya está disponible, invita a estudiar. No reenvía si ya estaba disponible.

**Landing / UX:**
- ✅ **WhatsApp** centralizado en `lib/contacto.ts` con **número oficial `573170905177`** y **redes** (`REDES`: TikTok/Instagram) enlazadas en el footer.
- ✅ **Contador "177/200 cupos vendidos"** centralizado en `plataforma/lib/cupos.ts` y compartido por la landing y `/comprar`; muestra 23 cupos restantes.
- ✅ **Botones del nav** con texto nítido (no heredan el gris de los enlaces).
- ✅ **Flujo "Cómo funciona"** reordenado al flujo real (datos+manual → pagar → armamos ruta → estudiar).
- ✅ **Compromiso de tiempo de estudio** comunicado en landing (recuadro en "Cómo funciona" + FAQ) y en el curso (tarjeta "Tu ruta de estudio"): **1 a 1½ h/día, guías de 60–90 min, lunes a viernes, 20 días + simulacro** (NO decir "3 semanas").
- ✅ Footer: enlaces a **/privacidad** y **/terminos** (antes apuntaban a `#datos`).

**Admin:**
- ✅ Ficha del cliente y lista de cursos muestran **OPEC + Entidad**.
- ✅ **Editar nombre** de usuario/admin en `/admin/usuarios` (acción `actualizarNombreUsuario`).
- ✅ **Detección automática de OPEC ya preparado:** si existe otro curso del mismo OPEC con funcionales, banner verde "Generar curso automáticamente" (copia el plan); si es el primero, avisa que se arma a mano.
- ✅ Convocatorias: imagen por **subida a bucket `imagenes`** (público, opcional de crear), **elegir una ya cargada** (desplegable `/fotos`) o **URL**.
- ✅ **Botón flotante de WhatsApp "¿Dudas?"** dentro del curso del estudiante.

**Herramientas:**
- ✅ **Checklist interactivo** servido en `https://ascensopublico.com/checklist-pruebas.html` (marca OK/Falla, guarda progreso, copia reporte de fallas). Plan también en `PRE-LANZAMIENTO-PRUEBAS.md`.
- ✅ **Reset password** soporta flujo `token_hash` (cross-device). Requiere plantilla de Supabase con `{{ .SiteURL }}/reset-password?token_hash={{ .TokenHash }}&type=recovery` (ya configurada).

**Documentos de continuidad creados (esta sesión):**
- `prompts/CONTINUIDAD-GENERACION.md` — para retomar la **generación de plan + guías** de un cargo en una sesión nueva.
- `prompts/CONTINUIDAD-DESARROLLO.md` — para retomar **ajustes/mejoras** de la plataforma en una sesión nueva.

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
- **✅ DESBLOQUEO DEL SIMULACRO (plataforma):** el simulacro de un curso queda **bloqueado hasta que el estudiante completa (lee) todas las guías del PLAN con archivo** (generales/nivel/funcionales). El **bonus NO es obligatorio** y el propio simulacro no se cuenta. Implementado en `plataforma/app/perfil/[cursoId]/page.tsx` (tarjeta "🔒 Simulacro bloqueado" con progreso N/total) y en `plataforma/app/guia/[id]/page.tsx` (bloqueo server-side del acceso directo por URL; no marca leída ni muestra el iframe si está bloqueado). Esto da margen de tiempo (días, por el plan de 21 días) para construir y publicar el simulacro del curso después del lanzamiento.
- **✅ SIM-001 REGISTRADO EN EL CATÁLOGO (seleccionable, no se sube a mano):** en `biblioteca/biblioteca.json` (y su copia `plataforma/lib/biblioteca.json`) SIM-001 quedó `estado:"publicada"` + `archivo:"guias/SIM-001.html"`, y su HTML está en `plataforma/public/seed-guias/SIM-001.html`. Así el admin lo **asigna por código desde el desplegable** de simulacro (`guiasSimulacroAsignables`), igual que las guías. `scripts/sync-biblioteca.sh` ahora también copia los simulacros finales (`simulacro/SIM-NNN.html`) a `seed-guias`.
- **✅ CARGA AUTOMÁTICA DE GUÍAS AL BUCKET (auto-sanación):** el visor `plataforma/app/api/guia/[id]/route.ts` ahora, si el HTML no está en el bucket, lo toma de `public/seed-guias/` y lo sube solo la primera vez que se abre. **Ya NO hay que correr `/api/admin/seed-guias` a mano** cuando se publica una guía nueva (ese endpoint queda como utilidad de carga masiva, opcional). El dominio quedó centralizado en `plataforma/lib/site.ts` (`SITE_URL`), usado por el visor, el seed, los correos (`email.ts`) y Wompi (`wompi.ts`) — sin dominios viejos regados.
- **✅ INTERFAZ DEL ESTUDIANTE MEJORADA (estilo currículo):** la vista del curso (`plataforma/app/perfil/[cursoId]/page.tsx`) ahora agrupa las guías en **módulos colapsables** (Introducción, Conocimientos Generales, Competencias por Nivel, Funciones del Cargo, Bonus, Simulacro) con progreso por módulo, indicador "DÍA n" legible, estado por guía (Comenzar/Completada) y acordeón (`<details>`). El **progreso de la tarjeta** en `/perfil` se calcula EN VIVO desde las guías leídas (ya no se queda en 0%). Estilos en `globals.css` (`.modulo`, `.guia-row`, `.curso-card-hover`).
- **✅ REUTILIZACIÓN DEL PLAN POR OPEC:** al comprar, si ya existe otro curso del **mismo OPEC** con el plan armado (con funcionales), se **copian automáticamente todas sus guías** (funcionales + "Conoce tu Entidad" + simulacro + genéricas) al curso nuevo, sin duplicar (`plataforma/lib/autocargarGuias.ts` → `copiarPlanDesdeOPEC`, conectado en `procesarPago.ts`). Si no hay un curso fuente, se cargan solo las genéricas como antes. Además, el panel admin tiene el botón **"⚡ Copiar plan de otro curso del mismo OPEC"** (`copiarPlanOPEC`) para cursos ya creados. Así, el primer comprador de un OPEC se arma a mano una vez y los siguientes quedan listos solos.
- **✅ LANDING + WHATSAPP:** el hero ahora usa una **imagen de fondo** (`plataforma/public/fotos/hero.jpg`, con overlay navy para legibilidad) — basta reemplazar ese archivo por una foto de personas celebrando (también es la imagen OG al compartir). WhatsApp centralizado en `plataforma/lib/contacto.ts` (`WHATSAPP_NUMERO`, `waUrl()`, `WA_MENSAJES`) y enlazado en: botón "Asesoría por WhatsApp" del hero, nota de garantía, "Escríbenos" de convocatorias, footer, botón flotante, not-found, perfil, activar y Contador. Estilo `.btn-wa` (verde WhatsApp) en `landing.css`.
- **➡️ PRÓXIMO PASO sugerido:** para un curso nuevo, copiar una receta de simulacro, elegir bancos según el nivel y escribir solo las `funcionales`; el simulacro se mostrará bloqueado al estudiante hasta que termine sus guías.

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
Formulario con Nombres+Apellidos separados (Title Case vía `lib/format.ts`), OPEC/cargo/nivel obligatorios, contador de cupos centralizado (**177/200**), pre-llena si está logueado (multi-curso), sube manual PDF a Storage. Flujo: `/comprar` → Wompi → webhook (`/api/webhooks/wompi`) → `procesarReferencia()` crea usuario + curso + auto-carga guías → `/activar`. Robusto ante usuarios residuales.

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
- **Precio:** $300.000 COP, pago único. **Cupos de lanzamiento:** 177 vendidos de 200 (23 disponibles).
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
