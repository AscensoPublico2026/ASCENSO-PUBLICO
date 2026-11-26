# -*- coding: utf-8 -*-
"""Día 11 · CPACA I: ámbito, principios, derechos y deberes, y derecho de petición."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol, modulos, armar
from _brenda import IDENTIDAD, CARGO, PLURAL, meta
from _lib import aplicar_todas as _ap
from _regimen import TODAS as _REGIMEN

META = meta(
    codigo='FUN-CPACA-4TC17B-01',
    archivo='FUN-CPACA-4TC17B-01-ambito-principios-derecho-peticion.html',
    dia=11,
    titulo_doc='CPACA I: ámbito, principios, derechos y deberes, y derecho de petición',
    h1='CPACA I<br>Ámbito, principios, derechos y deberes, y derecho de petición',
    kicker='Día 11 · Conocimiento específico',
    sub='El <strong>Código de Procedimiento Administrativo y de lo Contencioso Administrativo</strong> (Ley 1437 de 2011) es el segundo conocimiento específico que exige el formato de la Convocatoria 285-2026, y el que gobierna todo lo que proyectas en la <strong>División de Gestión Humana</strong>: cada acto de personal es un acto administrativo. Hoy, la primera mitad: a quién obliga el código y cuál es su <strong>ámbito</strong>, los <strong>principios</strong> del artículo 3, los <strong>derechos y deberes</strong> de las personas ante las autoridades y las <strong>prohibiciones</strong> a estas, cómo se inicia una actuación, y el <strong>derecho de petición</strong> completo: modalidades, requisitos, términos, prórroga, traslado por falta de competencia, peticiones de información y copias, y reserva legal.',
    badges=['⏱ 100-120 min', '⚖️ CPACA', '📖 Específico'],
    fmeta='CPACA I: ámbito, principios, derechos y deberes y derecho de petición (Ley 1437 de 2011 y Ley 1755 de 2015)',
    alerta='CPACA I: ámbito, principios, derechos y deberes y derecho de petición',
)

# la base trae 15 módulos: 1-7 son el ámbito, los principios y el derecho de petición
S = secciones_mapeadas('guias/FUN-ADM-09-cpaca-principios-procedimiento.html')
cabeza, mods = modulos(S[2])
S[2] = armar(cabeza, mods, set(range(1, 8)))

CIERRE = '''
      <div class="modulo-head"><div class="modulo-n">★</div><h3>Por qué el CPACA es tu norma de cabecera en Gestión Humana</h3></div>
      <div class="b-texto">
        <p>Puede parecer que el CPACA es cosa de abogados y de despachos. No lo es: es la norma que gobierna <mark>todo lo que tú proyectas</mark>. Cada nombramiento, cada encargo, cada reconocimiento de una prima, cada negativa de una licencia y cada certificación es un <strong>acto administrativo</strong> o una respuesta a una <strong>petición</strong>, y a los dos los rige la Ley 1437 de 2011.</p>
        <div class="tabla-wrap"><table>
          <thead><tr><th>Lo que llega a la División</th><th>Qué es, en lenguaje del CPACA</th><th>Qué obliga</th></tr></thead>
          <tbody>
            <tr><td>Un servidor pide su certificación laboral</td><td>Petición de <strong>copia o de documento</strong></td><td>Término propio, más corto que el de una petición general</td></tr>
            <tr><td>Un servidor reclama que le liquidaron mal una prima</td><td><strong>Petición en interés particular</strong></td><td>Respuesta de fondo, clara, precisa y congruente, dentro del término</td></tr>
            <tr><td>Un exservidor pide información de su historia laboral</td><td>Petición de <strong>información</strong>, con límites de reserva</td><td>Verificar la calidad de quien pide y los datos protegidos</td></tr>
            <tr><td>Un jefe pide un concepto sobre cómo tramitar una novedad</td><td><strong>Consulta</strong></td><td>Término propio; la respuesta no obliga ni compromete responsabilidad</td></tr>
            <tr><td>Llega una petición dirigida a otra dependencia</td><td><strong>Falta de competencia</strong></td><td>Remitir al competente e informar al peticionario, dentro del término</td></tr>
          </tbody>
        </table></div>
        <div class="ojo"><b>Ojo en la prueba:</b> hay un error que cuesta caro en el trabajo y varias preguntas en el examen: creer que <mark>responder es contestar algo</mark>. El CPACA exige una respuesta <strong>de fondo, clara, precisa y congruente</strong> con lo pedido, y <strong>notificada o comunicada</strong>. Un oficio que dice «su solicitud está en trámite» no resuelve la petición, no interrumpe el término y deja a la entidad en falta.</div>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Un exservidor radica un escrito pidiendo tres cosas: copia de su acta de posesión, certificación de los factores que devengó y que «le expliquen por qué no le pagaron una prima en 2023». Son <strong>tres peticiones en un mismo documento</strong>, con naturalezas y términos distintos: dos de copia o certificación y una de fondo. La respuesta debe resolverlas <strong>todas</strong> y ser congruente con cada una: responder solo las dos fáciles y callar la tercera es exactamente lo que el CPACA llama una respuesta incongruente, y abre la puerta a una tutela.</p>
          </div>
        </div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> el CPACA no es una norma ajena a la gestión del talento humano: es la que la gobierna. Todo lo que la División recibe es una petición —de fondo, de información, de copia o una consulta— y todo lo que proyecta es un acto administrativo. De ahí salen las tres obligaciones que debes tener siempre presentes: responder <strong>de fondo</strong>, dentro del <strong>término</strong> que corresponda a cada tipo de petición, y <strong>comunicar o notificar</strong> la respuesta.</p></div>
        <div class="box ok"><div class="box-title">💡 Idea clave del día</div><p><strong>Idea clave:</strong> ante cualquier escrito que llegue a la División, hazte siempre las mismas cuatro preguntas, en este orden: <strong>¿qué tipo de petición es?</strong> (de fondo, de información, de copia o consulta, porque de ahí sale el término) · <strong>¿somos competentes?</strong> (si no, se remite y se informa, no se devuelve) · <strong>¿qué hay que responder exactamente?</strong> (todo lo pedido, de fondo y de manera congruente) · <strong>¿cómo se comunica?</strong> (por el medio autorizado, con constancia de la fecha). Esas cuatro preguntas resuelven la mayoría de las situaciones de este día, en la prueba y en el puesto.</p></div>
        <div class="box ojo"><div class="box-title">🗣️ Frase para recordar</div><p>«No hay fórmulas sacramentales: lo que llega se radica, lo que no es nuestro se remite, lo que se pide se responde de fondo y dentro del término, y lo que se responde se comunica. — Día 11»</p></div>
      </div>
    </div>
  </div>
'''
S[2] = S[2] + CIERRE
SEC = aplicar_todas(S, IDENTIDAD + [('Gestor II', 'Técnico en Criminalística 4TC-17'), ('Gestor', 'Técnico en Criminalística 4TC-17')], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(CARGO, PLURAL), estricto=False)

SEC = _ap(SEC, _REGIMEN, estricto=False)   # carrera especial PGN, no CNSC

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el ámbito del '
              'CPACA, sus principios, los derechos y deberes ante las autoridades y el derecho de petición en todas '
              'sus modalidades. Fíjate siempre en dos cosas: qué tipo de petición es y quién es el competente.')

P = [
 (2,
  'Un lunes a primera hora llega a la División de Gestión Humana un escrito firmado por un contratista de la entidad. Pide «respuesta urgente» sobre el pago de una factura y copia del acta de recibo del servicio. El documento no indica a qué dependencia va dirigido, no invoca el derecho de petición y no trae el poder que acredita la representación, aunque en el expediente del contrato ya reposa el certificado de existencia y representación que la propia entidad consultó hace dos meses. Un compañero sugiere devolverlo para que lo presente «como debe ser».',
  '¿Cuál es la actuación correcta?',
  ['Devolver el escrito al peticionario indicándole que debe presentarlo nuevamente invocando el derecho de petición, dirigido a la dependencia competente y con el poder que acredite su representación.',
   'Radicarlo pero suspender su trámite hasta que el peticionario aporte el poder, porque sin acreditar la representación no es posible establecer si tiene legitimación para elevar la solicitud.',
   'Radicarlo con su fecha, tramitarlo como derecho de petición aunque no lo invoque, y no exigir un documento que la propia entidad ya tiene en su poder, dejando constancia de lo verificado.',
   'Radicarlo y responderlo directamente desde la División, porque la urgencia manifestada por el peticionario justifica resolver de inmediato sin remitirlo a la dependencia que lleva el contrato.'],
  'Correcto. El derecho de petición <strong>no exige fórmulas sacramentales</strong>: no hace falta invocarlo ni dirigirlo a una dependencia precisa. Y hay un deber expreso de las autoridades de <strong>no exigir documentos que ya reposan en la entidad</strong>. Se radica con su fecha, que es la que hace correr el término.',
  'Devolverlo por falta de formalidades desconoce la naturaleza del derecho de petición. Suspender el trámite por un documento que la entidad ya tiene es exactamente lo que la norma prohíbe. Y responder desde la División un asunto contractual ajeno excede su competencia: lo que procede es remitirlo e informarle.'),

 (0,
  'En el punto de atención, una persona mayor pide ayuda para presentar una solicitud. Un compañero le dice que debe traerla escrita a máquina, en el formato de la entidad y con copia de su cédula autenticada, y que mientras tanto no puede radicarse nada. La persona dice que no sabe escribir bien y que vive a tres horas de la ciudad. Otro compañero sugiere que se devuelva y que vuelva otro día con alguien que la ayude.',
  '¿Cuál es la actuación correcta?',
  ['Recibir la petición, incluso verbal, apoyar a la persona para dejarla por escrito si es necesario, radicarla con su fecha y entregarle constancia, sin exigir formatos ni autenticaciones que la ley no pide.',
   'Entregarle el formato de la entidad y explicarle que debe traerlo diligenciado, porque la uniformidad de los documentos es lo que permite tramitar las peticiones de manera ordenada y oportuna.',
   'Recibir la petición pero advertirle por escrito que no se tramitará hasta que aporte copia autenticada de su documento de identidad, requisito necesario para acreditar quién está solicitando.',
   'Remitirla a la oficina jurídica para que allí la asistan en la redacción, porque la División no tiene entre sus funciones ayudar a los ciudadanos a formular sus solicitudes por escrito.'],
  'Correcto. El CPACA admite las <strong>peticiones verbales</strong> y prohíbe exigir requisitos no previstos en la ley, como formatos propios o autenticaciones. Y el deber de las autoridades no es solo recibir: es <strong>facilitar</strong>, con especial cuidado hacia quien está en situación de vulnerabilidad. La constancia de radicación es su garantía.',
  'Exigir un formato propio, una autenticación o un trámite previo son precisamente las prohibiciones que el código impone a las autoridades. Y trasladarla a otra oficina para que «la ayuden» es desatender un deber que es de quien atiende.'),

 (1,
  'Llega a su puesto una petición en la que una persona pide que se revise la liquidación de una prestación. Al abrirla usted advierte que la peticionaria es su hermana, con quien no tiene ningún conflicto y a quien no ve hace meses. El grupo está corto de personal, el término ya está corriendo y nadie en la División conoce el parentesco. Usted está seguro de poder tramitar el asunto con total objetividad y, además, es quien más rápido lo resolvería.',
  '¿Cuál es la actuación correcta?',
  ['Tramitar la petición con normalidad y dejar al final una constancia en el expediente que advierta el parentesco, de modo que quien revise el trámite pueda valorarlo si lo considera pertinente.',
   'Manifestar el impedimento por escrito ante el competente antes de intervenir, describiendo el parentesco, y dejar constancia; quien decide dispondrá quién continúa el trámite.',
   'Tramitar la petición porque el impedimento solo opera cuando quien decide es el pariente, y usted no decide nada: se limita a verificar soportes y a proyectar la respuesta que otro firmará.',
   'Pedirle a un compañero que firme el proyecto en su lugar, conservando usted la elaboración del documento, de modo que el trámite avance sin que su nombre aparezca en la actuación.'],
  'Correcto. El <strong>impedimento</strong> se manifiesta <strong>por escrito y antes de intervenir</strong>, y lo resuelve quien es competente. Que usted se sienta objetivo no desplaza la regla, porque lo que protege la norma es también la <strong>apariencia</strong> de imparcialidad, que es lo que sostiene la confianza en la actuación.',
  'Dejar la constancia al final invierte el orden: la decisión sobre su participación debe tomarse antes. Y decir que no hay impedimento porque usted «solo proyecta» desconoce que quien prepara la actuación influye en ella. Repartir la firma con un compañero es, además, ocultar el vínculo.'),

 (3,
  'Una petición compleja fue radicada el día 2. Al estudiarla, usted advierte que para responderla de fondo hay que pedir información a dos dependencias y revisar un expediente que está en el archivo central, y que no alcanzará a resolverse dentro del término. Un compañero le dice que lo mejor es mandar antes del vencimiento un oficio diciendo que «la solicitud se encuentra en trámite» y responder de fondo cuando se tenga todo listo. Faltan cuatro días para el vencimiento y el archivo central informó que el expediente solo puede consultarse la semana entrante.',
  '¿Cuál es la actuación correcta?',
  ['Enviar el oficio informando que la solicitud se encuentra en trámite, porque con ello se da respuesta dentro del término y la respuesta de fondo puede remitirse cuando se complete la información.',
   'Responder dentro del término con la información disponible, aunque sea parcial, y advertir que lo faltante se complementará después, de modo que la respuesta quede formalmente rendida a tiempo.',
   'Dejar vencer el término y responder de fondo cuando se tenga todo, porque una respuesta completa y bien fundamentada protege mejor a la entidad que una respuesta apresurada e incompleta.',
   'Informar al peticionario, antes del vencimiento, la imposibilidad de responder en el término, explicando los motivos y señalando el plazo en que se responderá, sin exceder el que la norma permite.'],
  'Correcto. El CPACA prevé exactamente esta situación: cuando no es posible responder en el término, hay que <strong>informarlo al peticionario antes de su vencimiento</strong>, <strong>explicando los motivos</strong> y <strong>señalando el plazo</strong> en que se responderá, que no puede exceder el que la norma permite. Eso es una prórroga; un «está en trámite» no lo es.',
  'Un oficio que dice que el asunto está en trámite no resuelve nada, no interrumpe el término y deja a la entidad en falta. Una respuesta parcial que promete completarse después tampoco es respuesta de fondo. Y dejar vencer el término es, simplemente, incumplir.'),

 (0,
  'Se radica en la División una petición en la que una persona reclama por una actuación contractual que corresponde a otra dependencia de la entidad. Un compañero propone devolverla al peticionario indicándole a dónde debe dirigirse. Otro propone archivarla porque «aquí no es». El término ya empezó a correr desde la radicación, el peticionario dejó un correo electrónico de notificación y en el escrito advierte que es la tercera vez que intenta que le resuelvan el asunto.',
  '¿Cuál es la actuación correcta?',
  ['Remitirla a la dependencia competente dentro del término que la norma prevé e informar de ello al peticionario, dejando constancia de la remisión y de la comunicación enviada.',
   'Devolverla al peticionario con una nota que le indique cuál es la dependencia competente, para que la presente directamente allí y el trámite comience ante quien debe resolverlo.',
   'Archivarla dejando constancia de que la División carece de competencia, porque continuar un trámite para el que no se es competente vicia la actuación desde su inicio.',
   'Responderla desde la División con la información que se pueda obtener de la otra dependencia, porque el peticionario tiene derecho a una respuesta de quien recibió su escrito.'],
  'Correcto. La falta de competencia <strong>no se resuelve devolviendo</strong>: el CPACA obliga a <strong>remitir al competente dentro del término</strong> e <strong>informar al peticionario</strong>. Eso protege al ciudadano, que no tiene por qué conocer la estructura interna de la entidad, y evita que el término se pierda.',
  'Devolver o archivar traslada al peticionario una carga que es de la entidad y puede costarle el término. Y responder desde la División un asunto que no le compete produce una respuesta de quien no podía darla.'),

 (2,
  'Una persona pide copia completa del expediente de un trámite de personal de otro servidor. Afirma que es información pública porque se trata de una entidad del Estado y que la Ley de Transparencia le da derecho a conocerla. El expediente contiene, entre otros documentos, incapacidades médicas y la hoja de vida del servidor. La persona no acredita autorización del titular ni calidad alguna en el trámite, e insiste en que la negativa sería censura.',
  '¿Cuál es la actuación correcta?',
  ['Entregar el expediente completo, porque la información en poder de las entidades públicas es pública por regla general y la negativa debe ser excepcional y de interpretación restrictiva.',
   'Negar la solicitud sin más explicación, porque se trata de información de un tercero y la entidad no está obligada a motivar las negativas cuando están de por medio datos personales.',
   'Responder dentro del término explicando de manera motivada qué documentos no pueden entregarse y por qué, entregar lo que sí sea accesible y advertir que procede recurso contra esa negativa.',
   'Trasladar la solicitud al servidor titular del expediente para que sea él quien decida si autoriza la entrega, y responder al peticionario lo que el titular manifieste al respecto.'],
  'Correcto. La publicidad es la regla y la reserva la excepción, pero la excepción existe: los <strong>datos personales</strong> —y con mayor razón los de salud— están protegidos. Lo que el CPACA exige es una respuesta <strong>motivada</strong>, que distinga qué se entrega y qué no, con la norma que lo justifica, y que advierta que <strong>procede recurso</strong>.',
  'Entregar todo desconoce la protección de los datos del tercero. Negar sin motivar incumple una exigencia expresa del código. Y trasladar la decisión al titular convierte en consulta privada lo que es una decisión de la autoridad.'),

 (1,
  'Una servidora pide que se revoque un acto que le negó un reconocimiento. Al estudiar el caso, usted advierte que lo que se decida puede afectar a otra servidora, que ocupa un empleo relacionado y que no ha intervenido en la actuación. Un compañero le dice que no la vincule, «porque entre más gente, más se complica y más se demora». El término corre, la peticionaria presiona y la tercera servidora no tiene forma de enterarse del trámite por otra vía.',
  '¿Qué corresponde hacer?',
  ['Resolver sin vincular a la tercera, porque la actuación se inició a petición de una sola persona y ampliarla de oficio excede lo que la peticionaria solicitó expresamente a la entidad.',
   'Comunicar la existencia de la actuación a la tercera que puede resultar afectada, para que pueda hacerse parte y ejercer su derecho de defensa, y dejar constancia de esa comunicación.',
   'Resolver y, una vez expedida la decisión, notificarla a la tercera para que, si no está de acuerdo, pueda interponer los recursos que procedan contra el acto que ya fue adoptado.',
   'Suspender la actuación hasta que la tercera manifieste por escrito si tiene interés en el asunto, y reanudarla únicamente cuando ella responda o cuando venza el plazo que se le otorgue.'],
  'Correcto. Cuando la decisión puede afectar a un <strong>tercero determinado</strong>, el CPACA obliga a <strong>comunicarle la existencia de la actuación</strong> para que pueda hacerse parte. No es una cortesía ni una demora evitable: es debido proceso, y omitirlo vicia lo actuado.',
  'No vincularla por agilidad es exactamente lo que después anula la decisión. Notificarla al final la obliga a recurrir algo en cuya formación no pudo intervenir. Y suspender la actuación a la espera de su respuesta paraliza el trámite sin fundamento.'),

 (3,
  'Un servidor le pregunta cuál es el término para responder su solicitud. Usted revisa y encuentra que en un mismo escrito pidió tres cosas: copia de su acta de posesión, un concepto sobre si puede acumular vacaciones de dos vigencias, y que se revise la liquidación de su prima de servicios. Un compañero le dice que «todas las peticiones son quince días hábiles y listo». El servidor quiere una respuesta clara hoy mismo porque necesita saber para qué fecha debe estar pendiente de cada una de las tres cosas que pidió.',
  '¿Qué debe precisar?',
  ['Que el término es el mismo para las tres, porque el CPACA fijó un plazo general y uniforme para todas las peticiones con el fin de dar certeza a quien se dirige a la administración.',
   'Que el término se cuenta desde que la entidad reúne toda la información necesaria para responder, de modo que no es posible anticipar una fecha mientras el expediente no esté completo.',
   'Que debe presentar tres escritos separados, uno por cada solicitud, porque peticiones de naturaleza distinta no pueden tramitarse ni responderse dentro de un mismo documento.',
   'Que el CPACA fija términos distintos según el tipo de petición —uno general, otro más corto para documentos o información y otro más amplio para consultas— y que las tres deben resolverse.'],
  'Correcto. Los términos <strong>no son uniformes</strong>: el código distingue el término general, el más corto de las peticiones de <strong>documentos e información</strong> y el más amplio de las <strong>consultas</strong>. Y las tres solicitudes deben resolverse: responder unas y callar otras es una respuesta incongruente.',
  'Afirmar que todo es un solo plazo es el error más común en este tema. El término corre desde la radicación, no desde que la entidad se organiza. Y nada impide pedir varias cosas en un solo escrito: lo que la entidad debe hacer es resolverlas todas.'),

 (0,
  'Un ciudadano radica una petición y deja como dirección de notificación un correo electrónico, autorizando expresamente que se le notifique por ese medio. Al momento de responder, un compañero le dice que lo más seguro es enviar la respuesta por correo físico «porque el electrónico no tiene validez» y otro, que basta con dejar la respuesta disponible en el expediente por si el ciudadano la consulta. El término vence en dos días.',
  '¿Cuál es la actuación correcta?',
  ['Enviar la respuesta al correo electrónico autorizado, dejando constancia del envío y de su fecha, porque el peticionario aceptó expresamente ese medio y el CPACA lo admite.',
   'Enviar la respuesta por correo físico a pesar de la autorización, porque el medio escrito ofrece mayor seguridad jurídica y evita discusiones posteriores sobre la fecha de recibo.',
   'Dejar la respuesta disponible en el expediente y publicar un aviso en la cartelera de la entidad, de modo que el peticionario pueda consultarla cuando lo estime conveniente.',
   'Llamar al peticionario y leerle la respuesta por teléfono, dejando constancia escrita de la llamada, de modo que conozca el contenido dentro del término sin depender del correo.'],
  'Correcto. El CPACA admite la <strong>notificación y comunicación electrónica</strong> cuando el interesado la <strong>autoriza expresamente</strong>, y aquí la autorizó. Lo esencial es dejar <strong>constancia del envío y de su fecha</strong>, porque de ahí se cuentan los términos que siguen.',
  'Ignorar el medio autorizado para usar otro «más seguro» desconoce la voluntad del peticionario y puede retrasar la respuesta. Dejarla en el expediente o en una cartelera no es comunicar. Y una lectura telefónica no constituye respuesta.'),

 (1,
  'En una reunión, un compañero sostiene que los principios del artículo 3 del CPACA «son declaraciones generales sin consecuencia práctica» y propone no mencionarlos en los proyectos de respuesta para no alargarlos. Otro sostiene que basta con citarlos todos al comienzo de cada documento. El jefe le pide a usted una posición, porque la semana entrante revisarán la plantilla de respuestas de la División y quiere saber qué se conserva y qué se quita de ella.',
  '¿Cuál es la posición correcta?',
  ['El compañero tiene razón: los principios orientan la actuación pero no generan obligaciones concretas, de modo que su mención es prescindible en los documentos que produce la dependencia.',
   'Los principios son normas con efectos concretos —vinculan la interpretación y la actuación—, de modo que lo útil no es citarlos todos sino aplicar los pertinentes y que eso se note en la decisión.',
   'Deben citarse todos al comienzo de cada documento, porque así se acredita ante cualquier revisión que la actuación se ajustó al marco normativo que rige el procedimiento administrativo.',
   'Solo deben mencionarse cuando la decisión es desfavorable al peticionario, porque es allí donde la entidad necesita respaldar su posición frente a un eventual recurso o acción judicial.'],
  'Correcto. Los principios del <strong>artículo 3</strong> —debido proceso, igualdad, imparcialidad, buena fe, celeridad, economía, eficacia, publicidad, coordinación, entre otros— son <strong>normas</strong>: vinculan la interpretación y la actuación. Lo que no sirve es citarlos de adorno; lo que sirve es que la decisión muestre cómo se aplicaron.',
  'Tratarlos como declaraciones sin efecto desconoce su fuerza normativa. Citarlos todos de entrada es decoración. Y usarlos solo cuando conviene a la entidad invierte su función: existen para proteger al administrado, no para blindar la decisión.'),

 (2,
  'Una persona presenta una petición anónima en la que denuncia una irregularidad concreta en un trámite de personal y aporta datos verificables. Un compañero le dice que se archive de inmediato «porque sin nombre no hay petición» y otro, que se responda publicándola en la cartelera. El escrito no pide nada para el peticionario: pide que se verifique un hecho. Nadie en la División sabe quién lo presentó y el escrito no deja ninguna dirección ni correo de contacto.',
  '¿Qué corresponde hacer?',
  ['Archivarla de inmediato, porque el derecho de petición supone un peticionario identificado y sin él no existe un titular a quien deba dirigirse la respuesta de la entidad.',
   'Responderla mediante publicación en la cartelera de la entidad, de modo que quien la presentó pueda conocer el resultado sin necesidad de identificarse ante la administración.',
   'Darle trámite a la información que contiene, porque un anónimo con datos concretos y verificables obliga a la entidad a verificar el hecho, aunque no haya a quién notificar una respuesta.',
   'Devolverla al buzón de sugerencias y dejar constancia de que se recibió, porque la entidad no puede iniciar actuaciones a partir de documentos cuyo autor no está plenamente identificado.'],
  'Correcto. El anonimato no borra la información. Cuando el escrito aporta <strong>datos concretos y verificables</strong>, la entidad tiene el deber de <strong>verificar el hecho</strong>, aunque no haya destinatario a quien notificar una respuesta. Lo que no existe es la obligación de responder a quien no se identificó.',
  'Archivar por anónimo desperdicia una información que puede ser cierta. Publicar en cartelera no es responder a nadie y expone datos sin necesidad. Y mandar al buzón de sugerencias una denuncia concreta es devolverla al punto de partida.'),

 (0,
  'Un compañero le muestra una respuesta que proyectó: después de tres párrafos de antecedentes y citas normativas, concluye que «se procederá conforme a lo dispuesto en las normas vigentes». El peticionario había preguntado si tiene derecho a que se le reconozca una prima y desde cuándo. El compañero le dice que así se protege la entidad, porque no se compromete con nada, y que el jefe siempre firma ese tipo de cierre. El peticionario ya había radicado el mismo asunto dos meses antes.',
  '¿Cuál es la observación correcta?',
  ['La respuesta no resuelve de fondo ni es congruente con lo preguntado: debe decir si procede o no el reconocimiento y desde cuándo, con su fundamento, e indicar los recursos si es desfavorable.',
   'La respuesta es adecuada porque cita el fundamento normativo aplicable y evita comprometer a la entidad con una posición que podría resultar desfavorable en una eventual controversia judicial.',
   'La respuesta debe complementarse únicamente con la transcripción completa de las normas citadas, de modo que el peticionario pueda extraer por sí mismo la conclusión que corresponde a su caso.',
   'La respuesta es suficiente siempre que se notifique personalmente al peticionario, porque la notificación personal permite aclararle verbalmente cualquier duda sobre el sentido de la decisión.'],
  'Correcto. Una respuesta debe ser <strong>de fondo, clara, precisa y congruente</strong> con lo pedido. Decir que «se procederá conforme a las normas vigentes» no responde si tiene derecho ni desde cuándo. Y si la decisión es desfavorable, debe <strong>indicar los recursos</strong> que proceden.',
  'No comprometerse no protege a la entidad: la expone, porque una respuesta evasiva equivale a no responder. Transcribir normas no reemplaza la decisión. Y ninguna forma de notificación sanea una respuesta que no resuelve.'),

 (3,
  'Una petición fue radicada el viernes 28 a las 4:50 de la tarde, diez minutos antes del cierre. Un compañero le dice que el término empieza a contarse desde el lunes siguiente «porque llegó sobre la hora» y otro, que desde el mismo viernes. En la semana siguiente hay un festivo. El peticionario llama preguntando exactamente para qué fecha tendrá respuesta y usted quiere darle un dato correcto, porque de esa fecha depende que él sepa cuándo puede insistir.',
  '¿Cómo deben contarse los términos?',
  ['Desde el mismo viernes, contando todos los días calendario hasta completar el plazo, porque los términos del CPACA corren de manera continua salvo norma expresa en contrario.',
   'Desde el lunes siguiente, contando días calendario, porque una radicación hecha al filo del cierre se entiende presentada el primer día hábil siguiente a su recepción material.',
   'Desde el mismo viernes, contando días calendario pero descontando únicamente el festivo de la semana siguiente, por tratarse de un día en que la entidad no presta atención al público.',
   'Desde el día hábil siguiente a la radicación, contando días hábiles y excluyendo sábados, domingos y festivos, de modo que el festivo de esa semana no se computa en el plazo.'],
  'Correcto. Los términos del CPACA se cuentan en <strong>días hábiles</strong>, empezando el <strong>día hábil siguiente</strong> a la radicación, y se excluyen sábados, domingos y festivos. Contarlos mal es la causa más frecuente de respuestas extemporáneas, y el dato que usted le dé al peticionario debe ser exacto.',
  'Contar días calendario acorta indebidamente el plazo real de la entidad y confunde al peticionario. Y la hora de radicación no corre la fecha: el escrito presentado dentro del horario se radica ese día, y el término arranca al día hábil siguiente.'),

 (1,
  'Un jefe de dependencia envía un correo pidiendo un concepto sobre si puede encargar a un servidor que no cumple uno de los requisitos del empleo. Un compañero le dice que eso debe responderse en el término general de las peticiones y que la respuesta «vincula a la entidad, así que hay que tener cuidado». El jefe insiste en que necesita una posición clara para decidir esta semana, y advierte que si la División no responde a tiempo procederá con el encargo bajo su propia responsabilidad.',
  '¿Qué debe precisar sobre la naturaleza de esa solicitud?',
  ['Que es una petición en interés particular, con el término general, y que la respuesta obliga a la entidad porque define la situación concreta del servidor que se pretende encargar.',
   'Que es una consulta, con un término propio más amplio, y que la respuesta no es de obligatorio cumplimiento ni compromete la responsabilidad de quien la emite, sin perjuicio de su valor orientador.',
   'Que no es una petición de ninguna clase por provenir de un servidor de la entidad, de modo que puede responderse informalmente por correo sin registrar la solicitud ni su respuesta.',
   'Que es una petición de información, con el término más corto, porque lo que se pide es que la División informe cuáles son los requisitos exigidos para el empleo en cuestión.'],
  'Correcto. Es una <strong>consulta</strong>: se pide una opinión sobre materias a cargo de la autoridad. Tiene un <strong>término propio, más amplio</strong>, y su respuesta <strong>no obliga ni compromete la responsabilidad</strong> de quien la emite. Eso no la vuelve irrelevante: orienta, y por eso debe ser rigurosa.',
  'No es una petición particular ni de información: no se pide que se decida ni que se informe un dato, sino un criterio. Y el hecho de que venga de un servidor no la saca del régimen de peticiones ni autoriza a no registrarla.'),

 (2,
  'Un peticionario presenta un escrito que, por su contenido, es incomprensible: mezcla reclamos de varias épocas, no precisa qué pide y adjunta documentos sin relación aparente. Un compañero propone responder «lo que se entienda» y otro, archivarlo por falta de claridad. El escrito trae datos de contacto completos y fue radicado hace tres días, de modo que todavía hay margen dentro del término para gestionar lo que corresponda.',
  '¿Cuál es la actuación correcta?',
  ['Responder lo que razonablemente se entienda del escrito, porque es preferible una respuesta aproximada dentro del término que exponer a la entidad a un incumplimiento por no responder.',
   'Archivarlo dejando constancia de que no fue posible establecer qué se solicitaba, porque la entidad no está obligada a interpretar escritos cuyo contenido resulta incomprensible.',
   'Requerir al peticionario para que complete o aclare su solicitud dentro del plazo que la norma prevé, informándole con precisión qué debe aclarar y qué ocurre si no lo hace.',
   'Citarlo a una reunión en la entidad para que explique verbalmente lo que pide y, con base en esa explicación, proyectar la respuesta que corresponda a lo que manifieste.'],
  'Correcto. Cuando la petición está incompleta o es incomprensible, el CPACA prevé <strong>requerir al peticionario</strong> para que la complete o aclare, dentro del plazo previsto, informándole qué debe aclarar y cuál es la consecuencia de no hacerlo. Es lo que suspende el término sin perjudicar a nadie.',
  'Responder «lo que se entienda» produce una respuesta incongruente, que es como no responder. Archivar sin requerir le niega al peticionario la oportunidad de corregir. Y citarlo a una reunión impone una carga que la norma no prevé, sobre todo a quien vive lejos.'),
]
