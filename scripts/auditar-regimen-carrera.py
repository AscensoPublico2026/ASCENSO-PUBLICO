#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprueba que las guías no le atribuyan a la CNSC lo que es de la PGN.

Por qué existe. Las guías de este catálogo se construyen reutilizando guías
escritas para cargos de la DIAN, que se rigen por la Ley 909 de 2004 y cuyos
concursos los adelanta la CNSC. Los reemplazos de identidad cambian el nombre
del empleo y de la entidad, pero NO cambian el régimen. Así fue como el curso
del Técnico en Criminalística 4TC-17 llegó a afirmar «en la Procuraduría, la
CNSC es la que organiza el concurso» y «la lista de elegibles de la CNSC»,
mientras en otra sección del mismo curso enseñaba, correctamente, que el
artículo 130 de la Constitución exceptúa las carreras de carácter especial.

La PGN tiene carrera especial (arts. 130 y 279 de la Constitución y Decreto
Ley 262 de 2000, arts. 183 a 226) y adelanta sus concursos por medio de su
Oficina de Selección y Carrera y su Comisión de Carrera. Es justamente lo que
la prueba evalúa, y el distractor típico es el error contrario.

Cómo lee el HTML. Las etiquetas en línea (strong, em, mark, a…) se eliminan
sin dejar hueco, para que la frase quede entera; las de bloque se vuelven un
salto de línea, que sirve de borde. Esto importa: con un corte demasiado laxo
la «frase» atraviesa párrafos y una afirmación errónea queda exculpada por un
«régimen especial» que estaba más arriba; con uno demasiado estricto la frase
se parte y se pierde la aclaración que venía al final. Las dos versiones
dejaban pasar errores de verdad.

Qué marca y qué no:
  · CRITICO  Una afirmación del material que le entrega a la CNSC el concurso,
             la carrera, la lista de elegibles, los puntajes o las
             reclamaciones de la PGN.
  · No marca las frases que contrastan los dos regímenes, que es el contenido
    que se quiere («la CNSC administra la carrera general, no la de la PGN»).
  · No marca las opciones de las preguntas, las de los puntos de control ni la
    retroalimentación de error: ahí el enunciado equivocado es deliberado.

Uso:  python3 scripts/auditar-regimen-carrera.py <plan-id> [...]
"""
import json, os, re, sys, collections, html as H

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
BIB = 'biblioteca/biblioteca.json'

ESPECIAL = re.compile(r'^pgn-', re.I)   # planes cuya carrera no es de la CNSC

EN_LINEA = r'strong|em|mark|b|i|u|span|a|code|small|sup|sub|abbr'

# zonas donde una afirmación equivocada es un distractor deliberado
DISTRACTORES = [
    r'<div class="opciones">[\s\S]*?</div>\s*</div>',
    r'<div class="cp-opts">[\s\S]*?</div>',
    r'<(?:div|button) class="cp-opt?"[\s\S]*?</(?:div|button)>',
    r"no:'(?:\\.|[^'])*'",
    r'"ops"\s*:\s*\[[\s\S]*?\]',
    r'data-exp="[^"]*"',
]

# la CNSC como sujeto de un verbo de administración del concurso, o el
# concurso / la lista / la reclamación atribuidos a ella
ATRIBUYE = re.compile(
    r'\b(?:la\s+)?(?:CNSC|Comisi[oó]n Nacional del Servicio Civil)\b[^,]{0,40}'
    r'\b(?:organiza|adelanta|convoca|administra|expide|conforma|aplica|define|maneja|'
    r'califica|resuelve|vigila)\b'
    r'|\b(?:concurso|lista[s]? de elegibles|puntaje[s]?|reclamaci[oó]n(?:es)?|inscripci[oó]n)\b'
    r'[^,]{0,50}\b(?:de\s+la\s+|ante\s+la\s+|por\s+la\s+|que\s+convoque\s+la\s+)'
    r'(?:CNSC|Comisi[oó]n Nacional del Servicio Civil)\b', re.I)

# la frase contrasta los dos regímenes, o reporta una creencia ajena para
# corregirla: es el contenido que se quiere
CONTRASTE = re.compile(
    r'\bno\b|\bni\b|car[áa]cter especial|carrera[s]?(?:\s+\w+)? general'
    r'|carrera[s]?(?:\s+\w+)? especial|r[ée]gimen general|r[ée]gimen especial'
    r'|la mayor[ií]a de las entidades|otras entidades|propia entidad'
    r'|propia Procuradur[ií]a|Oficina de Selecci[oó]n|Comisi[oó]n de Carrera'
    r'|creer|supone|cree|dice|dijo|afirma|insiste|sospecha|asegur'
    r'|una opci[oó]n diga|parece|trampa|error \d|es incorrect|es falso|es falsa'
    r'|a diferencia|salvo|excepci[oó]n|except[uú]a|¿|\?'
    r'|art\.?\s*130|art[íi]culo 130', re.I)


def frases(html):
    """Frases del texto visible, sin romper las etiquetas en línea."""
    s = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', html)
    for p in DISTRACTORES:
        s = re.sub(p, ' ', s)
    s = re.sub(rf'</?(?:{EN_LINEA})(?:\s[^>]*)?>', '', s)   # en línea: sin hueco
    s = re.sub(r'<[^>]+>', '\n', s)                          # bloque: borde
    s = H.unescape(s)
    for fr in re.split(r'[.;!?\n]+', s):
        fr = re.sub(r'\s+', ' ', fr).strip()
        if fr:
            yield fr


def main():
    planes = [a for a in sys.argv[1:] if not a.startswith('--')]
    cat = json.load(open(BIB, encoding='utf-8'))['guias']
    hall, revisadas = [], 0
    for plan in planes:
        if not ESPECIAL.match(plan):
            print(f'⚠️  {plan}: no es un plan de la PGN; esta auditoría no aplica')
            continue
        for g in [x for x in cat if x.get('plan') == plan and x.get('archivo')]:
            arch = g['archivo']
            if not os.path.exists(arch):
                continue
            revisadas += 1
            for fr in frases(open(arch, encoding='utf-8').read()):
                if ATRIBUYE.search(fr) and not CONTRASTE.search(fr):
                    hall.append(('CRITICO', os.path.basename(arch), fr[:230]))
    sev = collections.Counter(h[0] for h in hall)
    print(f'Guías revisadas: {revisadas} · CRITICO {sev["CRITICO"]}')
    for h in hall:
        print(f'  [{h[0]}] {h[1]}: {h[2]}')
    return 1 if hall else 0


if __name__ == '__main__':
    sys.exit(main())
