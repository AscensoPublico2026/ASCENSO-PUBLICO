#!/usr/bin/env python3
"""BIBLIOTECA BASE PGN — extraer bases neutras y crear cursos nuevos a partir de ellas.

Una BASE es la mejor versión de un tema para un nivel, SIN identidad de ningún cliente.
La identidad queda como marcadores que el generador llena:
    {{COD}}    código del empleo           (ej. 3PU-17)
    {{CARGO}}  denominación del empleo     (ej. Profesional Universitario)
    {{CONV}}   número de convocatoria      (ej. 146-2026)
    {{GUIA}}   código de la guía nueva     (ej. FUN-OT-3PU12P-01)
    {{DIA}}    día del plan (1–21)

Comandos:
  python3 scripts/pgn_bases.py extraer <codigo_guia_fuente> <plan_fuente> <TEMA> <Nivel> [--enfoque "..."]
      → bases/pgn/<Nivel>/<TEMA>.html  y registro en bases/pgn/bases.json
  python3 scripts/pgn_bases.py curso <spec.json>
      → crea las guías del curso, las registra en las 2 biblioteca.json, agrega el plan
        en plataforma/lib/autocargarGuias.ts, agrega la identidad anti-fugas y corre el auditor.
  python3 scripts/pgn_bases.py listar [Nivel]

spec.json (ver referencias/pgn/EJEMPLO-SPEC.json):
  {"plan_id": "pgn-profesional-3pu12-pedro", "plan_nombre": "PGN · Profesional Universitario (3PU-12) ... (21 días)",
   "sufijo": "3PU12P", "cargo": "Profesional Universitario", "cod": "3PU-12", "conv": "300-2026",
   "nivel": "Profesional", "cliente": "Pedro Pérez Gómez", "nombres_cliente": ["Pedro", "Pérez Gómez"],
   "curso_biblioteca": "PGN Profesional Universitario 3PU-12 (Pedro Pérez Gómez · Conv. 300-2026)",
   "reemplazos": [["Procuradurías de Instrucción", "Procuradurías Provinciales"], ...],   # ajustes de dependencia/rol
   "temario": [["INTRO-00", 1], ["ENT-01", 1], ["GEN-01", 2], ... , ["SIM-001", 21]]}
"""
import re, json, os, sys, glob, shutil, subprocess, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BASES = 'bases/pgn'
REG = f'{BASES}/bases.json'
ID = json.load(open('referencias/pgn/identidades.json', encoding='utf-8'))
DIA_PAT = r'Día\s(\d{1,2})(?=\s?(?:de 21|·|:|<|"|\'|\)|\.|,|$| ))'


def reg_cargar():
    return json.load(open(REG, encoding='utf-8')) if os.path.exists(REG) else {}


def reg_guardar(r):
    os.makedirs(BASES, exist_ok=True)
    json.dump(r, open(REG, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def bib():
    return {e['codigo']: e for e in json.load(open('biblioteca/biblioteca.json', encoding='utf-8'))['guias']}


def dia_en_plan(codigo, plan):
    ts = open('plataforma/lib/autocargarGuias.ts', encoding='utf-8').read()
    m = re.search(r'id:\s*"' + re.escape(plan) + r'".*?\n  \},', ts, re.S)
    d = re.findall(r'codigo:\s*"' + re.escape(codigo) + r'",\s*dia:\s*(\d+)', m.group(0))
    return int(d[0]) if d else None


# ------------------------------------------------------------------ extraer
def extraer(codigo, plan, tema, nivel, enfoque=''):
    B = bib(); e = B[codigo]; src = e['archivo']; s = open(src, encoding='utf-8').read()
    idc = ID['cursos'][plan]; dia = dia_en_plan(codigo, plan)
    # 1) código de guía
    s = s.replace(codigo, '{{GUIA}}')
    # 2) identidad del curso fuente
    s = re.sub(re.escape(idc['cargo']) + r'\s+' + re.escape(idc['codigo']), '{{CARGO}} {{COD}}', s)
    s = s.replace(idc['codigo'], '{{COD}}')
    s = re.sub(re.escape(idc['codigo'].replace('-', '')) + r'(?=\b)', '{{COD}}', s)
    for c in idc['conv']:
        s = s.replace(c, '{{CONV}}')
    # 3) día propio
    if dia:
        s = re.sub(r'Día\s' + str(dia) + r'(?=\s?(?:de 21|·|:|<|"|\'|\)|\.|,|\s|$))', 'Día {{DIA}}', s)
    # 4) verificación: no puede quedar identidad de NINGÚN cliente
    resto = []
    plano = re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', s)))
    for k, c in ID['cursos'].items():
        for p in [c['codigo']] + c['conv'] + c['nombres']:
            if re.search(r'(?<![\w-])' + re.escape(p) + r'(?![\w])', plano):
                resto.append(p)
    dst = f'{BASES}/{nivel}/{tema}.html'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, 'w', encoding='utf-8').write(s)
    r = reg_cargar()
    tit = re.sub(re.escape(idc['cargo']) + r'\s+' + re.escape(idc['codigo']), '{{CARGO}} {{COD}}', e.get('titulo', '')).replace(idc['codigo'], '{{COD}}')
    r.setdefault(nivel, {})[tema] = {'archivo': dst, 'fuente': codigo, 'plan_fuente': plan, 'titulo': tit,
                                    'biblioteca': e.get('biblioteca'), 'tipo': e.get('tipo'), 'temas': e.get('temas', []),
                                    'simulacro': e.get('simulacro', False), 'enfoque': enfoque}
    # nombre de archivo: parte descriptiva después del código
    base_name = os.path.basename(src)
    m = re.match(re.escape(codigo) + r'-?(.*)\.html$', base_name)
    r[nivel][tema]['slug'] = (m.group(1) if m else re.sub(r'\.html$', '', base_name.split('-', 3)[-1]))
    reg_guardar(r)
    return dst, sorted(set(resto))


# ------------------------------------------------------------------ curso
def codigo_nuevo(tema, sufijo):
    """GEN-01 → GEN-01-PGN-<suf>; FUN-OT-01 → FUN-OT-<suf>-01; COM-01 → <suf>-COM-01; INTRO-00 → INTRO-00-PGN-<suf>;
    ENT-01 → ENT-PGN-<suf>-01; SIM-001 → SIM-PGN-<suf>-001"""
    if tema.startswith(('GEN-', 'INTRO-')):
        return f'{tema}-PGN-{sufijo}'
    if tema.startswith('COM-'):
        return f'{sufijo}-{tema}'
    if tema.startswith('ENT-'):
        return f'ENT-PGN-{sufijo}-01'
    if tema.startswith('SIM-'):
        return f'SIM-PGN-{sufijo}-001'
    m = re.match(r'(FUN-[A-Z]+)-(\d+)$', tema)
    if m:
        return f'{m.group(1)}-{sufijo}-{m.group(2)}'
    return f'{tema}-{sufijo}'


def instanciar(texto, spec, dia, guia):
    t = texto.replace('{{GUIA}}', guia).replace('{{COD}}', spec['cod']).replace('{{CARGO}}', spec['cargo'])
    t = t.replace('{{CONV}}', spec['conv']).replace('{{DIA}}', str(dia))
    for a, b in spec.get('reemplazos', []):
        t = t.replace(a, b)
    return t


def curso(spec_path):
    spec = json.load(open(spec_path, encoding='utf-8'))
    R = reg_cargar(); niv = R.get(spec['nivel'], {})
    creadas, faltan = [], []
    for item in spec['temario']:
        tema, dia = item[0], int(item[1])
        b = niv.get(tema)
        if not b:
            faltan.append((tema, dia)); continue
        guia = codigo_nuevo(tema, spec['sufijo'])
        carpeta = 'simulacro' if tema.startswith('SIM-') else 'guias'
        dst = f"{carpeta}/{guia}-{b['slug']}.html" if not tema.startswith('SIM-') else f'simulacro/{guia}.html'
        if os.path.exists(dst):
            print('YA EXISTE, no se sobrescribe:', dst); creadas.append((guia, dia, dst, b)); continue
        t = instanciar(open(b['archivo'], encoding='utf-8').read(), spec, dia, guia)
        if '{{' in t:
            print('MARCADOR SIN LLENAR en', dst, set(re.findall(r'\{\{[A-Z]+\}\}', t)))
        open(dst, 'w', encoding='utf-8').write(t)
        creadas.append((guia, dia, dst, b))
    # identidad anti-fugas
    d = json.load(open('referencias/pgn/identidades.json', encoding='utf-8'))
    d['cursos'][spec['plan_id']] = {'codigo': spec['cod'], 'conv': [spec['conv']], 'nombres': spec.get('nombres_cliente', []), 'cargo': spec['cargo']}
    for n in spec.get('nombres_cliente', [])[:1]:
        if n not in d['nombres_otros_clientes']:
            d['nombres_otros_clientes'].append(n)
    json.dump(d, open('referencias/pgn/identidades.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    # biblioteca (dos archivos)
    for fp in ('biblioteca/biblioteca.json', 'plataforma/lib/biblioteca.json'):
        dd = json.load(open(fp, encoding='utf-8')); L = dd['guias']; cods = {e['codigo'] for e in L}
        for guia, dia, dst, b in creadas:
            if guia in cods: continue
            L.append({'codigo': guia, 'dia': dia, 'titulo': instanciar(b['titulo'], spec, dia, guia),
                      'biblioteca': b.get('biblioteca') or 'Funcional', 'nivel': spec['nivel'], 'tipo': b.get('tipo') or 'funcional',
                      'estado': 'publicada', 'archivo': dst, 'reutilizable': False, 'simulacro': bool(b.get('simulacro')),
                      'temas': b.get('temas', []), 'curso': spec['curso_biblioteca']})
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(dd, f, ensure_ascii=False, indent=2); f.write('\n')
    # plan
    ts_path = 'plataforma/lib/autocargarGuias.ts'; ts = open(ts_path, encoding='utf-8').read()
    if f'id: "{spec["plan_id"]}"' not in ts and not faltan:
        filas = []
        orden = {}
        for guia, dia, dst, b in creadas:
            o = orden.get(dia, 0); orden[dia] = o + 1
            filas.append(f'      {{ codigo: "{guia}", dia: {dia}' + (f', orden: {o}' if o else '') + ' },')
        bloque = ('  "' + spec['plan_id'] + '": {\n    id: "' + spec['plan_id'] + '",\n    nombre: "' + spec['plan_nombre'] + '",\n    guias: [\n'
                  + '\n'.join(filas) + '\n    ],\n  },\n')
        i = ts.rfind('\n    id: "pgn-')
        j = ts.index('\n  },\n', i) + len('\n  },\n')
        ts = ts[:j] + bloque + ts[j:]
        open(ts_path, 'w', encoding='utf-8').write(ts)
        print('Plan agregado:', spec['plan_id'])
    elif faltan:
        print('Plan NO agregado todavía (faltan guías por crear).')
    print(f'Guías creadas desde bases: {len(creadas)}')
    if faltan:
        print('FALTAN (no hay base en este nivel; crear de cero o extraer una base):')
        for t, dd_ in faltan: print(f'   Día {dd_}: {t}')
    print('\nSIGUIENTE: revisar INTRO y SIM (cronograma de días), aplicar ajustes de rol y correr:')
    print(f'   python3 scripts/auditar-pgn.py --plan {spec["plan_id"]}')


def listar(nivel=None):
    R = reg_cargar()
    for n, T in sorted(R.items()):
        if nivel and n != nivel: continue
        print(f'== {n} ({len(T)} bases)')
        for t, b in sorted(T.items()):
            print(f'   {t:14s} {b["titulo"][:70]}  ← {b["fuente"]}')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    if a[0] == 'extraer':
        enf = a[a.index('--enfoque') + 1] if '--enfoque' in a else ''
        dst, resto = extraer(a[1], a[2], a[3], a[4], enf)
        print('Base:', dst, '| identidad restante:', resto or 'ninguna')
    elif a[0] == 'curso':
        curso(a[1])
    elif a[0] == 'listar':
        listar(a[1] if len(a) > 1 else None)
