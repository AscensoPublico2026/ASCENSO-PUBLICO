# -*- coding: utf-8 -*-
"""Día 13 · CPACA III: motivación, revocatoria, términos, publicidad y el concepto frente al acto."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol
from _brenda import IDENTIDAD, CARGO, PLURAL, meta

META = meta(
    codigo='FUN-CPACA-4TC17B-03',
    archivo='FUN-CPACA-4TC17B-03-motivacion-revocatoria-terminos-conceptos.html',
    dia=13,
    titulo_doc='CPACA III: motivación, revocatoria, términos, publicidad y el concepto frente al acto',
    h1='CPACA III<br>Motivación, revocatoria, términos y el concepto frente al acto',
    kicker='Día 13 · Conocimiento específico',
    sub='Cierra el bloque de CPACA con lo más práctico de todo: cómo se <strong>motiva</strong> un acto para que resista, la <strong>revocatoria directa</strong> y sus causales, cómo se <strong>cuentan los términos</strong> y qué pasa si se incumplen, las <strong>peticiones verbales, anónimas y presentadas por terceros</strong>, la <strong>remisión por falta de competencia</strong>, la <strong>corrección, aclaración y adición</strong> de los actos, la <strong>publicidad</strong> y el acceso al expediente, los <strong>medios de control judicial</strong> y dónde termina exactamente tu rol, y la diferencia entre un <strong>concepto</strong> y un <strong>acto administrativo</strong>. Es el día de las buenas prácticas de redacción jurídico-administrativa.',
    badges=['⏱ 100-120 min', '⚖️ CPACA', '📖 Específico'],
    fmeta='CPACA III: motivación, revocatoria, términos, publicidad y conceptos (Ley 1437 de 2011 y Ley 1755 de 2015)',
    alerta='CPACA III: motivación, revocatoria, términos, publicidad y el concepto frente al acto',
)

S = secciones_mapeadas('guias/FUN-JUR-4SU11-01-cpaca-procedimiento-administrativo.html')

CIERRE = '''
      <div class="modulo-head"><div class="modulo-n">★</div><h3>Cómo se escribe un acto de personal que resiste</h3></div>
      <div class="b-texto">
        <p>Después de tres días de CPACA, lo que queda es un oficio concreto: saber escribir. Casi todos los defectos que anulan un acto de personal no nacen de una mala decisión, sino de un documento mal hecho. Esta es la estructura mínima que debe tener todo lo que usted proyecte.</p>
        <div class="tabla-wrap"><table>
          <thead><tr><th>Parte</th><th>Qué debe contener</th><th>Error típico</th></tr></thead>
          <tbody>
            <tr><td><strong>Encabezado</strong></td><td>Identificación del acto, número y fecha, y la autoridad que lo expide.</td><td>Señalar como expedidor a quien no tiene la competencia del asunto.</td></tr>
            <tr><td><strong>Competencia</strong></td><td>La norma que faculta a quien firma: arts. 62 o 63 del Decreto Ley 262 de 2000, según el asunto.</td><td>Citar una norma genérica que no dice quién decide esto en concreto.</td></tr>
            <tr><td><strong>Hechos</strong></td><td>Qué se pidió, cuándo se radicó, qué soportes se aportaron y qué se verificó.</td><td>Saltar directo a la conclusión sin dejar rastro de lo verificado.</td></tr>
            <tr><td><strong>Fundamentos</strong></td><td>Las normas aplicadas y, sobre todo, <strong>por qué</strong> se aplican a estos hechos.</td><td>Transcribir artículos sin conectarlos con el caso: eso no es motivar.</td></tr>
            <tr><td><strong>Decisión</strong></td><td>Qué se resuelve, de manera clara, precisa y <strong>congruente</strong> con lo pedido.</td><td>Resolver una parte y callar las demás, o decidir algo que nadie pidió.</td></tr>
            <tr><td><strong>Recursos</strong></td><td>Cuáles proceden, ante quién y en qué término (cuando el acto es susceptible de ellos).</td><td>Omitirlos: la notificación queda irregular y el término no corre.</td></tr>
            <tr><td><strong>Notificación</strong></td><td>Cómo se notifica o comunica y la constancia de su fecha.</td><td>Dar el acto por surtido sin constancia alguna de su comunicación.</td></tr>
          </tbody>
        </table></div>
        <div class="ojo"><b>Ojo en la prueba:</b> distingue siempre el <mark>concepto</mark> del <mark>acto administrativo</mark>. Un <strong>concepto</strong> responde una consulta, orienta y <strong>no obliga</strong> ni compromete la responsabilidad de quien lo emite. Un <strong>acto administrativo</strong> crea, modifica o extingue una situación jurídica: obliga, se notifica, admite recursos y adquiere firmeza. Un error frecuente, y grave, es resolver con un concepto algo que exigía un acto —o al revés—. Si lo que la persona pide es que se decida su situación, no se le responde con una opinión.</div>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Un jefe consulta por escrito si puede encargar a un servidor que no acredita uno de los requisitos. Usted proyecta la respuesta: es un <strong>concepto</strong>, porque se pide una opinión sobre una materia a cargo de la dependencia, y así debe decirlo el propio documento —orienta, no obliga—. Si en cambio el jefe hubiera radicado la solicitud de encargo con sus soportes, lo que procede es un <strong>acto administrativo</strong>: motivado, firmado por el competente, notificado, con indicación de recursos. Confundir los dos caminos tiene consecuencias reales: un concepto favorable nunca habilita una posesión.</p>
          </div>
        </div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> un acto de personal que resiste tiene siempre las mismas siete partes —encabezado, competencia, hechos, fundamentos, decisión, recursos y notificación— y falla casi siempre por las mismas razones: competencia mal citada, motivación que transcribe en vez de explicar, decisión incongruente con lo pedido y notificación sin constancia. Y antes de escribir hay una pregunta previa: ¿esto es un <strong>concepto</strong> que orienta o un <strong>acto</strong> que decide? De esa respuesta depende todo lo demás.</p></div>
        <div class="box ok"><div class="box-title">💡 Idea clave del día</div><p><strong>Idea clave:</strong> motivar no es citar. Un acto está motivado cuando quien lo lee puede reconstruir el razonamiento: estos hechos, probados con estos soportes, encajan en esta norma, y por eso se resuelve así. Esa es, además, la única forma de que el interesado pueda controvertirlo, que es justamente para lo que sirve la motivación.</p></div>
        <div class="acordeon">
          <details class="acc"><summary>🔎 ¿Cuándo un documento es un concepto y cuándo es un acto administrativo?</summary><div class="acc-body"><p>La pregunta no se resuelve por el título del documento sino por lo que hace. Un <strong>concepto</strong> responde una consulta: expresa una opinión sobre una materia a cargo de la dependencia, <strong>orienta</strong> y, por disposición expresa del CPACA, <strong>no es de obligatorio cumplimiento ni compromete la responsabilidad</strong> de quien lo emite. Un <strong>acto administrativo</strong> <strong>crea, modifica o extingue una situación jurídica</strong>: obliga, se notifica, admite recursos y adquiere firmeza. El test práctico es sencillo: ¿después de este documento, la situación de alguien cambió? Si cambió, era un acto.</p></div></details>
          <details class="acc"><summary>🔎 ¿Corrección, aclaración o adición?</summary><div class="acc-body"><p>Tres figuras que la prueba confunde a propósito. La <strong>corrección</strong> arregla errores <em>formales</em> —de transcripción, aritméticos, de cálculo— y procede en cualquier tiempo, de oficio o a petición de parte, <strong>sin alterar el sentido material</strong> de la decisión. La <strong>aclaración</strong> precisa un punto <em>oscuro o ambiguo</em> del acto, sin cambiar lo decidido. La <strong>adición</strong> resuelve un punto que <em>debió decidirse y se omitió</em>. Ninguna de las tres sirve para cambiar la decisión: para eso están los recursos y la revocatoria directa.</p></div></details>
          <details class="acc"><summary>🔎 ¿Hasta dónde llega el rol del técnico frente a los medios de control judicial?</summary><div class="acc-body"><p>Hasta informar, y ni un paso más. Usted puede y debe <strong>informar</strong> que, además de los recursos, existen medios de control ante la jurisdicción de lo contencioso administrativo. Lo que no le corresponde es <strong>recomendar</strong> una vía, anticipar si prosperará o valorar los argumentos del interesado: él es parte en un asunto en el que la entidad también lo es, y asesorarlo comprometería la imparcialidad. Si pide asesoría, la orientación correcta es que acuda a un abogado o a los servicios de asistencia jurídica gratuita.</p></div></details>
        </div>
        <div class="fuentes">
          <h4>📚 Fuentes para verificar</h4>
          <ul>
            <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=41249" target="_blank" rel="noopener">Ley 1437 de 2011 (CPACA)</a> — procedimiento administrativo, notificaciones, recursos, revocatoria y silencio.</li>
            <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=65334" target="_blank" rel="noopener">Ley 1755 de 2015</a> — derecho de petición.</li>
            <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=40618" target="_blank" rel="noopener">Decreto Ley 262 de 2000</a> — estructura y funciones de la PGN (arts. 2, 62 y 63).</li>
            <li><a href="http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991.html" target="_blank" rel="noopener">Constitución Política</a> — arts. 23, 29 y 209.</li>
          </ul>
        </div>
        <div class="box ojo"><div class="box-title">🗣️ Frase para recordar</div><p>«El concepto orienta y no obliga; el acto decide, se notifica, admite recursos y queda en firme. Nunca se resuelve con el uno lo que exigía el otro. — Día 13»</p></div>
      </div>
'''
S[2] = S[2] + CIERRE
SEC = aplicar_todas(S, IDENTIDAD + [
    ('4SU-11', '4TC-17'), ('4SU11', '4TC17'),
    ('Convocatoria 288-2026', 'Convocatoria 285-2026'), ('288-2026', '285-2026'),
    ('Resolución 243 de 2026', 'Resolución 212 de 2026'),
    ('tu función 8', 'tu función 7'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(CARGO, PLURAL), estricto=False)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre motivación, '
              'revocatoria directa, conteo de términos, publicidad, corrección de actos, medios de control y la '
              'diferencia entre un concepto y un acto administrativo.')

P = [
 (2,
  'Un jefe de dependencia le envía por correo una consulta escrita: quiere saber si puede encargar en un empleo del nivel técnico a una servidora que no acredita uno de los requisitos del manual. Usted estudia el caso y concluye que no procede. Al proyectar la respuesta, un compañero le sugiere que la redacte como un acto administrativo «para que quede claro que no se puede y no vuelvan a insistir», con parte resolutiva y todo. El jefe, por su parte, dice que si la respuesta es favorable procederá con el encargo de una vez.',
  '¿Qué documento corresponde y qué debe advertirse?',
  ['Un acto administrativo con parte resolutiva, porque la respuesta define si el encargo procede o no y esa definición produce efectos jurídicos sobre la servidora involucrada en el caso.',
   'Un acto administrativo, pero sin indicación de recursos, porque la consulta la formuló un jefe de dependencia y no la persona directamente interesada en el resultado del trámite.',
   'Un concepto, que orienta y no obliga ni compromete la responsabilidad de quien lo emite, y debe advertirse que un concepto favorable no habilita por sí solo a surtir el encargo.',
   'Una comunicación informal por el mismo correo, porque las consultas entre dependencias de la misma entidad no requieren documento formal ni quedan sujetas a términos de respuesta.'],
  'Correcto. Lo que se pide es una <strong>opinión sobre una materia a cargo de la dependencia</strong>: eso es una <strong>consulta</strong>, y se responde con un <strong>concepto</strong>, que orienta y no obliga. Y la advertencia es esencial, porque el jefe anunció que actuaría con la respuesta: un concepto no habilita un encargo; para eso hace falta la solicitud con sus soportes y el acto del competente.',
  'Darle forma de acto administrativo a un concepto crea la apariencia de una decisión que nadie adoptó. Un acto sin indicación de recursos sería además irregular. Y tratarlo como comunicación informal desconoce que una consulta escrita es una petición con su propio término.'),

 (0,
  'Al revisar un proyecto de acto que niega una solicitud, usted encuentra que la parte motiva transcribe cuatro artículos completos del CPACA y del Decreto 1083, seguidos de la frase «en consecuencia, se niega lo solicitado». No hay un solo párrafo que explique qué hechos se probaron ni por qué esas normas conducen a negar. El compañero que lo proyectó dice que «citando la norma ya está motivado» y que agregar explicaciones solo le daría argumentos al interesado. El acto debe firmarse mañana y el interesado ya anunció que lo recurrirá.',
  '¿Cuál es la observación correcta?',
  ['Transcribir normas no es motivar: el acto debe exponer qué hechos se probaron, con qué soportes, y por qué esas normas aplicadas a esos hechos conducen a la decisión que se adopta.',
   'El proyecto está bien motivado porque identifica con precisión el fundamento normativo, que es lo que la ley exige, y añadir razones adicionales expondría innecesariamente a la entidad.',
   'Basta con reducir las transcripciones a los apartes pertinentes de cada artículo, porque el exceso de citas dificulta la lectura pero no afecta la validez de la motivación del acto.',
   'La motivación solo es exigible cuando el acto es favorable al interesado, de modo que en una negativa basta con invocar la norma que sustenta la decisión que se está adoptando.'],
  'Correcto. <strong>Motivar no es citar</strong>: es permitir que quien lee reconstruya el razonamiento —estos hechos, probados así, encajan en esta norma, y por eso se resuelve de este modo—. Y la razón de fondo es práctica: sin motivación el interesado no puede controvertir, que es justamente para lo que sirve.',
  'Identificar la norma es necesario pero no suficiente. Recortar las citas mejora la lectura pero no agrega razonamiento. Y es al revés de lo que dice la última opción: la motivación es especialmente exigible cuando la decisión es desfavorable.'),

 (3,
  'Una petición fue radicada el jueves 30 de abril a las 3 de la tarde. El viernes 1 de mayo es festivo. Un compañero le dice a usted que el término empieza el mismo jueves y que se cuentan días calendario. Otro, que empieza el lunes porque el jueves «ya estaba muy avanzado». La peticionaria llama y pide una fecha exacta para saber cuándo puede insistir, y advierte que de esa fecha depende un trámite suyo ante otra entidad.',
  '¿Cómo deben contarse los términos?',
  ['Desde el mismo jueves 30, en días calendario, descontando únicamente el festivo del 1 de mayo por tratarse de un día en que la entidad no presta atención al público.',
   'Desde el lunes siguiente, en días hábiles, porque una radicación hecha en horas de la tarde se entiende presentada el primer día hábil siguiente al de su recepción material.',
   'Desde el mismo jueves 30, en días hábiles, de modo que ese jueves cuenta como el primer día del término y el festivo del 1 de mayo simplemente no se computa.',
   'Desde el día hábil siguiente a la radicación, en días hábiles, excluyendo sábados, domingos y festivos: el jueves 30 no cuenta y el 1 de mayo tampoco.'],
  'Correcto. Dos reglas que van juntas: el término se cuenta en <strong>días hábiles</strong> y empieza el <strong>día hábil siguiente</strong> al de la radicación. El día de la radicación no cuenta, y sábados, domingos y festivos se excluyen. Darle a la peticionaria una fecha exacta y correcta es parte de atenderla bien.',
  'Contar días calendario acorta el plazo real. La hora de radicación no desplaza la fecha: lo presentado dentro del horario se radica ese día. Y contar el propio día de radicación adelanta indebidamente el vencimiento.'),

 (1,
  'Una servidora solicita la revocatoria directa de un acto que quedó en firme hace ocho meses y que, según ella, se expidió con una interpretación equivocada de la norma. Un compañero le dice a usted que la figura «no existe para los interesados, solo la administración puede revocar de oficio». Otro, que la sola presentación de la solicitud reabre el término para demandar el acto ante la jurisdicción. La servidora pregunta qué efectos tiene presentarla.',
  '¿Cuál es la orientación correcta?',
  ['La revocatoria directa solo procede de oficio: la servidora no está legitimada para solicitarla y su única alternativa es acudir directamente ante la jurisdicción de lo contencioso administrativo.',
   'Puede solicitarla, pero procede solo si se configura una de las causales legales, y debe advertírsele que presentarla no revive los términos para acudir ante la jurisdicción.',
   'Puede solicitarla por cualquier motivo y su presentación suspende los efectos del acto mientras la entidad resuelve, de modo que la situación vuelve al estado anterior a su expedición.',
   'No procede en ningún caso porque el acto quedó en firme hace más de seis meses, término máximo dentro del cual la administración puede volver sobre sus propias decisiones ya ejecutoriadas.'],
  'Correcto. La <strong>revocatoria directa</strong> puede pedirla el interesado, pero solo prospera si se configura una <strong>causal legal</strong> —y «una interpretación equivocada» no es cualquier desacuerdo—. Y hay que advertirle lo más importante: <strong>no revive los términos</strong> para demandar. Muchas personas pierden la vía judicial por creer lo contrario.',
  'No es una facultad exclusivamente oficiosa. No procede por cualquier motivo ni suspende los efectos del acto. Y no existe ese plazo de seis meses para que la administración revoque.'),

 (2,
  'Llega una petición presentada por una persona a nombre de otra: una hija radica, por su padre adulto mayor que no puede desplazarse, una solicitud de certificación laboral. Trae copia de la cédula del padre y un escrito firmado por él, pero no un poder. Un compañero propone rechazarla por falta de poder y otro, entregarle la certificación a la hija de una vez, «porque es evidente que el padre la autorizó al firmar». El padre tiene 84 años y la certificación la necesita para un trámite pensional.',
  '¿Cuál es la actuación correcta?',
  ['Rechazar la petición porque actuar a nombre de otro ante una autoridad exige poder, y sin él la hija carece por completo de legitimación para presentar la solicitud de su padre.',
   'Entregar la certificación a la hija de inmediato, porque el escrito firmado por el padre y la copia de su documento acreditan suficientemente su voluntad de solicitar y recibir el documento.',
   'Radicar la petición, que es del padre y está firmada por él, verificar qué exige el procedimiento para la entrega del documento a un tercero y responder de fondo dentro del término.',
   'Devolver el escrito indicando que el padre debe presentarse personalmente, porque una certificación laboral solo puede entregarse a su titular previa verificación directa de su identidad.'],
  'Correcto. Conviene separar dos cosas que la pregunta mezcla: <strong>quién pide</strong> y <strong>a quién se entrega</strong>. La petición es del padre y está firmada por él: se radica y se responde. La entrega a un tercero es lo que debe verificarse conforme al procedimiento, sin convertir eso en una barrera para radicar.',
  'Rechazar por falta de poder desconoce que el escrito es del titular. Entregar sin verificar nada expone un dato personal. Y exigir la comparecencia personal de un adulto mayor que no puede desplazarse es precisamente el trato que el CPACA quiere evitar.'),

 (0,
  'Un acto administrativo de personal quedó con un error en la liquidación de un valor: se sumó mal una cifra, aunque todos los conceptos y la decisión son correctos. El acto ya fue notificado. Un compañero propone revocarlo y expedir uno nuevo; otro, dejarlo así y ajustar la diferencia en la nómina sin tocar el documento. El interesado todavía no ha advertido el error, y el acto ya quedó archivado en su historia laboral con la cifra equivocada.',
  '¿Cuál es la actuación correcta?',
  ['Proyectar la corrección del error aritmético, que procede en cualquier tiempo, de oficio o a petición de parte, siempre que no se altere el sentido material de la decisión adoptada.',
   'Proyectar la revocatoria del acto y expedir uno nuevo con la cifra correcta, porque cualquier error numérico afecta la validez del acto y exige retirarlo del ordenamiento jurídico.',
   'Ajustar la diferencia directamente en la nómina y dejar una anotación interna, porque lo relevante es que el servidor reciba el valor correcto y el documento no se modifica.',
   'Esperar a que el interesado advierta el error y lo reclame, porque corregir de oficio un acto ya notificado podría interpretarse como una modificación unilateral en su perjuicio.'],
  'Correcto. Los <strong>errores aritméticos y de transcripción</strong> se corrigen <strong>en cualquier tiempo</strong>, de oficio o a petición de parte, con un límite: la corrección no puede <strong>alterar el sentido material</strong> de la decisión. Aquí no lo altera, así que ese es el camino.',
  'Revocar por un error de suma es desproporcionado. Ajustar la nómina sin tocar el acto deja el documento y el pago diciendo cosas distintas. Y esperar al reclamo deja correr un error que la entidad ya conoce.'),

 (1,
  'Una persona pregunta en el punto de atención si puede presentar su petición de manera verbal, porque no sabe escribir bien. Un compañero le dice que todo debe quedar por escrito y le entrega una hoja en blanco. Otro propone grabar lo que diga en su celular personal y transcribirlo después. La persona insiste en que necesita dejar radicado algo hoy porque vive a tres horas de la ciudad y no puede volver esta semana. Es la tercera vez que intenta presentar su solicitud.',
  '¿Cuál es la actuación correcta?',
  ['Entregarle la hoja y explicarle que debe traerla diligenciada, porque la entidad necesita un documento firmado por el peticionario para poder dar trámite a cualquier solicitud.',
   'Recibir la petición verbal, dejarla por escrito con el apoyo necesario, radicarla con su fecha y entregarle constancia, porque el CPACA admite expresamente las peticiones verbales.',
   'Grabar lo que la persona manifieste y transcribirlo después, de modo que quede registro fiel de sus palabras aunque no se cuente con un documento firmado por ella en ese momento.',
   'Remitirla a la oficina jurídica para que allí le ayuden a redactar el escrito, porque la redacción de documentos a nombre de los ciudadanos excede las funciones del punto de atención.'],
  'Correcto. El CPACA admite expresamente las <strong>peticiones verbales</strong>, y el deber de las autoridades no se agota en recibir: incluye <strong>facilitar</strong>, con especial atención a quien está en situación de vulnerabilidad. Se deja por escrito con el apoyo necesario, se radica con su fecha y se entrega constancia.',
  'Exigir un escrito firmado desconoce la norma y deja sin atención a quien vino de lejos. Grabar en un celular personal introduce un dato personal en un medio no institucional. Y trasladarla a otra oficina es desatender un deber propio.'),

 (3,
  'Una servidora, inconforme con un acto, le pregunta a usted si debe presentar un recurso de reposición o demandar directamente, y cuál «le conviene más». Añade que un abogado le dijo que demandar es más rápido. Un compañero le sugiere a usted que le recomiende la vía que, en su criterio, tiene más posibilidades de prosperar, para ayudarla. El término para presentar el recurso vence en tres días y la servidora dice que confía más en lo que le diga la propia entidad.',
  '¿Cuál es la orientación correcta?',
  ['Recomendarle la vía que a su juicio tenga mayores posibilidades de prosperar, porque orientar al administrado hace parte del deber de atención y ella necesita una respuesta útil.',
   'Explicarle que no puede recibir ninguna orientación sobre el punto, porque se trata de un asunto jurídico que solo un abogado está habilitado para absolver en estos casos.',
   'Recomendarle que agote primero el recurso, porque la vía judicial siempre exige agotar la vía administrativa y demandar sin hacerlo llevaría al rechazo de su demanda.',
   'Informarle objetivamente qué recursos proceden, ante quién y en qué término, y que existen medios de control judicial, sin recomendarle cuál escoger ni anticipar resultados.'],
  'Correcto. Su deber es <strong>informar</strong>: qué recursos proceden, ante quién, en qué término, y que existen medios de control judicial. Lo que no le corresponde es <strong>aconsejar</strong> cuál escoger ni anticipar si prosperará: eso compromete la imparcialidad de la entidad frente a un asunto en el que ella es parte.',
  'Recomendar una vía, aunque sea con buena intención, es asesorar a una parte. Negarse a informar incumple el deber de atención. Y afirmar que siempre hay que agotar el recurso es inexacto: los recursos obligatorios y los facultativos no son lo mismo.'),

 (2,
  'Llega una petición dirigida a la Procuraduría pero cuyo contenido corresponde íntegramente a otra entidad del Estado. Un compañero propone archivarla y avisarle al peticionario que «se equivocó de entidad». Otro propone responderla con lo poco que la Procuraduría pueda averiguar por su cuenta sobre ese asunto. El peticionario dejó dirección física y correo, y el término ya empezó a correr desde la radicación de la semana pasada. El escrito es claro en lo que pide, solo que lo pide a quien no puede resolverlo.',
  '¿Cuál es la actuación correcta?',
  ['Archivarla e informar al peticionario que debe dirigirse a la entidad competente, porque la Procuraduría no puede abrir trámites sobre asuntos que escapan por completo a su competencia.',
   'Responderla con la información que la Procuraduría pueda obtener, porque el peticionario tiene derecho a una respuesta de la entidad ante la cual presentó efectivamente su escrito.',
   'Remitirla a la entidad competente dentro del término previsto e informar de ello al peticionario, dejando constancia de la remisión y de la comunicación que se le envió.',
   'Devolverla físicamente al peticionario con una nota que indique cuál es la entidad competente, para que sea él quien la radique directamente y el término comience allá desde cero.'],
  'Correcto. La regla es la misma dentro y fuera de la entidad: la falta de competencia se resuelve <strong>remitiendo al competente dentro del término</strong> e <strong>informando al peticionario</strong>. El ciudadano no tiene por qué saber qué entidad hace qué, y perder el término por eso sería injusto.',
  'Archivar o devolver traslada al peticionario una carga que es de la administración. Y responder con información que la entidad no maneja produce una respuesta de quien no podía darla.'),

 (0,
  'El jefe le pide que proyecte la respuesta a una petición en la que se solicitan tres cosas. Al revisar el borrador de un compañero, usted ve que resuelve dos con claridad y que la tercera —la más difícil— quedó mencionada en una línea que dice «lo demás solicitado se resolverá oportunamente». El término vence pasado mañana y la tercera solicitud exigiría consultar a otra dependencia, que ya informó que su respuesta tardará al menos una semana más en llegar.',
  '¿Cuál es la observación correcta?',
  ['La respuesta sería incongruente: debe resolver las tres o, si no es posible, informar antes del vencimiento los motivos y el plazo en que se resolverá la tercera, dentro de lo que la norma permite.',
   'El borrador es adecuado porque resuelve lo esencial dentro del término y anuncia que lo restante se resolverá después, con lo cual la entidad cumple su deber de respuesta oportuna.',
   'Debe eliminarse la mención a la tercera solicitud, porque anunciar una respuesta futura compromete a la entidad a un plazo que todavía no puede determinar con certeza razonable.',
   'Debe responderse únicamente la tercera solicitud, que es la de fondo, y dejar las otras dos para una comunicación posterior en la que se entreguen los documentos solicitados.'],
  'Correcto. Una respuesta debe ser <strong>congruente</strong>: resolver todo lo pedido. Si una parte no alcanza, el camino es el que el CPACA prevé: <strong>informar antes del vencimiento</strong> los motivos y el plazo en que se resolverá, sin exceder lo que la norma permite. «Se resolverá oportunamente» no es eso.',
  'Anunciar vagamente una respuesta futura no cumple el deber. Borrar la mención empeora la incongruencia. Y responder solo una parte, cualquiera que sea, deja las otras sin resolver.'),

 (1,
  'Un peticionario solicita acceso al expediente de la actuación en la que es interesado y pide tomar fotografías de los documentos con su celular. Un compañero dice que fotografiar documentos oficiales está prohibido y que solo puede pedir copias pagando su costo. Otro, que puede llevarse el expediente a su casa para revisarlo con calma y devolverlo al día siguiente, dejando una copia de su cédula como garantía. En el expediente hay documentos de un tercero.',
  '¿Cuál es la actuación correcta?',
  ['Negar la toma de fotografías e informarle que solo puede obtener copias previo pago, porque la reproducción de documentos oficiales está sujeta al procedimiento y a las tarifas de la entidad.',
   'Permitir la consulta del expediente en las instalaciones y la reproducción por los medios que la entidad admita, con las salvedades de la reserva, sin que el expediente salga de la entidad.',
   'Entregarle el expediente para que lo revise fuera de la entidad y lo devuelva al día siguiente, dejando constancia escrita del préstamo y de la fecha comprometida de devolución.',
   'Remitirle por correo electrónico la totalidad del expediente escaneado, incluidos los documentos sujetos a reserva, porque frente al interesado no hay restricción alguna de acceso.'],
  'Correcto. El interesado tiene derecho a <strong>consultar el expediente y a obtener reproducciones</strong>, con las salvedades de la <strong>reserva</strong>. Lo que no ocurre es que el expediente salga de la entidad: su integridad y su custodia son responsabilidad de la administración.',
  'Negar toda reproducción desconoce el derecho de acceso. Prestar el expediente pone en riesgo documentos que soportan una actuación. Y enviar todo escaneado, incluidos los documentos reservados, desconoce los límites legales.'),

 (3,
  'Al proyectar un acto, usted advierte que la decisión resuelve correctamente lo pedido pero omitió pronunciarse sobre un punto accesorio que el interesado también planteó. El acto ya fue firmado y notificado. Un compañero propone revocarlo y rehacerlo completo; otro, responder el punto faltante en un oficio aparte sin relación formal con el acto. El interesado ya preguntó por escrito qué pasó con ese punto y el término para recurrir el acto todavía está corriendo.',
  '¿Cuál es la figura que corresponde?',
  ['La revocatoria directa del acto y la expedición de uno nuevo que resuelva todos los puntos, porque un acto incompleto es un acto inválido que debe retirarse del ordenamiento jurídico.',
   'Un oficio separado que responda el punto faltante, porque se trata de un aspecto accesorio que no afecta la decisión principal ya notificada y puede resolverse por una vía independiente.',
   'No hacer nada, porque el interesado puede plantear el punto omitido mediante un recurso contra el acto, y resolverlo de oficio sería anticiparse a una actuación que le corresponde a él.',
   'La adición del acto, que es la figura prevista para pronunciarse sobre un punto que debió resolverse y se omitió, sin alterar lo ya decidido, y que debe notificarse igual que el acto original.'],
  'Correcto. El CPACA distingue tres figuras que la prueba confunde a propósito: <strong>corrección</strong> (errores formales), <strong>aclaración</strong> (un punto oscuro) y <strong>adición</strong> (un punto que debió resolverse y se omitió). Aquí lo que falta es un pronunciamiento, de modo que la figura es la <strong>adición</strong>, y se notifica como el acto original.',
  'Revocar un acto correcto por una omisión parcial es desproporcionado. Un oficio suelto sin relación formal con el acto deja el punto resuelto fuera del acto que debía contenerlo. Y esperar a que el interesado recurra le traslada una carga que nació de un error de la entidad.'),

 (2,
  'Una servidora presenta una petición y, a la semana, presenta otra idéntica, y luego una tercera, todas sobre el mismo asunto y sin aportar hechos nuevos. La primera ya fue respondida de fondo, notificada y archivada en el expediente, con constancia de su fecha, y en ella se resolvieron todos los puntos que entonces se plantearon. Un compañero propone no responder las dos siguientes «porque ya se le contestó» y otro, volver a estudiar el asunto desde cero en cada una. Al comparar los tres escritos con detenimiento, usted confirma que el segundo es idéntico al primero y que el tercero añade un hecho nuevo que no figuraba en ninguno de los dos anteriores.',
  '¿Cuál es la actuación correcta?',
  ['No responder las peticiones posteriores, porque el asunto ya fue resuelto de fondo y responder lo mismo una y otra vez constituye un desgaste injustificado de la administración.',
   'Estudiar el asunto de nuevo en cada petición, porque cada escrito es una petición autónoma que genera para la entidad el deber de pronunciarse de fondo sobre lo solicitado.',
   'Responder remitiéndose a la respuesta ya dada, indicando su fecha y cómo puede obtenerla, y verificando que no se hayan planteado hechos o pretensiones nuevas en los escritos posteriores.',
   'Responder la segunda petición y archivar la tercera, porque a partir de la segunda reiteración puede entenderse que el peticionario está ejerciendo abusivamente su derecho de petición.'],
  'Correcto. Una petición reiterada sigue siendo una petición y <strong>debe responderse</strong>, pero la respuesta puede <strong>remitirse a la ya dada</strong>, indicando su fecha y cómo obtenerla. Lo que no puede omitirse es la <strong>verificación</strong>: si el nuevo escrito trae hechos o pretensiones nuevas, hay que resolverlos.',
  'El silencio no es opción, por reiterada que sea la petición. Volver a estudiar todo desde cero sin hechos nuevos es un desgaste innecesario. Y declarar «abusivo» el ejercicio de un derecho fundamental a partir de la segunda vez no tiene fundamento.'),

 (0,
  'Un acto de carácter general que modifica un procedimiento interno de la División debe darse a conocer. Un compañero propone publicarlo en la intranet y, además, notificarlo personalmente a los tres servidores que más lo usan «para asegurarse de que lo lean». Otro propone solo enviarlo por correo a esos tres servidores. El acto empieza a regir en quince días y afecta a toda la dependencia, no solo a quienes aplican el procedimiento a diario.',
  '¿Cuál es la actuación correcta?',
  ['Publicarlo conforme a lo previsto para los actos de carácter general y difundirlo internamente, sin notificar personalmente a nadie, porque la notificación personal es propia de los actos particulares.',
   'Publicarlo y, además, notificarlo personalmente a los tres servidores más involucrados, porque así se garantiza que quienes aplican el procedimiento conozcan efectivamente el cambio introducido.',
   'Enviarlo únicamente por correo a los tres servidores que aplican el procedimiento, porque son los destinatarios reales del acto y una publicación general resultaría innecesaria en este caso.',
   'Esperar a que empiece a regir y, en ese momento, comunicarlo a quienes deban aplicarlo, de modo que la difusión coincida con la entrada en vigencia y no genere confusión previa.'],
  'Correcto. Los actos de <strong>carácter general</strong> se dan a conocer por <strong>publicación</strong>, no por notificación personal, que corresponde a los de contenido particular. Difundirlos internamente es buena práctica de gestión, pero no cambia la naturaleza del mecanismo.',
  'Mezclar publicación con notificación personal confunde las figuras y puede hacer creer que a unos destinatarios les corren términos distintos. Limitarlo a tres correos deja sin conocer el acto a quien también debe aplicarlo. Y difundirlo solo al entrar en vigencia desaprovecha los quince días previstos.'),

 (1,
  'Vence hoy el término para responder una petición y nadie la respondió: se traspapeló. Un compañero propone fechar la respuesta con una fecha anterior «para que no aparezca vencida» y otro, no responder nada «porque ya operó el silencio y el asunto pasó a otra instancia». El peticionario no ha vuelto a comunicarse, el asunto es resoluble hoy mismo y el expediente está completo sobre su escritorio desde hace dos semanas.',
  '¿Cuál es la actuación correcta?',
  ['Fechar la respuesta dentro del término y remitirla hoy, porque el estudio del asunto efectivamente se adelantó dentro del plazo y la demora fue meramente administrativa e involuntaria.',
   'Responder de fondo hoy mismo, con la fecha real, informar la situación por el canal y dejar constancia de lo ocurrido, porque el silencio no releva a la entidad del deber de responder.',
   'No responder, porque al operar el silencio administrativo negativo el asunto quedó definido y cualquier respuesta posterior carecería de efecto jurídico frente al peticionario.',
   'Responder hoy pero omitir la fecha de radicación de la petición en el documento, de modo que no quede en evidencia el tiempo transcurrido entre la solicitud y la respuesta remitida.'],
  'Correcto. El <strong>silencio no releva</strong> a la entidad del deber de responder: la petición sigue viva y, si es resoluble hoy, se resuelve hoy, con la <strong>fecha real</strong>. Informar la situación y dejar constancia es lo que permite corregir la causa y lo que protege a quien actuó bien.',
  'Antedatar la respuesta convierte un retraso explicable en una falsedad documental. No responder perpetúa el incumplimiento. Y ocultar la fecha de radicación es la misma maniobra en versión disimulada.'),
]
