# 🏗️ ARQUITECTURA DE LA PLATAFORMA — Ascenso Público

> **Plano maestro de la plataforma web.** Define qué se construye, cómo, con qué herramientas, el flujo del cliente, el modelo de datos y las reglas. Es la fuente de verdad técnica del producto.
>
> Se relaciona con: `PROYECTO-MAESTRO.md` (visión), `PLAN-PROYECTO.md` (gestión/fases), `ESTANDAR-TECNICO.md` (diseño de las guías).
>
> **Última actualización:** 14 de junio de 2026 · **Estado:** definición (pre-construcción).

---

## 1. Qué es la plataforma

La plataforma web de Ascenso Público tiene **cuatro partes**:
1. **Landing page** — capta al visitante que llega desde TikTok (tráfico frío) y lo convierte en comprador.
2. **Flujo de compra y registro** — selección de convocatoria, formulario de datos + manual de funciones (PDF), y pago por Wompi.
3. **Portal del estudiante** — donde el cliente ve su curso y estudia sus guías embebidas.
4. **Panel de administrador** — solo para el fundador: clientes, cursos, subida de guías, habilitación de acceso y gestión de convocatorias.

---

## 2. Stack tecnológico (decidido)

| Capa | Herramienta | Plan | Por qué |
|---|---|---|---|
| Landing | HTML/CSS estático (marca propia) | Gratis | Rápido, liviano, se publica gratis; ideal para tráfico de TikTok. |
| App (portal + admin) | **Next.js / React** | Gratis | Se construye como código en el repo; sin depender de suscripción de un constructor. |
| Backend (auth, BD, archivos) | **Supabase** | Free tier | Login, base de datos PostgreSQL y almacenamiento de archivos privados. |
| Hosting | **Vercel** | Free (Hobby) | Conecta con GitHub y despliega solo. |
| Pagos | **Wompi** | Sandbox → Producción | PSE, Nequi, tarjetas (Colombia). Link de pago (MVP) o API (automatizado). |
| Correos | **Resend** | Free tier | Confirmación al cliente + aviso al admin. |
| Fuente de las guías | **GitHub** (este repo) | — | Desarrollo/fuente de verdad. La *entrega* al cliente es privada (ver §7). |

> **Costo hoy: $0.** Solo se paga al lanzar: **dominio** (`ascensopublico.com`, ~USD 10–15/año) + **Wompi en producción** (cobra por transacción, sin mensualidad).

---

## 3. Estrategia de costo y lanzamiento

- **Ahora (crecer TikTok, sin gastar):** landing al aire (gratis) + arquitectura y diseño listos. Las primeras ventas pueden hacerse en modo **"concierge"** (formulario gratis + link de pago Wompi + entrega manual), lo que además aporta el **primer caso OPEC real** para diseñar las guías funcionales y el simulacro.
- **Al lanzar:** compra de dominio + Wompi producción = "encender el switch".

---

## 4. Flujo completo del cliente (paso a paso)

1. **Landing.** Llega desde TikTok (link en bio), tráfico frío. La landing convence rápido: qué es, por qué es diferente (personalizado **por cargo**, no por convocatoria), cómo funciona, qué incluye, precio, convocatorias activas y botón de compra.
2. **Selección de convocatoria.** Elige, entre las convocatorias activas, la que le aplica.
3. **Registro + datos.** Ingresa: nombre, correo, celular, convocatoria, **número de OPEC**, nombre del cargo, **nivel** (Asistencial/Técnico/Profesional) y **sube el Manual de Funciones (PDF, obligatorio)**. Incluye un **video corto** que explica cómo descargar la OPEC y el manual desde la página de la CNSC.
4. **Pago.** Por Wompi. **Precio de lanzamiento: $300.000 COP.** Al completar: correo de confirmación automático al cliente + notificación al admin con todos los datos y el PDF.
5. **Perfil (acceso inmediato).** Ve su nombre, el nombre de su curso (ej. *"Técnico Almacenista — INDERVALLE"*), estado **"Curso en preparación"**, una **barra de progreso de 12 horas** desde la compra y un mensaje de "en máx. 12 h tendrás tus guías".
6. **Acceso al curso (a las 12 h).** Cuando el admin sube las guías y habilita el acceso, el estado pasa a **"Curso listo"** y aparece la biblioteca por día (Día 1 → Día 21, con el Simulacro Final al cierre). Cada guía **se abre embebida dentro del perfil** (no se descarga, no abre en otra pestaña). El acceso dura **60–90 días** desde la compra (a definir).

---

## 5. Landing page — secciones (en orden)

1. **Hero** — título, eslogan, propuesta de valor en una frase, botón de compra.
2. **El problema** — por qué los cursos genéricos no funcionan; estudiar sin dirección es perder tiempo.
3. **La solución** — qué es Ascenso Público y cómo lo resuelve.
4. **Cómo funciona** — proceso paso a paso (compra → perfil → guías → simulacro).
5. **Qué incluye el curso** — guías, simulacro, acceso personalizado.
6. **Convocatorias disponibles** — lista **dinámica** (gestionada desde el panel admin).
7. **Precio** — lanzamiento $300.000 COP + botón de compra.
8. **Preguntas frecuentes** — FAQ básico.
9. **Footer** — marca, eslogan, contacto.

---

## 6. Convocatorias (sección dinámica)

Las gestiona el admin (no van fijas en el código). El admin puede **agregar, editar y quitar**. Se muestran las que están en alguna de estas etapas:
- Inscripciones abiertas.
- Inscripciones cerradas, pero pruebas escritas pendientes.
- Pruebas escritas próximas.

Campos por convocatoria: **nombre, entidad, estado, fecha aproximada de pruebas, activa (sí/no)**.

---

## 7. Entrega de las guías (regla técnica importante)

Las guías son archivos HTML. Para cumplir **"embebidas y no descargables"**:
- **NO** se sirven desde GitHub público (sería descargable por URL `raw`).
- Se guardan en **almacenamiento privado** (Supabase Storage), asociadas al curso del estudiante.
- En el portal se muestran con **URL firmada temporal dentro de un `iframe`**; el estudiante las ve, pero no obtiene el archivo como descarga ni en otra pestaña.
- GitHub sigue siendo la **fuente de verdad** (desarrollo); la copia de entrega vive en el almacenamiento privado.

> Nota honesta: ninguna web evita 100% que un usuario técnico capture el HTML (devtools). Esta arquitectura es el estándar correcto y disuade a la práctica totalidad de los usuarios; se refuerza deshabilitando descarga directa, clic derecho y apertura en pestaña.

---

## 8. Portal del estudiante (qué ve)

- Su **nombre** y el **nombre de su curso**.
- **Estado del curso:** "Curso en preparación" / "Curso listo".
- Mientras está en preparación: **barra de progreso de 12 h** (contador desde la compra) + mensaje.
- Cuando está listo: **biblioteca por día** (Día 1 → 21 + Simulacro Final), cada guía **embebida** al hacer clic.
- **Fecha de vencimiento** del acceso (60–90 días).

---

## 9. Panel de administrador (solo fundador)

Con **login propio** (no visible para el estudiante), permite:
- Ver **todos los clientes** y sus datos.
- Ver el **estado de cada curso** (en preparación / listo).
- **Subir las guías** al perfil de cada estudiante.
- **Habilitar el acceso** cuando el curso esté listo (cambia el estado).
- **Gestionar convocatorias** que aparecen en la landing.
- Ver **fecha de vencimiento** del acceso de cada estudiante.

---

## 10. Modelo de datos (pensado para automatizar a futuro)

Tablas base en Supabase (nombres orientativos):

- **`convocatorias`** — `id, nombre, entidad, estado, fecha_prueba_aprox, activa, orden`.
- **`usuarios`** — `id, nombre, correo, celular, rol (estudiante|admin), created_at`. (Auth de Supabase).
- **`cursos`** — `id, usuario_id, convocatoria_id, opec, cargo_nombre, nivel, manual_pdf_url, estado (en_preparacion|listo), fecha_compra, fecha_vencimiento, progreso_pct`.
- **`guias_curso`** — `id, curso_id, dia, titulo, archivo_url (privado), tipo (general|nivel|funcional|bonus|simulacro), orden`.
- **`pagos`** — `id, usuario_id, curso_id, wompi_transaction_id, monto, estado, fecha`.

> **Automation-ready:** al confirmarse un pago se crea `usuario` + `curso` (estado `en_preparacion`). El admin —o, a futuro, la IA— llena `guias_curso` y cambia el estado a `listo`. El catálogo reutilizable sigue en `biblioteca/biblioteca.json`.

---

## 11. Pagos (Wompi)

- **MVP / concierge:** **Link de pago** de Wompi (no-code). Rápido para los primeros clientes; el registro de datos + PDF se hace por un formulario aparte.
- **Plataforma:** **API de Wompi + webhook** → al confirmarse el pago, se crea el perfil automáticamente y se disparan los correos.
- **Pre-lanzamiento:** todo se prueba en **sandbox** (gratis). Requiere registrar el comercio (datos del negocio) para producción.

---

## 12. Correos automáticos

- **Al cliente:** confirmación de compra + "tu curso estará listo en máx. 12 h".
- **Al admin:** notificación con todos los datos del cliente + enlace al PDF del manual.
- Herramienta sugerida: **Resend** (free tier).

---

## 13. Legal y privacidad (Colombia)

Se manejan datos personales y documentos (manual de funciones) → es obligatorio:
- **Política de privacidad** y **autorización de tratamiento de datos (habeas data, Ley 1581/2012)** con checkbox de consentimiento en el formulario de registro.
- Términos y condiciones del servicio (qué incluye, vigencia del acceso 60–90 días, no reembolso si aplica, etc.).

---

## 14. Identidad visual (CONGELADA)

- **Paleta:** fondo crema `#FBF9F4` · azul institucional `#0A2A5E` · dorado `#E8A33D`.
- **Logo:** V2 (en `brand/`).
- **Eslogan:** *Tu ruta personalizada hacia el empleo público.*
- **Estilo:** moderno, profesional, académico, limpio.
- Toda la plataforma respeta esta identidad **exactamente**.

---

## 15. Lo que NO se quiere

- Que las guías se puedan **descargar**.
- Que el estudiante vea el contenido **antes de las 12 h**.
- Tener que **tocar código** para agregar/quitar convocatorias (se gestionan desde el admin).
- Que el **panel admin** sea visible para el estudiante.
- Diseños genéricos que **no respeten** la paleta y el logo.

---

## 16. Fases de implementación

| Fase | Qué | Costo | Estado |
|---|---|---|---|
| **F1 · Landing** | Landing estática con marca + sección de convocatorias + CTA | $0 | ⬜ Próximo |
| **F2 · Concierge** | Formulario (datos + PDF) + link de pago Wompi + entrega manual | $0 | ⬜ |
| **F3 · Plataforma** | Portal estudiante + panel admin + Supabase + Wompi API + correos | $0 (hosting free) | ⬜ |
| **F4 · Lanzamiento** | Dominio + Wompi producción | dominio + transacciones | ⬜ |
| **F5 · Automatización** | Pago → analizar OPEC → generar plan/guías → subir → habilitar | — | 🔮 Visión |

---

## 17. Decisiones congeladas

1. **Stack:** Next.js + Supabase + Vercel + Wompi + Resend; landing estática.
2. **Costo:** todo en planes gratis hasta lanzar; gasto real = dominio + Wompi producción.
3. **Entrega de guías:** privada (Supabase Storage) + iframe; **nunca** desde GitHub público.
4. **Convocatorias:** dinámicas, gestionadas desde el panel admin.
5. **Precio de lanzamiento:** $300.000 COP.
6. **Acceso:** 60–90 días desde la compra (cifra exacta por definir).
7. **Identidad:** paleta 60-30-10, logo V2, eslogan (igual que las guías).
8. **Lo personalizable (guías funcionales + simulacro):** se diseña con el primer caso OPEC real.
