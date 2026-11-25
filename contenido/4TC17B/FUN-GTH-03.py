# -*- coding: utf-8 -*-
"""Día 16 · Talento humano III: compensación, nómina y seguridad social."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _brenda import base, meta

META = meta(
    codigo='FUN-GTH-4TC17B-03',
    archivo='FUN-GTH-4TC17B-03-compensacion-nomina-seguridad-social.html',
    dia=16,
    titulo_doc='Talento humano III: compensación, nómina y seguridad social',
    h1='Talento humano III<br>Compensación, nómina y seguridad social',
    kicker='Día 16 · Conocimiento específico',
    sub='El día más <strong>operativo</strong> del bloque y el que más consecuencias tiene si se hace mal, porque aquí los errores se traducen en dinero. Verás la <strong>estructura salarial</strong> del empleo público y por qué la asignación básica es reglada, qué es un <strong>factor salarial</strong> y para qué sirve, las <strong>prestaciones sociales</strong> y su base de liquidación, el <strong>ciclo de la nómina</strong> y el trámite de las <strong>novedades</strong>, la <strong>seguridad social</strong> (afiliaciones, aportes, PILA, incapacidades), las <strong>deducciones</strong> y el principio de <strong>inembargabilidad</strong> del salario con sus excepciones, y la <strong>liquidación definitiva</strong> al retiro. Y, con módulo propio, qué parte de todo esto hace la División de Gestión Humana y qué parte no.',
    badges=['⏱ 100-120 min', '💵 Nómina y prestaciones', '📖 Específico'],
    fmeta='Talento humano III: compensación, nómina y seguridad social (Ley 100 de 1993, Decreto 1083 de 2015 y Decreto Ley 262 de 2000)',
    alerta='Talento humano III: compensación, nómina y seguridad social',
)

MOD_PGN = '''
      <div class="modulo-head"><div class="modulo-n">★</div><h3>Qué hace —y qué no hace— la División de Gestión Humana con la nómina</h3></div>
      <div class="b-texto">
        <p>Este módulo aterriza todo lo anterior en tu puesto de trabajo. El <strong>artículo 63 del Decreto Ley 262 de 2000</strong> reparte la materia salarial y prestacional entre tres actores, y confundirlos es el error que más veces aparece en las preguntas de este tema.</p>
        <div class="tabla-wrap"><table>
          <thead><tr><th>Tarea</th><th>Quién</th><th>Norma</th></tr></thead>
          <tbody>
            <tr><td><strong>Elaborar las nóminas</strong>, con apoyo de la Oficina de Sistemas</td><td><strong>División de Gestión Humana</strong></td><td>art. 63, núm. 10</td></tr>
            <tr><td>Conservar la <strong>nómina, los salarios y las prestaciones</strong> del personal vinculado y <strong>expedir certificaciones</strong> sobre ellos</td><td><strong>División de Gestión Humana</strong></td><td>art. 63, núm. 3</td></tr>
            <tr><td>Tramitar las <strong>novedades</strong> y la <strong>afiliación a EPS y fondos de pensiones</strong></td><td><strong>División de Gestión Humana</strong></td><td>art. 63, núm. 5</td></tr>
            <tr><td><strong>Reconocer</strong> las prestaciones sociales, los viáticos y los gastos de viaje</td><td>Secretaría General</td><td>art. 62, núm. 7</td></tr>
            <tr><td>Dirigir y controlar el manejo presupuestal, contable y de <strong>tesorería</strong>, y el pago</td><td>División Financiera</td><td>art. 65, núm. 1</td></tr>
            <tr><td>Verificar la <strong>disponibilidad presupuestal</strong> y expedir los certificados</td><td>División Financiera</td><td>art. 65, núm. 8</td></tr>
          </tbody>
        </table></div>
        <div class="ojo"><b>Ojo en la prueba:</b> fíjate en la diferencia entre <mark>elaborar</mark>, <mark>reconocer</mark> y <mark>pagar</mark>. La División de Gestión Humana <strong>elabora</strong> la nómina y <strong>tramita</strong> las novedades; la Secretaría General <strong>reconoce</strong> las prestaciones; la División Financiera <strong>paga</strong>. Cuando una opción diga que Gestión Humana «reconoce» una prima o «paga» una liquidación, desconfía. Y dentro de la propia División, recuerda tu límite: tú <strong>verificas, registras y proyectas</strong>; no reconoces y no firmas.</div>
        <h4>Por qué la asignación básica no se negocia</h4>
        <p>La asignación básica del empleo público es <strong>reglada</strong>: la fija anualmente el Gobierno Nacional por decreto, según el empleo y el grado, y no depende de la antigüedad de quien lo ocupe, de su título ni de lo que acuerde con un jefe. Para el <strong>Técnico en Criminalística 4TC-17</strong>, el formato de la Convocatoria 285-2026 reporta una asignación básica de <strong>$8.972.318</strong> (vigencia 2025). Ese número no es negociable, y ninguna dependencia puede ofrecer más ni menos por el mismo empleo y grado: hacerlo sería desconocer el decreto salarial.</p>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Una servidora radica una incapacidad médica de ocho días el día 27, cuando la nómina del mes ya se cerró. Usted no puede «meterla a la fuerza» ni dejarla sin registrar: la <strong>radica con su fecha real</strong>, la registra como novedad del período correspondiente y verifica cómo se aplica —los primeros días a cargo de la entidad y el resto a cargo de la EPS, según el origen y la duración—. Si por el cierre debe aplicarse en el período siguiente, eso se documenta: la novedad no desaparece, se traslada con constancia. Y el documento de la incapacidad, que contiene un diagnóstico, es un <strong>dato sensible</strong>: se maneja con reserva.</p>
          </div>
        </div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> la División de Gestión Humana <strong>elabora</strong> las nóminas (art. 63, núm. 10), <strong>conserva</strong> la nómina, los salarios y las prestaciones y <strong>expide certificaciones</strong> (núm. 3), y <strong>tramita</strong> las novedades y las afiliaciones a EPS y pensiones (núm. 5). La Secretaría General <strong>reconoce</strong> las prestaciones, los viáticos y los gastos de viaje (art. 62, núm. 7) y la División Financiera maneja el presupuesto y el <strong>pago</strong> (art. 65). El Técnico en Criminalística 4TC-17 verifica, registra y proyecta dentro de la primera: no reconoce, no paga y no firma.</p></div>
      </div>
'''

SEC = base('guias/FUN-GHI-04-gestion-compensacion-nomina-seguridad-social.html', MOD_PGN, aviso=False)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre salario, '
              'factores salariales, prestaciones, nómina, novedades, seguridad social y deducciones. Aquí los '
              'errores se traducen en dinero: lee con atención quién elabora, quién reconoce y quién paga.')

P = [
 (2,
  'Un servidor recién posesionado en un empleo del nivel técnico se acerca a su puesto. Dice que tiene una maestría y diez años de experiencia, que en su empleo anterior ganaba más y que su jefe «ya le dijo que le iban a reconocer algo adicional» por su perfil. Le pide a usted que proyecte lo necesario para que su asignación básica quede por encima de la del grado, y le comenta que otro compañero del mismo grado, según él, gana más. Usted sabe que la asignación del grado la fija cada año un decreto del Gobierno Nacional.',
  '¿Cuál es la respuesta correcta?',
  ['Proyectar el ajuste solicitado, porque el perfil y la experiencia del servidor justifican objetivamente una asignación superior a la del grado y la entidad puede reconocerla por acto motivado.',
   'Verificar primero cuánto gana el compañero que él menciona y, si efectivamente es más, igualar las dos asignaciones para no vulnerar el derecho a la igualdad entre servidores del mismo grado.',
   'Explicarle que la asignación básica es reglada: la fija el Gobierno Nacional por decreto según el empleo y el grado, no depende del perfil ni de lo que acuerde un jefe, y orientarlo sobre el canal si considera que hay un error.',
   'Explicarle que no puede hacer nada y que su única alternativa es renunciar y volver a concursar por un empleo de grado superior, porque la asignación de su empleo actual no admite revisión de ningún tipo.'],
  'Correcto. La asignación básica del empleo público es <strong>reglada</strong>: la fija anualmente el Gobierno Nacional por decreto, según el empleo y el grado. Ni el título, ni la experiencia, ni la promesa de un jefe la modifican. Lo que sí cabe es orientar: si él cree que hay un error en lo que se le está liquidando, eso se revisa por el canal.',
  'Reconocer una asignación superior a la del grado desconoce el decreto salarial. Comparar con lo que gana otro servidor —y de paso consultar su dato— no es la vía, y la diferencia puede tener explicación legítima en factores distintos de la asignación básica. Y decirle que no hay nada que hacer le cierra un canal que sí existe.'),

 (3,
  'Un servidor le pregunta por qué en su desprendible aparece un descuento por aportes a salud y pensión, si él «no pidió ningún servicio este mes». Añade que un compañero le dijo que esos aportes son voluntarios para los servidores públicos y que puede pedir que se los dejen de descontar para recibir más en efectivo. Le pide a usted que le tramite la suspensión del descuento a partir del próximo mes y, si no se puede, que le explique por escrito quién lo obliga a aportar.',
  '¿Qué debe explicarle?',
  ['Que puede suspender los aportes si firma una autorización en la que asuma por escrito las consecuencias, porque se trata de una decisión que afecta únicamente su propio patrimonio futuro.',
   'Que los aportes son obligatorios solo mientras dure el período de prueba y que, superado este, el servidor puede optar entre el régimen contributivo y un plan voluntario de su elección.',
   'Que puede solicitar la devolución de los aportes de los meses en que no utilizó los servicios, presentando la solicitud ante la EPS con copia a la División de Gestión Humana.',
   'Que los aportes al Sistema de Seguridad Social Integral son obligatorios por mandato legal, no dependen de que se usen los servicios y no pueden suspenderse por voluntad del servidor ni de la entidad.'],
  'Correcto. La afiliación y la cotización al Sistema de Seguridad Social Integral son <strong>obligatorias por mandato legal</strong> (Ley 100 de 1993): no son un servicio que se contrate ni dependen de que se use. Ni el servidor ni la entidad pueden pactar su suspensión, y la entidad responde como aportante.',
  'No hay autorización que vuelva voluntario lo obligatorio, ni un régimen distinto al superar el período de prueba, ni devolución por no haber usado los servicios: el sistema es de aseguramiento, no de pago por uso.'),

 (0,
  'Un servidor solicita que se le reconozca la prima técnica porque, según él, «cumple los requisitos de sobra» y porque a un compañero de otra dependencia se la reconocieron el año pasado. Le pide a usted que la incluya directamente en la nómina del próximo mes «para no alargar el trámite», y le dice que el acto administrativo «se puede hacer después, cuando haya tiempo». El trámite de la prima técnica tiene requisitos propios que usted todavía no ha verificado.',
  '¿Cuál es la actuación correcta?',
  ['Explicarle que ningún factor se incluye en la nómina sin acto administrativo previo que lo reconozca, verificar qué soportes exige el trámite, dejar la solicitud radicada y encauzarla hacia el competente.',
   'Incluir el factor en la nómina del próximo mes y proyectar el acto administrativo en paralelo, de modo que el servidor no pierda un mes de pago mientras se surte la formalidad del reconocimiento.',
   'Negarle el trámite porque la prima técnica es un reconocimiento excepcional que solo procede para los niveles directivo y asesor, de modo que un servidor de otro nivel no puede siquiera solicitarla.',
   'Verificar qué le reconocieron al compañero de la otra dependencia y, si la situación es equivalente, incluir el mismo factor para evitar un trato desigual entre servidores de la misma entidad.'],
  'Correcto. La regla es simple y vale para cualquier factor: <strong>primero el acto administrativo que reconoce, después la nómina que paga</strong>. Un pago sin acto previo es un pago sin causa, con las consecuencias fiscales que eso tiene para quien lo elaboró. Su papel es verificar soportes, radicar y encauzar al competente.',
  'Pagar primero y formalizar después invierte el orden y deja el pago sin respaldo. Negar de plano la solicitud desconoce el derecho de petición. Y replicar lo que se le reconoció a otro, sin acto propio, multiplica el problema en vez de resolverlo.'),

 (1,
  'Una servidora radica el día 27 una incapacidad médica de ocho días, cuando la nómina del mes ya se cerró. Un compañero le dice que la registre con fecha del día 2 del mes siguiente «para que cuadre con el período» y otro, que la guarde sin radicar hasta el mes entrante. La servidora pregunta además si eso afecta su pago y quién asume los días. El documento trae el diagnóstico, el número de días y el origen común de la incapacidad, y la servidora pide que nadie más en la oficina se entere del motivo.',
  '¿Cuál es la actuación correcta?',
  ['Registrar la incapacidad con la fecha del mes siguiente para que coincida con el período de nómina en que se aplicará, de modo que el sistema no rechace la novedad por extemporánea.',
   'Radicar la incapacidad con su fecha real, registrarla como novedad del período que corresponde, documentar que por el cierre se aplicará en el siguiente, informar a la servidora y manejar el diagnóstico con reserva.',
   'Guardar el documento sin radicarlo hasta el mes entrante y entregarlo entonces, para evitar que quede una novedad pendiente de aplicación en un período de nómina ya cerrado.',
   'Radicarla con su fecha real y aplicarla de inmediato reabriendo la nómina del mes, porque una incapacidad es una novedad de obligatoria aplicación en el período en que se presenta.'],
  'Correcto. La fecha real es intocable: cambiarla es falsear el registro, y de ella dependen el conteo de días y quién los asume. Lo correcto es radicar con su fecha, registrar la novedad y documentar que el cierre la traslada al período siguiente. Y el diagnóstico es un <strong>dato sensible</strong>: se maneja con reserva.',
  'Antedatar o posfechar una novedad es falsear un registro del que depende dinero. Guardarla sin radicar deja a la servidora sin constancia de haberla presentado. Y reabrir una nómina cerrada por iniciativa propia no está en sus manos: lo que sí está es documentar y avisar.'),

 (2,
  'Llega a la División un oficio judicial que ordena el embargo del salario de un servidor por una obligación alimentaria. El mismo servidor tiene además una libranza vigente con una entidad financiera y pide que se suspenda el descuento de la libranza «porque con el embargo no le alcanza». Un compañero le dice que el salario es inembargable y que el oficio debe devolverse al juzgado. El oficio precisa el porcentaje ordenado y el despacho que lo profirió.',
  '¿Qué es lo correcto?',
  ['El salario es inembargable sin excepciones, de modo que el oficio debe devolverse al juzgado explicando que la entidad no puede dar trámite a la orden de embargo sobre un salario público.',
   'El salario es embargable sin límite cuando la orden proviene de autoridad judicial, de manera que debe descontarse la totalidad de lo ordenado y suspenderse la libranza para hacer efectiva la orden.',
   'El salario es inembargable como regla, pero la ley admite excepciones —entre ellas las alimentarias—, de modo que la orden se cumple dentro de los límites legales y la libranza no se suspende.',
   'La libranza debe suspenderse automáticamente porque el embargo judicial tiene prelación sobre cualquier descuento voluntario, y así se garantiza que el servidor conserve un ingreso suficiente.'],
  'Correcto. La <strong>inembargabilidad del salario es la regla</strong>, pero tiene excepciones legales, y las <strong>obligaciones alimentarias</strong> son la más conocida: allí el embargo procede, dentro de los límites que la ley fija. La libranza, por su parte, nace de una autorización del servidor con una entidad financiera: la División no la suspende por su cuenta.',
  'Devolver el oficio desconociendo una orden judicial legítima expone a la entidad. Descontar sin límite desconoce los topes legales. Y suspender la libranza «automáticamente» es decidir sobre una relación contractual ajena: lo que corresponde es aplicar la orden en sus términos y orientar al servidor sobre dónde gestionar la libranza.'),

 (0,
  'Al liquidar las prestaciones de un servidor que se retira, usted debe establecer la base de liquidación. Un compañero le dice que «se toma todo lo que aparece en el desprendible, que para eso lo recibió» e incluye en su cálculo un auxilio que la norma no define como factor salarial. Otro sostiene que solo se toma la asignación básica y nada más. El servidor pregunta cuándo le pagan y advierte que ya consultó con un abogado. Usted tiene a la vista el detalle de los conceptos que recibió durante el último año y la norma que define cuáles son factor.',
  '¿Cómo debe establecer la base?',
  ['Tomar la asignación básica y los factores que la norma define expresamente como salariales para esa prestación, verificando cada uno contra su fundamento, y excluir lo que no tenga esa naturaleza.',
   'Tomar todo lo que el servidor recibió durante el período, porque cualquier suma percibida con ocasión del servicio hace parte de su remuneración y debe reflejarse en la base de liquidación.',
   'Tomar únicamente la asignación básica, porque es el único concepto reglado por decreto y cualquier otro factor introduce un riesgo de sobrepago que la entidad no debe asumir.',
   'Tomar la base que el propio servidor indique en su solicitud, siempre que la respalde con los desprendibles correspondientes, y advertirle que cualquier diferencia se ajustará después del pago.'],
  'Correcto. No todo lo que se recibe es <strong>factor salarial</strong>: la norma define, para cada prestación, cuáles conceptos integran la base. Hay sumas que se perciben con ocasión del servicio y no constituyen factor —auxilios, reembolsos—, y hay factores que sí lo son. La verificación es concepto por concepto, contra su fundamento.',
  'Incluir todo genera sobrepago y un posible detrimento; limitarse a la asignación básica genera un pago incompleto y una reclamación fundada. Y dejar que el interesado defina la base invierte por completo el papel de quien liquida.'),

 (1,
  'Un servidor ingresó el día 20 del mes y usted debe reportar la novedad de afiliación. Un compañero le dice que lo reporte con fecha del primer día del mes siguiente «porque así el período queda completo y es más fácil de cuadrar». Otro, que lo reporte desde el día 1 de este mes «para que no quede ningún día descubierto». El servidor se posesionó y empezó a trabajar el día 20, y el acto de nombramiento se había expedido tres semanas antes.',
  '¿Cómo debe reportarse la novedad?',
  ['Desde el primer día del mes siguiente, porque las novedades de ingreso que ocurren después de la mitad del mes se consolidan en el período inmediatamente posterior para efectos del reporte.',
   'Desde la fecha real de inicio de la relación laboral, el día 20, porque la afiliación y la cotización se causan desde que comienza el vínculo y el reporte debe reflejar la realidad.',
   'Desde el día 1 del mes en curso, porque así se evita cualquier riesgo de que el servidor quede sin cobertura durante los primeros días de su vinculación con la entidad.',
   'Desde la fecha de expedición del acto de nombramiento, con independencia de cuándo se haya posesionado, porque es ese acto el que crea la relación jurídica con la entidad.'],
  'Correcto. El reporte sigue la <strong>realidad</strong>: la cobertura y la cotización se causan desde que comienza la relación, y la relación comienza con la posesión, no con la comodidad del cierre contable. Reportar la fecha real es además lo que protege al servidor si ocurre algo en esos días.',
  'Posfechar deja al servidor sin cobertura en días en que ya estaba trabajando, y la responsabilidad de ese vacío recae en la entidad. Antedatar reporta una cotización por días en que no había vínculo. Y la fecha del acto de nombramiento no es la del inicio del vínculo: esa es la de la posesión.'),

 (3,
  'Un servidor reclama porque este mes le descontaron retención en la fuente y el mes pasado no. Sostiene que «eso es un error de la nómina» y que la entidad no puede descontarle impuestos sin su autorización. Le pide a usted que le devuelva el valor descontado en el pago siguiente y que no vuelva a aplicarlo. Usted verifica y confirma que el cálculo corresponde al procedimiento aplicado y que este mes el servidor recibió, además del salario, el pago de un factor que elevó su base gravable.',
  '¿Qué debe explicarle?',
  ['Que tiene razón y que el descuento se le reintegrará en el pago siguiente, porque ninguna deducción puede practicarse sobre el salario sin autorización expresa y previa del servidor.',
   'Que la retención solo se aplica a los servidores de los niveles directivo y asesor, de modo que si se le descontó a él se trata efectivamente de un error que debe corregirse de inmediato.',
   'Que la retención depende de que el servidor haya autorizado el procedimiento al inicio del año y que, si no lo hizo, puede solicitar que se le aplique el que le resulte más favorable en cada mes.',
   'Que la retención en la fuente es una obligación legal del empleador como agente retenedor, que no requiere autorización del servidor y que varía según los ingresos del período y el procedimiento aplicable.'],
  'Correcto. La <strong>retención en la fuente</strong> no es una deducción voluntaria: es una obligación legal que la entidad cumple como <strong>agente retenedor</strong>. Que un mes se descuente y otro no se explica por la variación de los ingresos del período y por el procedimiento aplicable, no por un error.',
  'No hay reintegro por falta de autorización, porque la autorización no se requiere. La retención no distingue por nivel jerárquico. Y el procedimiento no se escoge mes a mes según conveniencia: tiene reglas propias de determinación y de vigencia.'),

 (1,
  'Un servidor pregunta por qué no le consignaron sus cesantías a comienzos de año «como a su hermano», que trabaja en una empresa privada. Agrega que necesita retirarlas para pagar una deuda de tarjeta de crédito y le pide a usted que tramite el retiro parcial. Usted verifica su fecha de vinculación y confirma a qué régimen de cesantías pertenece, y revisa para qué finalidades la norma autoriza el retiro parcial. El servidor insiste en que el dinero es suyo y que puede darle el uso que quiera.',
  '¿Qué debe precisar?',
  ['Que las cesantías se pagan directamente al servidor cada año en el mes de febrero y que puede destinarlas a cualquier finalidad, incluido el pago de obligaciones de consumo como la que menciona.',
   'Que el régimen de cesantías depende de la fecha de vinculación —anualizado con consignación al fondo, o retroactivo con pago al retiro— y que el retiro parcial solo procede para las finalidades que la ley autoriza.',
   'Que las cesantías solo se pagan al momento del retiro definitivo del servicio, sin excepción, de modo que ningún servidor activo puede disponer de ellas mientras conserve su vínculo con la entidad.',
   'Que el servidor puede elegir libremente cada año entre el régimen anualizado y el retroactivo, según le convenga, informando su decisión a la División antes del cierre de la vigencia correspondiente.'],
  'Correcto. Dos ideas. La primera: el <strong>régimen de cesantías depende de la fecha de vinculación</strong> —el anualizado consigna al fondo cada año; el retroactivo se liquida al retiro—. La segunda: el <strong>retiro parcial</strong> no es libre, solo procede para las finalidades que la ley autoriza, típicamente vivienda y educación. Una deuda de consumo no está entre ellas.',
  'Ni todos los regímenes consignan en febrero, ni todas las cesantías esperan al retiro, ni el régimen se elige año a año: lo determina la fecha de vinculación. Y autorizar un retiro parcial para una finalidad no prevista expone el trámite y a quien lo proyectó.'),

 (2,
  'Al revisar la base de aportes de un servidor, usted advierte que durante varios meses se incluyó en ella un concepto que, según la norma, no constituye factor salarial. Un compañero le dice que lo deje así «porque cotizar de más no perjudica a nadie y hasta le conviene al servidor para su pensión». Otro, que lo corrija de inmediato sin informar a nadie para que no se note. La diferencia acumulada es significativa y los aportes ya fueron girados a las administradoras.',
  '¿Cuál es la actuación correcta?',
  ['Dejar la base como está, porque una cotización superior a la debida beneficia al servidor en su pensión futura y no causa perjuicio alguno a la entidad ni al sistema de seguridad social.',
   'Corregir la base de inmediato en la nómina siguiente, sin informar, para que la diferencia deje de acumularse y el asunto no genere alarma en el equipo ni en el servidor afectado.',
   'Documentar el hallazgo con precisión, informarlo por el canal al competente y abstenerse de corregir por decisión propia, porque la corrección tiene efectos sobre aportes ya pagados y sobre el propio servidor.',
   'Consultar al servidor si prefiere que se corrija o que se mantenga la base actual, y actuar conforme a lo que él responda, dejando constancia escrita de su manifestación de voluntad.'],
  'Correcto. Un error en la <strong>base de aportes</strong> no es un detalle contable: afecta dinero público ya pagado, los derechos pensionales del servidor y la relación con las administradoras. Por eso no se corrige en silencio ni se perpetúa: se <strong>documenta y se informa</strong>, y el competente decide cómo se corrige y con qué efectos.',
  'Cotizar de más sí tiene consecuencias: es un pago sin causa con recursos públicos. Corregir en silencio borra el rastro de un error que alguien debe conocer. Y la base de aportes no depende de lo que el servidor prefiera: la fija la norma.'),

 (0,
  'Un servidor se retira con efectos del día 18 del mes. El jefe de su dependencia le pide a usted que proyecte la liquidación definitiva «como si saliera el 30, que es más fácil de calcular y de todos modos son unos días». El servidor, por su parte, pregunta si le pagarán el mes completo y si eso cambia su liquidación de vacaciones. Usted tiene a la vista el acto de retiro firmado, con su fecha, y la hoja de tiempo de servicio.',
  '¿Cómo debe proyectar la liquidación?',
  ['Con la fecha real de retiro que fija el acto, el día 18, liquidando hasta ese día los conceptos que correspondan, y explicar al servidor cómo se calculó cada uno.',
   'Con la fecha del día 30, como pide el jefe, porque la diferencia es de pocos días y simplifica un cálculo que de otro modo exigiría prorratear varios conceptos del período.',
   'Con la fecha del día 18 para el salario pero con el mes completo para las prestaciones, porque estas se causan por períodos mensuales y no admiten liquidación por fracción de mes.',
   'Con la fecha que el servidor prefiera entre las dos, siempre que lo manifieste por escrito, porque se trata de una diferencia menor que no afecta derechos de terceros ni recursos públicos.'],
  'Correcto. La fecha de retiro la fija el <strong>acto administrativo</strong>, no la conveniencia del cálculo: liquidar hasta el día 18 es lo que corresponde, prorrateando lo que haya que prorratear. Y explicar el cálculo no es un favor: es lo que evita la reclamación posterior.',
  'Liquidar hasta el día 30 paga doce días no trabajados con recursos públicos. Mezclar fechas entre salario y prestaciones no tiene fundamento: las prestaciones también se liquidan por el tiempo efectivamente servido. Y la fecha no se negocia con el interesado.'),

 (0,
  'Un servidor estuvo suspendido en el ejercicio del cargo durante dos meses por una medida de autoridad competente. La medida fue levantada y la autoridad ordenó el reconocimiento de los valores dejados de percibir. El servidor llega a su puesto pidiendo que «le paguen ya» y un compañero le dice que basta con incluir el valor en la nómina del próximo mes, porque la orden ya existe. Usted no ha verificado todavía ni la liquidación de los valores ni la disponibilidad presupuestal.',
  '¿Cuál es la actuación correcta?',
  ['Verificar y liquidar los valores conforme a la orden, proyectar lo que corresponda para el acto del competente y la disponibilidad presupuestal, e informar al servidor el estado real del trámite y los tiempos.',
   'Incluir el valor en la nómina del próximo mes, porque la orden de la autoridad competente es suficiente título para el pago y cualquier trámite adicional solo retrasaría un derecho ya reconocido.',
   'Explicar al servidor que los valores dejados de percibir durante una suspensión no se reconocen en ningún caso, porque durante ese período no hubo prestación efectiva del servicio.',
   'Esperar a que el servidor presente una petición escrita de reconocimiento, porque sin solicitud del interesado la entidad no puede iniciar de oficio un trámite de pago a su favor.'],
  'Correcto. La orden crea el derecho, pero el pago necesita su propio camino: <strong>liquidación verificada, acto del competente y respaldo presupuestal</strong>. Su tarea es que ese camino se recorra rápido y bien, y que el servidor sepa en qué va. Meter el valor directo a la nómina salta dos pasos que después nadie puede reconstruir.',
  'Ni el pago directo sin acto ni la negativa de plano son correctos. Y tampoco hace falta esperar una petición: la orden de la autoridad competente es la que activa el trámite, no la insistencia del interesado.'),

 (3,
  'Un exservidor solicita una certificación de los salarios y factores que devengó durante sus últimos tres años, para un trámite pensional. Un compañero le dice que la División no expide certificaciones a quien ya no trabaja en la entidad y que debe pedirla al fondo de pensiones. El exservidor insiste en que la necesita con urgencia, ofrece dejar una copia de su cédula y dice que si no se la expiden hoy perderá el turno que le asignó el fondo. Se retiró hace cuatro años y su historia laboral está en el archivo central.',
  '¿Qué corresponde hacer?',
  ['Explicarle que la División solo certifica sobre personal vinculado, de modo que debe solicitar la información al fondo de pensiones, que es quien administra su historia de aportes.',
   'Entregarle de inmediato una impresión de los desprendibles que estén en el sistema, porque es la información que él pide y así se resuelve su urgencia sin necesidad de un trámite formal.',
   'Negarle la certificación porque los datos salariales son información reservada y su entrega requeriría autorización judicial, dado que se destinarán a un trámite ante un tercero.',
   'Recibir y radicar la solicitud, verificar su identidad como titular, proyectar la certificación con los datos que arrojen los registros de la entidad y tramitarla para la firma del competente.'],
  'Correcto. El numeral 3 del artículo 63 encarga a la División <strong>conservar</strong> la nómina, los salarios y las prestaciones y <strong>expedir certificaciones</strong> sobre ellos: ese deber no se extingue cuando la persona se retira, porque los registros de su vinculación siguen en la entidad. Se radica, se verifica la identidad del titular, se proyecta y la firma el competente.',
  'El fondo administra los aportes, pero no puede certificar lo que la entidad pagó: esa información es suya. Entregar una impresión informal no es una certificación y no sirve para un trámite pensional. Y no hay reserva frente al propio titular: lo que hay es un deber de verificar que quien pide es quien dice ser.'),

 (2,
  'Al cerrar la nómina usted detecta que a un servidor se le pagó de más durante cuatro meses por un factor mal parametrizado en el sistema. El servidor no lo advirtió y el valor acumulado es considerable. Un compañero le dice que lo descuente todo de la nómina del próximo mes «antes de que alguien pregunte» y otro, que lo deje así porque «el error fue de la entidad y el servidor ya se lo gastó». La parametrización equivocada sigue activa y volverá a aplicarse en el cierre del próximo mes.',
  '¿Cuál es la actuación correcta?',
  ['Descontar el total en la nómina del mes siguiente, porque se trata de recursos públicos pagados sin causa y su recuperación inmediata evita que el detrimento siga creciendo.',
   'No hacer nada y corregir solo hacia adelante, porque el error fue imputable a la entidad y exigir la devolución de un pago que el servidor recibió de buena fe sería desproporcionado.',
   'Documentar el hallazgo con el detalle de los períodos y los valores, corregir la parametrización hacia adelante e informarlo por el canal al competente, sin decidir por su cuenta la forma de recuperar lo pagado.',
   'Hablar primero con el servidor y acordar con él un plan de descuentos que le resulte cómodo, dejando constancia escrita del acuerdo para formalizarlo después ante el competente.'],
  'Correcto. Dos cosas distintas: <strong>corregir el error hacia adelante</strong> es de su resorte técnico y debe hacerse ya; <strong>recuperar lo pagado de más</strong> no lo es, porque toca derechos del servidor, exige su propio procedimiento y lo decide el competente. Usted documenta, corrige la parametrización e informa.',
  'Descontar el total de un golpe afecta el mínimo vital y se hace sin procedimiento. No hacer nada deja un detrimento sin reportar. Y acordar directamente con el servidor un plan de descuentos es decidir un asunto que no está en sus manos, por bienintencionado que sea.'),

 (0,
  'La Oficina de Sistemas le informa que el aplicativo de nómina presentará una falla durante dos días, justo en la semana del cierre. Su jefe está de vacaciones y el calendario de pago no se puede mover. Un compañero propone liquidar esos dos días en una hoja de cálculo paralela «y después subirlo todo», y otro propone avisar al final, cuando se sepa si alcanzó a afectar el cierre. Son más de mil servidores los que dependen de ese pago y la Oficina de Sistemas no ha confirmado todavía la hora exacta en que el aplicativo volverá a estar disponible.',
  '¿Cuál es la actuación correcta?',
  ['Informar de inmediato la contingencia por el canal, con su impacto estimado en el cierre, documentar lo que se avance y actuar conforme a lo que se disponga, dejando constancia del procedimiento usado.',
   'Liquidar en una hoja de cálculo paralela y cargar los datos cuando el aplicativo se restablezca, porque lo importante es que el calendario de pago se cumpla sin afectar a los servidores.',
   'Esperar a que el jefe regrese de vacaciones para que él decida, porque se trata de una contingencia que excede la competencia de quien opera la nómina y nadie más puede autorizar un cambio.',
   'Avisar al final de la semana, una vez se confirme si la falla alcanzó a afectar el cierre, para no generar una alarma que podría resultar innecesaria si el aplicativo se restablece a tiempo.'],
  'Correcto. Una contingencia que puede afectar el pago se <strong>informa cuando se conoce, no cuando se confirma el daño</strong>: eso es lo que permite que alguien con competencia decida a tiempo. Mientras tanto, se avanza en lo que se pueda y se deja constancia del procedimiento efectivamente usado.',
  'Una liquidación paralela fuera del aplicativo rompe la trazabilidad y los controles del sistema. Esperar al regreso del jefe desatiende una urgencia que tiene otros canales. Y avisar al final convierte una contingencia manejable en un incumplimiento consumado.'),

]
