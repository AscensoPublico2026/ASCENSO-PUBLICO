# 🤖 Prompt — Generador de Planes de Estudio (Ascenso Público)

> **Qué hace:** recibe la información de un empleo (manual de funciones + OPEC + entidad) y genera un **plan de estudio personalizado de 21 días** tipo CNSC.
>
> **Cómo se usa:** copia TODO el bloque de prompt (desde `=== INICIO ===` hasta `=== FIN ===`), pégalo en la IA, reemplaza los campos `[Pegar aquí...]` con la info real y envía.
>
> **Versión:** 3.0 · **Alineado con:** numeración definitiva (INTRO-00 + GEN-01/02/03), formato de simulacro situacional y **fichas de contenido listas para pegar** en `generador-guias.md`.

---

```
=== INICIO DEL PROMPT ===

Actúa como un equipo multidisciplinario conformado por:
- Expertos en concursos de mérito CNSC.
- Especialistas en empleo público colombiano.
- Diseñadores instruccionales.
- Analistas de manuales de funciones.
- Especialistas en evaluación por competencias.
- Expertos en planeación académica.

Tu misión es diseñar un PLAN DE ESTUDIO completamente PERSONALIZADO para un aspirante a un concurso de méritos de la CNSC. Analiza cuidadosamente toda la información suministrada (manual de funciones, OPEC, entidad, propósito del empleo, funciones esenciales y requisitos) y construye una ruta de estudio estratégica orientada a maximizar las probabilidades de éxito en la PRUEBA ESCRITA.

FILOSOFÍA DEL PLAN
- El objetivo NO es enseñar normas de memoria, sino preparar al aspirante para INTERPRETAR, ANALIZAR y RESPONDER correctamente preguntas tipo CNSC (juicio situacional).
- Prioriza competencias y aplicación práctica.
- Identifica los conocimientos funcionales realmente relevantes para el cargo.
- Agrupa conocimientos relacionados y diseña una progresión lógica de aprendizaje.

ESTRUCTURA OBLIGATORIA DEL PLAN (21 días)

DÍA 1 — Introducción (siempre presente)
- INTRO-00 · Presentación del Curso y la CNSC (genérica, ya existe).
- INTRO-01 · Conoce tu Entidad (personalizada: misión, sector y estructura de la entidad de la vacante; encuadre de la OPEC, el cargo y el nivel).

DÍAS 2 a 4 — Biblioteca General (reutilizable, ya existe)
- Día 2 · GEN-01 · Estado y Función Pública.
- Día 3 · GEN-02 · Relación Estado-Ciudadano.
- Día 4 · GEN-03 · Marco Institucional.

DÍAS 5 a 8 — Biblioteca por Nivel
Determina el NIVEL JERÁRQUICO del empleo (Asistencial, Técnico o Profesional) y selecciona ÚNICAMENTE la ruta correspondiente. Las demás NO deben aparecer.
- Si es ASISTENCIAL: ASI-COM-01, ASI-COM-02, ASI-ESP-01, ASI-ESP-02.
- Si es TÉCNICO: TEC-COM-01, TEC-COM-02, TEC-ESP-01, TEC-ESP-02.
- Si es PROFESIONAL: PRO-COM-01, PRO-COM-02, PRO-ESP-01, PRO-ESP-02.
(Basadas en las competencias comportamentales del Decreto 815 de 2018: comunes + específicas por nivel.)

DÍAS 9 a 20 — Guías Funcionales Personalizadas
Analiza a profundidad el cargo: funciones principales, procesos asociados, conocimientos funcionales, normatividad aplicable, procedimientos, herramientas y responsabilidades.
Construye EXACTAMENTE 12 guías funcionales. Cada guía debe AGRUPAR:
- Mínimo 2 temas relacionados.
- Idealmente 3 temas relacionados.
- Máximo 4 temas relacionados.
CODIFICACIÓN Y REUTILIZACIÓN (importante):
- Cada guía funcional se codifica como FUN-[FAMILIA]-[Nº], donde FAMILIA es el dominio de conocimiento (ALM=Almacén, DOC=Gestión Documental, PRO=Procesos/Calidad, MIPG, OFI=Ofimática, ATC=Servicio/apoyo, TIC, FIN, TH, JUR…). El código es global y reutilizable; el "Día" se asigna en este plan.
- Distingue guías de DOMINIO (propias del cargo, p. ej. FUN-ALM-*) de guías TRANSVERSALES reutilizables en casi todos los cargos (FUN-PRO-*, FUN-MIPG-*, FUN-DOC-*, FUN-OFI-*, FUN-ATC-*). Antes de proponer una guía nueva, revisa si ya existe una transversal reutilizable en biblioteca.json y reúsala.
- Las guías funcionales NO mencionan la entidad del aspirante; son entidad-agnósticas. Lo específico de la entidad va solo en la guía de entidad (ENT-[SIGLA]-[Nº]).
REGLAS:
- NO crear una guía por cada tema individual.
- NO copiar el orden literal del manual de funciones.
- Construye bloques de conocimiento coherentes y estratégicos (piensa como diseñador instruccional).
Ejemplo correcto → FUN-ALM-01 "Fundamentos de la Gestión de Almacén" (temas: qué es el almacén, ciclo logístico, tipos de bienes).
Ejemplo incorrecto → una guía por "Gestión documental", otra por "Archivo", otra por "Tablas de retención".

DÍA 21 — Simulacro Integral Final
- SIM-001 · integra Biblioteca General + competencias comunes + competencias del nivel + guías funcionales.

TIEMPO DE ESTUDIO
- Guías funcionales: 75 a 120 min (ideal 90 min).

FORMATO DE SALIDA OBLIGATORIO (DOS PARTES)

PARTE 1 — TABLA DEL PLAN (21 días)
Presenta el plan en una TABLA con estas columnas exactas:
| Día | Código | Guía | Biblioteca | Estado | Temas |
- Columna "Estado": marca "✅ Reusar" si la guía YA existe en la biblioteca, o "🆕 Crear" si hay que generarla.
- Reglas para asignar el Estado:
  • INTRO-00, GEN-01/02/03 y las 4 guías del nivel: SIEMPRE "✅ Reusar".
  • INTRO-01 / Conoce tu Entidad (ENT-…) y el Simulacro final (SIM-…): SIEMPRE "🆕 Crear" (salvo que se indique que ya existen para esta OPEC).
  • Guías funcionales (FUN-…): si en la entrada se pegó la lista de códigos existentes en biblioteca.json, marca "✅ Reusar" las que coincidan (mismo dominio/tema) y "🆕 Crear" las demás. Si NO se pegó la lista, márcalas "🆕 Crear (verificar en biblioteca.json)".
- Para INTRO-01/ENT y las funcionales, detalla en "Temas" lo que personalizaste según el cargo.

PARTE 2 — FICHAS DE CONTENIDO (solo para las guías marcadas "🆕 Crear")
Por CADA guía a crear, entrega un bloque LISTO PARA PEGAR en el Generador de Guías (`prompts/generador-guias.md`), con EXACTAMENTE este formato (son los "DATOS DE ENTRADA" que ese prompt espera, con el temario ya expandido):

------------------------------------------------------------
FICHA → [CÓDIGO] · [Título]
- Código de la guía: [ej. FUN-XXX-0N / ENT-[SIGLA]-01 / SIM-001]
- Título: […]
- Día del plan: [N]
- Categoría/biblioteca: [Funcional / Por Entidad / Simulacro Final]
- Nivel (si aplica): [Asistencial / Técnico / Profesional / —]
- Próxima guía (para el botón Finalizar): [código + nombre de la guía del día siguiente]
- TEMA(S) A DESARROLLAR:
  • Temas (2 a 4): […]
  • Subtemas / conceptos clave por tema: […]
  • Normatividad / artículos a citar (oficiales y verificables): […]
  • Ejemplos por tipo de entidad (alcaldía, hospital, instituto, secretaría): […]
  • Qué evalúa la CNSC / trampas típicas del tema: […]
------------------------------------------------------------

Reglas de las fichas:
- El contenido debe ser SUFICIENTE para que el Generador de Guías produzca la guía completa SIN volver a leer el manual de funciones.
- Reutilización: las guías funcionales NO mencionan la entidad del aspirante (son entidad-agnósticas). Lo específico de la entidad va ÚNICAMENTE en la ficha de la guía ENT-…
- La ficha del Simulacro (SIM-…) NO lista temas nuevos: enumera las GUÍAS del plan que debe integrar (general + nivel + funcionales) para construir el juicio situacional final.
- Entrega las fichas en el mismo orden de los días.

REGLAS DE CALIDAD (verifícalas antes de entregar)
- Día 1 = INTRO-00 + INTRO-01. Días 2-4 = GEN-01/02/03.
- Días 5-8 corresponden ÚNICAMENTE al nivel jerárquico identificado.
- Existen EXACTAMENTE 12 guías funcionales (Días 9-20).
- Cada guía funcional agrupa entre 2 y 4 temas relacionados y coherentes.
- El simulacro final integra todos los conocimientos.
- La ruta tiene progresión lógica y se puede completar en 21 días.
- Cada guía marcada "🆕 Crear" tiene su FICHA DE CONTENIDO (Parte 2) lista para pegar en el generador de guías.

INFORMACIÓN DEL EMPLEO (analiza esto y construye el plan)
[Pegar aquí el Manual de Funciones]
[Pegar aquí la información de la OPEC]
[Pegar aquí información adicional de la entidad, si existe]
[Pegar aquí (OPCIONAL) la lista de códigos de guías ya existentes en biblioteca.json, para marcar cuáles reutilizar]

=== FIN DEL PROMPT ===
```

---

## Notas de mantenimiento

- Si cambia la numeración o la estructura del curso, **actualiza este prompt** y la sección §4 de `PROYECTO-MAESTRO.md`.
- Las guías que el plan referencia se registran en `biblioteca/biblioteca.json`. Si el generador propone una guía funcional nueva, regístrala allí cuando se cree.
- **Flujo completo y portable (independiente de cualquier IA):**
  1. Pega este prompt + el manual + OPEC (+ opcional: códigos existentes de `biblioteca.json`) en cualquier IA → obtienes la **Parte 1 (tabla del plan)** y la **Parte 2 (fichas de contenido)**.
  2. Por cada guía "🆕 Crear", copia su **ficha** y pégala en `prompts/generador-guias.md` (sección DATOS DE ENTRADA) → la IA devuelve el HTML de la guía.
  3. Guarda el HTML en `guias/`, registra la guía en `biblioteca/biblioteca.json`, corre `scripts/sync-biblioteca.sh` y sube con `/api/admin/seed-guias`.
  4. En `/admin/cursos/[id]` asignas la guía por su código.

## Changelog

| Fecha | Versión | Cambio |
|---|---|---|
| 2026-06-16 | 3.0 | La salida ahora tiene 2 partes: (1) tabla del plan con columna **Estado** (✅ Reusar / 🆕 Crear), y (2) **fichas de contenido** por cada guía a crear, en el formato exacto de DATOS DE ENTRADA de `generador-guias.md` (temario expandido: subtemas, normas/artículos, ejemplos por tipo de entidad, qué evalúa la CNSC). Nuevo input opcional: lista de códigos existentes en `biblioteca.json` para marcar reutilización. Hace el plan auto-suficiente y portable a cualquier IA. |
| (previo) | 2.0 | Alineado con numeración definitiva (INTRO-00 + GEN-01/02/03) y simulacro situacional. |
