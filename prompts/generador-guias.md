# 🤖 Prompt — Generador de Guías (Ascenso Público)

> **Qué hace:** recibe un **tema/título + código + día + nivel** y genera una **guía HTML completa** idéntica en formato a las que ya tenemos (INTRO-00, GEN-01/02/03).
>
> **Cómo se usa:** copia el bloque de prompt (`=== INICIO ===` … `=== FIN ===`), pégalo en la IA y completa los datos de entrada al final.
>
> **Documento VIVO:** cada vez que mejoremos una guía ("quita esto / agrega esto"), se actualiza este prompt y se anota en el **Changelog** (al final). Así toda guía nueva nace con las mejoras acumuladas.
>
> **Versión:** 2.1 · **Base técnica:** `ESTANDAR-TECNICO.md` + `PLANTILLA-GUIA.md`.

---

```
=== INICIO DEL PROMPT ===

Actúa como un diseñador instruccional experto en concursos de mérito CNSC y un desarrollador front-end. Vas a generar una GUÍA DE ESTUDIO en un ÚNICO archivo HTML autocontenido, idéntica en formato, estilo y calidad a las guías existentes de Ascenso Público.

== IDENTIDAD Y ESTILO (OBLIGATORIO) ==
- Marca "Ascenso Público" + eslogan "Tu ruta personalizada hacia el empleo público" en el header y el footer.
- Paleta 60-30-10: fondo crema #FBF9F4 · azul institucional #0A2A5E · dorado #E8A33D. Colores semánticos fijos: verde=correcto/tip, rojo=error, ámbar=advertencia, azul=info.
- Estilo cálido, profesional, académico y limpio; con emojis distintivos por concepto (sin "arcoíris").
- Tipografías: 'Plus Jakarta Sans' (texto) y 'Source Serif 4' (títulos) vía Google Fonts.
- Logo: SVG inline (flecha de impulso) en el header. Favicon: <link rel="icon" href="../brand/favicon.svg">.
- HTML 100% autocontenido (CSS y JS embebidos). Debe abrir con doble clic en el navegador.
- Tiempo de estudio objetivo: 75–110 minutos.

== REUTILIZACIÓN Y CODIFICACIÓN (OBLIGATORIO) ==
- Las guías FUNCIONALES deben ser REUTILIZABLES entre cargos y entidades: el mismo conocimiento le sirve a un almacenista de una alcaldía, un hospital o un instituto. Por eso NO menciones la entidad específica del aspirante (no "INDERVALLE"). Habla de "tu entidad" en genérico y usa ejemplos de varios tipos de entidad (alcaldía, hospital, instituto, secretaría). Todo lo específico de la entidad vive ÚNICAMENTE en la guía "Conoce tu Entidad" (ENT-xxx).
- Código de guía funcional: patrón FUN-[FAMILIA]-[Nº] (ej. FUN-ALM-04). La FAMILIA es el dominio de conocimiento (ALM=Almacén, DOC=Gestión Documental, PRO=Procesos/Calidad, MIPG, OFI=Ofimática, ATC=Servicio/apoyo, TIC, FIN, TH, JUR…). El código es global y fijo; el "Día" se asigna por cliente.
- Guía de entidad: ENT-[SIGLA]-[Nº] (ej. ENT-IDV-01). Esa SÍ es específica y no reutilizable.

== VARIANTE FUNCIONAL v2 (úsala en TODAS las guías FUN-*) ==
Las guías funcionales mantienen las 11 secciones y la identidad de marca, pero ELEVAN la dinámica de aprendizaje con estos componentes adicionales (más práctica, menos fatiga):
- HILO NARRATIVO: abre el Objetivo con un bloque ".narr" que pone al estudiante en situación ("Imagina que es tu primer día como Técnico de Almacén de tu entidad…"). Mantén ese tono de mentor cercano a lo largo de la guía.
- DIAGRAMAS DE PROCESO (".flujo"): cuando el tema sea un proceso/secuencia (ciclo logístico, flujo de recepción, etc.), represéntalo con pasos visuales numerados (".flujo-paso"), no solo con texto.
- CHECKPOINTS INTERCALADOS (".checkpoint" · "Aplica lo aprendido"): 2 o 3 mini-preguntas situacionales DENTRO del Desarrollo (no solo el simulacro final), cada una con feedback inmediato por opción. Mantienen la atención y verifican comprensión concepto a concepto.
- TARJETAS "EN LA PRÁCTICA" (".practica"): ejemplos concretos y tangibles (un acta de recibo, un kardex, una tabla de existencias mínimas, una mini-tabla comparativa).
- MICRO-TIPS "OJO EN LA PRUEBA" (".ojo"): avisos breves dentro del Desarrollo que anticipan cómo cae el tema en el examen.
- ENLACES A LA FUENTE (".fuentes"): en el Desarrollo, incluye un bloque con enlaces a las fuentes OFICIALES (norma, Constitución, entidad rectora) de los temas tratados, para que el estudiante que quiera profundice por su cuenta. Usa fuentes oficiales y estables (Constitución vía Secretaría del Senado; Función Pública; Contaduría General de la Nación; Colombia Compra Eficiente; etc.). Nunca enlaces inventados.
- REDACCIÓN: voz de mentor, cercana y clara, con ejemplos reales y CERO relleno. El estudiante debe sentir "aprendí muchísimo y valió la inversión".

== ESTRUCTURA OBLIGATORIA (11 secciones navegables con pestañas) ==
0. 🎯 Objetivo — qué dominará y para qué le sirve a su cargo (lista + box dorado de promesa).
1. ⭐ Importancia — por qué el tema cae en la prueba; qué pasa si no lo domina (box info "dato clave").
2. 📖 Desarrollo — 6 a 8 conceptos, cada uno en 4 CAPAS:
   🟦 Definición (qué es) · 🟩 Aplicación (cómo opera) · 🟨 Ejemplo real (entidad/caso concreto) · 🟥 Cómo lo evalúa la CNSC (trampa típica).
   Si un concepto tiene 3+ sub-componentes evaluables (que la CNSC pregunta por separado), añade SUB-BLOQUES desplegables: qué lo conforma, funciones, tabla comparativa, ⚠️ trampa CNSC y 🎯 mini-pregunta tipo CNSC.
   Reglas de longitud por capa: 2–4 párrafos cortos, con norma/artículo/entidad real verificable. Nunca "es importante" sin sustancia.
3. ⚖️ Comparaciones — 2 a 4 tablas que diferencian conceptos que se confunden + trampa típica.
4. 📂 Casos CNSC — 5 casos (situación → análisis → respuesta correcta + explicación).
5. ⚠️ Errores frecuentes — 6 (qué es + por qué falla + cómo corregir).
6. 💡 Tips — 6 (mnemotecnia, descarte de distractores, reglas rápidas).
7. 🎭 Trampas — 4 (lo que parece correcto / por qué es trampa / la respuesta correcta).
8. 🧠 Repaso (flashcards) — 10 tarjetas que voltean (pregunta corta → respuesta concisa), cubriendo todos los conceptos.
9. 📋 Resumen + Glosario — 6 cards de resumen + 6 términos de glosario + frase para recordar.
10. 📝 Simulacro — ver reglas abajo.

== SIMULACRO — JUICIO SITUACIONAL (CRÍTICO) ==
- Tipo: JUICIO SITUACIONAL. Cada pregunta plantea un CASO/contexto real del día a día del servidor y un enunciado tipo "¿qué es lo más apropiado que debe hacer?". NUNCA preguntes la norma de memoria ("¿qué dice la ley X?").
- 12 preguntas. Distribución: 4 básicas + 5 intermedias + 3 avanzadas.
- 4 opciones (A, B, C, D); solo una correcta. Las 4 son cursos de acción PLAUSIBLES.
- TODAS las preguntas llevan contexto (ctx).
- Retroalimentación POR OPCIÓN: al hacer clic en una opción se revelan las explicaciones de LAS 4 opciones (debajo de cada una), indicando por qué cada una es correcta o incorrecta; no solo la elegida ni solo la correcta. Aquí SÍ puedes citar el artículo/ley para reforzar.
- Los enunciados y contextos deben ser RICOS y realistas (varias líneas de caso), tal como los plantea la CNSC; nada de preguntas de una sola línea.
- Al final: puntaje + lista de "Temas a reforzar" (según preguntas falladas). Cada pregunta tiene un campo "tema".
- Distractores basados en errores reales: extralimitación de funciones, omisión de responsabilidades, incumplimiento de procedimiento, afectación al servicio al ciudadano, interpretación parcial, desconocimiento del alcance del cargo.
- Respuestas correctas distribuidas SIN patrón visible.
- Regla suprema: antes de aprobar cada pregunta, pregúntate "¿esto podría aparecer en una prueba escrita real de la CNSC?". Si no, rediséñala.

== FUNCIONALIDAD (JS) ==
- Navegación por pestañas (mostrar/ocultar secciones) + barra de progreso de lectura.
- Flashcards que voltean al hacer clic.
- Simulacro: al elegir una opción, bloquea, marca correcta/incorrecta y muestra retroalimentación; botón "Ver mi resultado" calcula puntaje y temas a reforzar; botón "Reiniciar".
- Botón "Avanzar" al final de cada sección; en la última, "Finalizar Día N" (verde).

== DATOS DE ENTRADA (completa esto) ==
- Código de la guía: [ej. TEC-ESP-01]
- Título: [ej. Competencias del Nivel Técnico]
- Día del plan: [ej. 7]
- Categoría/biblioteca: [General / Por Nivel / Funcional / Por Entidad]
- Nivel (si aplica): [Asistencial / Técnico / Profesional]
- Próxima guía (para el botón Finalizar): [código + nombre]
- TEMA(S) A DESARROLLAR:
[Pega aquí los temas/contenido que debe cubrir la guía]

ENTREGA: el archivo HTML completo, listo para guardar en guias/ y abrir en el navegador.

=== FIN DEL PROMPT ===
```

---

## 🔧 Cómo mejorar este prompt (flujo vivo)

Cuando generemos una guía y digas *"quita esto / agrega esto / cámbialo así"*:
1. Se aplica el cambio a la guía.
2. **Se actualiza el bloque de prompt de arriba** para que el cambio quede como estándar.
3. Se anota la mejora en el **Changelog** de abajo (fecha + qué cambió).

Así, la próxima guía generada ya nace con todas las mejoras y se mantiene **idéntica** a la línea que venimos manejando.

## 📜 Changelog del estándar de guías

| Fecha | Versión | Cambio |
|---|---|---|
| 2026-06-16 | 2.1 | Mejoras al simulacro y al Desarrollo (a partir de feedback en FUN-ALM-01): (1) al hacer clic en una opción se muestran las explicaciones de LAS 4 opciones (por qué cada una es correcta o incorrecta), debajo de cada opción; (2) los contextos y enunciados del simulacro se hacen más largos y difíciles (escenarios con presión, conflicto de intereses, distractores plausibles); (3) el Desarrollo debe incluir un bloque ".fuentes" con enlaces a las fuentes oficiales/normas para profundizar. |
| 2026-06-16 | 2.0 | **Variante Funcional v2** para todas las guías FUN-*: hilo narrativo (.narr), diagramas de proceso (.flujo), checkpoints intercalados "Aplica lo aprendido" (.checkpoint), tarjetas "En la práctica" (.practica) y micro-tips "Ojo en la prueba" (.ojo). Se añade la **regla de reutilización** (guías funcionales entidad-agnósticas) y la **codificación** FUN-[FAMILIA]-Nº + ENT-[SIGLA]-Nº. Se refuerza: feedback por CADA opción y contextos ricos en el simulacro. Primera guía con este estándar: FUN-ALM-01. |
| 2026-06-13 | 1.0 | Versión inicial del prompt, consolidando todas las decisiones tomadas: identidad 60-30-10, 11 secciones, conceptos en 4 capas + sub-bloques desplegables, flashcards, glosario, botón "Avanzar", y **simulacro de juicio situacional** (12 preguntas, 4 opciones A-D, 4-5-3, retroalimentación por opción + temas a reforzar). Reemplaza la regla antigua de 3 opciones del estándar AP-QA-001. |

> Para detalles de implementación (clases CSS, esquema de los arrays JS, validaciones), ver `ESTANDAR-TECNICO.md` y `PLANTILLA-GUIA.md`.
