# -*- coding: utf-8 -*-
"""Día 1 (2.ª guía) · Conoce tu entidad — Técnico Investigador 4TI-15 (DNIE, Conv. 257-2026).

Parte de la base neutra bases/pgn/Profesional/ENT-01.html y la reenfoca a la
Dirección Nacional de Investigaciones Especiales y al nivel técnico.
Ejecutar:  python3 contenido/4TI15O/ENT-01-patch.py
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

GUIA = 'ENT-PGN-4TI15O-01'
DEST = f'guias/{GUIA}-conoce-entidad-pgn.html'
s = open('bases/pgn/Profesional/ENT-01.html', encoding='utf-8').read()

# --- identidad ---
s = (s.replace('{{GUIA}}', GUIA).replace('{{CARGO}}', 'Técnico Investigador')
      .replace('{{COD}}', '4TI-15').replace('{{CONV}}', '257-2026').replace('{{DIA}}', '1'))

R = []

# 1. Nivel del cargo en la bienvenida
R.append(('para un cargo del <strong>nivel profesional</strong> en la <strong>Procuraduría General de la Nación</strong>',
          'para un cargo del <strong>nivel técnico</strong> en la <strong>Procuraduría General de la Nación</strong>'))

# 2. Imparcialidad: de "quien instruye" a "quien recauda la prueba"
R.append(('Quien instruye un proceso disciplinario debe buscar la verdad recaudando tanto la prueba que incrimina como la que favorece',
          'Quien recauda la prueba en un proceso disciplinario debe buscar la verdad reuniendo tanto lo que incrimina como lo que favorece'))

# 3. Ley 2094: qué significa para un cargo de apoyo probatorio
R.append(('Para tu cargo esto es decisivo: la fase de <strong>instrucción</strong>',
          'Para tu cargo esto es decisivo, porque el apoyo técnico se presta sobre todo en la fase de <strong>instrucción</strong>'))

# 4. El día a día: DNIE en lugar de Procuradurías de Instrucción
R.append(('''<div class="bt">💡 El día a día en las Procuradurías de Instrucción</div>
      <p>En las <strong>Procuradurías de Instrucción</strong> el trabajo gira principalmente en torno a las funciones <strong>disciplinaria</strong> y <strong>preventiva</strong>: se estudian expedientes, se practican y recaudan pruebas, se proyectan autos y decisiones para consideración del funcionario competente, se resuelven recursos e impedimentos, se tramitan segundas instancias y grados de consulta, y se elaboran advertencias y exhortos preventivos. Todas las funciones convergen en la misma meta: que el Estado funcione con integridad.</p>''',
          '''<div class="bt">💡 El día a día en la Dirección Nacional de Investigaciones Especiales</div>
      <p>En la <strong>Dirección Nacional de Investigaciones Especiales (DNIE)</strong> el trabajo gira en torno a la función <strong>disciplinaria</strong> y al <strong>apoyo técnico-científico</strong>: se adelantan las indagaciones e investigaciones que asigna o delega el Procurador General, se practican pruebas técnicas, se recaudan y aseguran elementos materiales probatorios, se elaboran informes técnicos y se apoya a las demás dependencias de la PGN y a los otros órganos del Ministerio Público. Todas las tareas convergen en la misma meta: que la decisión disciplinaria se apoye en <mark>prueba sólida y bien obtenida</mark>.</p>'''))

# 5. Estructura: agregar la DNIE a la lista de dependencias
R.append(('''<div class="linea"><div class="em">🏛️</div><h3>Procuradurías de Instrucción</h3>''',
          '''<div class="linea"><div class="em">🔬</div><h3>Dirección Nacional de Investigaciones Especiales</h3><p>Adscrita al Despacho del Procurador General (art. 10 del Decreto Ley 262 de 2000). Adelanta las indagaciones e investigaciones que le asignan o delegan, presta asesoría y apoyo técnico-científico a las demás dependencias y a los otros órganos del Ministerio Público, y <strong>ejerce funciones de policía judicial</strong>. Es la dependencia de tu cargo.</p></div>
      <div class="linea"><div class="em">🏛️</div><h3>Procuradurías de Instrucción</h3>'''))

# 6. Transparencia y reserva: ajustar la frase del cargo
R.append(('tu cargo proyecta respuestas a derechos de petición y maneja información sujeta a reserva',
          'tu cargo proyecta documentos para la firma del funcionario competente y maneja información sujeta a reserva'))

# 7. TU LUGAR: jerarquía propia del DNIE
R.append(('''<p>Como servidor del <strong>nivel profesional</strong> en una Procuraduría de Instrucción, te ubicarás en el equipo que impulsa y proyecta las actuaciones disciplinarias y preventivas de la dependencia. Así se ve la jerarquía simplificada de tu entorno de trabajo:</p>''',
          '''<p>Como servidor del <strong>nivel técnico</strong> en la Dirección Nacional de Investigaciones Especiales, te ubicarás en el equipo que <strong>produce y asegura la prueba técnica</strong> con la que otras dependencias y la propia Dirección sustentan sus decisiones. Así se ve la jerarquía simplificada de tu entorno de trabajo:</p>'''))

R.append(('''<div class="txt"><h4>Procurador (Distrital / Provincial de Instrucción)</h4><p>Titular de la dependencia. Adopta las decisiones de fondo del proceso disciplinario y dirige la actuación.</p></div>''',
          '''<div class="txt"><h4>Director Nacional de Investigaciones Especiales</h4><p>Titular de la dependencia. Dirige las investigaciones asignadas o delegadas, responde ante el Procurador General y es el servidor competente que delega las funciones de policía judicial.</p></div>'''))

R.append(('''<div class="txt"><h4>Profesional del nivel profesional — Tú estás aquí</h4><p>Evalúa la actuación disciplinaria, practica y recauda pruebas en la instrucción, proyecta autos y decisiones para consideración del jefe, resuelve recursos e impedimentos y ejecuta acciones preventivas.</p></div>''',
          '''<div class="txt"><h4>Técnico Investigador 4TI-15 — Tú estás aquí</h4><p>Acuerda la metodología de la investigación con la dependencia que pide el apoyo, practica pruebas técnicas, recauda y asegura elementos materiales probatorios con cadena de custodia, elabora informes técnicos y los presenta con sus anexos, y proyecta autos, conceptos y actos administrativos para la firma del funcionario competente.</p></div>'''))

R.append(('''<div class="txt"><h4>Personal técnico y de apoyo</h4><p>Notifica, registra actuaciones en los sistemas de información y brinda soporte administrativo a la labor de la dependencia.</p></div>''',
          '''<div class="txt"><h4>Personal administrativo y de apoyo</h4><p>Notifica, radica y registra actuaciones en los sistemas de información, custodia el archivo y brinda el soporte administrativo que necesita la dependencia.</p></div>'''))

R.append(('''<p>El profesional del nivel profesional es quien <strong>da forma jurídica al proceso disciplinario</strong>: estudia el expediente, recauda la prueba, califica provisionalmente la conducta y proyecta la decisión con criterio técnico. La decisión de fondo la firma el funcionario competente, pero la calidad de tu proyecto y de la prueba que recaudes <strong>determina la solidez del caso</strong>. Actúas con autonomía técnica, dentro de los límites del debido proceso.</p>''',
          '''<p>El Técnico Investigador es quien <strong>construye el soporte probatorio del proceso disciplinario</strong>: define con la dependencia la metodología, practica la prueba técnica, asegura cada elemento con su cadena de custodia y lo documenta en un informe que cualquiera pueda verificar. No califica la falta ni firma la decisión de fondo —eso corresponde al funcionario competente—, pero la calidad de lo que usted recaude <strong>determina si el caso se sostiene o se cae</strong>. Actúa con rigor técnico, dentro de los límites del debido proceso y del alcance de su cargo.</p>'''))

# 8. Resumen final
R.append(('En una Procuraduría de Instrucción priman la disciplinaria y la preventiva.',
          'En la Dirección Nacional de Investigaciones Especiales el trabajo se concentra en la disciplinaria y en el apoyo técnico-científico.'))

R.append(('''4) En el proceso disciplinario, quien instruye <strong>recauda prueba y proyecta con criterio</strong>''',
          '''4) En el proceso disciplinario, el técnico investigador <strong>recauda y asegura la prueba y proyecta documentos con rigor técnico</strong>'''))

faltan = [a for a, _ in R if a not in s]
if faltan:
    print('NO SE ENCONTRARON estos fragmentos:'); [print(' -', f[:90]) for f in faltan]; sys.exit(1)
for a, b in R:
    s = s.replace(a, b, 1)

# --- encabezado y pie ---
s = re.sub(r'<p class="header-sub">.*?</p>',
           '<p class="header-sub">Antes de estudiar los temas del cargo, conozcamos la entidad a la que vas a llegar: qué es la Procuraduría, qué hace, cómo está organizada, qué normas la rigen, qué es la <strong>Dirección Nacional de Investigaciones Especiales</strong> y por qué tu trabajo técnico va a importar.</p>',
           s, count=1, flags=re.S)

assert '{{' not in s
open(DEST, 'w', encoding='utf-8').write(s)
print(DEST, len(s), 'bytes')
