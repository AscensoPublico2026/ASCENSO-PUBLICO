# CONTINUIDAD — Marketing TikTok · Ascenso Público

> Documento maestro para retomar el proyecto de marketing en cualquier sesión.
> Todo el material está en la rama **`marketing/tiktok-plan-y-outro`** del repo.

## 🆕 GIRO ESTRATÉGICO (sesión jun 2026) — Video con rostro + simulacro gratis

> Las primeras publicaciones (carruseles/foto) tuvieron poco alcance. Cambiamos el enfoque:

- **🎥 VIDEO con ROSTRO es ahora el formato principal.** La encargada de marketing (la mamá de Julio)
  está dispuesta a dar la cara y grabar mucho contenido. TikTok premia el video y la gente conecta
  con personas, no con logos. Formato estrella: **persona hablando arriba + flyer abajo** (el que
  domina el nicho CNSC y da confianza).
- **🛠️ Nueva herramienta:** `plantillas/generador-flyer-video.html` — flyers diseñados para la mitad
  inferior (zona del rostro reservada arriba). 5 modos: **Pregunta CNSC** (A/B/C/D), **El porqué**
  (respuesta + explicación), **Dato/Convocatoria** (cifra grande + fechas), **Tips/Errores** (lista
  numerada) y **Simulacro GRATIS** (3 niveles). Resalta palabras con `[corchetes]`. Diseño más rico
  que las tarjetas viejas (tarjeta con borde dorado, opciones en cards, sello teal de “correcto”).
- **🎯 SIMULACRO GRATIS por nivel = imán de leads.** El producto ya tiene 3 simulacros gratis
  (asistencial / técnico / profesional, 20 preguntas c/u, tipo examen real, con resultado). Es el
  **gancho central de venta**: en vez de “compra”, decimos “mídete gratis” → captura el lead → vende.
- **📝 Guiones nuevos:** `guiones/lote-01-rostro-y-simulacro.md` — 5 videos cortos (15–30 s) con
  gancho fuerte y rostro: presentación (fijar en perfil), pregunta CNSC en serie, período de prueba,
  venta “genérico vs por cargo”, y el simulacro gratis como gancho de leads.
- **Regla de oro nueva:** gancho EMOCIONAL en el segundo 1 (curiosidad/miedo/identificación), no
  “Pregunta tipo examen CNSC”. El dato/valor viene después para retener hasta el final.

## 1. Contexto
- **Producto:** preparación para concursos CNSC, **personalizada por CARGO** (diferenciador central). Plan 21 días + guías + simulacro. $300.000 COP. Cupos lanzamiento 100. En producción en ascensopublico.com. Fundador: Julio César Deávila.
- **La parte difícil (producto) está hecha.** Ahora: **marketing y contenido en TikTok** → primeras ventas.
- **Cuenta:** @ascensopublico (recién empezando; primeras publicaciones hechas).

## 2. Identidad de marca (BLOQUEADA)
- **Colores:** navy `#0A2A5E` · dorado `#FFC233`/`#E8A33D` · teal `#16C2A3` · crema `#FBF9F4`.
- **Tipografía:** Source Serif 4 (títulos) + Plus Jakarta Sans (texto/subtítulos).
- **Logo:** flecha ascendente. **Sello:** "chip de cargo" + flecha + outro animado.
- **Código de color por contenido:** 🟦 Navy = informativo/tips/valor/venta · ⬜ Crema = preguntas tipo CNSC.

## 3. Herramientas creadas (en `marketing/`)
- **`plantillas/generador-casos-cnsc.html` ⭐⭐ NUEVO — Modo presentador para videos explicando casos.**
  No es para exportar una imagen: es para **compartir la pantalla en vivo** mientras Julio graba
  explicando una pregunta tipo CNSC. Tiene un panel editor (a la derecha, se oculta con el botón
  "✏️ Editar caso" o la tecla `Tab`) donde se escribe: el caso/contexto, la pregunta, las 4 opciones
  con su explicación cada una, y cuál es la correcta. Al ocultar el panel queda solo la tarjeta con
  la identidad de marca (navy/crema/oro + logo), lista para grabar. Durante la grabación: clic (o
  teclas `1`-`4`) revela cada opción — la correcta en **verde con ✓** y su explicación, las
  incorrectas en **rojo con ✗** y su explicación; tecla `Espacio` revela todas de una, `R` reinicia
  la vista para repetir la toma. Incluye **banco de casos** (guardar/cargar/eliminar, todo en el
  navegador vía `localStorage`) + exportar/importar el banco como JSON para respaldo o pasarlo a
  otro computador. Trae un caso de ejemplo real (almacén/INDERVALLE) precargado la primera vez.
  Probado end-to-end (19 pruebas automáticas: edición en vivo, revelado, atajos, panel, banco).
- **`plantillas/generador-flyer-video.html` ⭐ (formato principal para publicar)** — flyers para video
  “rostro arriba + flyer abajo”. 5 modos: Pregunta CNSC · El porqué · Dato/Convocatoria · Tips/Errores
  · Simulacro GRATIS. Resalta con `[corchetes]`, chip de nivel/cargo, guías de encuadre.
- `plantillas/generador-tarjetas.html` — tarjetas/portadas a pantalla completa (portada del perfil, hooks).
- `plantillas/generador-carrusel.html` — carruseles (uso secundario; el video manda).
- `plantillas/generador-flyer-certificado.html` — flyers específicos de certificado (laboral/electoral).
- `outro-logo/outro.html` — outro animado del logo, descarga video 9:16.
- Se abren: GitHub → archivo → "Download raw file" → abrir en navegador.

## 4. Documentos de estrategia (en `marketing/`)
- `guia-de-estilo-tiktok.md` — identidad bloqueada.
- `estrategia-copia-mejora.md` — filosofía + 3 pilares.
- `plan-lanzamiento.md` — sprint 12 días.
- `workflow-diario.md` — rutina, horarios, feedback video inicial.
- `produccion-video.md` — cómo armar videos (faceless + cara).
- `hashtags.md` — estrategia de hashtags 2026.
- `cronograma-semana1.md` — plan jue→dom.
- `banco-contenido.md` — **carruseles 1–9 listos** para copiar/pegar.
- `competencia-tiktok/analisis.md` — análisis visual de competidores.
- `competencia-tiktok/estudio-competidores.md` — plantilla estudio 6–7 competidores (en proceso).

## 5. Flujo de trabajo acordado
- **3 publicaciones/día:** 9am (informativo/reactivo) · 3pm (pregunta CNSC, crema) · 8pm (valor/venta).
- **Programar** posts en TikTok (Julio trabaja L–V 8–12 y 2–5; engancha en almuerzo y noche).
- **Domingo:** planear + producir en lote la semana. **Entre semana:** contenido reactivo del día + responder comentarios.
- **Copia + mejora:** la competencia inspira NIVEL y formato; el contenido es ORIGINAL nuestro.
- **CTAs en cada post:** comentar (pregunta) + guardar 📌 + compartir.
- 🔒 **REGLA DE ORO:** las preguntas técnico-legales las **verifica Julio** (con su material/la ley) antes de publicar. Datos exactos = credibilidad.

## 6. Estado actual de publicaciones
- Video reactivo "3.044 vacantes ESE" (publicado).
- Carrusel "competencias Decreto 815" (republicar arreglado tras corte de UI).
- Pendiente noche jueves: elegir entre carruseles del banco (recomendado: **Carrusel 9 — período de prueba**, original).

## 7. Próximos pasos
1. Publicar post de la noche (Carrusel 9 verificado).
2. Viernes AM: armar contenido del día (reactivo, según competencia).
3. Avanzar el estudio de 6–7 competidores (1 por día).
4. Seguir cronograma; el domingo armar semana 2 según resultados.
5. Mantener verificación legal en todas las preguntas técnicas.

## 8. Tono y rol del asistente
Estratega de marketing TikTok + creador de contenido + diseñador. Honesto (sin promesas de éxito garantizado), apoya en lo emocional (Julio siente algo de miedo con el marketing), entrega contenido EXCELENTE y verificable. Responder siempre en español.
