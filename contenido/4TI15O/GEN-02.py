# -*- coding: utf-8 -*-
"""Día 3 · La Relación Estado-Ciudadano — Técnico Investigador 4TI-15 (Conv. 257-2026)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas

META = dict(
    codigo='GEN-02-PGN-4TI15O',
    archivo='GEN-02-PGN-4TI15O-relacion-estado-ciudadano.html',
    dia=3,
    titulo_doc='La Relación Estado–Ciudadano',
    h1='La Relación Estado–Ciudadano',
    kicker='Día 3 · Conocimientos comunes',
    sub='El Estado no existe para sí mismo: existe para <strong>servir a las personas</strong>. Aquí verás los <strong>derechos</strong> de las personas frente al Estado y los <strong>deberes</strong> del ciudadano (art. 95 CP), el servicio al ciudadano como principio y como política, los canales de atención y el buen trato, el <strong>derecho de petición</strong> (art. 23 CP y Ley 1755 de 2015) con sus términos, las <strong>PQRSD</strong>, la <strong>participación ciudadana y el control social</strong> (Ley 1757 de 2015), y la frontera entre información pública y reservada. Todo aplicado al <strong>Técnico Investigador 4TI-15</strong> del DNIE, que atiende personas en diligencias, requiere información a las entidades y maneja expedientes con reserva.',
    badges=['⏱ 95-115 min', '🏛️ Régimen PGN', '📘 Conocimientos comunes'],
    fmeta='La Relación Estado–Ciudadano (derechos y deberes, derecho de petición, PQRSD y participación)',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='La relación Estado–ciudadano',
)

SEC = secciones_mapeadas('guias/GEN-02-PGN-4SP13-relacion-estado-ciudadano.html')

MOD8 = '''<h3 class="modulo">Módulo 8 · Tu rol como Técnico Investigador en la relación Estado-ciudadano</h3>
  <p>Cerramos aterrizando todo en tu cargo. Como <strong>Técnico Investigador (4TI-15)</strong> de la Dirección Nacional de Investigaciones Especiales no estarás en un punto de atención todo el día, pero la relación Estado-ciudadano te alcanza por tres vías muy concretas. La primera: en las <strong>diligencias</strong> tratas con personas —quejosos, investigados, testigos, servidores de la entidad visitada— y cada una de ellas es titular de derechos. La segunda: <strong>requieres información</strong> a entidades y a particulares, y ese requerimiento también es una actuación administrativa sujeta a principios. La tercera: el expediente que apoyas contiene <mark>información reservada y datos personales</mark>, y de tu cuidado depende que la reserva se respete.</p>
  <p>Hay además una razón de examen: <strong>atención al usuario</strong> y la relación con el ciudadano son <strong>conocimientos comunes</strong> expresamente listados en el formato de convocatoria de tu empleo. Se preguntan aunque tu cargo sea técnico, y se preguntan con casos: una persona que exige una respuesta inmediata, un peticionario que pide copia de un expediente en curso, alguien que te aborda en la calle durante una diligencia.</p>
  <h4>Los límites de tu rol (y por qué son un cuidado, no una limitación)</h4>
  <p>Es tan importante saber lo que <strong>sí</strong> haces como lo que <strong>no</strong> te corresponde. No decides el fondo de una queja, no calificas si una conducta es falta disciplinaria, no emites conceptos jurídicos a nombre de la entidad y no entregas por tu cuenta información sujeta a reserva. Cuando una persona te presiona para que "le adelantes el resultado" o "le digas qué encontraste", la respuesta correcta no es inventar ni prometer: es <mark>orientarla sobre el trámite y remitirla a quien sí tiene la competencia</mark>. Reconocer tus límites <strong>protege al ciudadano</strong> —de información equivocada— y te protege a ti —de asumir responsabilidades ajenas y de comprometer la reserva de la actuación—.</p>
  <div class="tabla-wrap"><table>
    <tr><th>Situación</th><th>Lo que SÍ haces (nivel técnico)</th><th>Lo que NO te corresponde</th></tr>
    <tr><td>Una persona quiere presentar una queja</td><td>Orientarla sobre dónde y cómo radicarla, y recibirla si corresponde</td><td>Valorar si los hechos constituyen falta disciplinaria</td></tr>
    <tr><td>Durante una diligencia alguien te pregunta qué encontraste</td><td>Explicar el objeto de la diligencia y remitir al despacho competente</td><td>Anticipar hallazgos o conclusiones del informe técnico</td></tr>
    <tr><td>Piden copia de piezas del expediente</td><td>Encauzar la petición por el trámite que corresponde</td><td>Entregar por tu cuenta información reservada o datos de terceros</td></tr>
    <tr><td>Presionan por un resultado</td><td>Informar sobre el trámite y los tiempos legales</td><td>Prometer decisiones o fijar fechas de resultado</td></tr>
  </table></div>
  <div class="practica"><div class="practica-tag">🛠️ En la práctica</div>
    <p>Durante una inspección, un servidor de la entidad visitada te dice: "Usted que está revisando los papeles, dígame de una vez si vamos a salir sancionados". Tú aplicas tu rol con claridad y amabilidad: "Mi función es practicar la prueba técnica que me encomendaron y rendir un informe; la valoración del caso y la decisión las adopta el funcionario competente, y la entidad será informada por los canales oficiales". No mentiste, no prometiste, no te pasaste de tu competencia y, aun así, <mark>serviste bien</mark>: diste certeza sobre lo que sí puedes hacer.</p>
  </div>'''

R = [
    # --- enfoque del cargo ---
    ('Piénsalo desde tu futura ventanilla en la Procuraduría: cada día llegará gente a radicar una queja, a pedir una copia, a preguntar por un trámite, a exigir "sus derechos".',
     'Piénsalo desde tu futuro trabajo en la Procuraduría: en cada diligencia habrá personas —quejosos, investigados, testigos, servidores de la entidad visitada— y todas llegarán con una pregunta, una exigencia o un temor.'),
    ('Hoy vas a dominar la <strong>relación Estado-ciudadano</strong> que un auxiliar administrativo debe conocer',
     'Hoy vas a dominar la <strong>relación Estado-ciudadano</strong> que un Técnico Investigador debe conocer'),
    ('Para un <strong>Secretario Procuraduría</strong> es doblemente importante: gran parte de tus funciones —recibir, radicar, tramitar, expedir copias, atender— <strong>son la relación Estado-ciudadano en acción</strong>.',
     'Para un <strong>Técnico Investigador</strong> es doblemente importante: la atención al usuario es un <strong>conocimiento común</strong> que tu convocatoria evalúa y, además, tu trabajo en diligencias te pone cara a cara con personas que son titulares de derechos.'),
    ('a la práctica diaria de tu ventanilla (petición, PQRSD, buen trato)',
     'a la práctica diaria de tu dependencia (petición, PQRSD, buen trato)'),
    ('ejemplos "En la práctica" en tu rol de Secretario Procuraduría',
     'ejemplos "En la práctica" en tu rol de Técnico Investigador'),
    ('Casos situados en tu rol de Secretario Procuraduría de la PGN',
     'Casos situados en tu rol de Técnico Investigador de la PGN'),
    ('Como <strong>Secretario Procuraduría</strong>, tú eres el rostro del Estado: recibes, radicas, tramitas, atiendes y orientas —sin decidir de fondo—, y de tu apoyo depende que esa relación funcione.',
     'Como <strong>Técnico Investigador</strong> también eres el rostro del Estado: atiendes personas en diligencias, requieres información y manejas expedientes sujetos a reserva —sin decidir de fondo—, y de tu cuidado depende que esa relación funcione.'),
    ('Un ciudadano te presiona para que le anticipes la decisión de su caso. Como Secretario Procuraduría (nivel Técnico), lo correcto es:',
     'Una persona te presiona para que le anticipes la decisión de su caso. Como Técnico Investigador (nivel técnico), lo correcto es:'),
]

SEC = aplicar_todas(SEC, R, estricto=True)

# Módulo 8 completo
i = SEC[2].find('<h3 class="modulo">Módulo 8 · Tu rol como')
j = SEC[2].find('<div class="box ojo">', i)
assert i > 0 and j > i, 'no se ubicó el módulo 8'
SEC[2] = SEC[2][:i] + MOD8 + '\n  ' + SEC[2][j:]

# identidad y menciones residuales
SEC = aplicar_todas(SEC, [('ventanilla', 'punto de atención'),
                          ('Secretario Procuraduría', 'Técnico Investigador'),
                          ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>',
                           '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
                          ], estricto=True)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre la relación '
              'Estado-ciudadano, el derecho de petición y el servicio al ciudadano. Los contextos son extensos y las '
              'cuatro opciones son plausibles. Al seleccionar una opción verás si acertaste y la explicación.')

P = [
 (1,
  'Un ciudadano radica en la Dirección Nacional de Investigaciones Especiales una solicitud en la que pide copia de varios documentos públicos que reposan en la dependencia. La petición es respetuosa y clara. El despacho atraviesa un pico de trabajo y un compañero le sugiere a usted dejarla «para cuando baje la carga», porque —dice— el silencio administrativo resuelve sola la solicitud y libera a la dependencia de responder de fondo.',
  '¿Cuál es el término aplicable y la forma correcta de proceder?',
  ['El término es de treinta días hábiles, porque toda solicitud dirigida a un órgano de control se tramita como una consulta especializada sobre sus funciones misionales y su régimen interno.',
   'El término es de diez días hábiles por tratarse de documentos e información: se proyecta la respuesta de fondo en ese plazo y, si no es posible, se informa antes del vencimiento el motivo y el nuevo plazo.',
   'No existe término perentorio cuando la dependencia atraviesa un pico de trabajo, de modo que basta responder cuando la carga lo permita, dejando constancia de la congestión en el expediente.',
   'El término es de quince días hábiles y, por tratarse de documentos, debe negarse el acceso salvo que el peticionario acredite un interés jurídico directo y actual en la información solicitada.'],
  'La Ley 1755 de 2015 fija diez días hábiles para las peticiones de documentos e información. Si no es posible responder a tiempo, hay que informar al peticionario antes del vencimiento los motivos y el plazo razonable en que se responderá. El silencio no exime del deber de responder.',
  'Ni treinta ni quince días, ni la congestión como excusa: el término de documentos es de diez días hábiles y el incumplimiento vulnera un derecho fundamental.'),

 (3,
  'Una persona presenta una petición en la que solicita información sobre una actuación, pero omite su dirección de notificación y no adjunta un documento indispensable para identificar el asunto. Un compañero propone negarla de inmediato «porque está incompleta» y otro, archivarla sin avisarle nada al peticionario para no generar expectativas. El jefe recuerda que una petición mal tramitada ya le costó una tutela a la dependencia el año pasado y pide que la respuesta quede proyectada hoy mismo.',
  'Conforme al artículo 17 del CPACA, ¿cómo debe procederse?',
  ['Negar la petición de inmediato por estar incompleta, ya que la carga de presentarla en debida forma recae exclusivamente en el ciudadano y la entidad no está obligada a subsanar sus errores.',
   'Archivar la solicitud sin comunicar nada al peticionario, porque una petición incompleta no genera ninguna obligación de respuesta ni hace correr término alguno para la autoridad.',
   'Responder con la información disponible aunque no corresponda a lo que el ciudadano quiso preguntar, de modo que el término se entienda cumplido formalmente dentro del plazo legal.',
   'Requerir al peticionario para que complete lo que falta dentro del plazo legal, suspendiendo el término mientras tanto, y solo si no lo completa proceder conforme a la ley.'],
  'El artículo 17 del CPACA ordena requerir al peticionario para que complete la información faltante; el término se suspende mientras se aporta. Una petición con defectos subsanables no se niega ni se archiva de plano.',
  'Negar, archivar en silencio o responder cualquier cosa vulnera el derecho de petición. Lo que procede es requerir y suspender el término.'),

 (2,
  'Durante una diligencia en una entidad territorial, un adulto mayor se acerca a usted, que es Técnico Investigador, y le pregunta dónde puede presentar una queja contra un funcionario. Hay varias personas esperando y un compañero le dice que siga con la inspección, que «la atención al público no es función del cargo» y que esa señora debería acudir a la oficina de atención al ciudadano de la entidad visitada. La persona vive en otro municipio, llegó con cita y un compañero insiste en que «si se le explica se demora más la diligencia».',
  '¿Cuál es la actuación correcta?',
  ['Indicarle que la Procuraduría solo recibe quejas por escrito y a través de su plataforma digital, de modo que debe conseguir ayuda de un tercero para presentarla por ese canal.',
   'Continuar con la inspección sin atenderla, porque interrumpir una diligencia técnica compromete el objeto de la actuación y la atención al público corresponde a otras dependencias.',
   'Orientarla con claridad y en lenguaje sencillo sobre los canales y la forma de radicar su queja, con la atención preferencial que le corresponde, sin descuidar el objeto de la diligencia.',
   'Recibirle la queja de manera informal y guardarla para entregarla al despacho cuando termine la diligencia, evitando así que la señora tenga que desplazarse nuevamente a otra sede.'],
  'La orientación es un deber de todo servidor, no de una dependencia en particular, y los adultos mayores tienen atención preferencial. Orientar bien toma un minuto y no compromete la diligencia.',
  'Ni despacharla, ni exigirle un canal digital, ni recibirle la queja por fuera del procedimiento: lo correcto es orientarla con claridad y con trato preferencial.'),

 (0,
  'Un periodista solicita copia de varias piezas de un expediente disciplinario que está en curso. Entre los documentos hay información pública, piezas sujetas a reserva mientras avanza la actuación y datos personales de un tercero ajeno al proceso. El jefe le pide a usted preparar el proyecto de respuesta y un compañero sugiere negar todo «para no equivocarse». El periodista advierte que publicará que la entidad «oculta información» si no recibe todo, y el jefe pide que el proyecto de respuesta quede motivado.',
  '¿Cuál es la actuación correcta frente a la solicitud?',
  ['Entregar las piezas públicas, negar de forma motivada las reservadas y proteger los datos personales del tercero, aplicando la divulgación parcial que prefiere la Ley 1712 de 2014.',
   'Negar la totalidad de la solicitud mientras la actuación esté en curso, porque la reserva del expediente cubre por igual todas las piezas que lo integran, sin distinción alguna.',
   'Entregar el expediente completo, porque la Ley de Transparencia establece que toda la información en poder del Estado es pública y de libre acceso, sin excepciones aplicables.',
   'Trasladar la solicitud al periodista para que indique cuáles piezas considera públicas y entregar únicamente las que él señale, dejando constancia de su manifestación en el expediente.'],
  'La Ley 1712 de 2014 consagra la máxima publicidad y prefiere la divulgación parcial frente a la negativa total: se entrega lo público, se niega motivadamente lo reservado y se protegen los datos personales de terceros.',
  'Ni negar todo, ni entregar todo, ni delegar en el peticionario la calificación de la información. La respuesta correcta separa lo público, lo reservado y los datos protegidos.'),

 (2,
  'En una capacitación, un compañero sostiene que el ciudadano «solo tiene derechos frente al Estado» y que hablar de deberes ciudadanos es un resabio autoritario. Otro responde que los deberes existen, pero que «no están en la Constitución sino en las leyes». El facilitador le pide a usted precisar el punto, porque de ello depende cómo se explica la relación en los casos de la prueba. El facilitador recuerda que en la prueba suelen aparecer opciones que niegan la existencia de deberes ciudadanos o que los reducen a simples recomendaciones.',
  '¿Cuál es la afirmación correcta?',
  ['El primer compañero tiene razón: la Constitución consagra únicamente derechos de las personas, y los deberes ciudadanos solo aparecen desarrollados en leyes posteriores de carácter sectorial.',
   'Los deberes del ciudadano existen pero carecen de fuerza jurídica, porque son recomendaciones de conducta cívica que el Estado no puede exigir ni respaldar con consecuencia alguna.',
   'El artículo 95 de la Constitución enumera deberes de la persona y del ciudadano, de modo que la relación es de doble vía: derechos que el Estado garantiza y deberes que la persona cumple.',
   'Los deberes del artículo 95 solo vinculan a los servidores públicos, porque son ellos quienes ejercen función pública y, por tanto, los únicos obligados frente al orden constitucional.'],
  'El artículo 95 consagra deberes de la persona y del ciudadano: respetar los derechos ajenos, obrar conforme al principio de solidaridad, colaborar con la justicia, contribuir al financiamiento de los gastos del Estado, entre otros. La relación es de doble vía.',
  'Los deberes están en la Constitución, tienen fuerza jurídica y vinculan a toda persona, no solo a los servidores públicos.'),

 (1,
  'Un ciudadano acude personalmente al DNIE y formula verbalmente una petición de información, porque no sabe escribir con fluidez y no tiene quien le ayude. El servidor que lo atiende le dice que vuelva con la solicitud por escrito, pues «las peticiones verbales no existen en la administración». El ciudadano se retira molesto y anuncia una queja. El ciudadano regresa al día siguiente con un familiar que escribió la solicitud por él y pregunta si esta vez «sí está bien hecha».',
  '¿Cuál es la lectura correcta?',
  ['El servidor actuó bien, porque el derecho de petición exige siempre la presentación de un escrito que permita identificar al peticionario y dejar constancia del contenido de la solicitud.',
   'El servidor se equivocó: la petición puede presentarse verbalmente y la entidad debe recibirla y dejar constancia, sin exigir formalidades que impidan el ejercicio del derecho.',
   'El servidor actuó bien, salvo que el ciudadano hubiera acreditado una discapacidad certificada, único supuesto en el que la ley admite la presentación verbal de una petición.',
   'El servidor debió remitir al ciudadano a un abogado, porque toda petición de información sobre actuaciones disciplinarias requiere presentación mediante apoderado con poder vigente.'],
  'El derecho de petición puede ejercerse verbalmente o por escrito y no requiere apoderado ni formalidades especiales. Exigir un escrito a quien no puede hacerlo convierte un derecho fundamental en un obstáculo.',
  'No se exige escrito, ni certificación de discapacidad, ni apoderado: la petición verbal es válida y la entidad debe recibirla y dejar constancia.'),

 (3,
  'Llega a la dependencia una petición que, por su contenido, corresponde a otra entidad del Estado. Un compañero propone devolvérsela al ciudadano indicándole que se equivocó, y otro sugiere archivarla porque «no somos competentes». El término ya empezó a correr y el peticionario es una persona mayor que vive lejos de la ciudad. El compañero insiste en que devolverla «es lo más rápido» y que la entidad no debe cargar con errores ajenos, mientras el término sigue corriendo.',
  'Conforme al artículo 21 del CPACA, ¿cómo debe procederse?',
  ['Devolver la petición al ciudadano explicándole que se equivocó de entidad, para que la presente ante la autoridad competente dentro del término que la ley le concede para ello.',
   'Archivar la petición por falta de competencia, dejando constancia en el expediente, porque la entidad no puede pronunciarse sobre asuntos ajenos a sus funciones misionales.',
   'Responder de fondo la petición con la información disponible, aunque el asunto sea de otra entidad, para no dejar al ciudadano sin respuesta dentro del término legal.',
   'Remitir la petición a la autoridad competente dentro del término legal e informar de ello al peticionario, para que el trámite continúe sin que la persona deba empezar de nuevo.'],
  'El artículo 21 del CPACA ordena remitir la petición al competente dentro de los cinco días siguientes a su recepción e informar al interesado. El ciudadano no debe cargar con el error de dirección.',
  'Ni devolver, ni archivar, ni responder lo que no es de la entidad: se remite al competente y se informa al peticionario.'),

 (0,
  'Durante una diligencia, el representante de la entidad visitada le pide a usted que le explique, «en términos sencillos», qué está revisando y para qué sirve el procedimiento. Un compañero le recomienda responder con tecnicismos y citas normativas extensas, para «marcar autoridad» y evitar preguntas incómodas sobre el alcance de la actuación. El representante añade que su abogado le dijo que la Procuraduría «no está obligada a explicar nada» y que cualquier información puede usarse en su contra.',
  '¿Qué criterio debe orientar su respuesta?',
  ['Usar lenguaje claro y comprensible para explicar el objeto y el alcance de la diligencia, porque la administración debe hacerse entender y eso no implica revelar hallazgos ni anticipar conclusiones.',
   'Responder con el mayor nivel técnico posible, ya que la precisión jurídica protege a la entidad y evita que la persona malinterprete el alcance de las facultades del servidor en la diligencia.',
   'Abstenerse de dar cualquier explicación, porque toda información sobre una actuación en curso está sujeta a reserva legal y comunicarla comprometería la validez de lo que se recaude.',
   'Remitir a la persona al sitio web institucional para que consulte allí los procedimientos, de modo que la explicación provenga de una fuente oficial y no de una manifestación personal.'],
  'El lenguaje claro es un deber de la administración: explicar el objeto de la diligencia no equivale a revelar hallazgos. Se puede ser claro sobre el procedimiento y reservado sobre el contenido.',
  'Ni el tecnicismo defensivo, ni el silencio absoluto, ni remitir a una página: se explica con claridad el objeto y se guarda la reserva sobre los resultados.'),

 (2,
  'Un grupo de ciudadanos solicita hacer seguimiento a la gestión de una entidad pública y pregunta en el DNIE qué mecanismos existen. Un compañero responde que «la participación ciudadana se agota en el voto» y otro, que las veedurías son organizaciones privadas sin respaldo legal que la administración no está obligada a atender. Uno de los ciudadanos trae un derecho de petición ya radicado y pregunta si debe esperar a las próximas elecciones para que le respondan.',
  '¿Cuál es la afirmación correcta sobre la participación y el control social?',
  ['La participación ciudadana se agota en el ejercicio del voto, de modo que entre elecciones los ciudadanos carecen de instrumentos jurídicos para incidir en la gestión de las entidades públicas.',
   'Las veedurías ciudadanas son agrupaciones privadas sin reconocimiento legal, por lo que las entidades pueden atender sus solicitudes de manera discrecional y sin sujeción a términos.',
   'La Constitución y la Ley 1757 de 2015 reconocen mecanismos de participación y de control social, como las veedurías ciudadanas, que las entidades deben atender y facilitar.',
   'El control social solo puede ejercerse a través de los órganos de control del Estado, de modo que los ciudadanos deben canalizar cualquier seguimiento mediante una queja formal ante la PGN.'],
  'Colombia es una democracia participativa: la Constitución y la Ley 1757 de 2015 regulan la participación y el control social, incluidas las veedurías ciudadanas, que tienen respaldo legal y deben ser atendidas.',
  'La participación no se agota en el voto, las veedurías sí tienen respaldo legal y el control social no es monopolio de los órganos de control.'),

 (1,
  'Una persona llega alterada a la sede, levanta la voz y exige que se le dé una respuesta inmediata sobre una queja que presentó hace dos meses. Hay otras personas esperando. Un compañero sugiere responderle en el mismo tono para «poner orden» y otro, ignorarla hasta que se calme por su cuenta. Otro compañero propone llamar a seguridad de inmediato, aunque la persona no ha amenazado a nadie y solo está hablando fuerte.',
  '¿Cuál es el manejo correcto de la situación?',
  ['Responder con firmeza en el mismo tono para restablecer el orden en la sala, dejando claro que ese comportamiento no se tolera y que no será atendida mientras continúe alterada.',
   'Mantener la calma, escuchar sin interrumpir, reconocer la molestia, verificar el estado del trámite e informar con precisión los pasos y tiempos, dejando constancia de lo informado.',
   'Ignorar a la persona hasta que se calme por sí sola, continuando con la atención de quienes esperan, porque responder a una exigencia agresiva premia ese comportamiento.',
   'Prometerle una respuesta para el día siguiente con tal de que se retire, y luego gestionar internamente lo que se pueda, dando prioridad a ese caso sobre los demás pendientes.'],
  'El protocolo de atención en situaciones difíciles es escuchar, reconocer la emoción, verificar la información y dar datos precisos sobre el trámite. La molestia del ciudadano no autoriza ni el maltrato ni la promesa falsa.',
  'Ni responder en el mismo tono, ni ignorar, ni prometer lo que no se puede cumplir: se escucha, se verifica y se informa con precisión.'),

 (3,
  'Un ciudadano presenta un escrito en el que, en un mismo documento, pide copia de unos documentos públicos, solicita que se investigue a un servidor y pide además asesoría jurídica gratuita para demandar a una entidad. Un compañero propone rechazar todo el escrito por indebida acumulación y otro, atender solo la solicitud de sanción. El escrito está firmado y tiene dirección de notificación, y el jefe pide que la respuesta cubra todo lo pedido sin dejar nada sin pronunciamiento.',
  '¿Cuál es la orientación correcta del escrito?',
  ['Rechazar de plano todo el escrito por acumular pretensiones distintas, exigiendo al ciudadano que presente tres solicitudes separadas antes de dar cualquier trámite a alguna de ellas.',
   'Atender solo la solicitud de sanción, que es la más relevante para la entidad, y omitir las demás pretensiones por tratarse de asuntos accesorios que no requieren respuesta de fondo.',
   'Responder únicamente la petición de documentos y guardar silencio sobre lo demás, dado que la entidad solo está obligada frente a las solicitudes que son claramente de su competencia.',
   'Separar las pretensiones: entregar la información pública en término, dar a la queja el trámite disciplinario que corresponda y explicar que la asesoría jurídica gratuita no es función de la PGN.'],
  'Un escrito puede contener varias pretensiones y la autoridad debe pronunciarse sobre todas: resolver lo que es de su competencia y orientar o remitir lo que no lo es. La asesoría jurídica gratuita corresponde, en su caso, a la Defensoría del Pueblo.',
  'Ni rechazar todo, ni atender una sola pretensión, ni guardar silencio: se separan las pretensiones y se responde cada una como corresponde.'),

 (0,
  'En el curso de una diligencia usted recibe de la entidad visitada una base de datos con información de empleados: nombres, cédulas, direcciones y datos de salud. Solo una parte es necesaria para el objeto del apoyo técnico. Un compañero sugiere conservarla completa «por si acaso» y compartirla por un grupo de mensajería del equipo para agilizar el trabajo. El equipo trabaja contrarreloj y el compañero insiste en que «nadie revisa qué archivos quedan en los teléfonos» una vez termina la diligencia.',
  '¿Cuál es la actuación correcta frente a esos datos personales?',
  ['Recaudar y conservar únicamente los datos pertinentes para el objeto de la actuación, protegerlos conforme a la Ley 1581 de 2012 y no difundirlos por canales ajenos a los institucionales.',
   'Conservar la base completa porque toda información recaudada en una diligencia pasa a ser pública al incorporarse al expediente, y compartirla por el canal más rápido disponible.',
   'Devolver la base completa a la entidad y continuar la diligencia sin ella, porque los datos personales de terceros no pueden recaudarse en ningún caso dentro de una actuación administrativa.',
   'Entregar la base al despacho sin revisarla, para que sea el funcionario competente quien decida qué datos conserva y cuáles elimina, sin que el técnico asuma ninguna responsabilidad.'],
  'Rigen los principios de finalidad y necesidad: se recauda lo pertinente al objeto de la actuación. Los datos sensibles, como los de salud, tienen protección reforzada y nunca se difunden por canales personales.',
  'Ni conservar todo, ni renunciar a recaudar lo necesario, ni trasladar la responsabilidad: se recauda lo pertinente y se protege conforme a la ley de datos.'),

 (2,
  'Un ciudadano insiste en que le expidan copia de una pieza del expediente que él mismo aportó hace meses, pero no recuerda la fecha ni el radicado. Un compañero propone negar la copia por falta de datos y otro, pedirle que vuelva cuando recuerde la información exacta del documento que necesita. La persona aportó el documento en una actuación de hace dos años y trae copia del recibido, aunque sin número de radicado legible.',
  '¿Cuál es la actuación que mejor respeta su derecho?',
  ['Negar la copia por falta de datos que permitan identificar la pieza, dejando constancia de la imposibilidad material de atender la solicitud en los términos planteados.',
   'Pedirle que regrese cuando tenga el radicado exacto, porque la carga de identificar el documento corresponde al peticionario y la entidad no puede hacer búsquedas generales.',
   'Buscar el documento con los datos que la persona sí puede aportar, usando los sistemas de información de la entidad, y expedir la copia que proceda dejando la trazabilidad del caso.',
   'Entregarle copia de todo el expediente para que él mismo ubique la pieza que le interesa, ahorrando así tiempo a la dependencia y garantizando que reciba lo que vino a buscar.'],
  'El principio de eficacia y el deber de colaboración imponen buscar con los datos disponibles antes de negar. La entidad tiene los sistemas de información; el ciudadano, no.',
  'Negar por falta de radicado o devolver al ciudadano traslada al usuario una carga que es de la entidad. Entregar el expediente completo, por su parte, desconoce la reserva y los datos de terceros.'),

 (1,
  'En una reunión del equipo se discute cómo responder una petición cuyo contenido exige un estudio técnico que no alcanza a hacerse dentro del término legal. Un compañero propone no responder y dejar que opere el silencio administrativo; otro, enviar una respuesta vacía que diga que «el asunto está en estudio» y cerrar el trámite. El jefe advierte que la dependencia ya tiene dos hallazgos por respuestas tardías y pide que la decisión quede documentada antes del vencimiento.',
  '¿Cuál es la actuación correcta?',
  ['No responder y permitir que opere el silencio administrativo negativo, porque así el ciudadano queda habilitado para acudir ante la jurisdicción sin esperar más tiempo del necesario.',
   'Informar al peticionario antes del vencimiento los motivos de la demora y el plazo razonable en que se responderá de fondo, y cumplir después con la respuesta sustancial.',
   'Enviar una respuesta formal que indique que el asunto está en estudio y archivar el trámite, de modo que el término se entienda cumplido y la dependencia quede al día en sus indicadores.',
   'Responder de fondo con la información incompleta disponible, aunque el estudio técnico no esté terminado, para evitar cualquier riesgo de sanción por el vencimiento del término.'],
  'Cuando no es posible responder a tiempo, la ley exige informar antes del vencimiento los motivos y el plazo razonable en que se responderá. El silencio no es una opción válida y una respuesta vacía no satisface el derecho.',
  'El silencio administrativo no sustituye la respuesta, una contestación evasiva no cumple el derecho de petición y responder mal por cumplir el plazo tampoco lo satisface.'),

 (3,
  'Una persona le pregunta a usted, durante una diligencia, por qué la Procuraduría puede revisar documentos de una entidad territorial elegida por voto popular. Sostiene que «eso es intromisión» y que la única forma de controlar a las autoridades locales es la elección siguiente. Le pide una explicación clara. La persona añade que varios vecinos piensan igual y que piensan presentar un derecho de petición colectivo para que la Procuraduría «se abstenga de intervenir».',
  '¿Qué explicación describe correctamente la relación entre democracia y control?',
  ['Tiene razón: en una democracia el control de las autoridades elegidas se ejerce exclusivamente en las urnas, y la vigilancia administrativa debilita la voluntad popular expresada en el voto.',
   'La vigilancia procede solo cuando la ciudadanía la solicita de manera expresa mediante una veeduría constituida formalmente, porque de lo contrario se afecta la autonomía territorial.',
   'La Procuraduría puede revisar documentos únicamente cuando existe una denuncia penal previa, pues sin ella no hay fundamento para intervenir en la gestión de una autoridad elegida.',
   'La legitimidad democrática no exime del control: la Constitución somete a todos los servidores al orden jurídico y encarga a la Procuraduría la vigilancia de la conducta oficial.'],
  'El voto legitima el origen del poder, no su ejercicio sin límites. El artículo 6 somete a los servidores a responsabilidad y el artículo 277 encarga a la Procuraduría vigilar la conducta de quienes desempeñan funciones públicas.',
  'Ni el control se agota en las urnas, ni depende de una veeduría o de una denuncia penal previa: la vigilancia de la conducta oficial es una función constitucional permanente.'),
]
