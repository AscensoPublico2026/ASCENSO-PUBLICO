# -*- coding: utf-8 -*-
"""Día 11 · CGD I: sujetos, deberes, faltas, ilicitud sustancial y culpabilidad — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-DIS-4TI15O-01',
    archivo='FUN-DIS-4TI15O-01-codigo-general-disciplinario-fundamentos.html',
    dia=11,
    titulo_doc='Código General Disciplinario I: fundamentos',
    h1='Código General Disciplinario I<br>Fundamentos',
    kicker='Día 11 · Conocimientos específicos',
    sub='El marco sustantivo que enmarca todo lo que recolectas: la <strong>Ley 1952 de 2019</strong> y su modificación por la <strong>Ley 2094 de 2021</strong>, los <strong>principios rectores</strong>, los <strong>sujetos disciplinables</strong>, la <strong>falta disciplinaria</strong> y sus elementos, la <strong>ilicitud sustancial</strong>, el <strong>dolo y la culpa</strong>, las causales de exclusión de responsabilidad y las sanciones. Saber qué es una falta y qué la hace sustancialmente ilícita es lo que te permite entender <em>qué</em> debe acreditar la prueba que tú practicas —sin calificarla tú, que es el límite de tu rol.',
    badges=['⏱ 100-120 min', '⚖️ CGD', '🧩 Fundamentos'],
    fmeta='Código General Disciplinario (Ley 1952 de 2019, modificada por la Ley 2094 de 2021): fundamentos',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Código General Disciplinario I: fundamentos',
)

FUENTE = 'guias/FUN-DIS-4SU11-01-derecho-disciplinario-fundamentos.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- bloques nuevos
MOD_ROL = (
    '<h3><span class="h3-chip">12</span> El rol del Técnico Investigador frente al derecho '
    'disciplinario: probar los hechos, nunca calificarlos</h3>\n'
    '  <h4>El módulo más importante de esta guía para tu día a día</h4>\n'
    '  <p>Todo lo estudiado hasta aquí —principios, sujetos, faltas, ilicitud sustancial, culpabilidad, '
    'sanciones— es el marco conceptual que necesitas dominar para ejercer con criterio tu función real. '
    'Pero conviene decir desde ya para qué te sirve: <strong>no para calificar</strong>, sino para '
    '<strong>saber qué hay que probar</strong>. Si no entiendes qué elementos configuran una falta, no '
    'puedes orientar bien la metodología de una prueba técnica ni saber qué debe quedar documentado en '
    'tu informe para que sirva.</p>\n'
    '  <p>El alcance exacto de tu función, conforme a tu manual, es: <strong>apoyar las actividades '
    'técnicas, técnico científicas y administrativas de investigación para la recolección de material '
    'probatorio</strong>, <strong>practicar pruebas técnicas previa delegación del servidor '
    'competente</strong>, <strong>elaborar informes técnicos</strong>, <strong>presentar las pruebas '
    'practicadas y sus anexos</strong> y <strong>proyectar</strong> autos, conceptos y actos '
    'administrativos para la firma de quien decide. Dicho en una línea: <mark>tú construyes el soporte '
    'probatorio; otro lo valora jurídicamente</mark>.</p>\n'
    '  <p>Esto significa, en términos concretos, que un Técnico Investigador <strong>sí describe</strong> '
    'con todo detalle qué observó, con qué método y con qué resultado, y <strong>sí proyecta</strong> el '
    'borrador de un auto o un concepto cuando se le pide. Pero <strong>nunca escribe que el servidor '
    'incurrió en una falta</strong>, nunca afirma que la conducta fue dolosa o culposa, nunca sostiene '
    'que hubo ilicitud sustancial y nunca propone la sanción. Esas cuatro son calificaciones jurídicas '
    'que corresponden al servidor competente.</p>\n'
    '  <div class="tabla-wrap">\n'
    '    <table>\n'
    '      <thead><tr><th>Actuación</th><th>¿Le corresponde al Técnico Investigador?</th>'
    '<th>¿Quién decide y firma?</th></tr></thead>\n'
    '      <tbody>\n'
    '        <tr><td>Acordar la metodología del apoyo con la dependencia solicitante</td><td>Sí, es '
    'función expresa del manual</td><td>Se concreta con la dependencia que solicita el apoyo</td></tr>\n'
    '        <tr><td>Practicar la prueba técnica</td><td>Sí, <strong>previa delegación</strong> del '
    'servidor competente</td><td>La delegación proviene del servidor competente</td></tr>\n'
    '        <tr><td>Describir hechos, método y resultados en el informe técnico</td><td>Sí, es el '
    'núcleo de su función</td><td>Suscribe el informe técnico en calidad de quien lo elaboró</td></tr>\n'
    '        <tr><td>Afirmar que la conducta constituye falta y calificar su gravedad</td><td>No. Puede '
    'aportar los hechos ordenados y verificables</td><td>Servidor competente / operador '
    'disciplinario</td></tr>\n'
    '        <tr><td>Afirmar que hubo dolo o culpa, o que hubo ilicitud sustancial</td><td>No: son '
    'juicios de valoración jurídica</td><td>Servidor competente / operador disciplinario</td></tr>\n'
    '        <tr><td>Proyectar un auto o un concepto</td><td>Sí, como borrador</td><td>Lo revisa, ajusta '
    'y <strong>firma</strong> el servidor competente</td></tr>\n'
    '        <tr><td>Decidir la compulsa de copias a Fiscalía o Contraloría</td><td>No. Documenta el '
    'hecho y lo pone en conocimiento</td><td>Servidor competente</td></tr>\n'
    '      </tbody>\n'
    '    </table>\n'
    '  </div>\n'
    '  <div class="box danger">\n'
    '    <div class="box-title">🚫 Lo que un Técnico Investigador NUNCA hace</div>\n'
    '    <p>Nunca califica la falta ni su gravedad, nunca afirma dolo o culpa, nunca concluye que hubo '
    'ilicitud sustancial, nunca propone ni impone una sanción, nunca firma el fallo, nunca practica una '
    'prueba sin delegación y nunca amplía por su cuenta el objeto de lo delegado. Su función es '
    'construir y documentar el soporte probatorio, por delegación y con método verificable.</p>\n'
    '  </div>\n'
    '  <div class="box gold">\n'
    '    <div class="box-title">🎯 En la prueba</div>\n'
    '    <p>Cualquier opción que describa al Técnico Investigador «concluyendo que incurrió en la '
    'falta», «calificando la gravedad», «determinando el dolo» o «investigando de oficio sin delegación» '
    'es, casi con seguridad, un distractor. La opción correcta describirá siempre: <strong>describir, '
    'documentar y poner en conocimiento del competente</strong>.</p>\n'
    '  </div>\n'
    '  <h4>Para qué te sirve, entonces, saber qué es la ilicitud sustancial</h4>\n'
    '  <p>Justo para lo contrario de calificarla: para <strong>no dejar huecos en la prueba</strong>. Si '
    'la ilicitud sustancial exige que la conducta afecte sustancialmente el deber funcional, entonces el '
    'informe que solo describe el hecho aislado —sin documentar las condiciones, el contexto y las '
    'circunstancias verificables en que ocurrió— deja al competente sin los elementos para valorarla. '
    'Conocer el marco te dice <strong>qué documentar</strong>, no qué concluir. Esa es la diferencia '
    'entre un técnico que entiende el proceso y uno que solo sigue un protocolo.</p>'
)

R = [
    ('<h3><span class="h3-chip">12</span> El rol del Sustanciador frente al derecho disciplinario: apoyo en la proyección, nunca decisión</h3>\n  <h4>El módulo más importante de esta guía para tu día a día</h4>\n  <p>Todo lo estudiado hasta aquí —principios, sujetos, faltas, sanciones— es el marco conceptual que necesitas dominar para ejercer con criterio tu función real dentro de un despacho con competencia disciplinaria. Es fundamental que tengas absoluta claridad sobre el alcance exacto de esa función, conforme a la función 1 de tu manual: <strong>apoyar en la proyección de conceptos, providencias, solicitudes, constancias, recursos y todo aquello que guarde relación con el cumplimiento de las funciones de la dependencia</strong>, siempre <mark>bajo la supervisión del jefe de despacho</mark>, quien es la única persona que suscribe y decide.</p>',
     MOD_ROL + '\n  <h4>__VIEJO_12__</h4>'),
]
SEC = aplicar_todas(SEC, R, estricto=True)

# el resto del módulo 12 original (párrafos, tabla y cajas del Sustanciador) se elimina por bloques
BORRAR = [
    '<p>Esto significa, en términos concretos, que un Sustanciador <strong>sí redacta el borrador</strong> de un auto de trámite, de un proyecto de pliego de cargos o de una constancia dentro de un proceso disciplinario, con base en los hechos y las pruebas que constan en el expediente y siguiendo las instrucciones del jefe de despacho. Pero ese borrador es exactamente eso: un proyecto sujeto a la revisión, corrección y decisión final de quien tiene la competencia legal para decidir. El Sustanciador <strong>nunca decide de fondo, nunca falla, nunca impone una sanción, y nunca investiga de oficio de forma autónoma</strong> como si fuera el titular del proceso disciplinario. La titularidad de la función disciplinaria, dentro de cada despacho, corresponde al procurador o funcionario competente que dirige esa dependencia, no a quien apoya la sustanciación.</p>',
    '<div class="tabla-wrap">\n    <table>\n      <thead><tr><th>Actuación</th><th>¿La proyecta (redacta el borrador) el Sustanciador?</th><th>¿Quién decide y firma?</th></tr></thead>\n      <tbody>\n        <tr><td>Auto de trámite (traslados, requerimientos de información)</td><td>Sí, bajo instrucción y supervisión</td><td>Jefe de despacho</td></tr>\n        <tr><td>Proyecto de pliego de cargos</td><td>Sí, con base en el expediente y bajo supervisión estrecha</td><td>Jefe de despacho, quien lo revisa, ajusta y suscribe</td></tr>\n        <tr><td>Calificación de la gravedad de la falta</td><td>No decide; puede aportar elementos fácticos organizados</td><td>Jefe de despacho / operador disciplinario competente</td></tr>\n        <tr><td>Fallo disciplinario (sanción o absolución)</td><td>No decide ni proyecta el análisis de fondo decisorio</td><td>Jefe de despacho / operador disciplinario competente, exclusivamente</td></tr>\n        <tr><td>Constancias de vencimiento de términos</td><td>Sí, documentando el hecho objetivo</td><td>Se pone en conocimiento del jefe de despacho para lo de su competencia</td></tr>\n      </tbody>\n    </table>\n  </div>',
    '<div class="box danger">\n    <div class="box-title">🚫 Lo que un Sustanciador NUNCA hace</div>\n    <p>Nunca decide el fondo de un proceso disciplinario, nunca suscribe un fallo, nunca impone una sanción, nunca abre una investigación disciplinaria por iniciativa propia sin la instrucción y el conocimiento del jefe de despacho, y nunca ejerce la función disciplinaria como si fuera la titular del proceso. Su función es de apoyo técnico en la proyección, bajo supervisión constante.</p>\n  </div>',
    '<div class="box gold">\n    <div class="box-title">🎯 En la prueba</div>\n    <p>Cualquier opción de respuesta que describa al Sustanciador "decidiendo", "fallando", "imponiendo una sanción" o "investigando de oficio de forma autónoma" es, casi con seguridad, un distractor. La opción correcta describirá siempre una función de <strong>apoyo en la proyección, bajo supervisión del jefe de despacho</strong>.</p>\n  </div>',
    '\n  <h4>__VIEJO_12__</h4>',
]
SEC = aplicar_todas(SEC, [(b, '') for b in BORRAR], estricto=True)

SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>',
     '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>',
     '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('(4SU-11)', '(4TI-15)'),
    ('4SU-11', '4TI-15'),
    ('288-2026', '257-2026'),
    ('Resolución 243 de 2026', 'Resolución 212 de 2026'),
    ('apoya la sustanciación', 'apoya técnicamente'),
    ('la sustanciación', 'el apoyo técnico'),
    ('apoyo en la proyección', 'apoyo técnico probatorio'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)   # filtro antifugas final


# ---------------------------------------------------------------- calidad: interactividad y cierre
CP1 = ("""<div class="checkpoint" data-cp="1">
      <div class="cp-q">✋ Punto de control 1: el despacho le pide que el informe técnico concluya que la conducta «afectó sustancialmente el deber funcional». ¿Qué corresponde?</div>
      <div class="cp-opts">
      <button class="cp-opt" data-ans="0">Incluirlo, porque es una constatación objetiva que el técnico puede verificar con su método.</button>
      <button class="cp-opt" data-ans="1">No incluirlo y documentar en cambio las condiciones y circunstancias verificables del hecho, que es lo que permite al competente valorarlo.</button>
      <button class="cp-opt" data-ans="0">Incluirlo como apreciación técnica, aclarando que no compromete la decisión del despacho.</button>
      </div>
      <div class="cp-fb"></div>
    </div>""")

CP2 = ("""<div class="checkpoint" data-cp="2">
      <div class="cp-q">✋ Punto de control 2: ¿a quién alcanza la ley disciplinaria?</div>
      <div class="cp-opts">
      <button class="cp-opt" data-ans="0">Solo a los servidores públicos vinculados por nombramiento y posesión.</button>
      <button class="cp-opt" data-ans="0">A todo contratista del Estado por el solo hecho de haber suscrito un contrato.</button>
      <button class="cp-opt" data-ans="1">A los servidores públicos y, en los casos que la ley señala, a particulares: típicamente quienes ejercen funciones públicas o administran recursos del Estado.</button>
      </div>
      <div class="cp-fb"></div>
    </div>""")

CP3 = ("""<div class="checkpoint" data-cp="3">
      <div class="cp-q">✋ Punto de control 3: la Fiscalía archivó el proceso penal sobre los mismos hechos. ¿Qué efecto tiene en lo disciplinario?</div>
      <div class="cp-opts">
      <button class="cp-opt" data-ans="0">Obliga a archivar también el expediente disciplinario, por tratarse de los mismos hechos.</button>
      <button class="cp-opt" data-ans="1">Ninguno automático: las acciones son independientes, porque lo que se valora y el estándar aplicable son distintos.</button>
      <button class="cp-opt" data-ans="0">Suspende la actuación disciplinaria hasta que el archivo penal quede en firme.</button>
      </div>
      <div class="cp-fb"></div>
    </div>""")

CP4 = ("""<div class="checkpoint" data-cp="4">
      <div class="cp-q">✋ Punto de control 4: usted documenta una foliación alterada y el despacho le pide decir si fue dolo o descuido. ¿Qué hace?</div>
      <div class="cp-opts">
      <button class="cp-opt" data-ans="1">Describe con precisión qué se alteró y cómo, y se abstiene de afirmar la intención: el dolo y la culpa los valora el competente.</button>
      <button class="cp-opt" data-ans="0">Concluye que fue dolosa, porque una alteración no se explica por un descuido.</button>
      <button class="cp-opt" data-ans="0">Concluye que fue un descuido, por aplicación de la presunción de inocencia.</button>
      </div>
      <div class="cp-fb"></div>
    </div>""")

PR1 = ("""<div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Practicando una prueba técnica delegada usted documenta que un servidor no siguió un procedimiento interno. El despacho le pide que el informe diga que «incurrió en falta grave».</p>
    <p><strong>Cómo proceder.</strong> Describir qué procedimiento se omitió, cómo lo verificó, en qué condiciones ocurrió y qué registros lo acreditan. Nada de calificación. El competente necesita hechos verificables para valorar la ilicitud sustancial: dárselos es su trabajo; calificarla, no.</p>
  </div>""")

PR2 = ("""<div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> El investigado le muestra, durante la diligencia, una orden escrita de su superior que —dice— explica su conducta.</p>
    <p><strong>Cómo proceder.</strong> Dejar constancia de que el documento fue exhibido, describirlo objetivamente (fecha, firma, contenido visible) y ponerlo en conocimiento del competente. Si eso configura o no una causal de exclusión de responsabilidad es una valoración jurídica que no le corresponde.</p>
  </div>""")

PR3 = ("""<div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Un compañero le dice que el informe puede ser breve «porque el hecho es evidente y todos en la dependencia lo saben».</p>
    <p><strong>Cómo proceder.</strong> Sin prueba no hay falta demostrada, por evidente que parezca el hecho. El informe documenta método, hallazgos y condiciones. Un informe apoyado en lo que «todos saben» no sostiene ninguna decisión y deja la actuación expuesta en segunda instancia.</p>
  </div>""")

OJO1 = ("""<div class="ojo"><b>👁️ Ojo en la prueba</b><p>Cuando una pregunta mezcla el marco disciplinario con su rol, hay <strong>dos preguntas</strong> escondidas: qué dice el Código sobre el hecho, y qué de eso le corresponde a usted hacer. Muchas opciones describen correctamente el derecho y, aun así, son incorrectas porque le atribuyen una actuación que no es suya.</p></div>""")

OJO2 = ("""<div class="ojo"><b>👁️ Ojo en la prueba</b><p>Cuatro verbos son, casi siempre, señal de distractor cuando el sujeto es el Técnico Investigador: <strong>calificar</strong> la falta, <strong>determinar</strong> el dolo, <strong>concluir</strong> la ilicitud sustancial y <strong>proponer</strong> la sanción. Los cuatro son valoración jurídica del servidor competente.</p></div>""")

CIERRE = ("""<div class="box gold">
    <div class="box-title">💡 Idea clave del día</div>
    <p>El Código General Disciplinario no se estudia para calificar: se estudia para <strong>saber qué hay que probar</strong>. Conocer los elementos de la falta, la ilicitud sustancial y la culpabilidad es lo que le permite orientar bien la metodología de una prueba técnica y documentar lo que el competente necesita para valorar. Describir y documentar es su trabajo; calificar, no.</p>
  </div>
  <div class="box ok">
    <div class="box-title">🧠 Frase para recordar</div>
    <p>«Yo construyo el soporte probatorio; otro lo valora jurídicamente. Si entiendo qué configura la falta, sé qué documentar —no qué concluir.»</p>
  </div>
  <div class="fuentes"><div class="fuentes-tag">📚 Fuentes oficiales para profundizar</div>
    <ul class="lista">
      <li><a href="https://funcionpublica.gov.co/eva/gestornormativo/norma.php?i=90324" target="_blank" rel="noopener">Ley 1952 de 2019 — Código General Disciplinario</a></li>
      <li><a href="https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_2094_2021.htm" target="_blank" rel="noopener">Ley 2094 de 2021 — Reforma del Código General Disciplinario</a></li>
      <li><a href="https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1952_2019_pr003.htm" target="_blank" rel="noopener">Ley 1952 de 2019, arts. 115 y 116 — Reserva de la actuación y requisitos formales</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=4125" target="_blank" rel="noopener">Constitución Política de Colombia — arts. 6, 29, 209 y 277</a></li>
      <li><a href="https://www.procuraduria.gov.co/" target="_blank" rel="noopener">Procuraduría General de la Nación — sitio oficial</a></li>
    </ul>
  </div>""")

SEC = aplicar_todas(SEC, [
    ('<h3><span class="h3-chip">6</span> El concepto de falta disciplinaria y sus elementos</h3>',
     CP2 + '\n\n  <h3><span class="h3-chip">6</span> El concepto de falta disciplinaria y sus elementos</h3>'),
    ('<h3><span class="h3-chip">9</span> Causales de exclusión de responsabilidad</h3>',
     PR1 + '\n  ' + CP4 + '\n\n  <h3><span class="h3-chip">9</span> Causales de exclusión de responsabilidad</h3>'),
    ('<h3><span class="h3-chip">10</span> Las sanciones disciplinarias y su graduación</h3>',
     PR2 + '\n\n  <h3><span class="h3-chip">10</span> Las sanciones disciplinarias y su graduación</h3>'),
    ('<h3><span class="h3-chip">14</span> Reserva y confidencialidad en materia disciplinaria</h3>',
     CP3 + '\n  ' + OJO1 + '\n\n  <h3><span class="h3-chip">14</span> Reserva y confidencialidad en materia disciplinaria</h3>'),
    ('<h3><span class="h3-chip">22</span> Regímenes disciplinarios especiales: cuándo no se aplica el CGD general</h3>',
     PR3 + '\n  ' + CP1 + '\n\n  <h3><span class="h3-chip">22</span> Regímenes disciplinarios especiales: cuándo no se aplica el CGD general</h3>'),
    ('<h3><span class="h3-chip">25</span> Ejercicios resueltos: clasificar faltas y anticipar la sanción que corresponde</h3>',
     OJO2 + '\n\n  <h3><span class="h3-chip">25</span> Ejercicios resueltos: clasificar faltas y anticipar la sanción que corresponde</h3>'),
    ('<button class="btn-continuar" onclick="showSection(3)">Continuar →</button>',
     CIERRE + '\n\n  <button class="btn-continuar" onclick="showSection(3)">Continuar →</button>'),
], estricto=True)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre los fundamentos '
              'del Código General Disciplinario aplicados al trabajo del Técnico Investigador: sujetos disciplinables, '
              'elementos de la falta, ilicitud sustancial, culpabilidad, causales de exclusión, sanciones y —sobre '
              'todo— la frontera entre documentar los hechos y calificarlos.')

P = [
 (1,
  'Usted practicó una prueba técnica y documentó que un equipo institucional fue usado fuera del horario para fines ajenos al servicio. El despacho solicitante le pide que el informe «diga que hubo falta gravísima, porque el uso indebido de bienes del Estado lo es». Usted conoce el Código General Disciplinario y sabe que la calificación depende de elementos que no se agotan en el hecho que usted documentó. El informe vence mañana y el servidor del despacho insiste en que así se agiliza la decisión.',
  '¿Cómo debe redactar el informe?',
  ['Consignar que el hecho documentado constituye falta gravísima, ya que el propio Código tipifica el uso indebido de bienes del Estado y el técnico puede constatar esa correspondencia.',
   'Describir el hecho, el método aplicado y el resultado, con las circunstancias verificables en que ocurrió, y poner el hallazgo en conocimiento del competente, sin calificar la falta.',
   'Consignar que el hecho «podría constituir» una falta gravísima, de modo que la calificación quede planteada como hipótesis técnica sin comprometer la decisión final del despacho.',
   'Describir el hecho sin mencionar las circunstancias en que ocurrió, para que la calificación quede enteramente en manos del despacho y el informe no condicione su valoración jurídica.'],
  'La calificación de la falta y de su gravedad es del servidor competente. Lo del técnico es describir el hecho, el método y el resultado, con las circunstancias verificables: eso es justamente lo que permite al competente valorar la ilicitud sustancial y la culpabilidad.',
  'Calificar la falta —aunque sea como hipótesis o con un «podría»— invade la competencia ajena. Pero omitir las circunstancias tampoco sirve: deja al competente sin los elementos que necesita para valorar.'),

 (2,
  'En una capacitación surge la duda de a quién alcanza la ley disciplinaria. Un compañero sostiene que solo a servidores públicos vinculados por nombramiento y posesión; otro, que también a cualquier contratista del Estado por el solo hecho de tener contrato. El jefe pide precisión porque el informe debe explicar por qué una persona que intervino en los hechos quedó dentro de la actuación y otra no.',
  '¿Cuál es la precisión correcta sobre los sujetos disciplinables?',
  ['Son disciplinables únicamente los servidores públicos, de modo que cualquier particular queda siempre fuera del alcance de la ley disciplinaria, cualquiera que sea su relación con el Estado.',
   'Son disciplinables todos los contratistas del Estado por el solo hecho de haber suscrito un contrato estatal, con independencia del objeto contratado y de las funciones que ejerzan.',
   'Son disciplinables los servidores públicos y también los particulares en los casos que la ley señala, como quienes ejercen funciones públicas o administran recursos del Estado.',
   'Son disciplinables los servidores públicos en ejercicio y los exservidores por hechos anteriores, pero nunca los particulares, cuya responsabilidad se rige exclusivamente por la vía civil o penal.'],
  'El Código extiende la ley disciplinaria a los servidores públicos y, en los casos que la propia ley señala, a particulares: típicamente quienes ejercen funciones públicas o administran recursos del Estado. Ni todos los particulares ni ninguno.',
  'Ni los particulares quedan siempre fuera, ni todo contratista queda dentro por el solo hecho del contrato: lo que define el alcance es ejercer funciones públicas o administrar recursos públicos, en los casos que la ley prevé.'),

 (0,
  'Un compañero está estudiando con un material que cita constantemente la Ley 734 de 2002 y el Código Disciplinario Único, y le dice que, aunque ha oído que esa ley fue derogada, «en la práctica todavía se aplican las dos». Le muestra además un cuadro de deberes y prohibiciones que remite a los artículos 34 y 35. Usted sabe que esos datos no corresponden al código vigente y que la prueba puede preguntar justamente por eso.',
  '¿Cuál es la precisión correcta sobre la normatividad vigente?',
  ['El Código General Disciplinario es la Ley 1952 de 2019, modificada por la Ley 2094 de 2021 y en vigencia plena desde el 29 de marzo de 2022; la Ley 734 de 2002 quedó derogada.',
   'La Ley 1952 de 2019 y la Ley 734 de 2002 coexisten: la primera rige los procesos nuevos y la segunda continúa aplicándose a cualquier consulta sobre deberes y prohibiciones del servidor.',
   'La Ley 2094 de 2021 derogó íntegramente la Ley 1952 de 2019 y es hoy el Código General Disciplinario, por lo que las citas deben hacerse siempre a la Ley 2094 y no a la Ley 1952.',
   'El Código Disciplinario Único sigue vigente como norma general y la Ley 1952 de 2019 solo regula el procedimiento, de modo que ambas deben citarse según el tema que se esté tratando.'],
  'El CGD es la Ley 1952 de 2019, modificada por la Ley 2094 de 2021, en vigencia plena desde el 29 de marzo de 2022. La Ley 734 de 2002 (CDU) quedó derogada: todo material que la cite como vigente está desactualizado.',
  'La Ley 2094 modificó la Ley 1952, no la derogó; y el CDU no sobrevive ni para deberes ni para prohibiciones. Si su material de estudio cita los arts. 34 y 35 para eso, es de la Ley 734.'),

 (3,
  'El despacho le pide practicar una prueba técnica para acreditar que un servidor no cumplió un procedimiento interno. Usted documenta que, en efecto, el procedimiento no se siguió. En el informe, un compañero le sugiere añadir que «la conducta afectó sustancialmente el deber funcional», porque es la fórmula que el despacho necesita para avanzar y porque, a su juicio, es evidente. La diligencia fue la semana pasada, usted conserva el registro fotográfico y el despacho espera el informe para evaluar el expediente.',
  '¿Qué debe hacer y por qué?',
  ['Incluir la frase, porque la ilicitud sustancial es una constatación objetiva sobre el cumplimiento del deber y el técnico puede verificarla con el mismo rigor con que verifica un hecho.',
   'Incluir la frase matizada como apreciación técnica, de modo que el despacho disponga del elemento sin que la afirmación comprometa formalmente la valoración jurídica que debe hacer.',
   'No incluirla y limitarse a consignar que el procedimiento no se siguió, sin describir el contexto ni las condiciones, para que la valoración quede intacta en manos del competente.',
   'No incluirla, y documentar en cambio las condiciones, el contexto y las circunstancias verificables en que ocurrió el incumplimiento, que es lo que el competente necesita para valorarlo.'],
  'La ilicitud sustancial es un juicio de valoración jurídica sobre la afectación del deber funcional: no la constata el técnico. Lo que sí le corresponde —y es decisivo— es documentar las condiciones y circunstancias que permiten al competente hacer esa valoración.',
  'Afirmar la ilicitud sustancial, aun matizada, es calificar. Pero quedarse en el hecho desnudo tampoco sirve: sin contexto ni condiciones, el competente no tiene con qué valorar si el deber funcional se afectó sustancialmente.'),

 (1,
  'Durante una diligencia, el servidor investigado le explica a usted que no cumplió el procedimiento porque el sistema institucional llevaba tres días caído y recibió una instrucción verbal de su jefe para proceder de otro modo. Le pide que eso quede en el informe. Un compañero le dice que no lo incluya, «porque las justificaciones las valora el despacho y el informe es técnico». El investigado pide que quede constancia exacta de lo dicho y el informe debe rendirse pasado mañana, con los anexos.',
  '¿Cómo debe proceder?',
  ['No incluir la manifestación, porque las causales de exclusión de responsabilidad son materia de valoración jurídica y el informe técnico no debe contener argumentos de defensa del investigado.',
   'Dejar constancia de la manifestación tal como fue hecha, sin calificarla ni valorarla, y documentar además los hechos objetivos verificables sobre el estado del sistema en esas fechas.',
   'Incluir la manifestación y verificar por su cuenta con el área de sistemas si la caída fue real, incorporando esa verificación al informe como elemento que respalda o desvirtúa lo dicho.',
   'Incluir la manifestación señalando que, a su juicio técnico, la falla del sistema explica razonablemente el incumplimiento y podría constituir una causal de exclusión de responsabilidad.'],
  'Lo manifestado se consigna tal como se dijo, sin calificarlo, y los hechos objetivos verificables se documentan. Valorar si eso configura una causal de exclusión de responsabilidad —fuerza mayor, caso fortuito, orden legítima— es del competente.',
  'Omitir lo manifestado empobrece el expediente; valorarlo como causal lo califica; y verificar por cuenta propia fuera del objeto delegado excede el rol, aunque la verificación parezca útil.'),

 (2,
  'El informe que usted debe rendir acreditará un hecho que ocurrió hace cuatro años y medio. Un compañero comenta que «seguro ya prescribió y el trabajo no sirve de nada». Otro responde que la prescripción no existe en lo disciplinario. El jefe pide que el informe se rinda igual y con el mismo rigor, pero quiere que usted entienda por qué. El expediente llegó a la Dirección la semana pasada y el jefe quiere que el equipo entienda bien el punto antes de seguir.',
  '¿Cuál es la precisión correcta?',
  ['La prescripción no opera en materia disciplinaria porque la potestad del Estado para sancionar las faltas de sus servidores no está sujeta a límites temporales de ninguna clase.',
   'La prescripción opera, por lo que el informe debe advertir expresamente que la acción está prescrita y que la actuación carece de objeto, para evitar un desgaste innecesario de la entidad.',
   'La potestad disciplinaria sí está limitada en el tiempo por la prescripción y la caducidad, pero establecer si operaron en el caso concreto es del competente: el técnico rinde su informe con el mismo rigor.',
   'La prescripción solo opera para las faltas leves; tratándose de faltas graves o gravísimas la acción disciplinaria puede iniciarse en cualquier momento sin límite temporal alguno.'],
  'El tiempo sí limita la potestad disciplinaria, pero determinar si la prescripción o la caducidad operaron en un caso concreto es una decisión jurídica del competente. El técnico no condiciona su trabajo a esa valoración: documenta con el mismo rigor.',
  'Ni la prescripción es inexistente en lo disciplinario, ni depende de la gravedad de la falta, ni le corresponde al informe técnico declarar prescrita una acción.'),

 (0,
  'Un hecho que usted documentó técnicamente fue archivado en sede penal por la Fiscalía. El despacho disciplinario le pide continuar con el apoyo técnico. Un compañero sostiene que no tiene sentido: «si la Fiscalía archivó, no hubo nada, y seguir es perder el tiempo». El jefe le pide que lo deje claro en una nota interna. El apoyo técnico está a medio camino y el despacho pidió expresamente que el informe se rinda dentro del término fijado.',
  '¿Cuál es la precisión correcta?',
  ['Las acciones son independientes: el archivo penal no cierra automáticamente el expediente disciplinario, porque lo que se valora en cada una y el estándar aplicable son distintos.',
   'El archivo penal obliga al archivo disciplinario cuando versa sobre los mismos hechos, porque lo contrario implicaría juzgar dos veces a la misma persona por la misma conducta.',
   'El archivo penal suspende la actuación disciplinaria hasta que quede en firme, momento en el cual el despacho debe decidir si continúa o archiva el expediente que venía tramitando.',
   'El archivo penal es irrelevante en lo disciplinario únicamente cuando la falta es gravísima; tratándose de faltas graves o leves el archivo penal sí tiene efecto vinculante sobre el expediente.'],
  'La independencia de las acciones es un principio central: lo penal valora el delito, lo disciplinario la afectación del deber funcional, y el archivo en una no determina el resultado en la otra. Por eso el apoyo técnico continúa.',
  'No hay doble juzgamiento porque no son la misma acción ni el mismo objeto; el archivo penal no suspende ni vincula lo disciplinario, y la independencia no depende de la gravedad de la falta.'),

 (3,
  'Su informe debe describir el resultado de una prueba técnica sobre un expediente físico. Al examinarlo, usted advierte que faltan folios y que la foliación fue alterada. El despacho le pide que el informe concluya si la alteración fue «dolosa o apenas un descuido». Usted tiene elementos para describir con precisión qué se alteró y cómo, pero no para afirmar la intención de nadie. El expediente físico quedó bajo custodia de la dependencia y usted levantó acta detallada del estado en que lo recibió.',
  '¿Cuál es la actuación correcta?',
  ['Concluir que la alteración fue dolosa, porque una foliación modificada y folios faltantes no se explican por un descuido y el técnico puede inferirlo de los hechos que documentó.',
   'Concluir que no es posible determinar la intención y, por esa razón, omitir del informe el detalle de la alteración, que podría leerse como una imputación implícita al responsable.',
   'Concluir que fue un descuido, porque en ausencia de prueba de la intención debe aplicarse la presunción de inocencia y el informe no puede sugerir una conducta más grave.',
   'Describir con precisión qué folios faltan, qué se alteró y cómo, y abstenerse de afirmar la intención, señalando que la valoración del dolo o la culpa corresponde al competente.'],
  'El dolo y la culpa son el elemento subjetivo de la falta y su valoración es jurídica, no técnica. Lo que el informe debe aportar es la descripción precisa de lo alterado, que es exactamente lo que permite al competente valorar ese elemento.',
  'Afirmar dolo o descartarlo son, las dos, calificaciones del elemento subjetivo. Y omitir el detalle de la alteración por prudencia priva al competente del único elemento con el que podría valorarlo.'),

 (1,
  'Un compañero afirma que la Procuraduría solo puede investigar cuando la oficina de control interno disciplinario de la entidad no ha abierto el caso, y que si la OCID ya lo tiene, la PGN debe esperar. El jefe pide precisión porque el informe técnico debe explicar por qué el caso llegó a la Dirección a pesar de existir una actuación en la entidad de origen. La entidad de origen ya abrió actuación por los mismos hechos y el jefe quiere dejar motivado el punto en el informe.',
  '¿Cuál es la precisión correcta?',
  ['La PGN y las OCID tienen competencias excluyentes: quien primero avoque conocimiento conserva el caso hasta su terminación, sin que la otra pueda intervenir mientras tanto.',
   'La PGN puede asumir el conocimiento de procesos que adelantan las oficinas de control interno disciplinario en virtud del poder preferente que la Constitución y la ley le reconocen.',
   'La PGN solo puede intervenir cuando la OCID se declara impedida o cuando la entidad de origen solicita expresamente que el caso sea asumido por el órgano de control externo.',
   'Las OCID carecen de competencia disciplinaria propia y actúan siempre por delegación de la PGN, de modo que todo expediente pertenece en realidad a la Procuraduría desde su inicio.'],
  'El poder preferente permite a la PGN asumir procesos que adelantan las OCID: es control externo que desplaza, no que espera. No es competencia excluyente por reparto temporal ni requiere solicitud de la entidad.',
  'Ni el primero que avoca conserva el caso, ni la PGN necesita impedimento o solicitud, ni las OCID actúan por delegación: tienen competencia propia, sobre la que la PGN mantiene el poder preferente.'),

 (2,
  'El despacho solicitante le pide un apoyo técnico que, en su criterio, resolvería el caso de una vez: examinar todos los equipos de la dependencia para ver «si alguien más hizo lo mismo». La delegación que usted recibió se refiere a un equipo específico, vinculado a una queja concreta. El servidor insiste en que es más eficiente hacerlo todo junto. El despacho formuló la solicitud por correo esta mañana y la diligencia está programada para pasado mañana en la sede de la dependencia.',
  '¿Qué principio del derecho disciplinario está en juego y qué corresponde hacer?',
  ['La eficacia: siendo más eficiente examinar todo junto, corresponde ampliar el examen y dejar constancia en el informe de que se actuó por economía procesal y a solicitud del despacho.',
   'La oficiosidad: como la investigación disciplinaria se adelanta de oficio, el técnico puede extender el examen a hechos conexos que aparezcan durante la práctica de la prueba delegada.',
   'La legalidad y el debido proceso: el examen se limita a lo delegado; si el despacho quiere ampliarlo, debe ampliar la delegación, y eso se tramita por escrito antes de actuar.',
   'La celeridad: debe practicar el examen ampliado para no retrasar el caso, y solicitar en paralelo la ampliación de la delegación para que se formalice lo que ya se está haciendo.'],
  'La delegación delimita qué está autorizado. Examinar equipos no comprendidos en ella es actuar sin título, por eficiente que parezca: lo que corresponde es pedir la ampliación por escrito y actuar después.',
  'Ni la eficacia, ni la celeridad, ni la oficiosidad del proceso habilitan al técnico a ampliar por su cuenta el objeto de lo delegado. Actuar primero y formalizar después deja la prueba expuesta a exclusión.'),

 (3,
  'Usted documentó un incumplimiento y el investigado, en el lugar, le dice que actuó así porque recibió una orden escrita de su superior. Le muestra el documento. Un compañero le dice que lo ignore, «porque la obediencia debida no existe y una orden no justifica nada». El informe debe rendirse en dos días. La diligencia continúa, hay dos testigos presentes y el documento exhibido tiene sello y firma legibles. Usted no tiene forma de verificar por su cuenta si la orden era legítima.',
  '¿Cómo debe tratarse ese documento?',
  ['Ignorarlo, porque la obediencia debida no es causal de exclusión de responsabilidad en materia disciplinaria y su inclusión induciría a error al servidor competente.',
   'Incluirlo y señalar en el informe que la orden exime de responsabilidad al investigado, ya que acredita que la conducta obedeció a una instrucción legítima de su superior jerárquico.',
   'Incluirlo solo si el despacho lo pide expresamente, dado que incorporar documentos aportados por el investigado podría exceder el objeto de la prueba técnica que le fue delegada.',
   'Dejar constancia de que el documento fue exhibido y describirlo objetivamente, sin valorar si configura o no una causal de exclusión, y ponerlo en conocimiento del competente.'],
  'El técnico documenta lo que aparece, lo describe con objetividad y lo pone en conocimiento. Si una orden del superior configura o no una causal de exclusión de responsabilidad es una valoración jurídica del competente.',
  'Ignorar el documento suprime un elemento relevante; afirmar que exime de responsabilidad lo califica; y esperar a que el despacho lo pida deja fuera del expediente algo que usted ya vio.'),

 (0,
  'El despacho le anticipa que, según su lectura, la falta sería leve y le pide que el informe «se ajuste a esa línea» para que el expediente sea coherente. Usted documentó hechos que, descritos completos, podrían leerse de otro modo, aunque no le corresponde decirlo. El servidor del despacho es cordial y le explica que así evitan devoluciones. La conversación ocurrió por teléfono esta mañana y usted tiene el borrador del informe con toda la descripción ya redactada.',
  '¿Cuál es la actuación correcta?',
  ['Rendir el informe con la descripción completa y objetiva de lo documentado, sin ajustarlo a ninguna calificación anticipada, y dejar constancia escrita de la solicitud recibida.',
   'Ajustar el informe a la línea del despacho, que es quien conoce el caso completo y tiene la competencia para calificar la falta y decidir sobre el fondo del asunto.',
   'Rendir el informe completo y añadir una nota señalando que, a su juicio, la calificación de leve no se corresponde con los hechos documentados durante la práctica de la prueba.',
   'Consultar con su jefe si debe ajustarse a la línea del despacho y proceder conforme a lo que él indique, dejando constancia verbal de la consulta realizada antes de rendir el informe.'],
  'El informe describe lo documentado, completo, sin ajustarse a una calificación anticipada: esa es la objetividad del Nivel B y el límite del rol. Y la solicitud recibida se deja por escrito, porque protege tanto el caso como a usted.',
  'Ajustar el informe a una calificación esperada es filtrar la prueba; cuestionar la calificación en una nota es calificar; y una consulta verbal sin constancia no deja rastro de la presión recibida.'),

 (1,
  'En el estudio, usted encuentra que la amonestación escrita aparece siempre separada de las demás sanciones. Un compañero dice que es por ser la más leve; otro, que además tiene una consecuencia distinta. El jefe propone que lo aclaren porque es una pregunta típica de la prueba escrita. La duda surgió preparando el simulacro del fin de semana y el jefe quiere dejarlo aclarado por escrito para todo el grupo.',
  '¿Cuál es la particularidad correcta de la amonestación escrita?',
  ['Es la única sanción que puede imponerse sin agotar el procedimiento disciplinario, por tratarse de un llamado de atención formal y no de una sanción en sentido estricto.',
   'Es la única sanción disciplinaria que no genera inhabilidad, es decir, que no restringe el ejercicio futuro de la función pública, a diferencia de la suspensión y la destitución.',
   'Es la única sanción que no se registra en el sistema de información de registro de sanciones, de modo que no aparece en los certificados de antecedentes disciplinarios.',
   'Es la única sanción que puede ser impuesta directamente por el jefe inmediato del servidor, sin intervención del operador disciplinario competente de la entidad o de la PGN.'],
  'La amonestación escrita es la única sanción disciplinaria que no genera inhabilidad: no restringe el ejercicio futuro de la función pública. Esa es su particularidad, y es pregunta frecuente.',
  'Toda sanción requiere el procedimiento previo; el registro de sanciones no depende de que generen inhabilidad; y ninguna sanción disciplinaria la impone el jefe inmediato por fuera del operador competente.'),

 (2,
  'Un compañero le dice que, como el hecho es «evidente» y todo el mundo en la dependencia lo sabe, el informe técnico puede ser breve: basta con afirmar que ocurrió. Añade que insistir en documentar cada paso es desconfiar de los compañeros y alargar innecesariamente el trabajo. El término vence en dos días y el informe ya está esbozado. El hecho ocurrió hace tres semanas, varias personas lo comentan en la dependencia y nadie ha dejado constancia escrita de nada.',
  '¿Cuál es el principio aplicable y qué corresponde hacer?',
  ['La buena fe: puede sostenerse en lo que la dependencia conoce y describir el hecho de manera sintética, documentando solo aquello que resulte controvertido o que el despacho pida expresamente.',
   'La celeridad: siendo el hecho notorio, el informe puede limitarse a constatarlo, lo que permite cumplir el término y dedicar el tiempo restante a otros apoyos pendientes de la Dirección.',
   'La presunción de inocencia y la necesidad de prueba: sin prueba no hay falta demostrada, por evidente que parezca el hecho, de modo que el informe documenta método, hallazgos y condiciones.',
   'La economía procesal: debe documentar únicamente los elementos que no consten ya en el expediente, para no duplicar información que el despacho tiene y agilizar así la decisión del caso.'],
  'Sin prueba no hay falta demostrada, por evidente que parezca el hecho: la presunción de inocencia solo se desvirtúa con prueba, y la prueba es justamente lo que usted produce. Documentar método, hallazgos y condiciones no es desconfianza: es el trabajo.',
  'Ni la buena fe, ni la celeridad, ni la economía procesal relevan de probar. Un informe que se apoya en lo que «todos saben» no sostiene ninguna decisión y deja la actuación expuesta.'),

 (3,
  'Faltan diez días para la prueba y usted nota que acierta las preguntas sobre faltas y sanciones, pero falla las que mezclan el marco disciplinario con su propio rol: duda entre la opción que describe correctamente el derecho y la que describe correctamente lo que a usted le toca hacer. Su lista de errores lo confirma en seis de los últimos diez casos resueltos. Lleva un registro de los simulacros resueltos y puede ver exactamente en qué opción cayó cada vez que falló.',
  '¿Cuál es la mejor manera de corregirlo?',
  ['Repasar de nuevo el articulado del Código General Disciplinario, porque dominar el contenido sustantivo hace que la respuesta correcta sobre el rol se deduzca sola del marco normativo.',
   'Memorizar que, ante la duda, la opción correcta es la que describe una conducta de apoyo, ya que el cargo es técnico y nunca tiene competencia para adoptar decisiones sobre el caso.',
   'Resolver más simulacros del bloque disciplinario hasta que el patrón se automatice, dejando el repaso del marco sustantivo para los días previos a la presentación de la prueba.',
   'Separar en cada caso dos preguntas: qué dice el marco disciplinario sobre el hecho, y qué de eso le corresponde a usted hacer, eligiendo la opción que responde bien a las dos.',
  ],
  'El error no está en el contenido sino en mezclar dos planos: el marco disciplinario y el alcance del rol. Separarlos en dos preguntas explícitas antes de mirar las opciones es lo que hace visible la respuesta correcta.',
  'Repasar más articulado no corrige la confusión de planos; una regla automática falla cuando el caso sí está dentro de su autonomía técnica; y repetir simulacros sin cambiar el método repite el error.'),
]
