# SPEC — Curso PGN Asesor 1AS-19 (Nathaly Johanna Rodríguez Ordóñez · Conv. 02-2026)

> Rama: `feat/curso-pgn-1as19-nathaly-rodriguez`. **REGLA DE ORO: push por guía.**

## 1. Cargo (fuente: matriz Convocatorias_Procuraduria.xlsx + ficha 02-2026)
| Dato | Valor |
|---|---|
| Aspirante | Nathaly Johanna Rodríguez Ordóñez (nathaly.jrodriguez@gmail.com) |
| Cargo | **Asesor, código y grado 1AS-19**, Nivel Asesor |
| Convocatoria | **02-2026** |
| Salario | $10.403.514 |
| Dependencia | **Despacho del Procurador General** |
| Proceso | **Direccionamiento y Planeación Institucional** |
| Sede | Bogotá D.C. · 6 plazas |
| Régimen | Especial PGN (Decretos Ley 262/263/264 de 2000). **NO es CNSC.** |

## 2. Enfoque del rol (CLAVE anti-fuga)
Asesor del **Despacho del Procurador General**: asesora en **proyectos de ley/decretos/actos**,
**planeación institucional y MIPG**, **control interno**, **intervención judicial del Ministerio Público**,
**función preventiva y control de gestión**, **DDHH**, **cooperación internacional** y **temas electorales**.
NO es el instructor disciplinario de Instrucción (ese es Silvia 33-2026). Rol transversal, estratégico y de alto nivel.

## 3. Fugas a ELIMINAR (grep = 0)
`33-2026`, `Res. 243`, `243 de 2026`, `Silvia`, `Cort`, `ingenier`, `Bucaramanga`, `Guateque`, `Sogamoso`,
`Procuradur.a. de Instrucci`, `3PU-15`, `3PU-17`, `Leyner`, `Mar.a Alej`, `perito`, `financier`, `contable`,
`dictamen`, `Gina`, `Viviana`, `DIAN`, `contribuyente`. Único código: **1AS-19**. Única conv.: **02-2026**. Sufijo: **-1AS19N**.

## 4. Plan de 21 días (día · archivo · decisión · base)
1 INTRO ✏️ INTRO-00-PGN-1AS19N-presentacion-curso.html ← INTRO-00-PGN-1AS19
2-4 GEN ✏️ GEN-01/02/03-PGN-1AS19N-*.html ← GEN-*-PGN-1AS19
5-8 COM ✏️ 1AS19N-COM-01/02/03/04-*.html ← 1AS19-COM-*
9 FUN ✏️ FUN-PGN-1AS19N-01 ← FUN-PGN-1AS19-01
10 FUN ✏️ FUN-GP-1AS19N-01 ← FUN-GP-1AS19-01
11 FUN ✏️ FUN-CONST-1AS19N-01 ← FUN-CONST-1AS19-01
12 FUN 🆕 FUN-LEG-1AS19N-01 (Técnica legislativa y proyectos de ley) **PILOTO**
13 FUN ✏️ FUN-JUR-1AS19N-01 ← FUN-JUR-1AS19-01
14 FUN 🆕 FUN-MP-1AS19N-01 (Intervención judicial y Ministerio Público)
15 FUN ✏️ FUN-PREV-1AS19N-01 (+DDHH) ← FUN-PREV-1AS19-01
16 FUN ✏️ FUN-CONT-1AS19N-01 ← FUN-CONT-1AS19-01
17 FUN ✏️ FUN-ANTIC-1AS19N-01 ← FUN-ANTIC-1AS19-01
18 FUN ✏️ FUN-PLAN-1AS19N-01 (Planeación/MIPG/Control interno) ← FUN-MIPG-1AS19-01
19 FUN 🆕 FUN-ELEC-1AS19N-01 (Derecho electoral y vigilancia preventiva)
20 FUN 🆕 FUN-COOP-1AS19N-01 (Cooperación internacional y relaciones institucionales)
21 SIM 🆕 SIM-PGN-1AS19N-001.html (50 funcional + 20 comportamental Likert)
— ENT ♻️ ENT-PGN-PU-01 (reutilizar tal cual)

## 5. Estándar (v3.0): Desarrollo ≥10.000 pal, módulos profundos, tablas+.practica+acordeones+.flujo+.ojo por módulo,
3-4 checkpoints, cierre Idea clave/Tips/Frase + .fuentes con enlaces reales target=_blank, <mark> dorado, día coherente.
Simulacro tipo prueba real (ctx 6-10 renglones, 4 ops 120-280 car). Registrar en biblioteca.json x2 + seed-guias + plan plantilla `pgn-asesor-1as19-nathaly`.


---

## 8. CURSO COMPLETO ✅ (22 guías construidas, validadas y pusheadas)
Rama `feat/curso-pgn-1as19-nathaly-rodriguez`. Plan plantilla `pgn-asesor-1as19-nathaly` en `plataforma/lib/autocargarGuias.ts`.

| Día | Código | Guía | Estado |
|---|---|---|---|
| 1 | INTRO-00-PGN-1AS19N | Presentación del curso | ✏️ reenfoque |
| 2-4 | GEN-01/02/03-PGN-1AS19N | Estado / Estado-ciudadano / Marco institucional | ✏️ reenfoque |
| 5-8 | 1AS19N-COM-01/02/03/04 | Comportamentales (7 competencias Dec. 815/2018) | ✏️ reenfoque |
| 9 | FUN-PGN-1AS19N-01 | Estructura y funciones de la PGN | ✏️ |
| 10 | FUN-GP-1AS19N-01 | Gestión pública | ✏️ |
| 11 | FUN-CONST-1AS19N-01 | Constitución | ✏️ |
| 12 | FUN-LEG-1AS19N-01 | Técnica legislativa y proyectos de ley | 🆕 (piloto) |
| 13 | FUN-JUR-1AS19N-01 | Derecho administrativo y CPACA | ✏️ |
| 14 | FUN-MP-1AS19N-01 | Intervención judicial y Ministerio Público | 🆕 |
| 15 | FUN-PREV-1AS19N-01 | Función preventiva, control de gestión y DDHH | ✏️ |
| 16 | FUN-CONT-1AS19N-01 | Contratación estatal | ✏️ |
| 17 | FUN-ANTIC-1AS19N-01 | Estatuto anticorrupción | ✏️ |
| 18 | FUN-PLAN-1AS19N-01 | Planeación institucional, MIPG y control interno | ✏️ |
| 19 | FUN-ELEC-1AS19N-01 | Derecho electoral y vigilancia preventiva | 🆕 |
| 20 | FUN-COOP-1AS19N-01 | Cooperación internacional y relaciones institucionales | 🆕 |
| 21 | SIM-PGN-1AS19N-001 | Simulacro final (50 funcional + 20 comportamental = 70) | 🆕 |
| — | ENT-PGN-PU-01 | Conoce tu entidad (PGN) | ♻️ reutilizada |

Validación: todas JS OK (node --check), HTML balanceado, Desarrollo ≥10.000 palabras (funcionales/generales 10.040–12.196), días coherentes, 0 fugas de Silvia/33-2026/instrucción/ingeniería. Simulacro: 70 preg = 70 feedbacks, correctas balanceadas (18/20/16/16). Registradas en biblioteca.json x2 + seed-guias. Plan plantilla `pgn-asesor-1as19-nathaly`.

PENDIENTE (Julio): merge PR a main → deploy Vercel → panel admin del curso de Nathaly "🔄 Rehacer" con plan `pgn-asesor-1as19-nathaly` → visitar /api/admin/seed-guias → recargar sin caché.
