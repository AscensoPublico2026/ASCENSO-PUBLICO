# -*- coding: utf-8 -*-
"""Día 12 · CGD II: procedimiento, instrucción y juzgamiento (Ley 2094 de 2021) — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-DIS-4TI15O-02',
    archivo='FUN-DIS-4TI15O-02-procedimiento-instruccion-juzgamiento.html',
    dia=12,
    titulo_doc='Código General Disciplinario II: procedimiento, instrucción y juzgamiento',
    h1='Código General Disciplinario II<br>Procedimiento',
    kicker='Día 12 · Conocimientos específicos',
    sub='El itinerario completo del expediente y <strong>dónde encaja tu trabajo en él</strong>: queja y calificación inicial, indagación preliminar, apertura, <strong>instrucción y actividad probatoria</strong> —tu etapa—, cierre y evaluación, pliego de cargos, descargos, <strong>período probatorio del juzgamiento</strong>, fallo, congruencia, recursos y ejecutoria, con la doble instancia que introdujo la <strong>Ley 2094 de 2021</strong>. Saber en qué etapa está el expediente te dice qué puede pedírsete y qué no.',
    badges=['⏱ 100-120 min', '⚖️ Procedimiento', '🔍 Prueba'],
    fmeta='Procedimiento disciplinario: instrucción y juzgamiento (Ley 1952 de 2019 y Ley 2094 de 2021)',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Procedimiento disciplinario: instrucción y juzgamiento',
)

FUENTE = 'guias/FUN-DIS-4SU11-02-procedimiento-instruccion-juzgamiento.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- bloques nuevos
MOD5 = (
    '<h3><span class="h3-chip">5</span> La etapa de instrucción: actividad probatoria y tu etapa de '
    'mayor volumen de trabajo</h3>\n'
    '  <h4>Aquí es donde entra, casi siempre, el apoyo técnico de la DNIE</h4>\n'
    '  <p>Una vez abierta formalmente la investigación se despliega la actividad central de la fase de '
    'instrucción: recaudar los elementos de prueba necesarios para establecer si el hecho ocurrió, si '
    'constituye falta y quién es responsable. Es, con diferencia, <mark>la etapa en la que el despacho '
    'solicita apoyo técnico</mark>, y por lo tanto la etapa en la que tú apareces: se acuerda la '
    'metodología del apoyo, el servidor competente te delega la práctica de una prueba técnica, la '
    'practicas, elaboras el informe y presentas las pruebas practicadas con sus anexos ante quien las '
    'solicitó.</p>\n'
    '  <p>Conviene que tengas presente un matiz que la prueba escrita explora: <strong>la instrucción no '
    'es la única etapa en que puedes ser requerido</strong>. Después del pliego de cargos y de los '
    'descargos se abre un <strong>período probatorio dentro del juzgamiento</strong>, en el que también '
    'pueden decretarse pruebas —incluidas las que el investigado solicita en su defensa—. Si en ese '
    'momento se requiere una prueba técnica, el mecanismo es el mismo: delegación del competente, '
    'metodología, práctica, informe y presentación. Lo que cambia es la etapa, no tu rol.</p>\n'
    '  <p>Es también la etapa donde el control riguroso de términos se vuelve más crítico: la '
    'instrucción tiene plazos legales definidos, y una demora en rendir un informe técnico puede '
    'comprometer seriamente el desarrollo del proceso, incluido el riesgo de una eventual prescripción '
    'de la acción disciplinaria. Por eso un apoyo que no alcanza a rendirse a tiempo <strong>se advierte '
    'por escrito en cuanto se ve venir</strong>, no el día del vencimiento.</p>\n'
    '  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Una pregunta frecuente te sitúa en una etapa '
    'posterior —ya formulado el pliego, o en pleno juzgamiento— y te pide actuar como si estuvieras en '
    'instrucción. Antes de elegir, ubica la etapa: <strong>qué puede pedírsete depende de dónde está el '
    'expediente</strong>, y en ninguna etapa cambia el hecho de que la prueba se practica por '
    'delegación.</p></div>'
)

MOD16 = (
    '<h3><span class="h3-chip">16</span> Practicar, documentar y proyectar: el alcance exacto de tu '
    'función en el procedimiento</h3>\n'
    '  <h4>El módulo central de esta guía</h4>\n'
    '  <p>Habiendo recorrido cada etapa del proceso, es momento de consolidar la idea que atraviesa toda '
    'esta guía. Tus funciones se materializan en el procedimiento de tres maneras, y conviene no '
    'confundirlas:</p>\n'
    '  <div class="flujo">\n'
    '    <div class="flujo-paso"><div class="fp-n">1</div><div><b>Practicar</b><p>La prueba técnica, '
    '<strong>previa delegación</strong> del servidor competente y conforme a la metodología acordada con '
    'la dependencia solicitante. Sin delegación no hay actuación.</p></div></div>\n'
    '    <div class="flujo-paso"><div class="fp-n">2</div><div><b>Documentar y presentar</b><p>El acta, '
    'el registro de los elementos, el informe técnico y los anexos, presentados ante la autoridad que '
    'solicitó el apoyo. Describes hechos, método y resultados.</p></div></div>\n'
    '    <div class="flujo-paso"><div class="fp-n">3</div><div><b>Proyectar</b><p>Autos, conceptos y '
    'actos administrativos <strong>para la firma del servidor competente</strong>. El borrador es '
    'borrador hasta que alguien con competencia lo revisa, lo ajusta y lo firma.</p></div></div>\n'
    '  </div>\n'
    '  <p>«Proyectar» significa, en términos concretos: leer y organizar el material disponible; '
    'redactar el documento siguiendo la estructura formal exigida y las instrucciones recibidas; '
    'asegurarte de que el lenguaje sea objetivo y <strong>no anticipe conclusiones que no te corresponde '
    'formular</strong>; y entregar el borrador completo para que el servidor competente ejerza su '
    'función de revisión, corrección y decisión. En ningún momento decides tú el fondo: ni calificas la '
    'falta, ni determinas una sanción, ni declaras una responsabilidad.</p>\n'
    '  <p>Y hay una regla que vale para las tres: <mark>lo que no quede documentado, no existió</mark>. '
    'Un hallazgo comentado de palabra, una inconsistencia advertida y no consignada, una delegación '
    'recibida verbalmente, una presión que no quedó por escrito: todo eso desaparece del expediente y, '
    'con él, de cualquier posibilidad de ser valorado o de protegerte a ti.</p>'
)

MOD_HALLAZGO = (
    '<h4>El hallazgo incidental durante la práctica de una prueba técnica</h4>\n'
    '  <p>Es la situación que más veces se repite en las preguntas situacionales de un cargo como el '
    'tuyo, y vale la pena fijarla con una regla única. Practicando una prueba delegada aparece algo que '
    '<strong>no estaba en el objeto</strong>: otro posible incumplimiento, un indicio de delito, un '
    'posible detrimento patrimonial, una irregularidad de otro servidor. La tentación es doble y las dos '
    'caras son errores: ampliar el trabajo por cuenta propia, u omitirlo «porque no me lo pidieron».</p>\n'
    '  <div class="tabla-wrap">\n'
    '    <table>\n'
    '      <thead><tr><th>Reacción</th><th>Por qué falla</th><th>Qué corresponde</th></tr></thead>\n'
    '      <tbody>\n'
    '        <tr><td>Ampliar el examen para precisar el hallazgo</td><td>Excede el objeto de la '
    'delegación: lo así obtenido queda expuesto a exclusión.</td><td>Documentar lo observado y pedir, si '
    'procede, la ampliación por escrito.</td></tr>\n'
    '        <tr><td>Omitirlo del informe</td><td>Compromete la veracidad: el informe deja de reflejar '
    'lo que ocurrió en la diligencia.</td><td>Consignarlo como hecho observado, sin calificarlo.</td></tr>\n'
    '        <tr><td>Comentarlo solo de palabra al despacho</td><td>No deja rastro: para el expediente, '
    'no ocurrió.</td><td>Ponerlo en conocimiento <strong>por escrito</strong> del competente.</td></tr>\n'
    '        <tr><td>Remitirlo directo a Fiscalía o Contraloría</td><td>La compulsa de copias es una '
    'decisión del competente, no del técnico.</td><td>Describir y poner en conocimiento; él '
    'decide.</td></tr>\n'
    '      </tbody>\n'
    '    </table>\n'
    '  </div>\n'
    '  <p>La regla única, entonces: <strong>describir sin calificar, consignar por escrito y poner en '
    'conocimiento del competente</strong>. Sirve para el hallazgo penal, para el fiscal, para el '
    'disciplinario y para la irregularidad de trámite. Si la memorizas, resuelves una familia entera de '
    'preguntas.</p>'
)

R = [
    ('<h3><span class="h3-chip">5</span> La etapa de instrucción: actividad probatoria y tu papel de mayor volumen de trabajo</h3>\n  <h4>Donde se pone a prueba tu capacidad de organización</h4>\n  <p>Una vez abierta formalmente la investigación, se despliega la actividad central de la fase de instrucción: recaudar los elementos de prueba necesarios para establecer si el hecho ocurrió, si constituye falta, y quién es responsable. Para ti, esta etapa suele representar el <mark>mayor volumen de trabajo operativo</mark> dentro del expediente: apoyar la elaboración de oficios para solicitar información (función 2 de tu manual), programar y apoyar la logística de diligencias probatorias, incorporar y organizar cada documento que llega al expediente, y mantener actualizado el sistema de información sobre el estado del proceso (función 3).</p>\n  <p>Es también la etapa donde el control riguroso de términos —que dominaste en la guía dedicada específicamente a ese tema— se vuelve más crítico: la instrucción tiene plazos legales definidos, y un descuido en su vigilancia puede comprometer seriamente el desarrollo del proceso, incluyendo el riesgo de una eventual prescripción de la acción disciplinaria, como estudiaste en la guía anterior.</p>',
     MOD5),
    ('<h3><span class="h3-chip">16</span> Apoyar la proyección de autos y providencias: el alcance exacto de tu función</h3>\n  <h4>El módulo central de esta guía</h4>\n  <p>Habiendo recorrido cada etapa del proceso, es momento de consolidar la idea que atraviesa toda esta guía: tu función 1, "apoyar en la proyección de conceptos, providencias, solicitudes, constancias, recursos y todo aquello que guarde relación con el cumplimiento de las funciones de la dependencia", se materializa en cada una de las etapas anteriores mediante la <mark>proyección de borradores</mark> —el auto de apertura, el pliego de cargos, el proyecto de fallo, la comunicación de un recurso— siempre bajo instrucción del jefe de despacho, siempre sujeta a su revisión, ajuste y decisión final, y siempre sin que tú misma decidas el contenido sustantivo de esas actuaciones.</p>\n  <p>"Proyectar" significa, en términos concretos: leer y organizar el acervo probatorio disponible; redactar el documento siguiendo la estructura formal exigida y las instrucciones específicas recibidas; asegurarte de que el lenguaje empleado sea objetivo y no anticipe conclusiones que no te corresponde formular; y entregar el borrador completo para que el jefe de despacho ejerza sobre él su función de revisión, corrección y decisión. En ningún momento de ese proceso decides tú el fondo del asunto: ni calificas definitivamente una falta, ni determinas una sanción, ni declaras una responsabilidad.',
     MOD16 + '\n  <p>__RESTO16__'),
    ('<h3><span class="h3-chip">31</span>',
     MOD_HALLAZGO + '\n\n  <h3><span class="h3-chip">31</span>'),
]
SEC = aplicar_todas(SEC, R, estricto=True)
SEC = aplicar_todas(SEC, [('<p>__RESTO16__', '<p>')], estricto=True)

# ---------------------------------------------------------------- calidad: interactividad y cierre
CP1 = """<div class="checkpoint" data-cp="1">
      <div class="cp-q">✋ Punto de control 1: ¿en qué etapas del proceso puede pedírsele a la DNIE la práctica de una prueba técnica?</div>
      <div class="cp-opts">
      <button class="cp-opt" data-ans="0">Solo durante la indagación preliminar, antes de que se abra formalmente la investigación.</button>
      <button class="cp-opt" data-ans="1">Principalmente en la instrucción, pero también en el período probatorio del juzgamiento: siempre previa delegación del competente.</button>
      <button class="cp-opt" data-ans="0">En cualquier etapa y sin delegación, porque las funciones de policía judicial son permanentes.</button>
      </div>
      <div class="cp-fb"></div>
    </div>"""

CP2 = """<div class="checkpoint" data-cp="2">
      <div class="cp-q">✋ Punto de control 2: durante una diligencia aparece un hallazgo que no está en el objeto de la delegación. ¿Qué hace?</div>
      <div class="cp-opts">
      <button class="cp-opt" data-ans="0">Amplía el examen para precisarlo, ya que está allí y sería ineficiente volver después.</button>
      <button class="cp-opt" data-ans="0">Lo omite del informe, porque no se lo pidieron y así no excede el objeto delegado.</button>
      <button class="cp-opt" data-ans="1">Lo describe sin calificarlo, lo consigna por escrito y lo pone en conocimiento del servidor competente, que decide qué hacer.</button>
      </div>
      <div class="cp-fb"></div>
    </div>"""

CP3 = """<div class="checkpoint" data-cp="3">
      <div class="cp-q">✋ Punto de control 3: usted ve venir que no alcanzará a rendir el informe dentro del término. ¿Cuándo lo advierte?</div>
      <div class="cp-opts">
      <button class="cp-opt" data-ans="1">En cuanto lo ve venir, por escrito y por el canal, para que el competente pueda disponer lo que corresponda.</button>
      <button class="cp-opt" data-ans="0">El día del vencimiento, cuando ya es seguro que no alcanzará a rendirlo.</button>
      <button class="cp-opt" data-ans="0">No lo advierte: rinde un informe más breve para cumplir el término.</button>
      </div>
      <div class="cp-fb"></div>
    </div>"""

CP4 = """<div class="checkpoint" data-cp="4">
      <div class="cp-q">✋ Punto de control 4: ¿qué aporta la Ley 2094 de 2021 al procedimiento?</div>
      <div class="cp-opts">
      <button class="cp-opt" data-ans="0">Derogó la Ley 1952 de 2019 y la sustituyó como Código General Disciplinario.</button>
      <button class="cp-opt" data-ans="1">Modificó la Ley 1952 de 2019 y reforzó garantías del procedimiento, entre ellas la doble instancia.</button>
      <button class="cp-opt" data-ans="0">Revivió el régimen disciplinario anterior para los procesos que estuvieran en curso.</button>
      </div>
      <div class="cp-fb"></div>
    </div>"""

PR1 = """<div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> El despacho le pide practicar una prueba técnica cuando el expediente ya está en juzgamiento, después de los descargos. Un compañero dice que «en juzgamiento ya no se practican pruebas».</p>
    <p><strong>Cómo proceder.</strong> Sí se practican: tras los descargos se abre un período probatorio dentro del juzgamiento, donde pueden decretarse pruebas, incluidas las que pide el investigado en su defensa. Lo que usted verifica no es la etapa, sino que exista delegación del competente y metodología acordada.</p>
  </div>"""

PR2 = """<div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Durante una diligencia que usted apoya, un testigo entrega una versión que contradice lo que había dicho por escrito. El servidor del despacho le pregunta cuál le parece más creíble.</p>
    <p><strong>Cómo proceder.</strong> Dejar constancia fiel y completa de las dos versiones, sin omitir ninguna y sin ordenarlas por credibilidad. Valorar cuál prevalece es del competente. Si le preguntan su impresión, lo correcto es describir lo que observó, no concluir.</p>
  </div>"""

PR3 = """<div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Usted advierte que el acta de una diligencia anterior no consigna la hora de una entrega de elementos, y el expediente está próximo a evaluación.</p>
    <p><strong>Cómo proceder.</strong> Las nulidades procesales no las declara usted, pero sí es quien está en posición de advertirlas. Deje constancia escrita de la inconsistencia concreta, informe por el canal y precise en su informe qué puede y qué no puede sostenerse con ese vacío. Advertir a tiempo es, muchas veces, lo que salva la actuación.</p>
  </div>"""

OJO2 = """<div class="ojo"><b>👁️ Ojo en la prueba</b><p>Cuidado con las opciones que lo hacen <strong>decidir sobre el trámite</strong>: suspender una diligencia, declarar una nulidad, archivar, decretar una prueba, ampliar un término. Todas esas son decisiones del operador disciplinario. Lo del técnico es <strong>advertir por escrito y a tiempo</strong>, que no es poco: una nulidad advertida antes del fallo se corrige; advertida después, cuesta el proceso.</p></div>"""

CIERRE = """<div class="box gold">
    <div class="box-title">💡 Idea clave del día</div>
    <p>El procedimiento disciplinario es un itinerario con etapas, y cada etapa define qué puede pedírsele a usted. Su trabajo se concentra en la <strong>instrucción</strong> y reaparece en el <strong>período probatorio del juzgamiento</strong>, siempre con la misma fórmula: delegación del competente, metodología acordada, práctica, informe y presentación de las pruebas con sus anexos. Y una regla que atraviesa todo el proceso: lo que no quede documentado, no existió.</p>
  </div>
  <div class="box ok">
    <div class="box-title">🧠 Frase para recordar</div>
    <p>«Describir sin calificar, consignar por escrito y poner en conocimiento del competente.» Sirve para el hallazgo penal, el fiscal, el disciplinario y la irregularidad de trámite.</p>
  </div>
  <div class="fuentes"><div class="fuentes-tag">📚 Fuentes oficiales para profundizar</div>
    <ul class="lista">
      <li><a href="https://funcionpublica.gov.co/eva/gestornormativo/norma.php?i=90324" target="_blank" rel="noopener">Ley 1952 de 2019 — Código General Disciplinario</a></li>
      <li><a href="https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_2094_2021.htm" target="_blank" rel="noopener">Ley 2094 de 2021 — Reforma del procedimiento disciplinario y doble instancia</a></li>
      <li><a href="https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1952_2019_pr003.htm" target="_blank" rel="noopener">Ley 1952 de 2019, arts. 115 y 116 — Reserva de la actuación y requisitos formales</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=4125" target="_blank" rel="noopener">Constitución Política de Colombia — art. 29 (debido proceso)</a></li>
      <li><a href="https://www.procuraduria.gov.co/" target="_blank" rel="noopener">Procuraduría General de la Nación — sitio oficial</a></li>
    </ul>
  </div>"""

SEC = aplicar_todas(SEC, [
    ('<h3><span class="h3-chip">7</span>', CP1 + '\n\n  <h3><span class="h3-chip">7</span>'),
    ('<h3><span class="h3-chip">12</span>', PR1 + '\n  ' + CP4 + '\n\n  <h3><span class="h3-chip">12</span>'),
    ('<h3><span class="h3-chip">19</span>', PR2 + '\n\n  <h3><span class="h3-chip">19</span>'),
    ('<h3><span class="h3-chip">20</span>', PR3 + '\n  ' + OJO2 + '\n\n  <h3><span class="h3-chip">20</span>'),
    ('<h3><span class="h3-chip">32</span>', CP2 + '\n  ' + CP3 + '\n\n  <h3><span class="h3-chip">32</span>'),
    ('<button class="btn-continuar" onclick="showSection(3)">Continuar →</button>',
     CIERRE + '\n\n  <button class="btn-continuar" onclick="showSection(3)">Continuar →</button>'),
], estricto=True)

SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>',
     '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('(4SU-11)', '(4TI-15)'),
    ('FUN-DIS-4SU11-01', 'FUN-DIS-4TI15O-01'),
    ('4SU11', '4TI15O'),
    ('4SU-11', '4TI-15'),
    ('288-2026', '257-2026'),
    ('Resolución 243 de 2026', 'Resolución 212 de 2026'),
    ('apoyas logísticamente', 'apoyas técnicamente'),
    ('apoyo en la proyección', 'apoyo técnico probatorio'),
    ('la sustanciación', 'el apoyo técnico'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)   # filtro antifugas final

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el '
              'procedimiento disciplinario y el lugar exacto del apoyo técnico en él: etapas, instrucción y '
              'actividad probatoria, pliego de cargos, descargos, período probatorio del juzgamiento, congruencia, '
              'recursos, nulidades y hallazgos incidentales.')

P = [
 (1,
  'El despacho le solicita practicar una prueba técnica. Al revisar la solicitud, usted advierte que el expediente ya tiene pliego de cargos formulado y notificado, y que el investigado presentó descargos pidiendo precisamente esa prueba. Un compañero le dice que no puede practicarse, «porque en juzgamiento ya no se recaudan pruebas y eso es cosa de la instrucción». La solicitud viene firmada por el servidor competente y acompañada de la delegación correspondiente.',
  '¿Cuál es la precisión correcta?',
  ['Su compañero tiene razón: una vez formulado el pliego de cargos se cierra la actividad probatoria, de modo que la solicitud debe devolverse al despacho para que corrija la etapa.',
   'Sí puede practicarse: después de los descargos se abre un período probatorio dentro del juzgamiento, donde pueden decretarse pruebas, incluidas las que el investigado pide en su defensa.',
   'Puede practicarse solo si el despacho la decreta de oficio; tratándose de una prueba solicitada por el investigado, debe esperarse a que el fallo de primera instancia resuelva sobre ella.',
   'Puede practicarse pero sin levantar acta formal, porque en la etapa de juzgamiento la actividad probatoria se documenta directamente en la audiencia y no en documentos separados.'],
  'Tras los descargos se abre un período probatorio dentro del juzgamiento: ahí se practican las pruebas decretadas, incluidas las pedidas por el investigado en su defensa. Lo que cambia es la etapa, no el mecanismo: delegación, metodología, práctica, informe.',
  'La actividad probatoria no termina con el pliego de cargos; las pruebas de la defensa no se aplazan al fallo; y toda diligencia se documenta en acta, cualquiera que sea la etapa.'),

 (2,
  'Practicando una prueba técnica delegada sobre un equipo, usted advierte que en la misma oficina hay otro equipo con señales del mismo problema, perteneciente a un servidor que no está vinculado a la investigación. El objeto de su delegación se limita al primer equipo. El servidor del despacho, al que llama por teléfono, le dice que «revise también ese, total ya está allá». El despacho llamó esta mañana y la diligencia está en curso, con el acta todavía abierta.',
  '¿Qué corresponde hacer?',
  ['Revisar el segundo equipo conforme a la indicación telefónica del despacho y dejar constancia en el acta de que la ampliación fue solicitada verbalmente durante la diligencia.',
   'Abstenerse de revisarlo y no mencionarlo, porque referirse a un servidor no vinculado a la investigación podría afectar sus derechos sin que exista actuación abierta en su contra.',
   'No revisarlo, dejar constancia escrita de lo observado y poner el hecho en conocimiento del competente, indicando que una ampliación del objeto requiere delegación escrita.',
   'Revisarlo de manera preliminar y sin levantar acta, de modo que el despacho tenga el dato para decidir si amplía formalmente el objeto de la prueba técnica ya delegada.'],
  'La delegación delimita el objeto y una indicación telefónica no la amplía. Lo correcto es no revisar, consignar por escrito lo observado y poner el hecho en conocimiento del competente, que decidirá si amplía la delegación.',
  'Actuar por indicación verbal deja la prueba expuesta a exclusión; una revisión «preliminar sin acta» es una actuación sin registro; y omitir el hecho priva al competente de información que usted ya observó.'),

 (0,
  'Usted apoya técnicamente una diligencia de testimonio. El testigo entrega una versión que contradice abiertamente lo que había consignado por escrito semanas antes. Al terminar, el servidor del despacho le pregunta cuál de las dos versiones le pareció más creíble, porque quiere orientar la evaluación del expediente. El acta aún no se ha cerrado. El testigo se retiró hace unos minutos y el servidor del despacho debe rendir la evaluación esta semana.',
  '¿Cuál es la actuación correcta?',
  ['Dejar constancia fiel y completa de las dos versiones, sin omitir ninguna y sin ordenarlas por credibilidad, y describir lo observado si le preguntan, sin concluir cuál prevalece.',
   'Consignar la versión más reciente, que es la que el testigo sostuvo bajo la formalidad de la diligencia, y anotar que existe una manifestación anterior de contenido distinto.',
   'Indicar cuál versión le pareció más creíble, ya que usted estuvo presente y puede apreciar elementos de la declaración que el servidor competente no podrá valorar después.',
   'Consignar ambas versiones y añadir una nota técnica señalando las contradicciones concretas entre ellas y cuál de los dos relatos resulta más consistente con el material examinado.'],
  'Ambas versiones se consignan completas y sin jerarquía de credibilidad. Valorar cuál prevalece es del competente. Describir lo observado está bien; concluir cuál es creíble, no.',
  'Privilegiar la versión reciente ya es valorar; opinar sobre credibilidad invade la valoración probatoria; y «señalar cuál relato es más consistente» es lo mismo con otras palabras.'),

 (3,
  'Al revisar un expediente que debe apoyar técnicamente, usted advierte que el pliego de cargos fue notificado por un medio que, según el procedimiento, no era el procedente para ese caso. El expediente está próximo a la etapa de fallo. Un compañero le dice que no es asunto suyo, que usted es técnico y que señalarlo podría leerse como un cuestionamiento al despacho. El expediente llegó a la Dirección ayer y el informe técnico se rinde pasado mañana, con sus anexos.',
  '¿Qué corresponde hacer?',
  ['No intervenir, porque las nulidades procesales son materia del operador disciplinario y una observación del técnico sobre el trámite excede por completo el alcance de su función.',
   'Declarar la irregularidad en su informe técnico y abstenerse de rendirlo hasta que el despacho sanee la notificación, para que su trabajo no quede comprometido por el vicio.',
   'Comentarlo verbalmente al servidor del despacho para que lo corrija discretamente, evitando que quede en el expediente un registro que exponga el error ante la segunda instancia.',
   'Dejar constancia escrita de la irregularidad concreta observada e informarla por el canal al competente, sin declarar nulidad alguna, para que él valore si procede sanearla.'],
  'Las nulidades no las declara el técnico, pero sí es quien está en posición de advertirlas. Una nulidad advertida antes del fallo se corrige; advertida después, puede costar el proceso. Se deja constancia escrita y se informa al competente.',
  'Callar deja correr un vicio que usted vio; declarar la nulidad o condicionar el informe a que se sanee invade competencia ajena; y comentarlo de palabra no deja rastro: para el expediente, no ocurrió.'),

 (1,
  'Un compañero sostiene que la Ley 2094 de 2021 «reemplazó» al Código General Disciplinario y que, por tanto, todas las citas deben hacerse a esa ley. Otro responde que la Ley 2094 solo cambió unos plazos. El jefe pide precisión porque el informe debe citar correctamente la norma aplicable al procedimiento. La duda surgió preparando el informe y el jefe quiere que la cita normativa quede impecable, porque el documento sale a otra dependencia.',
  '¿Cuál es la precisión correcta?',
  ['La Ley 2094 de 2021 derogó la Ley 1952 de 2019 y es hoy el Código General Disciplinario, de modo que toda referencia normativa debe hacerse exclusivamente a la Ley 2094.',
   'La Ley 2094 de 2021 modificó la Ley 1952 de 2019 —que sigue siendo el Código General Disciplinario— y reforzó garantías del procedimiento, entre ellas la doble instancia.',
   'La Ley 2094 de 2021 es una norma reglamentaria del Código General Disciplinario, por lo que las citas deben hacerse a la Ley 1952 y nunca a la Ley 2094, que carece de rango legal.',
   'La Ley 2094 de 2021 restableció parcialmente la vigencia de la Ley 734 de 2002, hoy derogada, para los procesos iniciados antes del 29 de marzo de 2022 y aún no fallados.'],
  'La Ley 2094 de 2021 modificó la Ley 1952 de 2019, que continúa siendo el Código General Disciplinario, y reforzó garantías del procedimiento, entre ellas la doble instancia. Se citan las dos, según el punto.',
  'No derogó la Ley 1952 ni es reglamentaria de ella, y nada restableció la vigencia de la Ley 734 de 2002, que quedó derogada con la entrada en vigencia plena del nuevo código.'),

 (2,
  'El informe técnico que usted debe rendir vence el viernes. Es martes y usted ya sabe, por el volumen del material, que no alcanzará a rendirlo con el rigor que exige. El despacho tiene un término de instrucción corriendo. Un compañero le dice que espere al viernes para avisar, «porque a lo mejor alcanzas y no vale la pena generar alarma antes de tiempo». Nadie más del grupo está disponible para asumir parte del material y el despacho no ha preguntado por el avance.',
  '¿Cuándo y cómo debe advertirlo?',
  ['El viernes, cuando ya sea seguro que no alcanzará, informando ese mismo día al despacho para que disponga lo que corresponda respecto del término de instrucción en curso.',
   'El viernes, rindiendo un informe más breve que cumpla formalmente el término y anunciando que ampliará el análisis en un documento complementario la semana siguiente.',
   'Ahora, por escrito y por el canal institucional, exponiendo la razón y el impacto en el término, para que el servidor competente pueda disponer lo que corresponda a tiempo.',
   'Ahora, pero verbalmente a su jefe inmediato, que es quien debe trasladar la situación al despacho si lo considera necesario para el trámite del expediente en curso.'],
  'Un apoyo que no alcanzará se advierte en cuanto se ve venir, por escrito y por el canal: solo así el competente conserva margen para disponer algo. Avisar el día del vencimiento le quita a él la posibilidad de reaccionar.',
  'Esperar al viernes consume el margen de maniobra; un informe breve «para cumplir» sacrifica el rigor que es la razón de ser del apoyo; y un aviso verbal no deja constancia de que usted advirtió a tiempo.'),

 (0,
  'Practicando una prueba técnica delegada, usted documenta hechos que apuntan a un posible delito. El objeto de su delegación es disciplinario y no cubre esa materia. Un compañero le propone que remita copia del informe a la Fiscalía apenas lo termine, «porque el delito no espera y la PGN no es competente para eso». El informe se rinde pasado mañana. La diligencia terminó esta mañana, usted conserva el registro fotográfico y el acta ya está firmada por los intervinientes.',
  '¿Cuál es la actuación correcta?',
  ['Describir los hechos observados en el informe, sin calificarlos jurídicamente, y ponerlos por escrito en conocimiento del servidor competente, a quien corresponde decidir la compulsa.',
   'Remitir copia del informe a la Fiscalía e informar de ello al despacho solicitante, ya que la competencia penal corresponde a esa entidad y la demora podría afectar la investigación.',
   'Omitir esos hechos del informe disciplinario y elaborar un documento separado dirigido al despacho, para que el expediente no contenga material ajeno al objeto de la delegación.',
   'Ampliar la prueba técnica para precisar los elementos penales, de modo que, si el competente decide compulsar copias, la Fiscalía reciba el hallazgo con soporte suficiente.'],
  'La regla única vale también aquí: describir sin calificar, consignar por escrito y poner en conocimiento del competente, que decide la compulsa. La remisión a la Fiscalía no es una decisión del técnico.',
  'Remitir por su cuenta usurpa una decisión ajena; omitir los hechos del informe compromete la veracidad; y ampliar la prueba excede el objeto de la delegación.'),

 (3,
  'El despacho le pide que, además del informe técnico, proyecte el auto por el cual se ordena incorporar las pruebas practicadas al expediente. Es la primera vez que le piden proyectar un auto. Un compañero le advierte que tenga cuidado «porque al firmarlo asume responsabilidad». Usted tiene claro el contenido y el formato institucional del documento. El despacho envió el modelo del auto por correo y el jefe de grupo está de comisión hasta el viernes.',
  '¿Cuál es la precisión correcta sobre proyectar?',
  ['Proyectar implica asumir la responsabilidad del contenido del auto, por lo que debe abstenerse si no tiene plena certeza jurídica sobre lo que el documento dispone.',
   'Proyectar es redactar y además suscribir el auto en calidad de quien lo elaboró, de modo que el documento tenga dos firmas: la del proyectante y la del servidor competente.',
   'Proyectar es una función ajena al cargo técnico y debe declinarse, porque la redacción de autos corresponde a los cargos del nivel profesional dentro de cada dependencia.',
   'Proyectar es redactar el borrador conforme a la estructura exigida y a las instrucciones recibidas; el documento es borrador hasta que el competente lo revisa, ajusta y firma.'],
  'Proyectar autos, conceptos y actos administrativos para la firma del servidor competente es función expresa de su manual. El borrador es borrador: quien asume la responsabilidad jurídica es quien lo revisa y lo firma.',
  'Ni proyectar traslada la responsabilidad jurídica al proyectante, ni el auto lleva su firma, ni es una función ajena al cargo: está expresamente en el manual de funciones.'),

 (1,
  'Usted debe presentar las pruebas practicadas y sus anexos ante el despacho. El material incluye un anexo digital extenso que el canal institucional no admite por su tamaño. El servidor del despacho le pide que se lo envíe por correo personal «para no demorar», porque necesita revisarlo antes de la evaluación del expediente, que es pasado mañana. La evaluación del expediente está programada para pasado mañana y el anexo pesa más de lo que el canal admite por envío.',
  '¿Cómo debe proceder?',
  ['Enviarlo por correo personal dado el carácter excepcional de la situación, y dejar constancia en el informe de que el envío se hizo por esa vía y por esa razón concreta.',
   'Remitir el informe y los anexos por el canal institucional, gestionar por el canal interno la entrega del anexo extenso, e informar al despacho ambas cosas, dejando constancia.',
   'Fraccionar el anexo en varios envíos por el canal institucional hasta completarlo, aunque ello implique dividir un documento único en partes que deberán recomponerse después.',
   'Entregar el anexo en medio físico directamente al servidor del despacho, sin registrar la entrega, porque se trata de una actuación material que no requiere trámite documental.'],
  'El canal institucional da trazabilidad y no se sustituye por uno personal. La necesidad real se atiende por una vía compatible —gestión interna para el anexo extenso— y todo queda informado y con constancia.',
  'Un correo personal rompe la trazabilidad por mucha urgencia que haya; fraccionar un documento único lo degrada; y una entrega física sin registro, para el expediente, no ocurrió.'),

 (2,
  'Una persona que dice ser familiar del investigado llama a la Dirección preguntando si ya se practicó la prueba técnica y qué arrojó. El expediente está en instrucción: no se ha formulado pliego de cargos ni se ha ordenado archivo. La persona es insistente y menciona que el investigado está muy angustiado. La llamada entró al teléfono de la Dirección y usted es quien está atendiendo en ese momento, sin nadie más disponible.',
  '¿Cuál es la actuación correcta?',
  ['Confirmarle únicamente si la prueba ya se practicó, sin revelar su resultado, porque la existencia de una diligencia no constituye por sí misma información sometida a reserva.',
   'Verificar si el investigado autorizó a esa persona y, en caso afirmativo, darle la información, ya que se trata de información del propio proceso del investigado.',
   'No suministrar información por esa vía, indicar el canal formal por el que el interesado o su apoderado pueden solicitarla, y dejar constancia de la llamada recibida.',
   'Remitirla al despacho que lleva la investigación sin dejar registro de la llamada, porque es ese despacho y no la DNIE el que debe responder sobre el estado de la actuación.'],
  'En el procedimiento disciplinario las actuaciones son reservadas hasta que se cite a audiencia y se formule pliego de cargos o se ordene el archivo definitivo, sin perjuicio de los derechos de los sujetos procesales. Se indica el canal y se deja constancia.',
  'Confirmar que la diligencia existe ya revela información de la actuación reservada; una autorización informal del investigado no habilita el acceso por teléfono; y remitir sin registrar deja la solicitud sin rastro.'),

 (0,
  'El despacho le anticipa que el pliego de cargos se formulará sobre un hecho concreto y le pide que el informe técnico «se centre en eso y no se disperse». Usted documentó ese hecho y, además, otros dos hallazgos verificables relacionados con la misma diligencia que el pliego no contempla. El informe debe rendirse mañana. El despacho se lo dijo por teléfono esta mañana y usted tiene el borrador del informe con los tres hallazgos ya descritos.',
  '¿Cómo debe rendir el informe?',
  ['Con la descripción completa de todo lo documentado, incluidos los otros dos hallazgos, porque el informe debe reflejar lo que la diligencia arrojó, no lo que el pliego contemplará.',
   'Centrado en el hecho que será objeto del pliego, para respetar el principio de congruencia entre el pliego de cargos y el fallo que posteriormente se adopte en el proceso.',
   'Centrado en ese hecho y mencionando los otros dos de manera general, sin detalle, para no condicionar la calificación que el despacho ya anunció sobre el objeto del proceso.',
   'Con la descripción completa, pero advirtiendo en el informe que los dos hallazgos adicionales no deben ser tenidos en cuenta por quedar fuera del objeto del pliego de cargos.'],
  'El informe refleja lo que la diligencia arrojó. La congruencia opera entre el pliego y el fallo, y es asunto del operador disciplinario: no es una razón para que el técnico recorte lo que documentó.',
  'Recortar o mencionar «de manera general» filtra la prueba; y decirle al despacho qué no debe tener en cuenta es, otra vez, decidir por él.'),

 (3,
  'Durante la práctica de una prueba técnica, el investigado le manifiesta que quiere rendir versión libre allí mismo, ante usted, porque «está dispuesto a contarlo todo». Nadie del despacho está presente. El objeto de su delegación es practicar una prueba técnica sobre un elemento. El investigado insiste en que puede arrepentirse después. La diligencia continúa, hay dos personas más presentes y el acta todavía no se ha cerrado ni firmado.',
  '¿Qué corresponde hacer?',
  ['Recibir la versión libre y remitirla con el informe, ya que se trata de una garantía del investigado y negarse podría leerse como una restricción de su derecho de defensa.',
   'Recibir la manifestación por escrito sin darle el carácter de versión libre, para preservar el contenido sin asumir una actuación procesal que no le fue delegada.',
   'Explicarle que no puede recibirla, continuar la diligencia y no dejar ninguna anotación al respecto, para no incorporar al expediente una actuación que no llegó a producirse.',
   'Informarle que la versión libre se rinde ante el servidor competente y por el procedimiento previsto, dejar constancia en el acta de su manifestación, y continuar la prueba delegada.'],
  'La versión libre es una garantía del investigado que se rinde ante el competente y por el procedimiento previsto. Lo que corresponde es informárselo, dejar constancia de que lo manifestó —para que el competente lo sepa— y continuar con lo delegado.',
  'Recibirla, con o sin el nombre de versión libre, es asumir una actuación procesal ajena. Y no dejar constancia alguna borra del expediente una manifestación relevante que el competente debería conocer.'),

 (1,
  'El fallo de primera instancia fue notificado y el investigado interpuso recurso de apelación. El despacho de segunda instancia pide a la DNIE una ampliación del informe técnico que usted rindió en la instrucción. Un compañero dice que no procede, «porque el apoyo técnico se agota con el informe inicial y en segunda instancia ya no se puede intervenir». La solicitud llegó por correo oficial, firmada por el servidor del despacho de segunda instancia, y pide respuesta en cinco días.',
  '¿Cuál es la precisión correcta?',
  ['Su compañero tiene razón: el apoyo técnico se agota con el informe rendido en la instrucción, de modo que la solicitud debe devolverse por improcedente al despacho de segunda instancia.',
   'La DNIE presta apoyo técnico a las dependencias que lo soliciten, y la doble instancia que reforzó la Ley 2094 de 2021 supone un despacho de segunda instancia que también puede requerirlo.',
   'Procede únicamente si el investigado lo solicita expresamente en el recurso de apelación, ya que de lo contrario se estaría ampliando de oficio el material probatorio en su contra.',
   'Procede, pero sin necesidad de nueva delegación, porque la delegación otorgada en la instrucción cubre todas las actuaciones derivadas del mismo expediente disciplinario.'],
  'El apoyo técnico se presta a las dependencias que lo soliciten, y la doble instancia reforzada por la Ley 2094 de 2021 supone un despacho de segunda instancia que puede requerirlo. Lo que no cambia es el mecanismo: hace falta delegación del competente.',
  'Ni el apoyo se agota con el primer informe, ni depende de que lo pida el investigado, ni la delegación anterior cubre automáticamente una actuación nueva.'),

 (2,
  'Usted mantiene actualizado el registro de los apoyos técnicos en el sistema de información. Advierte que un apoyo rendido hace dos semanas figura como «pendiente» porque nunca se cargó el acta de cierre, y que el expediente avanzó igual. El jefe de grupo está de permiso y el servidor del despacho dice que «no importa, porque el informe sí llegó». El sistema permite corregir el estado y el acta de cierre sigue guardada, sin cargar, en su carpeta de trabajo.',
  '¿Qué corresponde hacer?',
  ['Nada: si el informe llegó y el expediente avanzó, el estado en el sistema es un dato administrativo interno que no afecta la validez de la actuación ni los derechos de nadie.',
   'Cambiar el estado a «rendido» y cargar el acta de cierre con la fecha de hoy, de modo que el registro quede coherente con la actuación que efectivamente se cumplió en su momento.',
   'Cargar el acta con su fecha real, corregir el estado conforme al procedimiento y dejar constancia de la demora en el cargue, informándolo por el canal institucional.',
   'Esperar a que el jefe de grupo regrese de su permiso y plantearle entonces la situación, para que sea él quien decida cómo regularizar el registro del apoyo en el sistema.'],
  'El registro no es un dato interno sin consecuencias: es la trazabilidad de la actuación. Se carga el acta con su fecha real, se corrige el estado por el procedimiento y se deja constancia de la demora, que es un hecho que también debe quedar documentado.',
  'Dejarlo así perpetúa un registro que no refleja la realidad; cargar el acta con fecha de hoy falsea el dato; y esperar al regreso del jefe prolonga una inconsistencia que ya está en el sistema.'),

 (3,
  'Faltan nueve días para la prueba escrita. En los simulacros usted acierta las preguntas sobre etapas del procedimiento, pero falla las que le piden ubicar qué puede pedírsele en cada una: confunde lo que hace el operador disciplinario con lo que le toca a usted. Su registro muestra el mismo error en cinco de los últimos ocho casos resueltos. Lleva un registro de los simulacros resueltos y puede ver exactamente en qué opción cayó cada vez que falló.',
  '¿Cuál es la mejor manera de corregirlo?',
  ['Memorizar los términos de cada etapa del procedimiento, porque la mayoría de estas preguntas se resuelven identificando correctamente el plazo aplicable a la actuación descrita.',
   'Repasar las etapas hasta dominarlas de memoria, confiando en que la distinción de roles se deducirá sola una vez que el mapa del procedimiento esté completamente claro.',
   'Resolver más simulacros del bloque disciplinario hasta que la intuición mejore, dejando el repaso de las etapas para los días inmediatamente anteriores a la presentación.',
   'Leer cada caso ubicando primero la etapa y preguntándose después quién actúa —operador o técnico—, y descartar toda opción que le atribuya a usted una decisión de trámite.'],
  'El error no está en las etapas sino en el reparto de roles dentro de ellas. Ubicar la etapa y preguntarse enseguida quién actúa convierte en visible lo que hoy se confunde, y descarta de entrada las opciones que le atribuyen decisiones de trámite.',
  'Memorizar términos o etapas no corrige una confusión de roles; y repetir simulacros sin cambiar el método repite el mismo error ocho veces más.'),
]
