# 🤖 Prompt — Generador de Guías (Ascenso Público)

> **Qué hace:** recibe un **tema/título + código + día + nivel** y genera una **guía HTML completa** idéntica en formato a las que ya tenemos (INTRO-00, GEN-01/02/03).
>
> **Cómo se usa:** copia el bloque de prompt (`=== INICIO ===` … `=== FIN ===`), pégalo en la IA y completa los datos de entrada al final.
>
> **Documento VIVO:** cada vez que mejoremos una guía ("quita esto / agrega esto"), se actualiza este prompt y se anota en el **Changelog** (al final). Así toda guía nueva nace con las mejoras acumuladas.
>
> **Versión:** 2.2 · **Base técnica:** `ESTANDAR-TECNICO.md` + `PLANTILLA-GUIA.md`.

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
- LONGITUD Y RIQUEZA (OBLIGATORIO E INNEGOCIABLE — replicar y superar el formato real de la prueba escrita CNSC. Este es el estándar permanente de Ascenso Público; TODAS las guías, actuales y futuras, deben cumplirlo):
  * CONTEXTO (ctx): un párrafo robusto de 6 a 10 renglones (mínimo 450, ideal 550–1000 caracteres). Debe describir un escenario verosímil y situado: rol/cargo del servidor, dependencia o servicio, personas involucradas, antecedentes relevantes, la tensión o dilema central, varias presiones concurrentes (tiempo, jerarquía, terceros, recursos, familia) y al menos un elemento distractor plausible que invite al error. Nada de 1–3 frases.
  * ENUNCIADO (q): 2 a 4 renglones (mínimo 180, ideal 220–420 caracteres). No basta "¿qué debe hacer?": debe replantear la tensión del caso, recordar el criterio en juego (norma/competencia/principio) e incitar explícitamente a decidir la actuación MÁS apropiada.
  * OPCIONES (ops): las 4 deben ser LARGAS y ELABORADAS (mínimo 120, ideal 150–280 caracteres cada una), cada una un curso de acción completo y autosuficiente (qué se hace, cómo y con qué matiz/justificación implícita). TODAS plausibles, verosímiles y del mismo nivel de detalle (que la correcta no destaque por ser la más larga o la única elaborada; los distractores deben ser tentadores, no obviamente malos). Evitar opciones de 3–8 palabras.
  * EXPLICACIÓN (expl): una por opción, 1–3 renglones, que argumente con criterio por qué es correcta o por qué falla (puede y conviene citar norma/artículo/principio).
- CALIBRACIÓN OBLIGATORIA: antes de aprobar cada pregunta, verifica que ctx, q y las 4 ops cumplen las longitudes mínimas; si alguna quedó "telegráfica", reescríbela. Ante la duda, MÁS ROBUSTO ES MEJOR: preferir el caso más rico, con más matices y distractores más finos. Las CHECKPOINTS intercaladas pueden ser algo más breves, pero el SIMULACRO final debe igualar o superar la extensión real de la CNSC.
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
| 2026-09-03 | 3.0 | **ESTÁNDAR MÁXIMO consolidado + simulacro con sección Likert + lecciones aprendidas del curso DIAN.** Ver la sección "🧭 ESTÁNDAR v3.0 CONSOLIDADO" y "⚠️ ERRORES COMETIDOS Y CÓMO EVITARLOS" abajo. Resumen: (1) Desarrollo de guías funcionales sube a **MÍNIMO 10.000 palabras**, 10 módulos profundos (600-1.200 palabras c/u), 15+ ejemplos, 3-4 checkpoints, ejercicios con solución, flujos y tablas por módulo, bloque de fuentes con enlaces reales. (2) Simulacro final del curso (SIM-xxx) ahora tiene **DOS secciones**: 50 preguntas funcionales (juicio situacional) + **20 preguntas comportamentales en formato LIKERT** (escala "Muy en desacuerdo" a "Muy de acuerdo", Decreto 815/2018), con perfil por competencia. (3) Reglas anti-fuga, numeración de días, sincronización con bucket de Supabase, y método técnico de construcción por lotes. |
| 2026-07-12 | 2.2 | **Longitud y riqueza tipo CNSC en el simulacro** (feedback del cliente sobre las guías de terapias): se hace OBLIGATORIO que el simulacro replique la extensión real de la prueba escrita CNSC → contexto extenso (5–9 renglones, 450–900 caract.), enunciado que replantea la tensión (2–4 renglones) y **las 4 opciones de respuesta LARGAS y elaboradas** (120–260 caract. c/u), todas del mismo nivel de detalle. Se añade paso de CALIBRACIÓN por longitud antes de aprobar cada pregunta. Antes las preguntas quedaban "telegráficas". |
| 2026-06-16 | 2.1 | Mejoras al simulacro y al Desarrollo (a partir de feedback en FUN-ALM-01): (1) al hacer clic en una opción se muestran las explicaciones de LAS 4 opciones (por qué cada una es correcta o incorrecta), debajo de cada opción; (2) los contextos y enunciados del simulacro se hacen más largos y difíciles (escenarios con presión, conflicto de intereses, distractores plausibles); (3) el Desarrollo debe incluir un bloque ".fuentes" con enlaces a las fuentes oficiales/normas para profundizar. |
| 2026-06-16 | 2.0 | **Variante Funcional v2** para todas las guías FUN-*: hilo narrativo (.narr), diagramas de proceso (.flujo), checkpoints intercalados "Aplica lo aprendido" (.checkpoint), tarjetas "En la práctica" (.practica) y micro-tips "Ojo en la prueba" (.ojo). Se añade la **regla de reutilización** (guías funcionales entidad-agnósticas) y la **codificación** FUN-[FAMILIA]-Nº + ENT-[SIGLA]-Nº. Se refuerza: feedback por CADA opción y contextos ricos en el simulacro. Primera guía con este estándar: FUN-ALM-01. |
| 2026-06-13 | 1.0 | Versión inicial del prompt, consolidando todas las decisiones tomadas: identidad 60-30-10, 11 secciones, conceptos en 4 capas + sub-bloques desplegables, flashcards, glosario, botón "Avanzar", y **simulacro de juicio situacional** (12 preguntas, 4 opciones A-D, 4-5-3, retroalimentación por opción + temas a reforzar). Reemplaza la regla antigua de 3 opciones del estándar AP-QA-001. |

> Para detalles de implementación (clases CSS, esquema de los arrays JS, validaciones), ver `ESTANDAR-TECNICO.md` y `PLANTILLA-GUIA.md`.



---

# 🧭 ESTÁNDAR v3.0 CONSOLIDADO (leer SIEMPRE antes de crear una guía o simulacro)

> Esta sección recoge TODO lo aprendido hasta el curso DIAN Gestor I (sep-2026). Es la fuente de verdad operativa. Si algo aquí contradice el bloque de prompt de arriba, **manda esto**.

## 1) Profundidad de las guías FUNCIONALES (producto premium — "la cara del negocio")
- **Desarrollo: MÍNIMO 10.000 palabras.** Es lo que el cliente valora y por lo que paga (~$300.000). Nunca resúmenes.
- **10 módulos** temáticos, **600–1.200 palabras cada uno**. Cada módulo SIN EXCEPCIÓN debe tener:
  - Subtítulos internos + teoría desarrollada con frases clave en `<mark>` (subrayado dorado, NO fondo).
  - Al menos **una tabla/esquema comparativo**.
  - Al menos **2–3 ejemplos** prácticos desarrollados, ambientados en el rol real del servidor ("como Gestor I de fiscalización de la DIAN…").
  - Un **diagrama de flujo** (`.flujo`) cuando el tema sea un proceso/secuencia.
  - Acordeones (`details.acc`) con contenido complementario real.
  - Bloques "En la práctica" (`.practica`) extensos y realistas.
  - Micro-tips "Ojo en la prueba" (`.ojo`) y recuadros "En la prueba" (`.prueba`).
- **3–4 CHECKPOINTS interactivos** por guía (`.checkpoint` con `.cp-opt` + handler JS), repartidos DENTRO del Desarrollo.
- **EJERCICIOS con solución** dentro del Desarrollo (mini-casos para aplicar, no solo teoría).
- **Cierre del Desarrollo:** box "Idea clave" + box de Tips + box dorado "⚡ Frase para recordar" + bloque `.fuentes` con enlaces DIRECTOS y VERIFICADOS a las normas (secretariasenado.gov.co, funcionpublica.gov.co, corteconstitucional.gov.co, dian.gov.co, etc.).
- **Hilo narrativo:** un caso que abre en la sección Objetivo (`.narr`) y se retoma a lo largo de los módulos, cerrando en el módulo 10 ("resolviendo el caso del inicio").
- Estructura de **11 secciones navegables** (nav sticky): Objetivo · Importancia · Desarrollo · Comparaciones · Casos · Errores · Tips · Trampas · Repaso (flashcards) · Resumen · Simulacro.
- **Simulacro POR GUÍA:** 12 preguntas de juicio situacional (4 básicas + 5 intermedias + 3 avanzadas).
- Benchmarks aprobados: FUN-DIAN-03 (10.373), FUN-DIAN-04 (10.001), FUN-MIPG-01 (10.000), FUN-DOC-01 (10.000).

## 2) Guía "Conoce tu Entidad" (ENT-*) — PREMIUM y REUTILIZABLE por entidad
- ~4.000–4.500 palabras, ~15 secciones navegables. GENERAL para cualquier cargo/nivel de esa entidad (NO menciona cargo/código/OPEC en el cuerpo). Benchmark: ENT-DIAN-01.
- MUCHOS enlaces a fuentes oficiales verificadas, `<mark>` para frases clave, datos/cifras reales (nunca inventar).
- Si el concurso es CNSC, mencionarla como organizadora; si es **régimen especial (PGN)**, NO mencionar CNSC.

## 3) SIMULACRO FINAL DEL CURSO (SIM-xxx) — DOS SECCIONES (diseño v3.0)
### Sección 1 — Funcional (50 preguntas)
- Juicio situacional tipo CNSC. Modo "examen real" (responde todo → presenta → revisión + guía de refuerzo).
- Distribución típica: 6 Generales + 6 Comportamentales del nivel + 32 Funcionales del cargo + resto transversales.
- Dificultad: 15 básicas + 20 intermedias + 15 avanzadas. Contextos 450–1000 caract., 4 opciones 150–280 caract.
### Sección 2 — Comportamental (20 preguntas) · FORMATO LIKERT (NUEVO)
- La prueba comportamental real de la CNSC usa **escala Likert**: afirmaciones situacionales en primera persona que el aspirante califica de "Muy en desacuerdo" a "Muy de acuerdo" (escala de 5 puntos).
- 20 afirmaciones contextualizadas en la entidad/cargo, mapeadas a las competencias del **Decreto 815 de 2018** para el nivel (profesional: Aprendizaje continuo, Experticia profesional, Trabajo en equipo, Creatividad e innovación, Liderazgo de grupos, Toma de decisiones, Orientación a resultados).
- NO tienen respuesta "correcta/incorrecta": miden PERFIL. Al final se muestra un **perfil por competencia** (barras/porcentaje por competencia = suma de calificaciones).
- Motor con **tabs** para navegar entre las dos secciones. Diseño premium Inter + Crimson Pro, navy/gold (reutilizar CSS de `simulacro/SIM-001.html`).

## 4) NUMERACIÓN DE DÍAS (regla dura — ver .kiro/steering/numeracion-dias-guias.md)
- El "Día" mostrado en el HTML sale SIEMPRE del campo `dia` de `biblioteca/biblioteca.json` (o del plan real), NUNCA del número del código.
- Debe coincidir en 3 lugares: kicker (`Día N · …`), badge (`📅 Día N`) y botón de cierre (`✅ Finalizar Día N`).
- Excepciones sin día numérico: comportamentales -COM/-ESP ("Nivel …"), INTRO ("Presentación"), BON ("Bonus"), ENT ("Conoce tu Entidad"), SIM (plantilla propia).

## 5) MÉTODO TÉCNICO DE CONSTRUCCIÓN (para no romper el archivo)
- Escribir el HTML **directamente en el repo** por lotes (con `cat >> archivo << 'EOF'`), NO en /tmp (fs_write y el shell no comparten /tmp). Cuidado con heredocs sin cerrar → duplican contenido.
- Un simulacro de 70 preguntas es un archivo grande (~2.500 líneas). Escribir en **lotes de ~10 preguntas** y verificar líneas tras cada lote para evitar timeouts y corrupción.
- Reutilizar el CSS/JS ya validado (copiar de una guía benchmark con `sed` para adaptar título/día/código).
- **VALIDACIÓN OBLIGATORIA antes de entregar** (con `node -e`): (a) JS válido (`new Function(code)` por cada `<script>`); (b) HTML balanceado (open vs close de div/section/table/details); (c) conteo de palabras del Desarrollo ≥ 10.000; (d) 0 fugas; (e) día coherente; (f) todo botón con handler; (g) enlaces `target="_blank"` que abren la norma real.
- **BUG RECURRENTE:** en el array `preguntas` de JS NUNCA usar `ops3:` como key. SIEMPRE `ops:['op1','op2','op3','op4']` (las 4 opciones como strings dentro del array).

## 6) SINCRONIZACIÓN Y DESPLIEGUE
- Tras crear/editar una guía: actualizar `biblioteca/biblioteca.json` (campo `archivo`, `dia`, `temas`) y correr `bash scripts/sync-biblioteca.sh` (requiere `chmod +x`) que copia catálogo + HTML a `plataforma/lib/` y `plataforma/public/seed-guias/`.
- Las guías se sirven del **bucket de Supabase** ('guias'), NO directo del repo. Al MEJORAR una guía existente, el estudiante sigue viendo la versión vieja hasta re-subir el bucket: como admin visitar `https://ascensopublico.com/api/admin/seed-guias` (upsert=true) y recargar sin caché. El endpoint del estudiante auto-sube desde seed-guias solo si la guía NO existe aún en el bucket.
- Merge: enviar a Julio el **link directo** de crear PR (`https://github.com/AscensoPublico2026/ASCENSO-PUBLICO/pull/new/<rama>`), sin pasos intermedios.

## 7) EXPEDIENTES DE ASPIRANTES (un archivo = un aspirante)
- Cada aspirante tiene su carpeta en `referencias/expedientes/<slug-nombre>/` con: `expediente.md` (auditoría a profundidad), `documentos/LEEME.md` (para que suba PDFs) y `manuales-vacantes/` (fichas OPEC/manual de funciones).
- El expediente audita: datos, formación (verificada por diploma), experiencia (cómputo por norma del concurso), vacante objetivo + cumplimiento requisito por requisito, documentación recibida/pendiente y RIESGOS.
- NO mezclar información entre aspirantes. El USUARIO/cliente es **Julio César** (fundador); los aspirantes son los destinatarios del curso.

---

# ⚠️ ERRORES COMETIDOS Y CÓMO EVITARLOS (bitácora viva)

> Anotar aquí cada error real para no repetirlo. Actualizar en cada sesión.

1. **Guías con estructura "microlearning" incompatible.** Guías viejas (p.ej. la vieja FUN-MIPG-01 de 23 secciones cortas) NO sirven con el estándar actual. → Crear una NUEVA con nombre distinto y estructura de 11 secciones + 10 módulos; actualizar el `archivo` en biblioteca.json.
2. **FUGAS de contenido cruzado.** Las guías se reutilizan entre cursos → riesgo alto de que quede el nombre de otro aspirante, cargo/código ajeno, otra entidad (URT, INDERVALLE), otro concurso (89-2026) o "CNSC" cuando el concurso es de régimen especial (PGN). → ANTES de asignar, auditar con grep: `Sandra`, `Sustanciador`, `4SU-08`, `URT`, `INDERVALLE`, `Procurador`, `Gina`, `PGN`, `CNSC` (según corresponda). Reescribir el ENFOQUE, no solo cambiar términos.
3. **Día equivocado.** Se mostró el número del código en vez del día real del plan. → Tomar el día de biblioteca.json y verificarlo en kicker/badge/footer/JS.
4. **`</practica>` y otros cierres inventados.** Se cerró un `.practica` con `</practica>` (no existe en HTML) → desbalance de `<div>`. → Los bloques `.practica`, `.ojo`, `.checkpoint` son `<div>`: se cierran con `</div>`.
5. **`ops3:` en el simulacro.** Error de sintaxis JS recurrente. → SIEMPRE `ops:['a','b','c','d']`.
6. **Word count por debajo de 10.000.** Varias guías quedaron en 8.000–9.900. → Medir con `node -e` el Desarrollo (sección data-sec="2") y ampliar módulos hasta pasar 10.000 ANTES de hacer push.
7. **Heredoc que duplica contenido.** Un `cat >> << 'EOF'` mal cerrado repite el bloque. → Verificar `wc -l` y `tail` tras cada lote; si se duplicó, recortar con `head -N`.
8. **Cifras inventadas.** No inventar número de vacantes/plazas ni datos de la entidad. Si no hay fuente oficial confiable, redacción genérica.
9. **Archivo grande → timeouts.** Escribir simulacros/guías en lotes pequeños; considerar delegar en sub-agente con instrucciones muy detalladas, pero verificar SIEMPRE el resultado (el sub-agente puede quedar corto en palabras).
10. **Régimen especial vs CNSC.** PGN NO es CNSC. En cursos de PGN no mencionar a la CNSC como organizadora ni en guías ni en simulacros.
11. **Texto invisible en el subtítulo del header.** El CSS base trae `strong{color:var(--azul)}`. Como el header tiene fondo azul, las palabras en `<strong>` dentro de `.header-sub` salen azul sobre azul → INVISIBLES. → El molde DEBE incluir SIEMPRE la regla `.header-sub strong{color:#fff;font-weight:700}` justo después de `.header-sub{...}`. Verificar con grep tras crear cada guía.
12. **Simulacros telegráficos.** Casos/enunciados/opciones demasiado cortos se ven pobres y poco profesionales. → CONTEXTO 6-10 renglones (mín 550, ideal 650-1100 caracteres) con escenario situado, varias presiones y un distractor; ENUNCIADO 2-4 renglones que replantea la tensión (mín 180 car); 4 OPCIONES largas y elaboradas (mín 150, ideal 180-320 car c/u), todas plausibles y del mismo nivel de detalle. Nunca opciones de una línea.

---

# 🏛️ NOTA PGN (Procuraduría General de la Nación) — régimen ESPECIAL

- La PGN organiza su **propio** concurso (NO la CNSC). No mencionar CNSC como organizadora en guías/simulacros de PGN.
- Matriz fuente de vacantes: `Convocatorias_Procuraduria.xlsx` (296 vacantes / 2.824 plazas).
- Temario funcional típico PGN (nivel profesional): función disciplinaria (CGP/Ley 1952 de 2019 y reforma Ley 2094/2021), función de instrucción/investigación, intervención judicial, MASC/conciliación, DDHH y DIH, justicia transicional, contratación estatal, CPACA, control interno/MIPG, gestión documental. Reutilizar familias FUN-* existentes (FUN-JUR, FUN-DDHH, FUN-CONC, FUN-MIPG, FUN-DOC…) y crear las específicas del cargo con enfoque de nivel profesional ("interviene y decide con criterio").
- Guía de entidad: ENT-PGN-01 (ya existe) / ENT-PGN-PRO-01 (versión nivel profesional). Verificar cuál aplica y que no tenga fugas de otro aspirante.
