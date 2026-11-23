#!/usr/bin/env python3
"""Catálogo de temas PGN: agrupa las guías de todos los planes PGN por TEMA y NIVEL,
puntúa cada versión con la auditoría (referencias/pgn/AUDITORIA.json) y elige la mejor
como candidata a BASE. Escribe referencias/pgn/CATALOGO.json y CATALOGO.md.
Uso: python3 scripts/auditar-pgn.py && python3 scripts/catalogo-pgn.py
"""
import json, re, collections, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ts = open('plataforma/lib/autocargarGuias.ts', encoding='utf-8').read()
planes = {m.group(1): re.findall(r'codigo:\s*"([^"]+)",\s*dia:\s*(\d+)', m.group(3))
          for m in re.finditer(r'id:\s*"(pgn-[^"]+)",\s*nombre:\s*"([^"]+)"(.*?)\n  \},', ts, re.S)}
NIVEL = {'pgn-auxiliar-administrativo': 'Asistencial', 'pgn-asesor-1as19': 'Asesor', 'pgn-asesor-1as19-nathaly': 'Asesor',
         'pgn-secretario-4sp13': 'Técnico', 'pgn-secretario-4sp12': 'Técnico', 'pgn-sustanciador-4su11': 'Técnico',
         'pgn-citador-6ci04': 'Técnico', 'pgn-tecnico-administrativo-4tm16': 'Técnico'}
nivel = lambda p: NIVEL.get(p, 'Profesional')
bib = {e['codigo']: e for e in json.load(open('biblioteca/biblioteca.json', encoding='utf-8'))['guias']}
aud = {r['archivo']: r for r in json.load(open('referencias/pgn/AUDITORIA.json', encoding='utf-8'))}
ID = r'(3PU1[57][A-Z]?|1AS19N?|4SP1[23]|4SU11|6CI04|4TM16|5AM10|AUX|PU15|PU|PRO|TEC)'
def tema(c):
    k = re.sub(r'^' + ID + '-', '', c); k = re.sub(r'^PGN-(PRO-|AUX-)?', '', k)
    k = re.sub(r'-' + ID + r'(?=-|$)', '', k); k = re.sub(r'-PGN(?=-|$)', '', k)
    return k
def puntaje(r):
    H = r['hallazgos']; s = 0
    s += 100 * sum(h['sev'] == 'CRITICO' for h in H) + 10 * sum(h['sev'] == 'ALTO' for h in H) + sum(h['sev'] == 'MEDIO' for h in H)
    return s
cat = collections.defaultdict(lambda: collections.defaultdict(dict))
for p, L in planes.items():
    for c, d in L:
        e = bib[c]; r = aud.get(e['archivo'], {'hallazgos': []})
        v = cat[tema(c)][nivel(p)].setdefault(c, {'archivo': e['archivo'], 'titulo': e.get('titulo', ''), 'planes': [], 'dias': [],
                                                   'puntaje': puntaje(r), 'palabras': r.get('palabras'), 'npreg': r.get('npreg'),
                                                   'criticos_altos': [h['msg'][:90] for h in r['hallazgos'] if h['sev'] != 'MEDIO']})
        v['planes'].append(p); v['dias'].append(int(d))
out = {}
for t in sorted(cat):
    out[t] = {}
    for n, vers in sorted(cat[t].items()):
        mejor = min(vers, key=lambda c: (vers[c]['puntaje'], -(vers[c]['npreg'] or 0)))
        out[t][n] = {'mejor': mejor, 'versiones': vers}
json.dump(out, open('referencias/pgn/CATALOGO.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
L = ['# Catálogo de guías PGN por tema y nivel', '',
     'Generado por `scripts/catalogo-pgn.py` a partir de la auditoría. "Mejor" = versión con menos hallazgos (candidata a BASE).', '',
     '| Tema | Nivel | Versiones | Mejor versión | Hallazgos crít./altos de la mejor |', '|---|---|---|---|---|']
for t, N in out.items():
    for n, x in N.items():
        b = x['versiones'][x['mejor']]
        L.append(f"| {t} — {b['titulo'][:60]} | {n} | {len(x['versiones'])} | `{x['mejor']}` | {len(b['criticos_altos'])} |")
open('referencias/pgn/CATALOGO.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(len(out), 'temas;', sum(len(v) for v in out.values()), 'tema×nivel')
