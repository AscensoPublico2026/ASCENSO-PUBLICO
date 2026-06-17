#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de simulacros Ascenso Público — ensambla un simulacro HTML a partir de:
  - El molde fijo (motor/base-simulacro.html)  -> el diseño/flujo, NUNCA cambia
  - Un archivo de contenido (contenido/<CODIGO>.json) -> lo único que cambia

Uso:
    python3 motor/construir_simulacro.py contenido/SIM-001.json

Resultado: escribe simulacro/<archivo>.html listo para abrir en el navegador.

El molde implementa el "modo examen real": el aspirante responde todas las
preguntas sin ver aciertos, presenta el examen y recibe puntaje, % de aciertos,
revisión pregunta por pregunta y guía de refuerzo que remite a la guía del curso.
"""
import json
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(BASE_DIR)
BANCOS_DIR = os.path.join(SIM_DIR, 'bancos')

NIVELES = {'basic', 'intermediate', 'advanced'}


def ensamblar_preguntas(d):
    """Arma la lista de preguntas del simulacro.

    Soporta dos formatos de contenido:
      - Receta por bancos: 'bancos' (lista de nombres en bancos/<n>.json) +
        'funcionales' (preguntas propias del cargo). Las preguntas reutilizables
        se ensamblan desde los bancos; solo las funcionales se escriben por cargo.
      - Directo: 'preguntas' (lista completa). Retrocompatible.
    """
    if 'bancos' in d:
        preguntas = []
        fuentes = []
        for nombre in d.get('bancos', []):
            ruta = os.path.join(BANCOS_DIR, nombre + '.json')
            if not os.path.exists(ruta):
                raise SystemExit('No existe el banco: bancos/%s.json' % nombre)
            with open(ruta, encoding='utf-8') as fh:
                banco = json.load(fh)
            preguntas.extend(banco.get('preguntas', []))
            fuentes.append('%s(%d)' % (nombre, len(banco.get('preguntas', []))))
        funcionales = d.get('funcionales', [])
        preguntas.extend(funcionales)
        fuentes.append('funcionales-cargo(%d)' % len(funcionales))
        print('  Ensamblado desde bancos: %s' % ' + '.join(fuentes))
        return preguntas
    return d.get('preguntas', [])


def validar(d, preguntas):
    """Valida el contenido del simulacro. Devuelve (errores, avisos)."""
    err, warn = [], []
    req = ['codigo', 'archivo', 'kicker', 'titulo', 'hero_sub',
           'cargo', 'nivel', 'tiempo']
    for k in req:
        if k not in d:
            err.append('Falta el campo obligatorio: %s' % k)

    n = len(preguntas)
    if n == 0:
        err.append('El simulacro no tiene preguntas')
    elif n < 10:
        warn.append('El simulacro tiene solo %d preguntas (un simulacro final tipo CNSC suele tener 50+).' % n)

    refs = set()
    for i, p in enumerate(preguntas, 1):
        if p.get('nivel') not in NIVELES:
            err.append('Pregunta %d: nivel inválido (usa basic/intermediate/advanced)' % i)
        ops = p.get('ops', [])
        expl = p.get('expl', [])
        if len(ops) != 4:
            err.append('Pregunta %d: tiene %d opciones (deben ser 4)' % (i, len(ops)))
        if len(expl) != 4:
            err.append('Pregunta %d: tiene %d explicaciones (deben ser 4, una por opción)' % (i, len(expl)))
        c = p.get('correcta')
        if not isinstance(c, int) or not (0 <= c <= 3):
            err.append('Pregunta %d: "correcta" inválida (debe ser 0-3)' % i)
        if ops and len(set(ops)) != len(ops):
            err.append('Pregunta %d: tiene opciones repetidas' % i)
        ctx = p.get('ctx', '')
        if not ctx:
            err.append('Pregunta %d: sin contexto (ctx)' % i)
        elif len(ctx) < 150:
            warn.append('Pregunta %d: contexto corto (%d caracteres). Tipo CNSC pide un caso largo y verosímil (ideal >= 200).' % (i, len(ctx)))
        q = p.get('q', '')
        if not q:
            err.append('Pregunta %d: sin enunciado/dilema (q)' % i)
        elif len(q) < 80:
            warn.append('Pregunta %d: dilema corto (%d caracteres). Debe replantear la tensión e incitar la decisión (ideal >= 110).' % (i, len(q)))
        if not p.get('tema'):
            warn.append('Pregunta %d: sin "tema" (se usa en la guía de refuerzo)' % i)
        if not p.get('ref'):
            warn.append('Pregunta %d: sin "ref" (código de guía donde reforzar)' % i)
        else:
            refs.add(p['ref'])

    # Patrón obvio: que no todas las correctas sean iguales
    corr = [p.get('correcta') for p in preguntas]
    if preguntas and len(set(corr)) == 1:
        err.append('Todas las respuestas correctas son iguales (patrón obvio)')

    return err, warn


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

    with open(os.path.join(BASE_DIR, 'base-simulacro.html'), encoding='utf-8') as fh:
        base = fh.read()

    total = len(preguntas)
    nb = sum(1 for p in preguntas if p['nivel'] == 'basic')
    ni = sum(1 for p in preguntas if p['nivel'] == 'intermediate')
    na = sum(1 for p in preguntas if p['nivel'] == 'advanced')

    badges = (
        '<span class="badge">📝 %d preguntas</span>'
        '<span class="badge">⏱ %s</span>'
        '<span class="badge">🎓 %s</span>'
        '<span class="badge">🔁 Opciones barajadas</span>'
    ) % (total, d['tiempo'], d['nivel'])

    footer = '%s · %s · %d preguntas · Material independiente, no afiliado a la CNSC' % (
        d['codigo'], d['cargo'], total)

    title = '%s · Simulacro Final CNSC — Ascenso Público' % d['codigo']

    repl = {
        '{{TITLE}}': title,
        '{{KICKER}}': d['kicker'],
        '{{H1}}': d['titulo'],
        '{{HERO_SUB}}': d['hero_sub'],
        '{{BADGES}}': badges,
        '{{TOTAL}}': str(total),
        '{{FOOTER_META}}': footer,
        '{{PREGUNTAS}}': json.dumps(preguntas, ensure_ascii=False),
    }
    html = base
    for k, v in repl.items():
        html = html.replace(k, v)

    out_path = os.path.join(SIM_DIR, d['archivo'])
    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print('OK -> simulacro/%s (%d KB) · %d preguntas (%d basicas, %d intermedias, %d avanzadas)' % (
        d['archivo'], len(html.encode('utf-8')) // 1024, total, nb, ni, na))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python3 motor/construir_simulacro.py contenido/<CODIGO>.json')
        sys.exit(1)
    construir(sys.argv[1])
