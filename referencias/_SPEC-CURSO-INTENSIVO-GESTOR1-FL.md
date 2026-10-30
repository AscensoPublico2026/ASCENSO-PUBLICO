# SPEC — Curso INTENSIVO 15 días · DIAN Gestor I (301-01) · Fiscalización y liquidación · concurso DIAN 2676 · OPEC 236767

Ficha AT-FL-3008 (Res. 67 de 2024). Nivel Profesional, proceso misional, subproceso Fiscalización y liquidación. Ficha completa y plan de 21 días: `referencias/_SPEC-CURSO-GESTOR1-ANDREA.md`. Prueba: ingreso sin experiencia, funcionales 70 % (eliminatoria, mín. 70,00), comportamentales 20 %, integridad 10 %.

Primer uso: clienta Jessica Paola Caro Julião, que compró la modalidad de 15 días.

## Plan intensivo (duracion: 15) — `dian-gestor-i-fiscalizacion-intensivo-236767`
Exactamente 15 entregas (14 guías + simulacro), sin bonus ni complementarias.

| Día | Código | Tema | Origen |
|---|---|---|---|
| 1 | INTENS-DIAN-01 | Arranque: entidad, prueba y método | Transversal (reutilizada) |
| 2 | INTENS-DIAN-02 | Sistema tributario, aduanero y cambiario | Transversal |
| 3 | INTENS-DIAN-03 | Constitución, función pública, integridad y buen gobierno | Transversal |
| 4 | INTENS-DIAN-04 | CPACA, PQRSF y servicio al ciudadano | Transversal |
| 5 | INTENS-DIAN-05 | Evasión, elusión, contrabando y transparencia | Transversal |
| 6 | INTENS-DIAN-06 | Gestión documental y herramientas informáticas | Transversal |
| 7 | INTENS-DIAN-07 | MIPG | Transversal |
| 8 | INTENS-PRO-08 | Ético (4) y adaptabilidad (2) — nivel profesional | Fusión de DIAN-PRO-COM-01 |
| 9 | INTENS-PRO-09 | Comunicación (2), equipo (3), logro y usuario — nivel profesional | Fusión de DIAN-PRO-COM-02 y 03 |
| 10 | INTENS-GI-10 | Determinación y control tributario; proceso de fiscalización y liquidación | Fusión de FUN-DIAN-02 y 03 |
| 11 | INTENS-GI-11 | Fiscalización aduanera, cautelares, decomiso y destrucción | Fusión de FUN-DIAN-04 (+ FUN-AII-01, FUN-ADM-03) |
| 12 | INTENS-GI-12 | Régimen cambiario de competencia DIAN | Fusión de FUN-DIAN-05 y 05-AIV |
| 13 | INTENS-GI-13 | Fiscalización internacional y LA/FT con ROS | Fusión de FUN-DIAN-06 y 08 |
| 14 | INTENS-GI-14 | Alcance del Gestor I, informes, repaso y Likert | Fusión de DIAN-PRO-COM-04 y FUN-DIAN-09 |
| 15 | SIM-DIAN-001 | Simulacro final 50 + 30 del Gestor I | Reutilizado |

Las INTENS-PRO son reutilizables para cualquier intensivo DIAN de nivel profesional (no nombran el cargo en el título). Las INTENS-GI son propias del Gestor I de fiscalización y liquidación.
Estándar: Desarrollo ≥ 10.000 palabras, 8 módulos con checkpoint, 12 preguntas de 3 opciones (bbbbiiiiiaaa) y 10 flashcards. Validar con `python3 scripts/validar-guia-dian.py <guía> "Analista I|nivel técnico|AT-FL-2013" 10000`. Fuentes en `referencias/fuentes-guias/<código>/`, ensamblar con `scripts/armar-guia.py`.

## Cómo pasar un curso de 21 a 15 días
En /admin/cursos/[id], bloque "Armar plan completo": botón **⚡ Cambiar a intensivo de 15 días** → aparece la plantilla intensiva → **🔄 Rehacer** con ese plan (deja exactamente las 15 entregas).
