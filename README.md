# Ascenso Público

> **Plataforma de cursos personalizados para concursos de la CNSC** (Comisión Nacional del Servicio Civil, Colombia).
> El cliente compra un curso adaptado a su vacante (OPEC + manual de funciones) y recibe un plan de 21 días con guías HTML interactivas + simulacro final.
>
> *Slogan: Tu ruta personalizada al ascenso público.*

---

## 📁 Estructura del repositorio

```
ASCENSO-PUBLICO/
├── README.md                      ← este índice (puerta de entrada)
├── PROYECTO-MAESTRO.md            ← 🧭 documento NORTE: idea completa + estado + handoff
├── ESTANDAR-TECNICO.md            ← 🛠️ código CSS/HTML/JS de los componentes
├── PLANTILLA-GUIA.md              ← ✅ checklist paso a paso para crear una guía
├── prompts/                       ← 🤖 prompts reutilizables
│   ├── generador-plan-estudio.md  · genera el plan de 21 días desde OPEC + manual
│   └── generador-guias.md         · genera una guía HTML desde un tema (vivo)
├── biblioteca/                    ← 📚 catálogo maestro de guías (reemplaza el Excel)
│   ├── biblioteca.json            · fuente de verdad (códigos, estado, temas)
│   ├── BIBLIOTECA.md              · índice legible (generado)
│   ├── generar_indice.py          · regenera el índice desde el JSON
│   └── README.md                  · cómo registrar una guía
├── guias/                         ← 🎓 guías HTML definitivas (abren en el navegador)
│   ├── INTRO-00-presentacion-curso.html      · Día 1 — Presentación del curso + CNSC
│   ├── GEN-01-estado-funcion-publica.html    · Día 2 — Estado y Función Pública
│   ├── GEN-02-relacion-estado-ciudadano.html · Día 3 — Relación Estado-Ciudadano
│   └── GEN-03-marco-institucional.html       · Día 4 — Marco Institucional
├── brand/                         ← 🎨 logos oficiales (SVG + PNG) y guía de uso
└── .kiro/steering/                ← ⚙️ reglas para el agente AI (se cargan solas)
```

> 🧭 **¿Nuevo en el proyecto (o eres otra IA)?** Empieza por **[`PROYECTO-MAESTRO.md`](PROYECTO-MAESTRO.md)**: contiene la idea completa, el estado actual y el paso siguiente.

---

## 🎓 Las guías (cómo verlas)

Cada guía es un **archivo HTML autocontenido**: ábrelo con doble clic en cualquier navegador. No necesita internet (salvo la primera carga de fuentes de Google).

| Día | Código | Guía | Categoría | Estado |
|---|---|---|---|---|
| 1 | INTRO-00 | Presentación del Curso y CNSC | Bienvenida (genérica) | ✅ |
| 1 | INTRO-01 | Introducción a la Entidad | Bienvenida (se crea **bajo demanda** al comprar) | ⏳ por demanda |
| 2 | GEN-01 | Estado y Función Pública | Biblioteca General | ✅ |
| 3 | GEN-02 | Relación Estado-Ciudadano | Biblioteca General | ✅ |
| 4 | GEN-03 | Marco Institucional | Biblioteca General | ✅ |
| 5–8 | — | Guías por Nivel (Asistencial/Técnico/Profesional) | Biblioteca por Nivel | 🔜 siguiente |
| 9–20 | — | Guías Funcionales (según el cargo) | Biblioteca Funcional | ⬜ |
| 21 | SIM-001 | Simulacro Integral Final | Evaluación | ⬜ |

> ✅ **La Biblioteca General (Días 1–4) está completa.**

📚 **Catálogo completo de guías** (publicadas y pendientes, con sus temas): ver [`biblioteca/BIBLIOTECA.md`](biblioteca/BIBLIOTECA.md).

---

## 🎨 Identidad y estándar (congelados)

- **Logo:** V2 (flecha con impulso). Variantes en `brand/`.
- **Paleta 60-30-10:** crema `#FBF9F4` · azul `#0A2A5E` · dorado `#E8A33D`.
- **Cada guía** tiene 11 secciones, 75–110 min de estudio, conceptos en 4 capas + sub-bloques, y un **simulacro de juicio situacional** (12 preguntas, 4 opciones, casos reales — no memoria de la norma).

Detalles completos en [`PROYECTO-MAESTRO.md`](PROYECTO-MAESTRO.md), `ESTANDAR-TECNICO.md` y `PLANTILLA-GUIA.md`.

---

## 🚀 Cómo continuar el proyecto

1. Lee **[`PROYECTO-MAESTRO.md`](PROYECTO-MAESTRO.md)** (idea completa, estado y paso siguiente).
2. Para crear una guía nueva, usa `prompts/generador-guias.md` + `PLANTILLA-GUIA.md` (vía rápida: parte de una guía publicada en `guias/`).
3. Para generar el plan de 21 días de un aspirante, usa `prompts/generador-plan-estudio.md`.
4. Respeta las decisiones congeladas y la identidad de marca.
5. Próximo paso sugerido: **Biblioteca por Nivel (Día 5+)**.
