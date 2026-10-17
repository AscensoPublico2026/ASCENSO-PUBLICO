#!/usr/bin/env python3
"""Ensambla una guía HTML a partir de un MOLDE (CSS, cabecera, nav y scripts)
y del CONTENIDO propio de la guía.

Uso:
  python3 scripts/armar-guia.py <carpeta-fuente>

La carpeta-fuente contiene:
  meta.json       {molde, codigo, archivo, titulo_doc, h1, sub, kicker, dia,
                   badges:[...], quiz_titulo, siguiente, version}
  contenido.html  secciones data-sec 0..9 completas (<section ...>...</section>)
  datos.json      {"flashcards":[{"f":..,"b":..}], "preguntas":[{nivel,tema,ctx,q,ops,correcta,expl}]}

Escribe guias/<archivo> (o simulacro/) y la copia en plataforma/public/seed-guias/.
"""
import json, re, sys, os, html

src = sys.argv[1]
meta = json.load(open(os.path.join(src, "meta.json"), encoding="utf-8"))
contenido = open(os.path.join(src, "contenido.html"), encoding="utf-8").read()
datos = json.load(open(os.path.join(src, "datos.json"), encoding="utf-8"))
molde = open(meta["molde"], encoding="utf-8").read()

e = html.escape
codigo, dia = meta["codigo"], meta["dia"]

# ---------- head ----------
head = molde[: molde.find("<header>")]
head = re.sub(r"<title>.*?</title>", f"<title>{e(codigo)} · {e(meta['titulo_doc'])} — Ascenso Público</title>", head, count=1, flags=re.S)

# ---------- header ----------
hdr = molde[molde.find("<header>") : molde.find("</header>") + len("</header>")]
hdr = re.sub(r'<span class="doc-ref">.*?</span>', f'<span class="doc-ref">{e(codigo)}</span>', hdr, count=1)
hdr = re.sub(r'<div class="kicker">.*?</div>', f'<div class="kicker">{e(meta["kicker"])}</div>', hdr, count=1)
hdr = re.sub(r"<h1>.*?</h1>", f"<h1>{e(meta['h1'])}</h1>", hdr, count=1, flags=re.S)
hdr = re.sub(r'<p class="header-sub">.*?</p>', f'<p class="header-sub">{e(meta["sub"])}</p>', hdr, count=1, flags=re.S)
badges = "".join(f'<span class="badge">{e(b)}</span>' for b in meta["badges"])
hdr = re.sub(r'<div class="badges">.*?</div>', f'<div class="badges">{badges}</div>', hdr, count=1, flags=re.S)

nav = molde[molde.find("<nav>") : molde.find("</nav>") + len("</nav>")]

# ---------- sección 10 (simulacro) ----------
pregs = datos["preguntas"]
cnt = {k: sum(1 for p in pregs if p["nivel"] == k) for k in "bia"}
def plural(n, s, p): return f"{n} {s if n == 1 else p}"
tags = (f'<span class="tag b">{plural(cnt["b"], "Básica", "Básicas")}</span>'
        f'<span class="tag i">{plural(cnt["i"], "Intermedia", "Intermedias")}</span>'
        f'<span class="tag a">{plural(cnt["a"], "Avanzada", "Avanzadas")}</span>')
sig = meta["siguiente"]
confirm = f"✅ Finalizar Día {dia} y marcar como completado?\\n\\nPróxima guía: {sig}."
sec10 = f'''<section class="section" data-sec="10">
  <span class="eyebrow">Sección 11 · Simulacro</span>
  <h2 class="sec-title">🎓 {e(meta["quiz_titulo"])}</h2>
  <div class="quiz-intro">
    <p>{len(pregs)} preguntas tipo prueba escrita: un caso, un enunciado y 3 opciones (A, B, C), de las cuales solo una es la actuación correcta. Responde todas y al final verás tu puntaje y los temas a reforzar.</p>
    <div class="dific-tags">{tags}</div>
  </div>
  <div id="quiz"></div>
  <div style="text-align:center;margin-top:24px;">
    <button class="btn gold" id="btnCalcular">📊 Ver mi resultado</button>
  </div>
  <div id="resultado">
    <p class="score-num" id="scoreNum"></p>
    <p id="scoreMsg" style="font-size:1.05rem;margin:12px 0;"></p>
    <div id="temasReforzar"></div>
    <button class="btn" id="btnReiniciar" style="margin-top:18px;">🔄 Reiniciar simulacro</button>
  </div>
  <div class="advance-bar">
    <span class="advance-hint">Has completado el Día {dia}. Siguiente: {e(sig)}.</span>
    <button class="advance-btn final" id="btnFinalizar" onclick="if(confirm('{e(confirm)}'))window.parent.postMessage({{type:'GUIA_COMPLETADA'}},'*');">✅ Finalizar Día {dia}</button>
  </div>
</section>
'''

# ---------- footer ----------
foot = molde[molde.find("<footer>") : molde.find("</footer>") + len("</footer>")]
foot = re.sub(r'<div class="f-meta">.*?</div>',
              f'<div class="f-meta">{e(codigo)} · Día {dia} · {meta.get("version", "v1.0")} · © 2026 Ascenso Público · Preparación por cargo para concursos CNSC · Todos los derechos reservados</div>',
              foot, count=1, flags=re.S)

# ---------- scripts ----------
scripts = molde[molde.find("</footer>") + len("</footer>") : molde.rfind("</body>")]
def js_arr(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1).replace("</", "<\\/")
fl = js_arr(datos["flashcards"])
pq = js_arr([{k: p[k] for k in ("nivel", "tema", "ctx", "q", "ops", "correcta", "expl")} for p in pregs])
scripts, n1 = re.subn(r"const flashcards\s*=\s*\[.*?\n\];", lambda m: "const flashcards=" + fl + ";", scripts, count=1, flags=re.S)
if n1 == 0:
    scripts, n1 = re.subn(r"const flashcards\s*=\s*\[.*?\];", lambda m: "const flashcards=" + fl + ";", scripts, count=1, flags=re.S)
i = scripts.find("const preguntas")
j = scripts.find("const quizDiv", i)
assert n1 == 1 and i > 0 and j > i, "no se encontraron los arreglos en el molde"
scripts = scripts[:i] + "const preguntas=" + pq + ";\n" + scripts[j:]

out = head + hdr + "\n\n" + nav + "\n\n<main>\n" + contenido.strip() + "\n" + sec10 + "\n</main>\n\n" + foot + "\n" + scripts + "</body>\n</html>\n"

carpeta = "simulacro" if meta.get("es_simulacro") else "guias"
dest = os.path.join(carpeta, meta["archivo"])
open(dest, "w", encoding="utf-8").write(out)
open(os.path.join("plataforma/public/seed-guias", meta["archivo"]), "w", encoding="utf-8").write(out)
print(dest, len(out), "bytes")
