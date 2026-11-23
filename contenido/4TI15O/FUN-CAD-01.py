# -*- coding: utf-8 -*-
"""Día 15 · Cadena de custodia y manejo de EMP y EF — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol, modulos, armar

META = dict(
    codigo='FUN-CAD-4TI15O-01',
    archivo='FUN-CAD-4TI15O-01-cadena-custodia-emp-ef.html',
    dia=15,
    titulo_doc='Cadena de custodia y manejo de EMP y EF',
    h1='Cadena de custodia<br>y manejo de EMP y EF',
    kicker='Día 15 · Conocimientos específicos',
    sub='El procedimiento operativo que hace que lo recaudado <strong>sirva</strong>. La <strong>diligencia</strong> y su acta, la <strong>organización y logística</strong> de una actuación, el <strong>inventario paso a paso</strong>, la <strong>cadena de custodia</strong> con sus eslabones y responsables, el tratamiento de <strong>discrepancias y novedades</strong>, el <strong>registro fotográfico</strong>, la <strong>trazabilidad documental</strong> del expediente y los <strong>reportes</strong>. Es el día más práctico del curso: aquí no se discute qué dice la norma, sino cómo se cumple con las manos.',
    badges=['⏱ 110-130 min', '📦 EMP y EF', '🔗 Custodia'],
    fmeta='Cadena de custodia y manejo de elementos materiales probatorios y evidencia física',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Cadena de custodia y manejo de EMP y EF',
)

FUENTE = 'guias/FUN-AII-01-diligencias-inventarios-medidas-cautelares.html'
SEC = secciones_mapeadas(FUENTE)

# se dejan fuera los módulos propios del control aduanero (medidas cautelares y destrucción de mercancía)
CAB, MODS = modulos(SEC[2])
SEC[2] = armar(CAB, MODS, {1, 2, 3, 4, 6, 7, 8, 10, 11, 12})

# ---------------------------------------------------------------- módulo nuevo
EMP_EF = '''<h3>EMP y EF: qué es cada cosa y por qué la custodia existe</h3>
  <p>Antes del procedimiento conviene fijar el vocabulario, porque la prueba escrita lo usa con precisión y porque de él depende entender qué se custodia y para qué.</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Concepto</th><th>Qué es</th><th>Ejemplo en una actuación disciplinaria</th></tr></thead>
      <tbody>
        <tr><td><strong>EMP</strong><br>Elemento material probatorio</td><td>Objeto, documento o registro que, por sí mismo o analizado, permite establecer un hecho relevante para la actuación.</td><td>Un expediente físico, un disco duro, un registro de ingreso, un equipo, una muestra.</td></tr>
        <tr><td><strong>EF</strong><br>Evidencia física</td><td>Lo hallado y recolectado en el lugar de los hechos que se vincula a ellos y requiere un tratamiento técnico para no alterarse.</td><td>Un documento hallado en el sitio, un dispositivo encontrado conectado, restos o rastros materiales.</td></tr>
        <tr><td><strong>Cadena de custodia</strong></td><td>El conjunto de procedimientos que garantiza la <mark>autenticidad, identidad e integridad</mark> del elemento desde su recolección hasta su valoración.</td><td>El registro continuo de quién lo tuvo, cuándo, en qué estado y qué se le hizo.</td></tr>
        <tr><td><strong>Rótulo</strong></td><td>La identificación física que acompaña al elemento y lo individualiza sin lugar a confusión.</td><td>Número único, fecha y hora, quién recolectó, dónde, descripción breve.</td></tr>
        <tr><td><strong>Registro de custodia</strong></td><td>El documento donde consta cada traspaso del elemento, eslabón por eslabón.</td><td>Entrega al laboratorio, devolución, entrega a la dependencia que lo custodia.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>Las tres garantías que la custodia protege</h4>
  <div class="flujo">
    <div class="flujo-paso"><div class="fp-n">1</div><div><b>Autenticidad</b><p>Que el elemento es lo que se dice que es y proviene de donde se dice que proviene. Lo acredita el registro del origen.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">2</div><div><b>Identidad</b><p>Que el elemento valorado es <strong>exactamente el mismo</strong> que se recolectó, sin sustitución. Lo acredita el rótulo único y continuo.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">3</div><div><b>Integridad</b><p>Que no se alteró ni se contaminó entre la recolección y la valoración. Lo acreditan el embalaje, las condiciones de almacenamiento y el registro de cada manipulación.</p></div></div>
  </div>
  <h4>Por qué esto es de su exclusiva responsabilidad</h4>
  <p>Hay una asimetría que conviene tener muy presente: quien decide el caso <strong>no estuvo en la diligencia</strong>. No vio el elemento en su contexto, no observó el estado en que se encontraba, no sabe quién estaba presente ni qué ocurrió mientras se recolectaba. Todo lo que esa persona podrá saber es lo que usted documentó. Por eso la cadena de custodia no es un trámite administrativo que acompaña al trabajo técnico: <mark>es la parte del trabajo técnico que permite que lo demás tenga valor</mark>.</p>
  <p>Y el precio de fallar está escrito: el <strong>artículo 158 del Código General Disciplinario</strong> dispone que la prueba recaudada sin las formalidades sustanciales o desconociendo derechos fundamentales <strong>se tendrá como inexistente</strong>. Un elemento sin rótulo, un eslabón sin registro, un embalaje abierto sin constancia: cada uno de esos descuidos es una vía directa a que el trabajo de un día desaparezca del expediente.</p>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Una ruptura de la cadena <strong>no siempre</strong> conduce a excluir el elemento: lo que hace es trasladar la discusión a si puede acreditarse por otros medios que es el mismo y que no se alteró. Por eso las opciones extremas —«la prueba se excluye automáticamente» o «la ruptura es irrelevante si el elemento es el correcto»— suelen ser las incorrectas. Lo que siempre corresponde es <strong>documentar la ruptura y ponerla en conocimiento del competente</strong>.</p></div>
  <div class="checkpoint" data-cp="0">
    <div class="cp-q">✋ Punto de control: ¿qué garantiza exactamente la cadena de custodia?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">Que el elemento recolectado acredita el hecho que se investiga en la actuación disciplinaria.</button>
    <button class="cp-opt" data-ans="1">La autenticidad, la identidad y la integridad del elemento: que es lo que se dice, que es el mismo que se recolectó y que no se alteró.</button>
    <button class="cp-opt" data-ans="0">Que el elemento fue recolectado por un servidor con funciones de policía judicial debidamente delegadas.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  '''

R = [('<h3>Tu cargo en el proceso:', EMP_EF + '<h3>Tu cargo en el proceso:')]
SEC = aplicar_todas(SEC, R, estricto=True)

# reenfoque del contexto aduanero de la base al contexto investigativo disciplinario
SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>', '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>', '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('investigaciones tributarias, aduaneras y cambiarias', 'investigaciones disciplinarias'),
    ('tributarias, aduaneras y cambiarias', 'disciplinarias'),
    ('tributario, aduanero y cambiario', 'disciplinario'),
    ('tributaria, aduanera y cambiaria', 'disciplinaria'),
    ('operaciones sospechosas', 'hallazgos relevantes'),
    ('mercancías aprehendidas', 'elementos asegurados'),
    ('mercancía aprehendida', 'elemento asegurado'),
    ('las mercancías', 'los elementos'), ('la mercancía', 'el elemento'),
    ('de mercancías', 'de elementos'), ('de mercancía', 'de elementos'),
    ('mercancías', 'elementos'), ('mercancía', 'elemento'),
    ('bodegas', 'almacenes de evidencia'), ('bodega', 'almacén de evidencia'),
    ('depositarios', 'custodios'), ('depositario', 'custodio'),
    ('aduanero', 'disciplinario'), ('aduanera', 'disciplinaria'),
    ('tributario', 'disciplinario'), ('tributaria', 'disciplinaria'),
    ('cambiario', 'disciplinario'), ('cambiaria', 'disciplinaria'),
    ('contribuyentes', 'servidores investigados'), ('contribuyente', 'servidor investigado'),
    ('la DIAN', 'la PGN'), ('DIAN', 'PGN'),
    ('Analista II', 'Técnico Investigador'), ('Analista I', 'Técnico Investigador'),
    ('Analistas', 'Técnicos Investigadores'), ('Analista', 'Técnico Investigador'),
    ('AII-01', '4TI15O-01'), ('AII', '4TI15O'),
    ('decisión de aprehensión', 'decisión de aseguramiento'),
    ('acta de aprehensión', 'acta de aseguramiento'),
    ('una aprehensión', 'un aseguramiento'), ('La aprehensión', 'El aseguramiento'),
    ('aprehensiones', 'aseguramientos'), ('aprehensión', 'aseguramiento'), ('se aprehenda', 'se asegure'),
    ('Si se aprehendió, es porque ya se determinó que es ilegal', 'Si se aseguró un elemento, es porque ya se determinó que hubo falta'),
    ('aprehendió', 'aseguró'),
    ('aprehende', 'asegura'), ('aprehendido', 'asegurado'), ('aprehendida', 'asegurada'),
    ('contrabando y evasión', 'irregularidades administrativas'),
    ('lavado de activos', 'posibles delitos'),
    ('Casos tipo CNSC', 'Casos tipo prueba'),
    ('trampas favoritas de la CNSC', 'trampas favoritas de la prueba'),
    ('la CNSC', 'la prueba'), ('CNSC', 'la prueba escrita'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)

CIERRE = '''<div class="box gold">
    <div class="box-title">💡 Idea clave del día</div>
    <p>La cadena de custodia no acompaña al trabajo técnico: <strong>es la parte del trabajo técnico que permite que lo demás tenga valor</strong>. Quien decide el caso no estuvo en la diligencia; todo lo que podrá saber es lo que usted documentó. Por eso la regla que resuelve la familia entera de casos de este día es una sola: <mark>ante cualquier anomalía, documentar y poner en conocimiento; nunca reparar por cuenta propia</mark>. Corregir un registro, reembalar fuera de un acto documentado, refoliar o completar un dato de memoria son reparaciones silenciosas, y todas destruyen justamente lo que la custodia protege.</p>
  </div>
  <div class="box ok">
    <div class="box-title">🧠 Frase para recordar</div>
    <p>«Autenticidad, identidad e integridad: que es lo que digo, que es el mismo, que no se alteró. Y lo que no quede registrado en el momento, después es solo lo que alguien recuerda.»</p>
  </div>
  <div class="fuentes"><div class="fuentes-tag">📚 Fuentes oficiales para profundizar</div>
    <ul class="lista">
      <li><a href="https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1952_2019_pr003.htm" target="_blank" rel="noopener">Ley 1952 de 2019, Título VI — Pruebas (arts. 147 a 158: aseguramiento, apoyo técnico e inexistencia)</a></li>
      <li><a href="https://funcionpublica.gov.co/eva/gestornormativo/norma.php?i=90324" target="_blank" rel="noopener">Ley 1952 de 2019 — Código General Disciplinario</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=4125" target="_blank" rel="noopener">Constitución Política de Colombia — arts. 15, 28 y 29</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=6543" target="_blank" rel="noopener">Decreto Ley 262 de 2000 — Estructura y funciones de la PGN (art. 10: la DNIE)</a></li>
      <li><a href="https://www.procuraduria.gov.co/" target="_blank" rel="noopener">Procuraduría General de la Nación — sitio oficial</a></li>
    </ul>
  </div>'''
SEC[2] = SEC[2].rstrip() + "\n\n  " + CIERRE + "\n"

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre cadena de '
              'custodia y manejo de elementos materiales probatorios: recolección y rótulo, embalaje, registro de '
              'custodia, inventario, traslado y almacenamiento, discrepancias y novedades, registro fotográfico, '
              'evidencia digital y trazabilidad documental.')

P = [
 (1,
  'Usted recolecta un disco duro en una diligencia delegada. Al terminar, advierte que la bolsa de embalaje que llevaba no cierra bien y que el sello se despegó durante el traslado al vehículo. El elemento no salió de su vista en ningún momento y lo acompaña un compañero que puede dar fe de ello. Faltan veinte minutos para llegar a la Dirección y usted puede reembalarlo allí con material adecuado. El informe debe rendirse en tres días.',
  '¿Cuál es la actuación correcta?',
  ['Reembalar el elemento al llegar a la Dirección y no mencionar el incidente, dado que el disco no salió de su vista y su compañero puede dar fe de que no hubo manipulación alguna.',
   'Dejar constancia escrita e inmediata del incidente —qué pasó, cuándo, quién estuvo presente, en qué estado quedó—, reembalar documentando el cambio e informarlo por el canal al competente.',
   'Devolver el disco duro a la dependencia de origen y solicitar una nueva delegación, porque un embalaje comprometido invalida de manera insubsanable la recolección ya practicada.',
   'Reembalar y anotar el cambio únicamente en su libreta de campo, para tener el dato disponible si alguien cuestiona la integridad del elemento durante la contradicción de la prueba.'],
  'Una novedad en el embalaje se documenta en el momento, con todos sus detalles, y se informa: así la integridad queda explicada en lugar de quedar en duda. El testimonio de un compañero no reemplaza la constancia.',
  'Callar el incidente deja un hueco que aparecerá en la contradicción; devolver el elemento renuncia a una recolección válida; y anotarlo solo en su libreta no lo incorpora al expediente.'),

 (3,
  'Al recibir un elemento para examinarlo, usted advierte que el rótulo tiene un número de identificación distinto al que figura en el registro de custodia que lo acompaña: uno termina en 47 y el otro en 41. El resto de los datos coincide. La dependencia dice que es «un error de digitación obvio» y que el elemento es sin duda el correcto. El examen técnico debe practicarse mañana. La discrepancia la advierte al recibir el elemento y el registro de custodia viene firmado por tres eslabones anteriores.',
  '¿Qué corresponde hacer?',
  ['Practicar el examen y consignar en el informe que existía una discrepancia menor entre el rótulo y el registro, dejando que el competente valore su incidencia al decidir el fondo.',
   'Corregir el registro de custodia para que coincida con el rótulo, que es la identificación física del elemento y prevalece sobre cualquier documento que lo acompañe.',
   'Devolver el elemento sin practicar el examen, porque una discrepancia en la identificación rompe la cadena de custodia de forma insubsanable y lo inutiliza como prueba.',
   'No practicar el examen hasta aclarar la discrepancia, dejar constancia escrita de ambos números y de lo manifestado por la dependencia, e informarlo de inmediato al competente.'],
  'La identidad es una de las tres garantías de la custodia: si el rótulo y el registro no coinciden, no está acreditado que el elemento sea el mismo. Se documenta la discrepancia y se informa antes de manipularlo, no después.',
  'Examinar primero y mencionarlo después ya habría manipulado un elemento cuya identidad no está acreditada; corregir el registro de oído crea un documento falso; y devolverlo sin informar impide que el competente resuelva.'),

 (0,
  'Durante una diligencia usted debe recolectar doce documentos de distinta naturaleza y un dispositivo. El tiempo apremia porque la dependencia cierra. Un compañero propone embalar todo junto en una sola caja rotulada con un número y detallar el contenido después, en la Dirección, «porque así se gana una hora y el inventario queda igual de completo». Usted está solo con un compañero, la dependencia ya apagó las luces y el inventario todavía no se ha levantado.',
  '¿Cuál es la actuación correcta?',
  ['Individualizar y rotular cada elemento en el lugar, levantar el inventario allí mismo y dejar constancia de las condiciones en que se practicó la recolección.',
   'Embalar todo junto con un rótulo único y levantar el inventario detallado al llegar a la Dirección, dejando constancia de que se hizo así por el cierre de la dependencia.',
   'Recolectar solo el dispositivo, que es el elemento más relevante, y solicitar una nueva diligencia para los documentos cuando la dependencia esté disponible con más tiempo.',
   'Embalar todo junto, fotografiar el conjunto antes de cerrar la caja y usar esa fotografía como soporte del inventario que se levantará posteriormente en la Dirección.'],
  'La identidad se asegura individualizando en el lugar: un rótulo por elemento y el inventario levantado allí. Completarlo después abre precisamente el espacio para que se discuta qué entró y qué no en la caja.',
  'Un rótulo único para trece elementos impide acreditar la identidad de cada uno; una fotografía del conjunto no individualiza; y renunciar a los documentos pierde prueba que sí podía recolectarse.'),

 (2,
  'El elemento que usted recolectó debe quedar almacenado hasta que se practique el examen. El almacén de evidencia de la Dirección está lleno y el encargado propone guardarlo en un archivador de la oficina del grupo, que tiene llave y a la que acceden cuatro personas. El examen está programado para dentro de una semana y el elemento es un equipo de cómputo. El almacén de evidencia tiene lista de espera de tres días y el encargado insiste en que la solución es provisional.',
  '¿Cuál es la actuación correcta?',
  ['Aceptar la solución propuesta y anotar en el registro de custodia que el elemento quedó en el archivador de la oficina, con lo que la trazabilidad queda formalmente documentada.',
   'Llevar el equipo a su propio puesto de trabajo y custodiarlo personalmente hasta el examen, de modo que una sola persona responda por él durante toda la semana.',
   'Dejar constancia del problema de capacidad, informarlo por el canal y pedir instrucción, y no disponer por cuenta propia una ubicación que no garantiza acceso restringido ni trazabilidad.',
   'Practicar el examen de inmediato, aunque no estaba programado, para no tener que almacenar el equipo y eliminar así el riesgo que el almacenamiento prolongado representa.'],
  'La integridad depende de las condiciones de almacenamiento y del acceso restringido. Un archivador al que acceden cuatro personas no las garantiza. Lo que corresponde es informar el problema y pedir instrucción, no improvisar una ubicación.',
  'Anotar la ubicación no suple la falta de condiciones; custodiarlo personalmente lo hace responsable de algo que la entidad debe garantizar; y adelantar el examen altera una programación que no le corresponde cambiar.'),

 (1,
  'Usted entrega un elemento a otro servidor para que lo traslade al laboratorio. Él tiene prisa, le dice que firma el registro de custodia «cuando vuelva» y se lleva el elemento. Usted conserva su copia del registro sin la firma de recepción. El laboratorio confirma por teléfono que el elemento llegó bien. El laboratorio queda en otra sede y usted no verá de nuevo a ese servidor hasta la próxima semana. Usted debe rendir el informe técnico el viernes y el elemento es clave para el resultado.',
  '¿Qué debe hacer?',
  ['Nada adicional: la confirmación telefónica del laboratorio acredita que el elemento llegó y que el traslado se cumplió sin novedades durante el trayecto.',
   'Dejar constancia escrita de que el elemento se entregó sin la firma de recepción, identificando a quién, cuándo y en qué estado, e informarlo por el canal al competente.',
   'Firmar usted mismo la casilla de recepción indicando el nombre del servidor que se llevó el elemento, para que el registro de custodia quede completo y sin espacios en blanco.',
   'Esperar a que el servidor regrese y firme la casilla con la fecha de hoy, de modo que el registro quede cerrado antes de que termine la jornada y sin constancias adicionales.'],
  'Un eslabón sin firma es un eslabón sin acreditar. Lo que protege la cadena es dejar constancia de lo que efectivamente ocurrió —a quién, cuándo, en qué estado— e informarlo, no completar el registro después como si hubiera ocurrido de otro modo.',
  'La confirmación telefónica no acredita la entrega; firmar por otro falsifica el registro; y hacerlo firmar después con la fecha de hoy consigna como presente un acto que ya pasó.'),

 (3,
  'En una diligencia usted toma fotografías de un elemento antes de recolectarlo. Al revisarlas en la Dirección, advierte que tres salieron desenfocadas y que no se distingue el detalle que justificaba el registro fotográfico. El elemento ya está embalado y sellado, con su rótulo, y el examen está programado para mañana. Usted conserva la tarjeta de memoria con todas las imágenes y el embalaje está sellado desde la diligencia de ayer.',
  '¿Cuál es la actuación correcta?',
  ['Abrir el embalaje, repetir las fotografías y volver a sellar, dejando el registro fotográfico completo antes de que el examen técnico se practique al día siguiente.',
   'Usar fotografías de un elemento similar tomadas en otra diligencia, señalando en el informe que son ilustrativas del tipo de detalle que se pretendía registrar.',
   'No mencionar el problema, dado que el elemento está correctamente embalado y rotulado y el examen técnico permitirá documentar el detalle con mejor calidad que una fotografía.',
   'Dejar constancia de la limitación del registro fotográfico, conservar las imágenes tal como salieron y documentar el detalle durante el examen, con el embalaje abierto bajo registro.'],
  'El registro fotográfico documenta el estado previo; si salió deficiente, eso se declara. Abrir el embalaje fuera de un acto documentado rompe la integridad: el detalle se documenta en el examen, que sí es un acto registrado.',
  'Reabrir y resellar por fuera de un acto documentado compromete la integridad; usar fotos de otro elemento es sustituir material probatorio; y callar la limitación deja al competente creyendo que hay un registro que no existe.'),

 (2,
  'Le entregan un teléfono móvil encendido y con la pantalla desbloqueada, hallado durante una diligencia. El despacho quiere saber si contiene unas comunicaciones concretas. Un compañero le dice que revise el contenido ahora, «aprovechando que está desbloqueado, porque si se bloquea ya no se podrá entrar». No hay autorización para examinar comunicaciones y su delegación se refiere a asegurar el dispositivo. Hay otras personas presentes en el lugar, el acta sigue abierta y el despacho espera el informe para el viernes.',
  '¿Qué corresponde hacer?',
  ['Revisar el contenido aprovechando el estado del dispositivo y documentar con precisión lo hallado, dado que la delegación de asegurar comprende verificar qué es lo que se asegura.',
   'Fotografiar las pantallas visibles sin navegar por el dispositivo, de modo que quede registro del contenido a la vista sin que ello constituya un examen de las comunicaciones.',
   'Asegurar el dispositivo conforme a lo delegado, documentando el estado en que se halló, sin examinar su contenido, e informar la situación al competente para que disponga.',
   'Apagar el dispositivo de inmediato para preservar la batería y la integridad de la información, y consignarlo en el acta como medida técnica de aseguramiento del elemento.'],
  'Asegurar no es examinar. El contenido de las comunicaciones está protegido por el art. 15 de la Constitución y requiere la autorización que la ley prevea: se asegura, se documenta el estado en que se halló y decide el competente.',
  'Revisar o fotografiar pantallas es acceder al contenido sin autorización; y apagar el dispositivo por decisión propia puede alterar su estado: esa decisión técnica se consulta, no se improvisa.'),

 (0,
  'Al levantar el inventario de los elementos recolectados, usted advierte que el número de folios de un expediente no coincide con la foliación que trae: el documento dice 212 folios y usted cuenta 209. La dependencia que lo entrega no sabe explicarlo. La diligencia está por cerrarse y hay cinco personas presentes. Es su primera diligencia en esa dependencia y nadie allí recuerda quién folió el expediente ni cuándo. El despacho espera el inventario esta misma tarde para evaluar el expediente.',
  '¿Cuál es la actuación correcta?',
  ['Consignar en el acta la discrepancia exacta —lo que dice la foliación y lo que arroja el conteo—, dejar constancia de lo manifestado por la dependencia y hacerla firmar por los presentes.',
   'Refoliar el expediente con el número real de folios antes de recolectarlo, de modo que el inventario y el documento queden coherentes al momento de ingresar a custodia.',
   'Recolectar el expediente consignando el número que trae la foliación, por ser el dato oficial, y verificar el conteo con más calma en la Dirección antes de rendir el informe.',
   'No recolectar el expediente y solicitar a la dependencia que aclare previamente la diferencia, dejando constancia de que la recolección quedó pendiente de esa aclaración.'],
  'Una discrepancia documental se consigna exactamente como aparece, con los dos datos, lo manifestado y la firma de los presentes. Esa constancia es lo que después permite explicar la diferencia en lugar de que aparezca como una pérdida.',
  'Refoliar altera un documento ajeno; consignar solo el dato oficial oculta la diferencia que usted detectó; y dejar de recolectar pierde el elemento y deja la discrepancia sin registro.'),

 (1,
  'Usted practica el examen técnico de un elemento y debe abrir el embalaje sellado. Está solo en el laboratorio de la Dirección y el procedimiento no exige la presencia de un segundo servidor. El examen durará dos días y el elemento quedará en el laboratorio esa noche. Es la primera vez que practica un examen que se extiende más de una jornada y el laboratorio queda cerrado con llave. Nadie más del grupo está en la sede a esa hora y el procedimiento no prevé el caso.',
  '¿Qué debe documentar?',
  ['Basta consignar el resultado del examen en el informe técnico, ya que la apertura del embalaje es un acto interno del procedimiento que no modifica la cadena de custodia del elemento.',
   'La apertura con fecha y hora, el estado del sello y del embalaje al abrirlo, lo que se hizo, y las condiciones en que quedó el elemento durante la noche, con el nuevo sellado.',
   'Únicamente la fecha de apertura y la de cierre del examen, porque el detalle del estado del embalaje corresponde al momento de la recolección y no al de la práctica de la prueba.',
   'La apertura y el resultado, omitiendo las condiciones de permanencia nocturna, ya que el elemento permaneció dentro de las instalaciones de la Dirección bajo seguridad institucional.'],
  'Cada manipulación es un eslabón: la apertura, el estado del sello al abrirlo, lo que se hizo y las condiciones en que quedó. Que el elemento permanezca dentro de la entidad no suspende el registro.',
  'Ni la apertura es un acto interno sin consecuencias, ni basta la fecha, ni la seguridad institucional reemplaza la constancia de las condiciones de permanencia.'),

 (3,
  'El competente ordena devolver a la dependencia de origen unos elementos ya examinados. Al prepararlos, usted advierte que uno de ellos presenta un deterioro que no existía al recolectarlo: una carpeta tiene la cubierta doblada. El examen no explica ese deterioro y no afecta el contenido ni el resultado consignado. La orden de devolución llegó por escrito esta mañana y usted conserva el acta de recolección con el estado inicial.',
  '¿Cuál es la actuación correcta?',
  ['Devolverlo sin mencionarlo, dado que el deterioro es puramente externo, no afecta el contenido y no incide en el resultado técnico que ya fue consignado en el informe.',
   'Corregir el deterioro en lo posible antes de la devolución, de modo que el elemento regrese a la dependencia en condiciones equivalentes a las de su recolección.',
   'Suspender la devolución hasta establecer quién causó el deterioro, para que la entrega no se haga sin que esa responsabilidad quede previamente determinada en el expediente.',
   'Dejar constancia escrita del deterioro, compararlo con el estado registrado al recolectar, informarlo por el canal y hacerlo constar en el acta de devolución.'],
  'La integridad se acredita comparando el estado registrado al recolectar con el estado al devolver. Un cambio, por menor que sea, se documenta: ocultarlo es exactamente lo que después hace dudar de todo el resto del registro.',
  'Callar un deterioro mina la credibilidad de la custodia completa; corregirlo altera el elemento; y suspender la devolución para determinar responsables es una decisión que no le corresponde.'),

 (2,
  'La dependencia que solicitó el apoyo le pide que le entregue directamente los elementos ya examinados, sin pasar por el procedimiento de egreso de la Dirección, porque los necesita para una diligencia de mañana. Le dice que firma lo que haga falta y que así se ahorra un día. Usted tiene el informe listo y los elementos embalados y rotulados. La diligencia de la dependencia es a primera hora de mañana y el procedimiento de egreso toma un día hábil.',
  '¿Qué corresponde hacer?',
  ['Entregarlos contra firma en ese momento y registrar el egreso en el sistema al día siguiente, de modo que la urgencia se atienda sin que la trazabilidad se pierda definitivamente.',
   'Negarse a entregarlos y no dejar registro de la solicitud, porque una petición que se aparta del procedimiento no debería quedar documentada en el expediente de la actuación.',
   'Tramitar el egreso conforme al procedimiento, informar la urgencia por el canal para que se priorice, y dejar constancia de la solicitud recibida y de cómo se atendió.',
   'Entregar copia del informe técnico de inmediato y retener los elementos hasta completar el egreso, de modo que el despacho tenga el resultado aunque no tenga aún el material.'],
  'El procedimiento de egreso es lo que mantiene la trazabilidad: no se invierte el orden y se registra después. La urgencia real se atiende priorizando el trámite, no saltándoselo, y la solicitud se deja documentada.',
  'Entregar primero y registrar después deja un intervalo sin trazabilidad; negarse sin registrar borra la solicitud del expediente; y entregar solo el informe no resuelve la necesidad planteada ni tramita el egreso.'),

 (1,
  'Durante el traslado de unos elementos, el vehículo de la Dirección sufre una avería y usted debe esperar dos horas en la vía. Los elementos permanecen en el baúl, sellados, y usted no se separa del vehículo. Al llegar, todo está en orden aparente y nadie pregunta por el retraso. Usted viajaba solo con el conductor y la avería ocurrió en una vía con tránsito, a la vista de otros vehículos. Los elementos deben entregarse hoy mismo al almacén de evidencia de la Dirección.',
  '¿Debe documentarlo?',
  ['No: los elementos permanecieron sellados y bajo su control durante todo el tiempo, de modo que la cadena no sufrió interrupción alguna que deba quedar registrada.',
   'Sí: debe dejar constancia del tiempo, el lugar, la causa y las condiciones en que permanecieron los elementos, e informarlo, aunque no haya indicio de alteración alguna.',
   'Solo si al llegar se advierte alguna alteración en el estado de los elementos o en los sellos, porque de lo contrario se estaría documentando un hecho sin ninguna consecuencia.',
   'Solo en su libreta de campo, para tener el dato disponible si el retraso llegara a ser cuestionado durante la contradicción de la prueba en el proceso disciplinario.'],
  'La trazabilidad documenta el recorrido completo, no solo los incidentes con consecuencias visibles. Un intervalo no explicado es, después, un espacio para la duda; un intervalo explicado es simplemente un hecho registrado.',
  'Que no haya indicio de alteración no releva de documentar el intervalo; condicionar la constancia a que algo se note invierte la lógica de la custodia; y la libreta personal no es el expediente.'),

 (0,
  'Un compañero le comenta que, en su grupo, el registro de custodia se diligencia al final de la jornada «de corrido», con todos los movimientos del día, porque hacerlo en el momento de cada traspaso «retrasa mucho las diligencias». Le propone que usted haga lo mismo para no quedarse atrás con la carga de trabajo asignada. Su grupo tiene cuatro apoyos simultáneos esta semana y nadie ha observado nunca esa práctica en la dependencia.',
  '¿Cuál es la precisión correcta?',
  ['El registro se diligencia en el momento de cada traspaso: hacerlo después, de memoria, convierte el documento en una reconstrucción y le quita el valor que justifica su existencia.',
   'Es admisible si al final de la jornada se consignan todos los movimientos con sus horas reales, ya que lo relevante es que la información quede completa y no cuándo se escribe.',
   'Es admisible cuando la carga de trabajo lo justifica, siempre que se deje constancia de que el registro se diligenció de manera diferida por razones operativas de la dependencia.',
   'Es indiferente: lo que acredita la custodia es el rótulo del elemento y no el registro, que cumple una función meramente administrativa de control interno de la dependencia.'],
  'Un registro diligenciado después, de memoria, es una reconstrucción: deja de acreditar lo que ocurrió y pasa a afirmar lo que alguien recuerda. El valor del registro está, precisamente, en su simultaneidad con el hecho.',
  'Ni la integridad posterior de la información, ni la carga de trabajo, ni el rótulo suplen la simultaneidad del registro: es lo que lo hace un documento de custodia y no una memoria.'),

 (3,
  'Le piden apoyar una diligencia donde se recolectarán elementos de los que usted no conoce el tratamiento técnico adecuado: son de una naturaleza que nunca ha manipulado y sabe que un manejo incorrecto puede alterarlos de modo irreversible. En el grupo nadie más está disponible y la diligencia es mañana. Es su primer mes en la Dirección y el jefe dio por sentado que usted podía asumir la diligencia sin dificultad. La dependencia ya confirmó la diligencia y no hay margen para reprogramarla esta semana.',
  '¿Cuál es la conducta correcta?',
  ['Practicarla aplicando el procedimiento general de recolección, que es común a cualquier tipo de elemento, y consignar en el acta que era la primera vez que manipulaba ese material.',
   'Practicarla y pedir después a un compañero con experiencia que revise el estado del elemento, de modo que un eventual error de manipulación pueda detectarse antes del examen.',
   'Negarse a participar y dejar constancia de que no domina el tratamiento técnico, para que la responsabilidad por el aplazamiento recaiga en quien programó la diligencia.',
   'Informar por escrito la limitación y el riesgo de alteración irreversible, pedir acompañamiento o apoyo especializado, y dejar constancia de la situación antes de la diligencia.'],
  'Reconocer el límite de la propia competencia técnica es lo que protege el elemento, que no se recupera. Se informa por escrito el riesgo y se pide acompañamiento: ni se asume el riesgo en silencio ni se declina sin encauzar.',
  'El procedimiento general no cubre un tratamiento especializado; una revisión posterior no repara una alteración irreversible; y negarse sin pedir apoyo traslada el problema sin resolverlo.'),

 (2,
  'Faltan seis días para la prueba escrita. En los simulacros de este bloque usted acierta cuando la pregunta describe un error evidente, pero falla cuando las opciones proponen soluciones que «arreglan» el problema: corregir un registro, reembalar, refoliar, completar un dato que se conoce. Su registro muestra ese patrón en cinco de los últimos ocho casos. Lleva un registro de los simulacros resueltos y puede ver exactamente qué opción eligió cada vez que falló.',
  '¿Cuál es la mejor manera de corregirlo?',
  ['Memorizar los pasos del procedimiento de cadena de custodia en orden, porque conocer la secuencia completa permite identificar enseguida cuál de ellos se omitió en cada caso planteado.',
   'Resolver más simulacros de este bloque hasta que la intuición mejore, dejando el repaso del procedimiento para los últimos días antes de presentar la prueba escrita.',
   'Aplicar una regla única: ante cualquier anomalía, lo que corresponde es documentarla y ponerla en conocimiento, nunca repararla por cuenta propia. La reparación silenciosa siempre es el distractor.',
   'Concentrarse en los casos de evidencia digital, que son los que más preguntas generan hoy, y repasar el resto del procedimiento con el checklist del final de esta guía.'],
  'Todas esas opciones —corregir, reembalar, refoliar, completar— comparten la misma falla: reparan en silencio un hecho que debía quedar registrado. La regla «documentar y poner en conocimiento, nunca reparar por cuenta propia» resuelve la familia entera.',
  'Memorizar la secuencia no evita caer en la reparación silenciosa, que suena correcta; repetir simulacros sin cambiar el criterio repite el error; y concentrarse en un solo tipo de elemento deja fuera la mayoría de los casos.'),
]
