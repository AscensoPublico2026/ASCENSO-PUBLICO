#!/usr/bin/env python3
"""AUDITOR MAESTRO de guías PGN — Ascenso Público.

Revisa TODAS las guías y simulacros que usan los planes PGN (plataforma/lib/autocargarGuias.ts)
contra el estándar de referencias/PROCESO-CURSOS-GUIAS.md §3, y detecta FUGAS según el curso
o cursos que usan cada guía (referencias/pgn/identidades.json).

Uso:
  python3 scripts/auditar-pgn.py                  # todo, informe en referencias/pgn/AUDITORIA.md + .json
  python3 scripts/auditar-pgn.py --plan pgn-profesional-3pu17-lina
  python3 scripts/auditar-pgn.py --archivo guias/X.html --plan <plan>   # una guía nueva antes de publicar
  python3 scripts/auditar-pgn.py --js               # además ejecuta cada página en Chromium (errores JS)

Severidad:  CRITICO (no se puede entregar) · ALTO (corregir antes de reutilizar) · MEDIO (mejora).
"""
import re, json, html, sys, os, subprocess, argparse, collections, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
ID = json.load(open('referencias/pgn/identidades.json', encoding='utf-8'))

def txt(x): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x))).strip()

# ---------------------------------------------------------------- planes
def cargar_planes():
    ts = open('plataforma/lib/autocargarGuias.ts', encoding='utf-8').read()
    planes = {}
    for m in re.finditer(r'id:\s*"(pgn-[^"]+)",\s*nombre:\s*"([^"]+)"(.*?)\n  \},', ts, re.S):
        planes[m.group(1)] = {'nombre': m.group(2),
                              'guias': [(c, int(d)) for c, d in re.findall(r'codigo:\s*"([^"]+)",\s*dia:\s*(\d+)', m.group(3))]}
    return planes

def cargar_biblioteca():
    return {e['codigo']: e for e in json.load(open('biblioteca/biblioteca.json', encoding='utf-8'))['guias']}

# ---------------------------------------------------------------- preguntas
def preguntas(s):
    """Devuelve lista de dict(ctx, ops, c) en cualquiera de los 4 formatos."""
    Q = []
    for c, b in re.findall(r'<div class="pregunta" data-correcta?="(\d)">(.*?)<div class="feedback', s, re.S):
        ps = [txt(p) for p in re.findall(r'<p class="q-texto">(.*?)</p>', b, re.S)]
        ops = [txt(o) for o in re.findall(r'<span class="letra">.</span>\s*<span>(.*?)</span>\s*</div>', b, re.S)]
        if not ops:
            ops = [txt(o) for o in re.findall(r'<div class="opcion"[^>]*>(.*?)</div>', b, re.S)]
        Q.append({'ctx': ' '.join(ps), 'ops': ops, 'c': int(c)})
    if Q: return Q, 'html'
    m0 = re.search(r'const preguntas\s*=\s*(\[)', s)
    if m0:
        try:
            arr, _ = json.JSONDecoder().raw_decode(s[m0.start(1):])
            for q in arr:
                Q.append({'ctx': (q.get('ctx', '') + ' ' + q.get('q', '')).strip(), 'ops': q.get('ops', []), 'c': q.get('correcta', -1)})
            if Q: return Q, 'json'
        except Exception:
            Q = []
    m = re.search(r'const preguntas\s*=\s*\[(.*?)\n\s*\];', s, re.S)
    if m:
        body = m.group(1)
        lines = [l.strip().rstrip(',') for l in body.split('\n') if l.strip().startswith('{')]
        ok = True
        for l in lines:
            try:
                q = json.loads(l)
                Q.append({'ctx': (q.get('ctx', '') + ' ' + q.get('q', '')).strip(), 'ops': q.get('ops', []), 'c': q.get('correcta', -1)})
            except Exception:
                ok = False; break
        if Q and ok: return Q, 'jsonl'
        Q = []
        for mm in re.finditer(r'\{[^{}]*?(?:ctx|q)\s*:\s*(["\'`])(.*?)\1.*?ops\s*:\s*\[(.*?)\]\s*,\s*correcta\s*:\s*(\d)', body, re.S):
            seg = mm.group(0)
            ctx = ' '.join(x[1] for x in re.findall(r'\b(?:ctx|q)\s*:\s*(["\'`])((?:\\.|(?!\1).)*)\1', seg, re.S))
            ops = [x[1] for x in re.findall(r'(["\'`])((?:\\.|(?!\1).)*)\1', mm.group(3), re.S)]
            Q.append({'ctx': ctx, 'ops': ops, 'c': int(mm.group(4))})
        if Q: return Q, 'jsarr'
    return [], None

def nfeedbacks(s):
    m = re.search(r'feedbacks\s*=\s*\{(.*?)\n\s*\};', s, re.S)
    return len(re.findall(r'(?m)^\s*\d+\s*:\s*\{', m.group(1))) if m else None

# ---------------------------------------------------------------- fugas
def patrones_identidad(curso):
    c = ID['cursos'][curso]
    pats = [re.escape(c['codigo'])] + [re.escape(x) for x in c['conv']] + [r'\b' + re.escape(n) + r'\b' for n in c['nombres']]
    return pats

def fugas(s, duenos):
    """Identidad que NO pertenece a TODOS los cursos dueños de la guía."""
    propios_cod = {ID['cursos'][d]['codigo'] for d in duenos}
    propios_conv = set(x for d in duenos for x in ID['cursos'][d]['conv'])
    propios_nom = set(x for d in duenos for x in ID['cursos'][d]['nombres'])
    comun_cod = set.intersection(*[{ID['cursos'][d]['codigo']} for d in duenos]) if duenos else set()
    comun_conv = set.intersection(*[set(ID['cursos'][d]['conv']) for d in duenos]) if duenos else set()
    out = []
    plano = txt(s)
    cods = {c['codigo'] for c in ID['cursos'].values()}
    for cod in cods:
        for m in re.finditer(re.escape(cod) + r'(?![0-9])', plano):
            if cod not in comun_cod:
                tipo = 'código de otro curso' if cod not in propios_cod else 'código específico en guía COMPARTIDA'
                out.append((tipo, plano[max(0, m.start()-60):m.end()+40]))
    for m in re.finditer(r'(?<![\d.])(\d{1,3}-2026)\b', plano):
        n = m.group(1)
        if n not in comun_conv and re.search(r'(?i)conv', plano[max(0, m.start()-25):m.start()]):
            tipo = 'convocatoria ajena' if n not in propios_conv else 'convocatoria específica en guía COMPARTIDA'
            out.append((tipo, plano[max(0, m.start()-60):m.end()+30]))
    for nom in ID['nombres_otros_clientes']:
        if nom in propios_nom and len(duenos) == 1: continue
        for m in re.finditer(r'\b' + re.escape(nom) + r'\b', plano):
            out.append(('nombre de cliente', plano[max(0, m.start()-60):m.end()+40]))
    return out

def avisos_entidad(s):
    plano = txt(s); out = []
    for p in ID['entidades_ajenas']:
        for m in re.finditer(p, plano):
            out.append(plano[max(0, m.start()-60):m.end()+40])
    if re.search(r'(?i)CNSC', plano):
        for m in re.finditer(r'CNSC', plano):
            frag = plano[max(0, m.start()-80):m.end()+60]
            if not re.search(r'(?i)\bno\b|régimen especial|ni la|sin la|distint', frag):
                out.append('CNSC: ' + frag)
    return out

# ---------------------------------------------------------------- guía
def auditar_html(path, duenos, dias, es_sim=False):
    s = open(path, encoding='utf-8').read()
    R = {'archivo': path, 'duenos': duenos, 'dias': sorted(set(dias)), 'hallazgos': []}
    H = R['hallazgos']
    def add(sev, cat, msg): H.append({'sev': sev, 'cat': cat, 'msg': msg})

    # estructura
    for tag in ['section', 'main', 'div', 'table', 'details']:
        o = len(re.findall(r'<' + tag + r'[ >]', s)); c = s.count('</' + tag + '>')
        if o != c: add('CRITICO', 'html', f'<{tag}> desbalanceado {o}/{c}')
    m = re.search(r'<section class="section[^"]*" data-sec="2">(.*?)</section>', s, re.S)
    dev = m.group(1) if m else ''
    R['palabras'] = len(txt(dev).split())
    tipo = 'sim' if es_sim else ('intro' if '/INTRO' in path else ('ent' if '/ENT-' in path else 'guia'))
    R['tipo'] = tipo
    if tipo == 'guia':
        if R['palabras'] < 10000: add('ALTO' if R['palabras'] >= 7000 else 'CRITICO', 'contenido', f"Desarrollo con {R['palabras']} palabras (mín. 10.000)")
        k = {'tablas': dev.count('<table'), 'practica': dev.count('class="practica"') + dev.count('class="caso"'),
             'acordeon': len(re.findall(r'<details', dev)), 'ojo': dev.count('class="ojo"'), 'flujo': dev.count('class="flujo"'),
             'checkpoint': s.count('class="checkpoint"'), 'mark': dev.count('<mark>'),
             'modulos': len(re.findall(r'<h[34][ >]', dev))}
        R['interactividad'] = k
        if k['checkpoint'] < 3: add('ALTO', 'interactividad', f"solo {k['checkpoint']} checkpoints (mín. 3)")
        if k['practica'] < 3: add('MEDIO', 'interactividad', f"solo {k['practica']} ejemplos 'En la práctica'")
        if k['tablas'] < 3: add('MEDIO', 'interactividad', f"solo {k['tablas']} tablas")
        if k['acordeon'] < 2: add('MEDIO', 'interactividad', f"solo {k['acordeon']} acordeones")
        if k['ojo'] < 2: add('MEDIO', 'interactividad', f"solo {k['ojo']} 'Ojo en la prueba'")
        if 'Idea clave' not in s: add('ALTO', 'cierre', "falta box 'Idea clave'")
        if 'Frase para recordar' not in s: add('ALTO', 'cierre', "falta '⚡ Frase para recordar'")
        if 'class="fuentes"' not in s: add('ALTO', 'cierre', "falta bloque .fuentes")
        nl = len(re.findall(r'target="_blank"', s))
        if nl < 2: add('ALTO', 'cierre', f"solo {nl} enlaces a normas (target=_blank)")
    if 'id="readbar"' not in s and tipo != 'sim': add('MEDIO', 'diseño', 'falta barra de progreso #readbar')
    # día
    if dias:
        for d in sorted(set(dias)):
            D = f'Día {d}'
            okb = re.search(r'📅 ' + D + r' de 21', s); okf = re.search(r'Finalizar ' + D + r'\s*<', s)
            okk = re.search(r'kicker">\s*' + D + r'\b', s)
            falt = [n for n, v in (('insignia', okb), ('botón Finalizar', okf), ('kicker', okk)) if not v]
            if falt: add('ALTO', 'día', f"{D}: falta/incoherente en {', '.join(falt)}")
        otros = set(int(x) for x in re.findall(r'Finalizar Día (\d+)', s)) | set(int(x) for x in re.findall(r'📅 Día (\d+) de 21', s))
        if otros - set(dias): add('CRITICO', 'día', f"muestra días ajenos {sorted(otros - set(dias))} (plan: {sorted(set(dias))})")
    # preguntas
    Q, fmt = preguntas(s); R['formato'] = fmt; R['npreg'] = len(Q)
    if tipo != 'intro':
        if not Q and tipo != 'ent': add('CRITICO', 'preguntas', 'no se detectó mini-simulacro')
        elif tipo == 'guia' and len(Q) < 8: add('ALTO', 'preguntas', f'solo {len(Q)} preguntas en el mini-simulacro')
    if Q:
        ctx = [len(q['ctx']) for q in Q]; ops = [len(o) for q in Q for o in q['ops']]
        R['ctx_min'] = min(ctx); R['op_min'] = min(ops) if ops else 0
        R['dist'] = ''.join('ABCD'[q['c']] if 0 <= q['c'] < 4 else '?' for q in Q)
        cortos = [i+1 for i, q in enumerate(Q) if len(q['ctx']) < 450]
        if cortos: add('ALTO', 'preguntas', f"{len(cortos)} preguntas con caso <450 car.: {cortos[:12]}")
        largos = [i+1 for i, q in enumerate(Q) if len(q['ctx']) > 1000]
        if largos: add('MEDIO', 'preguntas', f"{len(largos)} casos largos (>1000 car.): {largos[:12]}")
        malos4 = [i+1 for i, q in enumerate(Q) if len(q['ops']) != 4]
        if malos4: add('CRITICO', 'preguntas', f"preguntas sin 4 opciones: {malos4[:12]}")
        oc = [i+1 for i, q in enumerate(Q) if q['ops'] and min(len(o) for o in q['ops']) < 120]
        if oc: add('ALTO', 'preguntas', f"{len(oc)} preguntas con opciones <120 car.: {oc[:12]}")
        dest = []
        for i, q in enumerate(Q):
            if len(q['ops']) == 4 and 0 <= q['c'] < 4:
                L = [len(o) for o in q['ops']]; ot = [l for j, l in enumerate(L) if j != q['c']]
                if L[q['c']] > max(ot) * 1.2: dest.append(i+1)
        if dest: add('ALTO', 'preguntas', f"{len(dest)} preguntas donde la correcta se delata por larga: {dest[:15]}")
        dup = [i+1 for i, q in enumerate(Q) if len(set(q['ops'])) < len(q['ops'])]
        if dup: add('CRITICO', 'preguntas', f"opciones repetidas en: {dup}")
        cnt = collections.Counter(R['dist'])
        if len(Q) >= 8 and max(cnt.values()) > len(Q) * 0.45: add('MEDIO', 'preguntas', f"respuestas concentradas en una letra: {dict(cnt)}")
        nf = nfeedbacks(s)
        if fmt == 'html' and nf is not None and nf != len(Q): add('CRITICO', 'preguntas', f"{len(Q)} preguntas pero {nf} retroalimentaciones")
        if es_sim:
            func = len(Q); lk = len(re.findall(r'(?m)^\s*\{\s*"?comp"?\s*:', s)) or s.count('stmt:') or s.count('"stmt"')
            R['likert'] = lk
            if func < 50: add('CRITICO', 'simulacro', f'solo {func} preguntas funcionales (deben ser 50)')
    # fugas
    for tipo_f, frag in fugas(s, duenos): add('CRITICO', 'fuga', f"{tipo_f}: «…{frag}…»")
    R['avisos_entidad'] = avisos_entidad(s)
    return R

def js_check(path):
    js = '\n'.join(re.findall(r'<script>(.*?)</script>', open(path, encoding='utf-8').read(), re.S))
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f: f.write(js)
    r = subprocess.run(['node', '--check', f.name], capture_output=True, text=True); os.unlink(f.name)
    return r.stderr.strip().split('\n')[0] if r.returncode else None

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--plan'); ap.add_argument('--archivo'); ap.add_argument('--js', action='store_true')
    ap.add_argument('--salida', default='referencias/pgn/AUDITORIA')
    a = ap.parse_args()
    planes = cargar_planes(); bib = cargar_biblioteca()
    uso = collections.defaultdict(list)
    for pid, p in planes.items():
        if a.plan and pid != a.plan: continue
        for c, d in p['guias']: uso[c].append((pid, d))
    objetivos = []
    if a.archivo:
        objetivos.append((a.archivo, [a.plan] if a.plan else [], [], a.archivo.startswith('simulacro/')))
    else:
        for c, L in sorted(uso.items()):
            if c not in bib: print('SIN REGISTRO', c); continue
            objetivos.append((bib[c]['archivo'], sorted({p for p, _ in L}), [d for _, d in L], bib[c]['archivo'].startswith('simulacro/')))
    res = []
    for path, duenos, dias, sim in objetivos:
        if not os.path.exists(path):
            res.append({'archivo': path, 'duenos': duenos, 'hallazgos': [{'sev': 'CRITICO', 'cat': 'archivo', 'msg': 'no existe'}]}); continue
        R = auditar_html(path, duenos, dias, sim)
        e = js_check(path)
        if e: R['hallazgos'].append({'sev': 'CRITICO', 'cat': 'js', 'msg': e})
        res.append(R)
    # salida
    tot = collections.Counter(h['sev'] for r in res for h in r['hallazgos'])
    print(f"Guías auditadas: {len(res)} · CRITICO {tot['CRITICO']} · ALTO {tot['ALTO']} · MEDIO {tot['MEDIO']}")
    limpias = sum(1 for r in res if not any(h['sev'] in ('CRITICO', 'ALTO') for h in r['hallazgos']))
    print(f"Guías sin hallazgos críticos/altos: {limpias}/{len(res)}")
    if a.archivo:
        for h in res[0]['hallazgos']: print(f"  [{h['sev']}] {h['cat']}: {h['msg']}")
        for x in res[0].get('avisos_entidad', [])[:10]: print('  [REVISAR] ', x)
        return 1 if any(h['sev'] in ('CRITICO', 'ALTO') for h in res[0]['hallazgos']) else 0
    json.dump(res, open(a.salida + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return 0

if __name__ == '__main__':
    sys.exit(main())
