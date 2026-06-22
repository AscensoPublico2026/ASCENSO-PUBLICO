#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de los SIMULACROS GRATIS (lead magnet del landing).

Usa el MISMO motor/validación que los simulacros del curso, pero:
  - Molde: motor/base-simulacro-gratis.html (incluye la "puerta" de captura de correo).
  - Salida: plataforma/public/simulacro-gratis/<archivo>  (servido estático por Next).
  - Reemplaza también {{NIVEL}} (asistencial|tecnico|profesional) que usa el JS para
    saber qué nivel reportar al guardar el lead.

Uso:
    python3 motor/construir_gratis.py contenido/SIM-GRATIS-ASI.json
    python3 motor/construir_gratis.py           # construye los tres (ASI/TEC/PRO)
"""
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(BASE_DIR)
REPO_DIR = os.path.dirname(SIM_DIR)
OUT_DIR = os.path.join(REPO_DIR, 'plataforma', 'public', 'simulacro-gratis')

sys.path.insert(0, BASE_DIR)
from construir_simulacro import ensamblar_preguntas, validar  # noqa: E402

MOLDE = os.path.join(BASE_DIR, 'base-simulacro-gratis.html')

GRATIS = ['SIM-GRATIS-ASI.json', 'SIM-GRATIS-TEC.json', 'SIM-GRATIS-PRO.json']


def construir(json_path):
    with open(json_path, encoding='utf-8') as fh:
        d = json.load(fh)

    preguntas = ensamblar_preguntas(d)
    err, warn = validar(d, preguntas)
    for w in warn:
        print('  AVISO: %s' % w)
    if err:
        print('  ERRORES en %s:' % os.path.basename(json_path))
        for e in err:
            print('     - %s' % e)
        raise SystemExit('Corrige los errores antes de generar el simulacro.')

    nivel_id = d.get('nivel_id')
    if nivel_id not in ('asistencial', 'tecnico', 'profesional'):
        raise SystemExit('Falta "nivel_id" valido (asistencial|tecnico|profesional) en %s' % json_path)

    with open(MOLDE, encoding='utf-8') as fh:
        base = fh.read()

    total = len(preguntas)
    nb = sum(1 for p in preguntas if p['nivel'] == 'basic')
    ni = sum(1 for p in preguntas if p['nivel'] == 'intermediate')
    na = sum(1 for p in preguntas if p['nivel'] == 'advanced')

    badges = (
        '<span class="badge">🎁 Gratis</span>'
        '<span class="badge">📝 %d preguntas</span>'
        '<span class="badge">⏱ %s</span>'
        '<span class="badge">🎓 %s</span>'
        '<span class="badge">🔁 Opciones barajadas</span>'
    ) % (total, d['tiempo'], d['nivel'])

    footer = '%s · Simulacro gratis · %d preguntas · Material independiente, no afiliado a la CNSC' % (
        d['codigo'], total)

    title = '%s · Simulacro CNSC gratis — Ascenso Público' % d['nivel']

    repl = {
        '{{TITLE}}': title,
        '{{KICKER}}': d['kicker'],
        '{{H1}}': d['titulo'],
        '{{HERO_SUB}}': d['hero_sub'],
        '{{BADGES}}': badges,
        '{{TOTAL}}': str(total),
        '{{NIVEL}}': nivel_id,
        '{{FOOTER_META}}': footer,
        '{{PREGUNTAS}}': json.dumps(preguntas, ensure_ascii=False),
    }
    html = base
    for k, v in repl.items():
        html = html.replace(k, v)

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, d['archivo'])
    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print('OK -> plataforma/public/simulacro-gratis/%s (%d KB) · %d preguntas (%d basicas, %d intermedias, %d avanzadas)' % (
        d['archivo'], len(html.encode('utf-8')) // 1024, total, nb, ni, na))


if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        for a in args:
            construir(a if os.path.isabs(a) else os.path.join(SIM_DIR, a))
    else:
        for nombre in GRATIS:
            construir(os.path.join(SIM_DIR, 'contenido', nombre))
