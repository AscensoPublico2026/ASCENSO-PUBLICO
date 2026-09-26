# SPEC — Curso PGN Secretario Procuraduría 4SP-12 (Humberto José Jiménez Ramírez · Conv. 291-2026)

> Rama: `feat/curso-pgn-4sp12-humberto-jimenez`. **REGLA DE ORO: push por guía.** Plan plantilla: `pgn-secretario-4sp12`.

## 1. Cargo (fuente: manual de funciones 291-2026.pdf, Resolución 212 de 2026)
| Dato | Valor |
|---|---|
| Aspirante | Humberto José Jiménez Ramírez (jimnezh661@gmail.com) |
| Cargo | **Secretario Procuraduría, código y grado 4SP-12**, Nivel **Técnico** |
| Convocatoria | **291-2026** |
| Salario | $5.846.100 (vigencia 2025) · **19 plazas** · Planta Global + Planta Fija |
| Dependencias iniciales | División de Gestión Humana, División de Registro de Sanciones y Causas de Inhabilidad, Procuradurías Delegadas con funciones Mixtas, de Intervención, Disciplinarias de Instrucción, Procuradurías Delegadas/Regionales/Distritales/Provinciales con funciones de Instrucción |
| Estudio | Aprobación de 2 años de educación superior. Experiencia: **No requiere**. |
| Régimen | Especial PGN (Decreto Ley 262/263 de 2000). **NO es CNSC.** |
| Pruebas | Conocimientos (65/100 eliminatoria, 70%) + Comportamentales (20%) + Antecedentes (10%). |

## 2. Enfoque del rol — IDÉNTICO al de Carolina Rueda (4SP-13)
**Hallazgo clave (confirmado contra el manual de funciones oficial):** el 4SP-12 de Humberto **NO es un nivel jerárquico distinto** al 4SP-13 de Carolina — ambos son **Secretario Procuraduría, nivel Técnico**, con funciones y competencias comportamentales prácticamente idénticas (mismas 5 competencias, mismos niveles B/B/B/C/B). Lo único que cambia es el grado/código (escalón salarial), la convocatoria, el salario, el número de plazas, las dependencias iniciales, y que este cargo **no exige experiencia** (el de Carolina sí, 6 meses).

Aplica el mismo enfoque anti-fuga: apoyo secretarial (radicar, tramitar, notificar, trasladar, archivar, actualizar sistema, atender usuarios) — **NUNCA investiga, decide ni sustancia procesos**.

## 3. Estrategia de reutilización (decisión de eficiencia, documentada)
De las 22 piezas del curso de Carolina, **12 guías funcionales (Días 9-20) son código-agnósticas por contenido** — ya se verificó que no mencionan "4SP-13", código, convocatoria, salario ni nombre de Carolina. Se **reutilizan tal cual, sin duplicar archivo**, vía el plan plantilla `pgn-secretario-4sp12` (mismo `archivo` HTML, solo referenciado por un código de plan distinto):
FUN-PGN-TEC-01, FUN-GP-TEC-01, FUN-CONST-TEC-01, FUN-MP-TEC-01, FUN-DIS-TEC-01, FUN-OFI-TEC-01, FUN-OFI-TEC-02, FUN-GDOC-TEC-01, FUN-GDOC-TEC-02, FUN-ATC-TEC-01, FUN-MIPG-TEC-01, FUN-TRANS-TEC-01.
(3 de ellas tenían menciones sueltas de "4SP-13" que ya se genericizaron en un commit aparte a `main` antes de crear esta rama — ver `fix/genericizar-guias-tec-compartidas`.)

`ENT-PGN-01` también se reutiliza tal cual (ya es genérica para cualquier cargo de la PGN, como en el curso de Carolina).

**Solo se construyen 9 piezas NUEVAS** (reenfocadas desde el molde de Carolina, cambiando código/convocatoria/salario/plazas/experiencia/dependencias/nombre):
Días 1-8 (INTRO + GEN + COM) y Día 21 (simulacro final).

## 4. Fugas a eliminar (grep = 0 en las 9 guías nuevas)
Todo el blocklist del curso de Carolina, MÁS: `4SP-13`, `283-2026`, `Resolución 243`, `Carolina Rueda`, `carito2951`, `6.334.864`, `16 plazas`, `6 meses` (como requisito de experiencia — el de Humberto no requiere), y el resto del blocklist heredado (`242-2026`, `264-2026`, `268-2026`, `269-2026`, `273-2026`, `274-2026`, `270-2026`, `144-2026`, `147-2026`, `112-2026`, `02-2026`, `33-2026`, `Auxiliar Administrativo`, `5AM-10`, `3PU-15`, `3PU-17`, `1AS-19`, nombres de otros aspirantes, `investigador`/`sustanciador` salvo aclarar que NO lo es).
Único código: **4SP-12**. Única conv.: **291-2026**. Sufijo de archivos: **-4SP12**.

## 5. Plan de 9 piezas nuevas (molde = versión ya reenfocada de Carolina)
| Día | Código | Tema | Molde (curso Carolina) |
|---|---|---|---|
| 1 | INTRO-00-PGN-4SP12 | Presentación del curso | INTRO-00-PGN-4SP13-presentacion-curso.html |
| 2 | GEN-01-PGN-4SP12 | El Estado y la función pública | GEN-01-PGN-4SP13-estado-funcion-publica.html |
| 3 | GEN-02-PGN-4SP12 | Relación Estado–ciudadano | GEN-02-PGN-4SP13-relacion-estado-ciudadano.html |
| 4 | GEN-03-PGN-4SP12 | Marco institucional del Estado | GEN-03-PGN-4SP13-marco-institucional.html |
| 5 | 4SP12-COM-01 | Responsabilidad con la Organización (B) + Organización del Trabajo (B) | 4SP13-COM-01-responsabilidad-organizacion-trabajo.html |
| 6 | 4SP12-COM-02 | Gestión de la Información (B) + Cumplimiento de Parámetros de Trabajo (C) | 4SP13-COM-02-gestion-informacion-cumplimiento-parametros.html |
| 7 | 4SP12-COM-03 | Objetividad (B) en el ejercicio secretarial | 4SP13-COM-03-objetividad.html |
| 8 | 4SP12-COM-04 | Alcance del cargo Técnico e integración de competencias | 4SP13-COM-04-alcance-cargo-tecnico-integracion.html |
| 9-20 | (reutilizadas, ver §3) | — | — |
| 21 | SIM-PGN-4SP12-001 | Simulacro final (50 funcional + 20 comportamental Likert = 70) | SIM-PGN-4SP13-001.html (los `ref`/`refT` NO cambian: apuntan a las mismas 12 guías FUN-*-TEC-* compartidas) |
| — | ENT-PGN-01 | Conoce tu entidad (PGN) | ♻️ reutilizada tal cual |

## 6. Estándar aplicado
Mismo estándar v3.0 del curso de Carolina: Desarrollo ≥10.000 palabras en INTRO/GEN/COM, módulos profundos, `.practica` en rol real secretarial, checkpoints, cierre + `.fuentes`, `<mark>` dorado. Simulacro 70 preguntas.

## 7. Validación (cada guía)
`node --check` del JS + grep de fugas = 0 + día coherente en kicker/badge/finalizar.

## 8. Carga a la plataforma
Registrar las 9 piezas nuevas en `biblioteca/biblioteca.json` Y `plataforma/lib/biblioteca.json` (sync con `scripts/sync-biblioteca.sh`), copiar a `plataforma/public/seed-guias/`. Crear plan plantilla `pgn-secretario-4sp12` en `plataforma/lib/autocargarGuias.ts` (22 ítems: 9 nuevos + 12 FUN-*-TEC-* compartidas + ENT-PGN-01).
