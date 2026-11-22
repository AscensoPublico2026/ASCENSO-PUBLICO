# -*- coding: utf-8 -*-
"""Utilidades para los archivos de contenido de las guías PGN.

secciones(path)  -> {0: html, 1: html, …} con el interior de cada <section data-sec="n">.
aplicar(html, R) -> aplica una lista de reemplazos [(viejo, nuevo), …] y avisa si alguno no estaba.
falta(html, R)   -> lista los reemplazos que no se encontraron (para depurar sin escribir).
"""
import re, sys


def secciones(path):
    s = open(path, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'<section class="section[^"]*" data-sec="(\d+)">(.*?)\n</section>', s, re.S):
        out[int(m.group(1))] = m.group(2).strip('\n')
    return out


def falta(texto, R):
    return [a for a, _ in R if a not in texto]


def aplicar(texto, R, estricto=True, etiqueta=''):
    f = falta(texto, R)
    if f:
        print(f'⚠️  {etiqueta}: {len(f)} reemplazo(s) sin coincidencia:', file=sys.stderr)
        for x in f:
            print('    -', x[:110].replace('\n', ' '), file=sys.stderr)
        if estricto:
            raise SystemExit(1)
    for a, b in R:
        texto = texto.replace(a, b)
    return texto


def aplicar_todas(SEC, R, estricto=False):
    """Aplica los reemplazos sobre todas las secciones; exige que cada uno aparezca al menos una vez."""
    usados = {a: False for a, _ in R}
    for n in SEC:
        for a, b in R:
            if a in SEC[n]:
                usados[a] = True
                SEC[n] = SEC[n].replace(a, b)
    sin = [a for a, u in usados.items() if not u]
    if sin:
        print(f'⚠️  {len(sin)} reemplazo(s) sin coincidencia en ninguna sección:', file=sys.stderr)
        for x in sin:
            print('    -', x[:110].replace('\n', ' '), file=sys.stderr)
        if estricto:
            raise SystemExit(1)
    return SEC


def secciones_mapeadas(path, mapa=None):
    """Devuelve las secciones renumeradas al molde de 10 secciones (0-8 de contenido).
    Por defecto convierte el molde de 11 secciones (8 = flashcards, 9 = resumen, 10 = simulacro)."""
    S = secciones(path)
    if mapa is None:
        mapa = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 9: 8} if 10 in S else {n: n for n in range(9)}
    return {dst: S[src] for src, dst in mapa.items() if src in S}
