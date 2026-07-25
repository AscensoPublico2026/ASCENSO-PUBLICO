---
inclusion: always
---

# Regla: numeración del "Día" en las guías (todas las familias y cursos)

> Se carga automáticamente en cada sesión. Aplica a **toda guía existente y futura**, en **todos los cursos**.

## Principio

El número de **día** que se muestra dentro del HTML de una guía **debe ser el día real del curso**, es decir, el valor del campo `"dia"` de esa guía en **`biblioteca/biblioteca.json`** — **NO** el índice de la familia ni el número del código.

- ❌ Error típico: `FUN-SAL-08` mostraba "Día 8" (índice de familia), pero en el curso es el **Día 16**.
- ✅ Correcto: el HTML muestra el mismo día que la plataforma (que lee `biblioteca.json`), evitando que el encabezado y la migaja de pan (breadcrumb) se contradigan.

La fuente de verdad del día es siempre **`biblioteca/biblioteca.json`** (campo `dia`). El código de la guía (`FUN-SAL-08`) es solo un identificador de familia y **no** representa el día.

## Dónde aparece el día en la plantilla estándar

En las guías con día numérico, el número aparece en **3 lugares** y los tres deben coincidir con `biblioteca.json`:

1. **Kicker:** `<div class="kicker">Día N · ...</div>`
2. **Badge:** `<span class="badge">📅 Día N</span>`
3. **Botón/alerta de cierre:** `const FINALIZAR_MSG={"boton": "✅ Finalizar Día N", ...}`

## Excepciones (guías que NO llevan día numérico — respetar su convención)

Algunas familias muestran a propósito una etiqueta en lugar del día numérico. **No** se les debe forzar un "Día N":

- **Comportamentales** (`TEC-COM-*`, `PRO-COM-*`, y sus `-ESP-`): muestran `Nivel Técnico` / `Nivel Profesional`.
- **Introducción** (`INTRO-*`): `Presentación del Curso`.
- **Bonus** (`BON-*`): `Bonus · Todos los niveles`.
- **Conoce tu Entidad** (`ENT-*`): `Conoce tu Entidad`.
- **Simulacros** (`SIM-*`): según su plantilla propia.

## Al crear o editar guías / cursos nuevos

1. Toma el día de `biblioteca/biblioteca.json` (campo `dia`) para esa guía; ese es el número que va en el HTML.
2. Escribe el mismo número en los 3 lugares (kicker, badge, botón "Finalizar").
3. Mantén sincronizadas las dos copias del archivo: `guias/<archivo>.html` y `plataforma/public/seed-guias/<archivo>.html` (usa `scripts/sync-biblioteca.sh`).
4. Si la guía es de una familia sin día numérico (ver excepciones), respeta su etiqueta.

## Verificación rápida (antes de commitear)

```bash
python3 - <<'PY'
import json,re,os
d=json.load(open("biblioteca/biblioteca.json",encoding="utf-8"))
for r in d["guias"]:
    a=r.get("archivo"); dia=r.get("dia")
    if not a or not os.path.exists(a): continue
    h=open(a,encoding="utf-8").read(); head=h.split("</header>")[0]
    m=re.search(r'📅 Día (\d+)',head)
    if m and int(m.group(1))!=dia:
        print("DESAJUSTE:",r.get("codigo"),"html=",m.group(1),"biblioteca=",dia)
print("Verificación de días completada.")
PY
```

Cualquier línea "DESAJUSTE" debe corregirse antes de publicar.
