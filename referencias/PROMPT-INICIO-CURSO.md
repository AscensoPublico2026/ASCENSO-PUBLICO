# 🚀 PROMPT DE INICIO DE SESIÓN — Construcción de CURSOS (guías HTML) · Ascenso Público

> **Cómo se usa:** al abrir una sesión NUEVA de Kiro para armar el curso de un aspirante,
> copia y pega TODO el bloque de abajo (desde 👇 hasta 👆) como primer mensaje.
> Luego dile el nombre del aspirante, su cargo/código y su convocatoria.
>
> Caso de referencia ya aprobado por Julio César: **Leyner Urrego — PGN 3PU-15, Conv. 112-2026** (curso completo, 21 días).

---

## PROMPT (copiar desde aquí 👇)

Kiro, vamos a **construir el CURSO de preparación (21 días de guías HTML)** de un nuevo aspirante para Ascenso Público. Sigue EXACTAMENTE el método y el estándar que ya dejamos documentado y aprobado.

**Antes de empezar, haz esto:**
1. Clona/actualiza el repo `AscensoPublico2026/ASCENSO-PUBLICO` (si ya está, `git pull` de `main`).
2. Lee estos archivos para retomar el método y el estándar de calidad:
   - `referencias/PROCESO-CURSOS-GUIAS.md`  ← el proceso maestro completo (léelo entero)
   - `referencias/_SPEC-CURSO-3PU15-LEYNER.md`  ← spec del curso de referencia ya aprobado
   - Una guía funcional de ejemplo del nivel: `guias/FUN-DIS-PU15-01-derecho-disciplinario.html`
   - El simulacro de ejemplo (calidad tipo prueba real): `simulacro/SIM-PGN-3PU15-001.html`
3. Confirma que existe el validador `scripts/validar-guia.py`.

**Reglas que NO se rompen (resumen; el detalle está en PROCESO-CURSOS-GUIAS.md):**
- **PUSH POR GUÍA.** Crea una rama `feat/curso-<entidad>-<código>-<aspirante>` y púshéala YA. Después de cada guía validada, commit + push inmediato. NUNCA acumular trabajo sin commitear (ya perdimos un curso completo por eso).
- **Desarrollo ≥ 10.000 palabras** en funcionales y generales, con módulos profundos, tablas, ejemplos `.practica` ambientados en el rol REAL del cargo, acordeones, checkpoints, `.flujo`, `.ojo`, cierre con "Idea clave" + Tips + "Frase para recordar" + `.fuentes` con enlaces reales `target="_blank"`. Frases clave en `<mark>` (subrayado dorado).
- **Simulacros IDÉNTICOS a la prueba real:** contexto largo (6-10 renglones, 450-1000 car), enunciado que replantea la tensión, y 4 opciones largas (120-280 car) y confusas (distractores que no se descartan a simple vista). El simulacro final (Día 21) = 50 funcionales + 20 comportamentales = 70 preguntas.
- **REENFOCAR el molde, no find-replace ciego:** cambia el ENFOQUE al rol real del cargo. Cuidado con regex agresivas (usar reemplazos literales o `\b`).
- **0 FUGAS:** ningún dato de otro aspirante/cargo/código/convocatoria/entidad. Verifícalo con grep en cada guía. La PGN es régimen especial (NO CNSC como organizadora).
- **Simulacro final:** archivo en `simulacro/SIM-...html` con nombre corto, y biblioteca `"Simulacro Final"` (para que quede en su módulo aparte, no mezclado con las generales).
- **Comportamentales:** biblioteca `"Por Nivel"` (no "Comportamental").
- **VALIDAR** cada guía: `node --check` del JS + `scripts/validar-guia.py` + grep de fugas = 0.
- **Registrar** cada guía en `biblioteca/biblioteca.json` Y `plataforma/lib/biblioteca.json` (sincronizados), sincronizar a `plataforma/public/seed-guias/`, y agregar el **plan plantilla** a `plataforma/lib/autocargarGuias.ts` para el botón de 1 clic.

**Flujo de trabajo esperado:**
1. Pídeme (o lee del expediente) el nombre del aspirante, su cargo, código de empleo, convocatoria, dependencia y perfil. Si su expediente/manual de vacante está en el repo (rama `expediente-<aspirante>` o `docs-<aspirante>`), léelo.
2. Escribe un spec corto del curso (como `_SPEC-CURSO-3PU15-LEYNER.md`) con el plan de 21 días mapeado a moldes.
3. Construye la guía PILOTO (una funcional central del cargo), valídala, púshéala y pásame el enlace para mi visto bueno ANTES de producir las 20 restantes.
4. Con mi OK, produce el resto (puedes paralelizar con sub-agentes), push por tanda.
5. Cierra con: registro en biblioteca.json (x2), sync a seed-guias, plan plantilla, PR a main, y me pasas los pasos de carga.

**Empecemos:** confírmame que ya leíste `PROCESO-CURSOS-GUIAS.md` y el caso de referencia, y quédate esperando a que te dé los datos del **nuevo aspirante** (nombre, cargo, código, convocatoria y perfil).

## 👆 (fin del prompt)
