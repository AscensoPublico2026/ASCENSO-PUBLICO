#!/usr/bin/env python3
"""Validador completo de guías DIAN (formato de 3 opciones).
Uso: python3 scripts/validar-guia-dian.py <archivo.html> "<regex de fugas>" [min_palabras_desarrollo]
Revisa: HTML balanceado, palabras del Desarrollo, JS (node --check), checkpoints,
flashcards, preguntas al estándar (3 ops/3 expl, ctx 550-1000, q 230-430,
ops 150-345, correcta variada) y fugas. Sale 1 si hay problemas.
"""
import re, html, sys, json, subprocess, tempfile, os

f = sys.argv[1]
fugas_rx = sys.argv[2] if len(sys.argv) > 2 else r"aduaner|importador|Gestor II|subpartida|arancel"
min_pal = int(sys.argv[3]) if len(sys.argv) > 3 else 10000
t = open(f, encoding="utf-8").read()
prob, ok = [], []

for tag in ["section", "main", "div", "table", "details", "ul", "ol"]:
    o = len(re.findall(r"<" + tag + r"[ >]", t)); c = t.count("</" + tag + ">")
    (ok if o == c else prob).append(f"<{tag}> {o}/{c}")

secs = re.findall(r'<section class="section[^"]*" data-sec="(\d+)"', t)
if secs != [str(i) for i in range(11)]: prob.append(f"secciones {secs}")

m = re.search(r'<section class="section" data-sec="2">(.*?)</section>', t, re.S)
pal = len(html.unescape(re.sub(r"<[^>]+>", " ", m.group(1) if m else "")).split())
(ok if pal >= min_pal else prob).append(f"Desarrollo {pal} palabras (mín {min_pal})")

with tempfile.TemporaryDirectory() as d:
    for i, js in enumerate(re.findall(r"<script>(.*?)</script>", t, re.S)):
        p = os.path.join(d, f"s{i}.js"); open(p, "w").write(js)
        r = subprocess.run(["node", "--check", p], capture_output=True, text=True)
        (ok if r.returncode == 0 else prob).append(f"script{i} node --check " + ("OK" if r.returncode == 0 else r.stderr[:300]))

cps = re.findall(r'class="checkpoint" id="cp(\d+)"', t)
fbs = re.findall(r'class="cp-fb" id="cpfb(\d+)"', t)
okcp = cps == [str(i) for i in range(1, len(cps) + 1)] and cps == fbs
for n in cps:
    blk = t[t.find(f'id="cp{n}"'): t.find(f'id="cpfb{n}"')]
    if blk.count('data-ans="1"') != 1 or len(re.findall(rf'data-cp="{n}"', blk)) != 3: okcp = False; prob.append(f"checkpoint {n} mal formado")
(ok if okcp and len(cps) >= 3 else prob).append(f"checkpoints {len(cps)}")

def arr(name):
    m = re.search(r"const " + name + r"\s*=\s*(\[.*?\]);\s*\n", t, re.S)
    if not m: return None
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
        tf.write("const x=" + m.group(1) + ";process.stdout.write(JSON.stringify(x));")
    r = subprocess.run(["node", tf.name], capture_output=True, text=True); os.unlink(tf.name)
    return json.loads(r.stdout) if r.returncode == 0 else None
fl = arr("flashcards"); pq = arr("preguntas")
(ok if fl and len(fl) >= 10 else prob).append(f"flashcards {len(fl) if fl else 0}")
if not pq: prob.append("sin preguntas")
else:
    ctx = [len(p["ctx"]) for p in pq]; q = [len(p["q"]) for p in pq]; ops = [len(o) for p in pq for o in p["ops"]]
    bad = [i + 1 for i, p in enumerate(pq) if len(p["ops"]) != 3 or len(p["expl"]) != 3 or p["correcta"] not in (0, 1, 2)]
    if bad: prob.append(f"preguntas sin 3 ops/expl: {bad}")
    if min(ctx) < 550 or max(ctx) > 1000: prob.append(f"ctx fuera de 550-1000: {[i+1 for i,c in enumerate(ctx) if c<550 or c>1000]} ({min(ctx)}-{max(ctx)})")
    if min(q) < 230 or max(q) > 430: prob.append(f"q fuera de 230-430: {[i+1 for i,c in enumerate(q) if c<230 or c>430]} ({min(q)}-{max(q)})")
    if min(ops) < 150 or max(ops) > 345: prob.append(f"ops fuera de 150-345 ({min(ops)}-{max(ops)}): " + str([(i+1,j) for i,p in enumerate(pq) for j,o in enumerate(p['ops']) if len(o)<150 or len(o)>345]))
    cs = [p["correcta"] for p in pq]
    if len(set(cs)) < 3: prob.append(f"correctas poco variadas {cs}")
    # la correcta no debe ser casi siempre la más larga
    larga = sum(1 for p in pq if max(range(3), key=lambda k: len(p["ops"][k])) == p["correcta"])
    if larga > len(pq) * 0.6: prob.append(f"la correcta es la más larga en {larga}/{len(pq)}")
    for i, p in enumerate(pq):
        if not p["expl"][p["correcta"]].lstrip().startswith(("Correcto", "✔")): prob.append(f"expl correcta P{i+1} no inicia con 'Correcto'")
    ok.append(f"{len(pq)} preguntas · ctx {min(ctx)}-{max(ctx)} · q {min(q)}-{max(q)} · ops {min(ops)}-{max(ops)} · correctas {cs} · niveles {''.join(p['nivel'] for p in pq)}")

texto = html.unescape(re.sub(r"<[^>]+>", " ", t))
fz = re.findall(fugas_rx, texto, re.I)
(ok if not fz else prob).append(f"fugas {len(fz)} {sorted(set(fz))[:8]}")

print("✔ " + "\n✔ ".join(ok))
if prob: print("✘ " + "\n✘ ".join(prob)); sys.exit(1)
print("RESULTADO: OK")
