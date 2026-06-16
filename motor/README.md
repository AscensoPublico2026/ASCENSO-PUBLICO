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


## Construir todas de una vez + validación

- `construir_guia.py` ahora **valida** cada guía antes de generarla: 12 preguntas (4-5-3), 4 opciones con sus 4 explicaciones, secciones completas, sin patrones obvios. Si hay un error, no genera y lo reporta.
- `construir_todas.py` arma **todas** las guías de `contenido/*.json` con un solo comando:
  ```bash
  python3 motor/construir_todas.py
  ```
  Reporta un resumen (generadas / con errores). Así garantizamos guías **completas y sin errores**.
