# ✅ Plan de pruebas de punta a punta — Pre-lanzamiento

> Objetivo: validar **enlace por enlace, botón por botón**, que TODO funciona y conecta donde debe, desde la **vista del cliente** y la **vista del admin**, antes de subir el curso a TikTok y empezar a recibir compras.
>
> Cómo usarlo: marca cada `[ ]` → `[x]` a medida que lo pruebas en https://ascensopublico.com. Si algo falla, anótalo en la columna **Notas / falla** y se lo pasas a Kiro para corregirlo.
>
> ⚠️ Lo que TÚ auditarás aparte (no incluido aquí): generación de las guías y su montaje. El resto debe quedar perfecto con este plan.

_Última actualización del plan: 17 jun 2026_

---

## 0. PRE-REQUISITOS (hacer antes de probar)

- [ ] **Mergear la rama `feature/landing-wpp`** a `main` → así producción tendrá el número WhatsApp nuevo (3170905177), la foto del hero y el mensaje sin el símbolo raro. _Hasta que no se mergee, producción sigue con el número viejo._
- [ ] Confirmar que **Wompi está en modo PRODUCCIÓN** (llave pública empieza por `pub_prod_`, no `pub_test_`). En sandbox NO se cobra dinero real.
- [ ] Confirmar variables en Vercel: `ADMIN_EMAIL = ascensopublico@gmail.com`, `NEXT_PUBLIC_SITE_URL = https://ascensopublico.com`, `NEXT_PUBLIC_WOMPI_REDIRECT_URL = https://ascensopublico.com/activar`, `PRECIO_COP = 300000`.
- [ ] Tener a mano: un correo de prueba real, una tarjeta/medio de pago real (para la prueba de compra), y un PDF cualquiera para el "manual de funciones".
- [ ] Tener tu cuenta admin lista (`profiles.rol = 'admin'`).

---

# 👤 PARTE A — VISTA DEL CLIENTE (sin iniciar sesión)

## A1. Landing — Hero y navegación superior
- [ ] La home carga sin errores y se ve la **foto de fondo del hero** (personas celebrando) con el texto legible encima.
- [ ] **Logo** (arriba izq.) → vuelve a `/` (inicio).
- [ ] Menú "El problema" → baja a la sección Problema.
- [ ] Menú "Cómo funciona" → baja a la sección Cómo.
- [ ] Menú "Qué incluye" → baja a la sección Incluye.
- [ ] Menú "Convocatorias" → baja a la sección Convocatorias.
- [ ] Menú "Precio" → baja a la sección Precio.
- [ ] Botón "Iniciar sesión" (navbar) → va a `/login`.
- [ ] Botón "Quiero mi curso" (navbar) → va a `/comprar`.
- [ ] Botón hero "Quiero mi curso personalizado" → va a `/comprar`.
- [ ] Botón hero "💬 Asesoría por WhatsApp" → abre WhatsApp al **3170905177** con mensaje de asesoría.
- [ ] Botón hero "Ver cómo funciona" → baja a la sección Cómo.

## A2. Landing — Secciones de contenido
- [ ] Sección "El problema" se ve completa.
- [ ] Sección "La solución" se ve completa.
- [ ] Sección "Ejemplo" (guía de muestra) se ve bien.
- [ ] Sección "Cómo funciona" (pasos) se ve bien.
- [ ] Sección "Qué incluye" se ve bien.
- [ ] Sección "Nosotros / fundador" (Julio César Deávila) se ve bien.
- [ ] Selector de **nivel interactivo** (Asistencial / Técnico / Profesional) cambia el contenido al hacer clic en cada pestaña.
- [ ] Sección "Precio" muestra **$300.000 COP** y el botón de compra funciona.
- [ ] Sección "FAQ" abre/cierra las preguntas.
- [ ] Sección "Datos / privacidad" se ve y enlaza correctamente.

## A3. Landing — Convocatorias dinámicas
- [ ] La grilla de convocatorias carga tarjetas desde la base de datos (no vacía).
- [ ] Las imágenes de cada convocatoria cargan.
- [ ] Clic en una convocatoria → abre su detalle `/convocatorias/[id]` correctamente.
- [ ] En el detalle de una convocatoria, el botón de comprar/prepararme lleva a `/comprar` (idealmente con esa convocatoria pre-seleccionada).
- [ ] Texto "¿No ves la tuya? Escríbenos" → abre WhatsApp con mensaje de convocatoria.
- [ ] Ir a `/convocatorias` (listado completo) carga y funciona.

## A4. Landing — Footer y elementos flotantes
- [ ] **Botón flotante de WhatsApp** (esquina inferior derecha) → abre WhatsApp al 3170905177.
- [ ] En móvil, el botón flotante se ve como círculo (sin texto) y funciona.
- [ ] Enlaces del footer: Política de privacidad → `/privacidad`.
- [ ] Enlace del footer: Términos → `/terminos`.
- [ ] Correo del footer (mailto) → abre el cliente de correo a `ascensopublico@gmail.com`.
- [ ] El **contador de cupos** (de 100) se muestra coherente.

## A5. Páginas legales
- [ ] `/privacidad` carga y se lee completa.
- [ ] `/terminos` carga y se lee completa.
- [ ] Verificar que mencionen tu marca y datos reales (no placeholders).

## A6. Página 404 (not-found)
- [ ] Entrar a una URL inexistente (ej. `/algo-que-no-existe`) → muestra la página 404 con marca.
- [ ] El enlace "Escríbenos por WhatsApp" del 404 funciona.
- [ ] El enlace de volver al inicio funciona.

---

# 🛒 PARTE B — FLUJO DE COMPRA Y PAGO (la ruta del dinero)

## B1. Formulario `/comprar` — validaciones
- [ ] Enlace "← Volver al inicio" funciona.
- [ ] El contador de cupos se muestra.
- [ ] Intentar enviar **vacío** → el navegador exige los campos obligatorios (Nombres, Apellidos, Correo, Convocatoria, OPEC, Cargo, Nivel, Manual PDF, Consentimiento).
- [ ] El desplegable "Convocatoria" lista las convocatorias activas.
- [ ] El desplegable "Nivel" tiene Asistencial / Técnico / Profesional.
- [ ] El campo "Manual de funciones" solo acepta PDF.
- [ ] El checkbox de **consentimiento** (Ley 1581) es obligatorio y su enlace a `/privacidad` funciona.
- [ ] Texto de ayuda "Pago seguro con Wompi · PSE, Nequi y tarjetas" visible.

## B2. Compra real
- [ ] Llenar todo con datos reales + subir un PDF → "Continuar al pago seguro →".
- [ ] Redirige al **checkout de Wompi** mostrando el monto **$300.000** (300000 COP).
- [ ] Métodos de pago disponibles (PSE / Nequi / tarjeta) se ven.
- [ ] Pagar con un medio real → la transacción se aprueba.
- [ ] Tras aprobar, Wompi redirige a `/activar`.

> 🚩 Si el monto NO es 300.000, o el checkout dice "sandbox/pruebas", o no redirige a /activar → reportar.

## B3. Verificación en base de datos / admin (tras la compra)
- [ ] En `/admin` el contador "Pagos aprobados" subió en 1.
- [ ] En `/admin/cursos` aparece el nuevo cliente con su curso "⏳ En preparación".
- [ ] El correo de **confirmación al cliente** llegó (revisar bandeja y spam).
- [ ] El **aviso de compra al admin** llegó a `ascensopublico@gmail.com`.

---

# 🔑 PARTE C — ACTIVACIÓN DE CUENTA

## C1. Página `/activar`
- [ ] Muestra "¡Pago confirmado!" y el correo del cliente (campo de solo lectura, correcto).
- [ ] Pide crear contraseña (mínimo 6 caracteres).
- [ ] Intentar con menos de 6 caracteres → no deja continuar.
- [ ] Crear contraseña válida → "Entrar a mi perfil →" inicia sesión y lleva a `/perfil`.
- [ ] El enlace "escríbenos por WhatsApp" (si hay problema) funciona.

---

# 🎓 PARTE D — VISTA DEL CLIENTE (con sesión iniciada)

## D1. Login `/login`
- [ ] Logo arriba → vuelve a `/`.
- [ ] Login con correo/clave **incorrectos** → muestra "Correo o contraseña incorrectos. ¿Ya activaste tu cuenta?".
- [ ] Login correcto → entra a `/perfil` (o a `?next=` si venía de una ruta protegida).
- [ ] "¿Olvidaste tu contraseña?" → cambia al modo recuperar.
- [ ] Enviar correo de recuperación → muestra "¡Correo enviado!".
- [ ] Llega el correo de recuperación (revisar spam) con la marca.
- [ ] El enlace del correo abre `/reset-password` y permite crear clave nueva.
- [ ] Tras crear clave nueva → entra a `/perfil`.
- [ ] "← Volver a iniciar sesión" funciona.

## D2. Perfil `/perfil`
- [ ] Saluda con el nombre del usuario (Title Case).
- [ ] Aparece el botón "⚙️ Panel admin" SOLO si el usuario es admin.
- [ ] Botón cerrar sesión (Logout) visible.
- [ ] Bloque "Cambiar contraseña" presente.
- [ ] Con 1 curso: se muestra la tarjeta del curso expandida + "¿Aplicas a otra convocatoria? + Comprar otro curso".
- [ ] La tarjeta muestra: OPEC, cargo (Title Case), convocatoria, estado (badge) y **% de progreso** (si está listo).
- [ ] **El % NO se queda en 0** si ya leíste guías (progreso en vivo).
- [ ] Clic en la tarjeta → abre `/perfil/[cursoId]`.
- [ ] Botón "+ Comprar otro curso" → `/comprar` (pre-llena tu correo si estás logueado).
- [ ] (Si tienes 2+ cursos) se muestran como grid "Tus cursos (N)".
- [ ] Estado vacío (usuario sin cursos): muestra "Aún no tienes cursos" + botón comprar + enlace WhatsApp.

## D3. Detalle del curso `/perfil/[cursoId]`
- [ ] Enlace "← Mis cursos" vuelve a `/perfil`.
- [ ] Hero del curso muestra OPEC + cargo + convocatoria con imagen.
- [ ] **Si el curso está "en preparación":** muestra "Curso en preparación" + contador hacia el deadline (12h).
- [ ] **Si está "listo" pero aún no pasan las 12h:** muestra "Tu curso está casi listo" + contador.
- [ ] **Si está listo y pasaron las 12h:** muestra la ruta de estudio completa.
- [ ] Barra "Tu ruta de estudio": muestra "X de Y guías completadas" y el % correcto.
- [ ] Banner "▶ Continúa donde quedaste" apunta a la próxima guía no leída.
- [ ] Los **módulos** se ven (Introducción, Conocimientos Generales, Competencias por Nivel, Funciones del Cargo, Material Bonus, Simulacro Final), numerados sin huecos.
- [ ] Cada módulo muestra: **rango de días** (📅 Día X / Días X–Y), número de guías, estado (Pendiente/En curso/Completado) y barra de progreso.
- [ ] El primer módulo con guías por leer aparece **abierto** por defecto; los demás colapsados.
- [ ] Cada módulo muestra su texto introductorio (💡).
- [ ] Abrir/cerrar el acordeón de cada módulo funciona.

## D4. Filas de guía y visor `/guia/[id]`
- [ ] Cada guía muestra "DÍA n" legible (o ★ si no tiene día).
- [ ] Guía no leída muestra botón "Comenzar →"; leída muestra "✓ Completada".
- [ ] Guía sin archivo aún muestra "Próximamente".
- [ ] Clic en una guía → abre el visor con el header (título + Día + tipo) y el contenido en el iframe.
- [ ] El contenido HTML de la guía se ve bien (estilos, sin errores).
- [ ] "← Mi curso" en el visor vuelve a `/perfil/[cursoId]`.
- [ ] Al abrir una guía por primera vez, al volver queda **marcada como completada** y el % sube.
- [ ] Abrir una guía "Próximamente" (sin archivo) → muestra "Esta guía aún está siendo preparada".

## D5. Bloqueo del simulacro
- [ ] Con guías del plan SIN terminar: el módulo Simulacro aparece **🔒 Bloqueado** con "Te faltan N guías por leer".
- [ ] Intentar abrir el simulacro por URL directa (`/guia/[idSimulacro]`) → muestra "🔒 Simulacro bloqueado" (no deja entrar).
- [ ] El **bonus NO cuenta** para desbloquear (puedes tener bonus sin leer y aun así desbloquear si terminaste el resto).
- [ ] Al completar TODAS las guías del plan (generales/nivel/funcionales) → el simulacro se **desbloquea**.
- [ ] Simulacro desbloqueado: abre, responde, "Presentar examen", muestra resultados + revisión + temas a reforzar.

## D6. Cuenta
- [ ] "Cambiar contraseña" (en `/perfil`) funciona y permite re-loguear con la nueva.
- [ ] Cerrar sesión → va a `/login` y ya no se puede entrar a `/perfil` sin loguear.

---

# ⚙️ PARTE E — VISTA DEL ADMIN

## E1. Dashboard `/admin`
- [ ] Muestra métricas: Cursos totales, Cursos listos, En preparación, Convocatorias activas, Pagos aprobados (números coherentes).
- [ ] Tarjeta "🎓 Gestionar cursos" → `/admin/cursos`; muestra aviso "⚠️ N cursos pendientes" si hay.
- [ ] Tarjeta "📋 Gestionar convocatorias" → `/admin/convocatorias`.

## E2. Cursos `/admin/cursos`
- [ ] "← Panel" vuelve a `/admin`.
- [ ] Tabla lista todos los cursos con Cliente, Cargo, Nivel, Estado.
- [ ] Estado muestra "✅ Listo" o "⏳ En preparación" correctamente.
- [ ] "Gestionar →" abre `/admin/cursos/[id]`.

## E3. Detalle del curso (admin) `/admin/cursos/[id]`
- [ ] "← Todos los cursos" funciona.
- [ ] **Datos del cliente** correctos (nombre, correo, celular, OPEC, nivel, estado).
- [ ] "📄 Ver manual de funciones" abre el PDF que subió el cliente (URL firmada).
- [ ] Botón "👁️ Previsualizar el curso como lo verá el estudiante" → abre `/perfil/[cursoId]` en **modo vista previa** (banner amarillo, simulacro desbloqueado, no marca progreso).
- [ ] **Si el curso NO está listo:** aparecen los 2 botones:
  - [ ] "✅ Curso listo (se habilita a las 12h)" → cambia estado a listo con deadline.
  - [ ] "⚡ Habilitar ahora (acceso inmediato)" → el cliente lo ve de inmediato.
- [ ] **Si está listo y faltan las 12h:** muestra fecha programada + botón "⚡ Habilitar curso ahora" (cambio de opinión) y funciona.
- [ ] **Si está listo y ya pasaron las 12h:** muestra "✅ Curso habilitado".
- [ ] **Día 1:** muestra INTRO-00 (auto) y el selector "Conoce tu Entidad" (solo guías ENT-).
- [ ] Asignar una guía de entidad por código → queda cargada al instante.
- [ ] **Generales y por nivel (auto):** lista las auto-cargadas según el nivel del cargo.
- [ ] **Funcionales (x/12):** selector para asignar funcionales por código (con día/orden) → carga al instante.
- [ ] Botón "⚡ Copiar plan de otro curso del mismo OPEC" → trae funcionales/entidad/simulacro de otro curso del mismo OPEC sin duplicar.
- [ ] **Simulacro:** selector permite asignar SIM-001 por código (no se sube a mano).
- [ ] Botón "Eliminar" en una guía asignada → la quita del curso.
- [ ] **Subir guía personalizada (HTML)** (fallback): subir un .html con título/día/tipo → queda cargada.

## E4. Convocatorias `/admin/convocatorias`
- [ ] Formulario "Agregar nueva convocatoria" crea una convocatoria (aparece en el listado y en la landing).
- [ ] Botón "Desactivar"/"Activar" cambia la visibilidad (las inactivas no salen en la landing/compra).
- [ ] Botón "Eliminar" borra la convocatoria.
- [ ] La imagen por URL (ej. `/fotos/nacional.jpg`) se muestra en la tarjeta.

## E5. Usuarios `/admin/usuarios`
- [ ] Lista todos los usuarios con nombre, correo, celular, rol y fecha.
- [ ] Los admin tienen el badge "ADMIN" y **no** muestran botón Eliminar.
- [ ] Eliminar un usuario de prueba (no admin) funciona.

---

# 📧 PARTE F — CORREOS (entregabilidad)

- [ ] Correo de confirmación de compra al **cliente** llega y se ve con marca (logo/colores).
- [ ] Correo de aviso de compra al **admin** (`ascensopublico@gmail.com`) llega.
- [ ] Correo de **recuperación de contraseña** llega en español con marca y el enlace funciona.
- [ ] Revisar que NO caigan en spam (si caen → pendiente DMARC, anotado para más adelante).
- [ ] El enlace de WhatsApp dentro de los correos apunta al número correcto.

---

# 🔒 PARTE G — SEGURIDAD Y RUTAS PROTEGIDAS

- [ ] Sin sesión, entrar a `/perfil` → redirige a `/login`.
- [ ] Sin sesión, entrar a `/guia/[id]` → redirige a `/login`.
- [ ] Sin sesión, entrar a `/admin` → redirige a `/login` (o niega acceso).
- [ ] Un usuario NO admin que entra a `/admin/*` → es rechazado (requireAdmin).
- [ ] Un cliente NO puede ver el curso de OTRO cliente por URL (`/perfil/[otroCursoId]`) — solo el admin puede previsualizar cualquiera.
- [ ] Un cliente NO puede abrir una guía de un curso ajeno por URL.

---

# 📱 PARTE H — RESPONSIVE Y NAVEGADORES

- [ ] Probar la landing en **móvil** (o ventana < 820px): menú hamburguesa abre/cierra y todos los enlaces funcionan.
- [ ] Hero, secciones, convocatorias y footer se ven bien en móvil.
- [ ] `/comprar`, `/perfil` y el visor de guía se ven bien en móvil.
- [ ] Probar en al menos 2 navegadores (Chrome + Safari/Firefox).
- [ ] Probar el botón flotante de WhatsApp en móvil.

---

# 🧪 PARTE I — SEGUNDA COMPRA (automatización por OPEC)

- [ ] Comprar un segundo curso con **otro usuario** pero el **mismo OPEC** del primero.
- [ ] Verificar que el curso nuevo se arma **solo** (copia funcionales + entidad + simulacro del primero), sin duplicar genéricas.
- [ ] Verificar en el panel admin que el segundo curso ya trae el plan cargado.

---

## Resumen de hallazgos / pendientes

| # | Página / botón | Falla observada | Estado |
|---|---|---|---|
|   |   |   |   |

> Cuando termines un bloque, pásale a Kiro lo que falló (con captura si puedes) y lo corrige en código. Si algo solo se ve en producción, indicar la URL exacta y el paso.
