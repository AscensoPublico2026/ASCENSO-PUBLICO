#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisa la coherencia interna de las preguntas y los puntos de control.

Lo que buscan las otras auditorías es que la guía esté completa y que sus
datos sean del cargo. Esto busca algo distinto: que la guía no se contradiga
a sí misma. Son errores que el estudiante ve de inmediato y que destruyen la
confianza en el material.

Comprueba:
  1. ORDINAL      Si la retroalimentación dice «la tercera» o «la opción C»,
                  que esa sea de verdad la opción marcada como correcta.
  2. CHECKPOINT   Lo mismo en los puntos de control (data-correcta vs. cp-fb).
  3. REPETIDAS    Que no haya dos preguntas con el mismo enunciado dentro de
                  una guía ni a lo largo de todo el plan.
  4. OPCIONES     Que las cuatro opciones de una pregunta sean distintas y que
                  no se repita una opción textual entre preguntas de la guía.
  5. VACÍOS       Que ninguna pregunta quede sin retroalimentación y que el
                  índice de la correcta esté dentro de rango.
  6. CONTRADICE   Que la retroalimentación de acierto no empiece negando
                  («Incorrecto…») ni la de error afirmando («Correcto…»).

Uso:  python3 scripts/auditar-coherencia-preguntas.py <plan-id> [...]
"""
import json, os, re, sys, collections, html as H

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
BIB = 'biblioteca/biblioteca.json'

ORDINAL = {'primera': 0, 'segunda': 1, 'tercera': 2, 'cuarta': 3,
           'primer': 0, 'segundo': 1, 'tercero': 2, 'cuarto': 3}
LETRA = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
ORD = ['primera', 'segunda', 'tercera', 'cuarta', 'quinta']


def limpio(x):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', H.unescape(x))).strip()


def preguntas(html):
    """[(n, correcta, enunciado, [opciones])] del mini-simulacro de la guía."""
    out = []
    for i, m in enumerate(re.finditer(
            r'<div class="pregunta" data-correct="(\d+)">(.*?)\n  </div>', html, re.S), 1):
        c = int(m.group(1)); cuerpo = m.group(2)
        txts = re.findall(r'<p class="q-texto">(.*?)</p>', cuerpo, re.S)
        ops = re.findall(r'<div class="opcion" data-idx="\d+"><span class="letra">[A-D]</span><span>(.*?)</span></div>', cuerpo, re.S)
        out.append((i, c, limpio(' '.join(txts)), [limpio(o) for o in ops]))
    return out


def feedbacks(html):
    """{n: (ok, no)} del objeto feedbacks del JS."""
    m = re.search(r'const feedbacks=\{(.*?)\n\};', html, re.S)
    if not m:
        return {}
    d = {}
    for mm in re.finditer(r'(\d+):\{ok:\'((?:\\.|[^\'])*)\',no:\'((?:\\.|[^\'])*)\'\}', m.group(1)):
        d[int(mm.group(1)) + 1] = (mm.group(2).replace("\\'", "'"), mm.group(3).replace("\\'", "'"))
    return d


def checkpoints(html):
    """[(n, correcta, explicación, [opciones])] en los DOS formatos que existen.

    Las guías conviven en dos generaciones de maquetado y si solo se reconoce
    una, el auditor pasa en silencio sobre la otra, que es peor que no auditar:
      · molde actual   <div class="checkpoint" data-correcta="1"> … <div class="cp-op">
      · bases antiguas <div class="checkpoint"> … <button class="cp-opt" data-ans="1">
    """
    out = []
    for m in re.finditer(r'<div class="checkpoint"(.*?)(?=<div class="checkpoint"|</section|\Z)', html, re.S):
        bloque = m.group(1)
        fb = re.search(r'<div class="cp-fb"[^>]*>(.*?)(?:</div>|\Z)', bloque, re.S)
        if not fb:
            continue
        cor = None
        ops = []
        cab = re.match(r'\s*data-correcta="(\d+)"', bloque)
        # marcas de «esta es la correcta» en los tres maquetados que existen
        # el maquetado varía entre generaciones: <div> o <button>, clase cp-op o
        # cp-opt, y el atributo data-ok o data-ans. Se reconocen todas.
        marcas = [(m.group(2), m.group(3)) for m in re.finditer(
            r'<(div|button)[^>]*class="cp-opt?"[^>]*data-(?:ok|ans)="(\d)"[^>]*>(.*?)</\1>', bloque, re.S)]
        if marcas:
            ops = [m[1] for m in marcas]
            buenas = [i for i, m in enumerate(marcas) if m[0] == '1']
            cor = buenas[0] if len(buenas) == 1 else (-1 if not buenas else -2)
        elif cab:                                # formato del molde: índice en la cabecera
            cor = int(cab.group(1))
            ops = re.findall(r'<div class="cp-op"[^>]*>(.*?)</div>', bloque, re.S)
        if cor is None:
            out.append((len(out) + 1, None, limpio(fb.group(1)), ops))
        else:
            out.append((len(out) + 1, cor, limpio(fb.group(1)), [limpio(o) for o in ops]))
    return out


# Solo se interpreta como referencia a una OPCIÓN cuando el texto lo dice sin
# ambigüedad. «La primera línea de defensa» o «la primera idea» no lo son, y
# marcarlas produciría falsos positivos que esconden los errores de verdad.
CITA_OPCION = [
    r'\bopci[oó]n\s+(?:es\s+)?(?:la\s+)?(primera|segunda|tercera|cuarta)\b',
    r'\b(?:respuesta|correcta|acertada)\s+(?:correcta\s+)?(?:es\s+)?(?:la\s+)?(primera|segunda|tercera|cuarta)\b',
    r'^\s*(?:correcto|correcta)\s*[:.\-–]\s*(?:es\s+)?(?:la\s+)?(primera|segunda|tercera|cuarta)\b',
    r'^\s*(?:la\s+)?(primera|segunda|tercera|cuarta)\s+(?:opci[oó]n|es\s+la\s+correcta)',
]
CITA_LETRA = [
    r'\bopci[oó]n\s+([A-D])\b',
    r'\b(?:respuesta|correcta)\s+(?:es\s+)?(?:la\s+)?([A-D])\b',
    r'^\s*(?:correcto|correcta)\s*[:.\-–]\s*(?:la\s+)?([A-D])\b',
]


def ordinal_citado(txt):
    """Índice de opción que la retroalimentación afirma explícitamente, o None."""
    plano = limpio(txt)
    t = plano.lower()
    for pat in CITA_OPCION:
        m = re.search(pat, t)
        if m:
            return ORDINAL[m.group(1)]
    for pat in CITA_LETRA:
        m = re.search(pat, plano)
        if m:
            return LETRA[m.group(1)]
    return None


def main():
    planes = [a for a in sys.argv[1:] if not a.startswith('--')]
    cat = json.load(open(BIB, encoding='utf-8'))['guias']
    hall = []
    enunciados_plan = collections.defaultdict(list)

    for plan in planes:
        guias = [g for g in cat if g.get('plan') == plan and g.get('archivo')]
        for g in guias:
            nombre = os.path.basename(g['archivo'])
            if not os.path.exists(g['archivo']):
                continue
            s = open(g['archivo'], encoding='utf-8').read()
            P = preguntas(s); F = feedbacks(s)

            vistas = {}
            opciones_guia = {}
            for n, c, enun, ops in P:
                if not 0 <= c <= 3:
                    hall.append(('CRITICO', nombre, f'P{n}: índice de correcta fuera de rango ({c})'))
                if len(ops) != 4:
                    hall.append(('CRITICO', nombre, f'P{n}: tiene {len(ops)} opciones'))
                if len(set(ops)) != len(ops):
                    hall.append(('CRITICO', nombre, f'P{n}: opciones repetidas entre sí'))
                if n not in F:
                    hall.append(('CRITICO', nombre, f'P{n}: sin retroalimentación'))
                else:
                    ok, no = F[n]
                    cit = ordinal_citado(ok)
                    if cit is not None and cit != c:
                        hall.append(('CRITICO', nombre,
                            f'P{n}: la retroalimentación dice «la {ORD[cit]}» '
                            f'pero la correcta es la {ORD[c]}'))
                    if re.match(r'\s*incorrect', ok, re.I):
                        hall.append(('CRITICO', nombre, f'P{n}: la retroalimentación de acierto empieza negando'))
                    if re.match(r'\s*correcto\b', no, re.I):
                        hall.append(('CRITICO', nombre, f'P{n}: la retroalimentación de error empieza afirmando'))
                    if len(limpio(ok)) < 40:
                        hall.append(('MEDIO', nombre, f'P{n}: retroalimentación de acierto muy corta'))
                clave = enun[:120].lower()
                if clave in vistas:
                    hall.append(('ALTO', nombre, f'P{n}: enunciado repetido de la P{vistas[clave]}'))
                vistas[clave] = n
                enunciados_plan[clave].append(f'{nombre}#P{n}')
                for o in ops:
                    k = o[:90].lower()
                    if k in opciones_guia and opciones_guia[k] != n:
                        hall.append(('MEDIO', nombre, f'P{n}: repite una opción de la P{opciones_guia[k]}'))
                    opciones_guia[k] = n

            CP = checkpoints(s)
            declarados = len(re.findall(r'<div class="checkpoint"', s))
            if len(CP) != declarados:
                hall.append(('ALTO', nombre,
                    f'puntos de control ilegibles: {declarados} en el HTML, {len(CP)} con explicación leída'))
            for i, c, fb, ops in CP:
                if c is None:
                    hall.append(('ALTO', nombre, f'Checkpoint {i}: no se puede saber cuál es la opción correcta'))
                    continue
                if c == -1:
                    hall.append(('CRITICO', nombre, f'Checkpoint {i}: ninguna opción está marcada como correcta'))
                    continue
                if c == -2:
                    hall.append(('CRITICO', nombre, f'Checkpoint {i}: hay más de una opción marcada como correcta'))
                    continue
                if ops and not 0 <= c < len(ops):
                    hall.append(('CRITICO', nombre, f'Checkpoint {i}: la correcta ({c}) está fuera de las {len(ops)} opciones'))
                    continue
                if ops and len(set(ops)) != len(ops):
                    hall.append(('MEDIO', nombre, f'Checkpoint {i}: tiene opciones repetidas entre sí'))
                cit = ordinal_citado(fb)
                if cit is not None and cit != c:
                    hall.append(('CRITICO', nombre,
                        f'Checkpoint {i}: la explicación dice «la {ORD[cit]}» '
                        f'pero la marcada como correcta es la {ORD[c]}'
                        + (f' («{ops[c][:60]}…»)' if ops and c < len(ops) else '')))

        # repetidas entre guías del mismo plan
        for clave, donde in enunciados_plan.items():
            if len(donde) > 1 and len(set(d.split('#')[0] for d in donde)) > 1:
                hall.append(('ALTO', plan, 'enunciado repetido en ' + ', '.join(donde)))

    sev = collections.Counter(h[0] for h in hall)
    print(f'CRITICO {sev["CRITICO"]} · ALTO {sev["ALTO"]} · MEDIO {sev["MEDIO"]}')
    for s_ in ('CRITICO', 'ALTO', 'MEDIO'):
        for h in [x for x in hall if x[0] == s_]:
            print(f'  [{h[0]}] {h[1]}: {h[2]}')
    return 1 if sev['CRITICO'] else 0


if __name__ == '__main__':
    sys.exit(main())
