#!/usr/bin/env python3
"""Herramientas para corregir los mini-simulacros en formato HTML (.pregunta data-correct / data-correcta).

Uso como módulo:
    from preguntas_pgn import volcar, reescribir, opciones, ampliar, verificar
    volcar('bases/pgn/Profesional/FUN-GP-01.html', [1, 2])
    reescribir(f, {3: (contexto, enunciado, [A, B, C, D])})   # conserva la letra correcta y la numeración
    opciones(f, {5: {0: 'nuevo texto A', 2: 'nuevo texto C'}})
    ampliar(f, {7: 'frase que se agrega al final del caso'})
Uso por consola:
    python3 scripts/preguntas_pgn.py <archivo> [n1,n2,...]      # vuelca preguntas con largos y correcta
Regla del estándar: caso+enunciado 450-1000 car.; 4 opciones de 150-280 car.; la correcta NO puede
superar en más de 20 % a la opción incorrecta más larga.
"""
import re, sys, html

PAT = r'<div class="pregunta" data-(correcta?)="(\d)">(.*?)<div class="feedback'


def _txt(x):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x))).strip()


def _bloques(s):
    return list(re.finditer(PAT, s, re.S))


def _ops(body):
    return list(re.finditer(r'(<div class="opcion"[^>]*>\s*<span class="letra">.</span>\s*<span>)(.*?)(</span>\s*</div>)', body, re.S))


def volcar(f, nums=None):
    s = open(f, encoding='utf-8').read()
    for i, m in enumerate(_bloques(s), 1):
        if nums and i not in nums: continue
        c = int(m.group(2)); body = m.group(3)
        ps = [_txt(p) for p in re.findall(r'<p class="q-texto">(.*?)</p>', body, re.S)]
        print(f'Q{i} correcta={"ABCD"[c]} caso={sum(map(len, ps))}')
        for p in ps: print('   P:', p)
        for k, o in enumerate(_ops(body)):
            t = _txt(o.group(2)); print(f'   {"ABCD"[k]}{"*" if k == c else " "}({len(t)}) {t}')


def reescribir(f, P):
    s = open(f, encoding='utf-8').read(); bl = _bloques(s)
    for n in sorted(P, reverse=True):
        m = bl[n - 1]; body = m.group(3); ctx, ask, ops = P[n]
        assert len(ops) == 4, n
        qn = re.search(r'<div class="q-num">.*?</div>', body, re.S).group(0)
        ma = re.search(r'<div class="opcion" (data-[a-z]+)=', body)
        attr = f' {ma.group(1)}="{{k}}"' if ma else ''
        o = '\n'.join(f'      <div class="opcion"{attr.format(k=k)}><span class="letra">{"ABCD"[k]}</span><span>{x}</span></div>' for k, x in enumerate(ops))
        nb = f'\n    {qn}\n    <p class="q-texto">{ctx}</p>\n    <p class="q-texto">{ask}</p>\n    <div class="opciones">\n{o}\n    </div>\n    '
        s = s[:m.start(3)] + nb + s[m.end(3):]
    open(f, 'w', encoding='utf-8').write(s)


def opciones(f, O):
    s = open(f, encoding='utf-8').read(); bl = _bloques(s)
    for n in sorted(O, reverse=True):
        m = bl[n - 1]; body = m.group(3); sp = _ops(body); nb = body
        for k in sorted(O[n], reverse=True):
            nb = nb[:sp[k].start(2)] + O[n][k] + nb[sp[k].end(2):]
        s = s[:m.start(3)] + nb + s[m.end(3):]
    open(f, 'w', encoding='utf-8').write(s)


def ampliar(f, E):
    s = open(f, encoding='utf-8').read(); bl = _bloques(s)
    for n in sorted(E, reverse=True):
        m = bl[n - 1]; p = re.search(r'<p class="q-texto">(.*?)</p>', m.group(3), re.S)
        a = m.start(3) + p.end(1); s = s[:a] + ' ' + E[n] + s[a:]
    open(f, 'w', encoding='utf-8').write(s)


def verificar(f):
    s = open(f, encoding='utf-8').read(); malos = []
    for a, b in (('{{CARGO}}', 'Profesional Universitario'), ('{{COD}}', '9XX-99'), ('{{CONV}}', '999-2026')):
        s = s.replace(a, b)
    for i, m in enumerate(_bloques(s), 1):
        c = int(m.group(2)); body = m.group(3)
        caso = sum(len(_txt(p)) for p in re.findall(r'<p class="q-texto">(.*?)</p>', body, re.S))
        L = [len(_txt(o.group(2))) for o in _ops(body)]
        otros = [l for k, l in enumerate(L) if k != c]
        prob = []
        if caso < 450: prob.append(f'caso {caso}')
        if caso > 1000: prob.append(f'caso largo {caso}')
        if len(L) != 4: prob.append(f'{len(L)} opciones')
        elif min(L) < 150: prob.append(f'opción corta {min(L)}')
        if len(L) == 4 and L[c] > max(otros) * 1.2: prob.append(f'correcta se delata {L[c]} vs {max(otros)}')
        if prob: malos.append((i, prob))
    for i, p in malos: print(f'  Q{i}: {", ".join(p)}')
    print(f'{f}: {"OK" if not malos else str(len(malos)) + " preguntas por corregir"}')
    return not malos


if __name__ == '__main__':
    nums = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else None
    volcar(sys.argv[1], nums)


def mover(f, M):
    """M = {n: letra_destino}. Intercambia la opción correcta con la de la letra destino y actualiza data-correct(a).
    OJO: revisar que la retroalimentación no mencione letras (A, B, C, D)."""
    s = open(f, encoding='utf-8').read()
    for n in sorted(M, reverse=True):
        bl = _bloques(s); m = bl[n - 1]; c = int(m.group(2)); d = 'ABCD'.index(M[n]); body = m.group(3)
        sp = _ops(body); tc, td = sp[c].group(2), sp[d].group(2)
        if c != d:
            a, b = (c, d) if c < d else (d, c); ta, tb = sp[a].group(2), sp[b].group(2)
            nb = body[:sp[a].start(2)] + tb + body[sp[a].end(2):sp[b].start(2)] + ta + body[sp[b].end(2):]
        else:
            nb = body
        head = s[m.start():m.start(3)].replace(f'="{c}"', f'="{d}"', 1)
        s = s[:m.start()] + head + nb + s[m.end(3):]
    open(f, 'w', encoding='utf-8').write(s)
