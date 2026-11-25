# -*- coding: utf-8 -*-
"""Día 7 · Gestión de la Información (B) y Cumplimiento de Parámetros de Trabajo (C) — 4TC-17."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='4TC17B-COM-02',
    archivo='4TC17B-COM-02-gestion-informacion-cumplimiento-parametros.html',
    dia=7,
    titulo_doc='Gestión de la Información y Cumplimiento de Parámetros de Trabajo',
    h1='Gestión de la Información<br>y Cumplimiento de Parámetros de Trabajo',
    kicker='Día 7 · Competencias comportamentales',
    sub='Las dos competencias <strong>por perfil</strong> que el formato de convocatoria exige al <strong>Técnico en Criminalística 4TC-17</strong> de la División de Gestión Humana: <strong>Gestión de la Información</strong> en <strong>Nivel B</strong> (registrar con exactitud, custodiar con reserva y usar la información institucional con veracidad) y <strong>Cumplimiento de Parámetros de Trabajo</strong> en <strong>Nivel C</strong>, un peldaño más exigente (aplicar con criterio las normas, formatos y protocolos que rigen la práctica de verificaciones técnicas, incluso cuando el caso no es perfectamente estándar). Son las dos competencias que más se cruzan en el trabajo de quien recolecta y documenta soportes documentales.',
    badges=['⏱ 95-115 min', '🧭 Niveles B y C', '🧠 Comportamental'],
    fmeta='Gestión de la Información (Nivel B) y Cumplimiento de Parámetros de Trabajo (Nivel C)',
    cargo='Técnico en Criminalística 4TC-17 (Nivel Técnico)',
    conv='285-2026',
    alerta='Gestión de la Información y Cumplimiento de Parámetros de Trabajo',
)

FUENTE = 'guias/4SP13-COM-02-gestion-informacion-cumplimiento-parametros.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- bloques nuevos
NARR = (
    '<p>Imagina un mismo día en la <strong>División de Gestión Humana</strong>: '
    'debes cargar en el sistema el acta de un trámite en curso practicada ayer, mantener exacto el '
    'registro de los elementos materiales de prueba que recibiste y entregaste, redactar el informe '
    'técnico en el formato institucional vigente, y atender a un abogado que pide consultar el '
    'expediente disciplinario sin ser sujeto procesal. Ninguna de esas tareas es "difícil" por '
    'separado, pero todas descansan en la misma base: <strong>manejar la información con exactitud y '
    'reserva</strong> y <strong>cumplir los parámetros de trabajo establecidos</strong>, incluso cuando '
    'nadie te está observando en el momento exacto en que decides cómo actuar.</p>\n'
    '    <p>Hoy vas a dominar las dos competencias <strong>por perfil</strong> de tu empleo: '
    '<mark>Gestión de la Información</mark> (nivel B) y <mark>Cumplimiento de Parámetros de Trabajo</mark> '
    '(nivel C, un grado más exigente). La primera mide cómo registras, custodias y usas con veracidad la '
    'información institucional; la segunda, qué tan bien te ciñes a las normas, formatos y protocolos que '
    'rigen la práctica de verificaciones técnicas, incluso cuando podrías "resolver más rápido" saltándotelos. '
    'Para un cargo que produce <strong>soportes documentales</strong>, estas dos competencias no son un '
    'adorno del perfil: son la condición de que tu trabajo sirva.</p>'
)

IMPORTANCIA = (
    '<p>Gran parte de tu jornada como <strong>Técnico en Criminalística</strong> consiste, literalmente, en '
    '<mark>producir y manejar información</mark>: recibir y documentar solicitudes de apoyo técnico, '
    'registrar lo que encuentras, dejar acta de cada trámite, consignar la metodología aplicada, '
    'elaborar el informe técnico y presentar las pruebas practicadas con sus anexos. Y todo eso ocurre '
    'dentro de parámetros establecidos —formatos institucionales, protocolos de la División de Gestión Humana, registros de '
    'custodia, plazos internos, tablas de retención documental— que existen precisamente para que esa '
    'información sea <strong>confiable, trazable y utilizable como prueba</strong>. Por eso estas dos '
    'competencias, aunque distintas, suelen evaluarse juntas: una situación que pone a prueba el manejo '
    'de información casi siempre involucra también el cumplimiento de un parámetro de trabajo específico.</p>'
)

MOD1_INTRO = (
    '<p>En la guía anterior estudiaste las dos competencias <strong>transversales</strong> de cualquier '
    'empleo público, ambas en nivel B. Hoy avanzas a las dos competencias <strong>por perfil</strong> '
    'que el formato de convocatoria asigna al <strong>Técnico en Criminalística 4TC-17</strong>, y que no '
    'tienen la misma exigencia: <strong>Gestión de la Información</strong> en <mark>nivel B</mark> '
    '(igual exigencia que las transversales) y <strong>Cumplimiento de Parámetros de Trabajo</strong> en '
    '<mark>nivel C</mark>, un peldaño más exigente. Que una de las dos esté un grado más arriba no es un '
    'detalle: te dice que la entidad espera de ti un apego a los procedimientos <em>con criterio propio</em>, '
    'no una simple obediencia mecánica, porque de los procedimientos que aplicas depende la validez de '
    'la prueba que recolectas.</p>'
)

MOD_INFO_PROPIA = (
    '<h4>La información que tú produces: acta, registro de custodia e informe técnico</h4>\n'
    '      <p>Hay una diferencia importante entre tu cargo y un empleo que solo <em>tramita</em> '
    'información ajena: una parte sustancial de la información que manejas <strong>la produces tú</strong>. '
    'Cuando practicas una verificación técnica por delegación, lo que queda en el expediente es el acta que '
    'levantas, el registro de los elementos que recibiste y entregaste, la descripción de la metodología '
    'que aplicaste y el informe técnico que elaboras. Si ese conjunto es exacto, completo y verificable, '
    'la prueba sirve; si tiene vacíos, contradicciones o datos que nadie puede reconstruir, la prueba se '
    'debilita, y con ella toda la actuación.</p>\n'
    '      <p>De ahí tres exigencias concretas que la prueba de la convocatoria evalúa una y otra vez:</p>\n'
    '      <ul class="lista">\n'
    '        <li><strong>Exactitud en el registro.</strong> Fechas, horas, cantidades, identificación de '
    'elementos, nombres y cargos de quienes intervienen, condiciones en que se encontró cada cosa. No se '
    '"redondea" un dato ni se escribe de memoria lo que no se anotó en el momento.</li>\n'
    '        <li><strong>Trazabilidad de la custodia.</strong> Todo elemento tiene un recorrido '
    'documentado: quién lo recibió, cuándo, de quién, en qué estado, a quién se entregó. Un eslabón sin '
    'registro no se "completa después de memoria": se deja constancia de la inconsistencia y se informa.</li>\n'
    '        <li><strong>Separación entre hecho y conclusión.</strong> Tu informe describe qué se hizo, '
    'cómo se hizo y qué resultó. <strong>No califica la falta, no atribuye responsabilidad y no decide de '
    'fondo</strong>: eso corresponde al servidor competente. Escribir "el servidor incurrió en la falta" '
    'en lugar de "la muestra presenta las siguientes características" no es un estilo distinto: es '
    'exceder el rol.</li>\n'
    '      </ul>\n'
    '      <div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>'
    '<p>Una opción puede ser técnicamente impecable y aun así ser incorrecta porque <strong>concluye</strong> '
    'lo que no te corresponde concluir. Cuando dos opciones describen bien el procedimiento, suele ganar '
    'la que se queda en la descripción del hallazgo y <em>pone el hallazgo en conocimiento del '
    'competente</em>, frente a la que lo califica jurídicamente.</p></div>'
)

MOD_RESERVA_CGD = (
    '<h4>La reserva de la actuación disciplinaria (art. 115 del CGD)</h4>\n'
    '      <p>Para tu cargo la reserva no es un principio abstracto: tiene una norma con nombre propio. '
    'El <strong>artículo 115 de la Ley 1952 de 2019</strong> (Código General Disciplinario) dispone que '
    '<em>en el procedimiento disciplinario las actuaciones serán reservadas hasta cuando se cite a '
    'audiencia y se formule pliego de cargos o se emita la providencia que ordene el archivo definitivo, '
    'sin perjuicio de los derechos de los sujetos procesales</em>, y añade que el disciplinado está '
    'obligado a guardar la reserva de las pruebas que por disposición de la Constitución o la ley tengan '
    'esa condición.</p>\n'
    '      <p>Tres consecuencias prácticas, y las tres aparecen en preguntas de juicio situacional:</p>\n'
    '      <div class="tabla-wrap"><table>\n'
    '        <tr><th>Situación</th><th>Lo que la norma permite</th><th>Lo que no</th></tr>\n'
    '        <tr><td>Lo pide un <strong>sujeto procesal</strong> (o su apoderado reconocido)</td>'
    '<td>La reserva no se opone a sus derechos: se verifica la calidad y se atiende por el canal y el '
    'procedimiento establecidos.</td><td>Negarle el acceso "porque hay reserva", sin verificar su '
    'calidad procesal.</td></tr>\n'
    '        <tr><td>Lo pide un <strong>tercero</strong> (abogado no reconocido, periodista, conocido)</td>'
    '<td>Orientarlo sobre el canal formal para elevar su solicitud y sobre quién decide.</td>'
    '<td>Entregar o describir el contenido, aunque la petición parezca razonable o urgente.</td></tr>\n'
    '        <tr><td>Ya se formuló <strong>pliego de cargos</strong> o se archivó definitivamente</td>'
    '<td>Cesa la reserva de la actuación, con los límites de los datos personales y de las pruebas '
    'legalmente reservadas.</td><td>Asumir que "ya no hay reserva de nada": los datos personales y las '
    'pruebas reservadas siguen protegidos.</td></tr>\n'
    '      </table></div>\n'
    '      <p>Y un parámetro que casi nadie estudia, pero que es específico de tu cargo: el '
    '<strong>artículo 63 del Decreto Ley 262 de 2000</strong> fija las funciones de la División de '
    'Gestión Humana y, con ellas, el perímetro exacto de lo que tu dependencia puede hacer. Allí está, '
    'por ejemplo, que la División <em>concede</em> los permisos de estudio que <strong>no superen dos '
    'horas diarias</strong> (núm. 6), mientras que los de más de dos horas, las vacaciones, las licencias '
    'y las comisiones de servicio los reconoce la <strong>Secretaría General</strong> (art. 62, núm. 6). '
    'Dos horas: ahí está la frontera. Confundirla es tramitar ante quien no tiene competencia y devolver '
    'el expediente al punto de partida. Lo trabajaremos a fondo en los días de talento humano; de momento '
    'retén la idea, porque es una distinción que separa a quien estudió el tema de quien lo supuso.</p>'
)

MOD5_INTRO = (
    '<p>Veamos con más detalle los tipos de parámetros de trabajo que enmarcan el día a día de un '
    '<strong>Técnico en Criminalística</strong> de la División de Gestión Humana. Observa que no son solo formatos: son los '
    'instrumentos que hacen que lo que tú haces pueda ser verificado por otro.</p>\n'
    '      <div class="tabla-wrap"><table>\n'
    '        <tr><th>Tipo de parámetro</th><th>Qué regula</th><th>Ejemplo en tu trabajo</th></tr>\n'
    '        <tr><td>Metodología acordada con la dependencia solicitante</td><td>Cómo se adelanta el '
    'apoyo técnico pedido: qué se busca, con qué técnica, en qué orden.</td><td>Fijar con el despacho '
    'qué verificaciones técnicas se practicarán y con qué alcance antes de iniciar.</td></tr>\n'
    '        <tr><td>Formatos institucionales</td><td>La estructura del acta, el informe técnico, el '
    'oficio remisorio y los anexos.</td><td>Membrete, numeración, identificación de la solicitud que '
    'origina el apoyo, pie de firma, código de dependencia.</td></tr>\n'
    '        <tr><td>Registros de recepción y entrega de elementos</td><td>La trazabilidad de todo lo '
    'que se recibe, se analiza y se devuelve.</td><td>Consignar quién entrega, quién recibe, fecha, hora '
    'y estado de cada elemento.</td></tr>\n'
    '        <tr><td>Tablas de Retención Documental (TRD)</td><td>En qué serie y por cuánto tiempo se '
    'archiva cada tipo de documento.</td><td>Ubicar un informe técnico en la serie documental correcta, '
    'no en la carpeta que resulte más cómoda.</td></tr>\n'
    '        <tr><td>Protocolos internos de reporte</td><td>Cómo y a quién se informan novedades y '
    'resultados.</td><td>Reportar el avance de los apoyos asignados y los trámites con término '
    'próximo.</td></tr>\n'
    '      </table></div>'
)

R = [
    # --- sección 0: caso que acompaña
    ('<p>Imagina que en un mismo día debes: cargar en el sistema de gestión documental un acto notificado, mantener actualizado el consecutivo de radicación, custodiar un expediente disciplinario que un abogado externo pide consultar sin ser parte del proceso, y cumplir al pie de la letra un formato que tu despacho exige para todos los oficios. Ninguna de estas tareas es "difícil" por separado, pero todas exigen la misma base: manejar la información con criterio y cumplir los parámetros de trabajo establecidos, incluso cuando nadie te está observando en el momento exacto en que decides cómo actuar.</p>',
     NARR),
    ('<p>Hoy vas a dominar dos competencias específicas de tu cargo: <mark>Gestión de la Información</mark> (nivel B) y <mark>Cumplimiento de Parámetros de Trabajo</mark> (nivel C, un grado más exigente). La primera mide cómo procesas, custodias y usas con veracidad la información institucional; la segunda mide qué tan bien te ciñes a las normas, formatos y disposiciones que rigen tu trabajo, incluso cuando podrías "resolver más rápido" saltándotelos.</p>',
     ''),
    # --- sección 1: importancia
    ('<p>Gran parte de tu jornada como Secretario Procuraduría consiste, literalmente, en <mark>manejar información</mark>: recibir, radicar, registrar, custodiar, expedir copias, actualizar sistemas. Y todo eso ocurre dentro de <mark>parámetros establecidos</mark> —formatos, plazos internos, protocolos de archivo— que existen precisamente para que ese manejo de información sea confiable y verificable. Por eso estas dos competencias, aunque distintas, suelen evaluarse juntas: una situación que pone a prueba el manejo de información casi siempre involucra también el cumplimiento de un parámetro de trabajo específico.</p>',
     IMPORTANCIA),
    ('<p>Manejas expedientes disciplinarios y datos personales a diario.</p>',
     '<p>Produces y custodias soportes documentales, actas y datos personales a diario.</p>'),
    ('<p>Nivel C: mayor exigencia de apego a normas y formatos que en nivel Asistencial.</p>',
     '<p>Nivel C: se espera criterio propio dentro del marco, no obediencia mecánica.</p>'),
    ('<p>De esto depende la validez y la reserva de todo lo que tramitas.</p>',
     '<p>De esto depende la validez y la reserva de la prueba que recolectas.</p>'),
    # --- sección 2: módulo 1
    ('<p>En la guía anterior estudiaste las dos competencias transversales de cualquier empleo público. Hoy avanzas a dos competencias más específicas del perfil del Secretario Procuraduría, que exigen un grado de exigencia distinto según el Diccionario de Competencias: <strong>Gestión de la Información</strong> en nivel B (igual exigencia que las transversales) y <strong>Cumplimiento de Parámetros de Trabajo</strong> en nivel C, un peldaño más exigente.</p>',
     MOD1_INTRO),
    # --- sección 2: módulo 5 (parámetros)
    ('<h3>Parámetros de trabajo en la práctica secretarial cotidiana</h3>',
     '<h3>Parámetros de trabajo en la práctica diaria de la División de Gestión Humana</h3>'),
    ('<p>Veamos con más detalle los tipos de parámetros de trabajo que enmarcan el día a día de un Secretario de despacho en la PGN.</p>\n      <div class="tabla-wrap"><table>\n        <tr><th>Tipo de parámetro</th><th>Qué regula</th><th>Ejemplo</th></tr>\n        <tr><td>Formatos institucionales</td><td>La estructura de oficios, autos, constancias y demás documentos.</td><td>Membrete, numeración, pie de firma, código de dependencia.</td></tr>\n        <tr><td>Protocolos de notificación</td><td>Cómo se notifica cada tipo de actuación según la norma.</td><td>Notificación personal vs. por aviso vs. por estado.</td></tr>\n        <tr><td>Tablas de Retención Documental (TRD)</td><td>Cuánto tiempo y en qué serie se archiva cada tipo de documento.</td><td>Ubicar un oficio en la serie documental correcta del despacho.</td></tr>\n        <tr><td>Protocolos internos de reporte</td><td>Cómo y a quién se informan novedades del trabajo diario.</td><td>Reportar diariamente el estado de expedientes con términos próximos.</td></tr>\n      </table></div>',
     MOD5_INTRO),
    # --- sección 2: bloques nuevos (antes de cierres de módulo existentes)
    ('<h4>Un último matiz: la diferencia entre "no saber" y "no haber verificado"</h4>',
     MOD_INFO_PROPIA + '\n      <h4>Un último matiz: la diferencia entre "no saber" y "no haber verificado"</h4>'),
    ('<h4>Un ejercicio mental para fijar las tres capas de reserva</h4>',
     MOD_RESERVA_CGD + '\n      <h4>Un ejercicio mental para fijar las tres capas de reserva</h4>'),
    # --- fuentes
    ('<li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=88704" target="_blank" rel="noopener">Decreto 815 de 2018 — Competencias comportamentales del empleo público</a></li>',
     '<li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=88704" target="_blank" rel="noopener">Decreto 815 de 2018 — Competencias comportamentales del empleo público</a></li>\n'
     '      <li><a href="https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1952_2019_pr003.htm" target="_blank" rel="noopener">Ley 1952 de 2019, arts. 115 y 116 — Reserva de la actuación disciplinaria y requisitos formales</a></li>\n'
     '      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=186" target="_blank" rel="noopener">Ley 594 de 2000 — Ley General de Archivos</a></li>'),
    # --- sección 5: errores
    ('<p>Compromete la trazabilidad y la seguridad de la información institucional.</p>',
     '<p>Compromete la trazabilidad: lo que se registre con tu usuario se te imputa a ti.</p>'),
    ('<p>Compromete gravemente la veracidad, incluso si la motivación parece menor.</p>',
     '<p>Compromete gravemente la veracidad y, con ella, el valor probatorio de todo el informe.</p>'),
]
SEC = aplicar_todas(SEC, R, estricto=True)
SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>',
     '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('4SP-13', '4TC-17'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol('Técnico en Criminalística', 'Técnicos en Criminalística'), estricto=False)   # filtro antifugas final

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre Gestión de la '
              'Información (Nivel B) y Cumplimiento de Parámetros de Trabajo (Nivel C) en el trabajo real de un '
              'Técnico en Criminalística de la División de Gestión Humana. Los contextos son extensos y las cuatro opciones son plausibles. '
              'Al seleccionar una opción verás si acertaste y la explicación.')

P = [
 (1,
  'Usted es Técnico en Criminalística 4TC-17 de la División de Gestión Humana y ayer terminó de verificar los soportes de la historia laboral de una servidora: entre ellos hay incapacidades médicas y la hoja de vida completa. Un abogado se presenta en la División, se identifica, dice que representa «los intereses de la familia» de la servidora y pide consultar la historia laboral. No exhibe poder ni autorización de la titular. Insiste en que la petición es urgente porque «hay términos corriendo» y le pide que al menos le cuente verbalmente qué contiene la carpeta.',
  '¿Cuál es la actuación correcta?',
  ['Permitirle consultar únicamente los documentos que usted mismo elaboró, como la lista de verificación de requisitos, y no el resto de la carpeta, que sí contiene datos personales protegidos.',
   'No darle acceso ni describirle el contenido, orientarlo sobre el canal formal para elevar su solicitud ante el servidor competente, y dejar constancia de la solicitud recibida.',
   'Atender la solicitud verbalmente sin entregar documentos, porque describir el contenido no constituye entrega de información protegida y evita una queja por mala atención.',
   'Entregarle copia de los soportes que no sean médicos, ya que la reserva solo cubre los datos sensibles de salud y los demás documentos de la historia laboral son información pública.'],
  'La historia laboral contiene datos personales y, en el caso de las incapacidades, <strong>datos sensibles de salud</strong>: su tratamiento exige autorización del titular (Ley 1581 de 2012) y el acceso de terceros está limitado (Ley 1712 de 2014, art. 18). Quien pide no acredita poder ni autorización. Lo correcto es no entregar ni describir, orientar sobre el canal formal y dejar constancia.',
  'La protección cubre la carpeta completa, incluidos los documentos que usted elaboró, y no se levanta por una descripción verbal ni por lo urgente que parezca la petición. Tampoco es cierto que «lo no médico» sea público: la hoja de vida es información personal. Verificar la legitimación es el paso previo a cualquier acceso.'),

 (3,
  'Usted proyectó y radicó la constancia de verificación de requisitos que soporta un nombramiento. Dos días después, al revisar sus apuntes, advierte que escribió que la posesión se surtió el 9 de marzo cuando en realidad fue el 10 de marzo: digitó mal la fecha. El dato no cambia la conclusión sobre los requisitos, pero sí aparece en la constancia y en el oficio remisorio. Su jefe inmediato está en comisión y regresa en cuatro días. Un compañero le dice que lo deje así, «porque un día no le importa a nadie y si lo corrige va a parecer que el documento está mal hecho».',
  '¿Qué debe hacer?',
  ['Dejar el dato como está, porque el error no altera la conclusión sobre el cumplimiento de requisitos y una corrección formal podría restar credibilidad al documento ya radicado.',
   'Esperar a que su jefe regrese de la comisión y, si para entonces nadie ha advertido la inconsistencia, no hacer nada, porque la corrección ya habría perdido toda utilidad práctica.',
   'Corregir el archivo digital y volverlo a cargar al sistema con la fecha correcta, sin dejar rastro de la versión anterior, para que la historia laboral quede consistente.',
   'Informar de inmediato por escrito la inconsistencia por el canal institucional, pidiendo la corrección conforme al procedimiento, y dejar constancia del dato real y de su origen.'],
  'Un error de digitación advertido a tiempo no es una falta de veracidad: lo que define la competencia es qué hace usted al detectarlo. Informarlo por escrito y pedir la corrección por el procedimiento preserva la exactitud y la trazabilidad; sustituir el archivo en silencio destruye precisamente la trazabilidad.',
  'Callar el error o sustituir la versión sin dejar rastro convierte un fallo subsanable en un problema de veracidad y trazabilidad. La ausencia del jefe no suspende el deber: existe un canal escrito para dejar la constancia.'),

 (0,
  'Usted verifica los requisitos de una persona nombrada antes de su posesión y, al documentar el resultado, encuentra que un soporte de experiencia no acredita el tiempo exigido. El jefe de otra dependencia, que necesita a la persona trabajando ya, lo llama y le pide que en la constancia «concluya que los requisitos están cumplidos, para no perder tiempo», porque el soporte faltante «llegará esta semana». Le explica que es solo una formulación y que al final el resultado será el mismo. La constancia debe entregarse mañana.',
  '¿Cuál conducta corresponde a su rol y a las dos competencias evaluadas?',
  ['Consignar qué documentos se verificaron, qué acredita cada uno y cuál requisito no quedó acreditado, y poner el resultado en conocimiento del servidor competente.',
   'Consignar la conclusión pedida, pues quien la solicita es jefe de dependencia, conoce la necesidad real del servicio y asume ante la entidad la responsabilidad de lo que se afirme en la constancia.',
   'Consignar la conclusión en un párrafo separado del documento, advirtiendo que se trata de una apreciación propia y no de una verificación, de modo que el competente pueda usarla o descartarla.',
   'Entregar la constancia sin mencionar el soporte faltante y advertirlo verbalmente al jefe de la dependencia, para que sea él quien decida cómo dejarlo documentado en la historia laboral.'],
  'La verificación de requisitos y el concepto escrito previo a la posesión están a cargo de la División (art. 63, núm. 7, del Decreto Ley 262 de 2000), y lo que la constancia afirme debe estar respaldado por los soportes. Usted describe qué acredita cada documento; no declara cumplido lo que no está acreditado. Que la petición venga de un jefe de dependencia no amplía su rol.',
  'Afirmar un cumplimiento que los soportes no respaldan —aunque sea «en un párrafo separado» o a pedido de un jefe— falsea la constancia y expone la posesión a nulidad; omitir el faltante compromete la veracidad. Lo correcto es consignar lo verificado y poner el resultado en conocimiento del competente.'),

 (2,
  'Su grupo de trabajo usa desde hace años una plantilla propia para las actas de trámite: es cómoda, todos la conocen y ha funcionado. Hace un mes la Dirección adoptó un formato institucional nuevo, con numeración y campos obligatorios distintos, y lo comunicó por memorando. Hoy debe levantar un acta y la compañera que lo acompaña le dice que use la plantilla antigua «porque el formato nuevo es engorroso y en el grupo seguimos con la de siempre». Usted verifica que el memorando está vigente y que el formato nuevo está publicado.',
  '¿Qué debe hacer?',
  ['Usar la plantilla antigua, porque es la práctica consolidada del grupo y mantener la uniformidad interna del equipo evita inconsistencias entre las actas de una misma investigación.',
   'Usar la plantilla antigua y transcribir después la información al formato nuevo, para no retrasar el trámite y cumplir igualmente con el formato institucional al final del trámite.',
   'Usar el formato institucional vigente y, si considera que dificulta el trabajo, plantear la observación con una propuesta concreta por el canal institucional, dejando constancia.',
   'Consultar con los demás integrantes del grupo y aplicar el formato que use la mayoría, para que la decisión sea del equipo y no una postura individual frente a la costumbre.'],
  'El parámetro formalmente vigente prevalece siempre sobre la costumbre de oficina, por arraigada que esté. El nivel C no consiste en obedecer sin pensar, sino en aplicar el parámetro y canalizar la mejora como propuesta, no como excepción propia.',
  'Una costumbre del grupo no deroga un formato adoptado y comunicado, y «transcribir después» introduce un paso donde se pierden datos. La iniciativa se canaliza como propuesta; el formato vigente se aplica desde ya.'),

 (1,
  'Debe cargar al sistema de información institucional el acta y los anexos de un trámite practicada esta mañana. El sistema está caído por una falla técnica reportada a la mesa de ayuda y nadie sabe cuándo se restablecerá. El protocolo de la dependencia exige el cargue dentro de la jornada. Un compañero le propone dos salidas: dejarlo para mañana sin más, o cargarlo mañana con la fecha de hoy «para que el sistema no muestre un incumplimiento». Usted tiene el acta firmada, los anexos digitalizados y el reporte del incidente.',
  '¿Cuál es la actuación de nivel C esperada?',
  ['Cargar mañana la información con la fecha de hoy, ya que el trámite efectivamente se practicó hoy y la demora es atribuible a una falla del sistema, no a su gestión.',
   'Dejar constancia escrita de la falla y de la información lista, informarla por el canal de reporte, y cargarla en cuanto el sistema se restablezca con su fecha real de cargue.',
   'Esperar a que el sistema se restablezca y cargarla entonces sin ninguna constancia adicional, porque la falla fue reportada a la mesa de ayuda y ese reporte ya documenta el hecho.',
   'Enviar el acta y los anexos por correo personal a su jefe inmediato para que quede evidencia del cumplimiento del plazo, y cargarla al sistema cuando el servicio se recupere.'],
  'Una contingencia técnica no autoriza a consignar una fecha que no corresponde: eso convierte una demora justificada en un dato falso. El nivel C espera que documente la contingencia, la reporte por el canal y cumpla en cuanto sea posible, con fechas reales.',
  'Anteponer la fecha «conveniente» afecta la veracidad del registro; callar la contingencia deja el incumplimiento sin explicación; y un correo personal no es el canal institucional ni sustituye el registro en el sistema.'),

 (3,
  'Un jefe de otra dependencia lo llama: necesita que un servidor salga en comisión de servicios mañana y le pide que «vaya alistando el acto» mientras formaliza la solicitud. No existe aún solicitud escrita del jefe inmediato, no se ha verificado la disponibilidad presupuestal de los viáticos y no hay decisión del competente —que en comisiones de servicio es la Secretaría General, conforme al art. 62, núm. 6, del Decreto Ley 262 de 2000—. El jefe insiste en que la urgencia es real, que ya han tramitado otras comisiones juntos y que la formalización llegará «en el transcurso del día».',
  '¿Cuál es la actuación correcta?',
  ['Proyectar el acto y darlo por autorizado para mañana, y pedir que la solicitud escrita y el soporte presupuestal se incorporen al expediente cuando estén listos.',
   'Negarse a cualquier gestión y no responder más llamadas sobre el asunto, porque sin solicitud escrita previa la División de Gestión Humana no tiene ninguna actuación posible frente a esa dependencia.',
   'Tramitar la comisión bajo la responsabilidad del jefe que la solicita, dejando constancia en el expediente de que la solicitud escrita estaba pendiente al momento de actuar.',
   'Orientar sobre cómo radicar la solicitud, informar a su jefe de la urgencia planteada y adelantar solo lo que no supone decisión —revisar qué soportes se necesitan y tener el proyecto listo—, dejando constancia.'],
  'La solicitud escrita, el soporte presupuestal y la decisión del competente no son trámites decorativos: son los parámetros que habilitan el acto y le dan validez. Se puede colaborar con la urgencia dentro del marco —orientar, informar al jefe, tener el proyecto listo— y dejar constancia.',
  'Dar por autorizada una comisión sin solicitud ni decisión del competente compromete la validez del acto y el pago de los viáticos, aunque la urgencia sea real; pero tampoco corresponde cerrar la puerta: la conducta esperada es encauzar la urgencia por el procedimiento e informar al jefe.'),

 (0,
  'Verificando los soportes de una historia laboral para un encargo, usted advierte que un certificado de estudios presenta señales de alteración —lo que, además de afectar los requisitos, podría ser constitutivo de delito— y que la persona ha recibido durante meses una prima que su situación no parece permitir, lo que apunta a un pago de lo no debido. El objeto de su tarea no cubre ninguno de los dos: se limita a verificar los requisitos del encargo. Un compañero le sugiere ampliar por su cuenta el alcance de la revisión «ya que está ahí» y otro, dejarlo por fuera de la constancia «porque no se lo pidieron».',
  '¿Qué corresponde hacer?',
  ['Documentar los hechos tal como los observó, dentro de la constancia y sin calificarlos jurídicamente, y ponerlos en conocimiento del servidor competente para que decida y compulse si procede.',
   'Ampliar por su cuenta el alcance de la revisión para precisar los dos hallazgos, de modo que la constancia llegue al competente con el soporte completo y no se pierda información valiosa.',
   'Omitirlos de la constancia y comentarlos verbalmente al jefe, para no exceder el objeto de su tarea ni dejar en la historia laboral información ajena a lo pedido.',
   'Remitir directamente los hallazgos a la Fiscalía y a la Contraloría, que son las autoridades competentes en materia penal y fiscal, e informar luego de ello a su jefe inmediato.'],
  'El hallazgo se documenta como hecho observado y se pone en conocimiento del competente: ampliar el alcance y compulsar copias a la Fiscalía o a la Contraloría no están en manos del técnico. Describir sin calificar y no omitir es la conducta esperada.',
  'Ampliar el alcance por iniciativa propia excede su tarea; omitir el hallazgo compromete la veracidad de la constancia; y compulsar directamente a otras autoridades es una decisión del servidor competente, no del técnico que verifica.'),

 (2,
  'Su usuario del sistema de información tiene permisos para cargar actas e informes. Un compañero del grupo, que hoy debe cargar un informe con término que vence, se quedó sin acceso porque su contraseña expiró y la mesa de ayuda demora en restablecerla. Le pide prestada su clave «solo para esa carga», y le recuerda que ya lo han hecho antes sin consecuencias. Usted sabe que el registro quedará asociado a su usuario y que el informe que se cargará no es de su autoría.',
  '¿Cuál es la actuación correcta?',
  ['Prestarle la clave para esa única carga y cambiarla inmediatamente después, de modo que el término se cumpla y el acceso extraordinario quede cerrado el mismo día.',
   'Cargar usted mismo el informe de su compañero con su propio usuario, ya que así la clave no se comparte y el término se cumple sin afectar la seguridad de su cuenta.',
   'No compartir la clave ni cargar documentos ajenos como propios, apoyar la gestión del restablecimiento ante la mesa de ayuda e informar al superior el riesgo de incumplimiento del término.',
   'Pedirle que le envíe el informe por correo y cargarlo con su usuario indicando en el campo de observaciones que el documento fue elaborado por el compañero y no por usted.'],
  'La clave es personal e intransferible y el registro se imputa a quien aparece en él: compartirla o cargar como propio un documento ajeno rompe la trazabilidad, que es el núcleo de la Gestión de la Información. Lo correcto es resolver el acceso por el canal e informar el riesgo del término.',
  'Cambiar la clave después no borra que un tercero actuó con su usuario, y cargar el informe ajeno —incluso aclarándolo en observaciones— deja el registro a su nombre. El término se protege informando el riesgo, no rompiendo la trazabilidad.'),

 (1,
  'Debe archivar la constancia de verificación y los soportes de un encargo ya surtido. Al consultar la Tabla de Retención Documental de la dependencia, encuentra que la serie que describe con más precisión este tipo de documento no aparece de forma literal: hay dos series parecidas —historias laborales y actos administrativos de personal— y ninguna coincide exactamente con el caso. El término para dejar el archivo organizado vence el viernes y la persona encargada de archivo está incapacitada.',
  '¿Cuál es la conducta de nivel C?',
  ['Archivar en la serie que más se parezca y anotar en la carpeta una nota explicando la duda, de modo que quien revise después pueda reclasificar el documento si lo considera necesario.',
   'Consultar por el canal institucional al responsable de gestión documental o a quien lo supla, dejar constancia escrita de la consulta y archivar conforme a la orientación recibida.',
   'Crear una carpeta nueva con el nombre del servidor y custodiarla aparte hasta que la encargada de archivo regrese, para no clasificar erróneamente un documento con valor probatorio.',
   'Archivar en la serie de mayor tiempo de retención, porque conservar más tiempo un documento nunca causa un perjuicio y evita el riesgo de una eliminación anticipada.'],
  'La TRD exige criterio, no adivinanza: ante un caso que no encaja, la conducta de nivel C es consultar por el canal, dejar constancia de la consulta y actuar conforme a la orientación. La constancia de la consulta es parte del propio cumplimiento del parámetro.',
  'Elegir «la más parecida», inventar una carpeta propia o escoger la serie de mayor retención son decisiones unilaterales sobre un instrumento que no le corresponde modificar. La incapacidad de la encargada no elimina el canal: hay quien la supla.'),

 (3,
  'Un conocido suyo le escribe por mensajería instantánea: se enteró de que usted trabaja en la División de Gestión Humana y que su hermano, servidor de la entidad, pidió un traslado. Le pide, «entre nosotros», que le confirme solo si el traslado ya se tramitó y, si es posible, qué dice el concepto de la División. Aclara que no quiere documentos ni copias, solo saber «cómo va la cosa» para tranquilizar a la familia, y le promete que no le dirá a nadie que la información salió de usted.',
  '¿Cuál es la actuación correcta?',
  ['Confirmarle únicamente si el trámite ya se surtió, sin mencionar el contenido del concepto, porque el hecho de que exista una solicitud no constituye por sí mismo información protegida.',
   'Responderle que no puede dar información por ese canal, pero ofrecerle una conversación personal donde pueda orientarlo con más detalle sobre la situación administrativa de su hermano.',
   'Verificar primero si el hermano autorizó a su familia y, en caso afirmativo, darle la información, ya que el titular del dato puede permitir que un tercero conozca su trámite.',
   'No suministrar ninguna información por ese ni por otro canal informal, indicarle el canal formal por el cual el propio servidor puede solicitarla, y abstenerse de comentar el trámite.'],
  'La información de un trámite de personal es un dato personal de su titular y está amparada por el deber de reserva de quien la maneja por razón de sus funciones. Los canales informales no son vía para información institucional, y una autorización verbal relatada por un tercero no es autorización del titular: el acceso se tramita por el canal formal y lo decide el servidor competente, no usted por mensajería.',
  'Confirmar «solo» que el trámite existe ya revela información del servidor; cambiar de canal —una conversación personal— no cambia el fondo; y creerle a un tercero que «el titular autorizó» no sustituye la autorización del titular. El acceso se tramita formalmente.'),

 (2,
  'Al revisar una historia laboral que recibió para continuar un trámite, usted advierte que faltan dos folios referidos a la entrega de los soportes de experiencia: el registro de recibido no coincide con el índice de la carpeta y nadie en el grupo recuerda quién los recibió. El plazo para rendir su constancia vence en dos días. Un compañero le dice que reconstruya el dato «de memoria, que seguro fue así» y otro, que no mencione nada «porque fue antes de que usted llegara al trámite».',
  '¿Qué debe hacer?',
  ['Reconstruir el registro faltante con la información que los compañeros recuerden y advertirlo verbalmente al jefe, para que la carpeta quede completa antes de rendir su constancia.',
   'Rendir la constancia sin aludir a la inconsistencia, porque ocurrió antes de que usted asumiera el trámite y señalarla podría afectar injustamente a quienes intervinieron antes.',
   'Dejar constancia escrita y detallada de la inconsistencia, informarla por el canal institucional al competente y rendir su documento señalando expresamente el alcance que ese vacío impone.',
   'Suspender la elaboración de la constancia hasta que se aclare el vacío documental, porque rendirla sobre una carpeta incompleta comprometería la validez de todo lo que usted consigne.'],
  'Un eslabón sin registro no se completa de memoria ni se oculta: se documenta la inconsistencia, se informa al competente y se rinde el documento precisando qué puede y qué no puede sostenerse con ese vacío. Así se protegen a la vez la veracidad y el término.',
  'Reconstruir «de memoria» crea un dato falso; callar el vacío compromete la veracidad; y suspender el trámite por decisión propia incumple el término cuando sí era posible rendirlo delimitando su alcance.'),

 (0,
  'Dos parámetros parecen chocar. El protocolo interno de la División de Gestión Humana exige que toda constancia de verificación se remita por el sistema de gestión documental con los soportes digitalizados. El jefe que solicitó el trámite le pide, por correo, que le envíe la constancia directamente en físico «porque el sistema le abre los soportes muy pesados y los necesita para la posesión de mañana». Ambas instrucciones son razonables y provienen de servidores que tienen competencia sobre su trabajo.',
  '¿Cuál es la actuación de nivel C?',
  ['Remitir la constancia por el sistema conforme al protocolo y, además, informar al jefe esa remisión y gestionar por el canal interno la entrega física adicional que requiere para la posesión.',
   'Atender la instrucción del jefe solicitante y entregar la constancia en físico, porque es quien tiene la necesidad concreta y conoce el uso que dará al documento mañana.',
   'Cumplir el protocolo interno y no entregar nada en físico, informando al jefe que debe descargar los soportes del sistema, que es el único canal institucional previsto para la remisión.',
   'Consultar a su jefe inmediato y, si no responde antes del cierre de la jornada, elegir la opción que menos retrase la posesión del día siguiente, dejando constancia de la consulta hecha.'],
  'Cuando dos parámetros parecen contradecirse, lo que casi siempre se espera no es elegir uno y sacrificar el otro, sino cumplir el que da validez y trazabilidad y atender la necesidad real por una vía compatible, dejando todo informado.',
  'Sustituir el canal institucional por una entrega física, negar sin más la necesidad de la otra dependencia, o dejar que el silencio del jefe decida son salidas que sacrifican un parámetro cuando ambos podían cumplirse.'),

 (1,
  'Usted detecta que la información de un caso en el que participó circuló fuera del círculo que debía conocerla: en una conversación ajena al trabajo, un tercero menciona con precisión el diagnóstico que aparece en una incapacidad médica que usted registró en una historia laboral, y que nadie fuera de la División debía conocer. No sabe quién lo divulgó ni por qué canal, y teme que señalar el hecho genere un ambiente de sospecha en el grupo, sobre todo porque uno de los compañeros con acceso a esa carpeta es amigo suyo desde antes de entrar a la entidad. Nadie más parece haberlo advertido.',
  '¿Cuál es la actuación correcta?',
  ['Averiguar discretamente dentro del grupo quién pudo haberlo divulgado y, solo si confirma al responsable, informarlo al jefe inmediato con el nombre y los datos que haya reunido.',
   'Informar el hecho por el canal institucional, con los datos concretos que conoce y sin atribuir responsabilidad a nadie, para que quien es competente adelante la verificación.',
   'Reforzar sus propias medidas de seguridad y no informar el hecho, ya que no tiene certeza de lo ocurrido y señalarlo sin pruebas podría afectar injustamente a un compañero.',
   'Comentarlo informalmente con el compañero que tiene acceso a la carpeta, para advertirle del riesgo y darle la oportunidad de corregir la situación antes de que el hecho tenga consecuencias.'],
  'Un diagnóstico médico es un <strong>dato sensible</strong> (Ley 1581 de 2012): su divulgación es un incidente de seguridad de la información. Lo que corresponde es poner el hecho en conocimiento del competente con los datos que se conocen, sin investigar por cuenta propia ni señalar a nadie. Informar no es acusar: es activar a quien sí tiene la competencia para verificar.',
  'Investigar por su cuenta, advertir al presunto responsable o callar por falta de certeza son decisiones que exceden su rol o dejan el riesgo activo, y aquí hay además un dato de salud expuesto. El canal institucional existe precisamente para que usted no tenga que decidir quién es responsable.'),

 (3,
  'Una verificación de soportes que usted debe cerrar hoy se extiende más allá del horario oficial porque la historia laboral solo estuvo disponible al final de la tarde, cuando la dependencia que la custodiaba pudo facilitarla. El protocolo de la dependencia no regula expresamente qué hacer cuando el trámite se prolonga fuera de la jornada: no lo prohíbe ni lo autoriza. Usted tiene el acta de entrega lista, firmada por quienes intervinieron, y el registro de la hora real de cierre, que es posterior al horario. Un compañero le dice que anote la hora de cierre dentro de la jornada «para no abrir un problema administrativo».',
  '¿Cuál es la actuación de nivel C?',
  ['Anotar la hora de cierre dentro del horario oficial, porque el trámite se inició en la jornada y el protocolo no exige consignar una prolongación que no está regulada.',
   'Consignar la hora real y no informar nada más, dado que el protocolo no regula el caso y, por lo tanto, no existe un deber específico de reportar la prolongación ocurrida.',
   'No cerrar el acta ese día y reanudar el trámite al día siguiente dentro del horario, para que todo quede enmarcado en la jornada oficial de trabajo, aunque la carpeta deba quedar fuera de su sitio una noche más.',
   'Consignar la hora real de cierre, documentar por escrito la razón de la prolongación y reportarla por el canal interno, dejando constancia de la situación no prevista en el protocolo.'],
  'Que el protocolo no cubra el caso no autoriza a ajustar el dato ni habilita el silencio: la conducta de nivel C es consignar lo real, documentar por qué ocurrió y reportarlo, de modo que la excepción quede registrada y no se convierta en costumbre.',
  'Ajustar la hora falsea el registro; guardar silencio deja sin explicación una actuación fuera de lo previsto; e interrumpir un trámite ya terminado para «encajarlo» en el horario deja la historia laboral fuera de su sitio y sin acta de cierre.'),

 (2,
  'Usted propone una mejora real: un campo adicional en el formato de acta que evitaría las confusiones de fechas que han aparecido en varios apoyos. La presenta por escrito al jefe inmediato, que responde que la estudiará con la Dirección y que por ahora se siga usando el formato vigente. Pasan tres semanas sin respuesta. Entre tanto, usted debe levantar dos actas más y sabe que el campo adicional las haría más claras. Un compañero le dice que lo incluya «total, es una mejora y nadie se va a oponer».',
  '¿Qué debe hacer?',
  ['Incluir el campo adicional en las dos actas, ya que la mejora fue propuesta formalmente, no fue rechazada y añadir información nunca puede perjudicar la claridad de un documento.',
   'Incluirlo solo en una de las dos actas, a modo de prueba piloto, y presentar el resultado comparado al jefe para acelerar la decisión pendiente de la Dirección sobre su propuesta.',
   'Usar el formato vigente sin modificaciones y reiterar por escrito la propuesta, pidiendo respuesta y dejando constancia de las confusiones de fechas que la justifican.',
   'Usar el formato vigente y abandonar la propuesta, dado que el silencio de tres semanas indica que la Dirección no considera necesaria la modificación planteada por usted.'],
  'La iniciativa se canaliza como propuesta, nunca como cambio no aprobado: mientras no se adopte, el formato vigente se aplica tal cual. Lo que sí corresponde es insistir por escrito y documentar el problema que la mejora resolvería.',
  'Aplicar unilateralmente la mejora —aunque sea «solo en una acta» como piloto— es modificar un parámetro que usted no adopta. Y abandonar la propuesta por el silencio desaprovecha una iniciativa legítima que debe reiterarse por el canal.'),
]
