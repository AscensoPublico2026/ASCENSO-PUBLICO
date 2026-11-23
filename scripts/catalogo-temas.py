#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Catálogo de la biblioteca: qué guía existe, de qué cargo viene y si cumple el estándar.

Uso:  python3 scripts/catalogo-temas.py [--buscar "policia judicial"] [--md referencias/CATALOGO-TEMAS.md]

Sirve para responder, ANTES de escribir nada, la pregunta que ahorra más trabajo al armar
un curso nuevo: «¿qué ya existe en la biblioteca que me sirva de base?».
"""
import re, sys, glob, os, json, argparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def txt(s):
    s = re.sub(r'<(script|style)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))


def seccion_dev(s):
    m = re.search(r'<section class="section[^"]*" data-sec="2">(.*?)\n</section>', s, re.S)
    return m.group(1) if m else ''


def analizar(path):
    s = open(path, encoding='utf-8').read()
    dev = seccion_dev(s)
    tit = re.search(r'<title>(.*?)</title>', s, re.S)
    cargo = re.search(r'class="fmeta"[^>]*>(.*?)<', s, re.S)
    mods = [re.sub('<[^>]+>', '', m.group(1)).strip() for m in re.finditer(r'<h3>(.*?)</h3>', dev)]
    return dict(
        archivo=os.path.relpath(path, RAIZ),
        titulo=txt(tit.group(1)).strip() if tit else '',
        cargo=txt(cargo.group(1)).strip() if cargo else '',
        palabras=len(txt(dev).split()),
        modulos=len(mods),
        temas=mods,
        preguntas=s.count('class="pregunta"'),
        checkpoint=s.count('class="checkpoint"'),
        practica=dev.count('class="practica"') + dev.count('class="caso"'),
        ojo=dev.count('class="ojo"'),
        fuentes=int('class="fuentes"' in s),
        idea=int('Idea clave' in s),
    )


def estandar(g):
    """¿Cumple el estándar actual (§3 de PROCESO-CURSOS-GUIAS.md)?"""
    return (g['palabras'] >= 10000 and g['preguntas'] >= 15 and g['checkpoint'] >= 3
            and g['practica'] >= 3 and g['ojo'] >= 2 and g['fuentes'] and g['idea'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--buscar', help='palabras clave en el título o en los módulos')
    ap.add_argument('--md', help='escribe el catálogo completo en este archivo markdown')
    ap.add_argument('--top', type=int, default=12)
    a = ap.parse_args()

    guias = [analizar(p) for p in sorted(glob.glob(os.path.join(RAIZ, 'guias', '*.html')))]

    if a.buscar:
        claves = [k.lower() for k in a.buscar.split()]
        def puntaje(g):
            blob = (g['titulo'] + ' ' + ' '.join(g['temas'])).lower()
            return sum(blob.count(k) for k in claves)
        hits = sorted(((puntaje(g), g) for g in guias), key=lambda x: -x[0])
        hits = [(p, g) for p, g in hits if p > 0][:a.top]
        if not hits:
            print('sin coincidencias'); return
        for p, g in hits:
            ok = '✅' if estandar(g) else '⚠️ '
            print(f"{ok} {p:3d}  {g['archivo']}")
            print(f"       {g['palabras']} palabras · {g['modulos']} módulos · {g['preguntas']} preguntas "
                  f"· cp{g['checkpoint']} pr{g['practica']} ojo{g['ojo']}")
            print(f"       {g['cargo'][:95]}")
            print(f"       temas: {'; '.join(t[:46] for t in g['temas'][:6])}")
        return

    if a.md:
        out = ['# Catálogo de temas de la biblioteca', '',
               'Generado por `scripts/catalogo-temas.py`. **Antes de escribir una guía nueva, búscala aquí.**', '',
               '✅ = cumple el estándar actual · ⚠️ = hay que completarla (palabras, preguntas o interactividad)', '',
               '| | Guía | Palabras | Mód. | Preg. | Temas principales |', '|---|---|---|---|---|---|']
            
        for g in sorted(guias, key=lambda g: g['archivo']):
            ok = '✅' if estandar(g) else '⚠️'
            temas = '; '.join(t[:40] for t in g['temas'][:4]) or '—'
            out.append(f"| {ok} | `{os.path.basename(g['archivo'])}` | {g['palabras']} | {g['modulos']} "
                       f"| {g['preguntas']} | {temas} |")
        open(os.path.join(RAIZ, a.md), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
        n_ok = sum(1 for g in guias if estandar(g))
        print(f"{a.md}: {len(guias)} guías · {n_ok} cumplen el estándar · {len(guias)-n_ok} por completar")
        return

    n_ok = sum(1 for g in guias if estandar(g))
    print(f"{len(guias)} guías · {n_ok} cumplen el estándar · {len(guias)-n_ok} por completar")
    print("usa --buscar \"<palabras>\" para encontrar una base, o --md <archivo> para el catálogo completo")


if __name__ == '__main__':
    main()
