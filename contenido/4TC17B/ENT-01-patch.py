# -*- coding: utf-8 -*-
"""Día 1 (2.ª guía) · Conoce tu entidad — Técnico en Criminalística 4TC-17 (División de Gestión Humana, Conv. 285-2026).

Parte de la base neutra bases/pgn/Profesional/ENT-01.html y la reenfoca a la
División de Gestión Humana y al nivel técnico.
Ejecutar:  python3 contenido/4TC17B/ENT-01-patch.py
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

GUIA = 'ENT-PGN-4TC17B-01'
DEST = f'guias/{GUIA}-conoce-entidad-pgn.html'
s = open('bases/pgn/Profesional/ENT-01.html', encoding='utf-8').read()

# --- identidad ---
s = (s.replace('{{GUIA}}', GUIA).replace('{{CARGO}}', 'Técnico en Criminalística')
      .replace('{{COD}}', '4TC-17').replace('{{CONV}}', '285-2026').replace('{{DIA}}', '1'))

R = []

# 1. Nivel del cargo en la bienvenida
R.append(('para un cargo del <strong>nivel profesional</strong> en la <strong>Procuraduría General de la Nación</strong>',
          'para un cargo del <strong>nivel técnico</strong> en la <strong>Procuraduría General de la Nación</strong>'))

# 2. Imparcialidad: aterrizada a quien tramita asuntos de personal
R.append(('Quien instruye un proceso disciplinario debe buscar la verdad recaudando tanto la prueba que incrimina como la que favorece',
          'Quien tramita un asunto de personal debe verificar los soportes con el mismo rigor, favorezcan o no al interesado'))

# 3. Ley 2094: qué significa para un cargo de soporte administrativo
R.append(('Para tu cargo esto es decisivo: la fase de <strong>instrucción</strong>',
          'Para tu cargo esto importa porque la historia laboral que custodias es la fuente de los antecedentes del servidor, y porque la fase de <strong>instrucción</strong>'))

# 4. El día a día: División de Gestión Humana en lugar de Procuradurías de Instrucción
R.append(('''<div class="bt">💡 El día a día en las Procuradurías de Instrucción</div>
      <p>En las <strong>Procuradurías de Instrucción</strong> el trabajo gira principalmente en torno a las funciones <strong>disciplinaria</strong> y <strong>preventiva</strong>: se estudian expedientes, se practican y recaudan pruebas, se proyectan autos y decisiones para consideración del funcionario competente, se resuelven recursos e impedimentos, se tramitan segundas instancias y grados de consulta, y se elaboran advertencias y exhortos preventivos. Todas las funciones convergen en la misma meta: que el Estado funcione con integridad.</p>''',
          '''<div class="bt">💡 El día a día en la División de Gestión Humana</div>
      <p>En la <strong>División de Gestión Humana</strong> el trabajo no es misional: es el <strong>soporte</strong> que hace posible lo misional. Allí se conservan las hojas de vida, la nómina, los salarios y las prestaciones y se expiden certificaciones; se tramitan las novedades y las situaciones administrativas y las afiliaciones a EPS y pensiones; se verifican los requisitos de quienes van a posesionarse y se emite el concepto escrito previo; se elaboran las nóminas; se apoya a la Comisión de Carrera; y se preparan los actos de personal para la firma del Procurador General. Todas las tareas convergen en la misma meta: que la entidad tenga <mark>servidores bien vinculados, bien pagados y con su situación en orden</mark> para ejercer el control que la Constitución le encarga.</p>'''))

# 5. Estructura: agregar la División de Gestión Humana a la lista de dependencias
R.append(('''<div class="linea"><div class="em">🏛️</div><h3>Procuradurías de Instrucción</h3>''',
          '''<div class="linea"><div class="em">👥</div><h3>Secretaría General y División de Gestión Humana</h3><p>El <strong>artículo 2 del Decreto Ley 262 de 2000</strong> ubica en el nivel central, bajo el numeral <strong>1.6</strong>, a la <strong>Secretaría General</strong>, y debajo de ella tres divisiones: <strong>Gestión Humana (1.6.1)</strong>, Administrativa (1.6.2) y Financiera (1.6.3). La División de Gestión Humana administra el talento humano de la entidad y sus funciones están en el <strong>artículo 63</strong>. <strong>Es la dependencia de tu cargo.</strong> No la confundas con la Dirección Nacional de Investigaciones Especiales, que sí depende del Despacho del Procurador y está regulada en el artículo 10.</p></div>
      <div class="linea"><div class="em">🏛️</div><h3>Procuradurías de Instrucción</h3>'''))

# 6. Transparencia y reserva: ajustar la frase del cargo
R.append(('tu cargo proyecta respuestas a derechos de petición y maneja información sujeta a reserva',
          'tu cargo proyecta documentos para la firma del funcionario competente y maneja información sujeta a reserva'))

# 7. TU LUGAR: jerarquía propia del División de Gestión Humana
R.append(('''<p>Como servidor del <strong>nivel profesional</strong> en una Procuraduría de Instrucción, te ubicarás en el equipo que impulsa y proyecta las actuaciones disciplinarias y preventivas de la dependencia. Así se ve la jerarquía simplificada de tu entorno de trabajo:</p>''',
          '''<p>Como servidor del <strong>nivel técnico</strong> en la División de Gestión Humana, te ubicarás en el equipo que <strong>verifica, tramita y proyecta</strong> los actos con los que la entidad vincula, mueve, paga y retira a su personal. Así se ve la jerarquía simplificada de tu entorno de trabajo:</p>'''))

R.append(('''<div class="txt"><h4>Procurador (Distrital / Provincial de Instrucción)</h4><p>Titular de la dependencia. Adopta las decisiones de fondo del proceso disciplinario y dirige la actuación.</p></div>''',
          '''<div class="txt"><h4>Secretario General</h4><p>Depende directamente del Procurador General. Dirige y coordina el soporte administrativo, humano y financiero de la entidad, y reconoce vacaciones, licencias, comisiones de servicio, prestaciones sociales y viáticos (art. 62).</p></div>
      <div class="txt"><h4>Jefe de la División de Gestión Humana</h4><p>Dirige la dependencia. Posesiona en el nivel central los empleos profesionales, técnicos, administrativos y operativos, concede los permisos de estudio de hasta dos horas diarias y responde por las funciones del artículo 63.</p></div>'''))

R.append(('''<div class="txt"><h4>Profesional del nivel profesional — Tú estás aquí</h4><p>Evalúa la actuación disciplinaria, practica y recauda pruebas en la instrucción, proyecta autos y decisiones para consideración del jefe, resuelve recursos e impedimentos y ejecuta acciones preventivas.</p></div>''',
          '''<div class="txt"><h4>Técnico en Criminalística 4TC-17 — Tú estás aquí</h4><p>Realiza las actividades relativas a <strong>movimientos de personal</strong> y <strong>elabora los actos administrativos según los modelos y procedimientos establecidos</strong>; verifica los soportes de los trámites; examina informes en cuanto a la pertinencia e idoneidad de los métodos y las técnicas de su especialidad; lleva el <strong>control de la correspondencia</strong> asignada; y apoya el <strong>archivo</strong> de los documentos de la dependencia, en especial las historias laborales.</p></div>'''))

R.append(('''<div class="txt"><h4>Personal técnico y de apoyo</h4><p>Notifica, registra actuaciones en los sistemas de información y brinda soporte administrativo a la labor de la dependencia.</p></div>''',
          '''<div class="txt"><h4>Personal administrativo y de apoyo</h4><p>Notifica, radica y registra actuaciones en los sistemas de información, custodia el archivo y brinda el soporte administrativo que necesita la dependencia.</p></div>'''))

R.append(('''<p>El profesional del nivel profesional es quien <strong>da forma jurídica al proceso disciplinario</strong>: estudia el expediente, recauda la prueba, califica provisionalmente la conducta y proyecta la decisión con criterio técnico. La decisión de fondo la firma el funcionario competente, pero la calidad de tu proyecto y de la prueba que recaudes <strong>determina la solidez del caso</strong>. Actúas con autonomía técnica, dentro de los límites del debido proceso.</p>''',
          '''<p>El Técnico en Criminalística 4TC-17 es quien <strong>construye el soporte de cada acto de personal</strong>: verifica que los documentos acrediten lo que dicen acreditar, deja constancia escrita de lo verificado, proyecta el acto conforme al modelo y controla el término. No concede, no reconoce y <strong>no firma</strong> —eso corresponde al jefe de la División, a la Secretaría General o al Procurador General, según el asunto—, pero de la exactitud de su verificación depende que un nombramiento se sostenga, que una prestación se reconozca sobre la base correcta y que la nómina pague lo que debe pagar. Actúa con rigor técnico, dentro de los límites del debido proceso administrativo y del alcance de su cargo.</p>'''))

# 8. Resumen final
R.append(('En una Procuraduría de Instrucción priman la disciplinaria y la preventiva.',
          'En la División de Gestión Humana el trabajo no es misional: es el soporte de talento humano que hace posibles las tres funciones misionales.'))

R.append(('''4) En el proceso disciplinario, quien instruye <strong>recauda prueba y proyecta con criterio</strong>''',
          '''4) En la gestión del talento humano, el técnico en criminalística <strong>verifica los soportes, tramita las novedades y proyecta los actos para la firma del competente</strong>'''))

faltan = [a for a, _ in R if a not in s]
if faltan:
    print('NO SE ENCONTRARON estos fragmentos:'); [print(' -', f[:90]) for f in faltan]; sys.exit(1)
for a, b in R:
    s = s.replace(a, b, 1)

# --- encabezado y pie ---
s = re.sub(r'<p class="header-sub">.*?</p>',
           '<p class="header-sub">Antes de estudiar los temas del cargo, conozcamos la entidad a la que vas a llegar: qué es la Procuraduría, qué hace, cómo está organizada, qué normas la rigen, qué es la <strong>División de Gestión Humana</strong>, de quién depende y por qué tu trabajo de soporte va a importar.</p>',
           s, count=1, flags=re.S)

assert '{{' not in s
open(DEST, 'w', encoding='utf-8').write(s)
print(DEST, len(s), 'bytes')
