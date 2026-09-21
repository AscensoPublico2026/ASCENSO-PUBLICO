# SPEC de construcción — Curso Leyner Urrego (Profesional Universitario 3PU-15 · PGN Conv. 112-2026)

## Contexto del cargo (usar en TODOS los ejemplos)
- Cargo: **Profesional Universitario 3PU-15**, Procuraduría General de la Nación (PGN), Convocatoria **112-2026**.
- Proceso: **Disciplinario**, Dirección Nacional de Investigaciones Especiales.
- Perfil del aspirante: **Contador Público** → énfasis **financiero-contable** fuerte.
- Funciones reales: apoyo técnico-científico a investigaciones disciplinarias; analiza información financiera/contable/tributaria; evalúa proyectos y contratos; verifica ejecución presupuestal; rinde **dictámenes**; ejerce **Policía Judicial**; asiste a audiencias. Cargo PROFESIONAL que **decide y conceptúa con criterio** (NO operativo).
- Régimen: PGN es **régimen especial** → el concurso **NO lo administra la CNSC** (solo se puede mencionar para aclarar "NO es CNSC").

## MÉTODO TÉCNICO OBLIGATORIO (para que valide a la primera)
1. La MEJOR forma es **partir del molde** `referencias/_MOLDE-DINAMICO-PU15.html` (es el Día 12 ya aprobado). Copiarlo al archivo destino y REEMPLAZAR el contenido (metadata, secciones, JS de flashcards y preguntas), conservando TODO el CSS y el andamiaje JS (barra de progreso, nav, checkpoints, flashcards, quiz, reveal).
2. Estructura de 11 secciones (data-sec 0..10): 0 Objetivo, 1 Importancia, 2 **Desarrollo**, 3 Distinciones, 4 Casos, 5 Errores, 6 Tips, 7 Trampas, 8 Repaso (flashcards), 9 Resumen, 10 Simulacro.
3. **Desarrollo (data-sec="2") = MÍNIMO 10.000 palabras**, 8 módulos (`<h3 class="modulo">`), cada uno 900-1.400 palabras con: teoría profunda con `<h4>` y frases clave en `<mark>`; VARIAS tablas (`.tabla-wrap>table`); VARIOS ejemplos `.practica` ("🛠️ En la práctica") ambientados en el rol 3PU-15 financiero; acordeones `details.acc`; tarjetas `.datoclave`; reto `.reto` (details con "¿Tú qué harías?"); cinta `.retoexpres` al cierre del módulo; `.flujo` con `.flujo-paso` numerados cuando el tema sea un proceso; 3-4 `.checkpoint` interactivos repartidos.
4. **Elementos dinámicos (lo que pidió el cliente): tono conversacional, `.datoclave`, `.reto`, `.retoexpres`, acordeones.**
5. Cierre del Desarrollo: `.box.key` (Idea clave) + `.box.tips` + `.box.gold` (⚡ Frase para recordar) + `.fuentes` con enlaces DIRECTOS y VERIFICADOS a las normas (secretariasenado.gov.co, funcionpublica.gov.co, corteconstitucional.gov.co, suin-juriscol, etc., con target=_blank).
6. **Simulacro (sección 10 / JS `const preguntas`)**: 5 preguntas de juicio situacional tipo prueba escrita PGN: `ctx` de 6-10 renglones (≥450 car) situado en el rol con presiones/distractores; `q` que replantea; 4 `ops` largas y elaboradas (150-280 car c/u, todas plausibles); `correcta` (índice) y `expl` (4 explicaciones). Formato objeto: `{nivel:'b'|'i'|'a', tema:'...', ctx:'...', q:'...', ops:[4], correcta:N, expl:[4]}`.
7. **Flashcards (JS `const flashcards`)**: 12 objetos `{f:'pregunta', b:'respuesta'}` del tema del día.
8. **Checkpoints**: markup `.checkpoint > .cp-q + <p> + varias .cp-op[data-ok="0|1"] + .cp-fb`. El handler JS ya está en el molde (busca `.checkpoint`/`.cp-op`/`data-ok`/`.cp-fb`). NO cambiar el handler.

## METADATA a cambiar por guía (coherencia de día)
- `<title>` y `.doc-ref`, `.kicker` = "Día N · <tema>", `<h1>`, `.header-sub` (subtítulo, el <strong> en BLANCO), `.badge` = "📅 Día N de 21", y en el JS el mensaje `btnFinalizar` = "✅ Has finalizado el Día N: <tema>...". El día N sale de biblioteca.json / del plan (ver tabla). El header-sub <strong> debe verse BLANCO.

## ANTI-FUGAS (crítico, 0 tolerancia)
- Borrar TODO rastro de otros cargos/cursos: `3PU-17`, `147-2026`, `Sustanciador`, `Procurador Judicial`, `4SU-`, `gina`, `Viviana`, `Auxiliar Administrativo`, `CNSC` como organizadora, otras entidades (DIAN, URT, etc.).
- El único código válido es **3PU-15** y la única convocatoria **112-2026**.
- Si se parte de una plantilla de otro cargo, REESCRIBIR EL ENFOQUE (no solo cambiar términos): nivel profesional que "interviene, dictamina y conceptúa con criterio".

## VALIDACIÓN antes de dar por terminada cada guía
- `python3 scripts/validar-guia.py <archivo> "Día N"` → debe decir `Desarrollo >=10.000`, secciones/main/div/table/details balanceados, preguntas simulacro: 5, Día N coherente. (El validador marca `3PU-15` como "posible fuga": es FALSO POSITIVO, es el cargo correcto; verificar que NO aparezca 3PU-17.)
- Extraer los `<script>` y correr `node --check` (node en `~/.nvm/versions/node/*/bin/node`).
- `grep` de fugas reales = 0.
