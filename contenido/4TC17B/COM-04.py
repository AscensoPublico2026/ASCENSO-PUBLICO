# -*- coding: utf-8 -*-
"""Día 9 · Alcance del cargo Técnico en Criminalística e integración de competencias — 4TC-17."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='4TC17B-COM-04',
    archivo='4TC17B-COM-04-alcance-cargo-tecnico-criminalistica.html',
    dia=9,
    titulo_doc='Alcance del cargo Técnico en Criminalística e integración de competencias',
    h1='Alcance del cargo<br>Técnico en Criminalística',
    kicker='Día 9 · Cierre del bloque comportamental',
    sub='Dónde empieza y dónde termina tu rol: el <strong>nivel Técnico</strong> dentro de la estructura de la PGN, la frontera entre <strong>apoyar técnicamente</strong> y <strong>decidir de fondo</strong>, los <strong>límites de la función de proyectar actos administrativos de personal</strong>, el reparto de competencias entre la División, la Secretaría General y el Procurador, qué se pone en conocimiento y a quién, y la integración de las <strong>cinco competencias comportamentales</strong> (Responsabilidad con la Organización B, Organización del Trabajo B, Gestión de la Información B, Cumplimiento de Parámetros de Trabajo C y Objetividad B). Es la guía que explica por qué tantas opciones de respuesta «suenan bien» y están mal: porque te hacen decidir lo que no te corresponde.',
    badges=['⏱ 95-115 min', '🧭 Alcance del rol', '🧠 Comportamental'],
    fmeta='Alcance del cargo Técnico en Criminalística 4TC-17 e integración de las cinco competencias',
    cargo='Técnico en Criminalística 4TC-17 (Nivel Técnico)',
    conv='285-2026',
    alerta='Alcance del cargo e integración de competencias',
)

FUENTE = 'guias/4SU11-COM-04-alcance-cargo-tecnico-integracion.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- bloques nuevos
UBICACION = (
    '<h4>Dónde se ubica exactamente el Técnico en Criminalística 4TC-17</h4>\n'
    '      <p>Tu cargo, <strong>Técnico en Criminalística código 4TC-17</strong>, se ubica en el '
    '<strong>nivel Técnico</strong> y, según el formato de la convocatoria 285-2026, su dependencia es '
    'la <strong>División de Gestión Humana</strong>, en planta global, con '
    '<strong>9 plazas</strong> ofertadas. Que sea nivel Técnico significa que tu función exige el '
    '<strong>dominio de una técnica o una tecnología</strong> —procedimientos de investigación, '
    'recolección y manejo de soportes documentales, elaboración de informes técnicos— aplicada con un '
    'grado de autonomía intermedio: mayor que el de un cargo asistencial (labores de apoyo manual, '
    'operativo o de trámite), pero menor que el de un cargo profesional, que decide de fondo dentro de '
    'su competencia.</p>\n'
    '      <p>Y hay un rasgo que distingue a tu cargo de casi cualquier otro empleo técnico de la '
    'entidad: el propósito del empleo es <mark>apoyar las actividades técnicas, técnico científicas y '
    'administrativas de investigación para la recolección de soportes documentales</mark> que soporte las '
    'investigaciones de la entidad. No apoyas un trámite: apoyas la construcción de la prueba. De ahí '
    'que el alcance de tu rol se juegue siempre en la misma frontera, y que la prueba escrita la explore '
    'una y otra vez.</p>'
)

FRONTERA = (
    '<div class="def-panel"><span class="def-label">Concepto</span><p>La frontera clave es: el nivel '
    'Técnico <mark>practica la verificación técnica, la documenta y la presenta</mark> —describe hechos, '
    'metodología y resultados—, mientras que el <mark>servidor competente califica, decide y firma</mark>, '
    'asumiendo la responsabilidad jurídica de esa decisión. Tú aportas el insumo probatorio; otro le da '
    'el valor jurídico.</p></div>\n'
    '      <h4>Qué significa "apoyar" en términos concretos</h4>\n'
    '      <p>Tus funciones lo dicen con precisión: <strong>establecer con la dependencia solicitante la '
    'metodología</strong> del apoyo, <strong>practicar las verificaciones técnicas por delegación</strong>, '
    '<strong>elaborar informes técnicos</strong>, <strong>presentar las pruebas practicadas y sus '
    'anexos</strong> ante la autoridad que solicitó el apoyo, <strong>proyectar</strong> autos, '
    'conceptos y actos administrativos, y aplicar los elementos técnicos para la evacuación de '
    'trámites. Fíjate en el verbo de la sexta: <em>proyectar</em>. Un auto que tú proyectas es un '
    '<strong>borrador</strong> hasta que el servidor con competencia lo revisa, lo ajusta si hace falta '
    'y lo firma. La firma no es un formalismo: es el acto por el cual alguien asume la responsabilidad '
    'jurídica de lo que ahí se decide.</p>\n'
    '      <h4>Por qué esta distinción no depende de "quién escribió cada palabra"</h4>\n'
    '      <p>Un malentendido frecuente es pensar que si tú practicaste la prueba, la documentaste y '
    'además redactaste el proyecto de auto, «en la práctica» la decisión fue tuya. No lo es: la '
    'responsabilidad jurídica no depende de quién escribió el texto, sino de quién lo revisó, lo avaló y '
    'lo firmó. Tu trabajo, por determinante que sea para el resultado, sigue siendo un '
    '<strong>insumo</strong> de la decisión, no la decisión.</p>'
)

AUTONOMIA = (
    '<h3>El alcance real de tu autonomía como Técnico en Criminalística</h3></div>\n'
    '    <div class="b-texto">\n'
    '      <p>Dentro de la frontera general que ya viste existe un margen de autonomía que sí te '
    'corresponde ejercer, y conviene delimitarlo con precisión para no caer en ninguno de los dos '
    'extremos: ni una pasividad que consulte cada detalle mínimo, ni una extralimitación que decida lo '
    'que no le corresponde.</p>\n'
    '      <div class="def-panel"><span class="def-label">Concepto</span><p>Tu <strong>autonomía '
    'técnica</strong> incluye decisiones <em>sobre cómo se hace el trabajo técnico</em>: qué técnica '
    'aplicar entre las procedentes, en qué orden examinar los elementos, cómo documentar un hallazgo, '
    'cómo estructurar el informe dentro del formato, cómo organizar tu día entre varios apoyos. '
    '<strong>No incluye</strong> decisiones sobre el <em>sentido jurídico</em> de la actuación, ni '
    'ampliar por cuenta propia el objeto de la delegación, ni firmar o notificar en nombre propio.</p></div>\n'
    '      <h4>Ejemplos concretos de decisiones que sí te corresponden</h4>\n'
    '      <p>Dentro de tu rol decides con autonomía razonable: qué técnica procedente aplicar y en qué '
    'secuencia; en qué orden examinar los elementos de un material extenso; cómo documentar y medir un '
    'hallazgo; cómo estructurar el informe técnico dentro del formato institucional para que la '
    'metodología y los resultados queden comprensibles; cómo priorizar tu jornada cuando tienes varios '
    'apoyos con términos distintos; y cuándo advertir por escrito una limitación de la técnica o del '
    'material.</p>\n'
    '      <h4>Ejemplos concretos de decisiones que exceden tu rol</h4>\n'
    '      <p>En cambio exceden tu rol: calificar la falta o atribuir responsabilidad en el informe; '
    'ampliar el alcance de la prueba más allá de la delegación recibida; decidir si se compulsan copias '
    'a otra autoridad; firmar o notificar en nombre propio un auto que proyectaste; ordenar una medida '
    'que requiera decisión del competente; y resolver por tu cuenta un vacío normativo relevante en '
    'lugar de consultarlo.</p>\n'
    '      <div class="tabla-wrap"><table>\n'
    '        <caption>Autonomía técnica: sí y no</caption>\n'
    '        <thead><tr><th>Sí te corresponde decidir</th><th>NO te corresponde decidir</th></tr></thead>\n'
    '        <tbody>\n'
    '          <tr><td>Qué técnica procedente aplicar y en qué secuencia.</td><td>Qué califica '
    'jurídicamente el hallazgo que documentaste.</td></tr>\n'
    '          <tr><td>Cómo describir con precisión qué acredita cada soporte.</td><td>Dar por cumplido '
    'un requisito que los soportes no acreditan.</td></tr>\n'
    '          <tr><td>Cómo estructurar el acto dentro del modelo establecido.</td><td>Firmar, conceder '
    'o reconocer en nombre propio el acto que proyectaste.</td></tr>\n'
    '          <tr><td>Advertir por escrito que falta un soporte o que el caso no encaja en el modelo.</td>'
    '<td>Si se compulsan copias y a qué autoridad se remiten.</td></tr>\n'
    '        </tbody>\n'
    '      </table></div>\n'
    '      ' + (
        '<h4>Los límites de tu función de proyectar actos administrativos</h4>\n'
        '      <p>Aquí está el punto más específico —y más mal entendido— del alcance de tu cargo. El '
        'manual de funciones dice que <mark>proyectas los actos administrativos de personal '
        '<strong>según los modelos y procedimientos establecidos</strong></mark>. Cada palabra de esa '
        'frase es un límite:</p>\n'
        '      <div class="flujo">\n'
        '        <div class="flujo-paso"><div class="fp-n">1</div><div><b>«Proyectas»</b><p>Proyectar es '
        'preparar el texto del acto para que lo firme quien tiene la competencia. No es expedir, no es '
        'autorizar y no es reconocer. Un acto de personal sin la firma del competente no existe '
        'jurídicamente, por bien redactado que esté.</p></div></div>\n'
        '        <div class="flujo-paso"><div class="fp-n">2</div><div><b>«Según los modelos '
        'establecidos»</b><p>No redactas desde cero ni improvisas la fórmula: la entidad tiene modelos y '
        'procedimientos, y apartarse de ellos es apartarse de la función. Si el caso no encaja en ningún '
        'modelo, eso se consulta y se deja constancia; no se resuelve por criterio propio.</p></div></div>\n'
        '        <div class="flujo-paso"><div class="fp-n">3</div><div><b>Quien firma depende del '
        'asunto</b><p>El <strong>artículo 63 del Decreto Ley 262 de 2000</strong> deja en la División los '
        'permisos de estudio de hasta dos horas diarias, la verificación de requisitos y la posesión en '
        'el nivel central; el <strong>artículo 62</strong> deja en la Secretaría General las vacaciones, '
        'las licencias, las comisiones de servicio y el reconocimiento de prestaciones; y los actos de '
        'nombramiento y de retiro los <strong>firma el Procurador General</strong>, aunque los proyecte '
        'la División.</p></div></div>\n'
        '        <div class="flujo-paso"><div class="fp-n">4</div><div><b>Con marco procedimental '
        'propio</b><p>Todo acto de personal es un acto administrativo: se motiva, se notifica o se '
        'comunica, admite recursos y adquiere firmeza conforme al <strong>CPACA</strong> (Ley 1437 de '
        '2011). Por eso el temario lo exige. Un acto bien decidido pero mal notificado no produce '
        'efectos, y ese defecto suele nacer en el trámite, no en la decisión.</p></div></div>\n'
        '      </div>\n'
        '      <div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div><p>Las opciones que te '
        'atribuyen la facultad de «autorizar», «conceder», «reconocer» o «firmar» un acto de personal, o '
        'que te hacen dar por cumplido un requisito para no frenar el servicio, son distractores '
        'diseñados exactamente sobre este punto. Suenan eficientes y son incorrectas: tu función es '
        '<strong>verificar, tramitar y proyectar</strong>, y dejar constancia de lo que falta.</p></div>\n'
        '      <h4>Qué se pone en conocimiento, a quién, y quién lo decide</h4>\n'
        '      <p>Verificando soportes y tramitando novedades es perfectamente posible que encuentres '
        'hechos que apunten a lo penal, a lo fiscal o a lo disciplinario: un título alterado, una prima '
        'pagada sin causa, una incompatibilidad no declarada. La regla de reparto es sencilla de recordar '
        'y muy frecuente en la prueba:</p>\n'
        '      <div class="tabla-wrap"><table>\n'
        '        <thead><tr><th>Lo que aparece</th><th>A quién corresponde</th><th>Qué haces tú</th></tr></thead>\n'
        '        <tbody>\n'
        '          <tr><td>Un soporte posiblemente falso o alterado</td><td>Fiscalía General de la '
        'Nación</td><td>Documentarlo como hecho observado, sin afirmar que hay delito, y ponerlo en '
        'conocimiento del competente, que decide la compulsa.</td></tr>\n'
        '          <tr><td>Un pago sin causa o un posible detrimento</td><td>Contraloría General de la '
        'República</td><td>Lo mismo: describir lo que muestran los documentos y poner en conocimiento; la '
        'remisión no la decides tú.</td></tr>\n'
        '          <tr><td>Una posible falta disciplinaria del servidor</td><td>El servidor competente de '
        'la PGN</td><td>Describir los hechos y lo que acredita cada soporte, sin calificar la '
        'falta.</td></tr>\n'
        '          <tr><td>Un requisito que no quedó acreditado</td><td>Quien decide el nombramiento o la '
        'novedad</td><td>Consignarlo en la constancia escrita y no proyectar el acto como si estuviera '
        'cumplido.</td></tr>\n'
        '        </tbody>\n'
        '      </table></div>\n'
        '      <p>En las cuatro filas tu conducta es la misma: <strong>describir y poner en '
        'conocimiento</strong>. Nunca callar el hallazgo, nunca calificarlo, nunca remitirlo por tu '
        'cuenta a otra autoridad.</p>'
    )
)

REQUISITOS = (
    '<div class="def-panel"><span class="def-label">Concepto</span><p>El formato de la convocatoria '
    '285-2026 exige para el Técnico en Criminalística 4TC-17, en estudio, '
    '<mark>tres años de educación superior en áreas relacionadas con las funciones del cargo</mark> '
    '<strong>o</strong> <mark>título de formación técnica profesional en áreas relacionadas más un curso '
    'específico relacionado con las funciones</mark>; y en experiencia, <mark>no requiere</mark> '
    '<strong>o</strong> <mark>un año de experiencia relacionada</mark>, según la alternativa de estudio '
    'que se acredite. La asignación básica reportada es de $8.972.318 (vigencia 2025).</p></div>\n'
    '      <h4>Por qué el requisito no es un título profesional</h4>\n'
    '      <p>Este requisito confirma, desde otro ángulo, la ubicación de tu cargo en el nivel Técnico: '
    'no se exige un título profesional completo —que sí se exigiría para un cargo del nivel '
    'Profesional—, sino una base formativa suficiente para <strong>dominar y aplicar una técnica</strong>, '
    'complementada con la experiencia o con un curso específico. Y hay una consecuencia que conviene '
    'tener clarísima: <strong>no debes asumir que el cargo es para abogados</strong>. Las alternativas '
    'de estudio admiten áreas relacionadas con las funciones, que para esta plaza son las de la '
    '<strong>División de Gestión Humana</strong>. Y esto explica algo que conviene tener clarísimo: '
    'aunque el empleo se llame «Técnico en Criminalística», los <strong>conocimientos esenciales '
    'específicos</strong> que la convocatoria evalúa son <mark>Constitución Política, gestión de talento '
    'humano, CPACA, herramientas ofimáticas, atención al usuario y conocimientos técnicos del área '
    'disciplinar</mark>. De criminalística es un renglón entre seis: no se te pide ser jurista ni '
    'criminalista en ejercicio, se te pide tramitar bien el talento humano dentro de un marco jurídico '
    'que debes conocer.</p>\n'
    '      <h4>Qué se espera, entonces, de tu formación jurídica</h4>\n'
    '      <p>Se espera que conozcas el marco que delimita tu actuación: la Constitución en lo que toca '
    'a la función pública y al debido proceso administrativo, el <strong>CPACA</strong> (motivación, '
    'notificación, recursos, firmeza, silencio administrativo), el régimen de <strong>situaciones '
    'administrativas</strong> y de carrera, y las reglas de manejo documental y de protección de datos '
    'personales. No se espera que califiques jurídicamente los hechos ni que resuelvas el fondo —eso es, '
    'precisamente, lo que no te corresponde—. La formación específica se adquiere con la capacitación '
    'institucional y la práctica, sobre esa base formativa inicial.</p>'
)

DEPENDENCIA = (
    '<p>Un elemento que conviene precisar es que el cargo Técnico en Criminalística 4TC-17 de esta '
    'convocatoria está adscrito a la <strong>División de Gestión Humana</strong> —que depende de la '
    '<strong>Secretaría General</strong>, numeral 1.6.1 del artículo 2 del Decreto Ley 262 de 2000—, en '
    '<strong>planta global</strong>: la plaza puede ubicarse donde la entidad lo requiera, y tu apoyo se '
    'presta <strong>a quien radique el trámite</strong> —un servidor, un jefe de dependencia, una '
    'procuraduría territorial, la propia Secretaría General—. Vale la pena entender si el alcance de tus '
    'funciones, y en particular la frontera entre tramitar y decidir, cambia según quién pida.</p>\n'
    '      <div class="def-panel"><span class="def-label">Concepto</span><p>La <mark>frontera '
    'técnico/decisorio es la misma</mark> cualquiera que sea el trámite: cambia el <strong>contenido '
    'temático</strong> y el procedimiento aplicable, pero no cambia tu naturaleza de apoyo técnico, ni '
    'la exigencia de que la decisión la asuma quien tiene la competencia. Lo que sí cambia con el asunto '
    'es <strong>quién es el competente</strong> que firma: la División, la Secretaría General o el '
    'Procurador General, según los artículos 62 y 63.</p></div>'
)

R = [
    # --- módulo 1
    ('<h4>Dónde se ubica exactamente el Sustanciador 4SU-11</h4>\n      <p>Tu cargo, Sustanciador código 4SU-11, se ubica en el <strong>nivel Técnico</strong>. Esto significa que tu función exige conocimientos específicos —normatividad, procedimientos, herramientas ofimáticas y de gestión documental— aplicados con un grado de autonomía intermedio: mayor que el de un cargo asistencial (que apoya labores más operativas), pero menor que el de un cargo profesional (que decide de fondo dentro de su competencia).</p>',
     UBICACION),
    # --- módulo 2: frontera
    ('<div class="def-panel"><span class="def-label">Concepto</span><p>La frontera clave es: el nivel Técnico <mark>apoya la proyección</mark> —redacta borradores sustantivos con base en el análisis de hechos y pruebas—, mientras que el nivel Profesional (o el jefe de despacho competente) <mark>decide y firma</mark> el acto final, asumiendo la responsabilidad jurídica de esa decisión.</p></div>\n      <h4>Qué significa "apoyar la proyección" en términos concretos</h4>\n      <p>Apoyar la proyección de un concepto, providencia, solicitud, constancia o recurso —tu función 1— significa que tú preparas el análisis y la redacción sustantiva del documento, pero ese documento es un <strong>borrador</strong> hasta que la persona con competencia decisoria lo revisa, eventualmente lo ajusta, y lo firma. La firma no es un trámite formal vacío: es el acto por el cual alguien asume la responsabilidad jurídica de la decisión contenida en el documento.</p>\n      <h4>Por qué esta distinción no depende de "quién redactó cada palabra"</h4>\n      <p>Un malentendido posible es pensar que, si tú redactaste la mayor parte del contenido sustantivo de un concepto, entonces "en la práctica" la decisión fue tuya. Esto no es correcto: la responsabilidad jurídica de una decisión no depende de quién escribió las palabras, sino de quién la revisó, avaló y firmó, asumiendo esa responsabilidad ante la ley y ante la propia entidad. Tu redacción, por sustantiva que sea, sigue siendo un insumo para esa decisión, no la decisión misma.</p>',
     FRONTERA),
    # --- módulo 3: autonomía (título + cuerpo completo)
    ('<h3>El alcance real de tu autonomía como Sustanciador</h3></div>\n    <div class="b-texto">\n      <p>Dentro de la frontera general que ya viste, existe un margen de autonomía que sí te corresponde ejercer como Sustanciador, y que conviene delimitar con precisión para no caer en ninguno de los dos extremos: ni una pasividad excesiva que consulte cada detalle mínimo, ni una extralimitación que decida lo que no le corresponde.</p>\n      <div class="def-panel"><span class="def-label">Concepto</span><p>Tu <strong>autonomía técnica</strong> incluye decisiones operativas dentro de tu función: cómo organizar tu análisis, qué pruebas priorizar en tu revisión, cómo estructurar la redacción de un borrador, cómo llevar tu control de términos. No incluye decisiones de fondo sobre el sentido de una actuación, ni la facultad de firmar o notificar un acto en tu propio nombre.</p></div>\n      <h4>Ejemplos concretos de decisiones que sí te corresponden</h4>\n      <p>Dentro de tu rol, decides con autonomía razonable: en qué orden revisar los documentos de un expediente extenso, qué estructura de redacción usar dentro del formato exigido para presentar mejor un argumento, cómo priorizar tu día cuando tienes varios proyectos pendientes, y qué información adicional solicitar dentro de un proceso cuando la normatividad te faculta para ello (tu función 2).</p>\n      <h4>Ejemplos concretos de decisiones que exceden tu rol</h4>\n      <p>En cambio, exceden tu rol: decidir el sentido final de un concepto o providencia sin que medie la revisión de tu jefe, firmar cualquier acto administrativo o disciplinario en tu propio nombre, notificar formalmente una decisión sin la autorización correspondiente, o resolver por tu cuenta un vacío normativo relevante sin consultar a quien tiene la competencia de definir el criterio institucional (como ya viste en la guía del día 6).</p>\n      <div class="tabla-wrap"><table>\n        <caption>Autonomía técnica: sí y no</caption>\n        <thead><tr><th>Sí te corresponde decidir</th><th>NO te corresponde decidir</th></tr></thead>\n        <tbody>\n          <tr><td>Cómo organizar y priorizar tu análisis de un expediente.</td><td>El sentido final de la decisión que se proyecta.</td></tr>\n          <tr><td>Qué estructura de redacción usar dentro del formato exigido.</td><td>Firmar el acto administrativo o disciplinario correspondiente.</td></tr>\n          <tr><td>Solicitar información adicional pertinente a un proceso.</td><td>Notificar formalmente una decisión sin autorización.</td></tr>\n        </tbody>\n      </table></div>',
     AUTONOMIA),
    # --- módulo 4: requisitos
    ('<div class="def-panel"><span class="def-label">Concepto</span><p>El manual de funciones exige para el Sustanciador 4SU-11 la <mark>aprobación de un año de educación superior</mark> en un listado amplio de programas (administración, derecho, ingenierías, ciencias sociales, entre otros) y <mark>un año y medio de experiencia relacionada</mark>, requisitos coherentes con un cargo que exige formación técnica de base, pero no una formación profesional completa ni una experiencia extensa de alta especialización.</p></div>\n      <h4>Por qué el requisito de estudio es "un año de educación superior", no un título profesional</h4>',
     REQUISITOS + '\n      <h4>__REQ_VIEJO__</h4>'),
    # --- módulo 9: dependencia
    ('<p>Un elemento que conviene precisar, porque puede generar dudas legítimas, es que el cargo Sustanciador 4SU-11 puede ubicarse en distintas dependencias dentro de la estructura de la PGN —Despacho del Procurador General, Despacho del Viceprocurador, direcciones nacionales especializadas, procuradurías delegadas, procuradurías regionales y provinciales, procuradurías judiciales, o el Centro de Conciliación en materia civil y comercial—. Vale la pena entender si el alcance de tus funciones, y en particular la frontera entre apoyo técnico y decisión de fondo, cambia según dónde te ubiques.</p>\n      <div class="def-panel"><span class="def-label">Concepto</span><p>La <mark>frontera Técnico/decisorio es la misma</mark> en cualquier dependencia de ubicación: cambia el <strong>contenido temático</strong> de lo que proyectas (un concepto disciplinario en una procuraduría delegada, un acta de conciliación en el Centro de Conciliación, un documento de apoyo al Despacho del Procurador), pero no cambia tu naturaleza de apoyo técnico bajo supervisión, ni la exigencia de que la decisión final la asuma quien tiene la competencia para ello.</p></div>',
     DEPENDENCIA),
]
SEC = aplicar_todas(SEC, R, estricto=True)
SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>',
     '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>',
     '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('(4SU-11)', '(4TC-17)'),
    ('4SU-11', '4TC-17'),
    ('Resolución 243 de 2026', 'Resolución 212 de 2026'),
    ('288-2026', '285-2026'),
    ('Estatuto de Conciliación', 'CPACA y el régimen de situaciones administrativas'),
    ('Centro de Conciliación en materia civil y comercial', 'dependencias que soliciten apoyo técnico'),
    ('Centro de Conciliación', 'División de Gestión Humana'),
    ('apoyo en sustanciación', 'apoyo técnico'),
    ('en sustanciación', 'en el apoyo técnico'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol('Técnico en Criminalística', 'Técnicos en Criminalística'), estricto=False)   # filtro antifugas final
for n in SEC:
    SEC[n] = SEC[n].replace('\n      <h4>__REQ_VIEJO__</h4>', '')

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el alcance del '
              'cargo Técnico en Criminalística 4TC-17: la frontera entre tramitar y decidir, los límites de la '
              'función de proyectar actos de personal, qué se pone en conocimiento y a quién, y la integración de las cinco competencias '
              'comportamentales. Son las preguntas que más distractores «que suenan bien» traen.')

P = [
 (2,
  'Usted está verificando los soportes de una hoja de vida para un encargo. Mientras le entrega los documentos, el propio servidor reconoce de viva voz que una de las certificaciones de experiencia «la hizo un amigo para completar el tiempo» y le dice que está dispuesto a «firmar lo que sea» para arreglarlo. Un compañero le sugiere recibirle de inmediato una declaración escrita y dejarla firmada, «para que no se arrepienta». Su tarea se limita a verificar los requisitos del encargo, y el jefe de la División no está en la oficina en ese momento.',
  '¿Cuál es la actuación que corresponde a su rol?',
  ['Recibir la declaración y anexarla a la constancia, ya que se trata de una manifestación espontánea cuya pérdida podría impedir que el hecho se conozca y se corrija oportunamente.',
   'Recibir la declaración por escrito pero sin firma, para dejar registro del contenido sin que constituya formalmente una declaración recibida fuera del objeto de su tarea.',
   'Documentar en la constancia que el servidor hizo esa manifestación, terminar la verificación de los requisitos y poner el hecho en conocimiento del competente para que decida.',
   'Suspender la verificación y comunicarse de inmediato con el jefe de la dependencia solicitante para pedir autorización que le permita recibir la declaración en ese mismo acto.'],
  'Su tarea acota el objeto: verificar requisitos. Recibir una declaración, y menos aún una preparada «para que no se arrepienta», excede ese objeto y además no tiene ningún valor recibida así. Lo correcto es documentar que la manifestación ocurrió, terminar la verificación —que ahora, con mayor razón, debe consignar que el requisito no está acreditado— y poner el hecho en conocimiento del competente.',
  'Recibir la declaración —con o sin firma— es actuar fuera de su función; y suspender la verificación para pedir autorización interrumpe lo que sí debía hacer, cuando bastaba documentar el hecho y continuar.'),

 (0,
  'Mientras verifica los soportes de una reclamación salarial, usted advierte que durante dos años se pagó a un servidor una prima técnica que su situación no permitía y que uno de los soportes que la respaldan parece alterado: podría haber un detrimento patrimonial y, además, un posible delito. Su tarea se refiere exclusivamente a verificar la autenticidad de tres soportes. Un compañero le dice que lo correcto es remitir copia de los hallazgos directamente a la Fiscalía y a la Contraloría, «porque son las autoridades competentes y así se gana tiempo».',
  '¿Qué corresponde hacer?',
  ['Describir los hallazgos en la constancia como hechos observados, sin calificarlos jurídicamente, y ponerlos en conocimiento del servidor competente, a quien corresponde decidir la compulsa de copias.',
   'Remitir copia de los hallazgos a la Fiscalía y a la Contraloría e informar luego de ello a su jefe, ya que la competencia penal y fiscal corresponde a esas entidades y no a la PGN.',
   'Limitar la constancia a la verificación de autenticidad que le fue encargada y abstenerse de mencionar los otros hallazgos, por tratarse de materias ajenas al objeto de su tarea.',
   'Ampliar por su cuenta la verificación para precisar los hallazgos penales y fiscales, de modo que la constancia llegue con el soporte suficiente para que las autoridades competentes puedan actuar.'],
  'El reparto es claro: lo penal a la Fiscalía y lo fiscal a la Contraloría, pero la compulsa la decide el servidor competente, no el técnico. Su conducta es describir sin calificar y poner en conocimiento, sin omitir el hallazgo ni ampliar la verificación por su cuenta.',
  'Remitir directamente a otras autoridades y ampliar el objeto de su tarea exceden su rol; omitir los hallazgos compromete la veracidad de la constancia. Describir y poner en conocimiento cumple las tres exigencias a la vez.'),

 (3,
  'Un servidor de una procuraduría regional le pide por teléfono que, aprovechando que usted ya tiene abierta su historia laboral por otro trámite, «le saque de una vez» el certificado de tiempo de servicio que necesita para una gestión personal. Le dice que es urgente, que él asume la responsabilidad y que la solicitud escrita llegará después. Usted no tiene ninguna solicitud radicada y la expedición de certificaciones es una función de la División que se surte por el canal previsto. Usted sabe que ese servidor ha tramitado antes solicitudes correctas y que la División sí expide esas certificaciones cuando se piden como corresponde.',
  '¿Cuál es la actuación correcta?',
  ['Expedir la certificación dejando constancia de que la solicitud escrita estaba pendiente, ya que el servidor que la pide asume expresamente la responsabilidad del trámite.',
   'Enviarle por mensajería los datos de tiempo de servicio sin expedir documento alguno, para no formalizar nada sin solicitud, y expedir la certificación cuando llegue el escrito.',
   'Negarse y no dar curso a la petición, informando al servidor que debe radicar la solicitud y que la División no atiende requerimientos formulados por vía telefónica.',
   'Explicar que la certificación se expide sobre una solicitud radicada, orientarlo sobre cómo presentarla —incluso por correo institucional— e informar a su jefe la urgencia planteada, dejando constancia.'],
  'Una certificación laboral es un documento que produce efectos frente a terceros y se expide sobre una solicitud que quede registrada: sin ella, no hay trámite que surtir y el documento quedaría sin respaldo. Pero tampoco corresponde cerrar la puerta: se orienta sobre cómo radicar, se informa la urgencia al jefe y se deja constancia.',
  'Expedir sin solicitud deja el documento sin respaldo, y mandar «los datos sin documento» es entregar información de una historia laboral por un canal informal, que es peor. Negarse sin encauzar la urgencia desatiende una necesidad real que tenía vía institucional.'),

 (1,
  'Usted proyectó un auto por solicitud del despacho competente. El jefe del despacho está de permiso y su informe técnico, con el auto proyectado, debe salir hoy porque hay un término. La secretaría del despacho le dice que firme usted el auto «como quien lo elaboró», que así ha pasado otras veces y que después se formaliza. El contenido del auto es exactamente el que el despacho pidió y usted no tiene dudas sobre su corrección técnica.',
  '¿Qué debe hacer?',
  ['Firmar el auto indicando expresamente que lo hace en calidad de quien lo elaboró, de modo que quede claro que la decisión de fondo sigue correspondiendo al despacho competente.',
   'No firmar el auto, remitir el proyecto por el canal institucional e informar por escrito el riesgo del término, para que el despacho disponga quién tiene competencia para suscribirlo.',
   'Firmar el auto para proteger el término y solicitar al despacho que, al regreso del jefe, se expida un acto de ratificación que convalide formalmente la suscripción que usted hizo.',
   'Remitir el auto sin firma de nadie y dejar que la secretaría del despacho resuelva el trámite, ya que la suscripción de los actos es un asunto interno que no le compete a usted.'],
  'Proyectar no es decidir: la firma es el acto por el que alguien asume la responsabilidad jurídica, y usted no tiene esa competencia, ni con aclaración ni con ratificación posterior. Lo que sí corresponde es remitir el proyecto e informar por escrito el riesgo del término.',
  'Firmar —aunque sea «como elaborador» o esperando una ratificación— es asumir una competencia ajena. Y desentenderse del trámite deja sin advertencia un término que estaba en riesgo: informarlo por escrito es parte de su responsabilidad.'),

 (2,
  'Mientras usted revisa una historia laboral en la sala de consulta, un servidor que vino a aportar documentos intenta retirarse llevándose un folio que usted había identificado como el soporte cuya autenticidad estaba verificando. Usted está acompañado por un compañero y el jefe de la División no se encuentra. El servidor se niega a devolverlo y hay tensión en el lugar. Su compañero le dice que lo retenga hasta que llegue alguien de la jefatura, «porque usted tiene funciones de criminalística».',
  '¿Cuál es la actuación correcta?',
  ['Retener a la persona hasta que llegue alguien de la jefatura, ya que el nombre del empleo y sus funciones técnicas le permiten asegurar el lugar y las personas durante el trámite.',
   'Recuperar el folio por sus propios medios y consignar en el acta la resistencia de la persona, para asegurar el soporte que el competente necesita para decidir el trámite.',
   'No retener a la persona, documentar con precisión en el acta lo ocurrido y el folio involucrado —su número, contenido y estado—, y comunicar de inmediato la situación al competente y a la autoridad que corresponda.',
   'Suspender el trámite y retirarse del lugar dejando constancia del incidente, para evitar que la tensión escale y comprometa la validez de la verificación que estaba haciendo.'],
  'El nombre del empleo no confiere ninguna facultad: el 4TC-17 es un cargo de apoyo técnico en la División de Gestión Humana, sin competencia para retener personas ni usar la fuerza. Lo que corresponde es documentar con precisión qué folio era y qué ocurrió, y comunicar de inmediato al competente y a la autoridad que proceda.',
  'Retener a una persona o recuperar el folio por la fuerza excede por completo el alcance de un empleo de apoyo técnico. Y retirarse sin documentar cuál era el folio pierde la única información que después no se recupera.'),

 (0,
  'Una persona llega a la División preguntando por el estado de un trámite de personal en el que usted verificó los soportes. Pide que usted le explique «qué encontró y qué va a pasar ahora». Es amable, parece informada del asunto y menciona detalles que coinciden con lo que usted vio. Usted no sabe si es el titular del dato ni si tiene autorización suya, y no hay nadie más en el punto de atención en ese momento. Su jefe está en una reunión y la División no tiene en ese momento a nadie más que conozca ese trámite.',
  '¿Cómo debe actuar?',
  ['Explicarle cuál es su rol y cuál es el canal para solicitar información sobre el trámite, sin describir lo verificado ni anticipar consecuencias, y dejar constancia de la solicitud.',
   'Explicarle lo que encontró sin anticipar consecuencias, ya que lo verificado son hechos objetivos y lo protegido es la decisión de fondo que adopte el servidor competente.',
   'Verificar en el sistema si la persona es la titular del dato y, si lo es, explicarle verbalmente lo verificado, que es información de su propia historia laboral y a la que tiene derecho.',
   'Remitirla directamente a la dependencia que impulsó el trámite sin registrar la solicitud, porque es esa dependencia y no la División la que debe responder sobre su estado.'],
  'Dos límites se cruzan aquí: la protección de los datos personales de la historia laboral y el alcance del rol. Ni el técnico describe lo verificado a quien se acerca, ni le corresponde anticipar consecuencias. Y la identidad del titular no se da por supuesta porque la persona «parezca informada». Se explica el rol y el canal, y se deja constancia de la solicitud recibida.',
  'Lo verificado forma parte de información personal protegida, así que describirlo no es menos grave por no anticipar consecuencias. Y aun frente al propio titular, el acceso se tramita por el canal y lo resuelve el competente, no usted en el punto de atención.'),

 (3,
  'Su jefe le asigna apoyar un caso que exige una técnica que usted no domina: la ha visto aplicar, pero nunca la ha practicado y sabe que un error de ejecución puede inutilizar el material. El término es corto, en el grupo nadie más está disponible y su jefe da por sentado que usted puede hacerlo. Admitirlo le incomoda porque llegó hace poco a la Dirección. El trámite está programada para pasado mañana, el material es único y, si se inutiliza, no existe forma de reponerlo ni de repetir la prueba.',
  '¿Cuál es la conducta esperada?',
  ['Practicar la prueba siguiendo el procedimiento documentado, y consignar en el informe que era la primera vez que aplicaba esa técnica para que el despacho valore ese factor.',
   'Practicar la prueba y pedir después a un compañero con experiencia que revise el resultado, de modo que un eventual error de ejecución pueda detectarse antes de rendir el informe.',
   'Aceptar la asignación sin observaciones, ya que cuestionar la propia capacidad ante una instrucción del jefe puede leerse como falta de disposición hacia las necesidades del grupo.',
   'Informar por escrito a su jefe que no domina la técnica y el riesgo que ello implica para el material, y pedir acompañamiento o reasignación, dejando constancia de la limitación.'],
  'Reconocer el límite de la propia competencia técnica no es falta de disposición: es lo que protege el soportes documentales, que no se recupera. Lo que corresponde es informar por escrito el riesgo y pedir acompañamiento o reasignación, dejando constancia.',
  'Practicar una técnica que no domina sobre material que puede inutilizarse es un riesgo que no se resuelve advirtiéndolo en el informe ni con una revisión posterior: el daño al material ya estaría hecho. Callar la limitación lo agrava.'),

 (1,
  'Un compañero del grupo, con más años en la entidad, le comenta que en la División «siempre» se han tramitado los encargos omitiendo un paso del procedimiento —la consulta previa de antecedentes—, «porque ese paso no aporta nada y solo alarga el trámite». Usted revisa el procedimiento vigente y confirma que el paso está previsto y no tiene excepciones. Mañana debe tramitar uno de esos encargos y el compañero trabajará con usted. El procedimiento fue adoptado hace dos años y está publicado en el repositorio interno, sin ninguna nota de suspensión ni de excepción.',
  '¿Qué debe hacer?',
  ['Seguir la práctica del grupo para no generar un conflicto con un compañero de más experiencia, y plantear después la inquietud al jefe en una conversación informal sobre el procedimiento.',
   'Aplicar el procedimiento completo, explicarlo al compañero con naturalidad, y si considera que el paso es innecesario, proponer su revisión por escrito al jefe con el sustento del caso.',
   'Aplicar el procedimiento completo y reportar por escrito a su jefe que el compañero omite ese paso, para que la División adopte las medidas que estime pertinentes frente a esa práctica.',
   'Consultar al jefe inmediato antes del trámite y aplicar lo que él indique verbalmente, aunque difiera del procedimiento escrito, porque es quien responde por el trabajo del grupo.'],
  'El parámetro formal vigente prevalece sobre la costumbre, por antigua que sea y por experimentado que sea quien la sostiene —y aquí el paso omitido es justamente el que protege a la entidad de encargar a quien tiene una inhabilidad—. Se aplica el procedimiento completo y, si hay una mejora, se propone por escrito: la iniciativa se canaliza, no se ejecuta.',
  'Seguir la costumbre incumple un procedimiento sin excepciones; una instrucción verbal no desplaza un procedimiento escrito; y convertir la inquietud en un reporte sobre el compañero desvía el asunto: lo primero es que usted cumpla el parámetro.'),

 (2,
  'Le encargan verificar tres soportes de una hoja de vida. Al consultar la carpeta, solo hay dos: el tercero —la certificación que acredita el último año de experiencia— no aparece en el índice y nadie sabe dónde está. Usted puede verificar los dos disponibles. El término vence en dos días y la dependencia solicitante insiste en recibir la constancia a tiempo. El archivo de gestión no expide certificación de la ausencia en el acto y su jefe inmediato se encuentra fuera de la ciudad hasta mañana por la tarde.',
  '¿Cuál es la actuación correcta?',
  ['Verificar los dos soportes disponibles y rendir la constancia sin aludir al tercero, para que la dependencia reciba a tiempo el resultado de lo que sí pudo examinarse.',
   'No verificar nada hasta que aparezca el tercer soporte, porque una constancia parcial podría llevar a la dependencia a conclusiones incompletas sobre el conjunto de la hoja de vida.',
   'Verificar los dos disponibles, dejar constancia escrita de la ausencia del tercero y de qué requisito queda sin acreditar por esa ausencia, e informarlo de inmediato al competente.',
   'Verificar los dos y pedir al archivo que certifique por escrito la ausencia del tercero, para anexar esa certificación a la constancia en lugar de dejar un registro propio.'],
  'Se hace lo que sí es posible hacer, se documenta con precisión lo que no fue posible y se informa de inmediato: así la constancia cumple el término y, al mismo tiempo, deja ver con exactitud qué requisito queda acreditado y cuál no. Eso es decisivo, porque sin ese soporte el competente no puede dar por cumplida la experiencia.',
  'Omitir la ausencia del tercer soporte presenta el resultado como más completo de lo que es; paralizar la verificación incumple el término sin necesidad; y esperar una certificación ajena no reemplaza su propia constancia ni el aviso inmediato al competente.'),

 (0,
  'Usted detecta que el informe técnico de un compañero, ya remitido, contiene una afirmación que excede lo que la técnica aplicada permite concluir: afirma una causa cuando el procedimiento solo permitía describir un estado. El compañero es amigo suyo, el caso sigue en instrucción y el despacho aún no ha decidido. Nadie más lo ha advertido y señalarlo podría generar tensión en el grupo. El informe del compañero ya fue remitido por el canal oficial y usted conoce el material porque participó como apoyo en la mismo trámite.',
  '¿Qué corresponde hacer?',
  ['Poner la observación técnica en conocimiento del superior por escrito, de manera objetiva y referida a la afirmación concreta, para que quien es competente valore su incidencia en el caso.',
   'Comentarlo primero con el compañero para que sea él quien lo corrija, y solo informarlo al superior si no lo hace en un plazo razonable antes de que el despacho adopte su decisión.',
   'No intervenir, porque el informe es responsabilidad de quien lo suscribió y una observación suya sobre el trabajo ajeno excedería el alcance de su propio rol dentro del grupo.',
   'Elaborar un informe propio sobre el mismo material, con la descripción correcta, y remitirlo al despacho para que disponga de los dos documentos al momento de decidir el caso.'],
  'Una afirmación que excede lo que la técnica permite concluir puede sostener una decisión equivocada: se informa por escrito, de modo objetivo y referido al punto concreto, y decide quien es competente. La amistad no es un criterio.',
  'Dar primero la oportunidad al compañero deja corriendo el riesgo mientras el despacho puede decidir; callar protege la relación a costa del caso; y elaborar un informe propio sobre material que no le fue delegado excede su rol.'),

 (3,
  'La dependencia solicitante le pide que, además de la verificación encargada, «de una vez» recomiende en la constancia qué medidas debería adoptar para que sus hojas de vida no vuelvan a llegar incompletas. Usted tiene criterio técnico para hacerlo y la recomendación sería útil. Pero su tarea se refiere a verificar unos soportes y el formato de la constancia no contempla un apartado de recomendaciones. La solicitud le llegó por correo y la constancia debe rendirse pasado mañana, dentro del término que la propia dependencia fijó.',
  '¿Cómo debe proceder?',
  ['Incluir las recomendaciones en la constancia, porque provienen de su criterio técnico y fueron expresamente solicitadas por la dependencia que pidió el trámite a la División.',
   'No incluirlas y no mencionar el tema, porque el objeto de su tarea es verificar los soportes y cualquier añadido alteraría el formato institucional de la constancia.',
   'Incluirlas en la constancia en un apartado creado para ello, advirtiendo que son recomendaciones técnicas y no conclusiones derivadas de la verificación que le fue encargada.',
   'Rendir la constancia conforme al formato y al objeto encargado, y presentar las recomendaciones por el canal institucional como documento separado, dejando registro de la solicitud.'],
  'Hay dos parámetros en juego: el objeto de la tarea y el formato de la constancia. Ninguno impide atender una solicitud legítima: se rinde la constancia como corresponde y las recomendaciones se presentan por separado, con registro de que fueron pedidas.',
  'Meter las recomendaciones dentro de la constancia —incluso en un apartado nuevo— altera el formato y mezcla lo encargado con lo que no lo está. Pero ignorar la solicitud desaprovecha un aporte técnico que tenía una vía institucional clara.'),

 (1,
  'Lleva ocho meses en el cargo y le ofrecen participar en un grupo de trabajo que estudiará la actualización de los protocolos técnicos de la Dirección. Implica dedicar tiempo fuera de sus apoyos asignados y usted tiene cuatro casos en curso, dos con término próximo. Su jefe le dice que la decisión es suya y que valorará su criterio para organizarse. Es su primera invitación de este tipo desde que ingresó y el grupo de trabajo se reunirá dos veces por semana durante el próximo mes.',
  '¿Cuál es la conducta que integra mejor las cinco competencias?',
  ['Declinar la invitación para no poner en riesgo los términos de sus cuatro casos, y ofrecer participar más adelante, cuando su carga de trabajo se haya reducido de manera estable.',
   'Aceptar e informar por escrito a su jefe cómo reorganizará los apoyos y qué términos podrían verse afectados, pidiendo los ajustes necesarios y dejando constancia del plan.',
   'Aceptar sin condiciones, porque la participación en la mejora de los protocolos es una muestra de responsabilidad con la organización que pesa más que la carga de trabajo propia.',
   'Consultar con los compañeros del grupo si pueden asumir sus casos con término próximo y aceptar solo si alguno acepta hacerlo, para no trasladar el problema a su jefe inmediato.'],
  'Aquí se integran las cinco: responsabilidad con la organización (aportar a la mejora), organización del trabajo (planear y advertir el impacto), gestión de la información y parámetros (dejarlo por escrito) y objetividad (evaluar la propia carga sin exagerar ni minimizar).',
  'Declinar sin más renuncia a un aporte posible; aceptar sin advertir el impacto arriesga términos ajenos a su decisión; y repartir los casos entre compañeros por acuerdo informal reasigna trabajo que no le corresponde reasignar.'),

 (2,
  'En un trámite conjunta con otra entidad, un servidor de esa entidad le pide que le entregue copia del acta que usted acaba de levantar, «para su propio expediente». No existe designación previa de comisión conjunta para ese asunto, el caso es de la PGN y usted no tiene instrucción alguna sobre entrega de documentos a terceros. El servidor insiste en que es lo habitual en este tipo de trámites. El trámite aún no ha terminado, el acta no ha sido remitida al expediente y usted es el único servidor de la PGN presente en el lugar.',
  '¿Qué corresponde hacer?',
  ['Entregar copia del acta, ya que fue levantada en un trámite en la que ese servidor estuvo presente y conoce de primera mano todo su contenido y las circunstancias del caso.',
   'Entregar copia del acta suprimiendo los datos personales que contiene, de modo que se atienda la solicitud sin comprometer la protección de la información de las personas involucradas.',
   'No entregar copia, explicar que la solicitud debe tramitarse ante el servidor competente de la PGN y dejar constancia escrita de la petición recibida durante el trámite.',
   'Consultar verbalmente al despacho solicitante y, si autoriza, entregar la copia en el acto, dejando anotación en el acta de la autorización verbal que recibió para hacerlo.'],
  'La entrega de documentos de la actuación a otra entidad no la decide el técnico, y sin designación previa de comisión conjunta no hay base para asumirla. Se explica el canal, se deja constancia y decide el competente.',
  'Entregar el acta —íntegra o depurada— es disponer de información de una actuación reservada; y una autorización verbal anotada en el acta no sustituye la decisión formal de quien es competente para resolver la solicitud.'),

 (0,
  'Después de nueve días de curso usted se da cuenta de que, en los simulacros, falla sobre todo en las preguntas donde la opción correcta consiste en «no actuar y poner en conocimiento», porque instintivamente elige la opción que resuelve el problema de inmediato. Le quedan doce días de preparación y el bloque funcional, más extenso, está por comenzar. Usted lleva un registro de los simulacros resueltos y puede ver que el patrón se repite en las tres últimas sesiones de práctica.',
  '¿Cuál es la mejor manera de corregirlo?',
  ['Identificar en cada caso, antes de mirar las opciones, qué parte del problema corresponde a su rol y qué parte al competente, y usar esa frontera como primer filtro de descarte.',
   'Memorizar que, ante la duda, la opción correcta es siempre la que consiste en consultar al superior, ya que el nivel Técnico implica apoyo y nunca decisión autónoma sobre un caso.',
   'Dedicar los doce días restantes a repetir simulacros comportamentales hasta que el patrón se automatice, y abordar el bloque funcional solo con los resúmenes de cada guía.',
   'Concentrarse en el bloque funcional, que pesa más en la prueba, y confiar en que el criterio comportamental se afinará por sí solo con la práctica de los casos funcionales.'],
  'El error no es de memoria sino de encuadre: casi todos estos casos se resuelven preguntándose primero qué parte es suya y qué parte es del competente. Convertir esa frontera en el primer filtro es lo que hace que la opción correcta salte a la vista.',
  'Una regla automática del tipo «siempre consultar» falla cuando el caso sí está dentro de su autonomía técnica; y ni abandonar el bloque funcional ni confiar en que el criterio se afine solo son estrategias razonables a doce días de la prueba.'),

 (3,
  'Un familiar le pregunta en qué trabaja exactamente y, al explicarle, le dice: «entonces tú investigas y determinas quién es el culpable». Usted advierte que esa idea es la que tiene mucha gente, incluida alguna persona que lo ha tratado en el punto de atención, y se da cuenta de que explicar mal su rol genera expectativas que después no puede cumplir. La persona del punto de atención se había molestado justamente porque esperaba de usted una respuesta sobre el resultado del caso.',
  '¿Cuál es la forma correcta de explicar el alcance de su cargo?',
  ['Que su cargo investiga los hechos y determina técnicamente la responsabilidad, que luego el despacho formaliza en una decisión escrita conforme al procedimiento disciplinario aplicable.',
   'Que su cargo practica verificaciones técnicas y, cuando los hallazgos son claros, concluye en el informe quién incurrió en la falta para que el despacho confirme esa conclusión y la firme.',
   'Que es un cargo de apoyo sin margen de decisión propio, cuya función consiste en ejecutar las instrucciones que el despacho competente imparta en cada caso que le sea asignado.',
   'Que practica verificaciones técnicas por delegación y documenta hechos, metodología y resultados, y que la calificación de la falta y la decisión corresponden al servidor competente.'],
  'La explicación correcta contiene las tres piezas: practica verificaciones técnicas por delegación, documenta hechos, metodología y resultados, y no califica ni decide. Saber explicarlo evita expectativas que usted no puede satisfacer.',
  'Determinar responsabilidad o concluir quién incurrió en la falta describe un rol que no es el suyo; y presentarse como un ejecutor sin margen propio desconoce la autonomía técnica real que el nivel C de parámetros precisamente exige.'),
]
