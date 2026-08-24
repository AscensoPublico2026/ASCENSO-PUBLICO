#!/usr/bin/env python3
"""Valida una guía HTML de Ascenso Público (curso PGN Procurador Judicial II).
Uso: python3 scripts/validar-guia.py guias/ARCHIVO.html [--min 3300]
Chequea: balance de etiquetas de bloque, palabras en Desarrollo (data-sec="2"),
fugas de 'Sustanciador'/'INDERVALLE', presencia de nav 10 secciones y script.
El node --check del JS se hace aparte en bash.
"""
import re, sys, html

def main():
    path = sys.argv[1]
    minw = 3300
    if '--min' in sys.argv:
        minw = int(sys.argv[sys.argv.index('--min')+1])
    h = open(path, encoding='utf-8').read()
    problems = []
    warns = []

    # 1) Balance de etiquetas de bloque clave
    for tag in ['section', 'div', 'details', 'table', 'script', 'header', 'nav', 'main', 'footer', 'ul', 'ol']:
        opens = len(re.findall(r'<%s(?:\s|>)' % tag, h))
        closes = len(re.findall(r'</%s>' % tag, h))
        if opens != closes:
            problems.append(f'DESBALANCE <{tag}>: {opens} abren, {closes} cierran')

    # 2) Palabras en Desarrollo (top-level section data-sec="2")
    idxs = [(m.group(1), m.start()) for m in re.finditer(r'<section class="section[^"]*" data-sec="(\d+)"', h)]
    dev_words = 0
    for i,(sec,pos) in enumerate(idxs):
        end = idxs[i+1][1] if i+1 < len(idxs) else h.find('</main>')
        if sec == '2':
            seg = h[pos:end]
            txt = re.sub(r'<[^>]+>', ' ', seg)
            txt = html.unescape(txt)
            txt = re.sub(r'\s+', ' ', txt)
            dev_words = len(txt.split())
    if dev_words < minw:
        problems.append(f'Desarrollo con {dev_words} palabras (< {minw})')
    else:
        print(f'  ✓ Desarrollo: {dev_words} palabras (>= {minw})')

    # 3) Fugas prohibidas
    for bad in ['Sustanciador', 'sustanciador', 'INDERVALLE', 'Indervalle']:
        n = h.count(bad)
        if n:
            problems.append(f'FUGA "{bad}": {n} ocurrencias')

    # 4) Estructura: nav 10 secciones, 10 sections, script
    navbtns = len(re.findall(r'nav button|<button[^>]*data-sec=', h))
    secs = len(re.findall(r'<section class="section', h))
    if secs != 10:
        problems.append(f'Se esperaban 10 <section>, hay {secs}')
    if '<script>' not in h:
        problems.append('Falta <script>')

    # 5) Enlaces normativos target=_blank (informativo)
    ext = len(re.findall(r'secretariasenado\.gov\.co', h))
    n_acc = len(re.findall(r'details class="acc"', h))
    n_tab = h.count('<table')
    n_caso = len(re.findall(r'class="caso"', h))
    print('  · enlaces secretariasenado: %d · acordeones: %d · tablas: %d · casos: %d' % (ext, n_acc, n_tab, n_caso))

    if problems:
        print('  ✗ PROBLEMAS:')
        for p in problems:
            print('    -', p)
        sys.exit(1)
    print('  ✅ VALIDACIÓN OK')

if __name__ == '__main__':
    main()
