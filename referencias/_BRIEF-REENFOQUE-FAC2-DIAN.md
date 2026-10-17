# BRIEF DE REENFOQUE — Curso DIAN Facilitador II (OPEC 236906) · Paula Molina

> Instrucciones comunes para reenfocar un molde existente a la guía del curso.
> La guía PILOTO ya aprobada (sigue su calidad y formato exacto):
> `guias/FUN-COR-FAC2-01-correspondencia-comunicaciones-oficiales.html`

## DATOS FIJOS DEL CURSO (usar siempre)
- Aspirante: Paula Andrea Molina Salazar.
- Cargo: **Facilitador II** · OPEC **236906** · Convocatoria **DIAN 2676** · Entidad **DIAN**
  (Dirección de Impuestos y Aduanas Nacionales) · Nivel **Asistencial**.
- Concurso administrado por la **CNSC** (SÍ se menciona la CNSC como organizadora).
- Requisitos del cargo: **título de bachiller** + **un (1) año de experiencia laboral**.
- Rol real: apoyo administrativo y operativo en una **Dirección Seccional de la DIAN** (o nivel
  central). Proyecta/alista documentos rutinarios; gestión documental (transferencia, recepción,
  organización, clasificación, conservación, custodia, préstamo, consulta); controla ingreso/salida
  de correspondencia y expedientes; apoyo logístico en operativos/inspecciones/campañas; mensajería
  interna y externa. NO decide, NO fiscaliza, NO liquida: **facilita y ejecuta bajo instrucciones**.
- Dependencias DIAN para ambientar ejemplos: Gestión Documental, Fiscalización, Operación Aduanera,
  Cobranzas, Talento Humano, Servicio al Ciudadano, Asistencia al Cliente. Documentos típicos:
  oficios/requerimientos a contribuyentes y usuarios aduaneros, memorandos internos, autos, actos
  administrativos, respuestas a PQRSF, comunicaciones de entes de control.

## REGLAS DE REENFOQUE (OBLIGATORIAS)
1. Parte del MOLDE indicado, conserva TODA su estructura/CSS/secciones/scripts; reescribe el CONTENIDO.
2. Elimina TODA fuga del molde original (otro cargo/entidad/aspirante/código/convocatoria). En
   particular: "Citador", "6CI-04", "Auxiliar Administrativo", "5AM-10", "Analista I", "nivel Técnico",
   "Secretario", "Sustanciador", "Procuraduría/PGN", "Convocatoria 90-2026 / 242-2026 / 245-2026",
   "Resolución 212", "régimen especial", "no lo administra la CNSC", "Syndy", "246932", "198368".
   Para la DIAN: el concurso SÍ es CNSC (Convocatoria 2676). Nivel **Asistencial** (no Técnico).
3. Reescribe el ENFOQUE al rol real del Facilitador II (apoya/ejecuta, no decide). Ambienta TODOS los
   ejemplos .practica, casos, narrativa y checkpoints en la DIAN con nombres propios ficticios.
4. Metadata: `doc-ref` = CÓDIGO NUEVO; `<title>` acorde; kicker con el DÍA correcto; badge
   `📅 Día N de 21`; si el molde tiene badge de régimen, cámbialo a "🏛️ DIAN · CNSC"; `btnFinalizar`
   y su alert con "Finalizar Día N". Footer igual. (Si es INTRO/COMPORTAMENTAL/ENT, respeta su etiqueta
   especial de kicker en vez de "Día N", según corresponda — ver indicación por guía.)
5. Frases clave en `<mark>` (subrayado dorado). Fuentes oficiales reales con `target="_blank"`
   (dian.gov.co, funcionpublica.gov.co, secretariasenado.gov.co, corteconstitucional.gov.co,
   suin-juriscol, cnsc.gov.co). NO enlaces inventados/rotos.

## ESTÁNDAR DEL SIMULACRO DE CADA GUÍA (formato DIAN de 3 OPCIONES) — LO MÁS IMPORTANTE
Las preguntas viven en el 2º `<script>` como `const preguntas=[{nivel,tema,ctx,q,ops,correcta,expl}]`.
- Formato DIAN = **3 opciones**. Si el molde usa `barajar([0,1,2,3])` (4 opciones), cámbialo a
  `barajar([0,1,2])` y deja cada pregunta con EXACTAMENTE 3 `ops` y 3 `expl`. Si el molde ya usa 3, mantenlo.
- Reescribe TODAS las preguntas al estándar, ambientadas en el rol Facilitador II DIAN del tema:
  * `ctx`: **550-1000 car** (ideal ~680-780), escenario situado con personas con nombre, antecedentes,
    VARIAS presiones y un distractor plausible.
  * `q`: **2-4 renglones (230-430 car)** que REPLANTEA la tensión e induce a decidir. NUNCA de una línea
    ni "¿cuál es la actuación correcta?" a secas.
  * `ops`: 3 opciones, cada una **mín 150, ideal 200-320 car**, todas plausibles y confusas, mismo nivel
    de detalle; la correcta no se delata por ser la única larga. VARÍA la posición de la correcta.
  * `expl`: 3 explicaciones (una por opción); la correcta empieza con "Correcto.".
  * Variedad de aperturas entre preguntas. Mantén el nº de preguntas que trae el molde (si es guía
    funcional/general suelen ser 5; respeta lo que haya) y conserva el TEMA de cada una.
- Conserva EXACTO el formato de checkpoints (.cp-opt data-ans='1' = correcta) y casos; solo reenfoca.
- Flashcards: reescríbelas al rol Facilitador II DIAN manteniendo el formato {f,b}.

## CALIDAD DEL DESARROLLO (sección data-sec="2")
- Debe quedar en **>= 10.000 palabras** (para INTRO/COMPORTAMENTAL/ENT, igualar o superar lo que trae el
  molde; para FUNCIONALES y GENERALES el piso es 10.000). No recortar: mantener o ampliar.
- Cada módulo: teoría con <h4>, VARIAS tablas, VARIOS ejemplos .practica (rol DIAN), acordeones .acc,
  .ojo, .flujo donde sea proceso, checkpoint, .idea. Cierre: Idea clave + Tips + Frase para recordar + .fuentes.

## VALIDACIÓN ANTES DE TERMINAR (hazla tú, no me entregues sin esto)
Intérprete: `/projects/sandbox/ASCENSO-PUBLICO/.venv/bin/python3`; node: `~/.nvm/versions/node/*/bin/node`.
1. Extrae los `<script>` y `node --check` → sin errores.
2. `python3 scripts/validar-guia.py guias/ARCHIVO.html "Día N"` desde el repo → Desarrollo >=10.000,
   HTML balanceado, día coherente. (Avisos esperados: "preguntas simulacro: N" si usa otro formato, y
   falsos positivos de fuga "DIAN/contribuyente/tributari" = OK, es el cargo correcto.)
3. Mide preguntas: 0 ctx<550, 0 q<230, 0 opciones<150, exactamente 3 ops y 3 expl por pregunta.
4. Fugas = 0 con grep de los términos del punto 2 de reglas.
5. `<div` abiertos == `</div>` cerrados.
Reporta: ruta, palabras Desarrollo, nº preguntas + min ctx/q/op, node --check, fugas. NO commit/push.
