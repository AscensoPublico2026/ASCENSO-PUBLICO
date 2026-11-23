# -*- coding: utf-8 -*-
"""Día 19 · Informes técnicos, dictámenes y presentación de pruebas — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-TEC-4TI15O-01',
    archivo='FUN-TEC-4TI15O-01-informes-tecnicos-presentacion-pruebas.html',
    dia=19,
    titulo_doc='Informes técnicos, dictámenes y presentación de pruebas',
    h1='Informes técnicos<br>y presentación de pruebas',
    kicker='Día 19 · Conocimientos específicos',
    sub='El producto final de su trabajo. Qué es un <strong>informe técnico</strong> y en qué se diferencia de un informe administrativo, la <strong>estructura</strong> que lo hace utilizable, la <strong>estadística descriptiva</strong> y la presentación de datos, la <strong>trazabilidad de la fuente</strong>, la <strong>ética del dato</strong>, la <strong>anonimización</strong>, los <strong>informes periódicos y ad hoc</strong>, los errores que más cuestan, y el bloque que cierra el curso: cómo se <strong>presentan las pruebas practicadas y sus anexos</strong> ante la autoridad que solicitó el apoyo, que es una función expresa de su manual.',
    badges=['⏱ 110-130 min', '📄 Informe técnico', '📊 Datos'],
    fmeta='Informes técnicos, dictámenes y presentación de pruebas practicadas',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Informes técnicos y presentación de pruebas',
)

FUENTE = 'guias/FUN-INF-4TM16-01-informes-estadisticas-datos.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- módulos nuevos
DICTAMEN = '''<h3>El informe técnico probatorio: por qué no es un informe administrativo</h3>
  <p>Conviene empezar separando dos cosas que esta guía va a tratar juntas pero que no son iguales. Un <strong>informe administrativo</strong> rinde cuentas de una gestión: cuántos trámites, en qué tiempos, con qué resultado. Un <strong>informe técnico probatorio</strong> —el que usted elabora cuando practica una prueba por delegación— hace algo distinto: <mark>acredita un hecho ante quien debe decidir sobre él</mark>. El primero se lee para informarse; el segundo se lee para fundar una decisión y, con frecuencia, se lee buscando por dónde atacarlo.</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th></th><th>Informe administrativo</th><th>Informe técnico probatorio</th></tr></thead>
      <tbody>
        <tr><td><strong>Para qué</strong></td><td>Informar sobre una gestión o un estado de cosas.</td><td>Acreditar un hecho para que otro decida sobre él.</td></tr>
        <tr><td><strong>Quién lo lee</strong></td><td>El superior o la dependencia interesada.</td><td>El servidor competente, el investigado y su defensa, y eventualmente la segunda instancia.</td></tr>
        <tr><td><strong>Qué exige</strong></td><td>Claridad, oportunidad, datos correctos.</td><td>Todo lo anterior <strong>más</strong> método descrito, resultados verificables y limitaciones declaradas.</td></tr>
        <tr><td><strong>Qué pasa si falla</strong></td><td>Se corrige y se vuelve a enviar.</td><td>Puede arrastrar la decisión que se funde en él, o quedar como inexistente (art. 158 del CGD).</td></tr>
        <tr><td><strong>Quién puede contradecirlo</strong></td><td>Nadie, formalmente.</td><td>El investigado, en ejercicio del derecho de contradicción.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>Las tres partes que no pueden faltar</h4>
  <div class="flujo">
    <div class="flujo-paso"><div class="fp-n">1</div><div><b>Qué se hizo y cómo</b><p>La metodología aplicada, en términos que permitan a otro técnico entender el procedimiento y, en su caso, repetirlo. Sin esto el informe pide un acto de fe.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">2</div><div><b>Qué resultó, completo</b><p>Todos los hallazgos —favorables y desfavorables a cualquier hipótesis— con el mismo nivel de detalle, y con mediciones donde haya algo medible.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">3</div><div><b>Qué no permite concluir</b><p>Las limitaciones de la técnica, del material o de las condiciones. Un informe que no declara sus límites invita a leerlo como más concluyente de lo que es.</p></div></div>
  </div>
  <p>Y la cuarta parte, que es la que no está: <strong>la calificación jurídica</strong>. El informe no dice si hubo falta, ni si la conducta fue dolosa, ni si procede una sanción. Lo vio en los días anteriores y vuelve aquí porque es, literalmente, el error de redacción más frecuente del oficio.</p>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Una pregunta típica contrasta dos redacciones del mismo hallazgo: una descriptiva y medida, otra conclusiva y breve. La segunda parece más útil para el despacho y es incorrecta. Regla práctica: si una frase del informe <strong>podría aparecer en el fallo</strong>, probablemente no debería estar en el informe.</p></div>
  <div class="checkpoint" data-cp="51">
    <div class="cp-q">✋ Punto de control: ¿qué distingue a un informe técnico probatorio de un informe administrativo?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">Su extensión y su nivel de detalle: el probatorio es más largo y más minucioso que el administrativo.</button>
    <button class="cp-opt" data-ans="1">Su finalidad y sus exigencias: acredita un hecho para que otro decida, y por eso debe describir el método, los resultados completos y sus limitaciones, y puede ser contradicho.</button>
    <button class="cp-opt" data-ans="0">El destinatario: el administrativo va al superior y el probatorio a la Fiscalía o a la Contraloría.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  '''

PRESENTACION = '''<h3>Presentar las pruebas practicadas y sus anexos: la función que cierra el ciclo</h3>
  <p>Su manual de funciones incluye una que casi nadie estudia y que es el acto final de todo su trabajo: <strong>presentar las pruebas practicadas y sus anexos ante la autoridad que solicitó el apoyo</strong>. No dice «remitir» ni «entregar»: dice <em>presentar</em>. Y presentar es un acto con contenido propio, no un trámite de mensajería.</p>
  <h4>Qué significa presentar bien</h4>
  <ul class="lista">
    <li><strong>Que el conjunto esté completo y ordenado.</strong> El informe, el acta, los registros de custodia, los anexos, el inventario. Un anexo anunciado y ausente es la primera cosa que una defensa encuentra.</li>
    <li><strong>Que cada anexo esté referido desde el informe.</strong> «Véase anexo 4» no sirve si el anexo 4 no está identificado en el inventario. La referencia cruzada es lo que convierte un paquete de papeles en un cuerpo probatorio.</li>
    <li><strong>Que la trazabilidad se pueda seguir sin preguntarle a usted.</strong> Quien lea debe poder reconstruir el recorrido de cada elemento sin llamarlo por teléfono. Si hace falta su explicación verbal, el documento está incompleto.</li>
    <li><strong>Que las limitaciones estén donde se leen.</strong> No en una nota al final, sino junto al hallazgo que condicionan.</li>
    <li><strong>Que el canal sea el institucional.</strong> La presentación deja constancia de la entrega; un correo personal no la deja.</li>
  </ul>
  <h4>La prueba de fuego: ¿resiste la contradicción?</h4>
  <p>Hay una manera sencilla de evaluar su propio informe antes de presentarlo, y consiste en leerlo como lo leería la defensa. Son cinco preguntas:</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Pregunta de la defensa</th><th>Qué debe poder responder el documento</th></tr></thead>
      <tbody>
        <tr><td>«¿Con qué título actuó?»</td><td>La delegación está identificada en el informe, con su fecha y su alcance.</td></tr>
        <tr><td>«¿Es el mismo elemento?»</td><td>Rótulo, registro de custodia y eslabones completos, con las novedades documentadas.</td></tr>
        <tr><td>«¿Cómo llegó a eso?»</td><td>El método está descrito con el detalle suficiente para que otro técnico lo siga.</td></tr>
        <tr><td>«¿Qué dejó por fuera?»</td><td>Lo que no se pudo hacer está consignado, con su causa.</td></tr>
        <tr><td>«¿Esto es lo que usted dice que es?»</td><td>Las limitaciones de la técnica están declaradas junto al hallazgo.</td></tr>
      </tbody>
    </table>
  </div>
  <p>Si el documento responde las cinco, la contradicción se convertirá en una discusión técnica, que es lo que debe ser. Si falla una, la discusión se desplazará a la regularidad de su actuación, y ahí el resultado del examen deja de importar.</p>
  <div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Su informe está listo y el despacho tiene audiencia mañana. Al revisar el paquete advierte que falta el anexo 3 —un registro fotográfico— porque quedó en otro equipo al que no tiene acceso hasta el lunes.</p>
    <p><strong>Cómo proceder.</strong> No presente el informe anunciando un anexo que no va. Dos salidas correctas: presentar el conjunto completo cuando el anexo esté disponible, informando por escrito el impacto en el término; o presentar lo que sí está, <strong>sin referir el anexo faltante como si fuera parte del paquete</strong>, consignando expresamente que queda pendiente, por qué y para cuándo. La diferencia entre las dos la decide el competente, no usted; su obligación es advertirlo hoy, no el lunes.</p>
  </div>
  <div class="checkpoint" data-cp="52">
    <div class="cp-q">✋ Punto de control: su informe remite a un anexo que no alcanzó a incorporarse. ¿Qué hace?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">Presenta el informe tal como está: el anexo se incorporará después y la referencia quedará satisfecha.</button>
    <button class="cp-opt" data-ans="1">No presenta un paquete que anuncie un anexo ausente: consigna expresamente qué queda pendiente, por qué y para cuándo, e informa el impacto en el término.</button>
    <button class="cp-opt" data-ans="0">Elimina del informe la referencia al anexo, para que el documento quede internamente coherente.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  <div class="box gold">
    <div class="box-title">💡 Idea clave del día</div>
    <p>Todo su trabajo termina convertido en un documento, y ese documento será leído por alguien que no estuvo en la diligencia y por alguien que quiere desvirtuarlo. Un informe técnico bien hecho tiene tres partes —<strong>qué se hizo y cómo, qué resultó completo, qué no permite concluir</strong>— y una que no tiene: la calificación jurídica. Si una frase suya podría aparecer en el fallo, no debería estar en el informe.</p>
  </div>
  <div class="box ok">
    <div class="box-title">🧠 Frase para recordar</div>
    <p>«Describo el método, muestro todos los resultados y declaro mis límites. No concluyo lo que no me toca. Y antes de presentar, leo mi informe como lo leería la defensa.»</p>
  </div>
  <div class="fuentes"><div class="fuentes-tag">📚 Fuentes oficiales para profundizar</div>
    <ul class="lista">
      <li><a href="https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1952_2019_pr003.htm" target="_blank" rel="noopener">Ley 1952 de 2019, Título VI — Pruebas (arts. 149 peritación, 156 apoyo técnico, 158 inexistencia)</a></li>
      <li><a href="https://funcionpublica.gov.co/eva/gestornormativo/norma.php?i=90324" target="_blank" rel="noopener">Ley 1952 de 2019 — Código General Disciplinario</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981" target="_blank" rel="noopener">Ley 1581 de 2012 — Protección de datos personales</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=56882" target="_blank" rel="noopener">Ley 1712 de 2014 — Transparencia y acceso a la información pública</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=186" target="_blank" rel="noopener">Ley 594 de 2000 — Ley General de Archivos</a></li>
    </ul>
  </div>

  '''

SEC[2] = DICTAMEN + SEC[2].rstrip() + '\n\n  ' + PRESENTACION + '\n'

SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>', '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>', '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('Técnico Administrativo 4TM-16', 'Técnico Investigador 4TI-15'),
    ('Técnico Administrativo, código 4TM-16', 'Técnico Investigador, código 4TI-15'),
    ('Técnico Administrativo', 'Técnico Investigador'),
    ('(4TM-16)', '(4TI-15)'), ('4TM-16', '4TI-15'), ('4TM16', '4TI15O'), ('4TM', '4TI'),
    ('245-2026', '257-2026'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)

ACC = '''<details class="acc"><summary>¿Un informe técnico puede concluir que «no hay irregularidad»?</summary><div class="acc-body"><p>Puede concluir que <strong>el examen no encontró</strong> lo que se buscaba, que es distinto. «No se hallaron inconsistencias entre los registros examinados y el inventario» es una conclusión técnica legítima: dice qué se examinó y qué resultó. «No hay irregularidad» es una calificación: afirma algo sobre el conjunto del asunto, incluido lo que usted no examinó. La diferencia no es de matiz: la primera fórmula es verificable y la segunda compromete al técnico con algo que su prueba no cubre.</p></div></details>
  <details class="acc"><summary>Si el despacho me pide el informe en un formato distinto al institucional, ¿qué hago?</summary><div class="acc-body"><p>El formato institucional es un parámetro vigente y no cede ante una preferencia. Lo que sí es posible es entregar, <strong>además</strong>, un resumen en el formato que la dependencia pida, como documento separado y claramente identificado como resumen, nunca en lugar del informe. Y conviene dejar constancia escrita de la solicitud: si mañana alguien pregunta por qué existen dos documentos, la respuesta está en el expediente.</p></div></details>
  <details class="acc"><summary>¿Las limitaciones van al final o junto al hallazgo?</summary><div class="acc-body"><p>Junto al hallazgo que condicionan. Una limitación al final del informe se lee después de que el lector ya formó su impresión, y muchas veces no se lee. Si la técnica aplicada no permite determinar la antigüedad del daño, eso tiene que estar en el párrafo donde se describe el daño, no en un apartado de observaciones finales.</p></div></details>
  <div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> El despacho le devuelve el informe pidiendo que «elimine la parte de las limitaciones, porque genera dudas y el expediente necesita claridad».</p>
    <p><strong>Cómo proceder.</strong> Se acata lo que es forma —orden, redacción, formato— y se objeta por escrito lo que afecta el fondo. Suprimir las limitaciones no da claridad: hace que el informe parezca más concluyente de lo que la técnica permite, y eso es exactamente lo que la contradicción va a atacar. Exponga por escrito por qué deben permanecer y deje constancia de su análisis.</p>
  </div>'''
SEC[2] = SEC[2].rstrip() + "\n\n  " + ACC + "\n"

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre informes '
              'técnicos y presentación de pruebas: estructura del informe, método y limitaciones, estadística y '
              'presentación de datos, trazabilidad de la fuente, ética del dato, anonimización, y la presentación '
              'de las pruebas practicadas con sus anexos.')

P = [
 (2,
  'Usted practicó una prueba técnica sobre un equipo y debe rendir el informe. El despacho le pide que sea «breve y al punto», porque el expediente ya está muy voluminoso. Usted puede describir el método aplicado en media página, los hallazgos en una y las limitaciones de la técnica en un párrafo. El servidor del despacho le sugiere dejar solo los hallazgos, que es lo que él necesita para decidir. El término vence pasado mañana y usted ya tiene el borrador con las tres partes redactadas.',
  '¿Cómo debe estructurarse el informe?',
  ['Con los hallazgos únicamente, atendiendo la solicitud del despacho, que conoce el expediente y sabe qué necesita para adoptar su decisión sobre el fondo del asunto.',
   'Con los hallazgos y el método, omitiendo las limitaciones, que pueden exponerse verbalmente si el despacho pregunta por el alcance del resultado obtenido.',
   'Con las tres partes: qué se hizo y cómo, qué resultó de manera completa, y qué no permite concluir la técnica aplicada o el estado del material examinado.',
   'Con los hallazgos y las limitaciones, omitiendo el método, que es información técnica interna y no aporta a la valoración que el competente debe realizar.'],
  'Un informe técnico probatorio sin método pide un acto de fe, y sin limitaciones invita a leerse como más concluyente de lo que es. Las tres partes no son extensión innecesaria: son lo que lo hace utilizable y resistente a la contradicción.',
  'Recortar el método o las limitaciones deja el informe sin lo que permite verificarlo, y una explicación verbal posterior no está en el expediente: para el proceso, no existe.'),

 (0,
  'Al redactar el informe, usted advierte que escribió «el servidor incurrió en una falta al no seguir el procedimiento». Lo que usted documentó es que el procedimiento establecido no se siguió en tres de los cinco pasos, con los registros que lo acreditan. El informe no ha sido remitido y el término vence mañana. Usted conserva el acta de la diligencia y el registro fotográfico de los cinco pasos del procedimiento. Nadie más ha leído el borrador y el despacho confía en lo que usted consigne.',
  '¿Qué debe corregir?',
  ['Sustituir la frase por la descripción de los tres pasos que no se siguieron, con sus registros, sin afirmar que hubo falta ni calificar la conducta del servidor.',
   'Nada: describir que el procedimiento no se siguió y que eso constituye una falta es una constatación objetiva que el examen técnico permite sostener plenamente.',
   'Matizar la frase a «habría incurrido en una falta», de modo que la afirmación quede planteada con reserva y no comprometa la decisión final del despacho.',
   'Mantener la frase y añadir al final del informe una nota aclarando que la calificación de la conducta corresponde al servidor competente y no al técnico.'],
  'Regla práctica del día: si una frase del informe podría aparecer en el fallo, no debería estar en el informe. «Incurrió en una falta» es exactamente eso. La descripción de los tres pasos omitidos, con registros, es más útil porque es verificable.',
  'Matizarla con un condicional o añadir una nota al final no borra la calificación del cuerpo del documento: el problema no es el grado de certeza, es la competencia.'),

 (3,
  'Su informe presenta un dato porcentual: de 40 registros examinados, 12 presentaban la inconsistencia. Un compañero le sugiere escribir «el 30 % de los registros presentaba la inconsistencia» y omitir el total, «porque el porcentaje es más impactante y más fácil de leer para el despacho». El informe se rinde esta semana y el despacho piensa citar el dato en el auto de evaluación del expediente. El compañero insiste y dos del grupo le dan la razón en la reunión de la mañana.',
  '¿Cuál es la actuación correcta?',
  ['Usar solo el porcentaje, que es la forma estándar de presentar este tipo de resultados y resulta más clara para un lector no técnico que las cifras absolutas.',
   'Usar solo las cifras absolutas, porque los porcentajes sobre bases pequeñas siempre inducen a error y no deben aparecer en un informe de contenido técnico.',
   'Usar el porcentaje en el cuerpo del informe y las cifras absolutas en un anexo, de modo que el texto quede ágil y el dato completo esté disponible si se requiere.',
   'Presentar el porcentaje junto con las cifras absolutas y el total examinado, para que el lector pueda valorar el dato con su base y no quede expuesto a una lectura engañosa.'],
  'Un porcentaje sin su base es un dato incompleto: 30 % sobre 40 no es lo mismo que 30 % sobre 4.000. Presentar ambos no es redundancia, es lo que permite al lector valorar lo que está leyendo.',
  'Ni el porcentaje solo ni las cifras solas; y relegar la base a un anexo deja en el cuerpo del informe un dato que no se puede valorar donde se lee.'),

 (1,
  'Usted elabora un informe que debe incluir datos de 14 servidores, de los cuales solo tres están vinculados a la actuación. Los datos de los otros once aparecen en los registros que usted examinó porque comparten el mismo sistema. El despacho no pidió nada sobre ellos. El sistema es compartido por toda la dependencia y el informe debe rendirse pasado mañana con sus anexos. El despacho no preguntó nada sobre los once servidores restantes del sistema.',
  '¿Cómo debe tratar esos datos?',
  ['Incluirlos todos, porque fueron efectivamente examinados y omitirlos podría leerse como una selección sesgada del material disponible en el sistema institucional.',
   'Incluir únicamente los datos de los tres servidores vinculados, y referirse a los demás de manera agregada y anonimizada cuando sea indispensable para describir el hallazgo.',
   'Incluirlos todos pero con las iniciales en lugar de los nombres completos, de modo que el informe quede completo sin identificar directamente a quienes no están vinculados.',
   'Excluir todos los datos personales, incluidos los de los tres vinculados, y describir los hallazgos de forma completamente anónima para proteger la intimidad de todos.'],
  'La protección de datos exige limitar el tratamiento a lo necesario para el fin que lo justifica. Los tres vinculados sí; los once restantes, de forma agregada y anonimizada solo si es indispensable para describir el hallazgo.',
  'Incluirlos todos trata datos de personas ajenas a la actuación, y las iniciales siguen identificando en un universo pequeño. Pero anonimizar también a los vinculados vaciaría de contenido el informe.'),

 (2,
  'Al revisar el borrador de su informe, usted advierte que los datos que sustentan un hallazgo provienen de una planilla que le entregó la dependencia, sin firma ni fecha, y que usted no pudo cotejar con el sistema. El hallazgo es relevante y el término vence pasado mañana. La planilla la entregó el jefe de la dependencia en la diligencia, en papel y sin membrete institucional. Usted pidió el cotejo al área de sistemas y la respuesta tardará una semana.',
  '¿Cómo debe proceder?',
  ['Presentar el hallazgo con los datos de la planilla, dado que fue entregada oficialmente por la dependencia competente del asunto y goza de presunción de veracidad documental.',
   'Omitir el hallazgo del informe por completo, porque un dato que no pudo cotejarse con la fuente oficial no debe sustentar ninguna afirmación en un documento con valor probatorio.',
   'Presentar el hallazgo identificando la fuente exacta —la planilla, quién la entregó, cuándo, y que no fue posible cotejarla— y declarar esa limitación junto al hallazgo.',
   'Solicitar a la dependencia que firme y feche la planilla retroactivamente, de modo que el soporte del hallazgo quede regularizado antes de presentar el informe.'],
  'La trazabilidad de la fuente es una exigencia del informe técnico: todo dato debe poder rastrearse. Un dato no cotejado no se oculta ni se presenta como firme: se presenta identificando su fuente y declarando la limitación junto al hallazgo.',
  'Presentarlo sin la advertencia lo hace parecer más firme de lo que es; omitirlo suprime un hallazgo relevante; y pedir una firma retroactiva produce un documento falso.'),

 (0,
  'El despacho le pide un informe ad hoc para hoy sobre un asunto que normalmente tomaría tres días de verificación. Usted puede entregar hoy un análisis parcial con los datos ya disponibles, o entregar el lunes el análisis completo. El término del expediente no vence esta semana. El informe lo pidió el despacho por correo esta mañana y usted tiene verificados tres de los cinco puntos. El despacho prefiere tener algo hoy antes de la reunión de la tarde con el jefe.',
  '¿Cuál es la actuación correcta?',
  ['Entregar hoy el análisis con los datos disponibles, identificando con precisión qué se verificó y qué no, y proponer la fecha en que puede completarse lo pendiente.',
   'Entregar hoy el análisis con los datos disponibles sin advertir qué quedó sin verificar, dado que el despacho conoce la urgencia con la que fue solicitado el informe.',
   'Negarse a entregar un análisis parcial y comprometer la entrega completa para el lunes, porque un informe incompleto no cumple el estándar de rigor exigible.',
   'Entregar hoy una versión preliminar sin carácter de informe técnico, y el lunes el informe formal, de modo que el despacho disponga de los datos sin comprometer el rigor.'],
  'Rapidez sin sacrificar rigor: se entrega lo verificado, se dice con precisión qué no se verificó y se propone cuándo se completa. El despacho decide con información sobre el alcance de lo que recibe.',
  'Callar lo no verificado es presentar como firme lo que no lo es; negarse desatiende una necesidad real; y una «versión preliminar» sin carácter de informe deja circular datos sin régimen claro.'),

 (3,
  'Su informe compara dos periodos y el resultado del segundo es notablemente mejor. Al revisar, usted advierte que en el segundo periodo cambió el criterio con que la dependencia registraba los casos, de modo que las dos cifras no son estrictamente comparables. El despacho ya conoce el dato preliminar y lo está citando. El despacho ya citó la cifra preliminar en un correo interno y el informe debe rendirse esta semana. Nadie en la dependencia advirtió el cambio de criterio cuando se produjo.',
  '¿Qué corresponde hacer?',
  ['Mantener la comparación, ya que las dos cifras provienen de la misma fuente oficial y el cambio de criterio es un detalle metodológico interno de la dependencia.',
   'Eliminar la comparación del informe y presentar solo las cifras de cada periodo por separado, sin referirse al cambio de criterio que afecta su comparabilidad.',
   'Mantener la comparación y añadir una nota al final del informe advirtiendo que hubo un cambio de criterio en el registro durante el periodo analizado.',
   'Advertir expresamente, junto a la comparación, que el criterio de registro cambió y que ello afecta la comparabilidad, e informarlo de inmediato al despacho.'],
  'Una serie de tiempo exige comparabilidad: si el criterio cambió, la comparación engaña aunque las cifras sean correctas. La advertencia va junto al dato, no al final, y el despacho debe saberlo ya porque está citando el preliminar.',
  'Mantenerla sin advertencia produce una lectura falsa; eliminar la comparación oculta el problema; y una nota al final no se lee donde el dato se usa.'),

 (1,
  'Usted debe presentar las pruebas practicadas con sus anexos. El informe remite a un «anexo 3» que es un registro fotográfico, pero el archivo quedó en un equipo al que no tiene acceso hasta el lunes. El despacho tiene audiencia mañana y le pide el paquete hoy. Usted ya tiene el informe firmado y el resto de los anexos completos, ordenados e inventariados. El servidor del despacho lo llama cada hora preguntando si el paquete ya salió.',
  '¿Cuál es la actuación correcta?',
  ['Presentar el paquete tal como está, con la referencia al anexo 3, e incorporar el archivo faltante el lunes, cuando la referencia del informe quedará plenamente satisfecha.',
   'No presentar un paquete que anuncie un anexo ausente: consignar expresamente qué queda pendiente, por qué y para cuándo, e informar hoy el impacto en la audiencia.',
   'Eliminar del informe la referencia al anexo 3, de modo que el documento quede internamente coherente, e incorporar luego el registro fotográfico como un anexo nuevo el lunes.',
   'Presentar el paquete y advertir verbalmente al servidor del despacho que el anexo 3 llegará el lunes, para que lo tenga en cuenta durante la audiencia de mañana.'],
  'Un anexo anunciado y ausente es lo primero que una defensa encuentra. Se consigna qué falta, por qué y para cuándo, y se informa hoy —no el lunes— para que el competente decida con tiempo.',
  'Presentarlo con la referencia vacía deja el defecto en el expediente; eliminar la referencia altera el informe; y una advertencia verbal no queda en ninguna parte.'),

 (2,
  'Un compañero le muestra su informe: presenta una gráfica de barras cuyo eje vertical empieza en 85 en lugar de cero, lo que hace que una diferencia de tres puntos parezca enorme. Le explica que así «se ve mejor el hallazgo» y que los datos son todos correctos. El compañero debe presentar su informe hoy y le pide su opinión antes de remitirlo al despacho. El hallazgo que la gráfica muestra es real y está bien documentado en el informe.',
  '¿Cuál es la precisión correcta?',
  ['La gráfica es admisible: los datos son correctos y la escala elegida es una decisión de presentación que no altera la veracidad de la información consignada en el informe.',
   'La gráfica es admisible si el eje está rotulado con sus valores, porque un lector atento puede advertir dónde comienza la escala y valorar el dato correctamente.',
   'La gráfica induce a error aunque los datos sean correctos: una escala truncada exagera la diferencia, y la presentación de datos no debe producir una lectura que los datos no sostienen.',
   'La gráfica debe reemplazarse por una tabla, porque las representaciones gráficas nunca son apropiadas en un informe con valor probatorio dentro de una actuación.'],
  'La ética del dato no se limita a no falsear cifras: incluye no presentarlas de modo que produzcan una lectura que no sostienen. Una escala truncada es exactamente eso, y el rótulo del eje no lo remedia.',
  'Que los datos sean correctos no salva una presentación engañosa, y el problema no es la gráfica como formato: una gráfica bien construida informa mejor que una tabla.'),

 (0,
  'Al terminar el informe, usted lo relee preguntándose cómo lo leería la defensa. Advierte que no identificó la delegación con la que actuó: el documento describe el método y los hallazgos, pero no dice de dónde salió su competencia para practicar la prueba. El informe está listo para firma. El informe quedó impreso y listo para su firma, y el despacho lo espera a primera hora de mañana. Es su primer informe en ese formato y nadie más lo ha revisado antes de la firma.',
  '¿Qué debe hacer?',
  ['Incorporar la identificación de la delegación —su fecha, quién la expidió y su alcance— antes de presentar el informe, porque es la primera pregunta que la contradicción va a plantear.',
   'Presentarlo así: la delegación consta en el expediente y el informe no necesita repetir información que ya obra en la actuación disciplinaria correspondiente.',
   'Presentarlo así y aportar la delegación por separado si la defensa llega a cuestionar la competencia con la que el examen técnico fue practicado en su momento.',
   'Incorporar únicamente el número de radicado de la solicitud de apoyo, que es suficiente para que quien lea pueda ubicar el antecedente en el expediente de la actuación.'],
  '«¿Con qué título actuó?» es la primera de las cinco preguntas que la defensa plantea. El informe debe responderla por sí mismo: fecha, quién expidió la delegación y su alcance. Si hace falta buscar en otra parte, el documento está incompleto.',
  'Que la delegación conste en el expediente no releva de identificarla en el informe; aportarla después concede la discusión; y el radicado de la solicitud no es lo mismo que la delegación ni describe su alcance.'),

 (3,
  'El despacho le pide que el informe incluya una recomendación sobre las medidas que la dependencia debería adoptar para evitar que el hecho se repita. Usted tiene criterio técnico para formularla y sería útil. El formato del informe técnico no contempla un apartado de recomendaciones. La solicitud llegó por correo del despacho y el informe debe rendirse dentro del término ya fijado. Es la primera vez que el despacho le pide algo así en un informe técnico.',
  '¿Cómo debe proceder?',
  ['Incluir la recomendación en el cuerpo del informe, porque fue expresamente solicitada por el despacho y proviene de su propio criterio técnico sobre el asunto examinado.',
   'No incluirla ni mencionar el tema, porque el objeto del informe es acreditar un hecho y cualquier añadido alteraría el formato institucional vigente del documento.',
   'Incluirla creando un apartado para ello, advirtiendo que es una recomendación técnica y no una conclusión derivada de la prueba que fue practicada por delegación.',
   'Rendir el informe conforme al formato y presentar la recomendación por el canal institucional como documento separado, dejando constancia de que fue solicitada.'],
  'Dos parámetros en juego —el objeto del informe y su formato— y ninguno impide atender una solicitud legítima: el informe se rinde como corresponde y la recomendación va por separado, con constancia de que fue pedida.',
  'Meter la recomendación en el informe, aun en un apartado nuevo, altera el formato y mezcla lo acreditado con lo opinado. Pero ignorar la solicitud desaprovecha un aporte que tenía vía institucional.'),

 (1,
  'Su informe periódico mensual sobre los apoyos de la Dirección debe entregarse hoy. Dos de los apoyos del mes quedaron sin rendir por demoras ajenas a usted. Un compañero le sugiere reportarlos como «en trámite» sin más detalle, «porque así no se ve mal el indicador del grupo». El reporte lo lee el jefe de grupo y queda en el expediente interno de seguimiento del mes. El indicador del grupo se publica en la reunión mensual de la Dirección.',
  '¿Cuál es la actuación correcta?',
  ['Reportarlos como «en trámite», que es técnicamente exacto, y reservar la explicación de las causas para cuando alguien pregunte por el estado de esos dos apoyos.',
   'Reportar el estado real de los dos apoyos con la causa de la demora y la fecha estimada de rendición, aunque el indicador del grupo refleje un resultado menos favorable.',
   'Excluir los dos apoyos del informe mensual e incorporarlos al del mes siguiente, cuando ya estén rendidos y el reporte pueda presentarlos como cumplidos en su totalidad.',
   'Reportarlos como rendidos, dado que el trabajo técnico ya está hecho y solo falta el trámite formal de remisión del documento a la dependencia solicitante.'],
  'La objetividad en los reportes internos corta en las dos direcciones: no minimizar lo propio. El estado real con su causa es lo que permite a quien lee entender el indicador; maquillarlo lo vuelve inútil.',
  'Un «en trámite» sin detalle es una minimización; excluirlos del mes falsea el periodo; y reportarlos como rendidos es, directamente, un dato falso.'),

 (2,
  'Al preparar el informe, usted debe elegir cómo presentar un resultado que depende de cuatro variables. Una tabla de cuatro columnas lo muestra con precisión pero obliga a leer con cuidado; una frase resume la conclusión pero pierde el detalle. El lector será el servidor competente, que no es técnico en la materia. El informe debe rendirse pasado mañana y usted ya tiene los datos de las cuatro variables verificados. El servidor competente le ha pedido antes que le explique los cuadros por teléfono.',
  '¿Cuál es la mejor decisión?',
  ['La frase resumen, porque el lector no es técnico en la materia y una tabla con cuatro variables distintas podría resultarle difícil de interpretar correctamente al adoptar su decisión.',
   'La tabla únicamente, porque es la presentación precisa y el informe técnico debe privilegiar siempre el rigor sobre la facilidad de lectura del destinatario.',
   'La tabla con el detalle, acompañada de una lectura en texto que explique qué muestra, de modo que el dato preciso esté disponible y su significado sea comprensible.',
   'Ambas en documentos separados: la tabla como anexo técnico y la frase en el informe, para que cada lector consulte el nivel de detalle que necesite.'],
  'Claridad para un lector que no es técnico no significa simplificar hasta perder el dato: significa presentar el dato preciso y explicar qué muestra. Las dos cosas, en el mismo lugar.',
  'La frase sola pierde el detalle que sustenta el resultado; la tabla sola deja al lector interpretando por su cuenta; y separar el dato de su lectura obliga a reconstruir la relación entre ambos.'),

 (0,
  'Usted detecta que un informe suyo de hace dos meses contiene un error de cálculo: un total está sumado mal y la cifra correcta cambia la magnitud del hallazgo, aunque no su sentido. El informe ya fue usado por el despacho en una decisión que está notificada. La decisión se notificó hace tres semanas y usted conserva la hoja de cálculo con la operación original. Nadie ha advertido el error y el expediente sigue su curso con normalidad.',
  '¿Qué corresponde hacer?',
  ['Informar el error por escrito al competente de inmediato, con el cálculo correcto y la precisión de cómo afecta la magnitud del hallazgo, para que valore su incidencia.',
   'No informarlo, dado que el sentido del hallazgo no cambia y la decisión ya está notificada, de modo que una corrección solo generaría confusión en la actuación.',
   'Corregir el archivo del informe y volverlo a cargar al sistema con la cifra correcta, de modo que el expediente quede consistente con el cálculo correcto del total.',
   'Informarlo verbalmente al servidor del despacho que tramitó el caso, para que decida si vale la pena formalizar una corrección sobre una decisión ya notificada.'],
  'Un error de cálculo detectado se informa por escrito y de inmediato, con la cifra correcta y su efecto: la decisión ya notificada es precisamente la razón para avisar, no para callar. Quien valora la incidencia es el competente.',
  'Callar porque «el sentido no cambia» decide por otro; sustituir el archivo destruye la trazabilidad; y un aviso verbal no deja constancia de que usted lo advirtió.'),

 (3,
  'Es el último día del bloque funcional. Usted revisa su desempeño en los simulacros y encuentra un patrón: acierta las preguntas sobre contenido pero falla las que le piden decidir cómo redactar o qué presentar. Casi siempre elige la opción más breve, más concluyente o más rápida de entregar. Lleva un registro de los simulacros resueltos y puede ver exactamente qué opción eligió cada vez que falló.',
  '¿Cuál es la mejor manera de corregirlo en el día que queda?',
  ['Repasar la estructura del informe técnico y memorizar sus partes, porque conocerlas con precisión hará evidente qué debe contener cada documento que se le pida.',
   'Resolver el simulacro final y confiar en que la práctica acumulada de los diecinueve días corrija el patrón sin necesidad de un ajuste deliberado de criterio.',
   'Concentrarse en las preguntas de redacción, que son las que más falla, y dejar el repaso de los contenidos funcionales para una revisión rápida de los resúmenes.',
   'Aplicar dos preguntas antes de elegir: ¿permite verificar lo que afirma? y ¿esta frase podría aparecer en el fallo? Lo breve y lo concluyente falla una de las dos.'],
  'El patrón —breve, concluyente, rápido— se corrige con dos preguntas, no con más contenido: si la opción no permite verificar lo que afirma, falla por método; si la frase podría aparecer en el fallo, falla por competencia.',
  'Memorizar la estructura no cambia el criterio de elección; confiar en la práctica acumulada repite el patrón; y abandonar el repaso de contenidos a un día de la prueba cambia un problema por otro.'),
]
