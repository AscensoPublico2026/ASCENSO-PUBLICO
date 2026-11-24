# -*- coding: utf-8 -*-
"""Día 20 · Gestión documental, archivo, correspondencia y documentos de oficina — 4TC-17."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-GDOC-4TC17B-01',
    archivo='FUN-GDOC-4TC17B-01-gestion-documental-correspondencia-ofimatica.html',
    dia=20,
    titulo_doc='Gestión documental, correspondencia y documentos de oficina',
    h1='Gestión documental<br>y documentos de oficina',
    kicker='Día 20 · Conocimientos comunes',
    sub='El último día de contenido reúne cuatro de los <strong>conocimientos comunes</strong> que el formato de convocatoria exige: <strong>gestión documental</strong>, <strong>archivo y correspondencia</strong>, <strong>elaboración de documentos de oficina</strong> y <strong>herramientas ofimáticas</strong>. Qué significa <strong>proyectar</strong> una comunicación, la anatomía de un oficio, el <strong>Acuerdo 060 de 2001</strong>, los términos para responder una petición y su traslado por competencia, la <strong>reserva</strong> y los datos personales en las respuestas, la firma y por qué usted no firma, actas y constancias, el procesador y la hoja de cálculo como instrumentos de calidad, la <strong>radicación</strong>, la <strong>Tabla de Retención Documental</strong>, el <strong>expediente y su foliación</strong>, y qué se hace con un documento ya firmado que salió con un error.',
    badges=['⏱ 110-130 min', '📁 Gestión documental', '🖥️ Ofimática'],
    fmeta='Gestión documental, archivo, correspondencia, documentos de oficina y herramientas ofimáticas',
    cargo='Técnico en Criminalística 4TC-17 (Nivel Técnico)',
    conv='285-2026',
    alerta='Gestión documental y documentos de oficina',
)

FUENTE = 'guias/FUN-OFI-4TM16-01-comunicaciones-documentos-oficina.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- módulo nuevo
EXPEDIENTE = '''<h3>El expediente: conformación, foliación y custodia documental</h3>
  <p>La guía anterior cubre el documento individual. Este módulo cubre el conjunto, porque en una actuación lo que se valora no es un oficio aislado sino un <strong>expediente</strong>: la unidad documental que reúne, en orden, todo lo producido y recibido en un mismo asunto. Para su cargo esto importa el doble: usted <strong>aporta</strong> documentos al expediente —informes, actas, anexos— y además <strong>examina</strong> expedientes como objeto de una verificación técnica. Las dos cosas exigen conocer sus reglas.</p>
  <h4>Qué hace que un expediente sea un expediente</h4>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Atributo</th><th>Qué significa</th><th>Cómo se rompe</th></tr></thead>
      <tbody>
        <tr><td><strong>Unidad</strong></td><td>Un asunto, un expediente. Todo lo del asunto está allí y nada ajeno.</td><td>Carpetas paralelas, documentos del asunto guardados «aparte» por comodidad.</td></tr>
        <tr><td><strong>Orden</strong></td><td>Los documentos se incorporan en el orden en que se producen o reciben.</td><td>Documentos insertados fuera de secuencia, o reordenados «para que se entienda mejor».</td></tr>
        <tr><td><strong>Integridad</strong></td><td>Nada falta y nada se retira sin dejar constancia.</td><td>Folios extraídos, anexos que no llegaron, documentos prestados sin registro.</td></tr>
        <tr><td><strong>Foliación</strong></td><td>Cada folio numerado de forma consecutiva, en el mismo lugar y sin repetir ni saltar.</td><td>Números repetidos, saltos, folios en blanco numerados, foliación a lápiz y luego sobrescrita.</td></tr>
        <tr><td><strong>Trazabilidad</strong></td><td>Se puede saber quién lo tuvo, cuándo y qué hizo con él.</td><td>Préstamos sin registro, consultas no anotadas.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>La foliación: una regla técnica que da certeza</h4>
  <p>Numerar folios parece el trámite más humilde del oficio y es, en realidad, lo que permite afirmar que un expediente está completo. Por eso tiene reglas: se folia <strong>el folio, no la hoja</strong> —una hoja escrita por ambas caras son dos folios solo si ambas tienen información—, se usa un <strong>consecutivo único</strong> sin repeticiones ni saltos, se escribe en el <strong>mismo lugar</strong> de cada folio, y <strong>no se folian</strong> las hojas en blanco ni los separadores. Y la regla que más importa: una foliación equivocada <strong>no se borra ni se sobrescribe</strong>; se corrige por el procedimiento, dejando constancia de la corrección.</p>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Cuando usted examina una historia laboral para verificar los soportes de un trámite y encuentra una inconsistencia de foliación, lo que ha encontrado es un <strong>hallazgo</strong>, no un error que deba arreglar. La conducta es la misma de todo el curso: consignar con precisión qué número aparece, cuántos folios hay, dónde está el salto, e informarlo. Refoliar un expediente ajeno es alterar un documento.</p></div>
  <h4>La Tabla de Retención Documental y lo que usted produce</h4>
  <p>Ya vio la TRD como instrumento de clasificación. Añada ahora una consecuencia práctica para su cargo: los documentos que usted produce —el informe técnico, el acta de trámite, los registros de custodia— tienen una <strong>serie documental</strong> y un tiempo de retención que no los decide usted. Cuando el caso no encaja claramente en una serie, lo que corresponde no es elegir la que más se parezca, sino <strong>consultar y dejar constancia de la consulta</strong>, que es parte del propio cumplimiento del parámetro.</p>
  <div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Al recibir un expediente para examinarlo, usted cuenta 209 folios y la última foliación dice 212. La dependencia no sabe explicarlo y le pide que «lo deje cuadrado» antes de devolverlo.</p>
    <p><strong>Cómo proceder.</strong> No refolie. Consigne por escrito el número que trae la foliación, el conteo real, dónde está la diferencia y lo manifestado por la dependencia; hágalo firmar por los presentes si la entrega es en trámite, e infórmelo al competente. «Dejarlo cuadrado» convertiría una inconsistencia documentada —que es útil— en una alteración ocultada, que es un problema.</p>
  </div>
  <div class="checkpoint" data-cp="41">
    <div class="cp-q">✋ Punto de control: examina un expediente y la foliación salta del 88 al 91. ¿Qué hace?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">Refolia el expediente desde el 88 para que el consecutivo quede correcto antes de examinarlo.</button>
    <button class="cp-opt" data-ans="1">Consigna con precisión el salto, el conteo real y lo manifestado por quien lo entrega, e informa al competente: es un hallazgo, no un error que deba arreglar.</button>
    <button class="cp-opt" data-ans="0">Anota la diferencia en su libreta de campo y continúa el examen, para no retrasar el trámite.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  '''

CIERRE = '''<div class="box gold">
    <div class="box-title">💡 Idea clave del día</div>
    <p>Estos cuatro conocimientos comunes —gestión documental, archivo y correspondencia, documentos de oficina y ofimática— parecen los más modestos del temario y son los que más veces aparecen en el día a día. Y tienen un hilo único con todo lo que estudió: <strong>el documento es el único rastro de lo que ocurrió</strong>. Un oficio sin los elementos que lo identifican, una petición respondida fuera de término, un expediente mal foliado o un dato personal de más en una respuesta no son fallas de forma: son los puntos por donde se cae una actuación bien hecha.</p>
  </div>
  <div class="box ok">
    <div class="box-title">🧠 Frase para recordar</div>
    <p>«Proyecto, no firmo. Respondo en término o advierto que no alcanzo. Entrego solo lo que puedo entregar, con los datos mínimos necesarios. Y lo que encuentro mal en un documento ajeno lo consigno, no lo arreglo.»</p>
  </div>
  <div class="fuentes"><div class="fuentes-tag">📚 Fuentes oficiales para profundizar</div>
    <ul class="lista">
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=186" target="_blank" rel="noopener">Ley 594 de 2000 — Ley General de Archivos</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=41249" target="_blank" rel="noopener">Ley 1437 de 2011 (CPACA)</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=65334" target="_blank" rel="noopener">Ley 1755 de 2015 — Derecho de petición</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=56882" target="_blank" rel="noopener">Ley 1712 de 2014 — Transparencia y acceso a la información pública</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981" target="_blank" rel="noopener">Ley 1581 de 2012 — Protección de datos personales</a></li>
      <li><a href="https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1952_2019_pr003.htm" target="_blank" rel="noopener">Ley 1952 de 2019, art. 115 — Reserva de la actuación disciplinaria</a></li>
    </ul>
  </div>

  '''

SEC[2] = SEC[2].rstrip() + '\n\n  ' + EXPEDIENTE + '\n\n  ' + CIERRE + '\n'

SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>', '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>', '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('Técnico Administrativo 4TM-16', 'Técnico en Criminalística 4TC-17'),
    ('Técnico Administrativo, código 4TM-16', 'Técnico en Criminalística, código 4TC-17'),
    ('Técnico Administrativo', 'Técnico en Criminalística'),
    ('(4TM-16)', '(4TC-17)'), ('4TM-16', '4TC-17'), ('4TM16', '4TC17B'), ('4TM', '4TI'),
    ('245-2026', '285-2026'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol('Técnico en Criminalística', 'Técnicos en Criminalística'), estricto=False)

ACC = '''<details class="acc"><summary>¿Puedo responder una petición por correo electrónico?</summary><div class="acc-body"><p>Sí, cuando el peticionario indicó ese medio para recibir notificaciones o cuando la entidad lo tiene habilitado como canal. Lo que no cambia es el resto: la respuesta debe salir <strong>radicada</strong>, con los elementos de una comunicación oficial y firmada por quien tiene competencia. Un correo desde una cuenta institucional con el documento firmado adjunto es una respuesta oficial; un correo redactado en el cuerpo del mensaje, desde una cuenta personal y sin firma, no lo es.</p></div></details>
  <details class="acc"><summary>Si el peticionario pide «toda la información» del expediente, ¿debo entregarla completa?</summary><div class="acc-body"><p>No automáticamente. Se verifica primero su <strong>calidad</strong> —sujeto procesal o tercero— y después se aplica el filtro del contenido: la reserva del art. 115 del CGD mientras la actuación esté en instrucción, los documentos legalmente reservados y la protección de los datos personales de terceros. Una respuesta correcta puede ser parcial, siempre que diga <strong>qué se entrega, qué no y por qué</strong>. Lo que nunca es correcto es el silencio.</p></div></details>
  <details class="acc"><summary>¿Qué hago si detecto un error en un documento que otro firmó?</summary><div class="acc-body"><p>Lo mismo que con un hallazgo en un trámite: se informa por escrito a quien es competente, de manera objetiva y referida al punto concreto, y se deja constancia. No se corrige el documento, no se sustituye el archivo y no se comenta de palabra esperando que alguien lo arregle. El criterio del curso completo vale también aquí: <strong>documentar y poner en conocimiento, nunca reparar por cuenta propia</strong>.</p></div></details>'''
SEC[2] = SEC[2].rstrip() + "\n\n  " + ACC + "\n"

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre gestión '
              'documental y documentos de oficina: proyectar una comunicación, anatomía del oficio, derecho de '
              'petición y sus términos, traslado por competencia, reserva y datos personales, firma, actas y '
              'constancias, radicación, TRD, expediente y foliación, y corrección de documentos ya firmados.')

P = [
 (2,
  'El jefe de la Dirección está en comisión y debe salir hoy un oficio dirigido a otra entidad solicitando información para un apoyo técnico. Usted proyectó el oficio y está impecable. La secretaría le dice que lo firme usted «como quien lo elaboró», que así ha pasado otras veces y que después se formaliza. El término para la solicitud vence hoy y la entidad destinataria cierra en dos horas. Usted lleva poco tiempo en la Dirección y es la primera vez que le piden algo así.',
  '¿Cuál es la actuación correcta?',
  ['Firmar el oficio indicando expresamente que lo hace en calidad de quien lo elaboró, de modo que quede claro que la decisión de fondo no es suya sino de la Dirección.',
   'Firmar el oficio para proteger el término y solicitar que, al regreso del jefe, se expida un acto que convalide formalmente la suscripción que usted realizó por necesidad.',
   'No firmar: remitir el proyecto por el canal institucional e informar por escrito el riesgo del término, para que se disponga quién tiene competencia para suscribirlo.',
   'Enviar el oficio sin firma con una nota explicando que la firma se incorporará mañana, de modo que la solicitud quede radicada dentro del término que vence hoy.'],
  'Proyectar no es firmar: la firma es el acto por el cual alguien asume la responsabilidad de lo que el documento dice, y esa competencia no es suya. Lo que corresponde es remitir el proyecto e informar por escrito el riesgo del término.',
  'Firmar —aunque sea «como elaborador» o esperando una convalidación— es asumir una competencia ajena; y un documento sin firma no es una comunicación oficial, así que radicarlo no protege nada.'),

 (0,
  'Llega a la Dirección una petición de información sobre un apoyo técnico que la División de Gestión Humana prestó. El solicitante no es sujeto procesal y el expediente está en instrucción: no se ha formulado pliego de cargos ni se ha ordenado archivo. El jefe le pide proyectar la respuesta y el término legal corre. La petición llegó por correo certificado hace ocho días y el jefe quiere la respuesta mañana para revisarla. Nadie más en la Dirección ha atendido una petición así y el jefe confía en el proyecto que usted presente.',
  '¿Cómo debe proyectarse la respuesta?',
  ['Informando que la actuación es reservada en esa etapa conforme al art. 115 del CGD, indicando el canal y los requisitos para que un interesado legitimado la solicite, y respondiendo dentro del término.',
   'Guardando silencio hasta que el expediente deje de ser reservado, dado que cualquier respuesta sobre una actuación reservada vulneraría la reserva legal que la protege.',
   'Entregando la información solicitada, porque la Ley 1712 de 2014 consagra el acceso a la información pública como regla general y la reserva debe interpretarse restrictivamente.',
   'Trasladando la petición al despacho que lleva la investigación, sin responder al solicitante, para que sea ese despacho el que decida qué información entrega y cuándo.'],
  'La reserva no autoriza el silencio: la petición se responde dentro del término, explicando que la actuación es reservada en esa etapa e indicando el canal. Reserva y derecho de petición no se excluyen: la reserva es el límite del contenido, no una excusa para no contestar.',
  'El silencio incumple el término y puede configurar falta; entregar la información desconoce el art. 115; y trasladar sin responder deja al peticionario sin respuesta de quien la recibió.'),

 (3,
  'Una petición dirigida a la División de Gestión Humana corresponde, por su contenido, a una procuraduría regional. El jefe le pide proyectar lo que corresponda. El término general para responder ya corre y el peticionario escribió desde otra ciudad. La petición llegó al correo institucional de la Dirección y el jefe quiere el proyecto hoy mismo para firmarlo. El peticionario anunció que insistirá si no recibe respuesta y el jefe quiere evitar una queja.',
  '¿Qué debe proyectarse?',
  ['Una respuesta de fondo elaborada con la información que la Dirección tenga disponible, aunque el asunto no sea de su competencia, para no dejar al peticionario sin respuesta.',
   'Un archivo de la petición por falta de competencia, con constancia en el expediente, dado que la Dirección no puede pronunciarse sobre asuntos ajenos a sus funciones.',
   'Una devolución de la petición al interesado explicándole que debe dirigirla a la dependencia competente, con la indicación de cuál es y de cómo puede ubicarla.',
   'El traslado de la petición a la dependencia competente dentro del término previsto, informando de ello al peticionario y precisando a quién fue remitida.'],
  'Cuando la petición no es de la competencia de quien la recibe, lo que procede es el traslado a la dependencia competente dentro del término, informando al peticionario a quién se remitió. No se archiva ni se devuelve.',
  'Responder de fondo un asunto ajeno excede la competencia; archivar deja la petición sin trámite; y devolverla al interesado le traslada una carga que la ley pone en la entidad.'),

 (1,
  'Usted proyecta la respuesta a una petición y advierte que, para explicar el trámite, el borrador incluye el nombre, la cédula, la dirección y el teléfono de un tercero que aparece en el expediente. Nada de eso es necesario para responder lo que se preguntó. El término vence mañana. El tercero no tiene relación alguna con lo que el peticionario preguntó y el jefe revisa el borrador mañana. El peticionario preguntó únicamente por el estado del trámite, nada sobre personas.',
  '¿Qué corresponde hacer?',
  ['Mantener los datos, porque obran en el expediente y suprimirlos podría dejar la respuesta incompleta frente a lo que el peticionario efectivamente consultó.',
   'Suprimir los datos del tercero que no son necesarios para responder lo preguntado, aplicando el principio de minimización, y dejar la respuesta ceñida a su finalidad.',
   'Mantener los datos pero advertir al peticionario que no puede divulgarlos, dejando constancia de esa advertencia en el cuerpo de la respuesta que se remite.',
   'Reemplazar los datos por las iniciales del tercero y los últimos dígitos de su documento, de modo que la respuesta quede completa sin identificarlo plenamente.'],
  'El principio de minimización exige tratar solo los datos necesarios para la finalidad que los justifica. Si la respuesta no requiere identificar al tercero, esos datos no van, y ninguna advertencia al peticionario repara su divulgación.',
  'Mantenerlos con o sin advertencia ya los divulga; y las iniciales con los últimos dígitos siguen identificando a una persona en un universo pequeño.'),

 (2,
  'Un oficio que usted proyectó y que el jefe firmó salió con un error: el número de radicado del expediente al que se refiere está equivocado, de modo que la entidad destinataria no podrá ubicarlo. El oficio ya fue radicado y enviado hace dos días. Nadie ha reclamado todavía. La entidad destinataria no ha acusado recibo y usted conserva el borrador original con el radicado correcto. El jefe que lo firmó está en comisión y regresa la próxima semana a la Dirección.',
  '¿Cuál es la actuación correcta?',
  ['Reimprimir el oficio con el radicado correcto, hacerlo firmar de nuevo y enviarlo con el mismo número de radicación, de modo que sustituya al anterior sin dejar rastro del error.',
   'No hacer nada hasta que la entidad destinataria reclame, momento en el cual se enviará la aclaración correspondiente con el número correcto del expediente.',
   'Informar por escrito el error al jefe y proyectar la comunicación aclaratoria que corresponda, dejando constancia del error y de la corrección en el expediente.',
   'Enviar un correo electrónico informal a la entidad destinataria con el radicado correcto, para resolver el problema sin generar un trámite documental adicional.'],
  'Un documento ya firmado y radicado no se sustituye: se corrige por el procedimiento, con una comunicación aclaratoria y constancia del error y de la corrección. Así la trazabilidad queda completa en lugar de borrada.',
  'Sustituir el documento con el mismo radicado destruye la trazabilidad; esperar el reclamo deja correr el error; y un correo informal no corrige una comunicación oficial.'),

 (0,
  'Debe levantar el acta de una reunión en la que se acordó la metodología de un apoyo técnico. Durante la reunión hubo una discusión en la que dos participantes discreparon abiertamente y uno de ellos pide que «eso no quede en el acta, que al final se acordó lo mismo». La reunión fue esta mañana, asistieron seis personas y el acta debe quedar lista hoy para la firma de los asistentes. Dos de los asistentes ya preguntaron cuándo podrán revisar el borrador del acta.',
  '¿Cómo debe elaborarse el acta?',
  ['Consignando lo tratado y lo acordado con fidelidad, incluida la existencia de las posiciones discrepantes y la decisión final, sin transcribir la discusión palabra por palabra.',
   'Consignando únicamente el acuerdo final, dado que es lo que produce efectos y la discusión previa no tiene relevancia para la ejecución del apoyo técnico acordado.',
   'Transcribiendo íntegramente la discusión, incluidas las intervenciones textuales de los participantes, para que el acta refleje con exactitud todo lo ocurrido en la reunión.',
   'Consignando el acuerdo final y atendiendo la petición del participante, dejando constancia aparte, en un documento interno, de que hubo posiciones discrepantes.'],
  'El acta es memoria fiel de lo tratado y lo acordado: debe reflejar que hubo posiciones distintas y cuál fue la decisión, sin convertirse en una transcripción. Una petición de un participante no define el contenido del acta.',
  'Consignar solo el acuerdo borra información relevante; transcribir todo desnaturaliza el acta; y repartir el contenido en dos documentos deja la memoria incompleta donde se consulta.'),

 (3,
  'Le piden expedir una constancia de que un expediente fue entregado a la Dirección en una fecha determinada. Usted no participó en esa entrega y lo que tiene es el registro del sistema, que muestra la fecha pero no quién entregó físicamente el expediente. La solicitud llegó por escrito y la respuesta debe salir esta semana con la firma del jefe de la Dirección. Quien la solicita la necesita para un trámite ante otra entidad y la pide para hoy.',
  '¿Cuál es la actuación correcta?',
  ['Expedir la constancia con la fecha que muestra el sistema, que es el registro oficial de la entidad y basta para acreditar el hecho que se solicita certificar.',
   'Negarse a expedir cualquier tipo de constancia, porque usted no presenció el hecho y dar fe de algo que no observó compromete directamente su responsabilidad personal.',
   'Expedir la constancia señalando el nombre de quien, según sus compañeros, hizo la entrega, de modo que el documento quede completo y plenamente útil.',
   'Expedir la constancia precisando exactamente qué acredita —lo que el registro del sistema muestra— y qué no, sin afirmar hechos que no presenció.'],
  'Dar fe es un acto de responsabilidad: la constancia certifica exactamente lo que se puede verificar, y lo dice con esa precisión. No se niega la constancia, pero tampoco se extiende a hechos que no se pueden acreditar.',
  'Expedirla sin precisar su alcance afirma más de lo que se verificó; negarse desatiende una solicitud legítima; e incorporar lo que dicen los compañeros certifica un hecho de oídas.'),

 (1,
  'Está organizando los documentos de un apoyo ya concluido y debe archivarlos. La TRD de la dependencia tiene dos series parecidas y ninguna coincide exactamente con el caso, que mezcla soporte técnico y actuación disciplinaria. El término para dejar el archivo organizado vence el viernes y la persona encargada está incapacitada. El apoyo se concluyó hace un mes y los documentos están sobre su escritorio, sin clasificar todavía.',
  '¿Cuál es la actuación correcta?',
  ['Archivar en la serie de mayor tiempo de retención, porque conservar más tiempo un documento nunca causa perjuicio y evita el riesgo de una eliminación anticipada.',
   'Consultar por el canal institucional al responsable de gestión documental o a quien lo supla, dejar constancia escrita de la consulta y archivar conforme a la orientación recibida.',
   'Archivar en la serie que más se parezca y anotar en la carpeta una nota con la duda, de modo que quien revise después pueda reclasificar el documento si lo estima necesario.',
   'Crear una serie nueva que describa con precisión este tipo de caso y proponer después su incorporación formal a la Tabla de Retención Documental de la dependencia.'],
  'La TRD exige criterio, no adivinanza: ante un caso que no encaja, se consulta por el canal, se deja constancia de la consulta y se actúa conforme a la orientación. La constancia de la consulta es parte del cumplimiento del parámetro.',
  'Elegir la más parecida o la de mayor retención son decisiones unilaterales sobre un instrumento que usted no modifica; y crear una serie nueva lo es con más razón.'),

 (0,
  'Al recibir un expediente para examinarlo, usted cuenta 209 folios y la última foliación dice 212. La dependencia no sabe explicarlo y le pide que «lo deje cuadrado» antes de devolverlo, porque de lo contrario «va a parecer que perdieron folios». Hay dos personas más presentes en la entrega y el examen está programado para esta misma tarde. La dependencia insiste en que el expediente está completo y que el conteo debe estar mal.',
  '¿Cuál es la actuación correcta?',
  ['Consignar por escrito el número que trae la foliación, el conteo real, dónde está la diferencia y lo manifestado por la dependencia, e informarlo al servidor competente.',
   'Refoliar el expediente con el número real de folios, de modo que el documento quede internamente consistente antes de que el examen técnico se practique sobre él.',
   'Devolver el expediente sin examinarlo y solicitar que la dependencia aclare previamente la diferencia, dejando constancia de que el examen quedó pendiente de esa aclaración.',
   'Examinarlo y consignar el número que trae la foliación, por ser el dato oficial del documento, verificando el conteo con más calma antes de rendir el informe.'],
  'Una inconsistencia de foliación en un expediente ajeno es un hallazgo, no un error que usted deba arreglar. Se consigna con precisión, se deja constancia de lo manifestado y se informa: refoliar sería alterar un documento.',
  'Refoliar altera el expediente; devolverlo sin examinar paraliza una actuación posible; y consignar solo el dato oficial oculta la diferencia que usted detectó.'),

 (2,
  'Debe remitir un informe técnico con anexos digitales que suman más de lo que el canal institucional admite. El despacho destinatario lo necesita hoy. Un compañero le sugiere comprimir todo y enviarlo desde su correo personal, «que es más rápido y total el contenido es el mismo». El informe está firmado y los anexos digitales pesan el triple de lo que el canal admite por envío. El despacho destinatario tiene audiencia mañana y llama cada hora preguntando por el envío.',
  '¿Cuál es la actuación correcta?',
  ['Enviarlo desde el correo personal y dejar constancia en el informe de que el envío se hizo por esa vía debido a la limitación técnica del canal institucional.',
   'Fraccionar el anexo en varios archivos y enviarlos por separado por el canal institucional, aunque ello implique dividir un documento único en partes que deban recomponerse.',
   'Remitir el informe por el canal institucional, gestionar por el canal interno la entrega del anexo extenso, e informar al despacho ambas cosas dejando constancia.',
   'Entregar el anexo en medio físico directamente al servidor del despacho y remitir solo el informe por el canal, sin registrar la entrega del medio físico.'],
  'El canal institucional da trazabilidad y no se sustituye por uno personal. La necesidad real se atiende por una vía compatible y todo queda informado y con constancia.',
  'Un correo personal rompe la trazabilidad por mucha urgencia que haya; fraccionar un documento único lo degrada; y una entrega física sin registro, para el expediente, no ocurrió.'),

 (3,
  'Usted elabora una hoja de cálculo para llevar el control de los apoyos de la Dirección: fechas de solicitud, delegación, práctica, rendición y términos. Un compañero le dice que es trabajo perdido, «porque el sistema institucional ya lleva eso y duplicar información genera inconsistencias». Usted elaboró la hoja esta semana y ya le sirvió para anticipar dos vencimientos del grupo. El compañero lo plantea delante del grupo en la reunión semanal de seguimiento.',
  '¿Cuál es la precisión correcta?',
  ['Tiene razón: llevar un control paralelo duplica la información y crea el riesgo de que los dos registros no coincidan, lo que resta credibilidad al trabajo del grupo.',
   'Tiene razón solo si el sistema institucional está actualizado; mientras no lo esté, el control propio sustituye al oficial y prevalece sobre él para efectos de reporte.',
   'Se equivoca: el control propio reemplaza al sistema institucional cuando resulta más completo, y en ese caso debe reportarse a partir de la hoja de cálculo elaborada.',
   'El control propio es una herramienta de trabajo legítima para anticipar vencimientos, siempre que el registro oficial sea el del sistema y no se reporte a partir del propio.'],
  'Un control propio para anticipar vencimientos es buena práctica de organización del trabajo. Lo que no puede ocurrir es que sustituya al registro oficial o que se reporte a partir de él: el dato institucional es el del sistema.',
  'Ni es trabajo perdido, ni el control propio prevalece o sustituye al oficial por estar más completo: convive con él como herramienta de anticipación.'),

 (1,
  'El despacho le pide que proyecte un oficio usando una plantilla que un compañero elaboró hace dos años y que no corresponde al formato institucional vigente. Le dicen que es la que siempre se usa en el grupo y que nadie ha tenido problemas con ella. El oficio debe salir pasado mañana y el formato institucional está publicado en el repositorio interno. El compañero que elaboró la plantilla ya no trabaja en la Dirección y nadie la ha revisado.',
  '¿Cuál es la actuación correcta?',
  ['Usar la plantilla del grupo, que es la práctica consolidada de la dependencia, y plantear la inquietud sobre el formato en la próxima reunión del equipo de trabajo.',
   'Usar el formato institucional vigente y, si considera que la plantilla del grupo es mejor, proponer su adopción por escrito al superior con el sustento correspondiente.',
   'Usar la plantilla del grupo y ajustar manualmente los elementos que el formato institucional exige, de modo que el documento cumpla con ambos requerimientos a la vez.',
   'Consultar al jefe inmediato y usar la plantilla que él indique verbalmente, aunque difiera del formato institucional publicado en el repositorio de la entidad.'],
  'El formato institucional vigente prevalece sobre la costumbre, por consolidada que esté. La iniciativa se canaliza como propuesta por escrito, no como excepción propia.',
  'Una costumbre del grupo no deroga un formato adoptado; «ajustar manualmente» produce un documento híbrido; y una instrucción verbal no desplaza un formato publicado.'),

 (0,
  'Una petición pide copia de un documento que obra en una actuación disciplinaria. El peticionario acredita ser apoderado reconocido del investigado. El expediente está en instrucción. El jefe le pide proyectar la respuesta y el término corre. El poder obra en el expediente y el término para responder vence en cuatro días hábiles. El apoderado llegó personalmente a la Dirección y espera respuesta sobre el trámite. Es la primera solicitud de copias que llega a la Dirección en ese expediente.',
  '¿Cómo debe proyectarse?',
  ['Verificando la calidad procesal acreditada y, confirmada, dando trámite al acceso conforme al procedimiento, porque la reserva no se opone a los derechos de los sujetos procesales.',
   'Negando el acceso por estar la actuación en instrucción, etapa en la que el art. 115 del CGD establece la reserva de las actuaciones disciplinarias sin excepciones.',
   'Entregando copia del documento de inmediato y sin verificación adicional, dado que el peticionario manifestó ser apoderado del investigado en la actuación disciplinaria.',
   'Trasladando la petición a la Procuraduría Auxiliar para Asuntos Disciplinarios, que es la dependencia competente para resolver sobre el acceso a expedientes en instrucción.'],
  'La reserva del art. 115 opera «sin perjuicio de los derechos de los sujetos procesales»: acreditada la calidad, el acceso se tramita por el procedimiento. Verificar primero y tramitar después es la secuencia correcta.',
  'Negar por la etapa desconoce la salvedad expresa de la norma; entregar sin verificar omite el paso previo indispensable; y no hay traslado que corresponda: la petición se tramita donde se recibió.'),

 (2,
  'Usted debe responder una petición cuyo término vence en dos días, pero la información que se requiere está en una dependencia que aún no ha contestado su requerimiento interno. Sin ese insumo no puede elaborarse una respuesta de fondo. La dependencia requerida no responde correos desde la semana pasada y el peticionario ya preguntó por el avance. El término no admite prórroga y usted ya requirió la información por escrito dos veces.',
  '¿Cuál es la actuación correcta?',
  ['Responder dentro del término con la información disponible, sin mencionar que falta el insumo, para no exponer una demora interna de la entidad ante el peticionario.',
   'Esperar el insumo y responder cuando esté completo, dado que una respuesta parcial no satisface el derecho de petición y podría generar una nueva solicitud del interesado.',
   'Proyectar, dentro del término, la comunicación que informe al peticionario la situación y el plazo en que se dará respuesta de fondo, y reiterar por escrito el requerimiento interno.',
   'Responder dentro del término indicando que la petición fue trasladada por competencia a la dependencia que tiene la información requerida por el peticionario.'],
  'El término no se incumple en silencio: se responde informando la situación y el plazo en que se resolverá de fondo, y se reitera el requerimiento interno. Así se cumple el deber y se protege al peticionario.',
  'Callar la carencia da una respuesta incompleta como si fuera completa; esperar incumple el término; y hablar de traslado por competencia es falso: la petición sí es de la Dirección.'),

 (3,
  'Es el último día de contenido. Usted revisa su desempeño y nota que en este bloque falla las preguntas donde la opción correcta implica un trámite más —informar, dejar constancia, consultar— frente a la que resuelve el asunto de una vez. Su registro muestra ese patrón en cinco de los últimos siete casos de este bloque. Lleva un registro de los simulacros resueltos y puede ver exactamente qué opción eligió cada vez que falló.',
  '¿Cuál es la mejor manera de corregirlo antes del simulacro final?',
  ['Memorizar los términos del derecho de petición y los elementos del oficio, que son los contenidos que más preguntas generan dentro de este bloque del temario.',
   'Resolver el simulacro final y confiar en que los veinte días de práctica acumulada corrijan el patrón sin un ajuste deliberado del criterio de elección.',
   'Concentrarse en las preguntas de gestión documental, que son las que más falla, y repasar lo demás con los resúmenes y las listas de verificación de las guías.',
   'Retener que el trámite no es burocracia: la constancia, el informe y la consulta son lo que deja rastro. Lo que resuelve sin dejar rastro es el distractor.'],
  'El patrón se corrige entendiendo por qué el trámite está ahí: el documento es el único rastro de lo que ocurrió. Una solución que no deja rastro resuelve hoy y no se puede acreditar mañana.',
  'Memorizar términos no cambia el criterio de elección; confiar en la práctica acumulada repite el patrón; y concentrarse en un solo tema deja fuera los demás a un día del simulacro.'),
]
