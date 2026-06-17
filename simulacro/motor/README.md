# 🏭 Motor de Simulacros — Ascenso Público

Genera un simulacro HTML completo **separando el diseño del contenido**. Crear el simulacro de un curso nuevo es **llenar un archivo de contenido (JSON)**, no escribir HTML ni tocar el diseño.

> Mismo enfoque que el motor de guías (`/motor`). El diseño y el flujo de examen quedaron **congelados** con SIM-001.

## Piezas

| Archivo | Qué es | ¿Cambia? |
|---|---|---|
| `base-simulacro.html` | El **molde**: diseño, CSS y JavaScript del "modo examen real" (responder todo → presentar → resultados con revisión y guía de refuerzo). | ❌ Nunca (salvo mejora global de diseño) |
| `../contenido/<CODIGO>.json` | El **contenido** de un simulacro (metadatos + preguntas). | ✅ Uno por simulacro/curso |
| `construir_simulacro.py` | El **ensamblador**: une molde + contenido → HTML final, con validación. | ❌ Casi nunca |
| `construir_todos.py` | Construye **todos** los simulacros de `contenido/*.json` de una vez. | ❌ Casi nunca |

## Cómo crear el simulacro de un curso nuevo

1. Copia un JSON existente como base:
   ```bash
   cp contenido/SIM-001.json contenido/SIM-002.json
   ```
2. Edita los metadatos y, sobre todo, el array `preguntas` del nuevo JSON.
   - `archivo`: nombre del HTML de salida (ej. `SIM-002.html`).
   - **Reutiliza** las preguntas transversales (Generales, Nivel, Ofimática) si el cargo es del mismo nivel; cambia solo las **Funcionales** según el nuevo cargo.
3. Genera el simulacro:
   ```bash
   python3 motor/construir_simulacro.py contenido/SIM-002.json
   ```
4. El HTML queda en `simulacro/`.

## Esquema del JSON

```json
{
  "codigo": "SIM-001",
  "archivo": "SIM-001.html",
  "kicker": "🎯 SIM-001 · Simulacro Final CNSC",
  "titulo": "INDERVALLE — Técnico Operativo 314-03<br>Gestión de Almacén e Inventarios",
  "hero_sub": "Texto bajo el título del encabezado.",
  "cargo": "INDERVALLE Técnico Operativo 314-03",
  "nivel": "Nivel Técnico",
  "tiempo": "90-120 minutos",
  "preguntas": [
    {
      "nivel": "basic | intermediate | advanced",
      "tema": "Tema corto (se muestra en la guía de refuerzo)",
      "ref": "FUN-ALM-02",
      "refT": "Recepción y Verificación de Bienes",
      "ctx": "Contexto largo del caso (>= 200 caracteres ideal).",
      "q": "Párrafo de dilema que replantea la tensión e incita la decisión.",
      "ops": ["Opción 1", "Opción 2", "Opción 3", "Opción 4"],
      "correcta": 0,
      "expl": ["Por qué 1...", "Por qué 2...", "Por qué 3...", "Por qué 4..."]
    }
  ]
}
```

El builder calcula solo: total de preguntas, badges, footer, contador de progreso y el `0/N` del resultado.

## Formato de pregunta tipo CNSC (congelado)
- **Contexto (Caso)** + **párrafo de dilema** (`q`) que incita la decisión; la pregunta va integrada, **no** como enunciado académico ("¿cuál es la actuación más apropiada?").
- **4 opciones** plausibles (cursos de acción) + **4 explicaciones breves** (una por opción), en `expl`.
- Las opciones se **barajan** en cada carga (el molde lo hace con `barajar()`).

## Flujo "modo examen real" (congelado en el molde)
1. El aspirante responde todas las preguntas (puede cambiar su respuesta; no ve aciertos).
2. Presiona **"Presentar examen"** (avisa si faltan preguntas).
3. Recibe: **puntaje + % de aciertos**, **revisión pregunta por pregunta** (su respuesta vs. la correcta + explicación) y **guía de refuerzo** que remite a la guía del curso (`ref` / `refT`) donde estudiar cada tema fallado.

## Validación automática
`construir_simulacro.py` valida antes de generar y **no genera si hay errores**:
- Campos obligatorios presentes.
- Cada pregunta con **4 opciones** y **4 explicaciones**, `correcta` 0-3, sin opciones repetidas.
- `ctx` y `q` presentes (avisa si son cortos).
- Avisa si falta `tema`/`ref` (se usan en la guía de refuerzo).
- Error si todas las respuestas correctas son iguales (patrón obvio).

## Construir todos de una vez
```bash
python3 motor/construir_todos.py
```
Arma todos los simulacros de `contenido/*.json` y reporta un resumen (generados / con errores).

## Ventajas
- **Rápido y barato:** para un curso nuevo solo se produce el JSON; el HTML se ensambla solo.
- **Consistente:** todos los simulacros comparten exactamente el mismo diseño y flujo.
- **Reutilizable:** las preguntas transversales (Generales, Nivel, Ofimática) se reaprovechan entre cargos del mismo nivel; solo cambian las Funcionales.
- **Sin romper nada:** el molde está congelado; el contenido no puede dañar el diseño.
