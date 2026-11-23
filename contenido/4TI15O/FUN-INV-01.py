# -*- coding: utf-8 -*-
"""Día 16 · Investigación criminal I: derecho penal aplicado al control y la frontera falta/delito — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol, modulos, armar

META = dict(
    codigo='FUN-INV-4TI15O-01',
    archivo='FUN-INV-4TI15O-01-investigacion-criminal-delito-falta.html',
    dia=16,
    titulo_doc='Investigación criminal I: la frontera entre falta y delito',
    h1='Investigación criminal I<br>Falta y delito',
    kicker='Día 16 · Conocimientos específicos',
    sub='Practicando una prueba técnica usted va a encontrarse, tarde o temprano, con un hecho que <strong>además</strong> puede ser delito. Este día le da el marco para reconocerlo sin invadir competencia ajena: el <strong>ius puniendi</strong> y la diferencia entre lo penal y lo disciplinario, los <strong>principios del derecho penal</strong> y su paralelo disciplinario, la <strong>conducta punible</strong> (dolo, culpa y preterintención), los <strong>delitos contra la administración pública</strong> que más aparecen en el control, el <strong>prevaricato</strong>, las causales de ausencia de responsabilidad, la <strong>autoría y participación</strong>, y —el módulo que más le va a servir— qué ocurre <strong>cuando un mismo hecho es falta y delito</strong>.',
    badges=['⏱ 110-130 min', '⚖️ Penal y disciplinario', '🔍 Investigación'],
    fmeta='Investigación criminal I: derecho penal aplicado al control y la frontera entre falta y delito',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Investigación criminal I: la frontera entre falta y delito',
)

FUENTE = 'guias/FUN-PEN-3PU17L-02-derecho-penal-procesal-penal.html'
SEC = secciones_mapeadas(FUENTE)

# el proceso penal y sus etapas (módulos 8, 9 y 10) se trabajan el día 17
CAB, MODS = modulos(SEC[2])
SEC[2] = armar(CAB, MODS, {1, 2, 3, 4, 5, 6, 7, 11, 12, 13})

# ---------------------------------------------------------------- módulo nuevo
QUE_DOCUMENTA = '''<h3><span class="h3-chip">0</span> Qué documenta un técnico cuando el hecho puede ser delito</h3>
  <p>Conviene empezar por el final, porque es lo que da sentido a todo lo que viene después. Usted no investiga delitos: practica pruebas técnicas en actuaciones disciplinarias. Entonces, ¿para qué estudiar derecho penal? Por una razón muy concreta y muy práctica: <mark>para reconocer lo que tiene delante sin cruzar la línea</mark>. Un técnico que no distingue un posible delito de una irregularidad administrativa hace una de dos cosas, y las dos son errores: o lo pasa por alto, y el hecho se pierde; o lo persigue, y se extralimita.</p>
  <h4>La regla de tres pasos</h4>
  <div class="flujo">
    <div class="flujo-paso"><div class="fp-n">1</div><div><b>Reconocer</b><p>Saber que lo que acaba de documentar <em>podría</em> encajar en un tipo penal —un peculado, un prevaricato, una falsedad— sin afirmarlo. Para eso sirve conocer los tipos: para no pasarlos por alto.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">2</div><div><b>Describir sin calificar</b><p>Consignar el hecho observado, el método con que lo estableció y las condiciones en que ocurrió. <strong>Nunca</strong> escribir el nombre del delito ni afirmar que la conducta lo constituye.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">3</div><div><b>Poner en conocimiento</b><p>Informarlo por escrito al servidor competente, que es quien decide si se compulsan copias a la Fiscalía. La remisión no es una decisión del técnico.</p></div></div>
  </div>
  <div class="tabla-wrap">
    <table>
      <caption>Qué sí y qué no escribe el Técnico Investigador</caption>
      <thead><tr><th>Sí</th><th>No</th></tr></thead>
      <tbody>
        <tr><td>«Los registros de los folios 14 a 19 presentan enmendaduras en la cifra, con tinta de distinta composición.»</td><td>«Se configuró una falsedad en documento público.»</td></tr>
        <tr><td>«El equipo fue retirado del inventario sin soporte de salida; el acta de baja no aparece en el expediente.»</td><td>«El servidor se apropió del bien, incurriendo en peculado.»</td></tr>
        <tr><td>«La resolución se profirió el 12 de marzo; la norma citada en ella fue derogada el 3 de enero anterior.»</td><td>«Hubo prevaricato por acción.»</td></tr>
        <tr><td>«Los hechos descritos se ponen en conocimiento del servidor competente para lo de su cargo.»</td><td>«Se compulsan copias a la Fiscalía General de la Nación.»</td></tr>
      </tbody>
    </table>
  </div>
  <p>Fíjese en la columna izquierda: es <strong>más útil</strong> que la derecha, no menos. Una descripción precisa de enmendaduras con tinta de distinta composición le sirve a quien decide mucho más que la palabra «falsedad», porque la palabra es una conclusión que él debe poder verificar, y lo que usted le entrega es justamente aquello con lo que la verificará.</p>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Hay un distractor que aparece una y otra vez en este bloque: la opción que propone <strong>remitir directamente a la Fiscalía</strong> «para ganar tiempo» o «porque es la competente». Suena diligente y es incorrecta: la compulsa de copias la decide el servidor competente. Lo del técnico es <strong>describir, consignar por escrito y poner en conocimiento</strong>.</p></div>
  <h4>Y la otra mitad: por qué el expediente disciplinario no se cierra</h4>
  <p>El otro error frecuente es el contrario: creer que, si aparece un posible delito, lo disciplinario se detiene o se traslada. No. Las acciones son <strong>independientes</strong>: lo penal valora el delito, lo disciplinario la afectación del deber funcional, con objetos y estándares distintos. Su apoyo técnico continúa, el término sigue corriendo y el informe se rinde igual. Lo verá desarrollado en el módulo sobre la compulsa de copias.</p>
  <div class="checkpoint" data-cp="0">
    <div class="cp-q">✋ Punto de control: usted documenta un hecho que podría ser delito. ¿Qué escribe en el informe?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">El nombre del tipo penal que, a su juicio técnico, encajaría con el hecho documentado.</button>
    <button class="cp-opt" data-ans="1">El hecho observado, el método con que lo estableció y las condiciones en que ocurrió, poniéndolo en conocimiento del competente sin calificarlo.</button>
    <button class="cp-opt" data-ans="0">Nada sobre ese hecho: al exceder el objeto disciplinario, corresponde omitirlo del informe técnico.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  '''

R = [('<h3><span class="h3-chip">1</span>', QUE_DOCUMENTA + '<h3><span class="h3-chip">1</span>')]
SEC = aplicar_todas(SEC, R, estricto=True)

SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>', '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>', '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('Profesional Universitario 3PU-17', 'Técnico Investigador 4TI-15'),
    ('Profesional Universitario, código 3PU-17', 'Técnico Investigador, código 4TI-15'),
    ('Profesional Universitario', 'Técnico Investigador'),
    ('(3PU-17)', '(4TI-15)'), ('3PU-17', '4TI-15'), ('3PU17L', '4TI15O'), ('3PU', '4TI'),
    ('146-2026', '257-2026'),
    ('Procuradurías de Instrucción', 'dependencias que solicitan apoyo técnico'),
    ('Procuraduría de Instrucción', 'Dirección Nacional de Investigaciones Especiales'),
    ('El instructor', 'El servidor que instruye'), ('el instructor', 'el servidor que instruye'),
    ('al instructor', 'al servidor que instruye'), ('del instructor', 'del servidor que instruye'),
    ('un instructor', 'un servidor que instruye'), ('Un instructor', 'Un servidor que instruye'),
    ('instructor', 'servidor que instruye'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)

METODOLOGIA = '''<h3><span class="h3-chip">N</span> Metodología del apoyo técnico: el programa, el lugar y la secuencia</h3>
  <p>Hasta aquí hemos visto <em>qué</em> puede aparecer en una diligencia. Conviene cerrar con el <em>cómo</em>: la manera de planear un apoyo técnico para que lo que aparezca pueda aprovecharse. Su manual de funciones lo dice expresamente: <strong>establecer con las dependencias la metodología para adelantar las investigaciones</strong>. No es una formalidad previa: es lo que separa una diligencia que produce prueba de una que produce un acta con buenas intenciones.</p>
  <h4>El programa metodológico: cuatro preguntas antes de salir</h4>
  <p>Antes de cualquier diligencia, el apoyo se acuerda sobre cuatro preguntas. Si alguna queda sin responder, la diligencia sale mal:</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Pregunta</th><th>Qué define</th><th>Qué pasa si no se responde</th></tr></thead>
      <tbody>
        <tr><td><strong>¿Qué se quiere establecer?</strong></td><td>El objetivo técnico concreto del apoyo, en términos verificables.</td><td>Se recolecta de más o de menos, y el informe no responde lo que el despacho necesitaba.</td></tr>
        <tr><td><strong>¿Con qué técnica?</strong></td><td>El procedimiento aplicable y sus limitaciones conocidas de antemano.</td><td>Se descubre en el lugar que la técnica no sirve, cuando ya no hay margen.</td></tr>
        <tr><td><strong>¿Sobre qué, y dónde está?</strong></td><td>Los elementos concretos, su ubicación y quién los custodia.</td><td>Se llega y el material no está disponible, o está en poder de quien no fue advertido.</td></tr>
        <tr><td><strong>¿Con qué título?</strong></td><td>La delegación escrita y su alcance exacto.</td><td>Lo actuado queda expuesto a inexistencia, por bien hecho que esté técnicamente.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>El lugar: tres reglas que valen para cualquier especialidad</h4>
  <div class="flujo">
    <div class="flujo-paso"><div class="fp-n">1</div><div><b>Primero observar, después tocar</b><p>El estado inicial solo existe una vez. Se documenta —descripción, registro fotográfico, posición y condiciones— <strong>antes</strong> de manipular nada. Lo que se altera para «ver mejor» ya no se puede volver a ver.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">2</div><div><b>De lo general a lo particular</b><p>Se registra primero el conjunto y el contexto, y después el detalle. Un detalle sin contexto es un dato que nadie puede ubicar; el contexto sin detalle es una descripción que no acredita nada.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">3</div><div><b>Nada sale sin registro</b><p>Cada elemento que se recolecta queda individualizado, rotulado e inventariado <strong>en el lugar</strong>. Lo que se decide «anotar después» es, en la práctica, lo que se anota de memoria.</p></div></div>
  </div>
  <h4>Cuando el lugar no coopera</h4>
  <p>La diligencia real rara vez se parece a la planeada: el material no está completo, alguien se opone, el sistema no abre, el horario se acaba. La metodología no desaparece por eso; lo que cambia es que <strong>la desviación se documenta</strong>. Una diligencia que se apartó del plan y lo explicó con precisión sigue siendo utilizable; una que se apartó y no lo dijo queda a merced de la primera contradicción de la defensa.</p>
  <div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> El programa metodológico preveía examinar cinco equipos. Al llegar, dos están en reparación fuera de la sede y uno fue dado de baja hace un mes. Usted puede examinar los otros dos hoy.</p>
    <p><strong>Cómo proceder.</strong> Examinar los dos disponibles, consignar con precisión qué pasó con los otros tres —quién lo informó, qué soporte existe, dónde estarían— y precisar en el informe qué puede y qué no puede sostenerse con el material efectivamente examinado. Eso es una diligencia bien hecha, no una diligencia fallida.</p>
  </div>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Ante una diligencia que se desvía de lo planeado, las opciones correctas casi nunca son «suspender» ni «improvisar una alternativa». Suelen ser: <strong>hacer lo que sí es posible, documentar con precisión lo que no, e informar</strong>. La misma estructura que ya reconoce de los días anteriores.</p></div>

  '''
SEC[2] = SEC[2].rstrip() + "\n\n  " + METODOLOGIA + "\n"

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre la frontera '
              'entre falta disciplinaria y delito: qué documenta el técnico cuando el hecho puede ser punible, la '
              'diferencia entre lo penal y lo disciplinario, los delitos contra la administración pública, el '
              'prevaricato, la independencia de las acciones y la compulsa de copias.')

P = [
 (1,
  'Practicando una prueba técnica sobre un expediente, usted documenta que una resolución cita como fundamento una norma que había sido derogada seis meses antes de que la resolución se profiriera. El despacho solicitante le dice que lo consigne como prevaricato por acción, «porque es evidente que el servidor resolvió contra derecho». Usted puede acreditar la fecha de la resolución, la de la derogatoria y el texto citado. El informe vence pasado mañana.',
  '¿Cómo debe redactarse el informe?',
  ['Consignando que la conducta configura prevaricato por acción, ya que los elementos objetivos están plenamente acreditados y el técnico puede constatar esa correspondencia.',
   'Consignando la fecha de la resolución, la de la derogatoria y el texto citado, sin nombrar el tipo penal, y poniendo el hecho en conocimiento del servidor competente.',
   'Consignando que la conducta «podría constituir» prevaricato, de modo que el despacho disponga de la calificación como hipótesis sin que el informe la afirme de forma categórica.',
   'Omitiendo el punto del informe técnico, por exceder el objeto disciplinario de la prueba delegada, y comunicándolo verbalmente al despacho para que decida qué hacer con él.'],
  'La descripción precisa —fechas, derogatoria, texto citado— es más útil que la palabra «prevaricato», porque es con lo que el competente verificará la calificación. Nombrar el tipo penal es calificar, y eso no le corresponde.',
  'Calificar, aunque sea con un «podría», invade competencia ajena. Pero omitir el hallazgo compromete la veracidad del informe, y comunicarlo de palabra no deja rastro en el expediente.'),

 (3,
  'Un compañero sostiene que, si la Fiscalía archiva el proceso penal por los mismos hechos, el expediente disciplinario debe archivarse también, «porque si no hubo delito tampoco hubo falta». Otro responde que son cosas distintas pero no sabe explicar por qué. El jefe pide la precisión porque el informe técnico debe explicar por qué el apoyo continúa pese al archivo penal. El archivo penal se notificó la semana pasada y el término de instrucción disciplinaria sigue corriendo.',
  '¿Cuál es la precisión correcta?',
  ['El archivo penal obliga al archivo disciplinario cuando versa sobre los mismos hechos, porque lo contrario implicaría juzgar dos veces a la misma persona por una sola conducta.',
   'El archivo penal obliga al archivo disciplinario solo cuando se fundó en que el hecho no existió; si se fundó en atipicidad, el expediente disciplinario puede continuar su curso.',
   'El archivo penal suspende la actuación disciplinaria hasta que quede ejecutoriado, momento en el cual el despacho decide si continúa o archiva el expediente que venía tramitando.',
   'Las acciones son independientes: lo penal valora el delito y lo disciplinario la afectación del deber funcional, con objetos y estándares distintos, de modo que el apoyo técnico continúa.'],
  'La independencia de las acciones es el principio que resuelve el caso: una conducta puede no ser delito y sí afectar sustancialmente el deber funcional. Por eso el archivo penal no cierra el expediente disciplinario ni suspende el apoyo.',
  'No hay doble juzgamiento porque no son la misma acción ni el mismo objeto; y ni el fundamento del archivo penal ni su ejecutoria condicionan la actuación disciplinaria.'),

 (0,
  'Durante una diligencia usted documenta que un equipo salió del inventario sin soporte de salida y que el acta de baja no aparece en el expediente. El servidor del despacho le dice que remita copia del hallazgo directamente a la Fiscalía, «porque esto es peculado y la PGN no es competente para lo penal, así ganamos tiempo». El informe debe rendirse en dos días y usted tiene el hallazgo plenamente documentado. El hallazgo quedó registrado en el acta, con fotografías del inventario y del espacio donde debía estar el equipo.',
  '¿Cuál es la actuación correcta?',
  ['Describir el hallazgo en el informe sin calificarlo y ponerlo por escrito en conocimiento del servidor competente, a quien corresponde decidir si se compulsan copias.',
   'Remitir copia del hallazgo a la Fiscalía e informar de ello al despacho, dado que la competencia penal es de esa entidad y la demora podría afectar la investigación penal.',
   'Omitir el hallazgo del informe disciplinario y elaborar un documento separado dirigido a la Fiscalía, para que el expediente no contenga material de naturaleza penal.',
   'Ampliar la prueba técnica para precisar los elementos del posible peculado, de modo que la Fiscalía reciba el hallazgo con el soporte técnico suficiente para actuar.'],
  'La compulsa de copias la decide el servidor competente, no el técnico. La conducta correcta es siempre la misma: describir sin calificar, consignar por escrito y poner en conocimiento.',
  'Remitir por cuenta propia usurpa una decisión ajena; omitir el hallazgo compromete la veracidad; y ampliar la prueba excede el objeto de la delegación.'),

 (2,
  'En una capacitación surge la pregunta de qué distingue el derecho penal del disciplinario, porque varios del grupo los usan como sinónimos. El jefe pide que el punto quede claro antes de abordar los delitos contra la administración pública, y quiere una formulación que el equipo pueda repetir. Varios del grupo llevan poco tiempo en la entidad y el jefe quiere una formulación corta que todos puedan repetir en la prueba.',
  '¿Cuál es la distinción correcta?',
  ['El penal sanciona conductas graves y el disciplinario conductas leves, de modo que la diferencia entre ambos es de gravedad de la conducta y de severidad de la sanción impuesta.',
   'El penal se aplica a particulares y el disciplinario a servidores públicos, por lo que un mismo hecho nunca puede ser objeto de las dos actuaciones de manera simultánea.',
   'El penal protege bienes jurídicos mediante el ius puniendi y sanciona la conducta punible; el disciplinario protege el correcto ejercicio de la función pública y sanciona la afectación del deber funcional.',
   'El penal exige dolo y el disciplinario admite solo la culpa, razón por la cual las conductas intencionales se tramitan siempre por la vía penal y nunca por la disciplinaria.'],
  'Lo que diferencia a las dos manifestaciones del ius puniendi es su objeto: el delito y el bien jurídico protegido frente a la falta y la afectación del deber funcional. De ahí se sigue todo lo demás, empezando por la independencia de las acciones.',
  'Ni la diferencia es de gravedad, ni los destinatarios son excluyentes —hay particulares disciplinables—, ni el elemento subjetivo reparte las vías: el régimen disciplinario admite dolo y culpa.'),

 (1,
  'Usted documenta que un servidor omitió proferir una decisión que legalmente debía adoptar y que el término venció hace cuatro meses. Un compañero comenta que eso «no es nada penal, porque no hizo nada», y otro que podría serlo. El informe debe rendirse esta semana y el jefe quiere que el equipo entienda el punto. El expediente está en instrucción, el despacho espera el informe esta semana y usted tiene las fechas acreditadas.',
  '¿Qué precisión conviene tener clara sobre el prevaricato?',
  ['Que solo existe el prevaricato por acción: se configura con una decisión manifiestamente contraria a la ley, y una omisión nunca puede dar lugar a esa conducta punible.',
   'Que existe también el prevaricato por omisión, de modo que no proferir una decisión que legalmente debía adoptarse puede ser relevante; aun así, el informe describe el hecho y no lo califica.',
   'Que la omisión solo es relevante si causó un perjuicio patrimonial verificable, razón por la cual el informe debe cuantificarlo antes de poner el hecho en conocimiento del competente.',
   'Que la omisión es exclusivamente disciplinaria y nunca penal, por lo que el hallazgo se consigna únicamente como un posible incumplimiento del deber funcional del servidor.'],
  'El prevaricato puede ser por acción y por omisión: conocer ambos evita pasar por alto un hallazgo. Pero conocerlos sirve para reconocer, no para calificar: el informe describe el hecho y la omisión, y pone el punto en conocimiento.',
  'Ni el prevaricato se limita a la acción, ni la relevancia depende de un perjuicio patrimonial, ni la omisión es solo disciplinaria. Y en ningún caso corresponde al técnico cuantificar o calificar.'),

 (3,
  'El despacho le pide que, en el informe, precise si el servidor investigado actuó «con dolo o con culpa», porque esa distinción define la línea del expediente. Usted documentó la conducta, las condiciones en que ocurrió y los registros que la acreditan, pero no tiene elementos sobre la intención de nadie. El término vence mañana y el servidor del despacho insiste. La conducta se repitió en cuatro oportunidades y usted documentó cada una con su fecha, hora y soporte.',
  '¿Cuál es la actuación correcta?',
  ['Precisar que hubo dolo, ya que la reiteración de la conducta documentada permite inferirlo con un grado de certeza suficiente para el análisis del expediente disciplinario.',
   'Precisar que hubo culpa, porque en ausencia de prueba directa sobre la intención debe aplicarse la interpretación más favorable al servidor investigado en la actuación.',
   'Abstenerse de pronunciarse y, por esa razón, omitir del informe las condiciones y la reiteración de la conducta, que podrían leerse como una imputación implícita de intención.',
   'Describir la conducta, su reiteración y las condiciones verificables en que ocurrió, y abstenerse de afirmar la intención, señalando que esa valoración es del competente.'],
  'El dolo y la culpa son el elemento subjetivo y su valoración es jurídica. Lo que el informe aporta —y es decisivo— son las condiciones y la reiteración verificables, que es exactamente el material con el que el competente valorará ese elemento.',
  'Afirmar dolo o culpa son, ambas, calificaciones del elemento subjetivo. Y omitir las condiciones por prudencia priva al competente del único material con el que podía valorarlo.'),

 (2,
  'Usted documenta un hecho en el que intervinieron tres servidores: uno dio la orden, otro la ejecutó materialmente y un tercero facilitó el acceso al sistema. El despacho le pide que el informe «deje claro quién es el responsable principal». Usted tiene acreditada la actuación material de cada uno, con registros y horarios. Los registros del sistema permiten establecer el horario exacto de cada intervención y quién usó cada usuario.',
  '¿Cómo debe tratarse ese punto?',
  ['Señalando como responsable principal a quien dio la orden, por ser quien determinó la conducta, y describiendo la intervención de los otros dos como accesoria a la suya.',
   'Señalando como responsable principal a quien ejecutó materialmente el hecho, porque es la conducta que el examen técnico pudo acreditar de manera directa y verificable.',
   'Describiendo con precisión qué hizo cada uno, con sus registros y horarios, sin atribuir grados de participación: autoría y participación son categorías jurídicas del competente.',
   'Absteniéndose de individualizar las actuaciones, para no anticipar una distribución de responsabilidades que corresponde establecer al servidor competente en su decisión.'],
  'Autoría, determinación y complicidad son categorías jurídicas. Lo del técnico es describir con precisión qué hizo cada quien y cuándo: ese es precisamente el material con el que el competente establecerá los grados de participación.',
  'Señalar un «responsable principal» —por la orden o por la ejecución— es aplicar categorías de participación. Pero no individualizar las actuaciones priva al competente del material que necesita.'),

 (0,
  'Un compañero afirma que los particulares nunca pueden ser investigados por la PGN y que, si en una diligencia aparece la conducta de un contratista, el asunto debe remitirse íntegramente a la Fiscalía. El jefe pide la precisión porque el informe debe explicar por qué una parte del hallazgo se queda en la entidad. El contratista administraba recursos públicos y el hallazgo quedó plenamente documentado en el acta de la diligencia.',
  '¿Cuál es la precisión correcta?',
  ['Los particulares son disciplinables en los casos que la ley señala, típicamente cuando ejercen funciones públicas o administran recursos del Estado, de modo que el hallazgo puede ser disciplinariamente relevante.',
   'Los particulares nunca son disciplinables: su responsabilidad se rige exclusivamente por la vía civil o penal, por lo que el asunto debe remitirse íntegramente a la autoridad penal competente.',
   'Los particulares son disciplinables únicamente cuando han sido vinculados previamente a un proceso penal por los mismos hechos, y solo mientras ese proceso se encuentre en curso.',
   'Los particulares son disciplinables en todos los casos, porque la ley disciplinaria protege el correcto ejercicio de la función pública frente a cualquier persona que se relacione con ella.'],
  'La ley disciplinaria alcanza a servidores públicos y, en los casos que la propia ley señala, a particulares: típicamente quienes ejercen funciones públicas o administran recursos del Estado. Ni ninguno ni todos.',
  'Ni quedan siempre fuera, ni la vinculación penal previa condiciona nada, ni alcanza a cualquier particular que se relacione con la administración.'),

 (1,
  'Durante una diligencia, el servidor investigado le manifiesta que actuó bajo amenaza de un superior y le pide que eso quede en el informe. Un compañero le dice que no lo incluya, «porque las causales de ausencia de responsabilidad son del derecho penal y este es un informe disciplinario». La diligencia continúa y el acta sigue abierta. Hay dos testigos presentes, el investigado lo repite con insistencia y el informe debe rendirse pasado mañana.',
  '¿Qué corresponde hacer?',
  ['No incluirlo, porque las causales de ausencia de responsabilidad son materia de valoración jurídica y su mención en un informe técnico podría inducir a error al competente.',
   'Dejar constancia de la manifestación tal como fue hecha, sin calificarla, y documentar además los hechos objetivos verificables que puedan relacionarse con lo manifestado.',
   'Incluirlo señalando que, a juicio técnico, la amenaza explica razonablemente la conducta y podría configurar una causal de ausencia de responsabilidad del investigado.',
   'Incluirlo solo después de verificar por su cuenta con otros servidores de la dependencia si la amenaza efectivamente ocurrió, para no trasladar al expediente una afirmación infundada.'],
  'Lo manifestado se consigna como fue dicho, sin calificarlo, y los hechos objetivos verificables se documentan. Si eso configura o no una causal de ausencia de responsabilidad es valoración del competente, aquí y en lo penal.',
  'Omitir la manifestación empobrece el expediente; valorarla como causal la califica; y verificarla por cuenta propia con terceros excede el objeto delegado.'),

 (3,
  'El despacho le anticipa que el expediente se orientará como falta leve y le pide que el informe «no se extienda» en un hallazgo que, descrito completo, podría sugerir un delito contra la administración pública. Le explica que incluirlo obligaría a compulsar copias y a alargar el trámite. El informe vence pasado mañana. El hallazgo está documentado con registros, fechas y fotografías, y el despacho se lo pidió por correo esta mañana.',
  '¿Cuál es la actuación correcta?',
  ['Ajustar la extensión del informe a la orientación del despacho, que conoce el expediente completo y tiene la competencia para calificar la falta y decidir sobre el fondo del asunto.',
   'Describir el hallazgo de forma general, sin detalle, para que el despacho conserve margen de decisión sin que el informe condicione la calificación que ya anunció.',
   'Incluir el hallazgo completo y añadir que, a su juicio, el expediente no debería orientarse como falta leve dada la entidad de lo que el examen técnico pudo documentar.',
   'Describir el hallazgo completo, con su método y condiciones, sin calificarlo, y dejar constancia escrita de la solicitud recibida del despacho sobre la extensión del informe.'],
  'El informe refleja lo documentado, completo. La decisión sobre la calificación y sobre la compulsa es del competente, y no es razón para recortar la prueba. La solicitud recibida se deja por escrito: protege el caso y protege a usted.',
  'Recortar o generalizar es filtrar la prueba; y opinar sobre cómo debería orientarse el expediente es calificar, que es justo lo que no le corresponde.'),

 (2,
  'Un compañero sostiene que, como un mismo hecho puede ser falta y delito, la PGN debería esperar siempre a que la Fiscalía defina primero, «para no contradecirse». Otro afirma que la PGN puede incluso asumir lo penal por su poder preferente. El jefe pide la precisión para un documento que sale a otra dependencia. El documento sale esta semana firmado por el jefe de la Dirección y la otra dependencia ya preguntó por el punto.',
  '¿Cuál es la precisión correcta?',
  ['La PGN debe esperar la definición penal cuando los hechos coinciden, de modo que la decisión disciplinaria no contradiga lo que la justicia penal establezca sobre los mismos hechos.',
   'La PGN puede asumir la investigación penal en virtud del poder preferente, que le permite desplazar a cualquier otra autoridad cuando los hechos surgen de una actuación propia.',
   'El poder preferente opera dentro de lo disciplinario frente al control interno de las entidades; lo penal corresponde a la Fiscalía y las dos actuaciones corren de forma independiente.',
   'Las dos actuaciones se acumulan cuando versan sobre los mismos hechos, y la autoridad que primero avoque conocimiento resuelve lo penal y lo disciplinario en una sola decisión.'],
  'El poder preferente es disciplinario: desplaza al control interno disciplinario de las entidades, no a la justicia penal. Y las acciones corren en paralelo, sin prejudicialidad ni acumulación.',
  'Ni hay prejudicialidad penal, ni el poder preferente alcanza lo penal, ni las actuaciones se acumulan en una sola decisión.'),

 (0,
  'Usted documenta enmendaduras en varios folios de un registro oficial: la cifra fue sobrescrita y la tinta difiere de la del resto del documento. El despacho le pide que el informe concluya que hubo falsedad. Usted puede describir con precisión las enmendaduras, su ubicación y las diferencias de tinta, pero no determinar quién las hizo ni cuándo. El registro es un libro oficial de la dependencia y el examen se practicó con los instrumentos disponibles en el laboratorio.',
  '¿Cómo debe redactar el informe?',
  ['Describiendo las enmendaduras, su ubicación exacta y las diferencias observadas, con el método aplicado y sus limitaciones, sin nombrar el tipo penal ni atribuir autoría.',
   'Concluyendo que hubo falsedad en documento público, ya que las enmendaduras con tinta distinta son objetivamente constitutivas de esa conducta punible y así puede constatarse.',
   'Concluyendo que hubo falsedad y advirtiendo que no fue posible determinar la autoría, de modo que el competente sepa qué parte de la calificación queda pendiente de establecer.',
   'Describiendo las enmendaduras sin mencionar las diferencias de tinta, para no sugerir una manipulación deliberada que el examen técnico no permite afirmar con certeza suficiente.'],
  'La descripción precisa —ubicación, sobrescritura, diferencias de tinta, método y límites— es más útil que la palabra «falsedad», porque es con lo que el competente verificará la calificación. Nombrar el tipo es calificar.',
  'Concluir falsedad, con o sin reserva sobre la autoría, invade competencia ajena; y omitir la diferencia de tinta suprime justamente el dato técnico más relevante del hallazgo.'),

 (1,
  'Faltan cinco días para la prueba. En los simulacros de este bloque usted acierta las preguntas sobre la diferencia entre lo penal y lo disciplinario, pero falla las que describen un hallazgo concreto y le piden decidir qué escribir: duda entre la opción que nombra el delito y la que lo describe. Su registro muestra ese patrón en seis de los últimos nueve casos. Lleva un registro de los simulacros resueltos y puede ver exactamente qué opción eligió cada vez que falló.',
  '¿Cuál es la mejor manera de corregirlo?',
  ['Memorizar los tipos penales contra la administración pública con sus elementos, porque reconocer con precisión el tipo hará evidente si corresponde o no nombrarlo en el informe.',
   'Aplicar una regla única: el informe describe hechos, método y condiciones, y nunca nombra el tipo penal; conocer los tipos sirve para no pasar por alto el hallazgo, no para calificarlo.',
   'Resolver más simulacros de este bloque hasta que la intuición mejore, dejando el repaso de los tipos penales para los días inmediatamente anteriores a la prueba escrita.',
   'Concentrarse en el prevaricato y el peculado, que son los delitos que más preguntas generan en esta convocatoria, y repasar los demás solo con la tabla de esta guía.'],
  'El error no está en el conocimiento de los tipos sino en para qué se usan: sirven para reconocer, no para calificar. Convertir eso en regla única —describir, nunca nombrar el tipo— resuelve la familia entera de casos.',
  'Memorizar más tipos refuerza la tentación de nombrarlos; repetir simulacros sin cambiar el criterio repite el error; y concentrarse en dos delitos deja fuera la mayoría de los hallazgos posibles.'),

 (3,
  'Durante una diligencia aparece un hecho que podría ser delito y también un posible detrimento patrimonial. El despacho solicitante está en otra ciudad y no responde llamadas. Un compañero propone que la Dirección remita de una vez a la Fiscalía y a la Contraloría, «porque son dos entidades distintas y así no se pierde tiempo con ninguna». El informe vence mañana. Los dos hallazgos quedaron documentados en el acta y el despacho no contesta correos ni llamadas desde ayer.',
  '¿Cuál es la actuación correcta?',
  ['Remitir a la Fiscalía lo penal y a la Contraloría lo fiscal, informando de ambas remisiones al despacho, ya que la competencia de cada entidad está claramente definida en la Constitución.',
   'Remitir solo lo fiscal a la Contraloría, que es materia menos urgente, y dejar lo penal en conocimiento del despacho para que decida la compulsa a la Fiscalía cuando sea posible.',
   'Esperar a que el despacho responda, sin rendir el informe ni dejar constancia, porque sin su instrucción no es posible determinar qué hacer con ninguno de los dos hallazgos.',
   'Describir los dos hechos en el informe, sin calificarlos, ponerlos por escrito en conocimiento del competente y rendir el informe dentro del término, dejando constancia de la imposibilidad de contactarlo.'],
  'En los tres supuestos —penal, fiscal y disciplinario— la conducta del técnico es la misma: describir sin calificar y poner en conocimiento. La compulsa la decide el competente, y la imposibilidad de contactarlo se documenta, no detiene el informe.',
  'Remitir por cuenta propia a una o a las dos entidades usurpa la decisión; y detener el informe esperando instrucción incumple el término cuando sí era posible rendirlo con constancia.'),

 (2,
  'El informe técnico que usted rindió fue usado por el despacho para formular pliego de cargos. El investigado, en sus descargos, sostiene que el informe «imputa un delito sin competencia». Al releerlo, usted advierte que en un párrafo escribió que los registros «fueron falsificados». El expediente está en juzgamiento y el despacho le pide concepto. El expediente ya pasó a juzgamiento y el despacho le pidió el concepto por escrito para esta semana.',
  '¿Qué corresponde hacer?',
  ['Sostener la redacción, porque «falsificados» describe un hecho técnico verificable y no constituye la calificación jurídica de un tipo penal determinado dentro del informe.',
   'Modificar el informe ya incorporado al expediente, sustituyendo la expresión por una descripción técnica neutra, de modo que la observación de la defensa quede sin fundamento.',
   'Reconocer por escrito que la expresión excede la descripción técnica, precisar qué fue lo efectivamente observado y con qué método, y poner la aclaración en conocimiento del competente.',
   'Abstenerse de pronunciarse, dado que la valoración del informe y de las observaciones de la defensa corresponde al servidor competente y no a quien elaboró el documento técnico.'],
  'Reconocer el exceso y precisar qué fue lo observado es lo que salva el informe: una aclaración técnica oportuna permite al competente separar el hecho de la calificación impropia. Sostenerla o modificar el documento ya incorporado empeoran el problema.',
  'Sostener «falsificados» mantiene una calificación en boca de quien no podía hacerla; modificar un documento ya incorporado al expediente es alterarlo; y callar deja el vicio en pie durante el juzgamiento.'),
]
