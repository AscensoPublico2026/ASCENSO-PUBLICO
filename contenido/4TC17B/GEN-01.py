# -*- coding: utf-8 -*-
"""Día 2 · El Estado y la Función Pública — Técnico en Criminalística 4TC-17 (Conv. 285-2026).

Reutiliza el desarrollo de GEN-01-PGN-4SP13 y lo corrige y reenfoca al cargo:
 · el nivel Técnico se define como la norma lo define (labores técnicas misionales
   y de apoyo + aplicación de ciencia y tecnología), no como apoyo administrativo;
 · los ejemplos pasan de ventanilla y correspondencia a apoyo técnico de investigación.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from _lib import secciones, aplicar_todas, limpieza_rol

META = dict(
    codigo='GEN-01-PGN-4TC17B',
    archivo='GEN-01-PGN-4TC17B-estado-funcion-publica.html',
    dia=2,
    titulo_doc='El Estado y la Función Pública',
    h1='El Estado y la Función Pública',
    kicker='Día 2 · Conocimientos comunes',
    sub='Antes de estudiar lo que hace la Procuraduría conviene entender <strong>en qué Estado se trabaja</strong>. Aquí verás los fines esenciales del Estado, el Estado social de derecho, la organización del poder y el lugar de los órganos de control, la <strong>función administrativa</strong> y sus principios (art. 209), quién es <strong>servidor público</strong>, la <strong>carrera administrativa y el mérito</strong> (art. 125), los <strong>niveles jerárquicos</strong> de los empleos y dónde se ubica el nivel técnico, el ciclo de ingreso, permanencia y retiro, los deberes, prohibiciones, inhabilidades e incompatibilidades, la responsabilidad del servidor y los controles sobre la administración. Todo aplicado al <strong>Técnico en Criminalística 4TC-17</strong> de la División de Gestión Humana de la PGN, <strong>Convocatoria 285-2026</strong>.',
    badges=['⏱ 95-115 min', '🏛️ Régimen PGN', '📘 Conocimientos comunes'],
    fmeta='El Estado y la Función Pública (Constitución, Ley 489 de 1998 y régimen del servidor público)',
    cargo='Técnico en Criminalística 4TC-17 (Nivel Técnico)',
    conv='285-2026',
    alerta='El Estado y la función pública',
)

SEC = secciones('guias/GEN-01-PGN-4SP13-estado-funcion-publica.html')
del SEC[9]

# ----------------------------------------------------------------- correcciones de fondo
R = [
    # --- el nivel técnico, bien definido (art. 2.2.2.2.4 del Decreto 1083 de 2015) ---
    ('<tr><td><strong>Técnico</strong></td><td>Dominio de una técnica o tecnología</td><td>Técnica o tecnológica</td></tr>',
     '<tr><td><strong>Técnico</strong></td><td>Desarrollo de procesos y procedimientos en <strong>labores técnicas misionales y de apoyo</strong>, y aplicación de la ciencia y la tecnología</td><td>Técnica profesional o tecnológica</td></tr>'),
    ('<tr><td><strong>Asistencial</strong></td><td>Apoyo administrativo, operativo y de servicios</td><td>Bachillerato / formación básica (según el empleo)</td></tr>',
     '<tr><td><strong>Asistencial</strong></td><td>Actividades de apoyo complementarias de las tareas de los niveles superiores, o labores de predominio manual o de simple ejecución</td><td>Bachillerato / formación básica (según el empleo)</td></tr>'),

    ('<h4>Dónde se ubica el Secretario Procuraduría</h4>\n  <p>El cargo de <strong>Secretario Procuraduría</strong> pertenece al <mark>nivel Técnico</mark>. Sus funciones son de <strong>apoyo</strong>: recibir, radicar y distribuir correspondencia; organizar y conservar archivos; atender y orientar al público; llevar agendas y registros; apoyar la elaboración de documentos; manejar insumos y elementos de la oficina; y, en general, todas las tareas operativas que hacen posible el funcionamiento cotidiano de la dependencia. No formula políticas (eso es directivo), no asesora (asesor), no aplica una profesión titulada (profesional) ni ejecuta funciones técnicas especializadas complejas (técnico): <strong>apoya la operación</strong>. Reconocer esto es esencial para responder preguntas sobre el "alcance del cargo": el Secretario Procuraduría tiene un rol de soporte, no de decisión de fondo.</p>',
     '<h4>Dónde se ubica el Técnico en Criminalística</h4>\n  <p>El cargo de <strong>Técnico en Criminalística</strong> pertenece al <mark>nivel técnico</mark>, que agrupa los empleos cuyas funciones exigen el desarrollo de procesos y procedimientos en <strong>labores técnicas misionales y de apoyo</strong>, así como las relacionadas con la <strong>aplicación de la ciencia y la tecnología</strong>. Conviene subrayar la palabra <em>misionales</em>: el nivel técnico no es un nivel de simple soporte administrativo —eso corresponde al nivel asistencial—, sino el nivel que <strong>ejecuta técnica</strong> dentro de la misión de la entidad. En tu caso, la plaza ofertada está en la <strong>División de Gestión Humana</strong>, y esa técnica se aplica a la <strong>gestión del talento humano</strong>: preparar y verificar los soportes de los trámites de personal, proyectar los actos administrativos según los modelos establecidos, examinar informes en cuanto al método y la técnica de tu especialidad, llevar el control de la correspondencia y apoyar el archivo de las historias laborales.</p>\n  <p>Ahora bien, ejecutar técnica no es decidir. El Técnico en Criminalística <strong>no formula políticas</strong> (eso es del nivel directivo), <strong>no asesora a la alta dirección</strong> (asesor), <strong>no aplica una profesión titulada</strong> en el sentido del nivel profesional y, sobre todo, <strong>no adopta la decisión de fondo</strong> sobre la situación de personal: no nombra, no encarga, no reconoce prestaciones, no sanciona y no firma el acto administrativo. Reconocer esa doble idea —técnica de apoyo, sin decisión de fondo— es esencial para responder las preguntas sobre el "alcance del cargo", que son de las más frecuentes en la prueba.</p>'),

    ('<p class="cp-q">Un empleo cuyas funciones son "recibir y radicar correspondencia, organizar el archivo de la dependencia y orientar al público que se acerca a la oficina" corresponde a un nivel jerárquico. ¿Cuál?</p>\n    <div class="cp-op">Nivel directivo, porque organiza y coordina el trabajo de la oficina.</div>\n    <div class="cp-op">Nivel asesor, porque orienta a las personas que llegan.</div>\n    <div class="cp-op">Nivel profesional, porque exige aplicar conocimientos especializados.</div>\n    <div class="cp-op">Nivel Técnico, porque son funciones de apoyo administrativo, operativo y de servicios.</div>\n    <div class="cp-fb">Correcto: recibir, radicar, archivar y orientar son funciones de <strong>apoyo</strong>, propias del <strong>nivel Técnico</strong>, donde se ubica el Secretario Procuraduría. No implican dirección (directivo), asesoría (asesor) ni aplicación de una profesión titulada (profesional).</div>',
     '<p class="cp-q">Un empleo cuyas funciones son "verificar los soportes de las novedades de personal, proyectar los actos administrativos según los modelos establecidos y llevar el control de la correspondencia de la dependencia" corresponde a un nivel jerárquico. ¿Cuál?</p>\n    <div class="cp-op">Nivel directivo, porque organiza y coordina el trabajo de la dependencia.</div>\n    <div class="cp-op">Nivel asistencial, porque son actividades de apoyo complementarias de otros niveles.</div>\n    <div class="cp-op">Nivel profesional, porque exige el ejercicio de una profesión titulada.</div>\n    <div class="cp-op">Nivel técnico, porque exige desarrollar procesos y procedimientos con dominio de una técnica.</div>\n    <div class="cp-fb">Correcto: la <strong>cuarta</strong>. Verificar soportes contra la norma, proyectar actos administrativos conforme a los modelos y controlar la correspondencia exige <strong>desarrollar procesos y procedimientos</strong> con dominio de una técnica: eso define al <strong>nivel técnico</strong>. No es una actividad de apoyo complementaria y de simple ejecución (asistencial), ni dirección, ni ejercicio de profesión titulada.</div>'),
    ('<div class="checkpoint" data-correcta="3">\n    <div class="cp-tag">✅ Checkpoint 4</div>',
     '<div class="checkpoint" data-correcta="3">\n    <div class="cp-tag">✅ Checkpoint 4</div>'),

    ('<details class="acc"><summary>¿"Auxiliar" y "técnico" son lo mismo?</summary><div class="acc-body"><p>No. Aunque ambos son niveles operativos, el <strong>nivel técnico</strong> exige el <strong>dominio de una técnica o tecnología</strong> específica (con formación técnica o tecnológica) y realiza funciones técnicas especializadas; el <strong>nivel Técnico</strong> (donde está el Secretario Procuraduría) cumple funciones de <strong>apoyo administrativo, operativo y de servicios</strong>, generalmente con requisitos de formación más básicos. Un mismo despacho puede tener empleos técnicos y asistenciales, con funciones y responsabilidades distintas.</p></div></details>',
     '<details class="acc"><summary>¿El nivel técnico y el asistencial son lo mismo?</summary><div class="acc-body"><p>No, y la prueba lo pregunta. El <strong>nivel técnico</strong> desarrolla <strong>procesos y procedimientos técnicos misionales y de apoyo</strong> y aplica ciencia y tecnología: exige el dominio de una técnica y, por eso, formación técnica profesional o tecnológica. El <strong>nivel asistencial</strong> realiza <strong>actividades de apoyo complementarias</strong> de las tareas de los niveles superiores, o labores de predominio manual o de simple ejecución. Una misma dependencia puede tener empleos de los dos niveles, con funciones y responsabilidades distintas: quien verifica si una novedad de personal cumple los requisitos de la norma y quien solo la entrega al despacho no hacen lo mismo ni responden por lo mismo.</p></div></details>'),

    ('<p>Memoriza el orden descendente: <strong>Directivo → Asesor → Profesional → Técnico → Asistencial</strong>. La palabra clave de cada nivel: directivo = <em>dirige/decide</em>; asesor = <em>aconseja</em>; profesional = <em>profesión titulada</em>; técnico = <em>técnica/tecnología</em>; asistencial = <em>apoya/opera</em>. Tu cargo vive en el nivel <strong>Técnico</strong>, el cuarto de los cinco.</p>',
     '<p>Memoriza el orden descendente: <strong>Directivo → Asesor → Profesional → Técnico → Asistencial</strong>. La palabra clave de cada nivel: directivo = <em>dirige y decide</em>; asesor = <em>aconseja a la alta dirección</em>; profesional = <em>profesión titulada</em>; técnico = <em>procesos y procedimientos con dominio de una técnica</em>; asistencial = <em>apoyo complementario</em>. Tu cargo vive en el <strong>nivel técnico</strong>, el cuarto de los cinco, y lo ejerce en la <strong>División de Gestión Humana</strong>: tramitar, verificar y proyectar, no decidir.</p>'),

    # --- alcance del cargo: ejemplo y tabla ---
    ('<p>Tu jefe está fuera y llega una situación que requiere <strong>decidir</strong> algo de fondo sobre un expediente (por ejemplo, resolver una solicitud sustancial). Un compañero te dice: "resuélvelo tú, para no dejar esperando a la persona". ¿Debes hacerlo?</p>\n      <p><strong>Cómo proceder:</strong> no. Como Secretario Procuraduría del <strong>nivel Técnico</strong>, tu función es de <strong>apoyo</strong>, no de decisión de fondo. Puedes recibir, registrar, orientar y preparar lo necesario para que la autoridad competente decida, pero decidir el fondo excede tu nivel y podría configurar una <strong>extralimitación de funciones</strong> (art. 6 CP). Lo correcto es dejar la solicitud lista para el funcionario competente e informar a la persona de los tiempos. Conocer tu nivel te protege.</p>',
     '<p>El jefe de la División está fuera y un servidor insiste: necesita que alguien <strong>autorice</strong> hoy su comisión de servicios, porque viaja mañana. Un compañero te dice: "tú ya tienes el proyecto hecho, fírmalo tú y después le cuentas". ¿Debes hacerlo?</p>\n      <p><strong>Cómo proceder:</strong> no. Como Técnico en Criminalística del <strong>nivel técnico</strong> ubicado en la División de Gestión Humana, tu función es <strong>preparar, verificar, tramitar y proyectar</strong>: puedes tener el acto listo, con los soportes completos y los fundamentos normativos citados. Pero <strong>conferir la comisión es competencia del funcionario facultado</strong>, y firmar en su lugar configuraría una <strong>extralimitación de funciones</strong> (art. 6 CP) y haría nulo el acto por falta de competencia. Lo correcto es dejar el proyecto y los soportes listos para la firma de quien decide, informar al servidor del trámite real y los tiempos, y dejar constancia. Conocer tu nivel te protege.</p>'),

    ('<thead><tr><th>Sí hace el Secretario Procuraduría (apoyo)</th><th>No le corresponde (excede su nivel)</th></tr></thead>\n      <tbody>\n        <tr><td>Recibir, radicar y distribuir correspondencia</td><td>Formular políticas o planes de la entidad</td></tr>\n        <tr><td>Organizar y conservar el archivo</td><td>Decidir el fondo de un asunto o expediente</td></tr>\n        <tr><td>Atender y orientar al público</td><td>Asesorar jurídicamente a la dirección</td></tr>\n        <tr><td>Apoyar la elaboración de documentos y registros</td><td>Firmar actos administrativos de competencia superior</td></tr>\n      </tbody>',
     '<thead><tr><th>Sí hace el Técnico en Criminalística 4TC-17 (apoyo técnico)</th><th>No le corresponde (excede su nivel)</th></tr></thead>\n      <tbody>\n        <tr><td>Preparar, verificar y tramitar las novedades y los trámites de personal, revisando que los soportes cumplan los requisitos</td><td>Formular las políticas o los planes de talento humano de la entidad</td></tr>\n        <tr><td>Proyectar los actos administrativos de personal «según los modelos y procedimientos establecidos», para la firma del competente</td><td>Nombrar, encargar, trasladar, conferir comisiones o aceptar renuncias</td></tr>\n        <tr><td>Examinar informes en cuanto a la pertinencia e idoneidad de los métodos, procedimientos y técnicas de su especialidad</td><td>Calificar jurídicamente el asunto, reconocer prestaciones o sancionar</td></tr>\n        <tr><td>Llevar el control de la correspondencia y apoyar el archivo de las historias laborales</td><td>Firmar los actos administrativos de competencia del superior</td></tr>\n      </tbody>'),

    # --- ejemplos reenfocados ---
    ('<p>Para ti como futuro Secretario Procuraduría, la función administrativa es <strong>tu hábitat natural</strong>: casi todo lo que harás (radicar, archivar, atender, apoyar trámites) es ejercicio de función administrativa.',
     '<p>Para ti como futuro Técnico en Criminalística, la función administrativa es <strong>tu hábitat natural</strong>: casi todo lo que harás (tramitar una novedad de personal, verificar un soporte, proyectar un acto administrativo, expedir una constancia laboral, radicar y controlar la correspondencia) es ejercicio de función administrativa: cada acto de personal que proyectas, cada soporte que verificas y cada constancia que expides producen efectos jurídicos sobre una persona concreta.'),

    ('<p>Estás en la ventanilla de correspondencia de una oficina de la PGN. Llega una persona mayor, confundida, con un sobre en la mano; no sabe si su documento debe radicarse allí o en otra dependencia. Tú tienes tres opciones: decirle secamente "aquí no es", ignorarla porque "no es tu función explicar", u orientarla con claridad indicándole dónde y cómo radicar.</p>',
     '<p>Estás en la División de Gestión Humana revisando los soportes de una novedad. Llega una persona mayor, confundida, con un sobre en la mano: es un exservidor que quiere pedir su certificación laboral y no sabe si debe radicarla allí o en otra dependencia. Tú tienes tres opciones: decirle secamente "aquí no es", ignorarla porque "no es tu función explicar", u orientarla con claridad indicándole dónde y cómo hacerlo.</p>'),

    ('Un Secretario Procuraduría que "despacha" a la gente sin orientarla traiciona el sentido mismo de su cargo.',
     'Un servidor que "despacha" a la gente sin orientarla traiciona el sentido mismo de su cargo, por técnico que sea su empleo.'),

    ('Tu trabajo, por sencillo que parezca (recibir un documento, atender a una persona, organizar un archivo), es una <mark>manifestación del poder estatal puesto al servicio de la comunidad</mark>.',
     'Tu trabajo —verificar un soporte, proyectar un acto de personal, expedir una certificación, controlar la correspondencia— es una <mark>manifestación del poder estatal puesto al servicio de la comunidad</mark>.'),

    ('Conocerlas es útil para tu trabajo: como Secretario Procuraduría tramitarás y registrarás muchas de estas situaciones del personal.',
     'Conocerlas es útil para tu trabajo: son <strong>exactamente</strong> los trámites que pasarán por tus manos todos los días en la División de Gestión Humana, y además son materia evaluada en la prueba de conocimientos.'),

    ('Como Secretario Procuraduría apoyarás, con tu trabajo operativo, el cumplimiento de esas funciones misionales de control.',
     'Como Técnico en Criminalística de la División de Gestión Humana apoyarás esas funciones misionales desde la <strong>gestión del talento humano</strong>: sin servidores bien nombrados, bien pagados, bien capacitados y con su historia laboral en orden, la entidad no puede ejercer el control que la Constitución le encarga.'),

    ('<p>Llega a tu ventanilla una comunicación que denuncia el "mal uso de los recursos públicos" de una entidad y pide que se investigue el detrimento patrimonial. El remitente la dirigió a la PGN.</p>',
     '<p>Al despacho llega una comunicación que denuncia el "mal uso de los recursos públicos" de una entidad y pide que se investigue el detrimento patrimonial. El remitente la dirigió a la PGN y llega a tu control de correspondencia para que la direcciones a la dependencia competente.</p>'),

    ('<p>El <strong>Secretario Procuraduría 4SP-13</strong> de la PGN es un <strong>servidor público del nivel Técnico</strong>: apoya la operación de una oficina de un <strong>órgano de control</strong>, bajo un <strong>régimen especial de carrera</strong>. Comprender el Estado y la función pública te dice dónde encajas, a qué reglas te sometes y por qué tu trabajo de apoyo contribuye a los fines del Estado.</p>',
     '<p>El <strong>Técnico en Criminalística 4TC-17</strong> de la PGN es un <strong>servidor público del nivel técnico</strong>: apoya técnicamente la <strong>gestión del talento humano</strong> —tramita, verifica, proyecta y archiva— en un <strong>órgano de control</strong>, bajo un <strong>régimen especial de carrera</strong>. Comprender el Estado y la función pública te dice dónde encajas, a qué reglas te sometes y por qué tu trabajo de apoyo contribuye a los fines del Estado.</p>'),

    ('"Estado que sirve, poder que se controla, función con principios y servidores de mérito: en ese mapa, la PGN es control autónomo de régimen especial —no CNSC— y el Secretario Procuraduría apoya, no decide. — Día 2"',
     '"Estado que sirve, poder que se controla, función con principios y servidores de mérito: en ese mapa, la PGN es un control autónomo de régimen especial —no CNSC— y el Técnico en Criminalística 4TC-17 tramita, verifica y proyecta; no decide ni firma. — Día 2"'),

    ('Como <strong>Secretario Procuraduría</strong> serás parte del <mark>nivel Técnico</mark> de una entidad del Estado: apoyarás la operación diaria de una oficina (documentos, correspondencia, atención, agenda, insumos), sin funciones de dirección ni decisión de fondo. Conocer el Estado y la función pública no es "teoría": es entender <strong>dónde encajas</strong>, a qué reglas te sometes y por qué tu trabajo, aunque de apoyo, contribuye a los fines del Estado.',
     'Como <strong>Técnico en Criminalística</strong> serás parte del <mark>nivel técnico</mark> de un órgano de control: aplicarás una técnica para apoyar la <strong>gestión del talento humano</strong> en la División de Gestión Humana: prepararás y verificarás los soportes de los trámites de personal, proyectarás actos administrativos para la firma del competente, examinarás informes y llevarás el control de la correspondencia y del archivo de las historias laborales, sin funciones de dirección ni decisión de fondo. Conocer el Estado y la función pública no es "teoría": es entender <strong>dónde encajas</strong>, a qué reglas te sometes y por qué la calidad de tu trabajo contribuye a los fines del Estado.'),

    ('Cuatro casos típicos del trabajo de un Secretario Procuraduría de la PGN.',
     'Cuatro casos típicos del trabajo de un Técnico en Criminalística 4TC-17 en la División de Gestión Humana de la PGN.'),

    # --- identidad ---
    ('Secretario Procuraduría', 'Técnico en Criminalística'),
    ('4SP-13', '4TC-17'),
    ('283-2026', '285-2026'),
]

SEC = aplicar_todas(SEC, R, estricto=True)
SEC = aplicar_todas(SEC, limpieza_rol('Técnico en Criminalística', 'Técnicos en Criminalística'), estricto=False)   # filtro antifugas final
SEC = aplicar_todas(SEC, [('(aquí el Secretario)', '(aquí el Técnico en Criminalística)'),
                          ('Secretaria', 'Técnico en Criminalística'), ('Secretario', 'Técnico en Criminalística')], estricto=False)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el Estado y la '
              'función pública. Los contextos son extensos y las cuatro opciones son plausibles y elaboradas. '
              'Al seleccionar una opción verás si acertaste y la explicación.')

P = [
 (2,
  'Usted es Técnico en Criminalística 4TC-17 de la División de Gestión Humana y está terminando un informe cuando una señora mayor entra al edificio buscando dónde presentar una queja contra un funcionario de su municipio. Trae los papeles desordenados y no entiende las indicaciones del aviso de la entrada. Un compañero le dice que no se distraiga, que «eso no es función suya» y que el término del informe corre.',
  'A la luz de los fines esenciales del Estado (art. 2 de la Constitución), ¿cuál es la actuación correcta?',
  ['Continuar con el informe sin atender a la señora, porque el término que corre es un deber concreto del cargo y la orientación al público corresponde exclusivamente al personal de atención al ciudadano.',
   'Recibirle los documentos y archivarlos en el expediente que usted tramita, para evitar que la señora tenga que hacer otra fila y resolverle el problema de la manera más rápida posible.',
   'Orientarla con claridad sobre dónde y cómo radicar su queja, sin descuidar el término del informe, porque servir a la comunidad y facilitar la participación son fines esenciales del Estado.',
   'Explicarle que la Procuraduría no recibe quejas de particulares contra funcionarios municipales y sugerirle que acuda directamente a la alcaldía del municipio donde ocurrieron los hechos.'],
  'Los fines esenciales del artículo 2 no son un adorno: «servir a la comunidad» y «facilitar la participación» se materializan en actos concretos como orientar a quien no sabe dónde radicar. Orientar no implica abandonar el término: son deberes compatibles.',
  'Ni despachar a la persona, ni archivar su queja en un expediente ajeno, ni negar una competencia que la PGN sí tiene. El Estado cumple su fin cuando el servidor orienta con claridad.'),

 (1,
  'En una capacitación interna, un compañero afirma que la Procuraduría «pertenece a la rama judicial, porque investiga y sanciona», y otro sostiene que es «una dependencia del Gobierno, porque vigila a los funcionarios del Ejecutivo». El jefe le pide a usted precisar la ubicación de la entidad dentro de la organización del Estado, porque de ello depende entender por qué puede vigilar a servidores de cualquier rama.',
  'Conforme al artículo 113 de la Constitución, ¿cuál es la afirmación correcta?',
  ['La Procuraduría pertenece a la rama judicial, y por eso sus decisiones disciplinarias tienen naturaleza jurisdiccional y son revisadas por el Consejo Superior de la Judicatura.',
   'Las ramas del poder son separadas pero colaboran armónicamente, y la Procuraduría es un órgano autónomo e independiente de control que no pertenece a ninguna de las tres ramas.',
   'La Procuraduría forma parte de la rama ejecutiva, porque ejerce funciones administrativas de vigilancia y su jefe es elegido con participación del Presidente de la República.',
   'La Procuraduría es una cuarta rama del poder público, jerárquicamente superior a las otras tres, lo que le permite revisar las decisiones de cualquier autoridad del Estado.'],
  'El artículo 113 enumera las tres ramas y añade que existen otros órganos autónomos e independientes para el cumplimiento de las demás funciones del Estado. La Procuraduría, como órgano de control, es uno de ellos: por eso puede vigilar a servidores de todas las ramas sin conflicto de interés.',
  'No pertenece a la rama judicial ni a la ejecutiva, y tampoco es una «cuarta rama» superior. Es un órgano autónomo de control, separado de las tres ramas y en colaboración armónica con ellas.'),

 (3,
  'Una entidad investigada le entrega a usted, como apoyo técnico, copia de un certificado que la propia Procuraduría ya le había solicitado meses atrás y que reposa en el expediente. Un compañero propone pedirle a la entidad que lo vuelva a allegar «autenticado y con firma fresca» para que no haya dudas, aunque eso tome tres semanas más y el expediente tenga términos corriendo.',
  '¿Qué principio de la función administrativa orienta la decisión y cómo se aplica?',
  ['El principio de publicidad, que obliga a comunicar todas las actuaciones a los interesados, por lo que debe requerirse de nuevo el documento para que quede constancia pública de su aporte.',
   'El principio de moralidad, que exige desconfiar de los documentos aportados por la entidad investigada y verificarlos siempre mediante un nuevo requerimiento formal con firma reciente.',
   'El principio de imparcialidad, que impide usar documentos que la propia entidad investigada aportó, de modo que la prueba debe reconstruirse por un canal distinto al de la entidad.',
   'El principio de economía (art. 209 CP), que ordena no exigir documentos que ya reposan en la entidad: se usa el que está en el expediente y se dejan los recursos para lo que sí falta.'],
  'El artículo 209 somete la función administrativa a los principios de igualdad, moralidad, eficacia, economía, celeridad, imparcialidad y publicidad. La economía impide repetir trámites y volver a pedir lo que ya se tiene; además, la celeridad protege los términos.',
  'Publicidad, moralidad e imparcialidad no obligan a repetir un documento que ya obra en el expediente. Repetirlo desgasta a la entidad y al despacho, y pone en riesgo los términos.'),

 (0,
  'Un familiar le comenta a usted, que aspira al cargo de Técnico en Criminalística 4TC-17, que conoce a una persona con influencia en la Procuraduría y que «con una recomendación entra más fácil». Añade que eso «se hace en todas partes» y que no tiene nada de malo porque usted de todos modos cumple los requisitos del empleo y presentó todas las pruebas del concurso. El jefe recuerda que la dependencia ya recibió una observación por repetir requerimientos innecesarios y pide que la respuesta quede motivada por escrito antes del vencimiento.',
  '¿Qué le responde y con qué fundamento constitucional?',
  ['Que a los empleos de carrera se ingresa por mérito, mediante concurso público, y que una recomendación no solo es inútil sino impropia, porque el artículo 125 impone el mérito como regla de ingreso.',
   'Que la recomendación es válida siempre que no implique pago de dinero, porque lo que prohíbe la Constitución es el cohecho y no la gestión de un tercero ante la entidad convocante.',
   'Que puede intentarlo, pues el mérito solo rige para la prueba de conocimientos y las demás etapas admiten la valoración discrecional de quien administra el proceso de selección.',
   'Que la recomendación conviene presentarla por escrito ante la Oficina de Selección y Carrera, para que quede en el expediente y pueda valorarse como parte del análisis de antecedentes.'],
  'El artículo 125 establece que los empleos en los órganos del Estado son de carrera y que el ingreso se hace previo cumplimiento de los requisitos y condiciones que fije la ley para determinar los méritos de los aspirantes. El mérito es la regla: la recomendación no cabe.',
  'No hay versión aceptable de la recomendación. El ingreso a un empleo de carrera se decide por mérito en un concurso público, y ninguna etapa admite valoraciones por influencia.'),

 (1,
  'Durante una diligencia de apoyo técnico, el jefe de una entidad investigada le dice a usted, en voz baja, que «le reconocería su gestión» si el informe técnico no menciona ciertos pagos. Le aclara que no es un soborno, sino «un detalle por el trabajo», y le recuerda que usted no firma la decisión de fondo, de modo que su informe «tampoco define nada». Usted está solo en la diligencia, el jefe no contesta el teléfono y el funcionario insiste en que «nadie se va a enterar» porque no hay nada firmado todavía.',
  '¿Qué está en juego y cuál es la conducta correcta?',
  ['Puede escuchar la propuesta sin comprometerse y decidir después, porque mientras no reciba nada no hay falta y conviene conocer qué información quiere ocultar la entidad investigada.',
   'Debe rechazar el ofrecimiento, dejar constancia escrita de lo ocurrido y ponerlo en conocimiento de la autoridad competente, porque recibir dádivas está prohibido y el hecho puede ser falta y delito.',
   'Puede aceptar el detalle si su valor es moderado y lo declara después ante su jefe, ya que lo prohibido es condicionar el contenido del informe y no recibir una atención por el trabajo realizado.',
   'Debe limitarse a no mencionar el episodio en el informe y continuar la diligencia con normalidad, porque incluir ese dato podría afectar la imparcialidad con que se valora a la entidad.'],
  'Recibir dádivas o beneficios por razón del cargo está expresamente prohibido y puede configurar falta gravísima, además de conductas penales. Que usted no firme la decisión de fondo no reduce su responsabilidad: su informe sí influye en el resultado.',
  'Ni escuchar «sin comprometerse», ni aceptar un detalle moderado, ni callar el episodio. La conducta íntegra es rechazar, dejar constancia y poner el hecho en conocimiento de quien corresponde.'),

 (2,
  'En un grupo de estudio se discute la diferencia entre inhabilidad e incompatibilidad. Un aspirante afirma que «son lo mismo, solo cambia el nombre»; otro sostiene que la inhabilidad aparece después de la posesión y la incompatibilidad antes. Le piden a usted ordenar los conceptos con un ejemplo aplicable al cargo que está concursando. El grupo ha discutido el punto dos veces sin ponerse de acuerdo y uno de ellos insiste en que la diferencia «no se pregunta en la prueba», mientras otro sostiene que depende de si la sanción fue penal o disciplinaria.',
  '¿Cuál es la distinción correcta?',
  ['La inhabilidad surge mientras se ejerce el empleo y la incompatibilidad impide acceder a él; por eso la primera se verifica en la evaluación de desempeño y la segunda en el concurso de méritos.',
   'Ambas figuras significan lo mismo en el derecho público colombiano y la diferencia es puramente terminológica, de modo que en la prueba pueden usarse de manera indistinta sin error.',
   'La inhabilidad es un impedimento para acceder al empleo o para ser designado; la incompatibilidad es la imposibilidad de ejercer simultáneamente el empleo con otra actividad o cargo.',
   'La inhabilidad solo proviene de sanciones penales en firme y la incompatibilidad solo de sanciones disciplinarias, de modo que ambas dependen de una decisión sancionatoria previa.'],
  'La inhabilidad opera como impedimento de entrada (no puede ser nombrado o elegido); la incompatibilidad opera durante el ejercicio (no puede hacer dos cosas a la vez). Es una de las comparaciones más preguntadas del régimen del servidor público.',
  'No son sinónimos ni se distinguen por el momento en que se sancionan. La inhabilidad impide acceder; la incompatibilidad impide ejercer simultáneamente otra actividad o cargo.'),

 (3,
  'Un compañero de estudio le dice que, para preparar el concurso de la Procuraduría, lo esencial es dominar la Ley 909 de 2004 y los acuerdos de la Comisión Nacional del Servicio Civil, porque «todos los concursos del Estado se rigen por esas normas». Usted recuerda que el formato de convocatoria menciona expresamente un régimen distinto. El compañero insiste en que descargó un material de estudio donde todo se explica con la Ley 909, y le muestra un cuadro de términos y reclamaciones de la CNSC que no coincide con el cronograma de la convocatoria.',
  '¿Cuál es la precisión correcta sobre el régimen de carrera de la PGN?',
  ['El compañero tiene razón: la Ley 909 de 2004 es la norma general de carrera y se aplica a todas las entidades del Estado, incluidos los órganos de control como la Procuraduría General de la Nación.',
   'La Procuraduría aplica la Ley 909 de 2004 en el ingreso y su régimen especial solo en el retiro, de modo que el concurso se rige íntegramente por las reglas de la Comisión Nacional del Servicio Civil.',
   'La Procuraduría carece de régimen de carrera propio y por eso cada convocatoria define libremente sus reglas, sin sujeción a una norma previa que regule el ingreso y la permanencia.',
   'La PGN tiene un régimen especial de carrera (Decretos Ley 262, 263 y 264 de 2000) y administra su propio concurso: no es un proceso de la Comisión Nacional del Servicio Civil.'],
  'La Constitución admite sistemas especiales de carrera y el de la Procuraduría está en el Decreto Ley 262 de 2000. La entidad convoca, administra y resuelve su proceso: por eso la plataforma, las reclamaciones y los términos son los de la PGN.',
  'La Ley 909 de 2004 es la norma general, pero no rige el sistema especial de la PGN, que tampoco carece de regulación: su carrera está en los decretos ley de 2000.'),

 (0,
  'Al despacho llega una queja ciudadana que denuncia el presunto «mal uso de los recursos públicos» de una entidad territorial y pide que se investigue el detrimento patrimonial y se recuperen los dineros. El jefe le pide a usted un concepto previo sobre la competencia antes de asignar el apoyo técnico, porque un compañero sostiene que todo debe tramitarlo la Procuraduría. Un tercer compañero propone devolver la queja al ciudadano indicándole que se equivocó de entidad, y el jefe advierte que esa salida ya generó una tutela el año pasado.',
  '¿Cómo se reparten las competencias entre los órganos de control?',
  ['El control fiscal y la declaratoria de responsabilidad fiscal corresponden a la Contraloría; la Procuraduría examina la conducta del servidor en lo disciplinario, de modo que el asunto se orienta a ambas.',
   'La Procuraduría asume el caso completo, declara el detrimento patrimonial y ordena el reintegro de los recursos, porque es el órgano de control con competencia preferente sobre los servidores públicos.',
   'El asunto es exclusivamente de la Contraloría, por lo que la Procuraduría debe abstenerse de cualquier actuación disciplinaria mientras no termine el proceso de responsabilidad fiscal.',
   'La competencia depende de la cuantía del detrimento: por debajo de cien salarios mínimos conoce la Procuraduría y por encima de esa suma conoce la Contraloría General de la República.'],
  'Son controles autónomos y concurrentes: la Contraloría ejerce el control fiscal y declara la responsabilidad fiscal; la Procuraduría ejerce el control disciplinario sobre la conducta del servidor. Un mismo hecho puede dar lugar a ambos.',
  'La PGN no declara responsabilidad fiscal ni ordena reintegros, no debe abstenerse por existir un proceso fiscal, y la competencia no se reparte por cuantía.'),

 (2,
  'Usted apoya técnicamente un expediente y advierte que un servidor, por descuido en el cumplimiento de sus deberes, dejó vencer un plazo que causó un perjuicio a la entidad. En la reunión de equipo, un compañero sostiene que «sin intención no hay responsabilidad» y otro, que «el servidor solo responde si se apropió de algo». El servidor investigado sostiene en su versión que «nunca quiso perjudicar a nadie» y que el vencimiento se debió a la carga de trabajo del despacho, y el jefe le pide a usted entender el marco antes de preparar el informe técnico.',
  'Conforme al artículo 6 de la Constitución, ¿cuál es la lectura correcta de la responsabilidad del servidor?',
  ['El compañero tiene razón: sin intención de causar daño no hay responsabilidad del servidor, porque el reproche exige siempre una conducta deliberada dirigida a perjudicar a la administración.',
   'El servidor solo responde cuando se apropia de recursos públicos o cuando obtiene un provecho personal, pues de lo contrario el perjuicio se atribuye a la entidad y no a la persona.',
   'Los servidores responden por infringir la Constitución y la ley y, además, por omisión o extralimitación en el ejercicio de sus funciones: el descuido en el cumplimiento del deber también genera reproche.',
   'La responsabilidad del servidor solo se configura cuando un juez penal lo condena previamente, de modo que antes de esa condena ninguna otra autoridad puede reprocharle su conducta.'],
  'El artículo 6 establece que los particulares solo responden por infringir la Constitución y la ley, y que los servidores públicos lo hacen también por omisión o extralimitación en el ejercicio de sus funciones. La omisión descuidada entra plenamente en ese marco.',
  'Ni se exige intención de dañar, ni apropiación, ni condena penal previa. La omisión y la extralimitación bastan para que el servidor responda.'),

 (1,
  'Un aspirante sostiene en el grupo de estudio que el Técnico en Criminalística de la PGN es un «trabajador oficial» y que, por eso, podría negociar sus funciones y su salario mediante convención colectiva. Otro responde que es «empleado público» pero no sabe explicar la consecuencia práctica de esa diferencia. El aspirante agrega que, según él, un compañero suyo que trabaja en otra entidad firmó un contrato donde le subieron el sueldo, y que lo mismo podría hacerse en la Procuraduría una vez superado el período de prueba.',
  '¿Cuál es la precisión correcta y qué consecuencia tiene?',
  ['Es trabajador oficial, vinculado por contrato de trabajo, y por eso sus funciones y su remuneración se fijan en el contrato y pueden modificarse por acuerdo entre las partes.',
   'Es empleado público, con vínculo legal y reglamentario: sus funciones y condiciones las fijan la ley y el manual de funciones, no un contrato que el servidor pueda negociar.',
   'Es empleado público, pero su vínculo es contractual, de modo que el manual de funciones opera apenas como una guía orientadora que admite ajustes individuales con el jefe.',
   'Su condición depende de la dependencia donde quede ubicado: en las direcciones nacionales es trabajador oficial y en las procuradurías territoriales es empleado público.'],
  'Los empleados públicos tienen vínculo legal y reglamentario: la ley y el manual específico de funciones definen qué hacen y en qué condiciones. Los trabajadores oficiales, vinculados por contrato, son típicamente los de construcción y sostenimiento de obras públicas.',
  'El vínculo no es contractual ni depende de la dependencia. Es legal y reglamentario, y por eso el manual de funciones no se negocia.'),

 (3,
  'En una reunión, el jefe explica que la dependencia debe ajustar su forma de documentar las actuaciones y pregunta al equipo quién vigila que la administración cumpla. Un integrante menciona solo a la Contraloría; otro cree que el control interno lo ejerce la Procuraduría sobre las entidades vigiladas. El jefe aclara que la pregunta no es teórica: de esa distinción depende a qué autoridad se remite cada hallazgo del informe técnico que la dependencia está preparando sobre la entidad vigilada.',
  '¿Cómo se distinguen los controles sobre la administración?',
  ['El control interno lo ejerce la Procuraduría sobre las entidades que vigila, el fiscal lo ejerce la Contraloría y el disciplinario corresponde a las oficinas de personal de cada entidad.',
   'Todos los controles los concentra la Contraloría General de la República, que por eso puede sancionar disciplinariamente y declarar la responsabilidad fiscal de los servidores públicos.',
   'El control interno y el control disciplinario son el mismo sistema con dos nombres, y ambos los ejerce la oficina de control interno disciplinario de cada entidad del Estado.',
   'El control interno es responsabilidad de cada entidad (Ley 87 de 1993), el fiscal lo ejerce la Contraloría, el disciplinario la PGN y las oficinas internas, y existe además el control social y ciudadano.'],
  'Cada control tiene su titular: el interno es de la propia entidad y de su representante legal; el fiscal, de la Contraloría; el disciplinario, de la PGN y de las oficinas de control interno disciplinario; y la ciudadanía ejerce control social.',
  'La Procuraduría no ejerce el control interno de las entidades vigiladas, la Contraloría no concentra todos los controles y el control interno no se confunde con el disciplinario.'),

 (0,
  'Usted acaba de ser nombrado en período de prueba como Técnico en Criminalística. Un compañero le dice que ese período «es una formalidad» y que la estabilidad de carrera se adquiere con el solo nombramiento, de modo que no debe preocuparse por la evaluación que se hará al final. El compañero añade que conoce a alguien que «nunca hizo la evaluación» y sigue trabajando sin problema, y le aconseja concentrarse únicamente en no cometer faltas disciplinarias durante los primeros meses.',
  '¿Cuál es la lectura correcta del período de prueba en un empleo de carrera?',
  ['Es la última fase del proceso de selección, ya en el puesto de trabajo: al superarlo con evaluación satisfactoria el servidor adquiere los derechos de carrera; si no lo supera, el nombramiento se declara insubsistente.',
   'Es una formalidad administrativa sin efectos, porque los derechos de carrera se adquieren desde la posesión y la evaluación posterior solo sirve para fines estadísticos de la entidad.',
   'Es un contrato temporal previo al nombramiento definitivo, de modo que durante ese lapso el servidor no tiene las obligaciones ni los deberes propios de los empleados públicos.',
   'Es un período en el que el servidor puede ser trasladado libremente a cualquier entidad del Estado, y solo al final se define en cuál de ellas quedará vinculado de manera definitiva.'],
  'El período de prueba cierra el proceso de selección dentro del puesto: se evalúa el desempeño y, si es satisfactorio, se inscribe al servidor en el registro de carrera. No es un trámite simbólico ni un contrato aparte.',
  'Los derechos de carrera no nacen con la sola posesión, el período de prueba no es un contrato temporal y no habilita traslados libres entre entidades.'),

 (2,
  'En la dependencia coinciden dos solicitudes de personal: un servidor pide vacaciones y otro presenta una incapacidad médica. El jefe le pide a usted, que apoya la organización del trabajo técnico de la semana, entender el efecto de cada situación para reprogramar las diligencias ya agendadas. Dos de esas diligencias son inspecciones con hora fija ya comunicadas a las entidades, y el jefe advierte que reprogramar sin justificación genera quejas de los sujetos procesales.',
  '¿Cómo se clasifican esas dos situaciones y qué implican?',
  ['Ambas son licencias: la diferencia es que una se pide y otra se impone, pero en los dos casos el servidor se separa definitivamente del empleo y debe proveerse la vacante de manera permanente.',
   'Ambas corresponden a comisiones, porque el servidor deja de ejercer temporalmente sus funciones, y durante ellas el empleo queda vacante para efectos de un nuevo nombramiento en propiedad.',
   'Son situaciones administrativas distintas —vacaciones y licencia por enfermedad—, que suspenden temporalmente el ejercicio de funciones sin romper el vínculo: las diligencias deben reprogramarse.',
   'Solo la incapacidad es una situación administrativa; las vacaciones son un derecho laboral que no afecta la disponibilidad del servidor ni obliga a reprogramar las diligencias agendadas.'],
  'Las situaciones administrativas describen la posición del servidor frente al empleo: servicio activo, vacaciones, licencias, comisiones, encargo, entre otras. Suspenden o modifican el ejercicio de funciones, pero no extinguen el vínculo.',
  'No son licencias idénticas ni comisiones, no implican separación definitiva y las vacaciones sí afectan la disponibilidad: por eso se reprograma la agenda.'),

 (1,
  'Un integrante nuevo del equipo sostiene que la función administrativa es exclusiva de la rama ejecutiva y que, por tanto, cuando la Procuraduría contrata insumos o adelanta este concurso «no ejerce función administrativa sino función de control». El jefe le pide a usted precisar el punto, porque de ello depende qué principios se aplican. El integrante insiste en que, si fuera función administrativa, cualquier ciudadano podría demandar las decisiones del concurso, y el jefe le pide a usted aclarar el punto con fundamento normativo.',
  '¿Cuál es la afirmación correcta?',
  ['El integrante tiene razón: la función administrativa es propia de la rama ejecutiva y los órganos de control ejercen una función distinta, sujeta únicamente a sus normas especiales de carrera.',
   'Todas las ramas y órganos del Estado cumplen función administrativa cuando gestionan su propio funcionamiento, y por eso la actuación de la PGN se somete a los principios del artículo 209.',
   'La función administrativa solo existe cuando se expide un acto administrativo de carácter general, de modo que la contratación de insumos o un concurso quedan por fuera de esa noción.',
   'La Procuraduría no ejerce función administrativa en ningún caso, porque sus actuaciones son manifestaciones de la función de control y se rigen exclusivamente por el Código General Disciplinario.'],
  'La función administrativa no se define por el órgano que la ejerce sino por su contenido: gestionar los asuntos propios del Estado. Por eso la PGN, al convocar un concurso o contratar, actúa administrativamente y queda sujeta al artículo 209.',
  'La función administrativa no es monopolio del Ejecutivo, no se limita a los actos generales y la PGN sí la ejerce cuando gestiona su funcionamiento.'),

 (3,
  'Un aspirante prepara el concurso y afirma que, como el cargo es del nivel técnico, sus funciones serán de apoyo administrativo: radicar documentos, organizar el archivo y atender al público. Otro compañero sostiene que el nivel técnico y el asistencial son equivalentes. El facilitador le pide a usted precisar la definición normativa del nivel técnico. El facilitador recuerda que de esa definición depende entender qué puede y qué no puede hacer el cargo, y advierte que en las pruebas anteriores varias preguntas giraron exactamente sobre esa distinción.',
  '¿Cuál es la descripción correcta del nivel técnico?',
  ['Agrupa los empleos de apoyo administrativo, operativo y de servicios, complementarios de las tareas de los niveles superiores, con requisitos de formación básica y sin contenido misional propio.',
   'Agrupa los empleos que requieren una profesión titulada y la aplicación de los conocimientos propios de una disciplina académica, con independencia de que su contenido sea misional o de apoyo.',
   'Es equivalente al nivel asistencial y la única diferencia práctica es la denominación del empleo en la planta de personal, pues ambos cumplen funciones de simple ejecución material.',
   'Agrupa los empleos cuyas funciones exigen el desarrollo de procesos y procedimientos en labores técnicas misionales y de apoyo, y las relacionadas con la aplicación de la ciencia y la tecnología.'],
  'Esa es la definición del nivel técnico: desarrollar procesos y procedimientos con dominio de una técnica. Como ocurre con el Técnico en Criminalística 4TC-17, que verifica soportes, tramita novedades y proyecta los actos administrativos de personal según los modelos establecidos.',
  'El apoyo administrativo complementario corresponde al nivel asistencial, la profesión titulada al nivel profesional, y el técnico no equivale al asistencial: ejecuta procesos técnicos, incluso misionales.'),
]
