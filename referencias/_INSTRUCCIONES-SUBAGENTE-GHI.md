# INSTRUCCIONES PARA CONSTRUIR UNA GUÍA — Curso DIAN Gestor I (Talento Humano) · Clary

Lee esto COMPLETO antes de escribir. Produces UNA guía HTML premium, nivel curso virtual de pago.

## Contexto del cargo (OBLIGATORIO ambientar TODO en esto)
- **Cargo:** Gestor I — Nivel **Profesional** de la **DIAN**, OPEC 236897, ficha TH-GH-3010.
- **Proceso: TALENTO HUMANO / GESTIÓN HUMANA** (NO es tributario/aduanero/fiscalización).
- El servidor gestiona: historias laborales, gestión del empleo (vinculación, situaciones
  administrativas, carrera administrativa), nómina y seguridad social, evaluación del desempeño (EDL),
  capacitación (PIC), bienestar laboral, SST, competencias laborales, apropiación de valores éticos.
- Trabaja en el área/coordinación de Talento Humano de una Dirección Seccional o del Nivel Central.
- Actúa bajo supervisión del superior inmediato; EJECUTA e IMPLEMENTA procedimientos; NO decide
  políticas de personal (eso es del jefe de Gestión Humana / Subdirección de Personal).
- La DIAN es concurso **CNSC** (prueba escrita 2676) → SÍ se puede mencionar la CNSC como organizadora.

## MOLDE ESTRUCTURAL (copiar su estructura, CSS y JS; reescribir TODO el contenido)
`guias/FUN-ADU-DOC-01-gestion-documental-pqrsf-servicio-tic.html`
- Head/CSS/footer idénticos (marca navy/oro, #readbar, nav sticky, flashcards, renderQuiz, botón finalizar).
- 11 secciones: 0 Objetivo · 1 Importancia · 2 **Desarrollo** · 3 Comparaciones · 4 Casos · 5 Errores ·
  6 Tips · 7 Trampas · 8 Repaso (flashcards) · 9 Resumen · 10 Simulacro.
- ⚠️ ELIMINAR TODA FUGA del molde: "Gestor II", "Buenaventura/Cali/Cartagena/Barranquilla" como seccional
  aduanera, "aduaner*", "importador", "agencia de aduanas", "servicio informático electrónico aduanero",
  "contribuyente", "subpartida/arancel". Reescribir al rol de Talento Humano.

## Sección 2 DESARROLLO — el núcleo (MÍNIMO 10.000 palabras)
- 7-9 módulos (`.modulo` con `.modulo-head`/`.modulo-n` numerados + `<h3>` y subtítulos `<h4>`).
- Cada módulo 600-1.200 palabras de teoría profunda y rigurosa (normas reales, clasificaciones,
  distinciones finas) EN EL ROL de Talento Humano.
- Por módulo, SIN EXCEPCIÓN: VARIAS tablas (`.tabla-wrap`+`table`), VARIOS ejemplos `.practica`
  ("En la práctica") ambientados en el día a día del Gestor I de TH; `.ojo` ("Ojo en la prueba");
  acordeones `details.acc` con contenido real; `.flujo` con pasos numerados si el tema es un proceso.
- 3-4 `.checkpoint` interactivos repartidos (con `data-cp`, `.cp-opt` y `data-ans`, y `#cpfbN`).
- Frases clave en `<mark>` (se ve como subrayado dorado).
- Cierre del Desarrollo: box "💡 Idea clave" + box de Tips + box dorado "⚡ Frase para recordar" +
  bloque `.fuentes` con enlaces DIRECTOS y REALES (`target="_blank"`) a normas en
  funcionpublica.gov.co, secretariasenado.gov.co, suin-juriscol, dian.gov.co, archivogeneral.gov.co, etc.

## Secciones 3-9 (completas, no de relleno)
- 3 Comparaciones: tabla(s) + `.trampa` de distinciones que confunde la prueba.
- 4 Casos: 2-3 `.caso` resueltos del rol TH (situación → análisis → respuesta correcta `.resp-correcta`).
- 5 Errores comunes. 6 Tips. 7 Trampas (`.trampa` con t-row parece/malo/bueno). 
- 8 Repaso: array `flashcards` (10 tarjetas) con preguntas/respuestas reales del tema.
- 9 Resumen: `.resumen` con items + glosario `.glosario` (dl/dt/dd) de 8-12 términos.

## Sección 10 SIMULACRO — 12 preguntas al ESTÁNDAR (lo más vigilado)
Array `const preguntas=[{nivel,tema,ctx,q,ops,correcta,expl}]` (claves SIN comillas, formato JS del molde).
- **3 opciones** (A/B/C) — formato DIAN. `correcta` es índice 0/1/2, VARIADO (no siempre el mismo).
- `ctx` (contexto): **550-1000 caracteres** (ideal ~700). Escenario situado con PERSONAS CON NOMBRE
  (compañeros, jefe de talento humano, un servidor que reclama), dependencia, antecedentes, VARIAS
  presiones y un distractor plausible. VARÍA las aperturas (no todas "Eres Gestor I...").
- `q` (enunciado): **230-430 caracteres**, 2-4 renglones, que REPLANTEA la tensión e induce a decidir.
  NUNCA "¿cuál es la actuación correcta?" a secas.
- `ops`: 3 opciones de **150-345 caracteres CADA UNA**, todas plausibles y del mismo nivel de detalle;
  la correcta NO se delata por ser la más larga. Trampa típica: A salida cómoda, C extremo que suena
  técnico, B correcta que exige comprensión.
- `expl`: lista de 3 explicaciones (una por opción), la correcta con ✔ al inicio.
- Distribución de nivel: ~4 "b", ~5 "i", ~3 "a". Los `.dific-tags` deben cuadrar.
- Flashcards (sección 8) también deben ser 10 y del tema.

## Metadata/identidad (ajustar según la guía asignada)
- `<span class="doc-ref">CÓDIGO</span>`, `<title>CÓDIGO · Título — Ascenso Público</title>`.
- kicker `Día N · Funcional` / badge `📅 Día N de 21`.
- Botón finalizar: `✅ Finalizar Día N` y confirm con el día correcto; `window.parent.postMessage(...)`.
- footer: `CÓDIGO · Día N · v1.0 · © 2026 Ascenso Público ...`.
- El día N y el "mañana: Día N+1 ..." según el plan.

## VALIDACIÓN que debe pasar (hazla tú antes de terminar)
- `node --check` del JS extraído (0 errores de sintaxis).
- `<div>` == `</div>` balanceados; `<section>`/`<details>`/`<table>` balanceados.
- Desarrollo ≥ 10.000 palabras.
- `python3 scripts/validar-preguntas.py ARCHIVO` → 0 ctx<550, 0 q<110, 0 ops<150, nops={3}.
- 0 fugas: `grep -icE "aduaner|importador|contribuyente|Gestor II|subpartida|arancel"` = 0.
Escribe el archivo final en `guias/CÓDIGO-....html`. NO hagas commit (lo hace el orquestador).
