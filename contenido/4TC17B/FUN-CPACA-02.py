# -*- coding: utf-8 -*-
"""Día 12 · CPACA II: procedimiento, acto administrativo, notificaciones, recursos, silencio y firmeza."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol, modulos, armar
from _brenda import IDENTIDAD, CARGO, PLURAL, meta
from _lib import aplicar_todas as _ap
from _regimen import TODAS as _REGIMEN

META = meta(
    codigo='FUN-CPACA-4TC17B-02',
    archivo='FUN-CPACA-4TC17B-02-procedimiento-acto-notificaciones-recursos.html',
    dia=12,
    titulo_doc='CPACA II: procedimiento, acto administrativo, notificaciones, recursos, silencio y firmeza',
    h1='CPACA II<br>Procedimiento, acto administrativo, notificaciones, recursos y firmeza',
    kicker='Día 12 · Conocimiento específico',
    sub='La segunda mitad del CPACA, y la que más se parece a tu día a día: el <strong>procedimiento administrativo general</strong> paso a paso, la <strong>decisión</strong> y sus exigencias de motivación, las <strong>publicaciones, citaciones, comunicaciones y notificaciones</strong> —personal, por aviso y electrónica—, los <strong>recursos</strong> contra los actos administrativos con sus términos y requisitos, el <strong>silencio administrativo</strong> negativo y positivo, y la <strong>firmeza</strong> del acto con la presunción de legalidad y la constancia de ejecutoria. Todo lo que proyectas en la División de Gestión Humana pasa por aquí.',
    badges=['⏱ 100-120 min', '⚖️ CPACA', '📖 Específico'],
    fmeta='CPACA II: procedimiento, acto administrativo, notificaciones, recursos, silencio y firmeza (Ley 1437 de 2011)',
    alerta='CPACA II: procedimiento, acto administrativo, notificaciones, recursos, silencio y firmeza',
)

S = secciones_mapeadas('guias/FUN-ADM-09-cpaca-principios-procedimiento.html')
cabeza, mods = modulos(S[2])
S[2] = armar(cabeza, mods, set(range(8, 16)))

CIERRE = '''
      <div class="modulo-head"><div class="modulo-n">★</div><h3>El acto de personal, leído con el CPACA en la mano</h3></div>
      <div class="b-texto">
        <p>Cierra el día aterrizando todo lo anterior en el documento que más vas a producir: el <strong>acto administrativo de personal</strong>. Un nombramiento, un encargo, el reconocimiento de una prima, la negativa de una licencia, un retiro. Cada uno recorre exactamente el mismo camino, y cada escalón tiene su regla.</p>
        <div class="tabla-wrap"><table>
          <thead><tr><th>Escalón</th><th>Qué exige el CPACA</th><th>Qué pasa si falla</th></tr></thead>
          <tbody>
            <tr><td><strong>Competencia</strong></td><td>Que lo expida quien la norma faculta: la División, la Secretaría General o el Procurador, según el asunto (arts. 62 y 63 del Decreto Ley 262).</td><td>Nulidad por falta de competencia. Es el vicio más difícil de sanear.</td></tr>
            <tr><td><strong>Motivación</strong></td><td>Hechos, norma aplicada y razón de la decisión. No basta citar artículos.</td><td>El interesado no puede defenderse; el acto queda expuesto.</td></tr>
            <tr><td><strong>Notificación o comunicación</strong></td><td>Personal, por aviso o electrónica cuando se autorizó; con constancia de fecha.</td><td>El acto <strong>no produce efectos</strong> frente a quien no fue notificado.</td></tr>
            <tr><td><strong>Indicación de recursos</strong></td><td>En la notificación personal: qué recursos proceden, ante quién y en qué término.</td><td>La notificación es irregular y el término no corre en contra del interesado.</td></tr>
            <tr><td><strong>Firmeza</strong></td><td>Cuando vencen los términos sin recursos, o se resuelven los interpuestos.</td><td>Ejecutar un acto que no está en firme es ejecutar lo que aún se discute.</td></tr>
          </tbody>
        </table></div>
        <div class="ojo"><b>Ojo en la prueba:</b> hay una secuencia que no se puede invertir y que resuelve muchas preguntas: <mark>se expide, se notifica, queda en firme y se ejecuta</mark>. Registrar una novedad en la nómina, dar de baja a alguien del sistema o posesionar a un reemplazo antes de que el acto esté en firme es adelantarse a un paso que todavía puede cambiar. Y recuerda el otro límite, el de siempre: la División <strong>proyecta</strong>, el competente <strong>firma</strong>.</div>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Se expide el acto que niega a una servidora el reconocimiento de una prima. Usted lo notifica personalmente, le entrega copia íntegra y le indica que procede recurso de reposición, ante quién y en qué término. Ella dice que no está de acuerdo pero que «lo pensará». <strong>No</strong> es el momento de archivar el expediente ni de responder a la dependencia que el asunto quedó cerrado: el acto <strong>no está en firme</strong> mientras corra el término para recurrir. Lo que corresponde es dejar el control del término y esperar. Si vence sin recurso, entonces sí: constancia de ejecutoria y archivo.</p>
          </div>
        </div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> todo acto de personal es un acto administrativo y recorre siempre el mismo camino: lo expide <strong>quien es competente</strong>, va <strong>motivado</strong>, se <strong>notifica o comunica</strong> con constancia, indica los <strong>recursos</strong> que proceden, adquiere <strong>firmeza</strong> y solo entonces se <strong>ejecuta</strong>. Un defecto en cualquiera de esos escalones compromete el acto entero, y casi siempre el defecto nace en el trámite, no en la decisión. Ahí es exactamente donde trabaja el Técnico en Criminalística 4TC-17.</p></div>
        <div class="box ok"><div class="box-title">💡 Idea clave del día</div><p><strong>Idea clave:</strong> la pregunta que debes hacerte frente a cualquier acto que pase por tus manos es <strong>«¿en qué escalón va?»</strong>. Expedido no es notificado; notificado no es en firme; en firme no es ejecutado. Casi todas las preguntas de este día —y casi todos los problemas reales de un expediente de personal— consisten en alguien que quiso saltarse un escalón por urgencia. El escalón saltado es, después, el vicio que anula el acto.</p></div>
        <div class="box ojo"><div class="box-title">🗣️ Frase para recordar</div><p>«Se expide, se notifica, queda en firme y se ejecuta. En ese orden, siempre, por urgente que sea. — Día 12»</p></div>
      </div>
'''
S[2] = S[2] + CIERRE
SEC = aplicar_todas(S, IDENTIDAD + [('Gestor II', 'Técnico en Criminalística 4TC-17'), ('Gestor', 'Técnico en Criminalística 4TC-17')], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(CARGO, PLURAL), estricto=False)

SEC = _ap(SEC, _REGIMEN, estricto=False)   # carrera especial PGN, no CNSC

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el '
              'procedimiento administrativo, la decisión, las notificaciones, los recursos, el silencio '
              'administrativo y la firmeza. Antes de responder, pregúntate siempre en qué escalón va el acto.')

P = [
 (1,
  'Se expide un acto que niega a una servidora el reconocimiento de una prima. Un compañero intenta notificarla personalmente, pero ella no se presenta pese a haber sido citada. Pasados varios días, el compañero le dice a usted que «ya se intentó, así que se entiende notificada» y propone registrar la decisión en el sistema y archivar el expediente. La servidora dejó en su solicitud una dirección física y un correo electrónico, pero no autorizó la notificación electrónica.',
  '¿Cuál es la actuación correcta?',
  ['Dar por surtida la notificación y archivar, porque la citación se envió oportunamente y la inasistencia de la interesada no puede paralizar indefinidamente la actuación de la entidad.',
   'Proceder a la notificación por aviso a la dirección registrada, con copia íntegra del acto y la indicación de los recursos, y dejar constancia de su envío y de la fecha de entrega.',
   'Enviar el acto al correo electrónico que la servidora registró en su solicitud, porque señalarlo como dato de contacto equivale a aceptar que se le notifique por ese medio.',
   'Publicar el acto en la cartelera de la entidad durante cinco días hábiles, de modo que la publicidad supla la notificación personal que no fue posible realizar por causa de la interesada.'],
  'Correcto. Cuando la notificación personal no se logra, el CPACA prevé la <strong>notificación por aviso</strong>: se remite a la dirección registrada, con <strong>copia íntegra del acto</strong> y la indicación de los <strong>recursos</strong>, y se deja constancia. La inasistencia no equivale a notificación.',
  'Dar por surtida la notificación por la sola citación deja el acto sin efectos frente a la interesada. El correo solo sirve si se autorizó expresamente, y aquí no se autorizó. Y la cartelera no es el medio previsto para notificar un acto de contenido particular.'),

 (3,
  'Un servidor fue notificado personalmente de un acto el día 10 y, al recibirlo, manifestó verbalmente que «no está de acuerdo y lo va a pelear». El día 14 un compañero le pregunta a usted si ya puede registrarse la novedad en el sistema y comunicarle a la dependencia que el asunto quedó resuelto, porque están esperando para reorganizar el trabajo. No se ha radicado ningún recurso y el término para recurrir no ha vencido. La dependencia insiste en que necesita certeza hoy para repartir las funciones de la semana entrante.',
  '¿Cuál es la actuación correcta?',
  ['Registrar la novedad, porque el servidor no ha presentado ningún recurso dentro de los días transcurridos y una manifestación verbal no tiene efecto jurídico alguno sobre el acto.',
   'Registrar la novedad pero advertir a la dependencia que podría revertirse, de modo que el trabajo se reorganice y, si llega un recurso, se deshaga el registro que se hubiera efectuado.',
   'Entender que la manifestación verbal equivale a un recurso de reposición y suspender el trámite hasta que el servidor presente por escrito los argumentos que sustentan su inconformidad.',
   'Esperar a que venza el término para recurrir: mientras corra, el acto no está en firme; llevar el control del término e informar a la dependencia el estado real, sin ejecutar todavía.'],
  'Correcto. El acto <strong>no está en firme</strong> mientras corra el término para recurrir, y lo que no está en firme no se ejecuta. Su papel es llevar el <strong>control del término</strong> e informar el estado real a quien lo necesita, sin adelantarse.',
  'Registrar la novedad —aunque sea «advirtiendo que puede revertirse»— es ejecutar un acto que todavía se puede discutir, con efectos reales sobre el servidor. Y una manifestación verbal no es un recurso: no suspende ni sustituye nada.'),

 (0,
  'Un servidor presenta por escrito, dentro del término, un documento titulado «recurso» contra un acto que le negó un encargo. El escrito expone con claridad por qué considera equivocada la decisión, pero no indica a cuál de los recursos se refiere ni cita el artículo que lo fundamenta. Un compañero propone rechazarlo de plano por no identificar el recurso. Otro propone responderlo como si fuera un derecho de petición nuevo, de modo que se le dé trámite sin reabrir la actuación ya concluida.',
  '¿Cuál es la actuación correcta?',
  ['Darle trámite como el recurso que corresponda según su contenido, porque lo que define el recurso es lo que se pide y no el nombre que el interesado le ponga ni la norma que cite.',
   'Rechazarlo de plano porque no identifica el recurso interpuesto, requisito sin el cual la entidad no puede establecer ante quién debe surtirse ni qué efectos produce su interposición.',
   'Responderlo como una petición nueva, de modo que se le dé respuesta de fondo dentro del término general sin reabrir una actuación que ya había concluido con el acto notificado.',
   'Requerirlo para que precise cuál recurso interpone y, si no responde dentro del plazo que se le otorgue, entender que desistió y archivar la actuación dejando constancia de ello.'],
  'Correcto. Lo que define un recurso es su <strong>contenido</strong>, no su rótulo: si está presentado en término, por quien tiene interés, y expone por qué se discute la decisión, debe tramitarse como el recurso que corresponda. El CPACA favorece el acceso, no las formalidades.',
  'Rechazar de plano por no citar la norma convierte un requisito inexistente en una barrera. Tratarlo como petición nueva le quita el efecto propio del recurso. Y requerirlo bajo amenaza de desistimiento impone una carga injustificada cuando el escrito ya es comprensible.'),

 (2,
  'Un acto administrativo de personal fue notificado personalmente, pero en la diligencia solo se le entregó al interesado un extracto con la parte resolutiva y se le dijo verbalmente que «si quiere, puede reclamar». No se le entregó copia íntegra ni se le indicó qué recurso procede, ante quién ni en qué término. El interesado se presenta un mes después diciendo que quiere recurrir y pregunta si está a tiempo. En el expediente solo reposa el acta de la diligencia, sin constancia de entrega de copia.',
  '¿Cuál es la situación correcta?',
  ['La notificación fue válida porque el interesado compareció y conoció el sentido de la decisión, de modo que el término corrió desde ese día y el recurso resulta extemporáneo.',
   'La notificación fue válida pero el término no corrió, de modo que el interesado puede recurrir en cualquier momento mientras el acto no haya sido ejecutado materialmente por la entidad.',
   'La notificación fue irregular: faltó la copia íntegra y la indicación de los recursos, de modo que no produjo el efecto de hacer correr el término y debe surtirse en debida forma.',
   'La notificación fue irregular pero el defecto quedó saneado por el paso del tiempo, de modo que el acto se entiende en firme y lo que procede es informarle que ya no puede recurrir.'],
  'Correcto. La notificación personal exige <strong>entregar copia íntegra</strong> del acto e <strong>indicar qué recursos proceden, ante quién y en qué término</strong>. Sin eso, la notificación es irregular y <strong>no hace correr el término</strong> en contra del interesado: lo que procede es surtirla en debida forma.',
  'Comparecer no sanea la falta de los elementos esenciales de la diligencia. Y el paso del tiempo no convalida una notificación irregular: precisamente por eso el término no corrió.'),

 (1,
  'Una petición en interés particular fue radicada hace más de tres meses y la entidad no la ha respondido. El peticionario llega preguntando qué pasó y qué puede hacer. Un compañero le dice que «como no hubo respuesta, se entiende aceptada su solicitud» y otro, que «ya no hay nada que hacer porque el plazo venció». El peticionario quiere saber exactamente cuál es su situación y qué puede hacer de aquí en adelante para que su solicitud se resuelva.',
  '¿Qué debe explicarle?',
  ['Que al vencer el plazo sin respuesta operó un silencio positivo y que, en consecuencia, su solicitud se entiende concedida y puede exigir su cumplimiento ante la propia entidad.',
   'Que la regla general es el silencio administrativo negativo —la petición se entiende negada— y que eso le permite acudir a los medios de control, sin que la entidad quede relevada de responder.',
   'Que el vencimiento del plazo extingue su derecho a obtener una respuesta, de modo que su única alternativa es presentar una nueva petición para que el término comience otra vez.',
   'Que el silencio no produce ningún efecto mientras la entidad no expida un acto que lo declare, de modo que debe esperar a que la administración se pronuncie formalmente al respecto.'],
  'Correcto. La regla general es el <strong>silencio administrativo negativo</strong>: transcurrido el plazo sin respuesta, la petición se entiende <strong>negada</strong>, y eso le abre al interesado la puerta de los medios de control. El silencio <strong>positivo</strong> es excepcional y solo opera donde una norma expresa lo prevé. Y la entidad <strong>no queda relevada</strong> de responder.',
  'Dar por concedida la solicitud invierte la regla general. El vencimiento no extingue el derecho a la respuesta. Y el silencio opera por ministerio de la ley: no necesita que la entidad lo declare.'),

 (2,
  'Un servidor interpone recurso de reposición contra un acto que le negó una prima. Mientras el recurso se resuelve, el jefe de su dependencia pide a la División que ejecute el acto, es decir, que no incluya el factor en la nómina del mes y cierre el asunto. Un compañero le dice a usted que el recurso «no detiene nada» porque el acto ya fue notificado y el servidor conoce la decisión. El cierre de la nómina es el viernes y el recurso apenas entró a estudio.',
  '¿Qué debe precisar?',
  ['Que el recurso no afecta la ejecución del acto, porque una vez notificada la decisión produce todos sus efectos hasta que sea revocada o anulada por la autoridad competente.',
   'Que el recurso suspende la ejecución de manera indefinida y que el acto no podrá ejecutarse nunca si el recurrente no manifiesta expresamente su conformidad con lo decidido.',
   'Que la interposición del recurso impide que el acto quede en firme y, por tanto, que se ejecute: debe esperarse a que se resuelva, e informar a la dependencia el estado real del trámite.',
   'Que el recurso solo suspende la ejecución si el recurrente lo pide expresamente y presta una caución que garantice los perjuicios que la demora pueda causar a la entidad.'],
  'Correcto. Un acto recurrido <strong>no está en firme</strong>, y lo que no está en firme no se ejecuta: hay que esperar a que el recurso se resuelva. Su papel es precisarlo y mantener informada a la dependencia del estado real, sin ceder a la presión del cierre.',
  'Decir que el recurso «no detiene nada» confunde notificación con firmeza. La suspensión no es indefinida: dura hasta que el recurso se resuelva. Y no existe caución alguna como condición para ese efecto.'),

 (0,
  'Al revisar un acto ya expedido y notificado, usted advierte que en la parte motiva aparece mal escrito el número de la cédula del servidor y que una fecha quedó transpuesta. El sentido de la decisión y su fundamento son correctos y no cambian. Un compañero propone expedir un acto nuevo que revoque el anterior y otro, dejarlo así porque «se entiende igual» y corregirlo cuando alguien reclame. El acto ya fue archivado en la historia laboral del servidor con esos datos.',
  '¿Cuál es la actuación correcta?',
  ['Proyectar la corrección de los errores formales, que procede en cualquier tiempo y a petición de parte o de oficio, siempre que no se altere el sentido material de la decisión adoptada.',
   'Proyectar la revocatoria del acto y expedir uno nuevo con los datos correctos, porque cualquier error en un acto administrativo afecta su validez y exige retirarlo del ordenamiento.',
   'Dejar el acto como está y anotar la corrección en el expediente interno, porque los errores de transcripción no afectan la decisión y una modificación posterior generaría confusión.',
   'Esperar a que el servidor advierta el error y lo solicite por escrito, porque la entidad no puede modificar de oficio un acto que ya fue notificado y respecto del cual corren términos.'],
  'Correcto. El CPACA prevé la <strong>corrección de errores formales</strong> —de transcripción, de cálculo, aritméticos— en <strong>cualquier tiempo</strong>, de oficio o a petición de parte, con un límite claro: no puede <strong>alterar el sentido material</strong> de la decisión. Aquí no lo altera.',
  'Revocar un acto correcto por un error de transcripción es desproporcionado y abre discusiones innecesarias. Dejarlo mal deja un documento que después no coincidirá con la historia laboral. Y la corrección sí procede de oficio: no hay que esperar al interesado.'),

 (3,
  'Un acto fue notificado y venció el término sin que se presentara ningún recurso. La dependencia pide una constancia de que la decisión ya es definitiva para poder reorganizar el trabajo, y el servidor pregunta si todavía puede hacer algo. Un compañero le dice a usted que la constancia «la puede firmar cualquiera del grupo, que es un trámite menor». Usted tiene a la vista la fecha de notificación y el registro de radicación de recursos.',
  '¿Cuál es la actuación correcta?',
  ['Expedir y firmar usted mismo la constancia, porque se trata de un documento meramente certificativo que se limita a dejar registro de un hecho verificable en el expediente.',
   'Explicar a la dependencia que no existe un documento que acredite la firmeza y que basta con informarle verbalmente que el término venció sin que se presentaran recursos contra el acto.',
   'Esperar un plazo prudencial adicional antes de certificar nada, porque el servidor podría presentar todavía un recurso extemporáneo que la entidad tendría que estudiar antes de cerrar.',
   'Verificar la fecha de notificación y que no se radicaron recursos, proyectar la constancia de ejecutoria para la firma del competente e informar al servidor que el acto quedó en firme.'],
  'Correcto. La <strong>firmeza</strong> se produce cuando vencen los términos sin recursos, y se documenta con la <strong>constancia de ejecutoria</strong>, que se proyecta sobre una verificación —fecha de notificación y ausencia de recursos— y la firma el competente. Esa constancia es la que habilita a ejecutar.',
  'Firmarla usted mismo desconoce el límite de siempre. Decir que no existe tal documento deja a la dependencia sin el respaldo que necesita. Y esperar «por si acaso» un recurso extemporáneo prolonga sin fundamento una situación ya definida.'),

 (1,
  'Un acto de contenido general que afecta a todos los servidores de una sede va a adoptarse. Un compañero propone notificarlo personalmente a cada uno «para que nadie alegue desconocimiento», lo que tomaría varias semanas. Otro propone enviarlo por correo masivo a los servidores y no hacer ningún otro trámite, porque considera que así todos quedan enterados. El acto modifica el horario de atención de la sede y debe empezar a regir el primer día del mes siguiente, de modo que el público también debe poder conocerlo antes de esa fecha.',
  '¿Cuál es la forma correcta de darlo a conocer?',
  ['Notificarlo personalmente a cada servidor, porque es la forma que ofrece mayor certeza sobre el conocimiento efectivo de la decisión por parte de todos los destinatarios del acto.',
   'Publicarlo, que es la forma de dar a conocer los actos de carácter general, en el medio oficialmente previsto para ello, y comunicarlo además por los canales internos de la entidad.',
   'Enviarlo por correo electrónico masivo a todos los servidores de la sede, porque ese medio garantiza la difusión simultánea y deja constancia automática del envío a cada destinatario.',
   'Fijarlo en la cartelera de la sede por un término de diez días hábiles, transcurridos los cuales se entiende notificado personalmente a cada uno de los servidores que allí laboran.'],
  'Correcto. Los actos de <strong>carácter general</strong> se dan a conocer mediante <strong>publicación</strong> en el medio oficialmente previsto, no mediante notificación personal, que es propia de los actos de contenido particular. Comunicarlo además por los canales internos es buena práctica, no sustituto.',
  'Notificar personalmente un acto general es confundir las dos figuras y, además, retrasaría semanas algo que debe regir pronto. El correo masivo y la cartelera son difusión interna, no la publicación que la norma exige.'),

 (2,
  'Un servidor presenta un recurso de reposición dos días después de vencido el término. En el escrito explica que estuvo incapacitado y adjunta la incapacidad médica, que cubre exactamente los días del término. Un compañero propone rechazarlo por extemporáneo sin más y otro, admitirlo sin analizar nada «porque la incapacidad lo justifica todo». El servidor pregunta qué va a pasar y si debe presentar algo más mientras tanto.',
  '¿Cuál es la actuación correcta?',
  ['Admitir el recurso sin analizar la oportunidad, porque una incapacidad médica que cubre el término acredita por sí sola una fuerza mayor que releva de cualquier otra consideración.',
   'Rechazarlo de plano por extemporáneo, porque los términos procesales son perentorios y su vencimiento produce la pérdida de la oportunidad con independencia de las razones alegadas.',
   'Proyectar el estudio del recurso verificando su oportunidad y los soportes aportados, y someter la decisión al competente, informando al servidor el estado real del trámite.',
   'Devolver el escrito al servidor indicándole que presente en su lugar una petición de revocatoria directa, porque es la única vía que queda cuando el término del recurso ya venció.'],
  'Correcto. Aquí hay dos cosas que no le corresponden a usted: decidir si el recurso es oportuno y decidir el fondo. Lo que sí le corresponde es <strong>verificar y documentar</strong> —fechas, soportes— y poner el asunto en manos de quien decide, manteniendo informado al servidor.',
  'Ni admitir ni rechazar por su cuenta: las dos cosas son decisiones del competente. Y orientarlo hacia la revocatoria directa como «única vía» anticipa un rechazo que todavía no se ha producido.'),

 (0,
  'Una servidora pide que se revoque directamente un acto que ya está en firme, porque considera que es manifiestamente contrario a la ley. Un compañero le dice a usted que la revocatoria directa «ya no procede porque el acto quedó en firme» y otro, que «procede siempre y además revive los términos para demandar». La servidora quiere saber si tiene alguna posibilidad y si presentar la solicitud le sirve para ganar tiempo frente a una eventual demanda.',
  '¿Qué debe explicarle?',
  ['Que la revocatoria directa procede frente a actos en firme cuando se configura alguna de las causales legales, y que su solicitud no revive los términos para acudir ante la jurisdicción.',
   'Que la revocatoria directa no procede frente a actos en firme, porque la firmeza cierra definitivamente la posibilidad de que la administración vuelva sobre su propia decisión.',
   'Que la revocatoria directa procede en cualquier caso y por cualquier motivo, y que su sola presentación suspende la ejecución del acto hasta que la entidad resuelva la solicitud.',
   'Que la revocatoria directa solo puede iniciarse de oficio por la propia administración, de modo que la servidora no está legitimada para solicitarla y debe limitarse a demandar el acto.'],
  'Correcto. La <strong>revocatoria directa</strong> es precisamente la figura que permite volver sobre un acto <strong>en firme</strong>, pero solo cuando se configura una de las <strong>causales legales</strong>. Y hay un punto que conviene advertirle con claridad: <strong>no revive los términos</strong> para acudir a la jurisdicción.',
  'Decir que no procede confunde firmeza con intangibilidad. Decir que procede por cualquier motivo y que suspende la ejecución desborda la figura. Y la solicitud de parte sí está prevista: no es una facultad exclusivamente oficiosa.'),

 (3,
  'Al proyectar la respuesta a un recurso, un compañero le propone redactar la decisión así: «estudiados los argumentos del recurrente, no se encuentra mérito para modificar la decisión, la cual se confirma en todas sus partes». El recurso planteaba tres argumentos concretos, dos de ellos con soportes nuevos. El jefe pregunta si así está bien para firmar, porque el término para resolver el recurso vence pasado mañana y no quiere devolverlo si no hace falta.',
  '¿Cuál es la observación correcta?',
  ['Está bien redactada porque expresa con claridad el sentido de la decisión y la confirmación integral del acto recurrido, que es lo que el recurrente necesita conocer para actuar.',
   'Debe añadirse únicamente la transcripción de los tres argumentos del recurrente, sin pronunciarse sobre cada uno, de modo que quede constancia de que fueron leídos por la entidad.',
   'Está bien siempre que se notifique personalmente, porque en esa diligencia puede explicarse verbalmente al recurrente por qué cada uno de sus argumentos resultó insuficiente.',
   'La decisión debe pronunciarse sobre cada uno de los argumentos y sobre los soportes nuevos, con su razón, porque una decisión que no los resuelve no está motivada ni es congruente.'],
  'Correcto. Resolver un recurso es <strong>responder sus argumentos</strong>, uno por uno, y valorar los soportes aportados. Una fórmula que confirma «en todas sus partes» sin decir por qué no está motivada, y deja al recurrente sin saber qué se le rechazó y con qué razón.',
  'Transcribir los argumentos sin resolverlos no los resuelve. Y una explicación verbal en la diligencia de notificación no suple la motivación del acto, que es escrita y debe bastarse a sí misma.'),

 (1,
  'Un servidor que fue notificado de un acto pregunta si puede pedir copia del expediente completo de la actuación en la que se adoptó, incluidos los conceptos internos y los correos entre dependencias. Un compañero dice que solo tiene derecho al acto. Otro, que debe entregársele todo sin excepción. El servidor es el directamente interesado en la actuación y quiere preparar un recurso dentro del término, que todavía está corriendo. En el expediente hay además documentos de un tercero.',
  '¿Cuál es la orientación correcta?',
  ['Solo tiene derecho a copia del acto notificado, porque los documentos internos reflejan el proceso de formación de la decisión y no hacen parte de lo que debe conocer el interesado.',
   'Como interesado tiene derecho a conocer el expediente y a obtener copias, con las salvedades que imponga una reserva legal, y la negativa parcial debe motivarse e indicar que procede recurso.',
   'Debe entregársele absolutamente todo lo que repose en el expediente, incluidos los documentos sujetos a reserva, porque frente al directamente interesado ninguna reserva resulta oponible.',
   'Solo puede consultar el expediente en las instalaciones de la entidad y tomar notas, pero no obtener copias, porque la reproducción de documentos oficiales requiere autorización del jefe.'],
  'Correcto. El interesado tiene derecho a <strong>conocer el expediente y a obtener copias</strong>: es la base de su defensa. Ese derecho tiene límites cuando hay <strong>reserva legal</strong>, pero la negativa —total o parcial— debe ser <strong>motivada</strong> e indicar que <strong>procede recurso</strong>.',
  'Limitarlo al acto le impide preparar su defensa. Afirmar que ninguna reserva le es oponible desconoce los límites legales, incluidos los datos de terceros. Y condicionar las copias a una autorización del jefe es un requisito que la norma no prevé.'),

 (2,
  'Un acto de personal fue firmado por el jefe de la División cuando, según los artículos 62 y 63 del Decreto Ley 262 de 2000, el asunto correspondía a la Secretaría General. El acto ya fue notificado y el servidor empezó a disfrutar de lo reconocido. Un compañero propone no decir nada «porque el beneficio ya se dio y nadie se ha quejado». La situación se repite en otros dos expedientes del mismo mes, firmados por la misma persona y por asuntos de la misma naturaleza.',
  '¿Cuál es la actuación correcta?',
  ['No decir nada, porque el acto produjo efectos favorables al servidor y removerlo ahora le causaría un perjuicio que la entidad tendría que reparar de todos modos.',
   'Proyectar de inmediato un acto que revoque los tres y expedirlos nuevamente con la firma correcta, sin comunicar nada a los servidores para no generar alarma innecesaria.',
   'Documentar el hallazgo con precisión, informarlo por el canal al competente —incluidos los otros dos casos— y abstenerse de decidir por su cuenta cómo se corrige la situación.',
   'Pedir a la Secretaría General que firme ahora los mismos actos con la fecha original, de modo que el expediente quede completo y el defecto de competencia desaparezca del expediente.'],
  'Correcto. La <strong>falta de competencia</strong> es el vicio más grave de un acto administrativo y no se arregla en silencio. Lo que corresponde es <strong>documentar e informar al competente</strong> —señalando que son tres casos, no uno—, y dejar que quien tiene la facultad decida cómo se corrige y con qué efectos.',
  'Callar deja tres actos viciados produciendo efectos. Revocar por su cuenta y sin comunicar a los afectados desconoce sus derechos. Y hacer firmar con fecha original es antedatar un documento: convierte un vicio en una falsedad.'),

 (0,
  'Vence hoy el término para resolver un recurso y el proyecto está listo, pero el competente no ha podido firmarlo porque está en una diligencia fuera de la ciudad y regresa mañana. Un compañero le dice a usted que ponga la fecha de hoy en el documento «y mañana lo firma, que total es un día». Otro propone no hacer nada y esperar al regreso del competente, sin dejar registro de nada. El recurrente ha llamado dos veces preguntando por el estado de su recurso y advirtió que, si no obtiene respuesta, acudirá a otras instancias.',
  '¿Cuál es la actuación correcta?',
  ['Remitir el proyecto por el canal, informar la situación y los tiempos reales a quien corresponda, dejar constancia del vencimiento y mantener informado al recurrente del estado del trámite.',
   'Fechar el documento con la fecha de hoy y hacerlo firmar mañana, porque el proyecto efectivamente estaba terminado dentro del término y un día de diferencia no altera nada sustancial.',
   'No hacer nada y esperar el regreso del competente, porque sin su firma no hay actuación posible y cualquier gestión adicional solo generaría documentos que después habría que corregir.',
   'Pedir a otro servidor del mismo nivel jerárquico que firme la decisión, de modo que el término se cumpla, y dejar constancia de que la firma se hizo por razones de urgencia justificada.'],
  'Correcto. El vencimiento ya no se puede evitar, pero sí se puede manejar bien: <strong>remitir, informar, dejar constancia</strong> y mantener al recurrente al tanto. Eso deja claro qué se hizo, cuándo y por qué, que es lo que después protege a la entidad y al servidor.',
  'Antedatar el documento convierte un retraso explicable en una falsedad. No hacer nada deja el vencimiento sin registro ni explicación. Y hacer firmar a otro servidor es un vicio de competencia, que es peor que el retraso.'),
]
