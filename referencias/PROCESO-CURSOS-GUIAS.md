# 📚 PROCESO MAESTRO — Construcción de CURSOS (guías HTML) · Ascenso Público

> Documento de referencia para armar el curso de preparación (21 días) de CUALQUIER aspirante,
> reutilizable entre cargos/entidades. Consolida TODO lo aprendido y aprobado por Julio César
> (caso de referencia: **Leyner Urrego — PGN Profesional Universitario 3PU-15, Conv. 112-2026**).
>
> ⚠️ NO confundir con `PROCESO-ASESORIA-VACANTES.md` (eso es la asesoría/identificación de vacantes).
> Este documento es para **producir el curso** una vez el aspirante ya eligió su cargo.

---

## 0. Qué es un curso y de qué se compone (21 días + entidad)

Un curso completo = **22 guías HTML** organizadas por día:

| Día | Tipo | Contenido | Código (ejemplo 3PU-15) |
|---|---|---|---|
| 1 | INTRO | Presentación del curso y el cargo | `INTRO-00-PGN-PU15` |
| 2-4 | GENERAL | Estado/función pública · relación Estado-ciudadano · marco institucional | `GEN-01/02/03-PGN-PU15` |
| 5-8 | COMPORTAMENTAL | Competencias del Decreto 815/2018 (por nivel) | `FUN-PU15-COM-01..04` |
| 9-20 | FUNCIONAL | 12 guías del conocimiento técnico del cargo | `FUN-*-PU15-01` |
| 21 | SIMULACRO | Simulacro final (50 funcionales + 20 comportamentales) | `SIM-PGN-<código>-001` |
| — | ENTIDAD | "Conoce tu entidad" (reutilizable, sin día) | `ENT-PGN-PU-01` |

Los temas funcionales (Días 9-20) se ajustan al **manual de funciones del cargo**. Para el 3PU-15 (perfil
financiero-contable) fueron: Estructura PGN, Gestión pública, Constitución, Disciplinario, CPACA,
Contratación, Presupuesto, Contabilidad pública, Finanzas/proyectos, Policía judicial, Anticorrupción,
Sistemas de gestión/MIPG.

---

## 1. Regla de oro del flujo: PUSH POR GUÍA (nada se pierde)

**LECCIÓN DURA (Leyner):** una sesión anterior produjo ~17 guías y NO se hizo commit → el sandbox
se recicló y se perdió TODO el trabajo (y créditos). **NUNCA MÁS.**

- Crear una rama `feat/curso-<entidad>-<código>-<aspirante>` al inicio y **pushearla de una**.
- Después de CADA guía (o tanda pequeña) validada → **commit + push inmediato**.
- Aunque el sandbox se caiga, cada guía queda a salvo en GitHub al instante.

---

## 2. Método técnico probado (reenfoque de molde)

Las guías se REUTILIZAN entre cargos. Casi nunca se escribe desde cero: se parte de un **molde**
de una guía existente del mismo nivel y se REENFOCA (no find-replace ciego).

**Moldes base recomendados (nivel Profesional Universitario PGN, familia `-PU`):**
`FUN-DIS-01-PU`, `FUN-JUR-01-PU`, `FUN-CONT-01-PU`, `FUN-MP-01-PU`, `FUN-PREV-01-PU`,
`FUN-PEN-01-PU`, `FUN-GDOC-01-PU`, `FUN-PROB-01-PU` (benchmark). Comportamentales: `PU-PRO-COM-01..04`.
Generales: `GEN-01/02/03-PGN-AUX`. INTRO: `INTRO-00-PGN-PU`. Entidad: `ENT-PGN-PU-01` (ya limpia).

**Pasos por guía:**
1. Copiar el molde al archivo destino con el código nuevo.
2. Ajustar metadata: `doc-ref`, `<title>`, `kicker` ("Día N · Funcional"), footer.
3. **REESCRIBIR EL ENFOQUE al rol real del cargo**, no solo cambiar términos. Ej. 3PU-15 (perito
   financiero) = "analiza soportes, cuantifica hallazgos y **emite dictámenes** que fundamentan la
   decisión del despacho; ejerce Policía Judicial; NO decide el fondo". (El molde 3PU-17 era
   "instructor que proyecta para firma del jefe" → hubo que reescribir ese rol en TODO el texto.)
4. Reenfocar los ejemplos `.practica`, casos, tips, trampas y simulacro al rol del cargo.
5. Añadir badge `<span style="..." class="badge">📅 Día N de 21</span>` (el `style` va ANTES de
   `class` para que el validador lo detecte) y botón `id="btnFinalizar"` "✅ Finalizar Día N" con
   su handler JS (`alert('✅ Has finalizado el Día N: ... ¡Excelente trabajo, sigue así!')`).
6. VALIDAR (ver §4). 7. Commit + push.

**Cómo hacer los reemplazos:** con un script Python EN EL REPO (no /tmp para pasar contenido al shell;
/tmp solo para extraer el JS al validar). ⚠️ Cuidado con regex agresivas: una vez `potestad de j\b`
dañó "juzgamiento". Preferir reemplazos de frases literales largas; usar regex solo con límites `\b`.

**Paralelización:** se puede delegar la construcción a varios sub-agentes en paralelo (2-3 guías c/u),
mientras el orquestador valida y hace push por tanda. Funcionó bien para las 22 guías.

---

## 3. ESTÁNDAR DE CALIDAD (inquebrantable — es "la cara" del negocio)

### 3.1 Desarrollo (sección `data-sec="2"`)
- **MÍNIMO 10.000 palabras** (funcionales y generales). Es EL producto por el que paga el cliente (~$300.000).
- 7-9 módulos con `<h4>`, teoría profunda (600-1.200 palabras/módulo).
- Por módulo: VARIAS tablas/esquemas, VARIOS ejemplos `.practica` ("En la práctica") ambientados en el
  rol real del cargo, acordeones `details.acc`, `.ojo` ("Ojo en la prueba"), `.flujo` si es proceso.
- 3-4 `.checkpoint` interactivos con handler JS.
- Cierre: box "Idea clave" + box Tips + box dorado "⚡ Frase para recordar" + `.fuentes` con enlaces
  DIRECTOS y VERIFICADOS (`target="_blank"`) a las normas (secretariasenado.gov.co, funcionpublica.gov.co,
  corteconstitucional.gov.co, etc.).
- Frases clave en `<mark>` (subrayado dorado, NO fondo de marcador).

### 3.2 Simulacros — CALIDAD TIPO PRUEBA REAL (regla reforzada por Julio, sep-2026)
**Las preguntas deben ser IDÉNTICAS a la prueba escrita real. NO cortas, NO sencillas, NO obvias.**
- **CONTEXTO largo**: 6-10 renglones (mín 450, ideal 550-1000 caracteres) — escenario situado con rol,
  dependencia, personas, antecedentes, una tensión y VARIAS presiones/distractores.
- **ENUNCIADO** de 2-4 renglones que replantea la tensión e induce a decidir la actuación MÁS apropiada.
- **4 OPCIONES largas y elaboradas** (mín 120, ideal 150-280 caracteres CADA UNA), todas plausibles, del
  mismo nivel de detalle, con "cascaritas" (que la correcta NO se delate por ser la única larga).
  Los distractores deben CONFUNDIR; que no se puedan descartar a simple vista.
- Benchmark medido aprobado: enunciado promedio ~285-371 car, opciones ~190-220 car, 0 opciones cortas.
- Simulacro final (Día 21): **50 funcionales + 20 comportamentales = 70 preguntas**, todas al estándar.
- `data-correct` variado (no siempre la misma letra).

### 3.3 Identidad y anti-fugas
- Marca navy/oro, barra de progreso `<div id="readbar">`, header con subtítulo blanco.
- **Día correcto** coherente en kicker, badge, footer y JS.
- **0 FUGAS**: nada de otro aspirante, cargo, código, entidad o convocatoria. Buscar con grep:
  otro código (`3PU-17`, `5AM-10`, `4SU-`), otra convocatoria (`147-2026`, `242-2026`),
  `Procuraduría de Instrucción`, `Procurador Judicial`, `Sustanciador`, nombres de otros aspirantes
  (`María Alejandra`, `Viviana`, `Gina`), otras entidades (`DIAN`, `URT`, `contribuyente`, `paciente`, `clínic`).
- La PGN es **régimen ESPECIAL**: NO mencionar la CNSC como organizadora (solo para aclarar que NO es CNSC).
- Nota: la palabra "tributario/a" SÍ es válida si el perfil del cargo lo incluye (p.ej. 3PU-15
  financiero-contable-tributario); el validador la marca pero es falso positivo del perfil.

---

## 4. VALIDACIÓN OBLIGATORIA por guía (antes de push)

```bash
NODE=$(ls ~/.nvm/versions/node/*/bin/node | tail -1)
# 1) JS sin errores
python3 -c "import re;open('/tmp/j.js','w').write(chr(10).join(re.findall(r'<script>(.*?)</script>',open('ARCHIVO',encoding='utf-8').read(),re.S)))"; "$NODE" --check /tmp/j.js
# 2) HTML balanceado + Desarrollo >=10000 + día coherente
python3 scripts/validar-guia.py ARCHIVO "Día N"
# 3) fugas reales = 0 (verificar que NO haya 3PU-17 u otro código ajeno)
grep -icE "3PU-17|147-2026|Procuradur.a. de Instrucci|Mar.a Alej|Procurador Judicial|\bSustanciador\b|Auxiliar Administrativo|5AM-10|242-2026|\bViviana\b|\bGina\b|\bDIAN\b|paciente|cl.nic|contribuyente" ARCHIVO
```
- El validador marca `POSIBLES FUGAS: <código correcto>` como **falso positivo** (es el cargo del curso).
  Lo importante: que NO aparezca el código de OTRO curso.
- Simulacro estático (`.pregunta[data-correct]` + objeto JS `feedbacks`): el validador dice
  "preguntas simulacro: 0" porque busca el formato `ops:[]`; es NORMAL en el molde `-PU`.

---

## 5. CARGA A LA PLATAFORMA (para que el estudiante vea el curso)

La plataforma (Next.js + Supabase) arma el curso desde la tabla `guias_curso`; el HTML se sirve desde
el BUCKET de Storage. Flujo para dejar un curso cargado y ORGANIZADO:

### 5.1 Registrar en biblioteca.json (DOS archivos)
- `biblioteca/biblioteca.json` (raíz) **Y** `plataforma/lib/biblioteca.json` (copia del deploy que lee el
  catálogo). **MANTENER LOS DOS SINCRONIZADOS** (copiar raíz → deploy).
- Campo `biblioteca` decide el MÓDULO donde se agrupa (vía `mapTipoDB` en `catalogoGuias.ts`):
  - `"Funcional"` → Funciones del Cargo
  - `"Por Nivel"` → Competencias por Nivel (usar ESTE para comportamentales, NO "Comportamental")
  - `"Simulacro Final"` → **Simulacro Final (módulo independiente, al final)** ⚠️ debe ser EXACTAMENTE
    "Simulacro Final"; si pones solo "Simulacro" cae en "general" y se MEZCLA con las generales.
  - `"General"`, `"Introducción"`, `"Por Entidad"` → Introducción / Conocimientos Generales.

### 5.2 El simulacro va en su carpeta propia
- Archivo del simulacro en `simulacro/SIM-...html` (NO en `guias/`), con nombre CORTO (ej.
  `SIM-PGN-3PU15-001.html`, sin sufijos largos), igual que los que ya funcionan (5AM10, 3PU17).
- El seed normaliza la ruta quitando el prefijo `simulacro/`.

### 5.3 Plan plantilla (botón de 1 clic en el panel admin)
- Agregar el plan a `PLANES_PLANTILLA` en `plataforma/lib/autocargarGuias.ts` (copiar el bloque de
  `pgn-auxiliar-administrativo` y cambiar id/nombre/códigos por día). Cada item resuelve por CÓDIGO
  contra el catálogo, así que basta con que el código esté en biblioteca.json con `estado: "publicada"`.
- Eso habilita en el panel admin (curso → "⚡ Armar plan completo") los botones:
  - **⚡ Armar** (agrega las que falten) · **🔄 Rehacer** (deja SOLO este plan) · **🗑️ Vaciar curso**.

### 5.4 Pasos finales del cliente (Julio) para ver el curso
1. Merge del PR a `main` y esperar deploy de Vercel (2-3 min).
2. Sincronizar `guias/` y `simulacro/` → `plataforma/public/seed-guias/` (copiar los HTML).
3. Como admin, abrir el curso del estudiante → **🔄 Rehacer** con el plan correcto (esto reinserta con
   el `tipo` y ruta correctos; necesario si el curso tenía una carga vieja mezclada).
4. Visitar `https://ascensopublico.com/api/admin/seed-guias` (sube los HTML nuevos al bucket).
5. Recargar sin caché (`Ctrl+Shift+R`).

⚠️ **Bug conocido:** cambiar biblioteca.json NO actualiza lo ya cargado en `guias_curso`. Si el curso ya
tenía guías, hay que **Rehacer** el plan para que tome tipo/ruta nuevos.

---

## 6. Checklist de cierre del curso
- [ ] 22 guías creadas, todas validadas (JS OK, HTML balanceado, Desarrollo ≥10.000, día coherente, 0 fugas).
- [ ] Simulacro final: 70 preguntas al estándar de prueba real; en `simulacro/` con nombre corto; biblioteca "Simulacro Final".
- [ ] Registradas en `biblioteca/biblioteca.json` Y `plataforma/lib/biblioteca.json` (sincronizados).
- [ ] Sincronizadas a `plataforma/public/seed-guias/`.
- [ ] Plan plantilla agregado a `autocargarGuias.ts`.
- [ ] Todo pusheado y PR mergeado a `main`.
- [ ] Se le pasan a Julio los pasos de carga (§5.4).

---

## 7. Caso de referencia aprobado
**Leyner Andrés Urrego Sanmartín** — PGN Profesional Universitario **3PU-15**, Conv. **112-2026**,
Dirección Nacional de Investigaciones Especiales, perfil financiero-contable. Plan plantilla:
`pgn-profesional-3pu15`. Spec detallado: `referencias/_SPEC-CURSO-3PU15-LEYNER.md`.
