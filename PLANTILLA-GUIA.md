# Ascenso Público — Plantilla y checklist para guías nuevas

> **Documento operativo.** Esta es la receta paso a paso para crear cualquier guía nueva (GEN, ASI, TEC, PRO, FUN o ENT) manteniendo la calidad y consistencia del estándar.
>
> **Tiempo estimado de creación:** 60–90 min de trabajo real (contenido + integración).
> **Resultado:** Un único archivo `.html` autocontenido de ~85–120 KB, con 11 secciones, 75–110 min de estudio, simulacro CNSC real.

---

## 1. Antes de empezar — entradas necesarias

Antes de tocar el archivo, ten claros estos 8 datos:

| Dato | Ejemplo | Por qué importa |
|---|---|---|
| **Código** | `GEN-03` | Va en title, header (`.doc-ref`), footer |
| **Nombre completo** | "Marco Institucional" | `<h1>` |
| **Día del plan** | `Día 4 de 21` | Badge, kicker, mensaje de cierre |
| **Categoría** | "Biblioteca General" | Kicker |
| **Subtítulo** | "Conoce las reglas de juego del empleo público" | `.header-sub`, máx 2 líneas |
| **Tiempo objetivo** | `75-90 min` ó `90-110 min` | Badge |
| **Próxima guía** | "GEN-04 · Cargos y nivel" | Mensaje de "Finalizar día" |
| **Lista de 6-8 conceptos** | (ver §3) | Será el corazón del Desarrollo |

**Si te falta alguno → pregunta, no inventes.**

---

## 2. Decisión clave — ¿necesita sub-bloques desplegables?

Para cada concepto, pregúntate: *¿tiene sub-componentes evaluables que la CNSC pregunta por separado?*

| Concepto típico | ¿Sub-bloques? |
|---|---|
| Las Tres Ramas del Poder | ✅ Sí (Legislativa, Ejecutiva, Judicial) |
| Órganos autónomos | ✅ Sí (Control, Electoral, Banca, Otros) |
| 7 principios art. 209 | ✅ Sí (uno por principio) |
| Tipos de servidor público | ✅ Sí (Empleado / Trabajador / Contratista) |
| Derecho de petición | ✅ Sí (general / documentos / consulta) |
| PQRSD | ✅ Sí (Petición / Queja / Reclamo / Sugerencia / Denuncia) |
| Acciones constitucionales | ✅ Sí (Tutela / Popular / Cumplimiento / Grupo) |
| Niveles del empleo | ⚠️ Tabla comparativa basta |
| Definición de Estado | ❌ No, suficiente con 4 capas |
| Función pública (concepto) | ❌ No, suficiente con 4 capas |

**Regla:** Si el concepto tiene **3 o más sub-componentes que aparecen como distractores en preguntas CNSC**, usa sub-bloques. Si no, las 4 capas bastan.

---

## 3. Las 11 secciones — qué contiene cada una

### Sección 1 — 🎯 Objetivo (~2 min)

**Propósito:** Decirle al estudiante qué va a aprender hoy y por qué le sirve para SU vacante.

**Estructura:**
```
1 párrafo introductorio (3-4 líneas)
Lista con check (3-5 items): "Aprenderás a..."
1 box.gold con la promesa: "Al terminar esta guía podrás..."
```

**Tiempo de lectura:** 2 minutos.

---

### Sección 2 — ⭐ Importancia (~3 min)

**Propósito:** Vender la guía. Explicar por qué este día vale la pena.

**Estructura:**
```
2-3 párrafos:
  • Por qué este tema cae en la prueba CNSC
  • Cuántas preguntas históricamente caen sobre esto
  • Qué pasa si NO lo dominas
1 box.info: "Dato clave"
```

---

### Sección 3 — 📖 Desarrollo (25–40 min) ← LA MÁS IMPORTANTE

**Propósito:** Enseñar los 6-8 conceptos clave del día.

**Estructura por concepto (4 capas):**

```html
<div class="concepto">
  <div class="concepto-head">
    <span class="ch-icon">{emoji distintivo}</span>
    <span>{Nombre del concepto}</span>
  </div>
  <div class="concepto-body">

    <!-- 🟦 Capa 1: Definición (qué ES) -->
    <div class="capa cap-def">
      ...
      <p>{2-4 párrafos cortos. Norma + artículo + definición.}</p>
    </div>

    <!-- 🟩 Capa 2: Aplicación (para qué SIRVE) -->
    <div class="capa cap-apl">
      ...
      <p>{Cómo opera en la práctica. Verbos clave que la CNSC usa.}</p>
    </div>

    <!-- 🟨 Capa 3: Ejemplo real (CASO concreto) -->
    <div class="capa cap-eje">
      ...
      <p>{Caso real con NOMBRES: entidad, OPEC, empleado, etc.}</p>
    </div>

    <!-- 🟥 Capa 4: Cómo lo evalúa la CNSC -->
    <div class="capa cap-cnsc">
      ...
      <p>{Cómo aparece en la prueba. Trampa típica. Verbo que usan.}</p>
    </div>

    <!-- (si aplica) Sub-bloques desplegables -->
    <div class="sub-bloques">
      <details class="sb sb-violeta" open>
        <summary>📜 Sub-componente 1</summary>
        <div class="sb-body">
          <p><strong>Quién/qué lo conforma:</strong> ...</p>
          <p><strong>Funciones:</strong> ...</p>
          <div class="box warn">
            <div class="box-title">⚠️ Trampa CNSC</div>
            <p>...</p>
          </div>
          <details class="miniq">
            <summary>🎯 Pregunta tipo CNSC</summary>
            <p>{enunciado}</p>
            <p><strong>✓ Respuesta:</strong> ...</p>
          </details>
        </div>
      </details>
      <details class="sb sb-oro">...</details>
      <details class="sb sb-verde">...</details>
    </div>

  </div>
</div>
```

**Reglas de longitud por capa:**
- Mínimo **2 párrafos cortos** (sin que se sienta perdido el dinero)
- Máximo **4 párrafos cortos** (sin que fatigue)
- Con datos verificables: norma, artículo, fecha, entidad real
- **Nunca:** "es muy importante", "es fundamental" sin sustancia

**Cantidad de conceptos por guía:**
- Mínimo: **5 conceptos**
- Recomendado: **6-8 conceptos**
- Máximo: **10 conceptos** (si superas, dividir en 2 guías)

---

### Sección 4 — ⚖️ Comparaciones (10–15 min)

**Propósito:** Diferenciar conceptos que se confunden en la prueba.

**Estructura:**
```
2-4 tablas comparativas
Cada tabla con 3-5 filas y 3-4 columnas
Bajo cada tabla, un box.warn con la trampa típica
```

**Ejemplos de comparaciones útiles:**
- Empleado público vs Trabajador oficial vs Contratista
- Carrera vs Libre nombramiento vs Provisional
- Petición vs Consulta vs Queja
- Tutela vs Popular vs Cumplimiento

---

### Sección 5 — 📂 Casos (10–15 min)

**Propósito:** Aplicar los conceptos a situaciones reales tipo CNSC.

**Estructura:**
```
5 casos
Cada caso con:
  • caso-head: "Caso N · Título corto"
  • Situación (2-3 líneas, contexto realista)
  • Pregunta (cómo lo preguntaría la CNSC)
  • Respuesta correcta + explicación de por qué
```

**Regla:** Los casos deben ser tipo problema-solución, no tipo trivia.

---

### Sección 6 — ⚠️ Errores frecuentes (~5 min)

**Propósito:** Listar los 6 errores más comunes que el estudiante debe evitar.

**Estructura:**
```
6 box.danger
Cada uno con:
  • Título: "Error N — {error}"
  • Por qué falla: 1-2 líneas
  • Cómo corregir: 1 línea
```

---

### Sección 7 — 💡 Tips (~5 min)

**Propósito:** Atajos de estudio, mnemotecnia, "trucos del mejor estudiante".

**Estructura:**
```
6 box.ok
Mezclar:
  • Mnemotecnia (acrónimos, frases)
  • Trucos de eliminación de distractores
  • Asociaciones con casos famosos
  • Reglas rápidas
```

---

### Sección 8 — 🎭 Trampas tipo CNSC (~5 min)

**Propósito:** Mostrar las 4 trampas que la CNSC usa para confundir.

**Estructura:**
```html
<div class="trampa">
  <div class="trampa-q">{Cómo aparecería la pregunta trampa}</div>
  <div class="trampa-detail">
    <div class="t-row parece">Lo que parece la respuesta...</div>
    <div class="t-row malo">Por qué es trampa...</div>
    <div class="t-row bueno">La respuesta correcta es...</div>
  </div>
</div>
```

**4 trampas mínimo, una por concepto principal del día.**

---

### Sección 9 — 🧠 Repaso (Flashcards, ~5 min)

**Propósito:** Fijar los 10 conceptos clave del día con tarjetas que voltean.

**Estructura:**
- 10 flashcards
- Pregunta corta (front) + respuesta concisa (back)
- Cubrir TODOS los conceptos del Desarrollo (al menos 1 flashcard por concepto)

**Array de datos:**
```js
const flashcards = [
  { f:'¿Pregunta corta?', b:'Respuesta concisa con norma/artículo.' },
  // ... 10 en total
];
```

---

### Sección 10 — 📝 Resumen + Glosario (~3 min)

**Propósito:** Cierre rápido para repasar antes del simulacro.

**Estructura:**
```
Resumen ejecutivo: 6 cards (.resumen-item)
Cada card:
  • Título: concepto en 1 línea
  • Explicación: 1-2 líneas

Glosario: 6 términos clave
Cada uno: término + definición de 1 línea
```

---

### Sección 11 — 🎓 Simulacro (15–20 min)

**Propósito:** Evaluar el dominio del día con 12 preguntas de **juicio situacional**, tal como las pruebas reales de competencias de la CNSC.

**Regla de oro:** son **casos**, no preguntas de memoria. Cada pregunta plantea una situación del día a día del servidor y pide la **actuación más apropiada**. NUNCA "¿qué dice la ley X?".

**Estructura:**
- **12 preguntas** total
- Distribución: **4 básicas + 5 intermedias + 3 avanzadas**
- **4 opciones (A, B, C, D)** — cursos de acción plausibles; solo uno correcto
- **`ctx` presente en TODAS** (el caso/contexto)
- Enunciado tipo "¿qué es lo más apropiado que debe hacer?" / "la actuación correcta es"
- **Cada pregunta tiene `tema`** (para "Temas a reforzar")
- **Cada opción tiene su `expl`** (retroalimentación específica; aquí SÍ se cita la norma para reforzar)
- Respuestas correctas distribuidas **sin patrón** (ej. B,C,A,D,C,A,D,B,A,C,D,B)

**Ejemplo de un item del array `preguntas`:**
```js
{
  nivel: 'i',
  tema: 'Conflicto de intereses',
  ctx: 'Trabajas en el área de contratación. Llega para evaluación una propuesta presentada por la empresa de tu hermano.',
  q: 'Lo más apropiado que debes hacer es:',
  ops: [
    'Evaluarla con objetividad, pues confías en tu imparcialidad',
    'Rechazar la propuesta de inmediato para evitar comentarios',
    'Manifestar el impedimento por conflicto de intereses y apartarte de esa evaluación',
    'Pedirle a un compañero que la firme, pero evaluarla tú igualmente'
  ],
  correcta: 2,
  expl: [
    'Aunque confíes en tu objetividad, el parentesco configura un conflicto de intereses que debes declarar.',
    'No te corresponde rechazar la propuesta; eso afectaría al proponente. Lo correcto es apartarte tú.',
    '✔ Ante un conflicto de intereses, el servidor debe declararse impedido y no participar en la decisión.',
    'Evaluar tú aunque otro firme mantiene el conflicto y agrava la irregularidad.'
  ]
}
```

**Reglas:**
- **Todas** las preguntas llevan `ctx` (un caso realista con nombres/situaciones concretas).
- Enunciados con verbos de acción: "lo más apropiado es", "¿cómo debes proceder?", "la actuación correcta es".
- Distractores = acciones plausibles (no absurdas): omitir, callar, aceptar la dádiva, favorecer, etc.
- La explicación de la opción correcta empieza con `✔` y puede citar el artículo/ley para reforzar el aprendizaje.

---

## 4. Receta paso a paso para crear una guía nueva

### Opción A — Con la plantilla existente (recomendado)

```
1. Tomar GEN-01-estado-funcion-publica.html como BASE
   • Es la versión más completa y aprobada
   • Tiene toda la estructura y estilos congelados

2. Hacer copia con el código nuevo:
   cp GEN-01-estado-funcion-publica.html GEN-03-marco-institucional.html

3. Reemplazar METADATA en el header:
   • <title>{nuevo código} · {nombre} — Ascenso Público</title>
   • .doc-ref → {nuevo código}
   • .kicker → "Día N · Biblioteca General"
   • <h1> → {nombre}
   • .header-sub → {subtítulo}
   • Badge "Día N de 21"

4. Reemplazar el CONTENIDO sección por sección:
   • Objetivo (sec 0)
   • Importancia (sec 1)
   • Desarrollo (sec 2) — reescribir conceptos
   • Comparaciones (sec 3)
   • Casos (sec 4)
   • Errores (sec 5)
   • Tips (sec 6)
   • Trampas (sec 7)
   • Repaso → array `flashcards` (10 nuevas)
   • Resumen + Glosario (sec 9)
   • Simulacro → array `preguntas` (12 nuevas)

5. Actualizar el JS:
   • flashcards = [...] (10 nuevos)
   • preguntas = [...] (12 nuevos)
   • alert de "Finalizar Día N" → mencionar la SIGUIENTE guía

6. Actualizar el footer: "{código} · Día N · v1.0"

7. Validar (ver §5)

8. Commit + push + PR
```

### Opción B — Construcción por bloques (si Opción A falla)

Si la copia falla por tamaño o el `str_replace` rompe algo:

```
1. fs_write con un archivo VACÍO o solo el <head>
2. fs_append: header + nav
3. fs_append: secciones 1, 2 (Objetivo + Importancia)
4. fs_append: sección 3 (Desarrollo) ← la más larga
5. fs_append: secciones 4-7 (Comparaciones, Casos, Errores, Tips, Trampas)
6. fs_append: secciones 8, 9, 10 (Repaso, Resumen, Simulacro)
7. fs_append: el </main>, footer y <script>
```

---

## 5. Validación final (antes de commit)

### Validación visual

- [ ] Abre en el navegador sin consola con errores
- [ ] El header se ve correcto (logo, kicker, badges)
- [ ] La nav sticky funciona y todas las pestañas cambian de sección
- [ ] La barra de progreso de lectura sube al hacer scroll
- [ ] Los conceptos del Desarrollo se ven con sus 4 capas
- [ ] Los sub-bloques se abren/cierran al hacer click
- [ ] Las flashcards voltean al hacer click
- [ ] El simulacro:
  - Muestra el contexto (`ctx`) cuando lo hay
  - Muestra el `nivel-pill` correcto
  - Al click en una opción: bloquea, muestra correcta y feedback
  - Al click en "Ver mi resultado": muestra puntaje + temas a reforzar
  - Al click en "Repetir": resetea
- [ ] Los botones "Avanzar" aparecen al final de cada sección
- [ ] El último botón dice "Finalizar Día N" en verde

### Validación técnica

```bash
# Etiquetas balanceadas
grep -c "<div" {archivo}.html
grep -c "</div>" {archivo}.html
# (deben ser iguales)

grep -c "<details" {archivo}.html
grep -c "</details>" {archivo}.html
# (deben ser iguales)

# Conteo de elementos clave
grep -c 'class="concepto"' {archivo}.html       # 5-10
grep -c 'class="caso"' {archivo}.html           # 5
grep -c 'class="trampa"' {archivo}.html         # 4
grep -c 'class="resumen-item"' {archivo}.html   # 6

# Simulacro
grep -c "nivel:'b'" {archivo}.html              # 4
grep -c "nivel:'i'" {archivo}.html              # 5
grep -c "nivel:'a'" {archivo}.html              # 3
grep -c "correcta:" {archivo}.html              # 12
```

### Validación de contenido

- [ ] Cada concepto tiene **norma + artículo** explícitos en al menos una capa
- [ ] Hay al menos **3 entidades reales** mencionadas (Indervalle, DIAN, SENA, etc.)
- [ ] El simulacro NO tiene preguntas con la misma respuesta seguidas (no `B,B,B`)
- [ ] El simulacro NO tiene patrón obvio (no `A,B,C,D,A,B,C,D...`)
- [ ] Los `expl` de cada opción son específicos (no genéricos)
- [ ] Los `tema` del simulacro coinciden con conceptos del Desarrollo
- [ ] No hay TODO / XXX / FIXME en el contenido
- [ ] Las longitudes de las capas están en 2-4 párrafos

---

## 6. Errores comunes a evitar

### ❌ De contenido

- **Capas de 1 línea** (sensación "perdí mi dinero")
- **Capas de 7+ párrafos** (fatiga lectora)
- **Conceptos sin norma/artículo** ("es importante" sin sustento)
- **Casos abstractos sin nombres reales** (siempre poner Indervalle, DIAN, etc.)
- **Distractores absurdos en el simulacro** (deben ser plausibles)
- **Simulacro con preguntas de memoria de la norma** ("¿qué dice la ley X?") — debe ser **juicio situacional**: un caso + "¿qué es lo más apropiado?"
- **Misma `tema` en múltiples preguntas** sin variar (limitan los temas a reforzar)

### ❌ De forma

- Cambiar la paleta `:root` (¡congelada!)
- Quitar el slogan del header/footer
- Romper la jerarquía de secciones (las 11 son obligatorias)
- Eliminar el botón "Avanzar"
- Modificar el formato del simulacro a 3 opciones (¡el real es 4!)
- Olvidar el `<link rel="icon">` al favicon

### ❌ De flujo

- Crear el archivo sin la estructura `<section data-sec="N">` correcta
- Olvidar incrementar `data-sec` correlativamente (0 a 10)
- No actualizar el JS de flashcards/preguntas (usar las anteriores por error)
- No actualizar el mensaje de "Finalizar Día N" con el día correcto

---

## 7. Plantilla de commits

Convenciones para el repo:

| Tipo de cambio | Formato del mensaje |
|---|---|
| Nueva guía completa | `feat({CODIGO}): {nombre} (Día N) — guía completa` |
| Profundización | `feat({CODIGO}): profundizar {concepto} con sub-bloques` |
| Ajuste de estilo | `style({CODIGO}): {qué se cambió}` |
| Corrección de contenido | `fix({CODIGO}): {qué se corrigió}` |
| Refactor de plantilla | `refactor: {qué se refactorizó}` |
| Cambio del estándar | `docs(estandar): {qué se actualizó}` |

---

## 8. Plantilla de PR

```markdown
## {CODIGO} · {Nombre} — Día N

### Resumen
- Guía completa de la {Biblioteca X}, sigue plantilla maestra y estándar AP-QA-001.
- {N} conceptos en 4 capas, {M} sub-bloques, 5 casos, 4 trampas, 10 flashcards, simulacro CNSC real.
- Tiempo de estudio: {75-90 / 90-110} min.

### Conceptos clave
- {Lista de 6-8 conceptos del Desarrollo}

### Validaciones realizadas
- [ ] Etiquetas HTML balanceadas
- [ ] Simulacro: 12 preguntas (4-5-3), 4 opciones, sin patrón
- [ ] Flashcards: 10 cubriendo todos los conceptos
- [ ] Open en navegador sin errores
- [ ] Botones "Avanzar" funcionan
- [ ] Mensaje de "Finalizar Día N" actualizado

### Próxima guía
{CODIGO siguiente} · {Nombre} (Día N+1)
```

---

## 9. Tabla resumen — qué tiene cada guía nueva

| Sección | Contenido | Cantidad | Tiempo |
|---|---|---|---|
| 1. Objetivo | Lista + promesa | 3-5 items | 2 min |
| 2. Importancia | Párrafos + dato clave | 2-3 párrafos | 3 min |
| 3. Desarrollo | Conceptos en 4 capas + sub-bloques | 6-8 conceptos | 25-40 min |
| 4. Comparaciones | Tablas | 2-4 tablas | 10-15 min |
| 5. Casos | Casos resueltos | 5 casos | 10-15 min |
| 6. Errores | Errores frecuentes | 6 errores | 5 min |
| 7. Tips | Atajos / mnemotecnia | 6 tips | 5 min |
| 8. Trampas | Trampas CNSC | 4 trampas | 5 min |
| 9. Repaso | Flashcards | 10 cards | 5 min |
| 10. Resumen | Cards + glosario | 6+6 | 3 min |
| 11. Simulacro | Preguntas tipo CNSC | 12 (4-5-3) | 15-20 min |
| **TOTAL** | | | **~88-118 min** |

---

*Fin de la plantilla. Para detalles del código ver `ESTANDAR-TECNICO.md`. Para visión general ver `ESTADO-PROYECTO.md`.*
