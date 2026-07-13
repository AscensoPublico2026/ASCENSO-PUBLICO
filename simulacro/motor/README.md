# 🏭 Motor de Simulacros — Ascenso Público

Genera un simulacro HTML completo **ensamblando bloques reutilizables (bancos) + las preguntas propias del cargo**. Crear el simulacro de un curso nuevo es, en la mayoría de los casos, **escribir solo las preguntas funcionales del cargo**: lo demás se reutiliza.

> Mismo enfoque que el motor de guías (`/motor`). El diseño y el flujo de examen quedaron **congelados** con SIM-001.

## Piezas

| Ruta | Qué es | ¿Cambia? |
|---|---|---|
| `motor/base-simulacro.html` | **Molde**: diseño, CSS y JS del "modo examen real". | ❌ Nunca |
| `bancos/*.json` | **Bancos de preguntas reutilizables** (ver abajo). | ➕ Crecen con el tiempo |
| `contenido/<CODIGO>.json` | **Receta** de un simulacro: metadatos + qué bancos usar + funcionales del cargo. | ✅ Una por simulacro |
| `motor/construir_simulacro.py` | **Ensamblador** con validación. | ❌ Casi nunca |
| `motor/construir_todos.py` | Construye **todos** los de `contenido/*.json`. | ❌ Casi nunca |

## 🧱 Bancos reutilizables (`bancos/`)

| Banco | Contenido | Reutilización |
|---|---|---|
| `generales.json` | Estado, función pública, marco institucional (GEN-*). | ♻️ **Todos** los cargos y niveles. |
| `nivel-asistencial.json` | Competencias nivel Asistencial (ASI-*). | Cargos nivel **Asistencial**. |
| `nivel-tecnico.json` | Competencias nivel Técnico (TEC-*). | Cargos nivel **Técnico**. |
| `nivel-profesional.json` | Competencias nivel Profesional (PRO-*). | Cargos nivel **Profesional**. |
| `ofimatica.json` | Ofimática aplicada (BON-02). | Casi todos (ajustar dificultad). |
| `funcionales-comunes.json` | Funcionales transversales: gestión documental, MIPG, sistemas/informes, procesos, servicio al usuario. | La mayoría de cargos. |

> Los bancos de nivel **Asistencial** y **Profesional** están como semilla (vacíos) listos para llenarse cuando se cree un curso de ese nivel.

### 🚫 Regla de oro: los bancos son ENTIDAD-AGNÓSTICOS
Como estos bancos se mezclan en **todos** los simulacros de **todos** los clientes, su `ctx`/`q`/`ops`/`expl` **NUNCA** deben mencionar el nombre de una entidad real (INDERVALLE, Hospital X, DIAN, etc.) ni un contexto operativo exclusivo de un solo cargo (p. ej. "almacén", "quirófano"). Usa siempre lenguaje neutral: *"tu entidad"*, *"la entidad"*, *"tu área"*, *"un compañero de otra dependencia"*. Lo específico del cliente (entidad + funciones reales del cargo) va **únicamente** en el bloque `funcionales` de la receta de ESE simulacro, que no se reutiliza en otros.

Si detectas que un banco quedó con el nombre de una entidad (por ejemplo, porque se copió de una receta existente sin generalizar el texto), corrígelo ahí mismo y reconstruye **todos** los simulacros que usan ese banco (no solo el que detectó el problema), porque el bug se propaga a cualquier curso que lo reutilice:
```bash
python3 motor/construir_todos.py
```
Luego resincroniza con `bash scripts/sync-biblioteca.sh` desde la raíz del repo.

## ✅ Cómo crear el simulacro de un curso nuevo

1. Copia una receta existente:
   ```bash
   cp contenido/SIM-001.json contenido/SIM-002.json
   ```
2. En el nuevo JSON edita:
   - **Metadatos** (`codigo`, `archivo`, `titulo`, `cargo`, `nivel`, `tiempo`, etc.).
   - **`bancos`**: elige los bloques según el nivel (p. ej. cargo Asistencial → `nivel-asistencial`).
   - **`funcionales`**: escribe aquí las preguntas propias del cargo (lo único realmente nuevo).
3. Genera:
   ```bash
   python3 motor/construir_simulacro.py contenido/SIM-002.json
   ```

### Reutilización en la práctica
- **Mismo nivel, otro cargo** → reutilizas Generales + Nivel + Ofimática + Funcionales-comunes; solo escribes `funcionales`. ⚡
- **Otro nivel** → cambias el banco de nivel (ASI/TEC/PRO) y escribes `funcionales`.

## 📄 Esquema de la receta (`contenido/<CODIGO>.json`)

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
  "bancos": ["generales", "nivel-tecnico", "ofimatica", "funcionales-comunes"],
  "funcionales": [ /* preguntas propias del cargo (mismo esquema que un banco) */ ]
}
```

> Retrocompatible: si la receta trae `"preguntas": [...]` en vez de `bancos`/`funcionales`, se usa esa lista directa.

## 📄 Esquema de una pregunta (en bancos y en `funcionales`)

```json
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
```

## Formato de pregunta tipo CNSC (congelado)
- **Contexto (Caso)** + **párrafo de dilema** (`q`) que incita la decisión; la pregunta va integrada, **no** como enunciado académico.
- **4 opciones** plausibles + **4 explicaciones breves** (una por opción).
- Las opciones se **barajan** en cada carga.

## Flujo "modo examen real" (congelado)
1. El aspirante responde todo (puede cambiar; no ve aciertos).
2. **"Presentar examen"** (avisa si faltan preguntas).
3. Resultados: **puntaje + % de aciertos**, **revisión pregunta por pregunta** y **guía de refuerzo** que remite a la guía del curso (`ref` / `refT`).

## Validación automática (no genera si hay errores)
- Campos obligatorios; 4 opciones y 4 explicaciones por pregunta; `correcta` 0-3; sin opciones repetidas.
- `ctx` y `q` presentes (avisa si son cortos); avisa si falta `tema`/`ref`.
- Error si todas las respuestas correctas son iguales (patrón obvio).

## Construir todos de una vez
```bash
python3 motor/construir_todos.py
```

## Ventajas
- **Rápido:** un curso nuevo = escribir las funcionales del cargo; el resto se ensambla.
- **Consistente:** todos los simulacros comparten diseño y flujo.
- **Reutilizable por bloques:** Generales (todos), Nivel (por nivel), Ofimática y Funcionales-comunes (la mayoría).
- **Seguro:** el molde está congelado; el contenido no puede dañar el diseño.
