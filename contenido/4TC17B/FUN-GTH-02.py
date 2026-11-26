# -*- coding: utf-8 -*-
"""Día 15 · Talento humano II: provisión, carrera, situaciones administrativas y retiro."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _brenda import base, meta
from _lib import aplicar_todas as _ap
from _regimen import TODAS as _REGIMEN

META = meta(
    codigo='FUN-GTH-4TC17B-02',
    archivo='FUN-GTH-4TC17B-02-provision-carrera-situaciones-administrativas-retiro.html',
    dia=15,
    titulo_doc='Talento humano II: provisión, carrera, situaciones administrativas y retiro',
    h1='Talento humano II<br>Provisión, carrera, situaciones administrativas y retiro',
    kicker='Día 15 · Conocimiento específico',
    sub='El día del <strong>ciclo de vida del servidor</strong>, y probablemente el más rentable de todo el curso: es lo que harás cada día en la <strong>División de Gestión Humana</strong> y lo que más se pregunta. Verás la <strong>provisión</strong> de los empleos y su orden legal, el <strong>nombramiento y la posesión</strong> (con la verificación de requisitos y el concepto escrito previo que te encarga el art. 63, núm. 7), la <strong>historia laboral</strong> y sus reglas, las <strong>situaciones administrativas</strong> una por una —vacaciones, licencias, permisos, comisiones, encargo, suspensión— distinguiendo las que son <strong>derecho</strong> de las que son <strong>potestativas</strong>, y las <strong>causales de retiro</strong> con sus efectos.',
    fmeta='Talento humano II: provisión, carrera, situaciones administrativas y retiro (Ley 909 de 2004, Decretos 1083 de 2015 y 648 de 2017, y Decreto Ley 262 de 2000)',
    alerta='Talento humano II: provisión, carrera, situaciones administrativas y retiro',
)

MOD_PGN = '''
      <div class="modulo-head"><div class="modulo-n">★</div><h3>Quién decide cada situación administrativa en la PGN</h3></div>
      <div class="b-texto">
        <p>Ya sabes qué es cada situación administrativa. Ahora lo que de verdad decide tus preguntas: <mark>quién la concede</mark>. En la PGN el reparto no está en la Ley 909 sino en los <strong>artículos 62 y 63 del Decreto Ley 262 de 2000</strong>, y es muy fácil de confundir porque las dos dependencias están en la misma línea.</p>
        <div class="tabla-wrap"><table>
          <thead><tr><th>Situación o trámite</th><th>Quién lo decide</th><th>Norma</th></tr></thead>
          <tbody>
            <tr><td>Permiso de estudio <strong>hasta</strong> dos horas diarias</td><td><strong>División de Gestión Humana</strong>, con visto bueno del jefe inmediato</td><td>art. 63, núm. 6</td></tr>
            <tr><td>Permiso de estudio de <strong>más</strong> de dos horas diarias</td><td>Secretaría General, con visto bueno del jefe inmediato</td><td>art. 62, núm. 6</td></tr>
            <tr><td>Vacaciones</td><td>Secretaría General</td><td>art. 62, núm. 6</td></tr>
            <tr><td>Licencias</td><td>Secretaría General</td><td>art. 62, núm. 6</td></tr>
            <tr><td>Comisiones de servicio</td><td>Secretaría General</td><td>art. 62, núm. 6</td></tr>
            <tr><td>Reconocimiento de prestaciones sociales, viáticos y gastos de viaje</td><td>Secretaría General</td><td>art. 62, núm. 7</td></tr>
            <tr><td>Posesión en los niveles directivo, asesor y ejecutivo</td><td>Secretaría General</td><td>art. 62, núm. 5</td></tr>
            <tr><td>Posesión en el nivel central de empleos profesionales, técnicos, administrativos y operativos</td><td><strong>División de Gestión Humana</strong></td><td>art. 63, núm. 8</td></tr>
            <tr><td>Verificación de requisitos y concepto escrito previo a la posesión</td><td><strong>División de Gestión Humana</strong></td><td>art. 63, núm. 7</td></tr>
            <tr><td>Trámite de novedades y situaciones administrativas, y afiliación a EPS y pensiones</td><td><strong>División de Gestión Humana</strong></td><td>art. 63, núm. 5</td></tr>
            <tr><td>Actos de personal, incluidos los de <strong>retiro</strong></td><td>Los <strong>prepara</strong> la División; los <strong>firma</strong> el Procurador General</td><td>art. 63, núm. 5</td></tr>
          </tbody>
        </table></div>
        <div class="ojo"><b>Ojo en la prueba:</b> memoriza dos cosas y tendrás resuelta media docena de preguntas. La primera, <mark>la frontera de las dos horas</mark>: un permiso de estudio de dos horas diarias lo concede la División; de dos horas y media, la Secretaría General. La segunda, <mark>el verbo</mark>: la División <strong>prepara</strong> y <strong>proyecta</strong> los actos de personal, pero quien los <strong>firma</strong> es el Procurador General. Cada vez que una opción diga que la División «expide», «concede» o «firma» un acto de retiro, es incorrecta.</div>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Un servidor radica el lunes una solicitud de comisión de servicios para viajar el jueves, con el visto bueno de su jefe. Usted verifica los soportes, confirma con la División Financiera la disponibilidad de los viáticos y <strong>proyecta</strong> el acto. Pero no lo firma: la comisión de servicios la reconoce la <strong>Secretaría General</strong> (art. 62, núm. 6). Su tarea es que el proyecto llegue completo y a tiempo al escritorio de quien decide, y dejar constancia de cuándo lo remitió. Si el jueves no hay acto firmado, el servidor no puede viajar con cargo a la entidad: por eso el término importa tanto como la exactitud.</p>
          </div>
        </div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> en la PGN las situaciones administrativas las deciden, según el asunto, la <strong>División de Gestión Humana</strong> (permisos de estudio de hasta dos horas, posesión en el nivel central de empleos profesionales, técnicos, administrativos y operativos, verificación de requisitos y trámite de novedades), la <strong>Secretaría General</strong> (vacaciones, licencias, comisiones, prestaciones, viáticos y posesión de directivos, asesores y ejecutivos) o el <strong>Procurador General</strong> (firma de los actos de personal, incluidos los de retiro). El Técnico en Criminalística 4TC-17 verifica, tramita y proyecta; no concede, no reconoce y no firma.</p></div>
      </div>
'''

SEC = base('guias/FUN-GHI-01-gestion-del-empleo-publico.html', MOD_PGN)


SEC = _ap(SEC, _REGIMEN, estricto=False)   # carrera especial PGN, no CNSC

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre provisión, '
              'posesión, historia laboral, situaciones administrativas y retiro. Varias se resuelven con una sola '
              'pregunta previa: ¿quién es el competente para decidir esto?')

P = [
 (0,
  'Llega a su puesto en la División de Gestión Humana el expediente de una persona nombrada en un empleo del nivel técnico del nivel central. El jefe de la dependencia donde va a trabajar llama insistiendo en que la posesión se surta mañana, porque el puesto lleva meses vacío. Al revisar los soportes usted encuentra que el certificado de experiencia de los últimos dos años no precisa las funciones desempeñadas, de modo que no puede establecer si la experiencia es relacionada. El jefe le dice que «eso se completa después» y que la persona ya renunció a su empleo anterior.',
  '¿Cuál es la actuación correcta?',
  ['Consignar por escrito qué acredita cada soporte y cuál requisito no quedó acreditado, requerir la certificación que precise las funciones e informar al competente, dejando constancia de la urgencia planteada.',
   'Emitir el concepto favorable y surtir la posesión mañana, dejando una nota en la historia laboral que advierta que el certificado de experiencia se completará dentro de los días siguientes al acto.',
   'Devolver el expediente a la dependencia solicitante sin emitir concepto alguno, porque mientras el soporte no venga completo no hay actuación posible ni documento que la División deba producir.',
   'Emitir el concepto favorable porque la persona ya renunció a su empleo anterior y negarle la posesión le causaría un perjuicio desproporcionado que la entidad tendría que reparar después.'],
  'Correcto. El numeral 7 del artículo 63 le encarga <strong>verificar los requisitos y emitir concepto escrito antes de la posesión</strong>. Ese concepto dice qué acredita cada documento, y un certificado que no precisa funciones no acredita experiencia relacionada. Usted requiere lo que falta, informa y deja constancia: así protege el acto y a la propia persona.',
  'Posesionar con el requisito sin acreditar expone el nombramiento a nulidad, y una nota que prometa completar el soporte después no sanea nada. Devolver sin emitir concepto deja a la dependencia sin saber qué falta exactamente. Y el perjuicio de quien renunció anticipadamente no habilita a declarar cumplido lo que no está acreditado.'),

 (3,
  'Una servidora radica el lunes una solicitud de permiso para estudiar dos horas diarias los martes y jueves, con el visto bueno de su jefe inmediato. El mismo día, otro servidor radica una solicitud de permiso de estudio de tres horas diarias, también con visto bueno. Su compañero de puesto le dice que proyecte los dos permisos para la firma del jefe de la División, «porque los permisos de estudio son de Gestión Humana y punto». Los dos cursos empiezan la semana entrante.',
  '¿Cómo debe tramitarlos?',
  ['Proyectar los dos para la firma del jefe de la División, porque el artículo 63 le asigna los permisos de estudio sin distinguir la cantidad de horas solicitadas por el servidor.',
   'Proyectar los dos para la firma de la Secretaría General, porque el artículo 62 le atribuye las licencias y los permisos y la División solo prepara los proyectos que aquella suscribe.',
   'Proyectar el de tres horas para la División y el de dos horas para la Secretaría General, porque a mayor afectación del servicio corresponde la instancia de menor jerarquía dentro de la línea.',
   'Proyectar el de dos horas para la División, que es competente hasta ese límite, y el de tres horas para la Secretaría General, que conoce de los que superan las dos horas diarias.'],
  'Correcto. La frontera está en el propio texto: el numeral 6 del artículo 63 faculta a la <strong>División</strong> para conceder los permisos de estudio «que no superen dos horas diarias»; los de más de dos horas, junto con vacaciones, licencias y comisiones, los reconoce la <strong>Secretaría General</strong> (art. 62, núm. 6). Dos horas exactas están dentro; dos y media, ya no.',
  'Ni los dos son de la División, ni los dos son de la Secretaría General. Y la tercera opción invierte la regla: la competencia de la instancia superior se activa cuando el permiso es <strong>mayor</strong>, no menor.'),

 (1,
  'Dos servidores se acercan el mismo día. El primero pide vacaciones para la próxima semana, porque ya cumplió el año de servicio y quiere descansar. El segundo pide una licencia no remunerada de dos meses para atender un asunto personal. Ambos le dicen que «eso es un derecho» y que la entidad no puede negárselo, y le piden que proyecte los dos actos de una vez. Su jefe le pide que, antes de proyectar nada, precise el punto por escrito.',
  '¿Qué distinción debe hacer?',
  ['Ambas son un derecho del servidor y la entidad debe concederlas en los términos pedidos, de modo que lo único que cabe verificar es que los soportes estén completos.',
   'Las vacaciones son un derecho causado una vez cumplido el año, aunque su fecha se concierte según las necesidades del servicio; la licencia no remunerada es potestativa y la entidad puede negarla motivadamente.',
   'Ninguna de las dos es un derecho: ambas dependen de la necesidad del servicio, de modo que la entidad puede negarlas sin necesidad de motivar la decisión en uno u otro caso.',
   'Las vacaciones son potestativas porque su disfrute depende de la necesidad del servicio, y la licencia no remunerada es un derecho porque el servidor no recibe salario durante ella.'],
  'Correcto. Es la distinción que más se pregunta. Las <strong>vacaciones</strong> son un derecho que se causa al cumplir el año de servicio: la entidad no puede negarlas, aunque sí concertar la fecha y, excepcionalmente, aplazarlas por necesidad del servicio con acto motivado. La <strong>licencia no remunerada</strong> es <strong>potestativa</strong>: la entidad puede concederla o negarla, con motivación.',
  'Tratar las dos igual es el error, en cualquiera de los dos sentidos. Y la última opción invierte la regla: que el servidor no reciba salario no convierte la licencia en un derecho, ni la concertación de la fecha convierte las vacaciones en una concesión graciosa.'),

 (2,
  'Al organizar una historia laboral usted encuentra que un documento quedó archivado sin foliar, que hay una copia de un examen médico ocupacional entre los soportes del nombramiento y que faltan dos folios cuya ausencia nadie advirtió. Un compañero le sugiere refoliar toda la carpeta desde el principio «para que quede derechita» y retirar el examen médico «porque ahí no va». El término para entregar la carpeta al archivo central vence el viernes.',
  '¿Cuál es la actuación correcta?',
  ['Refoliar la carpeta completa desde el folio uno y retirar el examen médico sin dejar registro, porque una foliación continua y una carpeta depurada son precisamente lo que exige el archivo central.',
   'Entregar la carpeta como está y advertir verbalmente al archivo central de los tres hallazgos, porque la responsabilidad de corregirlos es de quien conformó la carpeta y no de quien la recibe para remitir.',
   'Dejar constancia escrita de los tres hallazgos, no alterar la foliación existente ni retirar documentos por decisión propia, y consultar por el canal el manejo del documento de salud y la ausencia de folios.',
   'Reconstruir los dos folios faltantes con copias que puedan obtenerse de otras fuentes y refoliar solo el tramo afectado, de modo que la carpeta quede completa antes del vencimiento del viernes.'],
  'Correcto. La historia laboral es un expediente: su <strong>integridad y su trazabilidad</strong> son lo que la hace confiable. Refoliar borra la huella de lo que faltaba, retirar un documento es una decisión de depuración que no le corresponde, y el examen médico ocupacional contiene <strong>datos sensibles de salud</strong> cuyo manejo tiene reglas propias. Lo que corresponde es documentar, no corregir por su cuenta.',
  'Refoliar y depurar destruye precisamente la evidencia del problema; advertir solo verbalmente no deja registro; y «reconstruir» folios faltantes con copias de otras fuentes introduce documentos cuya correspondencia con los originales nadie verificó.'),

 (0,
  'Hay una vacante temporal de un empleo de carrera porque su titular salió en comisión para desempeñar un empleo de libre nombramiento y remoción. Un directivo le pide que proyecte el nombramiento en provisionalidad de una persona externa. En la planta hay dos empleados de carrera que cumplen los requisitos del empleo y tienen calificación sobresaliente, y uno de ellos ya manifestó interés por escrito. El directivo le dice que prefiere a su candidato «porque conoce el área» y que la decisión es suya.',
  '¿Cómo debe encauzar la provisión?',
  ['Verificar si procede el encargo de un empleado de carrera que cumpla los requisitos y tenga calificación satisfactoria, porque el encargo tiene prelación, y dejar constancia escrita de esa verificación.',
   'Proyectar el nombramiento provisional del candidato externo, porque tratándose de una vacante temporal la entidad conserva libertad de designación y el encargo solo opera en las vacantes definitivas.',
   'Proyectar el encargo a favor del empleado de carrera que manifestó interés por escrito, porque esa manifestación expresa le da mejor derecho frente al otro empleado que no se pronunció.',
   'Abstenerse de proyectar cualquier acto e informar al directivo que la vacante temporal no puede proveerse mientras dure la comisión del titular, de modo que las funciones deben redistribuirse.'],
  'Correcto. El <strong>encargo tiene prelación</strong> y opera tanto en vacantes definitivas como temporales: antes de nombrar en provisionalidad hay que verificar si hay un empleado de carrera que cumpla los requisitos y tenga calificación satisfactoria. La <strong>constancia escrita</strong> de esa verificación es lo que después demuestra que el orden se respetó.',
  'La vacante temporal no devuelve libertad de designación. Y haber manifestado interés no da mejor derecho por sí solo: lo que se compara son requisitos y calificación, no quién escribió primero. Tampoco corresponde dejar el empleo sin proveer.'),

 (1,
  'Un servidor fue designado para asistir, durante una semana y en otra ciudad, a una reunión interinstitucional en representación de la entidad. Otro fue designado para desempeñar transitoriamente un empleo de libre nombramiento y remoción. Un tercero solicitó permiso para adelantar un curso de dos semanas en el exterior, costeado por él. Un compañero le dice que «los tres son comisión de servicios, se proyecta el mismo acto y listo».',
  '¿Qué es lo correcto sobre las clases de comisión?',
  ['Las tres son comisión de servicios, porque en todos los casos el servidor se ausenta de su empleo por una causa relacionada con su vida laboral y conserva el vínculo con la entidad.',
   'La primera es comisión de servicios; la segunda, comisión para desempeñar un empleo de libre nombramiento y remoción, que tiene reglas propias; y la tercera, comisión de estudios, con su propio régimen.',
   'Solo la primera es comisión: la segunda es un encargo, porque implica asumir otras funciones, y la tercera es una licencia no remunerada, porque el curso lo costea el propio servidor.',
   'Solo la segunda es comisión propiamente dicha; la primera es un permiso de desplazamiento y la tercera, una licencia de estudios que la entidad concede cuando no asume el costo del programa.'],
  'Correcto. Las comisiones no son una sola figura: la <strong>de servicios</strong> para cumplir funciones propias fuera de la sede o asistir a reuniones y eventos; la <strong>para desempeñar un empleo de libre nombramiento y remoción</strong>, que permite al empleado de carrera ocuparlo conservando su empleo; y la <strong>de estudios</strong>, para adelantar programas de formación. Cada una tiene requisitos, duración y efectos distintos.',
  'Meterlas todas en el mismo acto es exactamente el error que la pregunta busca. Y la tercera opción confunde comisión con encargo: el encargo es asumir otro empleo vacante, no ser designado para desempeñar un empleo de libre nombramiento y remoción conservando el propio.'),

 (2,
  'Dos servidores van a ser retirados. El primero ocupa un empleo de libre nombramiento y remoción y el nominador decidió prescindir de sus servicios. El segundo es empleado de carrera y obtuvo calificación no satisfactoria en su evaluación del desempeño, ya en firme. Un compañero le dice que ambos actos se proyectan igual, «porque al final los dos salen de la entidad y la fórmula del acto es la misma», y le pasa una plantilla única para los dos casos.',
  '¿Qué diferencia debe reflejar cada acto?',
  ['Ninguna: en ambos casos basta invocar la facultad del nominador, porque el retiro es una decisión discrecional que no exige una motivación distinta según la naturaleza del empleo.',
   'El acto del empleado de carrera no requiere motivación porque la calificación ya la contiene, mientras que el del empleo de libre nombramiento y remoción sí debe motivarse por afectar la estabilidad.',
   'El retiro del empleo de libre nombramiento y remoción procede por la facultad discrecional del nominador; el del empleado de carrera solo procede por causal legal, y el acto debe fundarse en ella.',
   'Ambos retiros exigen agotar previamente un procedimiento disciplinario, porque ninguna persona puede ser retirada del servicio sin que se le haya garantizado el derecho de defensa dentro de un proceso.'],
  'Correcto. La <strong>naturaleza del empleo</strong> cambia todo. En el de libre nombramiento y remoción opera la facultad discrecional del nominador. El empleado de carrera tiene <strong>estabilidad</strong>: solo puede ser retirado por una <strong>causal legal</strong>, y aquí la causal es la calificación no satisfactoria <strong>en firme</strong> —esa firmeza no es un detalle: sin ella el retiro es prematuro—.',
  'Proyectar los dos actos igual es el error central. La segunda opción invierte las exigencias. Y la última confunde el retiro con la sanción disciplinaria: la calificación no satisfactoria no es una sanción y no exige un proceso disciplinario previo, aunque sí el debido proceso propio de la evaluación.'),

 (3,
  'Un viernes al final de la tarde, un servidor de otra dependencia se acerca y le pide que use su acceso al sistema de personal para consultar si un compañero de otra sede tiene una sanción disciplinaria anotada en su historia laboral. Le dice que es para saber «con quién se va a trabajar» en un equipo nuevo y que no necesita documentos, solo que le confirme sí o no. Insiste en que nadie se va a enterar y en que usted haría un favor al equipo.',
  '¿Cuál es la actuación correcta?',
  ['Confirmarle solo si existe o no la anotación, sin dar detalles ni entregar documentos, porque un sí o un no no constituye entrega de información y evita un problema de convivencia en el equipo nuevo.',
   'Consultar el sistema y, si efectivamente hay una sanción, informarlo al jefe de la dependencia que está armando el equipo, porque esa información es relevante para la conformación del grupo de trabajo.',
   'Negarse a consultar pero sugerirle que pida directamente al compañero su certificado de antecedentes disciplinarios, de modo que sea él quien decida si comparte o no esa información con el equipo.',
   'No usar el acceso para un fin ajeno a su función, explicarle que la información de la historia laboral está protegida y que existe un canal formal, y dejar constancia de la solicitud recibida.'],
  'Correcto. El acceso al sistema se tiene <strong>por razón de las funciones y para ellas</strong>. Una anotación disciplinaria es información personal del servidor y su divulgación puede afectarlo gravemente; además, la consulta queda registrada a nombre de usted. Explicar el límite y dejar constancia es lo que corresponde.',
  'Un «sí o no» es entregar exactamente la información pedida. Convertirse en informante ante un jefe que no la ha requerido por el canal agrava el asunto. Y sugerirle que presione al compañero para que entregue su propio certificado traslada la indebida presión a la persona afectada.'),

 (1,
  'Una persona fue nombrada y comunicada hace casi un mes, pero no se ha posesionado: dice que está terminando asuntos en su empleo anterior y que se presentará «cuando pueda». El jefe de la dependencia pregunta hasta cuándo hay que esperar y si debe reservarle el puesto indefinidamente. Usted revisa el expediente y confirma que la comunicación del nombramiento se surtió correctamente y que la persona la recibió, con constancia de la fecha. En el expediente no hay ninguna solicitud de prórroga.',
  '¿Qué debe precisar?',
  ['Que no existe término para posesionarse y que la persona conserva el derecho mientras no manifieste expresamente que no acepta, de modo que el empleo debe permanecer reservado a su nombre.',
   'Que la posesión debe surtirse dentro del término legal contado desde la comunicación del nombramiento, prorrogable por causa justificada, y que vencido sin posesión el nombramiento puede dejarse sin efecto.',
   'Que el nombramiento quedó sin efectos de manera automática al día siguiente de la comunicación, de modo que puede procederse de inmediato a proveer el empleo con otra persona sin ningún trámite.',
   'Que el término solo empieza a correr cuando la persona renuncie formalmente a su empleo anterior, porque nadie puede estar vinculado simultáneamente a dos empleos públicos distintos.'],
  'Correcto. El nombramiento no deja el empleo en suspenso indefinido: hay un <strong>término para posesionarse</strong> contado desde la comunicación, <strong>prorrogable por causa justificada</strong>, y vencido sin que la posesión se surta el nombramiento puede dejarse sin efecto. Su tarea es advertirlo a tiempo y dejar constancia de la comunicación y de su fecha.',
  'Ni hay reserva indefinida, ni el nombramiento decae automáticamente sin trámite alguno. Y aunque sea cierto que no se puede ocupar dos empleos públicos a la vez, eso no suspende el término: es precisamente lo que la persona debe resolver dentro de él.'),

 (2,
  'Le asignan verificar los requisitos de una persona nombrada y, al abrir el expediente, usted reconoce el nombre: es el cuñado de su mejor amiga, a quien ve con frecuencia en reuniones familiares. No hay parentesco entre ustedes. Nadie en la División conoce esa cercanía y el grupo está corto de personal. Usted se siente capaz de verificar los soportes con total objetividad y el trámite es urgente, porque la posesión está programada para pasado mañana y la dependencia lleva meses sin ese cargo.',
  '¿Cuál es la actuación correcta?',
  ['Verificar los requisitos con normalidad, porque no existe parentesco con el interesado y la cercanía es con una tercera persona que no participa en el trámite ni resulta afectada por él.',
   'Verificar los requisitos y consignar al final de la constancia que existe esa cercanía, para que el competente valore la información al momento de decidir sobre la posesión.',
   'Poner el vínculo en conocimiento de su jefe por escrito antes de iniciar, describiendo la relación, y dejar que quien es competente decida si procede o no su participación en el trámite.',
   'Pedirle a un compañero que revise con usted los soportes y firmen ambos la constancia, de modo que la objetividad quede respaldada por un segundo par de ojos sin frenar el trámite urgente.'],
  'Correcto. La imparcialidad que se protege no es solo la real, sino también la <strong>aparente</strong>. Un vínculo indirecto —con alguien cercano al interesado— amerita manifestación, y la manifestación debe ser <strong>por escrito y antes de actuar</strong>, para que otro decida. Sentirse capaz de ser objetivo no reemplaza la manifestación.',
  'La ausencia de parentesco no agota el análisis. Y hacerlo después de actuar, o repartir la firma con un compañero, no cumple la función de la manifestación: lo que se busca es que la decisión sobre su participación la tome otro <strong>antes</strong> de que usted intervenga.'),

 (1,
  'Un servidor le pide que «corrija» la fecha de ingreso que figura en su historia laboral porque, según él, está mal por tres meses y eso le afecta el conteo para una prima. Usted revisa y encuentra que la fecha registrada coincide con el acta de posesión, y que los tres meses que él reclama corresponden a un contrato de prestación de servicios anterior a su vinculación. Él insiste en que «eso también fue trabajar para la entidad» y le pide que lo ajuste «porque es justo».',
  '¿Qué corresponde hacer?',
  ['Ajustar la fecha de ingreso para incluir el período del contrato, porque el tiempo efectivamente trabajado para la entidad debe reflejarse en la historia laboral con independencia del tipo de vínculo.',
   'No modificar la fecha, explicarle que el tiempo como contratista no es tiempo de servicio porque el vínculo contractual no genera relación de empleo público, y orientarlo sobre cómo presentar su petición por escrito.',
   'Modificar la fecha dejando una anotación que advierta que los tres meses corresponden a un contrato, de modo que la historia laboral refleje la realidad y el competente decida qué efectos darle.',
   'Rechazar la petición de plano y no recibirle ningún escrito, porque la fecha de ingreso es un dato que proviene del acta de posesión y no admite discusión alguna por parte del interesado.'],
  'Correcto. El tiempo como <strong>contratista no es tiempo de servicio</strong>: el vínculo contractual no genera relación de empleo público y no computa para prestaciones ni para carrera. Y note el doble límite: usted no modifica el dato, y además no resuelve el fondo —lo orienta para que presente su petición y la responda el competente—.',
  'Ajustar la fecha crearía un dato falso en el documento que después soporta liquidaciones y certificaciones. Y aunque la petición no prospere, negarse a recibirle un escrito incumple el deber de atención: una cosa es no modificar el dato y otra, muy distinta, cerrarle el canal.'),

 (2,
  'Llega a la División una comunicación de autoridad competente que ordena la suspensión en el ejercicio del cargo de un servidor, como medida dentro de una actuación en curso. El jefe de la dependencia del servidor llama y pide que no se aplique todavía «porque hay un trabajo urgente que solo él sabe hacer» y propone esperar una semana. Otro compañero le dice que la División debería estudiar primero si la medida es procedente antes de darle trámite.',
  '¿Cuál es la actuación correcta?',
  ['Esperar la semana que pide el jefe de la dependencia, porque la continuidad del servicio es un principio de la función administrativa y justifica una aplicación diferida de la medida.',
   'Estudiar primero la procedencia de la medida y, si la División encuentra que no está debidamente fundada, devolver la comunicación a la autoridad que la profirió solicitando aclaración.',
   'Dar trámite inmediato a la orden, proyectar lo que corresponda para la firma del competente, registrar la novedad con sus efectos y comunicar al jefe de la dependencia, dejando constancia de su solicitud.',
   'Aplicar la medida pero permitir que el servidor termine el trabajo urgente desde casa, de modo que se cumpla formalmente la suspensión sin afectar la continuidad de un asunto que nadie más conoce.'],
  'Correcto. Una suspensión ordenada por <strong>autoridad competente</strong> no se negocia ni se difiere: se tramita. La División registra la novedad y proyecta lo que corresponda, con sus efectos sobre la nómina y el ejercicio del cargo, y comunica. La solicitud del jefe se deja por escrito y se informa, pero no suspende el cumplimiento.',
  'Diferir la medida por conveniencia del servicio desconoce una orden que no está sujeta a la valoración de la dependencia. Tampoco corresponde a la División calificar su procedencia. Y «suspender pero dejarlo trabajar desde casa» es, simplemente, no suspender.'),

 (0,
  'Una servidora de carrera es nombrada en un empleo de libre nombramiento y remoción de la misma entidad y pregunta qué pasa con su empleo de carrera. Un compañero le dice que «al aceptar, renuncia automáticamente a la carrera» y otro, que «conserva los dos empleos y cobra los dos sueldos». La servidora está preocupada, lleva nueve años en su empleo de carrera y necesita decidir antes del viernes. El jefe le pide a usted que precise el punto por escrito antes de que ella firme cualquier cosa.',
  '¿Cuál es la respuesta correcta?',
  ['Puede ser comisionada para desempeñar el empleo de libre nombramiento y remoción conservando los derechos de carrera sobre su empleo, al que regresa al terminar la comisión; su empleo de carrera queda en vacancia temporal.',
   'Al aceptar el nuevo empleo pierde de inmediato los derechos de carrera, porque aceptar un empleo de libre nombramiento y remoción constituye renuncia tácita a la estabilidad que la carrera le otorgaba.',
   'Conserva simultáneamente los dos empleos y percibe las dos asignaciones, porque la entidad es la misma y no hay incompatibilidad entre empleos de una misma planta de personal.',
   'Debe renunciar formalmente a su empleo de carrera antes de posesionarse, y si al terminar el nuevo empleo desea regresar deberá participar nuevamente en un concurso público de méritos.'],
  'Correcto. Es la <strong>comisión para desempeñar un empleo de libre nombramiento y remoción</strong>: la empleada de carrera la recibe por el término que corresponda, <strong>conserva sus derechos de carrera</strong> y regresa a su empleo al terminarla. Mientras tanto, su empleo queda en <strong>vacancia temporal</strong>, que es justamente lo que habilita proveerlo por encargo.',
  'Aceptar un empleo de libre nombramiento y remoción no es renuncia tácita a la carrera: existe precisamente una figura para evitar esa pérdida. Nadie percibe dos asignaciones por dos empleos públicos. Y exigirle renunciar y volver a concursar le haría perder un derecho que la ley le conserva.'),

 (3,
  'Un servidor presenta renuncia con efectos a partir del día quince del mes. El jefe de su dependencia le pide a usted que «le pida que la cambie» para el día treinta, porque necesita que termine un informe. El servidor, por su parte, le pregunta si puede retirar la renuncia si cambia de opinión la próxima semana, y si debe seguir asistiendo mientras tanto. Nadie ha aceptado todavía la renuncia, y el servidor ha seguido asistiendo con normalidad mientras se resuelve.',
  '¿Qué debe precisar?',
  ['Que la renuncia produce efectos desde su presentación, de modo que el servidor puede dejar de asistir desde ya y ni la entidad ni él pueden modificar la fecha indicada en el escrito.',
   'Que la entidad puede fijar unilateralmente la fecha de retiro que convenga al servicio, de modo que basta con que el acto de aceptación señale el día treinta en lugar del quince solicitado.',
   'Que mientras la renuncia no se acepte el servidor puede dejar de asistir sin consecuencia, porque la manifestación de voluntad basta para desvincularse y la aceptación es un trámite posterior.',
   'Que la renuncia requiere aceptación, que mientras tanto el servidor debe seguir cumpliendo sus funciones y puede retirarla, y que la entidad puede diferir la fecha de retiro dentro del término legal cuando el servicio lo exija.'],
  'Correcto. Tres ideas que la prueba mezcla. La renuncia <strong>requiere aceptación</strong>: mientras no se acepte, el servidor sigue vinculado y debe cumplir sus funciones, y puede retirarla. La entidad puede <strong>diferir</strong> la fecha de retiro dentro del término que la norma prevé cuando el servicio lo exija, pero eso se hace en el acto de aceptación, no pidiéndole al servidor que reescriba su escrito.',
  'La renuncia no produce efectos por sí sola ni autoriza a dejar de asistir. Y aunque la entidad sí puede diferir la fecha, no puede hacerlo sin límite ni sustituir la voluntad del servidor: lo que hace es aceptar con una fecha distinta dentro del término legal, no «pedirle que cambie» el documento.'),

 (1,
  'El jefe de la División le encarga preparar el acto de retiro por pensión de un servidor. Usted proyecta el documento con todos sus soportes: la resolución de reconocimiento de la pensión, la verificación del tiempo de servicio y la liquidación preliminar. Al terminar, su compañero le dice que lo firme usted mismo, «porque el jefe está en comisión toda la semana y el servidor necesita el acto para su trámite ante el fondo». El servidor, en efecto, está presionando.',
  '¿Qué corresponde hacer?',
  ['Firmar el acto en ausencia del jefe y dejar constancia de que lo hizo por razones de urgencia, de modo que el servidor pueda adelantar su trámite ante el fondo sin esperar al regreso.',
   'Dejar el proyecto listo con todos sus soportes, remitirlo por el canal para la firma del competente, informar al servidor el estado real del trámite y los tiempos, y dejar constancia de la urgencia planteada.',
   'Entregar al servidor una copia del proyecto sin firma, advirtiéndole que es un borrador, para que pueda ir adelantando su trámite ante el fondo mientras llega la firma del competente.',
   'Solicitar al jefe que autorice la firma por correo electrónico y, con esa autorización, suscribir el acto, porque la autorización escrita del superior suple su firma cuando media una urgencia acreditada.'],
  'Correcto. El numeral 5 del artículo 63 es explícito: la División <strong>prepara</strong> los actos y quien los <strong>firma</strong> es el Procurador General. Su trabajo termina en el proyecto completo, remitido a tiempo por el canal, con el servidor informado del estado real y la urgencia registrada. Eso es lo máximo que puede hacer, y es bastante.',
  'Firmar en lugar del competente vicia el acto por falta de competencia, y la urgencia no lo sanea. Entregar un borrador sin firma induce a error a quien lo reciba. Y una autorización por correo no transfiere la competencia: la competencia la asigna la norma, no el superior.'),
]
