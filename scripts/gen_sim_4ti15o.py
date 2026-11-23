#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta el simulacro final del curso 4TI-15 sobre la plantilla de simulacro de la PGN.

Uso: python3 scripts/gen_sim_4ti15o.py
Lee  contenido/4TI15O/sim/preguntas.json y contenido/4TI15O/sim/likert.json
Escribe simulacro/SIM-PGN-4TI15O-001.html
"""
import json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLA = os.path.join(RAIZ, 'simulacro', 'SIM-PGN-4SP12-001.html')
SALIDA = os.path.join(RAIZ, 'simulacro', 'SIM-PGN-4TI15O-001.html')

META = dict(
    codigo='SIM-PGN-4TI15O-001',
    cargo='Técnico Investigador 4TI-15',
    conv='257-2026',
)


def sustituir_array(s, nombre, datos):
    i = s.find(f'const {nombre}=[')
    assert i >= 0, f'no se encontró const {nombre}'
    j = s.find('\n];', i)
    assert j > i, f'no se encontró el cierre de {nombre}'
    nuevo = f'const {nombre}=' + json.dumps(datos, ensure_ascii=False, indent=0).replace('\n', '\n')
    return s[:i] + nuevo + s[j + 3:]


def main():
    s = open(PLANTILLA, encoding='utf-8').read()
    pregs = json.load(open(os.path.join(RAIZ, 'contenido/4TI15O/sim/preguntas.json'), encoding='utf-8'))
    likert = json.load(open(os.path.join(RAIZ, 'contenido/4TI15O/sim/likert.json'), encoding='utf-8'))

    # validaciones antes de escribir nada
    assert len(pregs) == 50, f'se esperaban 50 preguntas funcionales, hay {len(pregs)}'
    assert len(likert) == 20, f'se esperaban 20 afirmaciones comportamentales, hay {len(likert)}'
    for n, p in enumerate(pregs, 1):
        assert set(p) >= {'nivel', 'tema', 'ctx', 'q', 'ops', 'correcta', 'expl', 'ref', 'refT'}, f'faltan campos en la {n}'
        assert len(p['ops']) == 4, f'la pregunta {n} no tiene 4 opciones'
        assert 0 <= p['correcta'] <= 3, f'la pregunta {n} tiene índice de correcta fuera de rango'
        assert p['nivel'] in ('basic', 'intermediate', 'advanced'), f'nivel inválido en la {n}'
        cs = len(p['ctx']) + len(p['q'])
        assert 450 <= cs <= 1100, f'la pregunta {n} tiene caso de {cs} caracteres (450-1.100)'
        L = [len(o) for o in p['ops']]
        assert min(L) >= 120, f'la pregunta {n} tiene una opción de {min(L)} caracteres'
        assert max(L) <= 300, f'la pregunta {n} tiene una opción de {max(L)} caracteres'
        otras = max(l for k, l in enumerate(L) if k != p['correcta'])
        assert L[p['correcta']] <= otras * 1.25, f'la pregunta {n}: la correcta se delata por longitud'
        assert len(set(p['ops'])) == 4, f'la pregunta {n} tiene opciones repetidas'

    s = sustituir_array(s, 'preguntas', pregs)
    s = sustituir_array(s, 'likertItems', likert)

    # identidad
    s = re.sub(r'<title>[^<]*</title>',
               f"<title>{META['codigo']} · Simulacro Integral Final — Ascenso Público</title>", s, count=1)
    s = re.sub(r'<h1>.*?</h1>',
               f"<h1>Procuraduría General de la Nación<br>{META['cargo']} · Convocatoria {META['conv']}</h1>",
               s, count=1, flags=re.S)
    s = s.replace('Secretario Procuraduría 4SP-12', META['cargo'])
    s = s.replace('4SP-12', '4TI-15').replace('4SP12', '4TI15O')
    s = s.replace('291-2026', META['conv'])
    s = s.replace('SIM-PGN-4TI15O-001-001', META['codigo'])

    assert 'Secretari' not in s, 'quedaron menciones del cargo de la plantilla'
    assert '4SP' not in s and '291-2026' not in s, 'quedaron identidades de la plantilla'

    open(SALIDA, 'w', encoding='utf-8').write(s)
    import collections
    niv = collections.Counter(p['nivel'] for p in pregs)
    print(f"{os.path.relpath(SALIDA, RAIZ)}  ·  {len(pregs)} funcionales + {len(likert)} comportamentales")
    print(f"  niveles: {dict(niv)}  ·  temas distintos: {len(set(p['tema'] for p in pregs))}")
    print(f"  letras correctas: {dict(collections.Counter('ABCD'[p['correcta']] for p in pregs))}")


if __name__ == '__main__':
    main()
