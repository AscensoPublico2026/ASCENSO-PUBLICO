#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de guías Ascenso Público — ensambla una guía HTML a partir de:
  - El molde fijo (motor/base-guia.html)  -> el diseño, NUNCA cambia
  - Un archivo de contenido (motor/contenido/<CODIGO>.json) -> lo único que cambia

Uso:
    python3 motor/construir_guia.py motor/contenido/FUN-ALM-01.json

Resultado: escribe guias/<archivo>.html listo para abrir en el navegador.
"""
import json, sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(BASE_DIR)


def paras(x):
    """Convierte texto (str) o lista de textos en uno o varios <p>."""
    if isinstance(x, list):
        return ''.join('<p>%s</p>' % s for s in x)
    return '<p>%s</p>' % x


def attr(s):
    """Escapa comillas dobles para usar texto dentro de un atributo HTML."""
    return s.replace('"', '&quot;')


def render_concepto(c):
    capas = ''
    if c.get('def'):
        capas += '<div class="capa cap-def"><div class="capa-icon def">📘</div><div class="capa-content"><span class="label">Definición</span>%s</div></div>' % paras(c['def'])
    if c.get('apl'):
        capas += '<div class="capa cap-apl"><div class="capa-icon apl">🎯</div><div class="capa-content"><span class="label">Aplicación</span>%s</div></div>' % paras(c['apl'])
    if c.get('eje'):
        capas += '<div class="capa cap-eje"><div class="capa-icon eje">🏛️</div><div class="capa-content"><span class="label">Ejemplo real</span>%s</div></div>' % paras(c['eje'])
    if c.get('cnsc'):
        capas += '<div class="capa cap-cnsc"><div class="capa-icon cnsc">📝</div><div class="capa-content"><span class="label">Cómo lo evalúa la CNSC</span>%s</div></div>' % paras(c['cnsc'])

    extra = ''
    if c.get('flujo'):
        pasos = ''.join(
            '<div class="flujo-paso"><span class="fp-n">%s</span><h4>%s</h4><p>%s</p></div>' % (p['n'], p['h'], p['p'])
            for p in c['flujo'])
        extra += '<div class="full"><div class="flujo">%s</div></div>' % pasos
    if c.get('subbloques'):
        dets = ''
        for sb in c['subbloques']:
            op = ' open' if sb.get('open') else ''
            dets += '<details class="sb sb-%s"%s><summary>%s</summary><div class="sb-body">%s</div></details>' % (
                sb.get('color', 'azul'), op, sb['summary'], sb['html'])
        extra += '<div class="sub-bloques">%s</div>' % dets
    if c.get('practica'):
        pr = c['practica']
        extra += '<div class="practica full"><div class="practica-head">%s</div><div class="practica-body">%s</div></div>' % (
            pr['head'], pr['html'])
    if c.get('ojo'):
        extra += '<div class="ojo full"><b>👁️ Ojo en la prueba:</b> %s</div>' % c['ojo']

    return ('<div class="concepto"><div class="concepto-head"><span class="ch-icon">%s</span><span>%s</span></div>'
            '<div class="concepto-body">%s%s</div></div>') % (c['icono'], c['titulo'], capas, extra)


def render_checkpoint(cp):
    ops = ''
    for o in cp['opciones']:
        ok = '1' if o.get('ok') else '0'
        ops += '<button class="cp-opt" data-ok="%s" data-exp="%s">%s</button>' % (ok, attr(o['exp']), o['texto'])
    return ('<div class="checkpoint"><div class="cp-tag">✋ Aplica lo aprendido</div>'
            '<p class="cp-q">%s</p><div class="cp-opts">%s</div><div class="cp-fb"></div></div>') % (cp['q'], ops)


def render_fuentes(f):
    items = ''.join(
        '<li><strong>%s</strong> %s: <a href="%s" target="_blank" rel="noopener">consultar</a></li>' % (
            it['label'], it.get('desc', ''), it['url'])
        for it in f['items'])
    return ('<div class="fuentes"><div class="box-title">📚 Profundiza en las fuentes oficiales</div>'
            '<p>%s</p><ul class="lista">%s</ul></div>') % (f['intro'], items)


# ============================================================
# DESARROLLO v3 — estilo editorial con bloques flexibles por tema.
# Cada guía compone su Desarrollo con los bloques que necesite, así
# cada guía es única y trabaja sus temas con su propia profundidad.
# ============================================================
def render_bloque(b):
    t = b.get('tipo')
    if t == 'texto':
        return '<div class="b-texto">%s</div>' % b['html']
    if t == 'definicion':
        return '<div class="def-panel"><span class="def-label">Definición</span>%s</div>' % b['html']
    if t == 'idea':
        return '<div class="idea"><span class="idea-ic">💡</span><div>%s</div></div>' % b['html']
    if t == 'ejemplo':
        return '<div class="ejemplo"><div class="ejemplo-head">🏛️ Ejemplo</div><div class="ejemplo-body">%s</div></div>' % b['html']
    if t == 'prueba':
        return '<div class="prueba"><div class="prueba-head">🎯 En la prueba</div><div>%s</div></div>' % b['html']
    if t == 'lista':
        return '<ul class="lista">%s</ul>' % ''.join('<li>%s</li>' % i for i in b['items'])
    if t == 'tabla':
        head = ''.join('<th>%s</th>' % h for h in b['head'])
        filas = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in f) for f in b['filas'])
        return '<div class="tabla-wrap"><table><tr>%s</tr>%s</table></div>' % (head, filas)
    if t == 'acordeon':
        items = ''
        for it in b['items']:
            op = ' open' if it.get('open') else ''
            items += '<details class="acc"%s><summary>%s</summary><div class="acc-body">%s</div></details>' % (op, it['titulo'], it['html'])
        return '<div class="acordeon">%s</div>' % items
    if t == 'calculo':
        # Fórmulas y procesos matemáticos explicados paso a paso.
        intro = '<div class="calculo-intro"><p>%s</p></div>' % b['intro'] if b.get('intro') else ''
        datos = ''
        if b.get('datos'):
            lis = ''.join('<li>%s</li>' % d for d in b['datos'])
            datos = '<div class="calc-datos"><span class="cd-label">Datos de partida</span><ul>%s</ul></div>' % lis
        pasos = ''
        for i, p in enumerate(b.get('pasos', []), 1):
            n = p.get('n', i)
            formula = '<div class="calc-formula">%s</div>' % p['formula'] if p.get('formula') else ''
            res = '<div class="calc-res-paso">%s</div>' % p['resultado'] if p.get('resultado') else ''
            pasos += ('<div class="calc-paso"><span class="calc-n">%s</span>'
                      '<div class="calc-body"><div class="calc-label">%s</div>%s%s</div></div>') % (
                n, p.get('label', ''), formula, res)
        total = ''
        if b.get('total'):
            tt = b['total']
            total = ('<div class="calc-total"><span class="ct-label">%s</span>'
                     '<span class="ct-valor">%s</span></div>') % (tt.get('label', ''), tt.get('valor', ''))
        nota = '<div class="calc-nota">%s</div>' % b['nota'] if b.get('nota') else ''
        head = b.get('titulo', 'Cálculo paso a paso')
        return ('<div class="calculo"><div class="calculo-head">🧮 %s</div>%s%s'
                '<div class="calc-pasos">%s</div>%s%s</div>') % (head, intro, datos, pasos, total, nota)
    if t == 'minicheck':
        return render_checkpoint(b)
    return ''


def render_tema(t):
    bloques = ''.join(render_bloque(b) for b in t.get('bloques', []))
    chip = t.get('icono') or str(t.get('n', ''))
    return ('<div class="modulo"><div class="modulo-head"><span class="modulo-n">%s</span><h3>%s</h3></div>%s</div>'
            % (chip, t['titulo'], bloques))


def build_main(d):
    s = []
    # 0 Objetivo
    o = d['objetivo']
    narr = '<div class="narr"><span class="narr-tag">%s</span>%s</div>' % (o['narr']['tag'], paras(o['narr']['parrafos']))
    lista = ''.join('<li>%s</li>' % i for i in o['lista'])
    s.append('<section class="section visible" data-sec="0"><span class="eyebrow">Sección 1 · Objetivo</span>'
             '<h2 class="sec-title">🎯 ¿Qué vas a aprender hoy?</h2>%s'
             '<div class="card card-lead"><p>%s</p><ul class="lista">%s</ul></div>'
             '<div class="box gold"><div class="box-title">💎 La promesa de esta guía</div><p>%s</p></div></section>'
             % (narr, o['intro'], lista, o['promesa']))
    # 1 Importancia
    im = d['importancia']
    s.append('<section class="section" data-sec="1"><span class="eyebrow">Sección 2 · Importancia</span>'
             '<h2 class="sec-title">⭐ ¿Por qué este tema es clave para tu prueba?</h2>%s'
             '<div class="box info"><div class="box-title">ℹ️ Dato clave</div><p>%s</p></div></section>'
             % (paras(im['parrafos']), im['dato_clave']))
    # 2 Desarrollo
    de = d['desarrollo']
    cuerpo = ''
    if de.get('temas'):
        # Estilo editorial v3: cada tema con sus propios bloques (único por guía)
        for t in de['temas']:
            cuerpo += render_tema(t)
    else:
        # Estilo clásico: conceptos en 4 capas
        for c in de.get('conceptos', []):
            cuerpo += render_concepto(c)
            if c.get('checkpoint'):
                cuerpo += render_checkpoint(c['checkpoint'])
    if de.get('fuentes'):
        cuerpo += render_fuentes(de['fuentes'])
    s.append('<section class="section" data-sec="2"><span class="eyebrow">Sección 3 · Desarrollo</span>'
             '<h2 class="sec-title">📖 %s</h2><p>%s</p>%s</section>'
             % (de.get('titulo', 'Desarrollo del tema'), de['intro'], cuerpo))
    # 3 Comparaciones
    comp = ''
    for cp in d.get('comparaciones', []):
        filas = ''.join('<tr><td>%s</td><td>%s</td></tr>' % (f[0], f[1]) for f in cp['filas'])
        comp += '<div class="tabla-wrap"><table><tr><th>%s</th><th>%s</th></tr>%s</table></div>' % (cp['a'], cp['b'], filas)
        if cp.get('trampa'):
            comp += '<div class="box warn"><div class="box-title">⚠️ Trampa típica</div><p>%s</p></div>' % cp['trampa']
    s.append('<section class="section" data-sec="3"><span class="eyebrow">Sección 4 · Comparaciones</span>'
             '<h2 class="sec-title">⚖️ No los confundas</h2><p>%s</p>%s</section>'
             % (d.get('comparaciones_intro', 'Estos conceptos se parecen y por eso la CNSC los usa para confundir. Tenlos claros.'), comp))
    # 4 Casos
    casos = ''
    for c in d.get('casos', []):
        casos += ('<div class="caso"><div class="caso-head">📂 %s</div><div class="caso-body">'
                  '<span class="label">Situación</span><p>%s</p>'
                  '<span class="label">Pregunta</span><p>%s</p>'
                  '<span class="label">Respuesta</span><div class="resp-correcta">%s</div></div></div>'
                  % (c['titulo'], c['situacion'], c['pregunta'], c['respuesta']))
    s.append('<section class="section" data-sec="4"><span class="eyebrow">Sección 5 · Casos</span>'
             '<h2 class="sec-title">📂 Casos tipo CNSC resueltos</h2><p>%s</p>%s</section>'
             % (d.get('casos_intro', 'Situaciones reales del día a día, resueltas paso a paso.'), casos))
    # 5 Errores
    errs = ''.join('<div class="box danger"><div class="box-title">❌ %s</div><p><strong>Por qué falla:</strong> %s <strong>Corrige:</strong> %s</p></div>'
                   % (e['titulo'], e['porque'], e['corrige']) for e in d.get('errores', []))
    s.append('<section class="section" data-sec="5"><span class="eyebrow">Sección 6 · Errores frecuentes</span>'
             '<h2 class="sec-title">⚠️ Errores que debes evitar</h2>%s</section>' % errs)
    # 6 Tips
    tips = ''.join('<div class="box ok"><div class="box-title">✅ %s</div><p>%s</p></div>'
                   % (t['titulo'], t['texto']) for t in d.get('tips', []))
    s.append('<section class="section" data-sec="6"><span class="eyebrow">Sección 7 · Tips</span>'
             '<h2 class="sec-title">💡 Trucos para dominar el tema</h2>%s</section>' % tips)
    # 7 Trampas
    tr = ''.join('<div class="trampa"><div class="trampa-q">%s</div><div class="trampa-detail">'
                 '<div class="t-row parece">%s</div><div class="t-row malo">%s</div><div class="t-row bueno">%s</div></div></div>'
                 % (t['q'], t['parece'], t['malo'], t['bueno']) for t in d.get('trampas', []))
    s.append('<section class="section" data-sec="7"><span class="eyebrow">Sección 8 · Trampas</span>'
             '<h2 class="sec-title">🎭 Las trampas favoritas de la CNSC</h2>%s</section>' % tr)
    # 8 Repaso (shell fijo)
    s.append('<section class="section" data-sec="8"><span class="eyebrow">Sección 9 · Repaso</span>'
             '<h2 class="sec-title">🧠 Repasa con flashcards</h2><p>Toca la tarjeta para ver la respuesta. Repásalas hasta responderlas sin dudar.</p>'
             '<div class="flashcard-wrap"><div id="flashcard" class="flashcard">'
             '<div class="flash-face flash-front"><span class="flash-tag">Pregunta</span><p id="flashFront"></p><small class="flash-hint">Toca para ver la respuesta</small></div>'
             '<div class="flash-face flash-back"><span class="flash-tag">Respuesta</span><p id="flashBack"></p></div></div>'
             '<div class="flash-controls"><button id="flashPrev">← Anterior</button><span id="flashCounter">Tarjeta 1 de 10</span>'
             '<button id="flashFlip">Voltear</button><button id="flashNext">Siguiente →</button></div></div></section>')
    # 9 Resumen + glosario
    res = ''.join('<div class="resumen-item"><h4>%s</h4><p>%s</p></div>' % (r['h'], r['p']) for r in d.get('resumen', []))
    glo = ''.join('<dt>%s</dt><dd>%s</dd>' % (g['t'], g['d']) for g in d.get('glosario', []))
    s.append('<section class="section" data-sec="9"><span class="eyebrow">Sección 10 · Resumen</span>'
             '<h2 class="sec-title">📝 Resumen y glosario</h2><div class="resumen">%s</div>'
             '<h3 style="font-family:\'Source Serif 4\',serif;color:var(--azul);margin:24px 0 8px;">Glosario</h3>'
             '<dl class="glosario">%s</dl>'
             '<div class="box gold"><div class="box-title">💎 Para recordar</div><p>%s</p></div></section>'
             % (res, glo, d.get('para_recordar', '')))
    # 10 Simulacro (shell fijo; los datos van en el array preguntas)
    sim = d['simulacro']
    nb = sum(1 for p in sim if p['nivel'] == 'b')
    ni = sum(1 for p in sim if p['nivel'] == 'i')
    na = sum(1 for p in sim if p['nivel'] == 'a')
    s.append('<section class="section" data-sec="10"><span class="eyebrow">Sección 11 · Simulacro</span>'
             '<h2 class="sec-title">🎓 Simulacro tipo CNSC</h2>'
             '<div class="card card-lead quiz-intro"><p><strong>Formato CNSC — juicio situacional:</strong> cada pregunta presenta un caso real y te pide la actuación más apropiada, con 4 opciones (A, B, C, D); solo una es correcta. Al elegir, te explicamos por qué cada opción es correcta o incorrecta.</p>'
             '<div class="dific-tags"><span class="tag b">%d básicas</span><span class="tag i">%d intermedias</span><span class="tag a">%d avanzadas</span></div></div>'
             '<div id="quiz"></div>'
             '<div style="text-align:center;margin:28px 0;"><button id="btnCalcular" class="btn">Ver mi resultado</button></div>'
             '<div id="resultado"><div class="score-num" id="scoreNum">0/%d</div><p id="scoreMsg"></p><div id="temasReforzar"></div>'
             '<button id="btnReiniciar" class="btn gold">🔄 Repetir simulacro</button></div></section>'
             % (nb, ni, na, len(sim)))
    return '\n'.join(s)


def validar(d):
    """Valida que el contenido esté completo y correcto. Devuelve (errores, avisos)."""
    err, warn = [], []
    req = ['codigo', 'archivo', 'titulo', 'dia', 'familia', 'categoria', 'header_sub',
           'tiempo', 'proxima', 'objetivo', 'importancia', 'desarrollo', 'simulacro', 'flashcards']
    for k in req:
        if k not in d:
            err.append('Falta el campo obligatorio: %s' % k)
    # Desarrollo
    de = d.get('desarrollo', {})
    if de.get('temas'):
        temas = de['temas']
        if len(temas) < 4:
            warn.append('Hay %d temas en el desarrollo (recomendado 5-7)' % len(temas))
        for t in temas:
            if not t.get('titulo'):
                err.append('Hay un tema sin título')
            for b in t.get('bloques', []):
                if b.get('tipo') == 'minicheck' and not any(o.get('ok') for o in b.get('opciones', [])):
                    err.append('Minicheck sin opción correcta en el tema "%s"' % t.get('titulo', '?'))
    else:
        cps = de.get('conceptos', [])
        if len(cps) < 5:
            warn.append('Hay %d conceptos (recomendado 6-8, mínimo 5)' % len(cps))
        for i, c in enumerate(cps, 1):
            if not c.get('def') or not c.get('apl'):
                err.append('Concepto %d sin def/apl' % i)
            cp = c.get('checkpoint')
            if cp and not any(o.get('ok') for o in cp.get('opciones', [])):
                err.append('Checkpoint del concepto %d no tiene opción correcta' % i)
    if not de.get('fuentes', {}).get('items'):
        warn.append('Desarrollo sin enlaces a fuentes (.fuentes)')
    # Conteos recomendados
    for campo, ideal in [('casos', 5), ('errores', 6), ('tips', 6), ('trampas', 4), ('flashcards', 10), ('resumen', 6), ('glosario', 6)]:
        n = len(d.get(campo, []))
        if n != ideal:
            warn.append('%s: hay %d (recomendado %d)' % (campo, n, ideal))
    # Simulacro
    sim = d.get('simulacro', [])
    if len(sim) != 12:
        err.append('El simulacro tiene %d preguntas (deben ser 12)' % len(sim))
    nb = sum(1 for p in sim if p.get('nivel') == 'b')
    ni = sum(1 for p in sim if p.get('nivel') == 'i')
    na = sum(1 for p in sim if p.get('nivel') == 'a')
    if (nb, ni, na) != (4, 5, 3):
        err.append('Distribución del simulacro %d-%d-%d (debe ser 4-5-3)' % (nb, ni, na))
    for i, p in enumerate(sim, 1):
        if len(p.get('ops', [])) != 4:
            err.append('Pregunta %d no tiene 4 opciones' % i)
        if len(p.get('expl', [])) != 4:
            err.append('Pregunta %d no tiene 4 explicaciones (una por opción)' % i)
        if not isinstance(p.get('correcta'), int) or not (0 <= p.get('correcta', -1) <= 3):
            err.append('Pregunta %d: "correcta" inválida (debe ser 0-3)' % i)
        ctx = p.get('ctx', '')
        if not ctx:
            err.append('Pregunta %d sin contexto (ctx)' % i)
        elif len(ctx) < 200:
            warn.append('Pregunta %d: contexto corto (%d caracteres). Tipo CNSC pide un caso largo y verosímil (ideal ≥ 220).' % (i, len(ctx)))
        # Las opciones del simulacro no deben ser triviales (muy cortas) ni calcadas entre sí
        ops = p.get('ops', [])
        if ops and len(set(ops)) != len(ops):
            err.append('Pregunta %d: tiene opciones repetidas' % i)
        if ops and any(len(o) < 12 for o in ops):
            warn.append('Pregunta %d: alguna opción es muy corta; los distractores deben ser plausibles.' % i)
    # Patrón obvio de respuestas (todas iguales)
    corr = [p.get('correcta') for p in sim]
    if len(set(corr)) == 1:
        err.append('Todas las respuestas correctas son iguales (patrón obvio)')
    return err, warn


def construir(json_path):
    with open(json_path, encoding='utf-8') as fh:
        d = json.load(fh)

    err, warn = validar(d)
    for w in warn:
        print('  ⚠️  %s' % w)
    if err:
        print('  ❌ ERRORES en %s:' % os.path.basename(json_path))
        for e in err:
            print('     - %s' % e)
        raise SystemExit('Corrige los errores antes de generar la guía.')

    with open(os.path.join(BASE_DIR, 'base-guia.html'), encoding='utf-8') as fh:
        base = fh.read()

    badges = ('<span class="badge">📅 Día %s de 21</span>'
              '<span class="badge">⏱ %s</span>'
              '<span class="badge">🎯 Prueba escrita CNSC</span>'
              '<span class="badge">🔁 Familia %s</span>') % (d['dia'], d['tiempo'], d['familia'])
    footer = '%s · Día %s · Biblioteca Funcional (familia %s) · v1.0<br>Material de preparación independiente. No afiliado a la CNSC.' % (
        d['codigo'], d['dia'], d['familia'])
    finalizar = {
        'boton': '✅ Finalizar Día %s' % d['dia'],
        'alerta': '¡Felicitaciones! Terminaste el Día %s · %s.\n\nSigue con %s.' % (d['dia'], d['codigo'], d['proxima'])
    }

    html = base
    repl = {
        '{{TITLE}}': '%s · %s — Ascenso Público' % (d['codigo'], d['titulo']),
        '{{DOC_REF}}': d['codigo'],
        '{{KICKER}}': d['categoria'],
        '{{H1}}': d['titulo'],
        '{{HEADER_SUB}}': d['header_sub'],
        '{{BADGES}}': badges,
        '{{FOOTER_META}}': footer,
        '{{FINALIZAR_MSG}}': json.dumps(finalizar, ensure_ascii=False),
        '{{FLASHCARDS}}': json.dumps(d['flashcards'], ensure_ascii=False),
        '{{PREGUNTAS}}': json.dumps(d['simulacro'], ensure_ascii=False),
        '{{MAIN}}': build_main(d),
    }
    for k, v in repl.items():
        html = html.replace(k, v)

    out_path = os.path.join(REPO_DIR, 'guias', d['archivo'])
    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print('OK -> guias/%s (%d KB)' % (d['archivo'], len(html.encode('utf-8')) // 1024))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python3 motor/construir_guia.py motor/contenido/<CODIGO>.json')
        sys.exit(1)
    construir(sys.argv[1])
