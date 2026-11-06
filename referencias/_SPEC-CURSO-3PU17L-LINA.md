# SPEC — Curso PGN Profesional Universitario 3PU-17 Instrucción (Lina Lucía Ramírez Rodríguez · Conv. 146-2026)

> Plan plantilla: `pgn-profesional-3pu17-lina`. Sufijo de archivos: **-3PU17L**.

## 1. Cargo (fuente: formato de convocatoria TH-F-211 v3, Conv. 146-2026, Res. 212 de 2026)
| Dato | Valor |
|---|---|
| Aspirante | Lina Lucía Ramírez Rodríguez |
| Cargo | Profesional Universitario 3PU-17 · Nivel Profesional · $8.972.318 (2025) |
| Plazas | 19 · Procuradurías Regionales de Instrucción (Bolívar, Cesar, Chocó, Córdoba, La Guajira, Meta, Sucre, Valle) y Provinciales de Instrucción (Barranquilla ×2, Bucaramanga, Carmen de Bolívar, Cartagena, Chaparral, Magangué, Neiva ×2, Santa Marta, Valledupar) |
| Procesos | Preventivo – Disciplinario |
| Estudio | Título universitario en una de VARIAS disciplinas (Derecho, Administración, Contaduría, Economía, Ingenierías, Psicología, Medicina, Ciencias Políticas, etc.) + 2 años de experiencia. **No asumir que la aspirante es abogada.** |
| Prueba | Conocimientos 70 % (eliminatoria, mín. 65/100) · Comportamentales 20 % · Antecedentes 10 % · elegibles ≥ 70 |
| Competencias | Responsabilidad con la organización B · Organización del trabajo B · Investigación B · Pensamiento conceptual A · Orientación a resultados A · Cumplimiento de parámetros B |

Funciones idénticas a las de la Conv. 147-2026 (familia `-PU`). Conocimientos específicos: constitucional, disciplinario, probatorio, penal, procesal, administrativo, contratación, anticorrupción, **ordenamiento territorial**.

## 2. Plan (21 días)
| Día | Código | Base |
|---|---|---|
| 1 | INTRO-00-PGN-3PU17L + ENT-PGN-PU-01 ♻️ | INTRO-00-PGN-PU |
| 2-4 | GEN-01/02/03-PGN ♻️ (+ FUN-GDOC-3PU17L-01 en el Día 4) | genéricas PGN |
| 5-8 | 3PU17L-COM-01..04 | PU-PRO-COM-01..04 |
| 9 | FUN-PGN-3PU17L-01 | FUN-MP-01-PU |
| 10 | FUN-CONST-3PU17L-01 | FUN-CONST-01 |
| 11 / 12 / 14 | FUN-DIS-3PU17L-01 / 02 / 03 | FUN-DIS-0x-PU |
| 13 | FUN-PROB-3PU17L-01 | FUN-PROB-01-PU |
| 15 | FUN-PREV-3PU17L-01 | FUN-PREV-01-PU |
| 16 / 17 | FUN-PEN-3PU17L-01 / 02 | FUN-PEN-0x-PU |
| 18 | FUN-JUR-3PU17L-01 | FUN-JUR-01-PU |
| 19 | FUN-CONT-3PU17L-01 | FUN-CONT-01-PU |
| 20 | FUN-OT-3PU17L-01 🆕 para este cargo | FUN-OT-1AS19-01 reenfocada |
| 21 | SIM-PGN-3PU17L-001 | SIM-PGN-3PU17-001 (+3 preguntas de OT) |

## 3. Correcciones de fondo aplicadas (respecto de la familia -PU)
- **Intervención (función 5 del manual):** se eliminó la afirmación absoluta "el 3PU-17 nunca interviene ante jueces". Ahora: la intervención la ejercen de ordinario los procuradores judiciales; el 3PU-17 de instrucción solo realiza labores de intervención cuando la dependencia deba asumirlas y el jefe se las asigne.
- **Separación instrucción/juzgamiento (Ley 2094/2021):** los casos en que "el jefe de tu Procuraduría de Instrucción profirió el fallo" se reescribieron con el funcionario de juzgamiento como autor del fallo.
- **Culpa leve:** no es sancionable (art. 29 CGD); corregidas tabla, texto y la pregunta 15 de DIS-01.
- **SIRI:** nombre oficial "Sistema de Información de Registro de Sanciones y Causas de Inhabilidad".
- **Penal vs. disciplinario:** se quitó la idea de un "estándar menos gravoso"; ambos exigen certeza, sobre objetos distintos (arts. 381 Ley 906 y 142 CGD).
- **PEN-02:** las retroalimentaciones de las preguntas 12 y 13 estaban cruzadas (corregido también en la guía original FUN-PEN-02-PU).
- **COM-02:** cuatro preguntas duplicadas se reemplazaron por preguntas nuevas (registro en sistemas, reserva art. 115 CGD, mejora del control de términos, presión por indicadores).
- **Advertencia previa:** ya no se dice que "agrava" la responsabilidad; prueba el conocimiento del riesgo y puede pesar en la graduación.

## 4. Validación
0 fugas (147-2026, 154 cargos, María Alejandra, 1AS-19, 33-2026, "abogada" para la aspirante); 0 errores de JavaScript en Chromium; retroalimentación coherente con cada pregunta (verificado por script); correctas balanceadas.

## 5. Pasos para ver el curso
1. Merge del PR → deploy.
2. Visitar `/api/admin/seed-guias`.
3. En el curso de Lina → **Rehacer** con el plan `pgn-profesional-3pu17-lina`.
