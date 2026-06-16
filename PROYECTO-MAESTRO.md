# 🧭 PROYECTO MAESTRO — Ascenso Público

> ⚠️ **DOCUMENTO HISTÓRICO / PARCIALMENTE DESACTUALIZADO.** El estado real (lo hecho, lo pendiente y el próximo paso) vive en **`CONTINUIDAD.md`** (fuente de verdad). Varias cosas que aquí figuran como "pendiente/por iniciar" (mergear BON-01, plataforma, panel del estudiante/admin, specs de guías funcionales y del simulacro) **YA están hechas**. Este archivo conserva valor para el *porqué* y la visión; para el *estado actual*, consulta `CONTINUIDAD.md`.

> **Este es el documento NORTE del proyecto.** Contiene la idea de inicio a fin, las decisiones tomadas, el estado actual y el paso siguiente.
>
> **Dos usos:**
> 1. **Para César (fundador):** si pierdes el rumbo, abre este documento y te re-centra.
> 2. **Para una IA (handoff):** si cambias de asistente, pega o comparte este documento. La IA leerá y entenderá de qué trata el proyecto, qué se ha hecho, qué falta y por dónde seguir.
>
> **Regla:** este documento se mantiene vivo. Cada vez que se completa algo importante, se actualiza la sección **§9 Estado actual**.

**Última actualización:** 14 de junio de 2026

---

## 1. Qué es Ascenso Público

**Ascenso Público** es una plataforma de **preparación personalizada para concursos de méritos de la CNSC** (Comisión Nacional del Servicio Civil, Colombia).

- **Eslogan:** *Tu ruta personalizada hacia el empleo público.*
- **Nombre comercial:** Ascenso Público.
- **Idea central:** no preparamos para "una convocatoria" en general; preparamos para **el cargo específico** al que aspira cada persona.

---

## 2. El problema y la propuesta de valor

### El problema (origen de la idea)
La idea nace de una necesidad real del fundador al prepararse para un concurso CNSC. Los cursos del mercado ofrecían PDFs extensos, videos poco dinámicos, simulacros genéricos y preparación para toda una convocatoria (no para una vacante). El aspirante **no sabía exactamente qué estudiar para su cargo**.

> El aspirante no necesita más información. Necesita saber **exactamente qué estudiar**.

### La propuesta de valor
Preparación personalizada basada en: **OPEC · Manual de funciones · Nivel jerárquico · Competencias del cargo · Forma de evaluación CNSC**.

> No vendemos contenido. Diseñamos una preparación personalizada para cada aspirante.

### Filosofía
> No se trata de estudiar más. Se trata de **estudiar mejor**.

### Diferenciadores
- **Personalización** por cargo (no por convocatoria).
- **Interpretación de la OPEC** y del manual de funciones (funciones reales del empleo).
- **Experiencia de aprendizaje** que mantiene la atención, facilita la comprensión y evita el aburrimiento.
- **Preguntas tipo CNSC** (situacionales).
- **Estrategias CNSC**: identificar trampas, interpretar escenarios, entender cómo piensa la CNSC.

---

## 3. Cómo funciona (flujo del cliente)

1. **Compra:** el usuario adquiere el curso.
2. **Datos:** diligencia nombre, correo, celular, convocatoria, OPEC y **manual de funciones** (PDF).
3. **Acceso inmediato:** entra a la plataforma con estado *"Curso en preparación"* + barra de progreso.
4. **Análisis:** Ascenso Público analiza OPEC, funciones, competencias y nivel jerárquico.
5. **Construcción:** se arma la **ruta de estudio personalizada** (hasta ~12 horas; pendiente validar tiempo).
6. **Habilitación:** el curso pasa a estado *"Curso listo"* y el estudiante accede a sus guías por día.

El estudiante avanza a su ritmo; tendrá acceso al material por un tiempo definido (pendiente fijar, ~60 días).

---

## 4. Estructura del curso (21 días)

El curso está diseñado para ~1 mes de estudio, organizado en días.

| Días | Bloque | Detalle |
|---|---|---|
| **1** | Introducción | INTRO-00 (presentación + CNSC) + **INTRO-01 (Conoce tu Entidad)**, que se crea con la compra |
| **2–4** | Biblioteca General | GEN-01 Estado y Función Pública · GEN-02 Relación Estado-Ciudadano · GEN-03 Marco Institucional |
| **5–8** | Biblioteca por Nivel | Según el nivel del cargo: Asistencial / Técnico / Profesional (competencias Decreto 815/2018) |
| **9–20** | Biblioteca Funcional | 12 guías funcionales según las funciones reales del cargo (cada una agrupa 2–4 temas) |
| **21** | Evaluación | SIM-001 — Simulacro Integral Final |
| Bonus | Estrategia CNSC | BON-01 — aplica a todos los niveles |

### Las 4 bibliotecas (contenido reutilizable)
- **A) General** — igual para todos (INTRO-00 + GEN-01/02/03).
- **B) Por Nivel** — depende del nivel jerárquico (Asistencial/Técnico/Profesional).
- **C) Funcional** — depende de las funciones del cargo; se reutiliza cuando otro cargo comparte la función.
- **D) Por Entidad** — INTRO-01 "Conoce tu Entidad"; se crea con cada compra y se reutiliza (códigos `ENT-xxx`).

> El catálogo completo de guías (publicadas y pendientes, con sus temas) vive en **`biblioteca/`** (ver `biblioteca/BIBLIOTECA.md`).

---

## 5. Identidad de marca (CONGELADA)

- **Logo:** versión V2 (flecha con impulso). Variantes en `brand/` (gold, navy, mark, favicon, TikTok).
- **Paleta 60-30-10:** fondo crema `#FBF9F4` · azul institucional `#0A2A5E` · dorado `#E8A33D`.
- **Estilo:** moderno, profesional, académico, limpio. Cálido pero ordenado (cada color tiene un significado fijo).
- **Encabezado obligatorio:** "Ascenso Público" + eslogan.

---

## 6. Estándar de cada guía (resumen)

Cada guía es un **archivo HTML autocontenido** (abre en el navegador), con **11 secciones**, **75–110 min** de estudio, conceptos en **4 capas** (Definición → Aplicación → Ejemplo real → Cómo lo evalúa la CNSC) y sub-bloques desplegables cuando hay sub-componentes evaluables.

- Detalle de **código/CSS/JS** de los componentes → `ESTANDAR-TECNICO.md`.
- **Checklist paso a paso** para crear una guía → `PLANTILLA-GUIA.md`.
- **Prompts** para generar plan y guías → carpeta `prompts/`.

---

## 7. El simulacro (regla clave) — JUICIO SITUACIONAL

Las pruebas reales de la CNSC son de **juicio situacional**. Por lo tanto, **todos** los simulacros de Ascenso Público deben ser así:

- **Tipo:** caso/contexto real + enunciado "¿qué es lo más apropiado que debe hacer?".
- **NO** se pregunta la norma de memoria ("¿qué dice la ley X?").
- **12 preguntas** por guía · distribución **4 básicas + 5 intermedias + 3 avanzadas**.
- **4 opciones (A, B, C, D)** — *(esto actualiza el estándar original AP-QA-001, que decía 3 opciones; tras investigar el formato real de la CNSC se fijó en 4).*
- **Retroalimentación por opción** (aquí sí se cita la norma, para reforzar) + **lista de temas a reforzar** al final.
- Distractores plausibles basados en errores reales (extralimitación, omisión, incumplimiento de procedimiento, afectación al servicio, interpretación parcial, desconocimiento del alcance del cargo).
- Proporción ideal: ~80% juicio situacional, ~20% conceptual aplicado.

---

## 8. Mapa del repositorio (qué es cada cosa)

```
ASCENSO-PUBLICO/
├── README.md                  · Índice/puerta de entrada del repo
├── PROYECTO-MAESTRO.md        · 🧭 ESTE documento (norte + handoff)
├── PLAN-PROYECTO.md           · 📊 Gestión: fases, cronograma, % de avance, hitos
├── ARQUITECTURA-PLATAFORMA.md · 🏗️ Plano de la plataforma web (landing, portal, admin)
├── ESTANDAR-TECNICO.md        · 🛠️ Código (CSS/HTML/JS) de los componentes de las guías
├── PLANTILLA-GUIA.md          · ✅ Checklist paso a paso para crear una guía nueva
├── prompts/                   · 🤖 Prompts reutilizables
│   ├── generador-plan-estudio.md   · genera el plan de 21 días desde OPEC + manual
│   └── generador-guias.md          · genera una guía HTML desde un tema (vivo, se actualiza)
├── biblioteca/                · 📚 Catálogo maestro de guías (reemplaza el Excel)
│   ├── biblioteca.json             · fuente de verdad
│   ├── BIBLIOTECA.md               · índice legible (generado)
│   ├── generar_indice.py           · regenera el índice
│   └── README.md                   · cómo registrar una guía
├── guias/                     · 🎓 Guías HTML definitivas (abren en el navegador)
├── brand/                     · 🎨 Logos oficiales (SVG + PNG) y guía de uso
└── .kiro/steering/            · ⚙️ Reglas para el asistente IA (se cargan solas)
```

> **Nota histórica:** los documentos originales `.docx` (Fundacional, Estándar de Calidad, Prompt de Planes) y el `BIBLIOTECA.xlsx` se **convirtieron a Markdown** y se retiraron del repo para evitar duplicidad. Su contenido vive ahora en este documento, en `ESTANDAR-TECNICO.md`, `PLANTILLA-GUIA.md`, `prompts/` y `biblioteca/`. El historial git los conserva.

---

## 9. Estado actual ⭐ (se actualiza siempre)

> Para la **vista de gestión** (fases, cronograma, % de avance, hitos) ver **`PLAN-PROYECTO.md`**.

### ✅ Hecho
- Identidad de marca y logo (V2) — congelados.
- Plantilla maestra de guía (diseño + componentes) — congelada.
- **Biblioteca General COMPLETA:** INTRO-00, GEN-01/02/03 (Días 1–4).
- **Biblioteca por Nivel COMPLETA:** Asistencial, Técnico y Profesional — 12 guías (Días 5–8).
- Simulacros en **juicio situacional** con encuadre fiel a la CNSC (comportamental vs funcional) en las 12 guías por nivel.
- **BON-01 — Estrategia CNSC** construido *(PR pendiente de merge)*.
- Repositorio limpio; biblioteca versionable (`biblioteca/`); documentación maestra y de gestión.

### 🔜 Próximo paso inmediato
- **Fase 2 — Diseño de lo personalizable:** especificar el molde de las **guías funcionales** (Días 9–20) y del **simulacro final SIM-001**. En paralelo, abrir **landing page** y **línea de TikTok**.

### ⬜ Pendiente (orden sugerido)
1. Mergear BON-01 (cierra el contenido reutilizable).
2. Spec de diseño de **guías funcionales** + decisión de guías adicionales.
3. Spec de diseño del **simulacro final** (SIM-001, personalizado por OPEC).
4. **Landing page** y **TikTok** (en paralelo).
5. Plataforma web (compra, panel del estudiante con barra de progreso, panel admin).
6. Producción a demanda por cliente (funcionales + INTRO-01 + SIM-001).
7. (Visión futura) Automatización IA: analizar OPEC + manual → generar plan → generar guías → publicar.

> **Decisión registrada:** SIM-001 es **personalizado por cliente** (se arma con todas las guías de su plan y se enfoca en la OPEC).

---

## 10. Decisiones congeladas (no cambiar sin acuerdo)

1. **Numeración:** Día 1 = INTRO-00 (+ INTRO-01 bajo demanda). GEN-01 = Día 2, GEN-02 = Día 3, GEN-03 = Día 4. (La "Introducción CNSC" quedó absorbida en INTRO-00.)
2. **Guías:** HTML autocontenido, 11 secciones, 75–110 min, 4 capas + sub-bloques, favicon `../brand/favicon.svg`.
3. **Identidad:** paleta 60-30-10 (crema/azul/dorado), logo V2, eslogan en header y footer.
4. **Simulacro:** juicio situacional, 12 preguntas, 4 opciones (A–D), 4-5-3, retroalimentación por opción + temas a reforzar.
5. **Biblioteca:** fuente de verdad `biblioteca/biblioteca.json`; índice generado con `generar_indice.py`.
6. **Guías por nivel:** basadas en competencias del Decreto 815/2018 (comunes + específicas por nivel).

---

## 11. Cómo retomar el proyecto (handoff)

**Si eres una IA que toma el proyecto, haz esto:**
1. Lee este documento completo (es el norte).
2. Lee `.kiro/steering/proyecto-ascenso-publico.md` (reglas operativas).
3. Revisa `biblioteca/BIBLIOTECA.md` (qué guías hay y cuáles faltan).
4. Para crear una guía: usa `prompts/generador-guias.md` + `PLANTILLA-GUIA.md`, partiendo de una guía publicada en `guias/` como base.
5. Respeta las **decisiones congeladas** (§10).
6. Al terminar algo, **actualiza §9** y registra la guía en `biblioteca/biblioteca.json` (+ regenera el índice).

**Objetivo final del proyecto:** ser la plataforma líder de preparación **personalizada por cargo** para concursos de mérito en Colombia.
