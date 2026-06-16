# 🏭 Motor de Guías — Ascenso Público

Genera una guía HTML completa **separando el diseño del contenido**. Así crear una guía nueva es **llenar un archivo de contenido**, no escribir HTML.

## Piezas

| Archivo | Qué es | ¿Cambia? |
|---|---|---|
| `base-guia.html` | El **molde**: diseño, CSS y JavaScript (navegación, flashcards, simulacro). | ❌ Nunca (salvo mejora global de diseño) |
| `contenido/<CODIGO>.json` | El **contenido** de una guía (conceptos, casos, 12 preguntas…). | ✅ Uno por guía |
| `construir_guia.py` | El **ensamblador**: une molde + contenido → HTML final. | ❌ Casi nunca |

## Cómo crear una guía nueva

1. Copia un JSON existente como base:
   ```bash
   cp motor/contenido/FUN-ALM-01.json motor/contenido/FUN-ALM-02.json
   ```
2. Edita el contenido del nuevo JSON (título, conceptos, casos, simulacro, etc.).
   - `archivo`: nombre del HTML de salida (ej. `FUN-ALM-02-recepcion-verificacion.html`).
3. Genera la guía:
   ```bash
   python3 motor/construir_guia.py motor/contenido/FUN-ALM-02.json
   ```
4. El HTML queda en `guias/`.

## Ventajas
- **Rápido y barato:** la IA solo produce el JSON (pocos KB), no el HTML completo (~85 KB). Menos créditos, más velocidad.
- **Consistente:** todas las guías comparten exactamente el mismo diseño.
- **Sin romper nada:** el molde está congelado; el contenido no puede dañar el diseño.
- **Listo para automatizar:** el día de mañana, una API puede generar el JSON y este script lo convierte en guía.

## Esquema del JSON (resumen)
`codigo, archivo, titulo, dia, familia, categoria, header_sub, tiempo, proxima,`
`objetivo{narr, intro, lista[], promesa}, importancia{parrafos[], dato_clave},`
`desarrollo{titulo, intro, conceptos[{icono,titulo,def,apl,eje,cnsc, flujo?, subbloques?, practica?, ojo?, checkpoint?}], fuentes{intro, items[]}},`
`comparaciones[], casos[], errores[], tips[], trampas[], flashcards[], resumen[], glosario[], para_recordar, simulacro[]`

> Las capas `eje` y `cnsc` son opcionales (algunos conceptos usan sub-bloques en su lugar).

## Bloques del Desarrollo (estilo editorial v3)

Cada tema del Desarrollo se compone con bloques. Tipos disponibles: `texto`, `definicion`, `idea`, `ejemplo`, `prueba`, `lista`, `tabla`, `acordeon`, `minicheck` y **`calculo`**.

### Bloque `calculo` — fórmulas y procesos matemáticos paso a paso
Todo cálculo (promedio ponderado, PEPS, rotación, stock mín/máx, punto de reorden, porcentajes…) se explica con este bloque, **nunca comprimido en una línea**.

```json
{
  "tipo": "calculo",
  "titulo": "Promedio ponderado, paso a paso",
  "intro": "Qué hace el método, en palabras simples.",
  "datos": ["Compra 1: 100 uds. a $10", "Compra 2: 100 uds. a $12", "Salida: 150 uds."],
  "pasos": [
    {"n": 1, "label": "Costo total de las existencias",
     "formula": "(100 × $10) <b>+</b> (100 × $12) = $1.000 <b>+</b> $1.200",
     "resultado": "$2.200"},
    {"n": 2, "label": "Unidades totales", "formula": "100 <b>+</b> 100", "resultado": "200 unidades"},
    {"n": 3, "label": "Costo promedio por unidad", "formula": "$2.200 <b>÷</b> 200", "resultado": "$11"},
    {"n": 4, "label": "Valor de la salida", "formula": "150 <b>×</b> $11", "resultado": "$1.650"}
  ],
  "total": {"label": "Valor de la salida (150 unidades)", "valor": "$1.650"},
  "nota": "Aclaración o trampa típica del cálculo."
}
```
Campos `intro`, `datos`, `total` y `nota` son opcionales. Resalta los operadores con `<b>`. Ejemplo vivo: `contenido/FUN-ALM-04.json`.

## Simulacro tipo CNSC — reglas que valida el motor
- **12 preguntas** (4 básicas + 5 intermedias + 3 avanzadas), **4 opciones** y **4 explicaciones** (una por opción).
- `ctx` obligatorio y **largo** (caso verosímil, ideal ≥ 220 caracteres). El validador avisa si es corto.
- Opciones no repetidas ni triviales (el validador avisa).
- **El molde baraja las opciones (A/B/C/D) en cada carga** (`barajar()` en `base-guia.html`): el orden visible es aleatorio, así que la posición de la respuesta no es predecible.


## Construir todas de una vez + validación

- `construir_guia.py` ahora **valida** cada guía antes de generarla: 12 preguntas (4-5-3), 4 opciones con sus 4 explicaciones, secciones completas, sin patrones obvios. Si hay un error, no genera y lo reporta.
- `construir_todas.py` arma **todas** las guías de `contenido/*.json` con un solo comando:
  ```bash
  python3 motor/construir_todas.py
  ```
  Reporta un resumen (generadas / con errores). Así garantizamos guías **completas y sin errores**.
