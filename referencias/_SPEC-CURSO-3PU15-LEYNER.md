# SPEC — Curso PGN Profesional Universitario 3PU-15 (Leyner Urrego · Conv. 112-2026)

> Documento maestro para reconstruir el curso completo (21 días). Rama: `feat/curso-pgn-3pu15-leyner`.
> **REGLA DE ORO: push por guía. Nada se acumula sin commitear.**

## 1. Perfil del cargo (fuente: origin/expediente-leyner-urrego/ANALISIS-VACANTES.md)

| Dato | Valor |
|---|---|
| Aspirante | Leyner Andrés Urrego Sanmartín (Contador Público, ITM 2023, T.P. 332769-T) |
| Cargo | **Profesional Universitario, grado 3PU-15** |
| Convocatoria | **112-2026** (concurso "Mérito Construyendo Excelencia") |
| Salario | $6.889.867 |
| Dependencia | **Dirección Nacional de Investigaciones Especiales** |
| Sede | Medellín (2) + Bogotá (2) |
| Régimen | Especial de carrera PGN (Decretos Ley 262/263/264 de 2000). **NO es CNSC.** |
| Perfil funcional | Apoyo técnico-científico **financiero, contable y tributario** aplicado a las investigaciones disciplinarias. Elabora informes/dictámenes financieros, analiza operaciones y detecta irregularidades en el manejo de recursos públicos. Ejerce funciones de Policía Judicial. |
| Experiencia | NO requiere. |

## 2. Enfoque (CLAVE anti-fuga)

El molde base son las guías `-PU` del curso 3PU-17 (María Alejandra), cuyo rol es
**Procuradurías de Instrucción** (recauda pruebas y **proyecta decisiones para la firma del jefe**).

El 3PU-15 de Leyner es DISTINTO: **Dirección Nacional de Investigaciones Especiales**,
rol de **perito/analista financiero-contable** que:
- Analiza estados financieros, contratos, presupuestos y operaciones dentro de expedientes disciplinarios.
- Emite **dictámenes e informes técnicos** (financieros/contables/tributarios) que sirven de prueba.
- Reconstruye operaciones, detecta sobrecostos/desviación de recursos, cuantifica detrimento.
- Ejerce **Policía Judicial** para recaudar y asegurar EMP (elementos materiales probatorios) contables.

→ NO decir "proyectas la decisión para la firma del jefe" (eso es del instructor 3PU-17).
→ SÍ decir "emites un dictamen/informe técnico que fundamenta la decisión del despacho".

## 3. Fugas a ELIMINAR siempre (grep debe dar 0)
`3PU-17`, `147-2026`, `María Alejandra`, `Procuraduría(s) de Instrucción`,
`Procurador Judicial`, `Sustanciador`, `4SU-`, `Viviana`, `Auxiliar Administrativo`,
`5AM-10`, `242-2026`, `Gina`, `DIAN`, `Gestor I`, `URT`, `INDERVALLE`, `paciente`, `clínic`.
"CNSC" solo se permite para aclarar que la PGN **NO** es CNSC (régimen especial).
Único código válido: **3PU-15**. Única convocatoria: **112-2026**.

## 4. Estándar de calidad por guía funcional (molde -PU)
- 10 secciones: data-sec 0..9 (Objetivo/Importancia/Desarrollo/Comparaciones/Casos/Errores/Tips/Trampas/Resumen/Simulacro).
- **Desarrollo (data-sec="2") ≥ 10.000 palabras**, 7-8 módulos con `<h4>`, teoría profunda.
- Por módulo: varias tablas, varios ejemplos `.practica` ("En la práctica") ambientados en el rol financiero 3PU-15, acordeones `details.acc`, `.ojo` (Ojo en la prueba), `.flujo` si es proceso.
- 3-4 `.checkpoint` interactivos (con handler JS).
- Cierre del Desarrollo: box "Idea clave" + box Tips + box dorado "⚡ Frase para recordar" + `.fuentes` con enlaces reales verificados (`target="_blank"`).
- Simulacro (sec 9): mín. 8 preguntas situacionales largas (contexto 450-1000 car, 4 opciones elaboradas), formato estático `.pregunta[data-correct]` + objeto JS `feedbacks`.
- Frases clave en `<mark>` (subrayado dorado). Identidad navy/oro. `<div id="readbar">` barra de progreso.
- **Día coherente** en kicker (`Día N · Funcional`), y si se añade badge/finalizar deben coincidir.

## 5. Validación obligatoria por guía (antes de push)
```
NODE=$(ls ~/.nvm/versions/node/*/bin/node | tail -1)
"$NODE" --check <(extraer los <script>)         # JS sin errores
python3 scripts/validar-guia.py guias/ARCH.html "Día N"   # tags balanceados, Desarrollo>=10000
grep -icE "3PU-17|147-2026|Procuradur.a. de Instrucc|Procurador Judicial|Sustanciad|María Alej"  # = 0
```
El validador marcará "POSIBLES FUGAS: 3PU-15" → **falso positivo** (es el cargo correcto). Verificar que NO haya 3PU-17.

## 6. Plan de 21 días (mapa día → archivo)
| Día | Tipo | Tema | Archivo destino | Base a reenfocar |
|---|---|---|---|---|
| 1 | INTRO | Presentación del curso | INTRO-00-PGN-PU15-presentacion-curso.html | INTRO-00-PGN-PU |
| 2 | GEN | El Estado y la función pública | GEN-01-PGN-PU15-estado-funcion-publica.html | GEN-01-PGN-AUX |
| 3 | GEN | Relación Estado–ciudadano | GEN-02-PGN-PU15-relacion-estado-ciudadano.html | GEN-02-PGN-AUX |
| 4 | GEN | Marco institucional del Estado | GEN-03-PGN-PU15-marco-institucional.html | GEN-03-PGN-AUX |
| 5 | COM | Responsabilidad + Organización del trabajo | FUN-PU15-COM-01-responsabilidad-organizacion.html | PU-PRO-COM-01 |
| 6 | COM | Orientación a resultados + Cumplimiento | FUN-PU15-COM-02-orientacion-resultados.html | PU-PRO-COM-02 |
| 7 | COM | Investigación + Pensamiento conceptual | FUN-PU15-COM-03-investigacion-pensamiento.html | PU-PRO-COM-03 |
| 8 | COM | Alcance del cargo + integración | FUN-PU15-COM-04-alcance-integracion.html | PU-PRO-COM-04 |
| 9 | FUN | Estructura y funciones de la PGN | FUN-PGN-PU15-01-estructura-funciones-pgn.html | FUN-MP-01-PU |
| 10 | FUN | Gestión pública y funcionamiento del Estado | FUN-GP-PU15-01-gestion-publica-estado.html | FUN-PREV-01-PU |
| 11 | FUN | Constitución aplicada al cargo | FUN-CONST-PU15-01-constitucion-politica.html | (nueva desde molde) |
| 12 | FUN | Derecho disciplinario I: fundamentos | FUN-DIS-PU15-01-derecho-disciplinario.html | FUN-DIS-01-PU |
| 13 | FUN | Derecho administrativo / CPACA | FUN-JUR-PU15-01-derecho-administrativo-cpaca.html | FUN-JUR-01-PU |
| 14 | FUN | Contratación estatal | FUN-CONT-PU15-01-contratacion-estatal.html | FUN-CONT-01-PU |
| 15 | FUN | Presupuesto público | FUN-PPTO-PU15-01-presupuesto-publico.html | (nueva desde molde) |
| 16 | FUN | Contabilidad pública | FUN-CPUB-PU15-01-contabilidad-publica.html | (nueva desde molde) |
| 17 | FUN | Finanzas públicas y evaluación de proyectos | FUN-FINP-PU15-01-finanzas-publicas-proyectos.html | (nueva desde molde) |
| 18 | FUN | Policía judicial y cadena de custodia | FUN-PJUD-PU15-01-policia-judicial.html | (nueva desde molde) |
| 19 | FUN | Estatuto anticorrupción | FUN-ANTIC-PU15-01-estatuto-anticorrupcion.html | FUN-CONT-01-PU (parte) |
| 20 | FUN | Sistemas de gestión y documentos (MIPG) | FUN-MIPG-PU15-01-sistemas-gestion-documentos.html | FUN-GDOC-01-PU |
| 21 | SIM | Simulacro final (50 funcional + 20 comportamental) | SIM-PGN-3PU15-001-simulacro-final.html | plantilla SIM |
| — | ENT | Conoce tu entidad (PGN) | ENT-PGN-PU-01 (ya existe, reutilizable) | — |

## 7. Método técnico
- Copiar base → reenfocar módulo por módulo (rol financiero) → limpiar fugas → validar → push.
- Escribir fragmentos en el repo (no /tmp para pasar contenido a shell).
- Registrar cada guía en biblioteca/biblioteca.json (biblioteca "Funcional"/"General"/"Por Nivel").
- Sincronizar guias/ ↔ plataforma/public/seed-guias/ al final.



---

## 8. AJUSTES FINALES APLICADOS (post-revisión de Julio, sep-2026)

1. **Plan plantilla en la plataforma:** se agregó `pgn-profesional-3pu15` a `plataforma/lib/autocargarGuias.ts`
   (22 guías por código, Días 1-21). Habilita el botón "⚡ Armar plan completo / 🔄 Rehacer" en el panel admin.

2. **Simulacro final reorganizado (independiente):** el simulacro se movió de `guias/` a `simulacro/SIM-PGN-3PU15-001.html`
   (nombre corto, igual que los que funcionan 5AM10/3PU17), y su categoría en biblioteca pasó de "Simulacro" a
   **"Simulacro Final"**. Sin esto, se agrupaba por error en "Conocimientos Generales". Ahora queda en su módulo
   propio al final del plan.

3. **Simulacro reconstruido al nivel de la prueba real:** las 70 preguntas se rehicieron con contexto largo
   (6-10 renglones), enunciado que replantea la tensión, y 4 opciones largas y confusas (enunciado prom ~371 car,
   opciones prom ~190 car, 0 opciones cortas). Antes estaban demasiado cortas y sencillas.

4. **Sincronización biblioteca.json:** recordar que el catálogo lee `plataforma/lib/biblioteca.json` (copia del
   deploy), no solo `biblioteca/biblioteca.json`. Mantener ambos iguales.

El proceso completo y reutilizable quedó documentado en `referencias/PROCESO-CURSOS-GUIAS.md` y el prompt de
inicio para nuevos cursos en `referencias/PROMPT-INICIO-CURSO.md`.
