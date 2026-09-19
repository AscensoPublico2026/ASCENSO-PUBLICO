#!/usr/bin/env python3
"""Validador de guías Ascenso Público (uso interno del curso Viviana/PGN 242).
Uso: python3 scripts/validar-guia.py guias/ARCHIVO.html "Día N"
Verifica: HTML balanceado, conteo palabras Desarrollo, 4 opciones/pregunta,
día coherente, fugas de otro cargo/entidad. NO valida JS (usar node --check aparte).
Sale con código 0 si todo OK, 1 si hay problemas.
"""
import re, html, sys

def main():
    if len(sys.argv) < 2:
        print("Uso: validar-guia.py <archivo.html> [Dia N]"); return 2
    f = sys.argv[1]
    dia = sys.argv[2] if len(sys.argv) > 2 else None
    t = open(f, encoding='utf-8').read()
    problemas = []
    ok = []

    # 1. Balance de etiquetas
    for tag in ['section','main','div','table','details']:
        o = len(re.findall(r'<'+tag+r'[ >]', t)); c = t.count('</'+tag+'>')
        if o != c: problemas.append(f"MISMATCH <{tag}>: {o} abiertas / {c} cerradas")
        else: ok.append(f"{tag} {o}/{c}")

    # 2. Palabras del Desarrollo (section data-sec=2)
    m = re.search(r'<section class="section" data-sec="2">(.*?)</section>', t, re.S)
    seg = m.group(1) if m else ''
    des = len(html.unescape(re.sub(r'<[^>]+>',' ', seg)).split())
    if des < 10000: problemas.append(f"Desarrollo con {des} palabras (<10.000)")
    else: ok.append(f"Desarrollo {des} pal")

    # 3. Opciones por pregunta del simulacro (deben ser 4)
    for i, ops in enumerate(re.findall(r'ops:\[(.*?)\], correcta', t, re.S)):
        n = ops.count("','") + 1
        if n != 4: problemas.append(f"Pregunta {i+1} tiene {n} opciones (deben ser 4)")
    npreg = len(re.findall(r'ops:\[.*?\], correcta', t, re.S))
    ok.append(f"preguntas simulacro: {npreg}")

    # 4. Día coherente
    if dia:
        kick = re.search(r'kicker">'+re.escape(dia)+r' ', t)
        badge = re.search(r'badge">📅 '+re.escape(dia)+r' de 21', t)
        fin = re.search(r'Finalizar '+re.escape(dia)+r'<', t)
        if not kick: problemas.append(f"kicker no dice '{dia}'")
        if not badge: problemas.append(f"badge no dice '{dia} de 21'")
        if not fin: problemas.append(f"botón finalizar no dice '{dia}'")
        if kick and badge and fin: ok.append(f"{dia} coherente")
        # que no haya otro "Finalizar Día X" distinto
        otros = set(re.findall(r'Finalizar (Día \d+)<', t))
        if otros - {dia}: problemas.append(f"botón finalizar con día ajeno: {otros}")

    # 5. Fugas de contenido (contexto real, no substrings)
    fugas = []
    for pat in [r'\bGestor I\b', r'\bSustanciador\b', r'\b3PU-\d', r'\b4SU-\d',
                r'\bProcurador Judicial\b', r'\bURT\b', r'\bINDERVALLE\b',
                r'\bpaciente', r'\bcl[ií]nic', r'\btributari', r'\bcontribuyente',
                r'\bDIAN\b']:
        for mm in re.finditer(pat, t):
            frag = t[max(0,mm.start()-30):mm.start()+40]
            fugas.append(frag.strip())
    if fugas:
        problemas.append("POSIBLES FUGAS: " + " || ".join(fugas[:6]))

    print("ARCHIVO:", f)
    print("OK:", " | ".join(ok))
    if problemas:
        print("*** PROBLEMAS ***")
        for p in problemas: print("  -", p)
        return 1
    print(">>> VALIDACIÓN OK <<<")
    return 0

sys.exit(main())
