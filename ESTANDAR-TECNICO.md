# Ascenso Público — Estándar Técnico de Guías

> **Documento de referencia técnica.** Permite reconstruir cualquier guía desde cero conservando la identidad visual y los componentes interactivos.
>
> **Versión:** 1.0 — extraída de `INTRO-00-presentacion-curso.html` y `GEN-01-estado-funcion-publica.html`
> **Estructura del archivo HTML:** Un solo `.html` autocontenido. Estructura: `<head>` con `<style>` → `<body>` con `<div id="readbar">`, `<header>`, `<nav>`, `<main>` con secciones, `<footer>` y `<script>` final.

---

## 1. Cabecera HTML estándar

Todas las guías arrancan con la misma cabecera:

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{CODIGO} · {Nombre de la guía} — Ascenso Público</title>
<link rel="icon" type="image/svg+xml" href="../brand/favicon.svg">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" rel="stylesheet">
<style>
  /* ... CSS de §2 ... */
</style>
</head>
```

> **Ruta del favicon:** las guías viven en `guias/`, por eso el favicon se referencia como `../brand/favicon.svg` (sube un nivel a la carpeta `brand/`). El logo del header va **inline** como SVG, así que no depende de rutas externas.

**Tipografías oficiales:**
- `'Plus Jakarta Sans'` (sans-serif) — texto general
- `'Source Serif 4'` (serif) — títulos H1, H2 y números grandes

---

## 2. Sistema de variables CSS (paleta y tokens)

Esto va al inicio del `<style>` y NO se modifica entre guías:

```css
:root {
  /* ===== PRINCIPALES (30%) ===== */
  --azul:        #0A2A5E;   /* Azul institucional */
  --azul-medio:  #1A4A8A;
  --azul-claro:  #2D6CC0;
  --azul-suave:  #EAF1FB;   /* fondo info */
  --azul-borde:  #C9DCF4;

  /* ===== ACENTO CÁLIDO (10%) ===== */
  --oro:         #E8A33D;   /* dorado cálido — guiño bandera */
  --oro-claro:   #F6C56B;
  --oro-suave:   #FDF4E3;
  --oro-borde:   #F0DCB0;

  /* ===== FONDO (60%) ===== */
  --crema:       #FBF9F4;   /* fondo cálido, baja fatiga */
  --blanco:      #FFFFFF;
  --gris-bg:     #F2F0EA;
  --gris-borde:  #E6E2D8;

  /* ===== SEMÁNTICOS ===== */
  --verde:       #1A7A4A;   --verde-suave: #E8F6EE;   --verde-borde:#BFE6CF;
  --rojo:        #C0392B;   --rojo-suave:  #FCEDEB;   --rojo-borde: #F2CDC8;
  --ambar:       #B8600A;   --ambar-suave: #FBEFDD;   --ambar-borde:#EFD7B0;

  /* ===== TEXTO ===== */
  --texto:       #2A3441;
  --texto-suave: #5B6675;

  --sombra:      0 4px 20px rgba(10,42,94,0.08);
  --sombra-lg:   0 10px 36px rgba(10,42,94,0.16);
  --radio:       16px;
}
```

---

## 3. Reset y body base

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: var(--crema);
  color: var(--texto);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}
#readbar {
  position: fixed; top: 0; left: 0; height: 4px; width: 0%;
  background: linear-gradient(90deg, var(--oro), var(--oro-claro));
  z-index: 999; transition: width 0.1s linear;
}
```

---

## 4. Header con logo, kicker y badges

### HTML

```html
<header>
  <span class="doc-ref">{CODIGO}</span>
  <div class="brand">
    <div class="brand-logo">
      <!-- SVG inline del logo (ver brand/logo-ascenso-publico.svg) -->
      <svg viewBox="0 0 60 60" width="32" height="32">
        <!-- ... contenido del logo ... -->
      </svg>
    </div>
    <div>
      <div class="brand-name">Ascenso Público</div>
      <div class="brand-slogan">Tu ruta personalizada al ascenso público</div>
    </div>
  </div>
  <div class="kicker">{Día X · Categoría}</div>
  <h1>{Título completo de la guía}</h1>
  <p class="header-sub">{Subtítulo motivacional, máximo 2 líneas}</p>
  <!-- Badges (solo si NO es INTRO) -->
  <div class="badges">
    <span class="badge">📅 Día X de 21</span>
    <span class="badge">⏱ 75-90 min</span>
    <span class="badge">🎯 Prueba escrita CNSC</span>
  </div>
</header>
```

### CSS

```css
header {
  background: linear-gradient(140deg, #08234F 0%, var(--azul) 45%, var(--azul-medio) 100%);
  color: var(--blanco);
  padding: 42px 20px 36px;
  text-align: center;
  position: relative;
  overflow: hidden;
}
header::before {
  content:''; position:absolute; top:-60px; right:-60px;
  width: 220px; height: 220px; border-radius: 50%;
  background: radial-gradient(circle, rgba(232,163,61,0.22), transparent 70%);
}
header::after {
  content:''; position:absolute; bottom:0; left:0; right:0; height:5px;
  background: linear-gradient(90deg, var(--oro) 0%, var(--oro-claro) 50%, var(--oro) 100%);
}
.brand { display: inline-flex; align-items: center; gap: 13px; position: relative; z-index: 2; }
.brand-logo {
  width: 50px; height: 50px; border-radius: 13px;
  background: linear-gradient(135deg, var(--oro-claro), var(--oro));
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 6px 18px rgba(232,163,61,0.4);
}
.brand-name { font-size: 1.6rem; font-weight: 800; }
.brand-slogan { font-size: 0.82rem; color: rgba(255,255,255,0.78); margin-top: 4px; }
.doc-ref {
  position: absolute; top: 16px; right: 18px; z-index: 3;
  font-size: 0.68rem; font-weight: 700; letter-spacing: 0.16em;
  color: rgba(255,255,255,0.55);
  border: 1px solid rgba(255,255,255,0.22);
  padding: 4px 11px; border-radius: 7px; text-transform: uppercase;
}
.kicker {
  display: inline-flex; align-items: center; gap: 11px;
  margin: 24px 0 12px; position: relative; z-index: 2;
  color: var(--oro-claro); font-weight: 700; font-size: 0.78rem;
  letter-spacing: 0.2em; text-transform: uppercase;
}
.kicker::before, .kicker::after {
  content:''; width: 26px; height: 2px; border-radius: 2px;
  background: linear-gradient(90deg, transparent, var(--oro), transparent);
}
header h1 {
  font-family: 'Source Serif 4', serif;
  font-size: clamp(1.7rem, 4.5vw, 2.6rem);
  font-weight: 700; line-height: 1.16; max-width: 740px; margin: 0 auto;
  position: relative; z-index: 2;
}
.header-sub {
  max-width: 600px; margin: 18px auto 0; position: relative; z-index: 2;
  color: rgba(255,255,255,0.82); font-size: 0.98rem;
}
```

---

## 5. Navegación sticky

```html
<nav>
  <button class="active" data-sec="0">🎯 Objetivo</button>
  <button data-sec="1">⭐ Importancia</button>
  <button data-sec="2">📖 Desarrollo</button>
  <button data-sec="3">⚖️ Comparaciones</button>
  <button data-sec="4">📂 Casos</button>
  <button data-sec="5">⚠️ Errores</button>
  <button data-sec="6">💡 Tips</button>
  <button data-sec="7">🎭 Trampas</button>
  <button data-sec="8">🧠 Repaso</button>
  <button data-sec="9">📝 Resumen</button>
  <button data-sec="10">🎓 Simulacro</button>
</nav>
```

```css
nav {
  position: sticky; top: 0; z-index: 50;
  background: var(--azul);
  display: flex; gap: 5px; padding: 11px 12px;
  overflow-x: auto;
  box-shadow: 0 4px 18px rgba(10,42,94,0.22);
}
nav button {
  background: rgba(255,255,255,0.07); color: rgba(255,255,255,0.78);
  border: none; padding: 9px 16px; border-radius: 9px;
  cursor: pointer; font-weight: 600; white-space: nowrap;
}
nav button:hover { background: rgba(255,255,255,0.16); color: #fff; }
nav button.active {
  background: linear-gradient(135deg, var(--oro), var(--oro-claro));
  color: var(--azul);
  box-shadow: 0 4px 12px rgba(232,163,61,0.4);
}
```

---

## 6. Secciones principales

Cada sección sigue este patrón:

```html
<main>
  <section class="section visible" data-sec="0">
    <span class="eyebrow">Sección 1 · Objetivo</span>
    <h2 class="sec-title">🎯 ¿Qué vas a aprender hoy?</h2>
    <div class="card card-lead">
      <p>{intro de 2-3 líneas}</p>
      <ul class="lista">
        <li>Aprenderás a identificar...</li>
        <li>Comprenderás la diferencia entre...</li>
      </ul>
    </div>
    <!-- El botón "Avanzar" lo agrega el JS al final -->
  </section>

  <section class="section" data-sec="1">
    <!-- ... -->
  </section>
  <!-- ... más secciones ... -->
</main>
```

```css
main { max-width: 880px; margin: 0 auto; padding: 36px 18px 80px; }
.section { display: none; animation: fade 0.4s ease; }
.section.visible { display: block; }
@keyframes fade { from { opacity: 0; transform: translateY(12px);} to { opacity:1; transform:none;} }

.eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  color: var(--ambar); font-weight: 700; font-size: 0.78rem;
  letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 12px;
}
.eyebrow::before {
  content:''; width: 26px; height: 3px;
  background: linear-gradient(90deg,var(--oro),var(--oro-claro));
  border-radius: 3px;
}
h2.sec-title {
  font-family: 'Source Serif 4', serif;
  font-size: clamp(1.55rem, 3.6vw, 2.1rem); color: var(--azul);
  line-height: 1.2; margin-bottom: 20px;
}
```

---

## 7. Componente "Concepto en 4 capas" (CORAZÓN del Desarrollo)

### HTML

```html
<div class="concepto">
  <div class="concepto-head">
    <span class="ch-icon">🏛️</span>
    <span>{Nombre del concepto}</span>
  </div>
  <div class="concepto-body">

    <div class="capa cap-def">
      <div class="capa-icon def">📘</div>
      <div class="capa-content">
        <span class="label">Definición</span>
        <p>{Qué es exactamente, con norma/artículo. 2-4 párrafos cortos.}</p>
      </div>
    </div>

    <div class="capa cap-apl">
      <div class="capa-icon apl">🎯</div>
      <div class="capa-content">
        <span class="label">Aplicación</span>
        <p>{Para qué sirve, cómo opera en la práctica.}</p>
      </div>
    </div>

    <div class="capa cap-eje">
      <div class="capa-icon eje">🏛️</div>
      <div class="capa-content">
        <span class="label">Ejemplo real</span>
        <p>{Caso real verificable: entidad, OPEC, etc.}</p>
      </div>
    </div>

    <div class="capa cap-cnsc">
      <div class="capa-icon cnsc">📝</div>
      <div class="capa-content">
        <span class="label">Cómo lo evalúa la CNSC</span>
        <p>{Cómo aparece en la prueba, trampas típicas.}</p>
      </div>
    </div>

  </div>
</div>
```

### CSS

```css
.concepto {
  background: var(--blanco);
  border: 1px solid var(--oro-borde);
  border-radius: var(--radio); margin: 18px 0;
  box-shadow: var(--sombra); overflow: hidden;
}
.concepto-head {
  background: linear-gradient(100deg, var(--oro-suave), var(--blanco) 80%);
  padding: 16px 22px;
  font-size: 1.08rem; font-weight: 700; color: var(--azul);
  display: flex; align-items: center; gap: 11px;
  border-bottom: 1px dashed var(--oro);
}
.ch-icon { font-size: 1.4rem; }
.concepto-body {
  display: grid; grid-template-columns: 1fr; gap: 12px;
  padding: 20px 22px;
}
@media (min-width: 700px) {
  .concepto-body { grid-template-columns: 1fr 1fr; }
}
.capa {
  display: flex; gap: 12px; padding: 14px 16px;
  background: var(--gris-bg); border-radius: 12px;
  border: 1px solid var(--gris-borde); transition: transform 0.18s;
}
.capa:hover { transform: translateY(-2px); }
.capa-icon {
  width: 38px; height: 38px; border-radius: 10px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.25rem;
}
.capa-icon.def  { background: var(--azul-suave); }
.capa-icon.apl  { background: var(--verde-suave); }
.capa-icon.eje  { background: var(--oro-suave); }
.capa-icon.cnsc { background: var(--rojo-suave); }
.capa-content .label {
  display: block; font-size: 0.7rem; font-weight: 800;
  text-transform: uppercase; letter-spacing: 0.08em;
  margin-bottom: 4px;
}
.capa.cap-def  .label { color: var(--azul-claro); }
.capa.cap-apl  .label { color: var(--verde); }
.capa.cap-eje  .label { color: var(--ambar); }
.capa.cap-cnsc .label { color: var(--rojo); }
.capa-content p { font-size: 0.9rem; margin: 0; }
```

---

## 8. Sub-bloques desplegables (patrón "concepto madre")

Para conceptos con sub-componentes evaluables (ramas del poder, órganos autónomos, etc.). Se ubican **dentro** de `.concepto-body` después de las 4 capas.

### HTML

```html
<div class="sub-bloques">
  <details class="sb sb-violeta" open>
    <summary>📜 Rama Legislativa</summary>
    <div class="sb-body">
      <p><strong>Quién la conforma:</strong> ...</p>
      <p><strong>Funciones:</strong> ...</p>
      <div class="tabla-wrap">
        <table>...</table>
      </div>
      <div class="box warn">
        <div class="box-title">⚠️ Trampa CNSC</div>
        <p>...</p>
      </div>
      <details class="miniq">
        <summary>🎯 Pregunta tipo CNSC</summary>
        <p>...{enunciado}</p>
        <p><strong>✓ Respuesta:</strong> ...</p>
      </details>
    </div>
  </details>

  <details class="sb sb-oro">
    <summary>🏛️ Rama Ejecutiva</summary>
    ...
  </details>
</div>
```

### CSS

```css
.sub-bloques { display: flex; flex-direction: column; gap: 10px; margin-top: 14px; }
.sb {
  border: 1.5px solid var(--gris-borde); border-radius: 12px;
  background: var(--blanco); overflow: hidden;
}
.sb summary {
  padding: 13px 18px; font-weight: 700; cursor: pointer;
  display: flex; align-items: center; gap: 10px;
  list-style: none; user-select: none;
}
.sb summary::-webkit-details-marker { display: none; }
.sb summary::after {
  content: '▾'; margin-left: auto;
  transition: transform 0.2s;
}
.sb[open] summary::after { transform: rotate(180deg); }
.sb-violeta summary { background: #F5F0FB; color: #5B3F8C; border-left: 5px solid #8B6BC9; }
.sb-oro summary    { background: var(--oro-suave); color: var(--ambar); border-left: 5px solid var(--oro); }
.sb-verde summary  { background: var(--verde-suave); color: var(--verde); border-left: 5px solid var(--verde); }
.sb-azul summary   { background: var(--azul-suave); color: var(--azul); border-left: 5px solid var(--azul-claro); }
.sb-body { padding: 16px 20px; }
.miniq {
  margin-top: 12px; background: var(--azul-suave);
  border-radius: 10px; padding: 10px 14px;
}
.miniq summary { font-weight: 700; color: var(--azul); cursor: pointer; }
```

---

## 9. Cajas destacadas (info, ok, warn, danger, gold)

```html
<div class="box info">
  <div class="box-title">ℹ️ Para tener en cuenta</div>
  <p>...</p>
</div>
<div class="box warn"><div class="box-title">⚠️ Atención</div><p>...</p></div>
<div class="box danger"><div class="box-title">❌ Error frecuente</div><p>...</p></div>
<div class="box ok"><div class="box-title">✅ Tip</div><p>...</p></div>
<div class="box gold"><div class="box-title">💎 Importante</div><p>...</p></div>
```

```css
.box { border-radius: 13px; padding: 18px 20px; margin: 16px 0; border: 1px solid; }
.box-title { font-weight: 700; display: flex; align-items: center; gap: 8px; margin-bottom: 7px; }
.box.info   { background: var(--azul-suave); border-color: var(--azul-borde); }
.box.info .box-title { color: var(--azul); }
.box.ok     { background: var(--verde-suave); border-color: var(--verde-borde); }
.box.ok .box-title { color: var(--verde); }
.box.warn   { background: var(--ambar-suave); border-color: var(--ambar-borde); }
.box.warn .box-title { color: var(--ambar); }
.box.danger { background: var(--rojo-suave); border-color: var(--rojo-borde); }
.box.danger .box-title { color: var(--rojo); }
.box.gold   { background: var(--oro-suave); border-color: var(--oro-borde); }
.box.gold .box-title { color: var(--ambar); }
```

---

## 10. Casos CNSC

```html
<div class="caso">
  <div class="caso-head">📂 Caso 1 · {Título corto}</div>
  <div class="caso-body">
    <span class="label">Situación</span>
    <p>...</p>
    <span class="label">Pregunta</span>
    <p>...</p>
    <span class="label">Respuesta</span>
    <div class="resp-correcta">
      <strong>✅ {Opción correcta}</strong> — {explicación}
    </div>
  </div>
</div>
```

```css
.caso {
  background: var(--blanco); border: 1px solid var(--gris-borde);
  border-radius: 14px; overflow: hidden; margin: 16px 0;
  box-shadow: var(--sombra);
}
.caso-head {
  background: linear-gradient(135deg, var(--azul), var(--azul-medio));
  color: #fff; padding: 13px 18px; font-weight: 700;
}
.caso-body { padding: 18px 20px; }
.caso-body .label {
  font-weight: 800; color: var(--ambar); display: block;
  margin-top: 14px; margin-bottom: 3px; font-size: 0.76rem;
  text-transform: uppercase; letter-spacing: 0.06em;
}
.caso-body .label:first-child { margin-top: 0; }
.resp-correcta {
  background: var(--verde-suave); border-left: 4px solid var(--verde);
  padding: 11px 15px; border-radius: 9px; margin-top: 8px;
}
```

---

## 11. Flashcards interactivas (sección Repaso)

### HTML

```html
<div class="flashcard-wrap">
  <div id="flashcard" class="flashcard">
    <div class="flash-face flash-front">
      <span class="flash-tag">Pregunta</span>
      <p id="flashFront"></p>
      <small class="flash-hint">Toca para ver la respuesta</small>
    </div>
    <div class="flash-face flash-back">
      <span class="flash-tag">Respuesta</span>
      <p id="flashBack"></p>
    </div>
  </div>
  <div class="flash-controls">
    <button id="flashPrev">← Anterior</button>
    <span id="flashCounter">Tarjeta 1 de 10</span>
    <button id="flashFlip">Voltear</button>
    <button id="flashNext">Siguiente →</button>
  </div>
</div>
```

### CSS

```css
.flashcard-wrap { max-width: 560px; margin: 24px auto; perspective: 1200px; }
.flashcard {
  position: relative; height: 240px;
  transform-style: preserve-3d;
  transition: transform 0.5s; cursor: pointer;
}
.flashcard.flipped { transform: rotateY(180deg); }
.flash-face {
  position: absolute; inset: 0; backface-visibility: hidden;
  border-radius: var(--radio); padding: 28px;
  display: flex; flex-direction: column; justify-content: center;
  box-shadow: var(--sombra-lg);
}
.flash-front {
  background: linear-gradient(135deg, var(--oro-suave), var(--blanco));
  border: 2px solid var(--oro);
}
.flash-back {
  background: linear-gradient(135deg, var(--azul), var(--azul-medio));
  color: #fff; transform: rotateY(180deg);
}
.flash-tag {
  font-size: 0.7rem; font-weight: 800; letter-spacing: 0.16em;
  text-transform: uppercase; margin-bottom: 12px;
  color: var(--ambar);
}
.flash-back .flash-tag { color: var(--oro-claro); }
.flash-controls {
  display: flex; justify-content: space-between; align-items: center;
  gap: 8px; margin-top: 14px; flex-wrap: wrap;
}
.flash-controls button {
  background: var(--blanco); border: 1.5px solid var(--gris-borde);
  color: var(--azul); padding: 9px 16px; border-radius: 9px;
  cursor: pointer; font-weight: 700; font-size: 0.84rem;
}
```

### JS — array y lógica

```js
const flashcards = [
  { f:'¿Pregunta 1?', b:'Respuesta 1.' },
  { f:'¿Pregunta 2?', b:'Respuesta 2.' },
  // ... 10 en total
];

let flashIndex = 0;
const flashEl = document.getElementById('flashcard');
const flashFront = document.getElementById('flashFront');
const flashBack = document.getElementById('flashBack');
const flashCounter = document.getElementById('flashCounter');

function renderFlash() {
  flashEl.classList.remove('flipped');
  flashFront.textContent = flashcards[flashIndex].f;
  flashBack.textContent = flashcards[flashIndex].b;
  flashCounter.textContent = `Tarjeta ${flashIndex + 1} de ${flashcards.length}`;
}
flashEl.addEventListener('click', () => flashEl.classList.toggle('flipped'));
document.getElementById('flashFlip').addEventListener('click', e => {
  e.stopPropagation(); flashEl.classList.toggle('flipped');
});
document.getElementById('flashPrev').addEventListener('click', () => {
  flashIndex = (flashIndex - 1 + flashcards.length) % flashcards.length;
  renderFlash();
});
document.getElementById('flashNext').addEventListener('click', () => {
  flashIndex = (flashIndex + 1) % flashcards.length;
  renderFlash();
});
renderFlash();
```

---

## 12. Simulacro CNSC (4 opciones + retroalimentación + temas a reforzar)

### HTML

```html
<section class="section" data-sec="10">
  <span class="eyebrow">Sección 11 · Simulacro</span>
  <h2 class="sec-title">🎓 Simulacro tipo CNSC</h2>

  <div class="card card-lead quiz-intro">
    <p><strong>Formato CNSC — juicio situacional:</strong> cada pregunta presenta un <strong>caso/contexto</strong> real y un enunciado tipo "¿qué es lo más apropiado que debe hacer?", con 4 opciones de acción (A, B, C, D); solo una es la correcta. No se pregunta la norma de memoria.</p>
    <div class="dific-tags">
      <span class="tag b">4 básicas</span>
      <span class="tag i">5 intermedias</span>
      <span class="tag a">3 avanzadas</span>
    </div>
  </div>

  <div id="quiz"></div>

  <div style="text-align:center; margin: 28px 0;">
    <button id="btnCalcular" class="btn">Ver mi resultado</button>
  </div>

  <div id="resultado">
    <div class="score-num" id="scoreNum">0/12</div>
    <p id="scoreMsg"></p>
    <div id="temasReforzar"></div>
    <button id="btnReiniciar" class="btn gold">🔄 Repetir simulacro</button>
  </div>
</section>
```

### CSS

```css
.quiz-intro { text-align: center; }
.dific-tags {
  display: flex; justify-content: center; gap: 8px;
  flex-wrap: wrap; margin-top: 14px;
}
.tag { font-size: 0.75rem; font-weight: 700; padding: 5px 14px; border-radius: 20px; }
.tag.b { background: var(--verde-suave); color: var(--verde); }
.tag.i { background: var(--azul-suave); color: var(--azul); }
.tag.a { background: var(--rojo-suave); color: var(--rojo); }

.pregunta {
  background: var(--blanco); border: 1px solid var(--gris-borde);
  border-radius: 14px; padding: 21px 22px; margin-bottom: 16px;
  box-shadow: var(--sombra);
}
.q-num {
  display: inline-flex; align-items: center; gap: 9px;
  font-weight: 800; color: var(--azul); margin-bottom: 5px;
}
.nivel-pill {
  font-size: 0.66rem; font-weight: 700; padding: 3px 10px;
  border-radius: 20px; text-transform: uppercase;
}
.nivel-pill.b { background: var(--verde-suave); color: var(--verde); }
.nivel-pill.i { background: var(--azul-suave); color: var(--azul); }
.nivel-pill.a { background: var(--rojo-suave); color: var(--rojo); }

.q-contexto {
  background: var(--azul-suave); border-left: 4px solid var(--azul-claro);
  padding: 11px 14px; border-radius: 9px;
  font-size: 0.88rem; margin: 9px 0;
}
.q-texto { font-weight: 600; margin: 9px 0 15px; }

.opciones { display: flex; flex-direction: column; gap: 9px; }
.opcion {
  display: flex; align-items: flex-start; gap: 12px;
  border: 1.5px solid var(--gris-borde); border-radius: 11px;
  padding: 13px 15px; cursor: pointer; transition: all 0.18s; background: #fff;
}
.opcion:hover { border-color: var(--oro); background: var(--oro-suave); }
.opcion .letra {
  width: 27px; height: 27px; border-radius: 50%;
  background: var(--gris-bg); color: var(--texto-suave); font-weight: 800;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.opcion.correcta { border-color: var(--verde); background: var(--verde-suave); }
.opcion.correcta .letra { background: var(--verde); color: #fff; }
.opcion.incorrecta { border-color: var(--rojo); background: var(--rojo-suave); }
.opcion.incorrecta .letra { background: var(--rojo); color: #fff; }
.opcion.bloqueada { pointer-events: none; }

.feedback {
  margin-top: 12px; padding: 12px 15px; border-radius: 10px;
  font-size: 0.88rem; display: none;
}
.feedback.show { display: block; }
.feedback.ok { background: var(--verde-suave); border-left: 4px solid var(--verde); }
.feedback.no { background: var(--rojo-suave); border-left: 4px solid var(--rojo); }

#resultado {
  display: none; text-align: center; background: var(--blanco);
  border: 2px solid var(--oro); border-radius: 18px; padding: 32px;
  margin-top: 24px; box-shadow: var(--sombra-lg);
}
#resultado.show { display: block; }
.score-num {
  font-size: 3.2rem; font-weight: 800; color: var(--azul);
  font-family: 'Source Serif 4', serif;
}
.btn {
  background: linear-gradient(135deg, var(--azul), var(--azul-medio));
  color: #fff; border: none;
  padding: 13px 30px; border-radius: 11px;
  font-weight: 700; cursor: pointer;
}
.btn.gold {
  background: linear-gradient(135deg, var(--oro), var(--oro-claro));
  color: var(--azul);
}
```

### JS — array `preguntas` (esquema de cada item)

> **Formato de juicio situacional (tipo CNSC).** El enunciado y las opciones plantean un **caso** y posibles **cursos de acción**; la respuesta correcta es la actuación más apropiada. La explicación por opción (`expl`) sí cita la norma para reforzar. Por eso `ctx` está **presente en todas** las preguntas.

```js
const preguntas = [
  {
    nivel: 'b',                     // 'b' básica · 'i' intermedia · 'a' avanzada
    tema: 'Conflicto de intereses', // Aparece en "Temas a reforzar"
    ctx:  'Trabajas en contratación y llega para evaluación la propuesta de la empresa de tu hermano.', // El CASO (siempre presente)
    q:    '¿Cuál es la actuación más apropiada?',
    ops:  ['Acción A', 'Acción B', 'Acción C', 'Acción D'],
    correcta: 1,                    // índice 0-3
    expl: [                         // explicación POR opción (puede citar la norma)
      'Por qué la acción A no es la correcta',
      '✔ Por qué la acción B es la correcta',
      'Por qué la acción C no es la correcta',
      'Por qué la acción D no es la correcta'
    ]
  },
  // ... 12 en total: 4 básicas + 5 intermedias + 3 avanzadas
];
```

### JS — render del simulacro

```js
const quizDiv = document.getElementById('quiz');
let respondidas = {};

function renderQuiz() {
  respondidas = {};
  quizDiv.innerHTML = '';
  const nivelLabel = { b:'Básica', i:'Intermedia', a:'Avanzada' };
  preguntas.forEach((p, idx) => {
    const card = document.createElement('div');
    card.className = 'pregunta';
    let opsHtml = '';
    p.ops.forEach((op, j) => {
      const letra = String.fromCharCode(65 + j);
      opsHtml += `<div class="opcion" data-q="${idx}" data-op="${j}">
                    <span class="letra">${letra}</span><span>${op}</span>
                  </div>`;
    });
    const ctxHtml = p.ctx ? `<div class="q-contexto">${p.ctx}</div>` : '';
    card.innerHTML = `
      <div class="q-num">Pregunta ${idx+1}
        <span class="nivel-pill ${p.nivel}">${nivelLabel[p.nivel]}</span>
      </div>
      ${ctxHtml}
      <div class="q-texto">${p.q}</div>
      <div class="opciones">${opsHtml}</div>
      <div class="feedback" id="fb-${idx}"></div>`;
    quizDiv.appendChild(card);
  });

  document.querySelectorAll('.opcion').forEach(op => {
    op.addEventListener('click', function() {
      const qi = +this.dataset.q;
      const oi = +this.dataset.op;
      if (respondidas[qi] !== undefined) return;
      respondidas[qi] = oi;
      const p = preguntas[qi];
      const cont = this.parentElement;
      cont.querySelectorAll('.opcion').forEach((o, k) => {
        o.classList.add('bloqueada');
        if (k === p.correcta) o.classList.add('correcta');
      });
      const fb = document.getElementById('fb-' + qi);
      const letraCorrecta = String.fromCharCode(65 + p.correcta);
      if (oi === p.correcta) {
        fb.className = 'feedback ok show';
        fb.innerHTML = '✅ <strong>¡Correcto!</strong> ' + p.expl[p.correcta];
      } else {
        this.classList.add('incorrecta');
        fb.className = 'feedback no show';
        fb.innerHTML = '❌ <strong>Incorrecto.</strong> Tu opción: ' + p.expl[oi]
          + '<br><br>✅ <strong>La respuesta correcta es ' + letraCorrecta + ':</strong> '
          + p.expl[p.correcta];
      }
    });
  });
}
```

### JS — calcular resultado y temas a reforzar

```js
document.getElementById('btnCalcular').addEventListener('click', () => {
  let correctas = 0;
  const temasFallados = [];
  preguntas.forEach((p, i) => {
    if (respondidas[i] === p.correcta) correctas++;
    else if (temasFallados.indexOf(p.tema) === -1) temasFallados.push(p.tema);
  });
  const res = document.getElementById('resultado');
  document.getElementById('scoreNum').textContent = correctas + '/12';

  let msg;
  const pct = correctas / 12;
  if (pct >= 0.83) msg = '🏆 ¡Excelente! Listo para el siguiente día.';
  else if (pct >= 0.58) msg = '👍 Buen trabajo. Refuerza los temas marcados.';
  else msg = '📚 Vas por buen camino. Repasa los temas y repite el simulacro.';
  document.getElementById('scoreMsg').textContent = msg;

  const cont = document.getElementById('temasReforzar');
  if (temasFallados.length === 0) {
    cont.innerHTML = '<div class="box ok" style="text-align:left;">' +
      '<div class="box-title">🎯 ¡Sin temas pendientes!</div>' +
      '<p>Respondiste todo correctamente.</p></div>';
  } else {
    let items = temasFallados.map(t => '<li>' + t + '</li>').join('');
    cont.innerHTML = '<div class="box warn" style="text-align:left;">' +
      '<div class="box-title">📌 Temas que debes reforzar</div>' +
      '<p>Vuelve a la sección <strong>Desarrollo</strong> y repásalos:</p>' +
      '<ul class="lista">' + items + '</ul></div>';
  }
  res.classList.add('show');
  res.scrollIntoView({ behavior: 'smooth' });
});

document.getElementById('btnReiniciar').addEventListener('click', () => {
  renderQuiz();
  document.getElementById('resultado').classList.remove('show');
  window.scrollTo({
    top: document.querySelector('[data-sec="10"]').offsetTop,
    behavior: 'smooth'
  });
});

renderQuiz();
```

---

## 13. Botón "Avanzar" al final de cada sección

Se genera dinámicamente con JS — no se escribe en cada sección a mano.

### CSS

```css
.advance-bar {
  margin-top: 36px; padding-top: 22px;
  border-top: 2px dashed var(--oro);
  display: flex; align-items: center; justify-content: space-between;
  gap: 12px; flex-wrap: wrap;
}
.advance-hint { color: var(--texto-suave); font-style: italic; }
.advance-btn {
  background: linear-gradient(135deg, var(--oro), var(--oro-claro));
  color: var(--azul); border: none;
  padding: 12px 26px; border-radius: 11px;
  font-weight: 800; cursor: pointer;
  box-shadow: 0 4px 12px rgba(232,163,61,0.35);
  transition: all 0.2s;
}
.advance-btn:hover { transform: translateY(-2px); box-shadow: var(--sombra-lg); }
.advance-btn.final {
  background: linear-gradient(135deg, var(--verde), #2A9F66);
  color: #fff;
}
```

### JS

```js
const titulosCortos = [
  'Importancia',     // de Objetivo
  'Desarrollo',      // de Importancia
  'Comparaciones',
  'Casos CNSC',
  'Errores',
  'Tips',
  'Trampas',
  'Repaso',
  'Resumen',
  'Simulacro',
  null               // última sección → botón Finalizar
];

sections.forEach((sec, i) => {
  const bar = document.createElement('div');
  bar.className = 'advance-bar';
  if (i < sections.length - 1) {
    bar.innerHTML = `
      <span class="advance-hint">¿Listo para continuar?</span>
      <button class="advance-btn" data-target="${i + 1}">
        Avanzar a ${titulosCortos[i]} →
      </button>`;
  } else {
    bar.innerHTML = `
      <span class="advance-hint">🎓 Has completado todo el contenido</span>
      <button class="advance-btn final" data-target="finalizar">
        ✅ Finalizar Día {N}
      </button>`;
  }
  sec.appendChild(bar);
});

document.querySelectorAll('.advance-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const t = btn.dataset.target;
    if (t === 'finalizar') {
      alert('🎓 ¡Felicitaciones! Completaste el Día {N}.\n\nMañana avanzas con {SIGUIENTE GUÍA}.\n\n🚀');
    } else {
      showSection(parseInt(t));
    }
  });
});
```

---

## 14. Navegación entre secciones + barra de lectura

```js
const sections = document.querySelectorAll('.section');
const navBtns = document.querySelectorAll('nav button');

function showSection(i) {
  sections.forEach(s => s.classList.remove('visible'));
  navBtns.forEach(b => b.classList.remove('active'));
  sections[i].classList.add('visible');
  navBtns[i].classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
navBtns.forEach((btn, i) => btn.addEventListener('click', () => showSection(i)));

// Barra de lectura (top progress bar)
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  const scrolled = (h.scrollTop) / (h.scrollHeight - h.clientHeight) * 100;
  document.getElementById('readbar').style.width = scrolled + '%';
});
```

---

## 15. Footer

```html
<footer>
  <div class="fbrand">Ascenso Público</div>
  <div class="fslogan">Tu ruta personalizada al ascenso público</div>
  <div class="fmeta">
    {CODIGO} · Día {N} · v1.0 — junio 2026<br>
    © Ascenso Público — Todos los derechos reservados
  </div>
</footer>
```

```css
footer {
  background: var(--azul); color: rgba(255,255,255,0.8);
  text-align: center; padding: 28px 20px;
}
footer .fbrand { font-weight: 800; color: #fff; font-size: 1.05rem; }
footer .fslogan { font-size: 0.78rem; margin-top: 3px; color: var(--oro-claro); }
footer .fmeta {
  margin-top: 14px; font-size: 0.72rem;
  color: rgba(255,255,255,0.55); line-height: 1.7;
}
```

---

## 16. Logos SVG (recuperación de emergencia)

Si la carpeta `/brand/` se pierde, estos son los logos en SVG inline (V2 — flecha con impulso):

### Logo principal — `logo-ascenso-publico.svg`

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <rect width="100" height="100" rx="22" fill="url(#g)"/>
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F6C56B"/>
      <stop offset="100%" stop-color="#E8A33D"/>
    </linearGradient>
  </defs>
  <!-- Flecha de impulso -->
  <path d="M28 70 L52 30 L60 38 L72 30"
        stroke="#0A2A5E" stroke-width="6"
        stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <!-- Punta -->
  <path d="M64 28 L72 30 L70 38 Z" fill="#0A2A5E"/>
</svg>
```

### Logo navy — `logo-ascenso-publico-navy.svg`

Igual que el anterior pero invertido: `rect fill="#0A2A5E"`, `path stroke="#E8A33D"`, `path fill="#E8A33D"`.

### Logo TikTok — `logo-ascenso-publico-tiktok.svg`

Versión más vibrante con colores de redes:
- Fondo: `#0A2A5E`
- Flecha: `#FFD93D` (amarillo vibrante)
- Estela: `#5AE5C1` (menta)

### Favicon — `favicon.svg`

Versión simplificada del logo principal a 32×32.

---

## 17. Checklist de validación de una guía nueva

Antes de dar por terminada una guía, validar:

- [ ] El `<title>` empieza con `{CODIGO} · ...`
- [ ] El `<link rel="icon">` apunta a `brand/favicon.svg`
- [ ] Las dos fuentes (Plus Jakarta Sans + Source Serif 4) están en el `<link>` de Google Fonts
- [ ] El bloque `:root` tiene los 4 grupos de variables (azul, oro, crema, semánticos)
- [ ] El header tiene: `.doc-ref`, `.brand` (logo + name + slogan), `.kicker`, `<h1>`, `.header-sub`
- [ ] Si NO es INTRO: tiene 3 badges (día / tiempo / examen)
- [ ] El `<nav>` tiene 11 botones (uno por sección)
- [ ] Cada `.section` tiene `.eyebrow`, `<h2 class="sec-title">` y contenido
- [ ] El Desarrollo usa `.concepto` con las 4 capas (def/apl/eje/cnsc)
- [ ] Los conceptos con sub-componentes usan sub-bloques desplegables
- [ ] Casos = 5 · Errores = 6 · Tips = 6 · Trampas = 4
- [ ] Flashcards = 10 (array `flashcards`)
- [ ] Simulacro = 12 preguntas, 4 opciones cada una, distribución 4-5-3
- [ ] Cada pregunta tiene `tema`, `expl[4]`, `correcta`
- [ ] Las respuestas correctas no siguen un patrón visible
- [ ] El JS al final genera los botones "Avanzar" automáticamente
- [ ] El footer tiene `{CODIGO} · Día {N}` y el slogan
- [ ] El archivo abre en navegador sin errores en consola
- [ ] Etiquetas HTML balanceadas (validar con `grep -c "<div"` y `grep -c "</div>"`)

---

*Fin del estándar técnico. Para usar como checklist al construir nuevas guías ver `PLANTILLA-GUIA.md`.*
