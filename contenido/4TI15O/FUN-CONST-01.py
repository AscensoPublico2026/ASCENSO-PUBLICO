# -*- coding: utf-8 -*-
"""Día 10 · Constitución aplicada a la investigación y al control disciplinario — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-CONST-4TI15O-01',
    archivo='FUN-CONST-4TI15O-01-constitucion-aplicada-investigacion.html',
    dia=10,
    titulo_doc='Constitución aplicada a la investigación y al control disciplinario',
    h1='Constitución aplicada<br>a la investigación',
    kicker='Día 10 · Conocimientos específicos',
    sub='El cimiento de todo el bloque funcional: la <strong>supremacía de la Constitución</strong> (art. 4), el <strong>debido proceso</strong> (art. 29) y su regla de oro probatoria, los <strong>derechos fundamentales</strong> que limitan la actuación material de quien recolecta prueba (arts. 15, 28 y 32), el <strong>bloque de constitucionalidad</strong> (art. 93), los principios de la función administrativa (art. 209), la <strong>función disciplinaria de la PGN</strong> (arts. 277 y 278), la acción de tutela (art. 86) y la <strong>regla de exclusión de la prueba ilícita</strong>. Si una prueba se obtiene mal, no sirve: por eso esta guía va antes que cualquier técnica.',
    badges=['⏱ 100-120 min', '📜 Constitución', '🔍 Prueba'],
    fmeta='Constitución Política aplicada a la investigación y al control disciplinario',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Constitución aplicada a la investigación',
)

FUENTE = 'guias/FUN-CONST-3PU17L-01-derecho-constitucional-control-disciplinario.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- bloques nuevos
OBJ = (
    'Sabrás con precisión cómo el <strong>Técnico Investigador, código 4TI-15</strong>, adscrito a la '
    '<strong>Dirección Nacional de Investigaciones Especiales</strong>, debe practicar y documentar '
    'pruebas técnicas respetando la Constitución, para que lo recaudado <mark>sirva</mark> y no termine '
    'excluido. Este es el cimiento de todas las guías funcionales de la <strong>Convocatoria '
    '257-2026</strong>.'
)

REPARTO = (
    'Ten presente el reparto de roles del cargo: el <strong>Técnico Investigador 4TI-15</strong> '
    '<strong>practica pruebas técnicas por delegación del servidor competente</strong>, las documenta y '
    'las presenta con sus anexos, y proyecta autos y conceptos para la firma de quien decide; '
    '<mark>no decreta pruebas, no califica la falta, no decide de fondo ni firma</mark>. Dicho de otro '
    'modo: la Constitución te vincula en el <strong>cómo</strong> de lo que haces materialmente, que es '
    'justamente donde una prueba se gana o se pierde.'
)

TODA_ACTUACION = (
    'Toda actuación de un <strong>Técnico Investigador 4TI-15</strong> —practicar una prueba técnica, '
    'examinar un elemento, documentar un hallazgo, proyectar un auto para la firma del jefe— descansa '
    'sobre garantías constitucionales.'
)

MOD_LIMITES = (
    '<h4>Los límites materiales de tu actuación: arts. 15, 28 y 32</h4>\n'
    '      <p>Hay tres artículos de la Constitución que no suelen aparecer en las guías de cargos de '
    'escritorio y que, para ti, son el límite diario de lo que puedes hacer <em>con las manos</em>. '
    'Convienen memorizados:</p>\n'
    '      <div class="tabla-wrap"><table>\n'
    '        <thead><tr><th>Artículo</th><th>Qué protege</th><th>Qué significa en tu trabajo</th></tr></thead>\n'
    '        <tbody>\n'
    '          <tr><td><strong>Art. 15</strong></td><td>Intimidad personal y familiar, buen nombre y '
    'habeas data; inviolabilidad de la correspondencia y de los papeles privados, que solo pueden '
    'interceptarse o registrarse en los casos y con las formalidades que la ley establezca.</td>'
    '<td>No examinas un dispositivo, una comunicación ni un documento privado «porque estaba ahí»: hace '
    'falta la orden o la autorización que la ley prevea, y debe constar.</td></tr>\n'
    '          <tr><td><strong>Art. 28</strong></td><td>Libertad personal: nadie puede ser molestado en '
    'su persona o familia, ni detenido, ni su domicilio registrado, sino en virtud de mandamiento '
    'escrito de autoridad judicial competente, con las formalidades legales y por motivo previamente '
    'definido en la ley.</td><td>No retienes a nadie, no registras un domicilio y no «aseguras» a una '
    'persona. Si la situación lo exige, documentas y comunicas a la autoridad competente.</td></tr>\n'
    '          <tr><td><strong>Art. 32</strong></td><td>Flagrancia: al sorprendido en flagrancia puede '
    'aprehenderlo cualquier persona para llevarlo ante el juez, con reglas estrictas sobre el '
    'domicilio.</td><td>Es una facultad excepcional y de entrega inmediata a la autoridad judicial; no '
    'es una competencia de investigación penal que tu cargo pueda ejercer por su cuenta.</td></tr>\n'
    '        </tbody>\n'
    '      </table></div>\n'
    '      <div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div><p>Las preguntas que '
    'más se fallan en este punto son las que te ponen delante de un hallazgo valiosísimo obtenido '
    '<strong>sin la autorización debida</strong>. La respuesta correcta nunca es «aprovecharlo porque es '
    'decisivo»: una prueba obtenida con violación del debido proceso es <strong>nula de pleno '
    'derecho</strong> (art. 29) y arrastra consigo el trabajo que se apoye en ella. Lo que protege el '
    'caso es documentar cómo se obtuvo y poner la situación en conocimiento del competente.</p></div>'
)

MOD_REPARTO_PENAL = (
    '<h4>Quién investiga qué: arts. 250 y 281, y por qué te importan</h4>\n'
    '      <p>Dos artículos más cierran el mapa de competencias en el que tú te mueves, y los dos '
    'generan preguntas:</p>\n'
    '      <ul class="lista">\n'
    '        <li><strong>Art. 250 — la Fiscalía General de la Nación.</strong> A la Fiscalía corresponde '
    'el ejercicio de la acción penal y la investigación de los hechos que revistan las características '
    'de un delito, con las funciones y los controles judiciales que la Constitución prevé. Cuando en una '
    'investigación disciplinaria aparece un posible delito, <strong>el asunto penal no es tuyo ni de la '
    'PGN</strong>: se compulsa a la Fiscalía, y esa compulsa la decide el servidor competente, no el '
    'técnico que encontró el hecho.</li>\n'
    '        <li><strong>Art. 281 — el Defensor del Pueblo.</strong> Tras el '
    '<strong>Acto Legislativo 02 de 2015</strong>, el art. 281 dispone que <em>«el Defensor del Pueblo '
    'ejercerá sus funciones de manera autónoma»</em> y que <em>«será elegido por la Cámara de '
    'Representantes para un periodo institucional de cuatro años de terna elaborada por el Presidente '
    'de la República»</em>. La Defensoría integra el Ministerio Público, pero <mark>no está bajo la '
    'suprema dirección del Procurador</mark>: esa fórmula del texto original ya no está vigente. Es un '
    'distractor clásico, y lo encontrarás redactado con naturalidad en más de una opción de '
    'respuesta.</li>\n'
    '      </ul>\n'
    '      <div class="practica"><div class="practica-tag">🧩 En la práctica</div>\n'
    '        <p><strong>Situación.</strong> Practicando una prueba técnica usted documenta un hecho que '
    'parece delito y otro que parece detrimento patrimonial. Un compañero propone remitir copia a la '
    'Fiscalía y a la Contraloría «para ganar tiempo».</p>\n'
    '        <p><strong>Cómo proceder.</strong> Describir los dos hechos en el informe, sin calificarlos '
    'jurídicamente, y ponerlos en conocimiento del servidor competente. Él decide la compulsa. Remitir '
    'por cuenta propia a otra autoridad no acelera nada: desordena el expediente y excede el rol.</p>\n'
    '      </div>'
)

MOD_PROBATORIO = (
    '<p>Gran parte del trabajo del <strong>Técnico Investigador 4TI-15</strong> es '
    '<strong>probatorio</strong>: practica pruebas técnicas por delegación, documenta lo observado y '
    'presenta el resultado. Por eso el debido proceso probatorio merece un módulo propio. El '
    '<strong>artículo 29</strong>, en su parte final, contiene una regla de oro: <mark>"es nula, de '
    'pleno derecho, la prueba obtenida con violación del debido proceso"</mark>. Esta es la base '
    'constitucional de la <strong>regla de exclusión</strong> de la prueba ilícita: una prueba '
    'conseguida vulnerando derechos fundamentales o el debido proceso no puede fundar una decisión. Y '
    'conviene que lo veas sin rodeos: el eslabón que suele romper esa regla no es la decisión final, es '
    '<strong>la práctica</strong>. Es decir, tu trabajo.</p>'
)

R = [
    ('Sabrás con precisión cómo el <strong>Profesional Universitario, código 3PU-17</strong>, adscrito a las <strong>Procuradurías de Instrucción</strong>, debe instruir respetando la Constitución para no viciar lo actuado. Este es el cimiento de todas las guías funcionales de la <strong>Convocatoria 146-2026</strong>.',
     OBJ),
    ('Ten presente el reparto de roles del cargo: el <strong>Profesional Universitario 3PU-17</strong> recauda y practica pruebas, califica provisionalmente las faltas y proyecta autos y decisiones para la firma del jefe; <mark>no firma la decisión de fondo ni interviene ante jueces por su cuenta</mark>.',
     REPARTO),
    ('Toda actuación de un <strong>Profesional Universitario 3PU-17</strong> —recaudar una prueba, calificar una falta, proyectar un auto o el pliego de cargos para la firma del jefe— descansa sobre garantías constitucionales.',
     TODA_ACTUACION),
    ('<p>Gran parte del trabajo del Profesional Universitario 3PU-17 es <strong>probatorio</strong>: recauda, decreta y practica pruebas. Por eso el debido proceso probatorio merece un módulo propio. El <strong>artículo 29</strong>, en su parte final, contiene una regla de oro: <mark>"es nula, de pleno derecho, la prueba obtenida con violación del debido proceso"</mark>. Esta es la base constitucional de la <strong>regla de exclusión</strong> de la prueba ilícita: una prueba conseguida vulnerando derechos fundamentales o el debido proceso no puede fundar una decisión.</p>',
     MOD_PROBATORIO),
    ('<h4>Prueba ilícita vs. prueba irregular; pertinencia y conducencia</h4>',
     MOD_LIMITES + '\n      <h4>Prueba ilícita vs. prueba irregular; pertinencia y conducencia</h4>'),
    ('<!-- MÓDULO 11 -->',
     MOD_REPARTO_PENAL + '\n\n  <!-- MÓDULO 11 -->'),
]
SEC = aplicar_todas(SEC, R, estricto=True)
SEC = aplicar_todas(SEC, [
    # el bloque de competencias penales se ancla al final del módulo 10 (sujeto disciplinable)
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>',
     '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>',
     '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('Profesional Universitario 3PU-17', 'Técnico Investigador 4TI-15'),
    ('Profesional Universitario, código 3PU-17', 'Técnico Investigador, código 4TI-15'),
    ('Profesional Universitario', 'Técnico Investigador'),
    ('(3PU-17)', '(4TI-15)'),
    ('3PU-17', '4TI-15'),
    ('146-2026', '257-2026'),
    ('Procuradurías de Instrucción', 'dependencias que solicitan apoyo técnico'),
    ('Procuraduría de Instrucción', 'investigación disciplinaria'),
    # el "instructor" es el servidor competente, no el técnico
    ('El instructor', 'El servidor que instruye'),
    ('el instructor', 'el servidor que instruye'),
    ('al instructor', 'al servidor que instruye'),
    ('del instructor', 'del servidor que instruye'),
    ('un instructor', 'un servidor que instruye'),
    ('Un instructor', 'Un servidor que instruye'),
    ('instructor', 'servidor que instruye'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)   # filtro antifugas final

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre la Constitución '
              'aplicada a la investigación: supremacía constitucional, debido proceso y regla de exclusión, límites '
              'materiales de tu actuación (arts. 15, 28 y 32), bloque de constitucionalidad, principios del art. 209, '
              'función disciplinaria de la PGN y reparto de competencias con la Fiscalía.')

P = [
 (2,
  'Usted practica por delegación una prueba técnica en una oficina pública. Sobre un escritorio hay un cuaderno personal de la servidora investigada, abierto, con anotaciones que parecen directamente relacionadas con los hechos. Nadie le ha autorizado examinar documentos privados y la delegación se refiere a examinar un equipo de cómputo institucional. Un compañero le dice que lo fotografíe «porque está a la vista y eso no es un registro». La servidora no se encuentra en el lugar y el cuaderno quedaría para siempre fuera del expediente si usted no actúa ahora.',
  '¿Cuál es la actuación constitucionalmente correcta?',
  ['Fotografiar las páginas visibles y anexarlas al informe, porque el documento estaba a la vista y no hubo registro de ningún espacio cerrado ni acceso forzado a información reservada.',
   'Asegurar el cuaderno y entregarlo al despacho solicitante, para que sea este quien decida si lo incorpora o no al expediente de la investigación disciplinaria en curso.',
   'No examinar ni registrar el cuaderno, dejar constancia en el acta de su existencia y ubicación, y poner el hecho en conocimiento del servidor competente para que decida.',
   'Examinar el cuaderno únicamente en lo que se relacione con los hechos investigados, consignando que se limitó a lo pertinente y que no revisó anotaciones de carácter personal.'],
  'El artículo 15 protege los papeles privados: solo pueden examinarse o registrarse en los casos y con las formalidades que la ley establezca. Que algo esté a la vista no suple la autorización. Lo que protege el caso es documentar la existencia del elemento y dejar que el competente decida.',
  'Fotografiarlo, asegurarlo o «limitarse a lo pertinente» son todas formas de examinar un papel privado sin la autorización debida. Y una prueba obtenida con violación del debido proceso es nula de pleno derecho (art. 29): el hallazgo se perdería de todos modos.'),

 (3,
  'Durante una diligencia técnica, un servidor presente en el lugar se niega a entregar un elemento que usted debe examinar y comienza a retirarse. Usted está acompañado por un compañero y no hay servidores del despacho en el sitio. El compañero le dice que lo detenga hasta que llegue alguien, «porque la DNIE tiene funciones de policía judicial y esto es flagrancia». El elemento es relevante para la prueba delegada y el tiempo juega en contra.',
  '¿Qué dice la Constitución sobre lo que usted puede hacer?',
  ['Puede retenerlo transitoriamente, porque el artículo 32 autoriza a cualquier persona a aprehender a quien es sorprendido en flagrancia y llevarlo ante la autoridad competente.',
   'Puede impedirle físicamente la salida sin retenerlo, por un tiempo razonable, mientras se comunica con el despacho solicitante para recibir instrucciones sobre cómo proceder.',
   'Puede registrar sus pertenencias para recuperar el elemento, ya que la delegación de funciones de policía judicial habilita los actos necesarios para asegurar el material probatorio.',
   'No puede retenerlo ni registrarlo: debe documentar con precisión lo ocurrido y el elemento involucrado, y comunicarlo de inmediato al competente y a la autoridad que corresponda.'],
  'El artículo 28 reserva la privación de la libertad y el registro a mandamiento escrito de autoridad judicial competente, con las formalidades legales. Su delegación es para practicar pruebas técnicas: no confiere competencia penal. Lo que corresponde es documentar y comunicar.',
  'La flagrancia del art. 32 es una facultad excepcional de aprehensión y entrega inmediata al juez, referida a un delito, no un título para retener a quien no entrega un elemento en una diligencia disciplinaria. Ni la delegación ni la urgencia habilitan un registro.'),

 (0,
  'El despacho solicitante le pide que practique una prueba técnica sobre un dispositivo entregado por un tercero, que afirma haberlo tomado de la oficina del investigado sin autorización de nadie. El contenido, según el tercero, es decisivo. El despacho insiste en que lo examine «porque el dato es el que resuelve el caso» y le recuerda que el término está corriendo. Usted tiene la delegación firmada y el dispositivo en sus manos.',
  '¿Cuál es la actuación correcta?',
  ['Advertir por escrito al competente el origen del dispositivo y el riesgo de exclusión de la prueba, y no practicar el examen hasta que él resuelva expresamente cómo proceder.',
   'Practicar el examen y consignar en el informe el origen del dispositivo, para que el competente valore su admisibilidad al momento de decidir sobre el fondo del asunto.',
   'Practicar el examen limitándose a describir el estado del dispositivo, sin acceder a su contenido, de modo que no se vulnere la intimidad del investigado durante la diligencia.',
   'Devolver el dispositivo al tercero que lo entregó y dejar constancia de ello, porque un elemento de origen irregular no puede permanecer bajo custodia de la Dirección.'],
  'Un elemento de origen irregular contamina lo que se haga con él: la prueba obtenida con violación del debido proceso es nula de pleno derecho. Lo que protege el caso es advertir el riesgo por escrito y esperar la decisión del competente, no avanzar y dejar el problema para después.',
  'Practicar el examen y «dejar que el competente valore» traslada a otro un vicio que usted ya identificó. Y devolver el elemento al tercero elimina la posibilidad de que el competente resuelva sobre él.'),

 (1,
  'Usted debe proyectar un auto que niega una solicitud de prueba del investigado. La norma reglamentaria interna que aplicaría permite negarla sin motivación cuando el término apremia. Usted advierte que negar una prueba sin motivar afecta el derecho de defensa. El jefe está de acuerdo con la norma interna y le recuerda que ha operado así durante años en la dependencia, sin que nadie la cuestione.',
  '¿Cómo debe proceder a la luz del artículo 4 de la Constitución?',
  ['Aplicar la norma interna, porque mientras no haya sido anulada o inaplicada por una autoridad competente conserva su presunción de legalidad y obliga a quienes trabajan en la dependencia.',
   'Proyectar el auto motivando la negativa, y advertir por escrito al competente la tensión entre la norma interna y las garantías del artículo 29, dejando constancia de su análisis.',
   'Negarse a proyectar el auto e informar el caso a la Dirección, porque proyectar un documento que se apoya en una norma contraria a la Constitución lo compromete personalmente.',
   'Proyectar el auto conforme a la norma interna y añadir una nota aclarando que la falta de motivación obedece a lo previsto en ella y no a una omisión de quien lo elabora.'],
  'La Constitución es norma de normas (art. 4) y el debido proceso (art. 29) incluye la motivación de las decisiones que afectan la defensa. Proyectar motivando y advertir la tensión por escrito cumple su rol sin invadir la competencia de quien decide.',
  'Aplicar la norma interna sin motivar reproduce el vicio; negarse a proyectar abandona la tarea cuando sí había una vía correcta; y una nota aclaratoria no repara la falta de motivación del auto.'),

 (2,
  'En una capacitación, un compañero sostiene que los tratados de derechos humanos ratificados por Colombia «son recomendaciones» y que en el proceso disciplinario solo obligan la Constitución y la ley interna. Otro responde que esos tratados prevalecen siempre sobre la Constitución. El jefe les pide que precisen el punto porque va a usarse en un documento que la Dirección remitirá a otra dependencia.',
  '¿Cuál es la precisión correcta sobre el artículo 93?',
  ['Los tratados de derechos humanos ratificados prevalecen sobre la Constitución y, en caso de conflicto, desplazan cualquier norma constitucional que los contradiga en materia de garantías.',
   'Los tratados de derechos humanos son criterios de interpretación sin fuerza vinculante propia, de modo que orientan la lectura de las normas internas pero no pueden fundar una decisión.',
   'Los tratados y convenios internacionales ratificados que reconocen derechos humanos y prohíben su limitación en estados de excepción prevalecen en el orden interno, e integran el bloque de constitucionalidad.',
   'Los tratados de derechos humanos obligan únicamente cuando una ley interna los incorpora expresamente al procedimiento aplicable, y mientras eso no ocurra no son exigibles en sede disciplinaria.'],
  'El artículo 93 dispone que los tratados y convenios internacionales ratificados que reconocen derechos humanos y prohíben su limitación en estados de excepción prevalecen en el orden interno, y que los derechos y deberes constitucionales se interpretan conforme a los tratados ratificados: de ahí el bloque de constitucionalidad.',
  'Ni son meras recomendaciones sin fuerza, ni requieren una ley que los incorpore caso por caso, ni desplazan la Constitución: se integran con ella y orientan la interpretación de los derechos.'),

 (3,
  'El informe técnico que usted debe rendir exige consultar una base de datos institucional que contiene datos personales de terceros no vinculados a la investigación. Para llegar al dato que necesita, inevitablemente verá información de otras personas. El sistema registra cada consulta con su usuario. Un compañero le dice que descargue el reporte completo «y después filtra», porque es más rápido que hacer consultas puntuales.',
  '¿Cuál es la actuación correcta frente al artículo 15?',
  ['Descargar el reporte completo y filtrar después lo que no corresponde al caso, dejando constancia en el informe de que el resto de la información no fue utilizada.',
   'Descargar el reporte completo y conservarlo en su carpeta de trabajo por si el despacho amplía el objeto de la prueba, sin incorporarlo al expediente de la actuación.',
   'Pedir a un compañero con más permisos que haga la consulta y le entregue solo el dato, de modo que la descarga masiva no quede registrada bajo su propio usuario.',
   'Hacer consultas puntuales limitadas al dato que la prueba requiere y dejar constancia de la consulta realizada, sin extraer ni conservar información de terceros ajenos al caso.'],
  'El habeas data y la intimidad del artículo 15 exigen que el acceso a datos personales se limite a lo necesario para el fin que lo justifica. Consultas puntuales y constancia de lo consultado es lo que corresponde; una descarga masiva es un tratamiento de datos que nadie autorizó.',
  'Descargar todo «y filtrar después» ya es haber extraído datos de terceros; conservarlo por si acaso agrava el problema; y usar el usuario de un compañero rompe además la trazabilidad de la consulta.'),

 (1,
  'El investigado en un caso donde usted practicó una prueba técnica interpone acción de tutela: alega que la prueba se practicó sin que él pudiera estar presente y que eso vulneró su derecho de defensa. El juez pide informe a la entidad. Su jefe le pide que prepare los insumos técnicos del informe. Usted revisa el acta y confirma que la diligencia se practicó conforme al procedimiento y que la ausencia del investigado estaba prevista por la naturaleza de la prueba.',
  '¿Cómo debe preparar su aporte?',
  ['Elaborar un escrito dirigido al juez explicando por qué la tutela es improcedente, ya que usted es quien conoce de primera mano cómo se practicó la prueba técnica cuestionada.',
   'Aportar, de manera objetiva y documentada, el acta, la delegación y la descripción del procedimiento aplicado, sin pronunciarse sobre la procedencia de la tutela ni sobre el fondo.',
   'Aportar únicamente el acta, que es el documento que acredita lo ocurrido, y abstenerse de entregar la delegación y el procedimiento, que son documentos internos de la Dirección.',
   'Esperar a que el juez requiera expresamente los documentos técnicos, porque entregar información no solicitada en una tutela podría ampliar innecesariamente el debate procesal.'],
  'Su aporte es técnico y documental: el acta, la delegación y el procedimiento aplicado, presentados con objetividad. Quien contesta la tutela y argumenta sobre su procedencia es la entidad por conducto de quien tiene la competencia, no el técnico.',
  'Dirigirse al juez por su cuenta excede el rol; retener la delegación y el procedimiento debilita precisamente lo que acredita la regularidad; y esperar un requerimiento expreso retrasa la defensa de la actuación.'),

 (0,
  'Su jefe le pide que practique una prueba técnica con una técnica que, según él, «es la que siempre se ha usado», pero que el protocolo vigente sustituyó hace un año por otra más confiable. El resultado con la técnica antigua sería más rápido y probablemente coincidiría. El término es corto y el jefe insiste. Usted sabe que si la contraparte cuestiona la técnica, el resultado podría discutirse.',
  '¿Qué principio del artículo 209 orienta la respuesta y qué debe hacer?',
  ['La eficacia y la responsabilidad no se oponen a la celeridad: debe aplicar la técnica del protocolo vigente y exponer por escrito el impacto en el término, dejando constancia.',
   'La celeridad es el principio prevalente cuando hay un término en riesgo, de modo que debe aplicar la técnica más rápida y advertirlo en el informe para que el competente lo valore.',
   'La economía impone escoger la técnica menos costosa en tiempo y recursos, siempre que el resultado esperado sea equivalente, lo que aquí autoriza a usar la técnica anterior.',
   'La moralidad administrativa solo se ve comprometida si el resultado cambia, por lo que debe aplicar la técnica antigua y verificar después si coincide con la del protocolo vigente.'],
  'El artículo 209 somete la función administrativa a la igualdad, moralidad, eficacia, economía, celeridad, imparcialidad y publicidad, pero ninguno autoriza a sacrificar la validez de lo actuado. La técnica vigente se aplica y el impacto en el término se advierte por escrito.',
  'La celeridad y la economía no son licencias para usar un procedimiento sustituido: si el resultado se discute, el tiempo ganado se pierde entero. Y comprobar «después si coincide» es decidir primero y verificar al final.'),

 (2,
  'Un compañero afirma que, como la PGN tiene poder preferente, la Dirección puede asumir directamente cualquier investigación penal que aparezca en un caso disciplinario. Otro sostiene que la PGN no puede investigar nada que toque a un particular. El jefe pide precisión porque el informe debe explicar por qué una parte del asunto se remite a otra autoridad y otra se queda en la entidad. El informe debe salir hoy y es el documento con el que el despacho explicará el reparto a la persona interesada.',
  '¿Cuál es la precisión correcta?',
  ['La PGN puede asumir la investigación penal cuando el hecho surge dentro de una actuación disciplinaria propia, en virtud del poder preferente que la Constitución le reconoce en el art. 277.',
   'La PGN solo puede investigar disciplinariamente a servidores públicos y carece de toda competencia frente a particulares, incluso cuando estos ejercen funciones públicas o administran recursos.',
   'El poder preferente opera dentro de lo disciplinario frente al control interno de las entidades; la investigación de los delitos corresponde a la Fiscalía (art. 250), y lo fiscal a la Contraloría.',
   'La PGN y la Fiscalía tienen competencia concurrente sobre los hechos que son a la vez falta y delito, de modo que cualquiera de las dos puede asumir la investigación que primero inicie.'],
  'El poder preferente es disciplinario: desplaza al control interno disciplinario, no a la justicia penal. La investigación de los delitos corresponde a la Fiscalía conforme al art. 250, y el detrimento patrimonial a la Contraloría.',
  'Ni el poder preferente alcanza lo penal, ni la PGN carece por completo de competencia frente a particulares, ni existe competencia concurrente que permita a cualquiera de las dos entidades asumir lo penal.'),

 (3,
  'Durante la práctica de una prueba, el investigado le dice que no entiende qué se está haciendo ni para qué, que nadie le explicó nada y que se siente humillado por la forma en que se está desarrollando la diligencia. Técnicamente todo se está haciendo conforme al protocolo. Un compañero le dice que no se detenga, «porque explicar no es parte del procedimiento y solo alarga la diligencia». La diligencia continúa, hay otras personas presentes y el acta aún no se ha cerrado ni firmado.',
  '¿Qué corresponde hacer?',
  ['Continuar la diligencia sin interrupciones y consignar al final que el investigado manifestó incomodidad, para que el competente valore esa manifestación al decidir sobre el fondo.',
   'Suspender la diligencia hasta que el investigado cuente con su apoderado presente, porque sin asistencia profesional no puede comprender el alcance de lo que se está practicando.',
   'Explicarle el fondo del caso y las consecuencias que la prueba puede tener para él, de modo que comprenda la situación y pueda decidir si colabora con la diligencia.',
   'Informarle con claridad qué se está practicando y en qué consiste el procedimiento, dejar constancia de su manifestación y continuar conforme al protocolo, con trato digno.'],
  'La dignidad humana (art. 1) y el debido proceso no son un añadido a la técnica: informar con claridad qué se practica, dejar constancia de lo manifestado y mantener un trato digno es parte del procedimiento correcto, no una pérdida de tiempo.',
  'Callar y anotarlo al final deja sin atender una garantía durante la diligencia; suspenderla por decisión propia excede su rol; y explicarle el fondo del caso o sus consecuencias es precisamente lo que no le corresponde hacer.'),

 (1,
  'Usted encuentra dos sentencias de la Corte Constitucional que parecen aplicables a una duda de procedimiento que surgió en una diligencia. Una es anterior y la otra, más reciente, matiza la primera. El jefe le pide que el informe deje claro cuál es la regla aplicable. Un compañero le sugiere citar la que resulte más favorable al resultado que el despacho espera. El informe debe rendirse mañana y el jefe quiere que la explicación resista una eventual contradicción del investigado.',
  '¿Cómo debe tratarse la jurisprudencia constitucional?',
  ['Citar las dos sentencias sin tomar partido, porque elegir entre precedentes es una labor interpretativa que corresponde exclusivamente al servidor que adopta la decisión de fondo.',
   'Identificar la ratio decidendi de cada una y señalar objetivamente cuál es la regla vigente, sin elegirla por su conveniencia para el resultado que el despacho espera del caso.',
   'Citar únicamente la sentencia más reciente, porque en materia de precedente constitucional la fecha determina siempre cuál es la regla aplicable al caso concreto que se analiza.',
   'Omitir la referencia jurisprudencial del informe técnico, ya que la cita de sentencias corresponde a los documentos jurídicos y no a un informe de contenido técnico.'],
  'Lo que vincula de una sentencia es su ratio decidendi, no su fecha ni su conveniencia. Identificarla y señalar objetivamente la regla vigente es compatible con su rol; escoger la sentencia que favorece un resultado esperado es exactamente lo contrario de la objetividad.',
  'Citar ambas sin precisar la regla deja el trabajo a medias; la fecha por sí sola no define el precedente; y omitir la referencia priva al competente de un elemento que usted ya identificó.'),

 (0,
  'El acta de una diligencia que usted practicó omite la hora de inicio y la identificación de una de las personas presentes. Son dos omisiones de forma; el procedimiento técnico se cumplió íntegramente y el resultado no depende de esos datos. El acta ya fue incorporada al expediente. El investigado no ha alegado nada y el despacho está próximo a decidir. Nadie ha advertido las omisiones y usted conserva su libreta de campo, donde sí están anotados los dos datos.',
  '¿Cómo se califica la situación y qué debe hacer?',
  ['Es una irregularidad de forma, no una prueba ilícita: debe informarla por escrito al competente con los datos reales, para que valore si procede sanearla antes de decidir.',
   'Es una prueba ilícita que debe excluirse, porque un acta incompleta no permite verificar las condiciones en que se practicó la diligencia ni contradecir lo consignado en ella.',
   'No es irregularidad alguna, dado que el procedimiento técnico se cumplió y los datos omitidos no inciden en el resultado que el informe técnico consigna sobre el material examinado.',
   'Es una irregularidad que debe corregirse directamente en el acta ya incorporada, anotando al margen los datos faltantes y la fecha en que se hizo la anotación correspondiente.'],
  'Conviene distinguir la prueba ilícita —obtenida con violación de derechos fundamentales, que se excluye— de la prueba irregular, con defectos de forma que a veces pueden sanearse. Aquí lo que corresponde es informar por escrito con los datos reales y dejar que el competente resuelva.',
  'No es una prueba ilícita, pero tampoco es irrelevante: el acta es lo que permite verificar y contradecir. Y corregirla por su cuenta, aunque sea al margen, es intervenir un documento ya incorporado al expediente.'),

 (2,
  'Dos investigaciones equivalentes llegan a la Dirección. En una, el investigado es un servidor de alto nivel y el caso tiene atención pública; en la otra, nadie ha preguntado. Para la primera, el despacho pide que la diligencia se practique con dos técnicos y registro audiovisual; para la segunda, con el procedimiento estándar. Usted debe practicar las dos y advierte la diferencia de trato.',
  '¿Qué principio constitucional está en juego y cómo debe actuar?',
  ['La publicidad: la mayor atención pública justifica objetivamente un registro más completo de la diligencia, de modo que la diferencia de trato es razonable y no requiere ningún ajuste.',
   'La celeridad: debe aplicar el procedimiento más completo solo donde el despacho lo pidió, para no consumir en el segundo caso recursos que la dependencia no ha considerado necesarios.',
   'La igualdad del art. 13 y del art. 209: debe practicar las dos con el mismo rigor técnico y plantear por escrito la diferencia de trato para que la Dirección la unifique o la justifique.',
   'La imparcialidad: debe negarse a practicar la diligencia reforzada en el primer caso, porque aplicar un estándar distinto por el perfil del investigado compromete su propia objetividad.'],
  'La igualdad (arts. 13 y 209) exige que el estándar técnico no dependa del perfil del investigado. Lo que corresponde es aplicar el mismo rigor y plantear la diferencia por escrito, para que la Dirección la unifique o explique su razón.',
  'La atención pública no es una razón válida para un doble estándar probatorio; limitarse a lo pedido consolida la desigualdad; y negarse a practicar la diligencia reforzada renuncia a un mayor rigor que sí era posible.'),

 (3,
  'El despacho solicitante le pide que practique una prueba técnica sobre comunicaciones privadas del investigado, y adjunta una autorización suscrita por un servidor de la propia dependencia, no por autoridad judicial. Le explican que en la entidad «siempre se ha hecho así» para los casos disciplinarios y que la práctica nunca ha sido cuestionada. El término vence pasado mañana. Usted debe practicar la prueba pasado mañana y la autorización llegó adjunta al correo de la solicitud, sin ningún otro soporte.',
  '¿Cuál es la actuación correcta?',
  ['Practicar la prueba amparado en la autorización recibida, ya que proviene de la dependencia competente para el asunto disciplinario y usted no tiene que calificar su validez jurídica.',
   'Practicar la prueba y consignar en el informe que la autorización no fue expedida por autoridad judicial, de modo que el competente valore su validez al momento de decidir.',
   'Devolver la solicitud sin trámite y archivar la comunicación recibida, porque una autorización expedida por autoridad incompetente no puede generar ninguna actuación en la Dirección.',
   'No practicar la prueba, advertir por escrito al competente que la interceptación o registro de comunicaciones exige mandamiento de autoridad judicial, y pedir instrucción expresa.'],
  'El artículo 15 reserva la interceptación y el registro de comunicaciones a los casos y formalidades que la ley establezca, y el artículo 28 exige mandamiento escrito de autoridad judicial competente. Una autorización interna no suple eso: advertirlo por escrito y pedir instrucción expresa es lo que protege el caso.',
  'Practicar la prueba —con o sin advertencia en el informe— produciría material nulo de pleno derecho. Y devolver la solicitud sin trámite ni advertencia deja a la dependencia repitiendo la misma práctica en el próximo caso.'),

 (1,
  'Faltan doce días para la prueba escrita y usted advierte que recuerda los artículos de memoria, pero falla en los casos: duda entre dos opciones que ambas parecen respetar la Constitución. Su lista de errores muestra que casi siempre elige la opción que resuelve el problema práctico y descarta la que documenta y consulta. El bloque funcional, el más extenso, apenas comienza. Lleva un registro de los simulacros resueltos y el mismo patrón se repite en las cuatro últimas sesiones de práctica.',
  '¿Cuál es la mejor manera de corregir ese patrón?',
  ['Memorizar el texto literal de los artículos 4, 15, 28, 29, 32, 93, 209, 277 y 278, ya que la mayoría de las preguntas se resuelven identificando la norma exacta que aplica al caso.',
   'Preguntarse en cada caso, antes de mirar las opciones, qué garantía está en juego y si lo que la opción propone es algo que su cargo puede hacer, usando las dos cosas como filtro.',
   'Resolver el mayor número posible de simulacros constitucionales hasta que la intuición mejore, y dejar el estudio del texto normativo para los últimos días antes de la prueba.',
   'Concentrarse en los módulos de prueba ilícita y regla de exclusión, que son los que más preguntas generan, y repasar el resto de los artículos solo con los resúmenes de cada guía.'],
  'El patrón revela un problema de encuadre, no de memoria: casi todos estos casos se resuelven con dos preguntas —qué garantía está en juego y si la conducta propuesta cabe en su rol—. Convertirlas en filtro previo es lo que hace visible la opción correcta.',
  'Memorizar el texto no corrige un error de encuadre; repetir simulacros sin cambiar el método repite el error; y concentrarse solo en la regla de exclusión deja fuera la mitad de los casos que la prueba plantea.'),
]
