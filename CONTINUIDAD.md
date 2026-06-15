# 🔄 CONTINUIDAD DEL PROYECTO — Ascenso Público

> **Para retomar en una nueva sesión de Kiro:** conecta este repositorio y pídele a Kiro:
> *"Lee CONTINUIDAD.md y ARQUITECTURA-PLATAFORMA.md y continuemos donde quedamos."*

_Última actualización: 15 de junio de 2026._

---

## 1. Qué es el proyecto
**Ascenso Público**: preparación **personalizada por el CARGO específico** (no solo por nivel) para los concursos de méritos de la **CNSC** (Colombia). Plan de 21 días + guías + simulacros tipo CNSC, a partir del OPEC y el **manual de funciones** del aspirante.

Tiene **dos partes**:
1. **Landing** (marketing) — ✅ en vivo.
2. **Plataforma** (portal del estudiante + compra + panel admin) — ✅ código completo, ⏳ falta desplegar.

## 2. Repositorio
- **GitHub:** `ascensopublico2026/ASCENSO-PUBLICO` (antes `CesarDeavila1126`; se renombró la cuenta, GitHub mantiene redirecciones, no se perdió nada).
- **Rama principal:** `main` (todo el trabajo está mergeado ahí).
- **Para conectar en la nueva sesión:** usa la herramienta de setup de repositorio con `owner=ascensopublico2026`, `repo=ASCENSO-PUBLICO`. Asegúrate de que la nueva cuenta de Kiro tenga acceso a ese GitHub.

## 3. Estructura del repo
```
landing/index.html         · Landing v4 (EN VIVO en GitHub Pages)
landing/preparacion.html   · Página post-pago con contador 12h (puente hasta el portal)
plataforma/                · App Next.js + Supabase + Wompi + Resend (CÓDIGO COMPLETO, SIN DESPLEGAR)
  ├─ app/                  · páginas (comprar, convocatorias, activar, login, perfil, admin, api/webhooks)
  ├─ lib/                  · supabase, wompi, email, auth, procesarPago
  ├─ supabase/schema.sql   · modelo de datos + RLS + buckets
  ├─ SETUP.md y DESPLIEGUE.md · guías de instalación y despliegue
brand/                     · logos + brand/fotos (fotos reales optimizadas)
guias/                     · guías HTML de ejemplo
biblioteca/ · prompts/ · scripts/   · utilidades y contenido
docs/investigacion-competencia/      · capturas de la competencia (referencia)
ARQUITECTURA-PLATAFORMA.md · PROYECTO-MAESTRO.md · PLAN-PROYECTO.md · ESTANDAR-TECNICO.md · PLANTILLA-GUIA.md
```
**URL landing en vivo:** https://ascensopublico2026.github.io/ASCENSO-PUBLICO/landing/

## 4. Estado actual
### ✅ Hecho
- **Landing v4 en vivo:** hero con foto + velo navy, historia del fundador (Julio César Deávila), 6 convocatorias reales con fotos, captura de leads ("Avísame"), interactivo por nivel, FAQ, política de datos, WhatsApp flotante. _(Quedan ajustes finos menores que el usuario hará.)_
- **Plataforma — código completo (13/14 hitos):** formulario de compra con subida de PDF, checkout Wompi, **webhook** (crea cuenta + curso, deadline 12h), **/activar** (crear contraseña post-pago), **/login**, **/perfil** (estado + contador 12h + guías embebidas no descargables), **panel /admin** (clientes, subir guías, habilitar acceso, CRUD convocatorias), **correos** (Resend), **legal** (privacidad/términos).

### ⏳ Lo siguiente (PASO ACTUAL) — Desplegar la plataforma
Seguir `plataforma/DESPLIEGUE.md` en orden:
1. **Supabase**: crear proyecto + correr `supabase/schema.sql` + verificar buckets `manuales` y `guias`.
2. **Resend** (API key para correos).
3. **Wompi**: copiar las 4 llaves/secretos (pública, privada, integridad, eventos).
4. **Vercel**: desplegar con **Root Directory = `plataforma`** + variables de entorno.
5. **Webhook** de Wompi → `https://TU-URL/api/webhooks/wompi`.
6. **Hacerse admin** (update profiles set rol='admin').
7. **Prueba end-to-end en sandbox** de Wompi antes de producción.

> ⚠️ El código de la plataforma **no se ha probado** (se escribió en un entorno sin internet). Al desplegar habrá ajustes; ir probando paso a paso. Verificar contra la doc de Wompi: formato del evento del webhook y orden de las firmas (marcado con 🔎 en el código).

### Otros pendientes
- Ajustes finos de la landing (menores).
- Conectar **dominio propio** (opcional) y actualizar los meta **Open Graph** (hoy dicen `https://TU-DOMINIO.com`).
- Decidir si la compra se hace por la **plataforma** (recomendado) o por un **link de pago de Wompi** suelto.

## 5. Datos clave y decisiones (NO cambiar sin avisar)
- **Marca:** navy `#0A2A5E` · crema `#FBF9F4` · oro `#E8A33D`. Tipos: Source Serif 4 + Plus Jakarta Sans.
- **Contacto:** WhatsApp **+57 315 197 2091** · correo **ascensopublico@gmail.com**.
- **Precio:** $300.000 COP, pago único (precio de lanzamiento).
- **Fundador:** Julio César Deávila.
- **Diferenciador:** personalización por **cargo específico** + explicar el "cómo" (genera confianza).
- **Wompi:** cuenta creada (persona natural); categoría "Productos digitales".
- **Stack plataforma:** Next.js (App Router) + Supabase (Auth/DB/Storage) + Vercel + Wompi + Resend.

## 6. Reglas de trabajo aprendidas (IMPORTANTES)
- 🚫 **Integridad:** nada de testimonios, fotos de personas ni cifras **inventadas**. Solo datos reales y verificables.
- 🖼️ **Imágenes:** comprimir (p. ej. squoosh.app) antes de subir; nombres web-friendly (sin espacios/mayúsculas).
- 🔒 **Datos personales (Ley 1581):** consentimiento + política. **Nunca** exponer secretos (`service_role`, llaves privadas).
- 🧾 **IVA/facturación:** posiblemente "no responsable de IVA"/educación excluida — **confirmar con un contador** (no es asesoría legal).
- 🌐 **El sandbox de Kiro no tiene internet:** Kiro escribe y sube el código; **instalar/desplegar lo hace el usuario** (Vercel/Supabase).
- 🔀 **Git:** trabajar en ramas y mergear a `main`; usar las herramientas de push/PR (no `git push` directo).

## 7. Cómo dejaste esta conversación
Acabábamos de: hacer **merge a main**, confirmar que la **landing está en vivo**, y estábamos por iniciar el **despliegue de la plataforma (Paso 1: Supabase)**. Continúa por ahí.
