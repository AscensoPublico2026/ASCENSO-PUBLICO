# -*- coding: utf-8 -*-
"""Día 14 · Talento humano I: función pública, clasificación de empleos y planeación — Técnico en Criminalística 4TC-17."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol
from _lib import aplicar_todas as _ap
from _regimen import TODAS as _REGIMEN

META = dict(
    codigo='FUN-GTH-4TC17B-01',
    archivo='FUN-GTH-4TC17B-01-funcion-publica-clasificacion-empleos-planeacion.html',
    dia=14,
    titulo_doc='Talento humano I: función pública, clasificación de los empleos y planeación',
    h1='Talento humano I<br>Función pública, clasificación de los empleos y planeación',
    kicker='Día 14 · Conocimiento específico',
    sub='Empieza el bloque más importante de tu preparación. La <strong>gestión del talento humano</strong> es uno de los <strong>conocimientos esenciales específicos</strong> que el formato de la Convocatoria 285-2026 exige para el <strong>Técnico en Criminalística 4TC-17</strong>, y es el terreno donde trabajarás todos los días en la <strong>División de Gestión Humana</strong>. Hoy: qué es un empleo público y dónde nace, la <strong>clasificación de los empleos</strong> por naturaleza y por nivel, quién es servidor público y quién no, los <strong>actores del sistema</strong> de función pública, la <strong>planeación</strong> del talento humano (plan de vacantes, plan de previsión, manual de funciones, SIGEP II) y las formas de provisión, con su orden legal. Y, con módulo propio, <strong>en qué se aparta la PGN del régimen general</strong>, porque tiene carrera especial.',
    badges=['⏱ 100-120 min', '👥 Talento humano', '📖 Específico'],
    fmeta='Talento humano I: función pública, clasificación de los empleos y planeación (Ley 909 de 2004, Decreto 1083 de 2015 y Decreto Ley 262 de 2000)',
    cargo='Técnico en Criminalística 4TC-17 (Nivel Técnico)',
    conv='285-2026',
    alerta='Talento humano I: función pública, clasificación de los empleos y planeación',
)

SEC = secciones_mapeadas('guias/FUN-GHI-02-generalidades-gestion-humana-publica.html')

# ---------------------------------------------------------------- módulo propio de la PGN
MOD_PGN = '''
      <div class="modulo-head"><div class="modulo-n">★</div><h3>Lo que cambia en la PGN: carrera especial, no régimen general</h3></div>
      <div class="b-texto">
        <p>Todo lo anterior es el <strong>régimen general</strong> del empleo público: Ley 909 de 2004, Decreto 1083 de 2015 y la <strong>Comisión Nacional del Servicio Civil</strong> como administradora de la carrera. Debes dominarlo, porque el formato de convocatoria lo exige y porque es el marco de referencia de toda la gestión del talento humano en Colombia. Pero hay una advertencia que no puedes perder de vista ni un segundo: <mark>la Procuraduría General de la Nación no se rige por ese sistema de carrera</mark>.</p>
        <div class="def-panel"><span class="def-label">Concepto</span><p>La PGN tiene un <strong>régimen especial de carrera</strong> de origen constitucional (art. 279 de la Constitución), desarrollado por los <strong>Decretos Ley 262, 263 y 264 de 2000</strong>. Eso significa que <strong>la propia entidad</strong> —no la CNSC— convoca, administra y vigila sus concursos y su carrera, a través de sus órganos internos, entre ellos la <strong>Comisión de Carrera</strong>. La Convocatoria 285-2026, la que tú estás presentando, es un proceso de la PGN bajo ese régimen especial.</p></div>
        <div class="tabla-wrap"><table>
          <thead><tr><th>Asunto</th><th>Régimen general (Ley 909)</th><th>PGN (Decretos Ley 262-264 de 2000)</th></tr></thead>
          <tbody>
            <tr><td>Norma base de carrera</td><td>Ley 909 de 2004 y Decreto 1083 de 2015</td><td><strong>Decretos Ley 262, 263 y 264 de 2000</strong></td></tr>
            <tr><td>Quién administra y vigila la carrera</td><td><strong>CNSC</strong> (art. 130 de la Constitución)</td><td><strong>La propia PGN</strong>, con su Comisión de Carrera</td></tr>
            <tr><td>Quién convoca el concurso</td><td>CNSC, a solicitud de la entidad</td><td><strong>La PGN</strong>, por resolución del Procurador General</td></tr>
            <tr><td>Ante quién se reclama en el concurso</td><td>CNSC, según la convocatoria</td><td><strong>La PGN</strong>, según su propia convocatoria</td></tr>
            <tr><td>Apoyo a la Comisión de Carrera</td><td>—</td><td><strong>División de Gestión Humana</strong> (art. 63, núm. 12)</td></tr>
            <tr><td>Elección de representantes a la Comisión de Personal</td><td>Entidad y CNSC, según el reglamento</td><td><strong>División de Gestión Humana</strong> coordina y vigila (art. 63, núm. 13)</td></tr>
          </tbody>
        </table></div>
        <div class="ojo"><b>Ojo en la prueba:</b> este es uno de los distractores más usados en las pruebas de la PGN, y funciona porque «la CNSC es la de los concursos» suena razonable. Cada vez que una opción diga que <mark>la CNSC administra el concurso de la PGN</mark>, que <mark>la lista de elegibles la expide la CNSC</mark> o que <mark>la reclamación se presenta ante la CNSC</mark>, es incorrecta. Pero cuidado con el extremo contrario: la pregunta puede estar planteada en otra entidad del régimen general, y allí la CNSC sí es la respuesta correcta. <strong>Lee siempre de qué entidad habla el caso.</strong></p></div>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Un aspirante llama a la División de Gestión Humana, molesto porque cree que le calificaron mal una prueba de la Convocatoria 285-2026, y anuncia que «va a reclamar ante la CNSC». La orientación correcta no es remitirlo allá: la reclamación se presenta <strong>ante la propia Procuraduría</strong>, por el canal y dentro de los términos que la convocatoria fija. Si lo remites a la CNSC, pierde el término y el error habrá sido tuyo. Radicas su escrito, lo orientas sobre el canal real y dejas constancia; la respuesta de fondo la da el competente.</p>
          </div>
        </div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> el régimen general del empleo público (Ley 909, Decreto 1083, CNSC) es materia de estudio obligatoria y rige en la mayoría de las entidades. La PGN, en cambio, tiene <strong>carrera especial</strong> por mandato del artículo 279 de la Constitución, desarrollada por los Decretos Ley 262, 263 y 264 de 2000: administra sus propios concursos y su propia carrera, y la División de Gestión Humana apoya a la Comisión de Carrera y coordina la elección de los representantes a la Comisión de Personal. Distinguir los dos regímenes vale varias preguntas de la prueba.</p></div>
      </div>
'''

SEC[2] = SEC[2] + MOD_PGN

# ---------------------------------------------------------------- identidad
R = [
    # el escenario pasa de la DIAN a la División de Gestión Humana de la PGN
    ('una Dirección Seccional de la DIAN', 'la División de Gestión Humana de la Procuraduría General de la Nación'),
    ('la Dirección Seccional de la DIAN', 'la División de Gestión Humana de la Procuraduría General de la Nación'),
    ('Dirección Seccional de la DIAN', 'División de Gestión Humana de la Procuraduría General de la Nación'),
    ('de la DIAN', 'de la Procuraduría'),
    ('la DIAN', 'la Procuraduría'),
    ('DIAN', 'Procuraduría General de la Nación'),
    ('Gestor I del área de Talento Humano', 'Técnico en Criminalística 4TC-17 de la División de Gestión Humana'),
    ('Gestor I del proceso de Talento Humano', 'Técnico en Criminalística 4TC-17 del proceso de Talento Humano'),
    ('Gestor I de Talento Humano', 'Técnico en Criminalística 4TC-17'),
    ('Gestor I', 'Técnico en Criminalística 4TC-17'),
    ('la Seccional', 'la División'),
    ('Seccional', 'División'),
]
SEC = aplicar_todas(SEC, R, estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol('Técnico en Criminalística', 'Técnicos en Criminalística'), estricto=False)


SEC = _ap(SEC, _REGIMEN, estricto=False)   # carrera especial PGN, no CNSC

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre función '
              'pública, clasificación de los empleos, actores del sistema y planeación del talento humano. '
              'Varias ponen a prueba la distinción entre el régimen general y la carrera especial de la PGN: '
              'lee con cuidado de qué entidad habla cada caso.')

P = [
 (2,
  'Andrés, servidor nombrado en provisionalidad hace cuatro años en un empleo de carrera de la Procuraduría, llega a su puesto en la División de Gestión Humana con un escrito. Sostiene que, por su antigüedad y porque su jefe lo califica bien, ya le corresponde quedar inscrito en carrera administrativa; añade que una compañera le aseguró que «a los cinco años entra uno solo» y que, si no le tramita la inscripción, se quejará. El jefe de la División está en comisión y le pidió a usted orientar el caso y radicar lo que corresponda.',
  '¿Cuál es la actuación correcta?',
  ['Tramitar la inscripción en carrera con fundamento en la antigüedad y en la buena calificación de su jefe, porque cuatro años de permanencia consolidan una estabilidad equivalente a la del empleado de carrera.',
   'Explicarle que no puede recibirle el escrito, porque la inscripción en carrera es un asunto de la Comisión Nacional del Servicio Civil y la entidad carece por completo de competencia para radicarlo o responderlo.',
   'Explicarle que la carrera solo se adquiere superando el concurso de méritos, que la antigüedad en provisionalidad no la otorga, radicar su escrito para la respuesta del competente y dejar constancia de la orientación.',
   'Proyectar un acto que reconozca su permanencia como derecho preferente para la próxima vacante, de modo que no quede desprotegido mientras se abre un concurso que podría tardar varios años más.'],
  'Correcto. La carrera se adquiere solo por concurso de méritos: la antigüedad en provisionalidad no la otorga, por larga que sea, y una buena calificación tampoco. Y fíjese en el límite de su rol: usted orienta, radica y deja constancia; la respuesta de fondo la da el competente.',
  'La antigüedad en provisionalidad no equivale a derechos de carrera y ceder a la presión no sanea la falta de concurso. Tampoco es cierto que la entidad no tenga competencia para radicar: negarse a recibir el escrito incumple el deber de atención. Y «reconocer un derecho preferente» por acto administrativo sería crear un derecho que la norma no prevé.'),

 (1,
  'En una reunión del equipo de la División de Gestión Humana, Camila sostiene que a Esteban, contratista de prestación de servicios que apoya el área hace un año, se le debe tramitar la evaluación del desempeño, reconocerle vacaciones remuneradas y computarle ese tiempo para carrera, «porque trabaja aquí todos los días igual que nosotros y lleva más tiempo que algunos de planta». El jefe le pide a usted precisar el punto antes de que el equipo tramite algo, porque de ello depende qué documentos se le abren a Esteban en el sistema de personal.',
  '¿Qué es lo correcto, según la naturaleza del vínculo?',
  ['Camila tiene razón: quien presta servicios de forma permanente para la entidad adquiere de hecho la condición de servidor público y, con ella, evaluación del desempeño, vacaciones remuneradas y tiempo para carrera.',
   'El contratista no es servidor público ni ocupa un empleo de la planta: su vínculo se rige por la contratación estatal y no por el régimen de función pública, de modo que no le corresponden carrera, situaciones administrativas ni evaluación del desempeño.',
   'El contratista es un servidor público de régimen especial, de manera que le corresponden la evaluación del desempeño y el cómputo del tiempo para carrera, pero no las vacaciones remuneradas, que son exclusivas de la planta.',
   'El contratista no es servidor público, pero una vez superado el año de vinculación continua la entidad debe incorporarlo a la planta temporal y, desde ese momento, reconocerle las garantías propias del empleo público.'],
  'Correcto. El contratista de prestación de servicios no ocupa un empleo de la planta y su vínculo es contractual, no legal y reglamentario: se rige por el estatuto de contratación, no por el régimen de función pública. No hay carrera, ni situaciones administrativas, ni evaluación del desempeño.',
  'La permanencia de hecho no convierte a nadie en servidor público ni crea derechos de carrera; esa es precisamente la situación irregular que la jurisprudencia llama contrato realidad, y corregirla no es tramitarle una evaluación del desempeño. Tampoco existe una «incorporación automática» a la planta temporal por cumplir un año.'),

 (0,
  'Un aspirante llama a la División un jueves por la tarde, muy molesto. Dice que revisó su resultado en la Convocatoria 285-2026 y que, según él, le calificaron mal una prueba. Exige que «ustedes, que son la entidad, le corrijan el puntaje» y, cuando usted le explica que hay un procedimiento, responde que entonces «reclamará ante la CNSC, que es la que manda en los concursos». El término de reclamación que fijó la convocatoria vence pasado mañana.',
  '¿Cuál es la orientación correcta?',
  ['Explicarle que la PGN tiene carrera especial y administra su propio concurso, de modo que la reclamación se presenta ante la propia entidad por el canal y dentro del término que fija la convocatoria, y dejar constancia de la orientación.',
   'Confirmarle que la entidad revisará y, si procede, corregirá su puntaje, porque la Procuraduría es la responsable del concurso y puede modificar de oficio los resultados que un aspirante cuestione por escrito.',
   'Orientarlo para que presente la reclamación ante la Comisión Nacional del Servicio Civil, que es el órgano constitucional encargado de administrar y vigilar las carreras de los servidores públicos del país.',
   'Explicarle que los puntajes publicados son definitivos y que no existe reclamación posible, de modo que su única alternativa sería demandar el acto ante la jurisdicción de lo contencioso administrativo.'],
  'Correcto. La PGN tiene régimen especial de carrera (art. 279 de la Constitución y Decretos Ley 262, 263 y 264 de 2000): administra su propio concurso, y la reclamación se presenta ante ella, por el canal y en el término de la convocatoria. Orientarlo mal aquí le cuesta el término al aspirante.',
  'Remitirlo a la CNSC es el error clásico, y con el término corriendo sería grave. Tampoco la entidad «corrige de oficio» un puntaje por una llamada: existe un procedimiento reglado. Y afirmar que no hay reclamación posible desconoce la propia convocatoria.'),

 (3,
  'Su jefe inmediato le pide, un lunes a primera hora, que «cree un empleo nuevo» para el área porque la carga de trabajo desbordó al equipo. Le dice que basta con describirlo en el manual específico de funciones y registrarlo en el SIGEP II, y que con eso ya se puede nombrar a alguien esta misma semana. Le insiste en que hay urgencia real, que «eso siempre se ha hecho así» y que el área de presupuesto ya le confirmó verbalmente que hay recursos. Usted sabe que en la planta de personal vigente ese empleo no existe.',
  '¿Qué corresponde hacer?',
  ['Describir el empleo en el manual específico y registrarlo en el SIGEP II de inmediato, porque el manual es el instrumento que crea los empleos y el registro en el sistema formaliza su existencia jurídica.',
   'Registrar el empleo únicamente en el SIGEP II, sin modificar el manual, porque ese sistema es el que da existencia a los cargos de la entidad y, una vez registrado, el nombramiento ya puede surtirse.',
   'Proyectar el acto de creación del empleo y someterlo a la firma del jefe de la División, porque la urgencia del servicio habilita a la dependencia a ampliar su planta cuando la carga de trabajo lo justifica.',
   'Explicarle que el manual describe y el SIGEP II registra, pero que ninguno de los dos crea empleos: el empleo nace en la planta de personal, cuya modificación exige estudio técnico y un acto de la autoridad competente.'],
  'Correcto. Son tres cosas distintas que la prueba mezcla a propósito: la planta de personal crea el empleo, el manual específico de funciones lo describe y el SIGEP II lo registra. Describir y registrar un empleo que no existe en la planta no lo hace existir, y el nombramiento sería nulo por falta de empleo.',
  'Ni el manual ni el SIGEP II crean empleos, y proyectar un acto de creación en la División tampoco: modificar la planta de personal exige estudio técnico y un acto de la autoridad competente. Que «siempre se haya hecho así» no cambia el orden de los instrumentos.'),

 (0,
  'Hay una vacante definitiva de un empleo de carrera en la entidad y no existe lista de elegibles vigente para ese cargo. Un directivo le pide que proyecte «para hoy» el nombramiento en provisionalidad de una persona externa que él recomienda. En la planta hay empleados de carrera que cumplirían los requisitos del empleo y tienen calificación sobresaliente. El directivo insiste en que la necesidad del servicio es real y en que él asume la responsabilidad de la decisión.',
  '¿Cómo debe encauzar la provisión de esa vacante?',
  ['Verificar primero si procede el encargo de un empleado de carrera que cumpla los requisitos y tenga buena calificación, porque el encargo tiene prelación, y solo si no procede proyectar la provisionalidad, dejando constancia de la verificación.',
   'Proyectar de una vez el nombramiento provisional de la persona recomendada, porque al no existir lista de elegibles la entidad recupera plena libertad para designar en provisionalidad a quien el nominador considere idóneo.',
   'Negarse a tramitar cualquier provisión, porque sin lista de elegibles vigente la vacante solo puede proveerse cuando se convoque un nuevo concurso y el empleo debe permanecer desierto hasta entonces.',
   'Proyectar el nombramiento provisional pero por un término máximo de seis meses, de modo que el acto quede condicionado y la vacante vuelva a estar disponible cuando los empleados de carrera puedan participar.'],
  'Correcto. Antes de la provisionalidad hay que agotar el encargo de empleados de carrera que cumplan los requisitos y tengan calificación satisfactoria: esa prelación protege el derecho de quienes ya ganaron su empleo por mérito. Y usted deja constancia de la verificación, que es lo que después demuestra que el orden se respetó.',
  'Que no haya lista de elegibles no devuelve libertad de designación: el orden legal de provisión sigue vigente, empezando por el encargo. Tampoco corresponde dejar el empleo desierto. Y ponerle un término de seis meses al acto no sanea nada: ese término existe —el artículo 188 del Decreto Ley 262 de 2000 lo fija, prorrogable por otro igual— pero es el límite de duración de la provisionalidad, no una autorización para saltarse la prelación del encargo.'),

 (2,
  'Para una vacante de la entidad, un aspirante presenta un título de formación técnica profesional y varios años de experiencia relacionada, y pregunta si cumple los requisitos. Un compañero le dice que lo dé por cumplido «porque se ve que sabe del tema y así agilizamos la posesión»; otro sostiene que debe descartarlo de inmediato porque no trae el título exacto que menciona el manual. El jefe le pide a usted el concepto escrito antes de que el trámite siga.',
  '¿Cómo debe verificar si el aspirante cumple?',
  ['Dar por cumplidos los requisitos sin revisar los soportes, porque la experiencia evidente del aspirante y su conocimiento acreditan el perfil, y así se agiliza una posesión que el servicio necesita.',
   'Descartar al aspirante de inmediato por no tener el título exacto, sin analizar la experiencia, porque los requisitos del manual son inflexibles y ninguna norma permite sustituir un requisito por otro.',
   'Consultar en el manual específico los requisitos del empleo y verificar si el caso encaja en alguna de las alternativas o equivalencias que el propio manual prevé, y consignar por escrito el resultado con los soportes revisados.',
   'Consultar al aspirante qué alternativa prefiere que se le aplique y, con base en su respuesta, consignar en el concepto la que resulte más favorable a su situación personal.'],
  'Correcto. La verificación no se resuelve ni por impresión ni por rigidez: se hace contra el manual, que es el que fija los requisitos y, muchas veces, las alternativas entre estudio y experiencia. El formato de la Convocatoria 285-2026 es un buen ejemplo: para el 4TC-17 ofrece dos alternativas de estudio, cada una con su exigencia de experiencia. Y el resultado se consigna por escrito (art. 63, núm. 7).',
  'Dar por cumplido lo que no está acreditado expone el acto a nulidad; descartar sin mirar las alternativas niega un derecho que el propio manual reconoce; y dejar que el aspirante elija la alternativa convierte una verificación objetiva en una negociación.'),

 (0,
  'Le encargan revisar por qué una vacante definitiva de un empleo de carrera lleva meses sin proveerse. Al indagar, descubre que el retiro por pensión del anterior titular nunca se registró en el plan anual de vacantes, de modo que la vacante quedó «invisible» para la planeación. Además, verifica que sí existe una lista de elegibles vigente para ese empleo. Un compañero le dice que lo más práctico es nombrar ya en provisionalidad a alguien conocido, «porque agotar la lista demora».',
  '¿Cómo debe encauzar la provisión?',
  ['Registrar la vacante en el plan anual de vacantes y, como existe lista de elegibles vigente, impulsar la provisión en estricto orden de mérito a partir de esa lista, dejando constancia del hallazgo.',
   'Dejar la vacante sin registrar y sin proveer hasta que alguien la solicite expresamente, porque si el empleo estuvo meses sin causar problemas no hay urgencia real en formalizar nada.',
   'Proyectar de inmediato el nombramiento en provisionalidad de la persona que sugiere el compañero, sin usar la lista, porque la provisionalidad es más rápida y la lista puede agotarse después.',
   'Registrar la vacante en el plan y solicitar que se declare desierta la lista de elegibles, porque una lista expedida antes de que la vacante existiera formalmente no puede aplicarse a ese empleo.'],
  'Correcto. Dos cosas a la vez: se corrige la planeación registrando la vacante, y se provee en estricto orden de mérito con la lista de elegibles vigente, que es el primer llamado para una vacante definitiva de carrera. Dejar constancia del hallazgo es lo que evita que el error se repita.',
  'No registrar perpetúa el error de planeación; saltar la lista para nombrar en provisionalidad desconoce el derecho de quienes ganaron el concurso y vicia el nombramiento; y no hay fundamento para declarar desierta una lista por un defecto de registro que es imputable a la entidad.'),

 (1,
  'En un comité, un servidor comenta que el MIPG «es puro papeleo de planeación» y que no tiene relación con lo que hace el área de Talento Humano, de modo que propone no dedicarle tiempo a diligenciar sus instrumentos. Varios asienten. El jefe le pide a usted la aclaración, porque los instrumentos los diligencia su equipo y quiere que todos entiendan para qué sirven antes del próximo autodiagnóstico institucional, cuyo resultado se reporta y se publica.',
  '¿Cuál es la aclaración correcta?',
  ['El servidor tiene razón en parte: el MIPG abarca la planeación institucional y los indicadores, de modo que el área de Talento Humano puede operar al margen del modelo sin consecuencia alguna.',
   'La primera dimensión del MIPG es precisamente Talento Humano, gestionada con la política de Gestión Estratégica del Talento Humano y sus rutas de creación de valor: por eso las tareas del área son el corazón del modelo, no un anexo suyo.',
   'El MIPG se relaciona con el talento humano únicamente a través de la nómina y la liquidación de salarios, así que basta con reportar esos datos financieros y no hace falta diligenciar otros instrumentos.',
   'El MIPG no aplica a la Procuraduría por tratarse de un órgano de control autónomo, de modo que los instrumentos que diligencia el área responden a una exigencia interna y no al modelo nacional.'],
  'Correcto. El MIPG tiene al Talento Humano como su primera dimensión, y la política de Gestión Estratégica del Talento Humano con sus rutas de creación de valor es justamente el instrumento que la desarrolla. Lo que hace el área no es periférico al modelo: es su punto de partida, porque el modelo considera al servidor el activo más importante de la entidad.',
  'Ni el talento humano está al margen del MIPG, ni la relación se agota en la nómina, ni el modelo es ajeno a la entidad. Diligenciar bien los instrumentos no es papeleo: es lo que permite medir y mejorar la propia gestión del área.'),

 (3,
  'Un viernes al final de la tarde, un servidor de otra dependencia se acerca a su puesto y le dice en voz baja: «ya que tú manejas el sistema de personal, sácame los datos de contacto y la dirección de un compañero de otra sede; es para un asunto personal, nada del trabajo». Insiste en que es rápido, que nadie se va a enterar y que él haría lo mismo por usted. No hay nadie más en la oficina en ese momento y su jefe ya se retiró. El sistema registra cada consulta con el usuario que la hace.',
  '¿Cuál es la actuación correcta?',
  ['Entregarle los datos, porque la información del empleo público tiene un componente de publicidad y quien tiene acceso técnico al sistema puede consultarla y compartirla sin restricción.',
   'Entregarle solo el número de teléfono y no la dirección, porque así comparte «lo mínimo indispensable» y evita que el compañero tenga que dar más vueltas para un asunto que es personal.',
   'Entregarle los datos pidiéndole que no diga de dónde los obtuvo, y registrar después la consulta en el sistema para que quede trazabilidad de que usted actuó de buena fe.',
   'No usar el acceso para un fin ajeno a su función: explicarle que el sistema es para la gestión del empleo, que los datos personales están protegidos por la Ley 1581 de 2012 y orientarlo sobre el canal formal.'],
  'Correcto. El acceso al sistema se tiene por razón de las funciones y para ellas: usarlo para un fin privado es una desviación, aunque el dato parezca inofensivo y la intención sea buena. Los datos personales de los servidores están protegidos por la Ley 1581 de 2012 y su tratamiento exige finalidad legítima.',
  'Que el empleo público tenga publicidad no vuelve públicos los datos de contacto personales. Entregar «solo el teléfono» es entregar un dato personal igual. Y pedir discreción mientras se registra la consulta no sanea nada: agrava, porque muestra conciencia de que el uso era indebido.'),

 (2,
  'La entidad tiene una necesidad permanente de personal por el crecimiento sostenido de la operación. Para cubrirla rápido, un directivo propone crear un «empleo temporal» y nombrar en él, sin concurso, a una persona de su confianza. Le dice que es una figura legal, que está prevista en la ley y que, al ser temporal, «no afecta el mérito de nadie». Le pide a usted que proyecte lo necesario para esta semana y le advierte que, si el trámite se demora, la responsabilidad por el retraso del servicio quedará registrada a nombre de la División.',
  '¿Cómo debe actuar?',
  ['Proyectar la creación del empleo temporal y el nombramiento como pide el directivo, porque la figura está prevista en la ley, permite vincular con agilidad sin concurso y su carácter temporal impide que llegue a afectar el mérito de nadie.',
   'Proyectar solo el nombramiento en el empleo temporal, sin crear formalmente el cargo ni motivarlo, porque lo urgente es cubrir la necesidad del servicio y la formalización puede completarse después.',
   'Explicarle que el empleo temporal es excepcional, solo procede para funciones no permanentes y exige motivación técnica y respaldo presupuestal, de modo que usarlo así es un fraude al mérito.',
   'Proyectar la creación del empleo temporal pero exigir que la persona se seleccione de la lista de elegibles vigente más próxima, de modo que la figura quede saneada por el componente de mérito.'],
  'Correcto. El empleo temporal existe para funciones que no son permanentes —un proyecto, un pico de carga, una labor de duración definida— y exige motivación técnica, planta de temporales y presupuesto. Usarlo para una necesidad permanente y para vincular sin concurso a una persona de confianza es usarlo contra su finalidad: eso es fraude al mérito.',
  'Ni la agilidad ni el carácter «temporal» del rótulo sanean el fraude; nombrar sin crear ni motivar el cargo agrava el vicio; y tomar a alguien de una lista de elegibles para un empleo distinto de aquel para el que concursó no es mérito, es otra irregularidad.'),

 (0,
  'Una vacante temporal de un empleo de carrera se proveyó por encargo. Mariana, empleada de carrera que creía tener mejor derecho por cumplir los requisitos y tener calificación sobresaliente, considera que el encargo se otorgó mal y anuncia que acudirá a la Comisión de Personal. Llega a su puesto con el escrito en la mano y le pide que usted «le diga de una vez si tiene razón o no», porque no quiere perder tiempo si el reclamo no procede.',
  '¿Cuál es la actuación correcta?',
  ['Radicar el escrito de Mariana y encauzarlo hacia la Comisión de Personal, que es el órgano interno que vela por que las actuaciones de personal se ajusten a las normas de carrera, informar al jefe y dejar constancia, sin pronunciarse sobre el fondo.',
   'Responderle usted mismo que el encargo ya está decidido y que no hay nada que revisar, porque una vez otorgado un encargo la decisión es definitiva e inmodificable, y así se evita un trámite inútil.',
   'Modificar el encargo a favor de Mariana de inmediato, porque si ella cumple los requisitos y tiene calificación sobresaliente es evidente que tenía mejor derecho y corregirlo cuanto antes reduce el perjuicio.',
   'Revisar con ella los soportes del encargo y darle su opinión técnica sobre si el reclamo prospera, para que decida con información si vale la pena presentarlo ante la Comisión de Personal.'],
  'Correcto. La Comisión de Personal es el órgano interno que vela por que las actuaciones de personal se ajusten a las normas de carrera; en la PGN, la División de Gestión Humana coordina y vigila la elección de sus representantes (art. 63, núm. 13). Su papel es radicar, encauzar, informar y dejar constancia: el fondo no lo resuelve usted.',
  'Cerrarle la puerta con un «ya está decidido» desconoce la instancia que existe precisamente para eso; modificar el encargo excede por completo su competencia; y anticiparle una opinión sobre si el reclamo prospera compromete su imparcialidad y puede inducirla a desistir de un derecho.'),

 (1,
  'Antes de abrir una vacante de un empleo de carrera, un directivo lo llama a su oficina y le pide que «ajuste» en el manual específico de funciones los requisitos de estudio y experiencia, de modo que coincidan exactamente con el perfil de una persona concreta que él quiere vincular. Le dice que el manual «es un documento interno que se puede actualizar cuando la entidad lo necesite» y que nadie va a notar el cambio. Cierra la puerta de la oficina antes de planteárselo.',
  '¿Cómo debe actuar?',
  ['Ajustar los requisitos como pide el directivo, porque el manual es un instrumento interno y flexible que la entidad adapta a sus necesidades de vinculación y, una vez ajustado y publicado, el nombramiento que se haga con él queda en regla.',
   'No ajustar los requisitos para favorecer a una persona, explicar que el manual refleja las funciones reales del empleo y que modificarlo con nombre propio vicia el instrumento, y dejar constancia escrita.',
   'Ajustar los requisitos solo «un poco», rebajando la experiencia exigida pero conservando el título, de modo que el candidato encaje sin que el cambio resulte evidente para quien revise el manual.',
   'Consultar al jefe de la División si procede el ajuste y, si él lo autoriza verbalmente, proyectarlo, porque la responsabilidad por la modificación recaería entonces en quien dio la instrucción.'],
  'Correcto. El manual describe las funciones reales del empleo y de ahí derivan sus requisitos: modificarlo «con nombre propio» invierte el orden, vulnera el mérito, la igualdad y la moralidad, y vicia el instrumento y el nombramiento que se funde en él. La constancia escrita no es un gesto defensivo: es lo que deja registro de una solicitud que no debió hacerse.',
  'Que el manual sea actualizable no significa que sea moldeable a una persona; «rebajar un poco» es el mismo vicio en menor escala y además revela la intención; y una autorización verbal no traslada la responsabilidad ni vuelve legítimo lo que no lo es.'),

 (3,
  'Durante la inducción, una persona recién posesionada en un empleo de la Procuraduría pregunta por qué a ella le exigieron concurso y a un compañero suyo, nombrado la misma semana en un cargo de nivel directivo, no. Un servidor le responde que «en los órganos de control todos los empleos son de carrera» y otro, que «como la PGN tiene régimen especial, allí nada es de carrera». El jefe le pide a usted precisar el punto.',
  '¿Cuál es la respuesta correcta sobre la clasificación de los empleos por su naturaleza?',
  ['Todos los empleos de la Procuraduría son de carrera, porque el artículo 125 de la Constitución establece la carrera como regla general y los órganos de control no tienen excepción alguna a ese mandato.',
   'Ningún empleo de la Procuraduría es de carrera, porque su régimen especial sustituye por completo el sistema de carrera y permite que la entidad provea todos sus cargos por designación directa del Procurador.',
   'La diferencia depende del nivel jerárquico: los empleos de los niveles directivo y asesor nunca son de carrera y los de los niveles profesional, técnico y asistencial siempre lo son, sin excepción posible.',
   'La carrera es la regla general y la excepción son, entre otros, los empleos de libre nombramiento y remoción: la PGN tiene carrera especial, no ausencia de carrera, y también en ella conviven empleos de carrera y de libre nombramiento y remoción.'],
  'Correcto. El artículo 125 de la Constitución hace de la carrera la regla general y deja como excepción, entre otros, los empleos de libre nombramiento y remoción. Que la PGN tenga carrera especial (art. 279) significa que su carrera se rige por normas propias, no que carezca de carrera: en ella conviven las dos naturalezas, y por eso la convocatoria que usted presenta existe.',
  'Ni todos los empleos son de carrera, ni la entidad puede proveerlos todos por designación. Y aunque el libre nombramiento y remoción se concentra en los niveles superiores, la clasificación por naturaleza no coincide mecánicamente con la clasificación por nivel: son dos criterios distintos que la prueba suele superponer.'),

 (2,
  'Se acerca la elección de los representantes de los servidores ante la Comisión de Personal y el jefe de la División le asigna apoyar el proceso. Un servidor con aspiraciones le pide que le facilite el listado completo de correos institucionales «para hacer campaña» y, por otro lado, un directivo le sugiere que la votación se haga en una reunión presencial de su dependencia «para asegurar que participe la gente seria». Ninguno de los dos quiere que quede nada por escrito.',
  '¿Cuál es la actuación correcta?',
  ['Facilitar el listado de correos al servidor, porque hacer campaña es legítimo y la información de contacto institucional de los servidores es de libre circulación dentro de la propia entidad.',
   'Aceptar la propuesta del directivo y organizar la votación en la reunión presencial de su dependencia, porque lo importante es que haya participación efectiva y el procedimiento concreto no está reglado en detalle.',
   'Aplicar el procedimiento establecido, dejar constancia de cada etapa, informar a su jefe las dos solicitudes y no acceder a ninguna: la División coordina y vigila una elección libre.',
   'Atender ambas solicitudes por tratarse de servidores de la entidad, pero exigirles que envíen la petición por escrito, de modo que la responsabilidad por lo que se haga recaiga en quienes lo pidieron.'],
  'Correcto. El numeral 13 del artículo 63 del Decreto Ley 262 de 2000 encarga a la División coordinar y vigilar la elección de los representantes de los servidores ante la Comisión de Personal. Vigilar una elección significa garantizar que sea libre e igual para todos: ni facilitar recursos a un aspirante, ni dejar que una dependencia defina dónde y quiénes votan.',
  'Entregar el listado a un aspirante le da una ventaja que los demás no tienen; concentrar la votación en una dependencia excluye a los demás servidores; y pedir que la solicitud irregular se haga por escrito no la vuelve atendible: solo deja constancia de que usted accedió a ella.'),

 (1,
  'Entra un grupo de servidores recién posesionados y el jefe le pide a usted apoyar la inducción. Un compañero le comenta que «eso se resuelve con un correo de bienvenida y el enlace al reglamento» y que la reinducción «no existe, eso es solo para los que entran». Usted debe proponer al jefe cómo se atenderá tanto a los que acaban de entrar como a un grupo de servidores antiguos que cambió de funciones tras una reorganización.',
  '¿Cuál es el planteamiento correcto?',
  ['El compañero tiene razón: la inducción se agota con la entrega de información institucional y la reinducción no está prevista en la gestión del talento humano, de modo que basta un correo para los nuevos.',
   'Hay que programar inducción para quienes ingresan y reinducción para quienes ya están pero enfrentan cambios —de funciones, de normas o de estructura—, porque el numeral 2 del artículo 63 encarga a la División contribuir al diseño y aplicación de ambos programas.',
   'Debe programarse inducción para los dos grupos por igual, porque quien cambia de funciones ingresa materialmente a un nuevo empleo y le corresponde exactamente el mismo proceso que a quien entra por primera vez a la entidad.',
   'No corresponde a la División programar nada: la inducción y la reinducción son responsabilidad del jefe inmediato de cada servidor, que es quien conoce las funciones concretas del puesto de trabajo.'],
  'Correcto. Son dos programas distintos y los dos existen: la inducción integra a quien llega y la reinducción actualiza a quien ya está cuando cambian las funciones, las normas o la estructura. El numeral 2 del artículo 63 encarga a la División contribuir a su diseño y aplicación, lo que incluye proponer cómo se atiende a cada grupo.',
  'La inducción no se agota en un correo, y la reinducción sí existe y es exactamente lo que necesita el grupo que cambió de funciones. Tampoco son lo mismo ni se delegan por completo en el jefe inmediato: el jefe aporta lo propio del puesto, pero el programa lo diseña y aplica el área, con la División contribuyendo a ello.'),
]
