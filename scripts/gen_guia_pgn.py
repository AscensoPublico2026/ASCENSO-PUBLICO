#!/usr/bin/env python3
"""Genera una guía PGN completa a partir de un MOLDE probado y de un archivo de contenido.

El molde (`bases/pgn/_molde/guia-pgn.html`) aporta el diseño, la navegación de 10 secciones,
la barra de lectura, los checkpoints, el motor del mini-simulacro y el botón Finalizar.
El archivo de contenido aporta el texto y las preguntas.

Uso:  python3 scripts/gen_guia_pgn.py contenido/4TI15O/FUN-PJUD-01.py

El archivo de contenido es un módulo de Python con:

    META = dict(
        codigo='FUN-PJUD-4TI15O-01',
        archivo='FUN-PJUD-4TI15O-01-marco-normativo-policia-judicial.html',
        dia=14,
        titulo_doc='Marco normativo de Policía Judicial',
        h1='...',                      # título grande del encabezado
        kicker='Día 14 · Funcional',
        sub='<strong>…</strong> párrafo de presentación (admite HTML)',
        badges=['⏱ 95-115 min', '🏛️ Régimen PGN', '📖 Funcional'],
        fmeta='Marco normativo de Policía Judicial (Ley 906 de 2004 y Manual Único)',
        cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
        conv='257-2026',
        alerta='Marco normativo de Policía Judicial',   # texto del alert al finalizar
        es_simulacro=False,
    )
    SEC = {0: '…', 1: '…', …, 8: '…'}   # HTML interno de cada sección (sin la etiqueta <section>)
    QUIZ_INTRO = 'Responde estas 15 preguntas…'
    P = [ (correcta, ctx, enunciado, [opA, opB, opC, opD], feedback_ok, feedback_no), … ]

Cada sección debe empezar por su `<div class="eyebrow">…</div>` y su `<h2 class="sec-title">…</h2>`.
La sección 2 (Desarrollo) es la que debe superar las 10.000 palabras.
Valida el resultado con scripts/auditar-pgn.py y scripts/probar-paginas.js.
"""
import re, sys, os, json, importlib.util, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
MOLDE_DEF = 'bases/pgn/_molde/guia-pgn.html'
L = 'ABCD'


def cargar(path):
    spec = importlib.util.spec_from_file_location('contenido', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def castellano(s):
    """Repara las contracciones que rompen los reemplazos de identidad.

    Cuando una sustitución cambia «la ventanilla» por «el punto de atención»,
    una frase como «se acerca a la ventanilla» queda como «se acerca a el punto
    de atención». Son errores que el estudiante ve en la primera lectura. Solo
    se corrige la forma en minúscula: «siendo A el más exigente» (la letra de
    una opción) debe quedar intacta.
    """
    s = re.sub(r'\ba el\s+(?=[A-Za-zÁÉÍÓÚÑáéíóúñ])', 'al ', s)
    s = re.sub(r'\bde el\s+(?=[A-Za-zÁÉÍÓÚÑáéíóúñ])', 'del ', s)
    # concordancia de género: «la Seccional» → «la División» deja «el División»
    for mal, bien in (('el División', 'la División'), ('El División', 'La División'),
                      ('del División', 'de la División'), ('al División', 'a la División'),
                      ('un División', 'una División'), ('este División', 'esta División'),
                      ('ese División', 'esa División'), ('los División', 'las División')):
        s = re.sub(r'\b' + mal + r'\b', bien, s)
    # Las denominaciones de empleo de la PGN son gramaticalmente masculinas
    # aunque la aspirante sea mujer; los reemplazos de identidad dejaban
    # mezclas como «la Técnico en Criminalística» junto a «el Técnico en
    # Criminalística» en la misma guía, que se leen como un descuido.
    for d in ('Técnico en Criminalística', 'Técnico Investigador', 'Técnico Administrativo',
              'Sustanciador', 'Citador', 'Asesor', 'Gestor', 'Analista'):
        s = re.sub(r'\bLa (' + d + r')\b', r'El \1', s)
        s = re.sub(r'\bla (' + d + r')\b', r'el \1', s)
        s = re.sub(r'\bUna (' + d + r')\b', r'Un \1', s)
        s = re.sub(r'\buna (' + d + r')\b', r'un \1', s)
        s = re.sub(r'\bde la (' + d + r')\b', r'del \1', s)
        s = re.sub(r'\ba la (' + d + r')\b', r'al \1', s)
    return s


def bloque_pregunta(n, correcta, ctx, ask, ops):
    assert len(ops) == 4, f'pregunta {n}: deben ser 4 opciones'
    o = '\n'.join(
        f'      <div class="opcion" data-idx="{k}"><span class="letra">{L[k]}</span><span>{x}</span></div>'
        for k, x in enumerate(ops))
    return (f'  <div class="pregunta" data-correct="{correcta}">\n'
            f'    <div class="q-num">Pregunta {n}</div>\n'
            f'    <p class="q-texto">{ctx}</p>\n'
            f'    <p class="q-texto">{ask}</p>\n'
            f'    <div class="opciones">\n{o}\n    </div>\n'
            f'    <div class="feedback"></div>\n  </div>\n')


def generar(path):
    c = cargar(path)
    M, SEC, P = c.META, c.SEC, c.P
    s = open(M.get('molde', MOLDE_DEF), encoding='utf-8').read()
    nsec = len(set(re.findall(r'data-sec="(\d+)"', s)))
    con_quiz = 9 in SEC or bool(P)

    # --- head / header ---
    s = re.sub(r'<title>.*?</title>',
               f"<title>{M['codigo']} · {H.escape(M['titulo_doc'])} — {H.escape(M['cargo'].split(' (')[0])} · Ascenso Público</title>",
               s, count=1, flags=re.S)
    s = re.sub(r'<span class="doc-ref">.*?</span>', f'<span class="doc-ref">{M["codigo"]}</span>', s, count=1)
    s = re.sub(r'<div class="kicker">.*?</div>', f'<div class="kicker">{H.escape(M["kicker"])}</div>', s, count=1)
    s = re.sub(r'<h1>.*?</h1>', f'<h1>{M["h1"]}</h1>', s, count=1, flags=re.S)
    est = ('background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);color:#fff;'
           'padding:5px 13px;border-radius:20px;font-size:.78rem;font-weight:600')
    badges = (f'<span style="{est}" class="badge">📅 Día {M["dia"]} de 21</span>'
              + ''.join(f'<span class="badge" style="{est}">{b}</span>' for b in M['badges']))
    s = re.sub(r'<div class="badges"[^>]*>.*?</div>\n',
               '<div class="badges" style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;'
               f'margin-top:16px;position:relative;z-index:2">{badges}</div>\n', s, count=1, flags=re.S)
    s = re.sub(r'<p class="header-sub">.*?</p>', f'<p class="header-sub">{M["sub"]}</p>', s, count=1, flags=re.S)

    # --- secciones de contenido ---
    for n in range(nsec if not con_quiz else nsec - 1):
        pat = re.compile(r'(<section class="section[^"]*" data-sec="%d">)(.*?)(\s*</section>)' % n, re.S)
        assert pat.search(s), f'no se encontró la sección {n} en el molde'
        s = pat.sub(lambda m: m.group(1) + '\n' + SEC[n].strip() + m.group(3), s, count=1)

    # --- última sección: simulacro ---
    if not con_quiz:
        P = []
    pregs = ''.join(bloque_pregunta(i, p[0], p[1], p[2], p[3]) + '\n' for i, p in enumerate(P, 1))
    # el contenido de las preguntas puede traer «%» (porcentajes), que rompería el formateo de abajo
    sec9 = ('\n  <div class="eyebrow">Simulacro de práctica</div>\n'
            f'  <h2 class="sec-title">Pon a prueba lo aprendido</h2>\n  <p>{c.QUIZ_INTRO}</p>\n\n'.replace('%', '%%')
            + pregs.replace('%', '%%') +
            '  <div id="resultado">\n    <div class="score-num"><span id="aciertos">0</span>/%d</div>\n'
            '    <p id="msg-resultado"></p>\n'
            '    <button class="btn gold" onclick="reiniciar()">🔄 Reintentar</button>\n  </div>\n\n'
            '  <div style="text-align:center;margin-top:26px">\n'
            '    <button class="btn gold" id="btnFinalizar" style="font-size:1rem">✅ Finalizar Día %d</button>\n  </div>\n\n'
            '  <div class="nav-footer">\n    <button id="btnPrev">← Sección anterior</button>\n'
            '    <button id="btnNext">Siguiente sección →</button>\n  </div>\n') % (len(P), M['dia'])
    if not con_quiz:
        cierre = ('\n  <div style="text-align:center;margin:30px 0 8px">\n'
                  '    <button id="btnFinalizar" style="background:linear-gradient(135deg,#c9a227,#e0b84a);color:#1a1a1a;'
                  'border:none;padding:14px 32px;border-radius:10px;font-weight:700;font-size:1rem;cursor:pointer">'
                  f'✅ Finalizar Día {M["dia"]}</button>\n  </div>\n')
        s = re.sub(r'(<section class="section[^"]*" data-sec="%d">)(.*?)(\s*</section>)' % (nsec - 1),
                   lambda m: m.group(1) + m.group(2) + cierre + m.group(3), s, count=1, flags=re.S)
    if con_quiz:
        s = re.sub(r'(<section class="section[^"]*" data-sec="%d">)(.*?)(\s*</section>)' % (nsec - 1),
                   lambda m: m.group(1) + sec9 + m.group(3), s, count=1, flags=re.S)

    # --- footer ---
    s = re.sub(r'<div class="fmeta">.*?</div>',
               f'<div class="fmeta">{M["codigo"]} · {H.escape(M["fmeta"])} · Día {M["dia"]} · {H.escape(M["cargo"])}'
               f'<br>© Ascenso Público. Preparación para el Concurso de Méritos de la Procuraduría General de la Nación · '
               f'Convocatoria {M["conv"]}</div>', s, count=1, flags=re.S)

    # --- JS: feedbacks, alert del botón y umbrales del puntaje ---
    esc = lambda x: x.replace('\\', '\\\\').replace("'", "\\'")
    if P:
      fb = 'const feedbacks={\n' + ''.join(
        f"{i}:{{ok:'{esc(p[4])}',no:'{esc(p[5])}'}},\n" for i, p in enumerate(P)) + '};\n'
      s = re.sub(r'const feedbacks=\{.*?\n\};\n', fb, s, count=1, flags=re.S)
    s = re.sub(r"alert\('[^']*D[ií]a[^']*'\)",
               lambda _m: f"alert('✅ Has finalizado el Día {M['dia']}: {esc(M['alerta'])}. ¡Excelente trabajo, sigue así!')",
               s, count=1)
    alto, medio = max(1, round(len(P) * 0.8)), max(1, round(len(P) * 0.6))
    s = re.sub(r'aciertos>=\d+\?', f'aciertos>={alto}?', s, count=1)
    s = re.sub(r'aciertos>=\d+\?', f'aciertos>={medio}?', s, count=1)
    s = re.sub(r"<span id=\"aciertos\">0</span>/\d+", f'<span id="aciertos">0</span>/{len(P)}', s)
    s = re.sub(r'respondidas===\d+', f'respondidas==={len(P)}', s)

    s = castellano(s)
    assert '{{' not in s, 'quedaron marcadores sin reemplazar: ' + str(set(re.findall(r'\{\{[A-Z]+\}\}', s)))
    carpeta = 'simulacro' if M.get('es_simulacro') else 'guias'
    dest = os.path.join(carpeta, M['archivo'])
    open(dest, 'w', encoding='utf-8').write(s)
    pal = len(re.sub(r'<[^>]+>', ' ', SEC.get(2, '')).split())
    print(f'{dest}  ·  Desarrollo {pal} palabras  ·  {len(P)} preguntas')
    return dest


if __name__ == '__main__':
    for p in sys.argv[1:]:
        generar(p)
