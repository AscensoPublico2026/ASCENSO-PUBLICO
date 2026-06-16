# 🤖 Prompt — Generador de Planes de Estudio (Ascenso Público)

> **Qué hace:** recibe la información de un empleo (manual de funciones + OPEC + entidad) y genera un **plan de estudio personalizado de 21 días** tipo CNSC.
>
> **Cómo se usa:** copia TODO el bloque de prompt (desde `=== INICIO ===` hasta `=== FIN ===`), pégalo en la IA, reemplaza los campos `[Pegar aquí...]` con la info real y envía.
>
> **Versión:** 2.0 · **Alineado con:** numeración definitiva (INTRO-00 + GEN-01/02/03) y formato de simulacro situacional.

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

FORMATO DE SALIDA OBLIGATORIO
Presenta el plan en una TABLA con estas columnas exactas:
| Día | Código | Guía | Biblioteca | Temas |
(Para INTRO-01 y las funcionales, detalla los temas que personalizaste según el cargo.)

REGLAS DE CALIDAD (verifícalas antes de entregar)
- Día 1 = INTRO-00 + INTRO-01. Días 2-4 = GEN-01/02/03.
- Días 5-8 corresponden ÚNICAMENTE al nivel jerárquico identificado.
- Existen EXACTAMENTE 12 guías funcionales (Días 9-20).
- Cada guía funcional agrupa entre 2 y 4 temas relacionados y coherentes.
- El simulacro final integra todos los conocimientos.
- La ruta tiene progresión lógica y se puede completar en 21 días.

INFORMACIÓN DEL EMPLEO (analiza esto y construye el plan)
[Pegar aquí el Manual de Funciones]
[Pegar aquí la información de la OPEC]
[Pegar aquí información adicional de la entidad, si existe]

=== FIN DEL PROMPT ===
```

---

## Notas de mantenimiento

- Si cambia la numeración o la estructura del curso, **actualiza este prompt** y la sección §4 de `PROYECTO-MAESTRO.md`.
- Las guías que el plan referencia se registran en `biblioteca/biblioteca.json`. Si el generador propone una guía funcional nueva, regístrala allí cuando se cree.
