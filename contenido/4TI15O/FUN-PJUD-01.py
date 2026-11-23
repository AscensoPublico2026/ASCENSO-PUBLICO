# -*- coding: utf-8 -*-
"""Día 14 · Marco normativo de Policía Judicial — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-PJUD-4TI15O-01',
    archivo='FUN-PJUD-4TI15O-01-marco-normativo-policia-judicial.html',
    dia=14,
    titulo_doc='Marco normativo de Policía Judicial',
    h1='Marco normativo<br>de Policía Judicial',
    kicker='Día 14 · Conocimientos específicos',
    sub='El conocimiento específico que más distingue a tu cargo. Qué es la <strong>policía judicial</strong> y de dónde nace, quiénes la ejercen de forma <strong>permanente, transitoria y especial</strong>, por qué la <strong>DNIE</strong> la ejerce (art. 10 del Decreto Ley 262 de 2000), qué significa que tus funciones sean <strong>por delegación del servidor competente y para la práctica de pruebas técnicas</strong>, cuál es el <strong>marco procesal aplicable</strong> cuando la PGN la ejerce —y aquí hay una sorpresa que casi nadie estudia—, los <strong>actos urgentes</strong>, los <strong>límites y garantías</strong>, y la <strong>coordinación con la Fiscalía</strong> cuando el hallazgo disciplinario revela un posible delito.',
    badges=['⏱ 110-130 min', '🔍 Policía judicial', '⚖️ Marco normativo'],
    fmeta='Marco normativo de Policía Judicial aplicado a la DNIE',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Marco normativo de Policía Judicial',
)

FUENTE = 'guias/FUN-PJUD-PU15-01-policia-judicial.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- módulo nuevo
MARCO_PGN = '''<h3><span class="h3-chip">0</span> La policía judicial de la PGN: de dónde sale y con qué código se ejerce</h3>
  <p>Antes de entrar en la teoría general conviene fijar las tres normas que, encadenadas, explican por qué tú ejerces funciones de policía judicial y con qué reglas. Son tres y la tercera sorprende a casi todo el mundo.</p>
  <div class="flujo">
    <div class="flujo-paso"><div class="fp-n">1</div><div><b>Decreto Ley 262 de 2000, art. 10</b><p>Atribuye a la <strong>Dirección Nacional de Investigaciones Especiales</strong> —dependencia del nivel central adscrita al Despacho del Procurador General— funciones de <strong>policía judicial</strong>, y prevé que las <strong>comisiones conjuntas</strong> con la Fiscalía o la Contraloría requieren <strong>designación previa</strong>. Aquí nace la facultad en la entidad.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">2</div><div><b>Tu manual de funciones (Conv. 257-2026)</b><p>Te atribuye <strong>«ejercer funciones de Policía Judicial para la práctica de pruebas técnicas, previa delegación del servidor competente»</strong>. Aquí la facultad llega a tu cargo, y llega <strong>acotada</strong>: para pruebas técnicas, y previa delegación.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">3</div><div><b>Ley 1952 de 2019, art. 116</b><p>Dispone que <strong>cuando la Procuraduría General de la Nación ejerza funciones de policía judicial se aplicará la Ley 600 de 2000</strong> en cuanto no se oponga a las previsiones del Código General Disciplinario. Aquí se define el <strong>marco procesal</strong>.</p></div></div>
  </div>
  <h4>Por qué el tercer eslabón importa tanto</h4>
  <p>La intuición de cualquiera que estudie policía judicial es que el código aplicable es la <strong>Ley 906 de 2004</strong>, el sistema penal acusatorio, que es donde está desarrollada la institución con más detalle y de donde provienen las reglas técnicas de cadena de custodia que todo el mundo usa. Y esa intuición es útil, porque esas reglas técnicas son las que efectivamente se aplican en la práctica. Pero el <strong>artículo 116 del Código General Disciplinario</strong> dice otra cosa sobre el marco procesal: cuando la <em>PGN</em> ejerce funciones de policía judicial, se aplica la <strong>Ley 600 de 2000</strong> en cuanto no se oponga al propio Código.</p>
  <p>Dicho de otro modo: la referencia procesal que la ley disciplinaria hace no es automáticamente al sistema acusatorio. Es una precisión fina, que distingue a quien estudió el tema de quien lo supuso, y es exactamente el tipo de detalle que una prueba de conocimientos específicos usa para separar candidatos.</p>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Si una opción afirma que «la PGN ejerce policía judicial conforme a la Ley 906 de 2004 por remisión del Código General Disciplinario», está invirtiendo el art. 116. Si otra afirma que la DNIE puede conformar comisiones conjuntas con la Fiscalía «cuando lo estime necesario», está omitiendo la <strong>designación previa</strong> que exige el art. 10 del Decreto Ley 262.</p></div>
  <h4>Los cuatro límites de la fórmula de tu manual</h4>
  <p>Vale la pena desarmar la frase palabra por palabra, porque cada una es un límite que la prueba explora:</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Expresión</th><th>Qué habilita</th><th>Qué excluye</th></tr></thead>
      <tbody>
        <tr><td><strong>«Previa delegación»</strong></td><td>Actuar en el asunto concreto para el que el servidor competente te delegó.</td><td>Una facultad permanente que venga con el cargo. Sin delegación no hay función que ejercer.</td></tr>
        <tr><td><strong>«Del servidor competente»</strong></td><td>Que la delegación provenga de quien tiene la competencia en la actuación.</td><td>Una petición verbal de un compañero, de otra dependencia o de quien no conoce del asunto.</td></tr>
        <tr><td><strong>«Para la práctica»</strong></td><td>Ejecutar materialmente la prueba y documentarla.</td><td>Decretarla, valorarla o decidir su alcance: eso es del competente.</td></tr>
        <tr><td><strong>«De pruebas técnicas»</strong></td><td>El objeto técnico acotado de la diligencia.</td><td><mark>Competencia penal general: no captura, no imputa, no tipifica delitos, no resuelve situación jurídica.</mark></td></tr>
      </tbody>
    </table>
  </div>
  <div class="checkpoint" data-cp="0">
    <div class="cp-q">✋ Punto de control: según el art. 116 de la Ley 1952 de 2019, ¿qué código se aplica cuando la PGN ejerce funciones de policía judicial?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">La Ley 906 de 2004, por ser el estatuto que desarrolla la policía judicial en el sistema acusatorio.</button>
    <button class="cp-opt" data-ans="1">La Ley 600 de 2000, en cuanto no se oponga a las previsiones del Código General Disciplinario.</button>
    <button class="cp-opt" data-ans="0">Únicamente el Código General Disciplinario, que regula la materia de forma completa y autónoma.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  '''

R = [
    ('<h3><span class="h3-chip">1</span> Qué es la policía judicial y cuál es su fundamento</h3>',
     MARCO_PGN + '<h3><span class="h3-chip">1</span> Qué es la policía judicial y cuál es su fundamento</h3>'),
]
SEC = aplicar_todas(SEC, R, estricto=True)

# generalizar el perfil contable de la base al perfil técnico del cargo
SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>', '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>', '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('Por qué un Contador Público ejerce funciones de policía judicial',
     'Por qué un servidor técnico de la PGN ejerce funciones de policía judicial'),
    ('Contador Público', 'Técnico Investigador'),
    ('soportes contables y financieros', 'elementos materiales probatorios'),
    ('soportes contables', 'elementos materiales probatorios'),
    ('EMP contables', 'elementos materiales probatorios'),
    ('EMP contable', 'elemento material probatorio'),
    ('evidencia digital contable', 'evidencia digital'),
    ('hallazgo contable', 'hallazgo técnico'),
    ('rol financiero-contable', 'rol técnico'),
    ('tipología de EMP contables', 'tipología de elementos materiales probatorios'),
    ('documentos contables', 'documentos y registros'),
    ('registros contables', 'registros y soportes'),
    ('información contable y financiera', 'información técnica y documental'),
    ('análisis contable', 'análisis técnico'),
    ('materia contable', 'materia técnica'),
    ('pericial contable', 'pericial técnico'),
    ('peritaje contable', 'peritaje técnico'),
    ('contable y financiero', 'técnico'),
    ('contables y financieros', 'técnicos'),
    ('contable', 'técnico'), ('contables', 'técnicos'),
    ('financiero', 'técnico'), ('financieros', 'técnicos'),
    ('Profesional Universitario 3PU-15', 'Técnico Investigador 4TI-15'),
    ('Profesional Universitario, código 3PU-15', 'Técnico Investigador, código 4TI-15'),
    ('Profesional Universitario', 'Técnico Investigador'),
    ('(3PU-15)', '(4TI-15)'), ('3PU-15', '4TI-15'), ('3PU15', '4TI15O'), ('PU-15', '4TI-15'), ('3PU', '4TI'),
    ('112-2026', '257-2026'),
    ('el instructor', 'el servidor que instruye'), ('El instructor', 'El servidor que instruye'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el marco '
              'normativo de Policía Judicial aplicado a la DNIE: fundamento y clases, el art. 10 del Decreto Ley 262 '
              'de 2000, el art. 116 del CGD y el código procesal aplicable, los límites de la delegación, los actos '
              'urgentes, las garantías y la coordinación con la Fiscalía.')

P = [
 (1,
  'Un compañero afirma en el grupo que, como la DNIE ejerce funciones de policía judicial, el marco procesal que se le aplica es la Ley 906 de 2004, «porque es la norma que desarrolla la policía judicial en el sistema acusatorio». Otro responde que el Código General Disciplinario remite a otra ley. El jefe pide la precisión exacta porque el punto va en un documento que la Dirección remitirá a una procuraduría regional, y quiere que quede citado el artículo.',
  '¿Cuál es la precisión correcta?',
  ['Su compañero tiene razón: la Ley 906 de 2004 es el estatuto aplicable, porque allí está desarrollada la institución de la policía judicial y de allí provienen las reglas de cadena de custodia.',
   'El art. 116 de la Ley 1952 de 2019 dispone que cuando la PGN ejerza funciones de policía judicial se aplicará la Ley 600 de 2000, en cuanto no se oponga a las previsiones del propio Código.',
   'No existe remisión alguna: el Código General Disciplinario regula la materia de forma completa y autónoma, de modo que no se aplica ningún estatuto procesal penal a la actuación de la PGN.',
   'Se aplica la Ley 906 de 2004 para los actos urgentes y la Ley 600 de 2000 para el resto de la actuación, según el momento procesal en que se ejerza la función de policía judicial.'],
  'El art. 116 del CGD es explícito: cuando la PGN ejerce funciones de policía judicial se aplica la Ley 600 de 2000 en cuanto no se oponga a ese código. Las reglas técnicas de custodia del sistema acusatorio se usan en la práctica, pero la remisión procesal de la ley disciplinaria es esa.',
  'La intuición apunta a la Ley 906 y es justo lo que la pregunta explora. Tampoco hay autonomía completa del CGD ni un reparto por momentos procesales: la remisión es una sola y está en el art. 116.'),

 (3,
  'Un servidor de una procuraduría provincial lo llama: quiere que la DNIE asegure unos elementos en una entidad y le dice que «con la llamada basta, porque la DNIE tiene funciones de policía judicial permanentes y puede actuar de oficio». No hay solicitud escrita ni delegación. El riesgo de alteración, según él, es inmediato y la entidad cierra en dos horas. Usted conoce a ese servidor de apoyos anteriores, todos tramitados por escrito y sin inconvenientes.',
  '¿Cuál es la precisión correcta sobre esas funciones?',
  ['Tiene razón: la atribución del art. 10 del Decreto Ley 262 de 2000 es permanente para la DNIE, de modo que sus servidores pueden actuar de oficio cuando adviertan riesgo para la prueba.',
   'Tiene razón parcialmente: puede actuarse de inmediato y la delegación se incorpora después, siempre que se deje constancia en el acta de que estaba pendiente al momento de la diligencia.',
   'No tiene razón, y por eso no cabe gestión alguna: sin solicitud escrita la DNIE no puede atender requerimientos de otras dependencias, ni siquiera orientando sobre el trámite aplicable.',
   'No tiene razón: su manual exige delegación previa del servidor competente. Lo que cabe es orientar sobre el trámite, informar la urgencia a su superior y dejar constancia de lo planteado.'],
  'La atribución del art. 10 es de la entidad; en su cargo la función se ejerce «previa delegación del servidor competente». Sin delegación no hay actuación, pero sí hay deber de encauzar: orientar, informar al superior y dejar constancia.',
  'Ni la atribución institucional convierte la función en permanente para cada servidor, ni una delegación posterior sanea una actuación ya hecha. Tampoco corresponde cerrar la puerta sin encauzar la urgencia.'),

 (0,
  'Durante una diligencia en la que usted asegura elementos, un servidor de la entidad admite en voz alta haber alterado unos registros y hay dos testigos presentes. Un compañero le dice que, como usted ejerce funciones de policía judicial, puede ponerlo a disposición de las autoridades allí mismo y que eso es flagrancia. El investigado permanece en el lugar y la diligencia continúa. La diligencia fue delegada esta mañana y el acta todavía no se ha cerrado ni firmado por los intervinientes.',
  '¿Cuál es la actuación correcta?',
  ['Documentar con precisión en el acta la manifestación y lo observado, continuar con lo delegado y poner los hechos en conocimiento del servidor competente para que decida.',
   'Ponerlo a disposición de la autoridad competente en el lugar, ya que la función de policía judicial habilita la aprehensión de quien es sorprendido en la comisión de una conducta punible.',
   'Recibirle una declaración escrita y firmada en ese momento, para que la manifestación no se pierda, y anexarla al informe técnico como soporte del hallazgo documentado.',
   'Suspender la diligencia y comunicarse con la Fiscalía para que asuma de inmediato, por tratarse de un hecho que podría constituir delito y exceder la competencia disciplinaria.'],
  'Su delegación es para practicar pruebas técnicas: no confiere competencia penal ni facultad de aprehender, ni lo habilita para recibir declaraciones. Se documenta, se continúa con lo delegado y se pone en conocimiento del competente.',
  'Ni la policía judicial de la PGN habilita aprehensiones, ni corresponde recibir declaraciones fuera del objeto delegado, ni comunicarse directamente con la Fiscalía: la compulsa la decide el competente.'),

 (2,
  'El despacho propone conformar una comisión conjunta con la Fiscalía para adelantar unas diligencias en las que la DNIE aportaría el componente técnico. Un compañero dice que basta con un acuerdo entre las dos entidades a nivel operativo, y otro afirma que la PGN no puede actuar junto con la Fiscalía bajo ninguna circunstancia. El jefe pide la precisión para motivar la respuesta que se enviará. La propuesta llegó por correo del despacho y la respuesta debe salir firmada por el jefe de la Dirección esta semana.',
  '¿Qué dispone el art. 10 del Decreto Ley 262 de 2000?',
  ['Que la PGN y la Fiscalía no pueden conformar comisiones conjuntas, por tratarse de entidades con competencias separadas y naturalezas constitucionales distintas entre sí.',
   'Que basta un acuerdo operativo entre las dependencias involucradas, porque la coordinación interinstitucional no requiere formalidad adicional cuando ambas ejercen policía judicial.',
   'Que la DNIE puede conformar comisiones conjuntas con la Fiscalía o la Contraloría para adelantar actuaciones, pero que esas comisiones requieren designación previa de quien es competente.',
   'Que las comisiones conjuntas solo proceden con la Contraloría, por versar sobre recursos públicos, y nunca con la Fiscalía, cuya competencia es exclusivamente penal.'],
  'El art. 10 prevé las comisiones conjuntas con la Fiscalía o la Contraloría y exige designación previa. No están prohibidas ni se improvisan con un acuerdo operativo: hay una formalidad que las habilita.',
  'Ni están vedadas, ni bastan acuerdos informales, ni se limitan a la Contraloría: la norma menciona las dos entidades y condiciona la comisión a la designación previa.'),

 (1,
  'Al llegar a una dependencia para practicar una prueba técnica delegada, usted advierte que unos elementos relevantes están siendo movidos en ese momento y que, si no actúa, probablemente se pierdan. Su delegación cubre el examen de esos elementos. Un compañero le dice que espere instrucciones porque «no se puede improvisar», y otro que asegure todo lo que vea, sin distinguir. Usted está solo con un compañero, la delegación escrita está en su poder y el movimiento continúa mientras consulta.',
  '¿Qué corresponde hacer?',
  ['Esperar instrucciones del despacho antes de cualquier actuación material, porque toda medida de aseguramiento requiere una orden específica adicional a la delegación recibida.',
   'Asegurar los elementos comprendidos en su delegación, documentando con precisión el estado en que los halló y las condiciones de la actuación, e informar de inmediato al competente.',
   'Asegurar todos los elementos presentes en el lugar, incluidos los no comprendidos en la delegación, porque la urgencia justifica un aseguramiento amplio que después se depura.',
   'Grabar lo que ocurre sin intervenir, para dejar registro audiovisual del movimiento de los elementos, y rendir el informe describiendo lo observado durante la diligencia.'],
  'El aseguramiento de la prueba es precisamente el núcleo de la función: se asegura lo comprendido en la delegación, documentando el estado y las condiciones, y se informa de inmediato. Ni se espera cuando la prueba se pierde, ni se amplía el objeto.',
  'Esperar instrucciones deja perder lo que sí estaba delegado; asegurar todo excede el objeto y expone lo recaudado a inexistencia; y limitarse a grabar renuncia a la medida que la delegación autorizaba.'),

 (3,
  'Asegurando elementos en una investigación disciplinaria, usted documenta un hecho que podría constituir delito. El despacho solicitante está en otra ciudad. Un compañero propone que la DNIE, por tener funciones de policía judicial, adelante directamente los actos urgentes propios de la investigación penal para no perder evidencia. El despacho no responde llamadas desde ayer y los elementos ya están asegurados conforme a lo delegado.',
  '¿Cuál es la precisión correcta sobre el alcance de la función?',
  ['Es correcto: las funciones de policía judicial de la DNIE habilitan a adelantar actos urgentes de investigación penal cuando existe riesgo inminente de pérdida de la evidencia.',
   'Es correcto siempre que después se informe a la Fiscalía, que convalidará lo actuado e incorporará los elementos recaudados a la investigación penal que corresponda adelantar.',
   'Es incorrecto: al advertir un posible delito debe suspenderse toda actuación y remitirse el expediente íntegro a la Fiscalía, por pérdida sobreviniente de competencia de la PGN.',
   'Es incorrecto: la función está restringida al ámbito disciplinario. Se asegura lo delegado, se deja constancia del posible delito y la compulsa de copias la decide el servidor competente.'],
  'La función de policía judicial de la PGN está al servicio de sus propias competencias: es una función restringida al ámbito disciplinario. Lo penal se compulsa, y la compulsa la decide el competente, no el técnico.',
  'Ni la urgencia ni una convalidación posterior amplían la competencia a lo penal; pero tampoco se pierde la competencia disciplinaria por aparecer un posible delito: las acciones son independientes.'),

 (0,
  'Usted asegura un dispositivo y lo rotula. Al día siguiente, el despacho pide examinarlo y advierte que el rótulo no consigna la hora de recolección ni el nombre de quien lo entregó, solo la fecha. Usted recuerda ambos datos y los tiene anotados en su libreta de campo. El informe debe rendirse en dos días y nadie más ha advertido el punto. La dependencia que entregó el dispositivo no expide certificaciones en el acto y su jefe está en comisión.',
  '¿Cuál es la actuación correcta?',
  ['Dejar constancia escrita del dato faltante en el rótulo, aportar lo consignado en su libreta como soporte de la trazabilidad e informarlo por el canal al servidor competente.',
   'Completar el rótulo con los datos que recuerda y que están en su libreta, de modo que el registro quede íntegro antes de que el examen técnico del dispositivo se practique.',
   'No mencionar el punto, dado que usted recuerda los datos y puede declararlos si alguien los cuestiona durante la contradicción de la prueba en el proceso disciplinario.',
   'Rechazar el examen del dispositivo y devolverlo a la dependencia, porque un elemento con rótulo incompleto rompe la cadena de custodia de manera insubsanable.'],
  'Un eslabón incompleto no se completa después sobre el propio rótulo: eso altera un documento ya producido. Se deja constancia del faltante, se aporta el soporte que sí existe y se informa, para que el competente valore su alcance.',
  'Rellenar el rótulo a posteriori compromete la autenticidad del registro; callar el vacío deja al competente sin saberlo; y devolver el elemento sin más paraliza una actuación que podía adelantarse delimitando su alcance.'),

 (2,
  'Un compañero sostiene que todos los servidores de la PGN ejercen funciones de policía judicial por el hecho de pertenecer a la entidad. Otro afirma que solo las ejerce la Policía Nacional. El jefe pide la distinción porque debe explicarse en un documento dirigido a otra entidad que pidió apoyo a la Dirección. La entidad que pidió el apoyo nunca ha tramitado una solicitud de este tipo y el documento sale esta semana.',
  '¿Cuál es la distinción correcta?',
  ['Solo ejercen policía judicial los cuerpos de policía judicial permanentes; cualquier otra entidad que la ejerza lo hace por delegación directa de la Policía Nacional en cada caso.',
   'Todos los servidores de la PGN la ejercen, porque la atribución del Decreto Ley 262 de 2000 se extiende a la entidad en su conjunto y a cada uno de sus servidores públicos.',
   'Hay policía judicial permanente, transitoria y especial: la atribución a la DNIE es de la entidad, y dentro de ella cada cargo la ejerce según lo que su manual de funciones disponga.',
   'La ejercen únicamente los servidores con formación jurídica, porque la función implica calificar jurídicamente los hechos que se recaudan durante las diligencias de investigación.'],
  'La función se clasifica en permanente, transitoria y especial, y la atribución del Decreto Ley 262 es de la entidad: dentro de ella, cada cargo la ejerce en los términos de su manual. El del Técnico Investigador la acota a pruebas técnicas y previa delegación.',
  'Ni se limita a los cuerpos permanentes, ni alcanza a todo servidor de la PGN por el solo hecho de serlo, ni depende de la formación jurídica: la función no consiste en calificar.'),

 (1,
  'El despacho le delega practicar una prueba técnica sobre un equipo y, por separado, le pide que «aproveche» para entrevistar al servidor que lo usaba, porque está disponible en ese momento y después será difícil ubicarlo. La delegación escrita se refiere únicamente al examen del equipo. El servidor accede de buena gana a conversar. La diligencia está en curso, el servidor espera en la oficina contigua y nadie más del despacho está presente.',
  '¿Qué corresponde hacer?',
  ['Entrevistarlo e incorporar el resultado al informe técnico como anexo, dejando constancia de que la entrevista se realizó a solicitud verbal del despacho durante la diligencia.',
   'No entrevistarlo, practicar lo delegado, dejar constancia de la disponibilidad del servidor y de la solicitud recibida, e informarlo para que el competente disponga lo que corresponda.',
   'Entrevistarlo de manera informal sin levantar acta, para conocer el contexto del caso y orientar mejor el examen técnico del equipo que sí le fue delegado formalmente.',
   'Negarse y no dejar registro de la solicitud, porque una petición que excede la delegación no debería quedar documentada en el expediente de la actuación disciplinaria.'],
  'Recibir una entrevista o declaración excede el objeto de una delegación para practicar una prueba técnica. Se practica lo delegado, se deja constancia de la oportunidad y de la solicitud, y decide el competente.',
  'Entrevistar —con acta o sin ella— es actuar fuera de la delegación; y no dejar registro de la solicitud priva al competente de un dato útil y borra el rastro de una petición que excedía el encargo.'),

 (3,
  'Durante el aseguramiento de unos elementos, el apoderado del investigado le exige que le entregue copia del acta en ese momento y le advierte que, de lo contrario, la diligencia será nula por violación del derecho de defensa. Usted no tiene instrucción sobre entrega de documentos y la diligencia aún no ha terminado. Hay dos testigos presentes, el apoderado alza la voz y el acta sigue abierta sobre la mesa. Usted lleva poco tiempo en la Dirección y es su primera diligencia con un apoderado presente.',
  '¿Cuál es la actuación correcta?',
  ['Entregarle copia del acta de inmediato, ya que el derecho de defensa incluye el acceso a las actuaciones y negarlo efectivamente podría viciar la diligencia que se practica.',
   'Entregarle copia parcial del acta, limitada a lo que concierne directamente a su representado, de modo que se atienda el derecho sin exponer información de terceros.',
   'Negarse y no dejar registro de la solicitud, porque las peticiones de los apoderados se tramitan ante el despacho y no durante la práctica material de una prueba técnica.',
   'Explicarle que la solicitud se tramita ante el servidor competente, dejar constancia en el acta de la petición y de la advertencia, y continuar con la diligencia delegada.'],
  'El derecho a controvertir la prueba está reconocido, pero la entrega de copias se tramita ante el competente. Lo que protege la diligencia es dejar constancia de la petición y de la advertencia, y continuar con lo delegado.',
  'Entregar el acta —íntegra o parcial— es disponer de un documento de una actuación reservada; y negarse sin dejar constancia borra del expediente una solicitud que el competente debe conocer.'),

 (2,
  'Un compañero le comenta que, como la cadena de custodia proviene del sistema penal acusatorio y la PGN se rige por el Código General Disciplinario, las reglas técnicas de custodia «no son obligatorias» en las diligencias disciplinarias y bastan los registros que cada grupo use. El jefe pide precisión porque el punto afecta todos los apoyos de la Dirección. El punto afecta a todos los grupos de la Dirección y el jefe quiere dejarlo por escrito antes del próximo apoyo.',
  '¿Cuál es la precisión correcta?',
  ['Tiene razón: al no existir remisión expresa del CGD a las reglas técnicas de custodia, cada dependencia puede adoptar los registros que considere adecuados a su propia operación.',
   'Tiene razón parcialmente: las reglas aplican solo cuando el elemento vaya a remitirse a la Fiscalía, y no cuando el material permanezca dentro de la actuación disciplinaria.',
   'Se equivoca: la custodia garantiza autenticidad, identidad e integridad del elemento, y sin ella la prueba queda expuesta a inexistencia (art. 158 CGD) por falta de formalidades sustanciales.',
   'Se equivoca: la cadena de custodia es exigible porque el art. 116 del CGD remite íntegramente a la Ley 906 de 2004 en materia de aseguramiento de elementos materiales probatorios.'],
  'La custodia no es un formalismo importado: garantiza que la prueba valorada es la misma que se recaudó. Sin ella, el elemento queda expuesto a la inexistencia del art. 158 por ausencia de formalidades sustanciales.',
  'Ni cada grupo define sus registros, ni la exigencia depende del destino del elemento. Y la remisión del art. 116 es a la Ley 600 de 2000, no a la Ley 906: cuidado con esa opción, que suena técnica y está mal.'),

 (0,
  'La Dirección le asigna apoyar una diligencia en la que participarán también servidores de otra entidad de control. No hay designación previa de comisión conjunta: el despacho coordinó la actuación por teléfono con la otra entidad. Le piden que aporte el componente técnico y que firme el acta conjunta que se levantará al final. La diligencia está programada para pasado mañana y el acta conjunta ya viene redactada por la otra entidad.',
  '¿Qué corresponde hacer?',
  ['Advertir por escrito que no consta designación previa de comisión conjunta, pedir instrucción expresa al competente y abstenerse de suscribir un acta conjunta sin esa formalidad.',
   'Participar y firmar el acta conjunta, dejando constancia en ella de que la coordinación entre las entidades se hizo por vía telefónica y no mediante designación previa escrita.',
   'Participar aportando el componente técnico pero sin firmar el acta conjunta, de modo que su actuación quede documentada solo en el informe técnico que rinda la Dirección.',
   'Negarse a participar y no informar nada, porque una actuación sin designación previa carece de validez y la Dirección no debe dejar registro de haber sido convocada a ella.'],
  'Las comisiones conjuntas requieren designación previa (art. 10 del Decreto Ley 262 de 2000). Lo que protege la actuación es advertirlo por escrito y pedir instrucción expresa antes de intervenir y, sobre todo, antes de suscribir un acta conjunta.',
  'Participar y firmar dejando una constancia no suple la designación; aportar el componente sin firmar deja igualmente su intervención sin título; y negarse sin informar priva al competente de la oportunidad de subsanarlo.'),

 (1,
  'Usted practica una diligencia de aseguramiento y, al terminar, el jefe de la dependencia le pide que no deje copia del acta allí «porque puede generar alarma entre los empleados». El procedimiento interno de la Dirección prevé dejar constancia de la diligencia en el lugar. El jefe insiste y le recuerda que la entidad ha colaborado en todo. Varios empleados observan la diligencia desde sus puestos y el acta está lista para firmarse.',
  '¿Cuál es la actuación correcta?',
  ['Acceder a la petición por tratarse de una consideración razonable sobre el clima laboral, y dejar constancia en el informe de que no se entregó copia a solicitud de la dependencia.',
   'Cumplir el procedimiento interno dejando la constancia prevista, explicar brevemente por qué es parte del procedimiento, y consignar la petición recibida en el acta de la diligencia.',
   'Consultar al despacho solicitante y proceder conforme a lo que indique verbalmente, dejando anotación en el acta de la orientación recibida sobre la entrega de la constancia.',
   'No dejar la constancia y tampoco mencionar la petición, para no generar un conflicto innecesario con una dependencia que colaboró durante toda la diligencia practicada.'],
  'El procedimiento interno es un parámetro vigente y no cede ante una petición de conveniencia. Se cumple, se explica y se consigna la petición: así la actuación queda completa y la solicitud, documentada.',
  'Acceder incumple el procedimiento; una orientación verbal del despacho no lo deroga; y callar la petición borra del expediente un hecho que el competente debería conocer.'),

 (3,
  'Un compañero afirma que, cuando un mismo hecho es falta disciplinaria y delito, la PGN debe suspender su actuación hasta que la Fiscalía resuelva, para evitar decisiones contradictorias. Otro sostiene que las dos actuaciones corren en paralelo. El jefe pide la precisión porque el informe debe explicar por qué el apoyo técnico continúa pese a existir una investigación penal en curso. La investigación penal lleva dos meses y el despacho disciplinario tiene un término de instrucción corriendo.',
  '¿Cuál es la precisión correcta?',
  ['La PGN debe suspender su actuación hasta que la Fiscalía resuelva, porque lo penal es prejudicial respecto de lo disciplinario cuando ambos recaen sobre los mismos hechos.',
   'La PGN debe remitir el expediente a la Fiscalía y archivar su actuación, ya que la existencia de un posible delito desplaza la competencia disciplinaria hacia la jurisdicción penal.',
   'Las dos actuaciones se acumulan en una sola, de modo que la Fiscalía resuelve lo penal y lo disciplinario en la misma decisión, con lo que se evita cualquier contradicción entre ellas.',
   'Las acciones son independientes y corren en paralelo: lo penal valora el delito y lo disciplinario la afectación del deber funcional, con estándares y objetos distintos.'],
  'La independencia de las acciones es un principio central: cada una valora algo distinto, con estándares distintos. Por eso el apoyo técnico continúa aunque exista investigación penal, y por eso el archivo penal no cierra el expediente disciplinario.',
  'Ni hay prejudicialidad penal, ni la competencia disciplinaria se desplaza, ni las actuaciones se acumulan: corren en paralelo, cada una en su ámbito.'),

 (2,
  'Faltan siete días para la prueba escrita. En los simulacros usted acierta cuando la pregunta describe un acto material concreto, pero falla cuando le piden identificar la norma o el código aplicable: confunde la Ley 906, la Ley 600 y el Decreto Ley 262. Su registro muestra el mismo tipo de error en cuatro de los últimos siete casos resueltos. Lleva un registro de los simulacros resueltos y puede ver exactamente en qué norma se equivocó cada vez.',
  '¿Cuál es la mejor manera de corregirlo?',
  ['Memorizar el articulado de la Ley 906 de 2004, que es la norma que desarrolla con más detalle la institución y de la que provienen las reglas técnicas que se aplican en la práctica.',
   'Resolver más simulacros del bloque hasta que la asociación entre norma y situación se automatice, dejando el repaso del marco normativo para los últimos días de preparación.',
   'Fijar la cadena de tres eslabones —Decreto Ley 262 art. 10, manual de funciones y art. 116 del CGD— y ubicar cada caso en el eslabón que le corresponde.',
   'Concentrarse en los actos materiales, que son la mayoría de las preguntas, y asumir que las preguntas puramente normativas son pocas y no compensan el tiempo que exige dominarlas.'],
  'Los tres eslabones responden tres preguntas distintas: de dónde nace la facultad, hasta dónde llega en su cargo y con qué código se ejerce. Ubicar cada caso en uno de ellos elimina la confusión entre las tres normas.',
  'Memorizar la Ley 906 refuerza justamente la confusión que se quiere corregir; repetir simulacros sin cambiar el método repite el error; y renunciar a las preguntas normativas es renunciar a puntos en una prueba eliminatoria.'),
]
