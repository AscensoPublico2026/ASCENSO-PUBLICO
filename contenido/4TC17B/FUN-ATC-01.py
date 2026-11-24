# -*- coding: utf-8 -*-
"""Día 3 (2.ª guía) · Atención al Usuario y Servicio al Ciudadano — Técnico en Criminalística 4TC-17."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-ATC-4TC17B-01',
    archivo='FUN-ATC-4TC17B-01-atencion-usuario-servicio-ciudadano.html',
    dia=3,
    titulo_doc='Atención al Usuario y Servicio al Ciudadano',
    h1='Atención al Usuario y Servicio al Ciudadano',
    kicker='Día 3 · Conocimientos comunes',
    sub='<strong>Atención al usuario</strong> es uno de los conocimientos comunes que exige el formato de convocatoria del <strong>Técnico en Criminalística 4TC-17</strong>. Aquí verás el servicio al ciudadano como deber y como política, los <strong>canales de atención</strong> y sus reglas, el <strong>protocolo</strong> de atención presencial, telefónica y virtual, la <strong>atención preferencial</strong> y los enfoques diferenciales, el manejo de situaciones difíciles, el <strong>lenguaje claro</strong>, la <strong>carta de trato digno</strong> (art. 7 del CPACA) y la frontera entre informar y revelar: lo que puedes decir y lo que está sujeto a reserva cuando trabajas con expedientes y trámites.',
    badges=['⏱ 95-115 min', '🏛️ Régimen PGN', '📘 Conocimientos comunes'],
    fmeta='Atención al Usuario y Servicio al Ciudadano (CPACA, Ley 1755 de 2015 y protocolos de servicio)',
    cargo='Técnico en Criminalística 4TC-17 (Nivel Técnico)',
    conv='285-2026',
    alerta='Atención al usuario y servicio al ciudadano',
)

SEC = secciones_mapeadas('guias/FUN-ATC-TEC-01-servicio-ciudadano.html')

R = [
    ('<p>Estás en la ventanilla de atención de una Procuraduría Regional. En cinco minutos se te juntan varias situaciones: llega una <strong>señora mayor con bastón</strong> que apenas puede quedarse de pie en la fila; un <strong>ciudadano molesto</strong> que alza la voz porque "lleva un mes esperando una respuesta y nadie le dice nada"; una persona que no habla bien español y trae unos documentos; y suena el teléfono con alguien que pregunta cómo radicar una queja. Tu compañero, agotado, murmura: "atiende como puedas y que sigan". Tú te preguntas: ¿a quién atiendo primero? ¿cómo calmo al ciudadano molesto sin pelear? ¿qué hago con la señora mayor? ¿puedo simplemente decirle "eso no es aquí"? ¿cómo trato a alguien que no me entiende?</p>',
     '<p>Estás de turno en la atención al público en una sede de la Procuraduría y, mientras organizas los documentos recibidos, se te juntan varias situaciones: una <strong>señora mayor con bastón</strong> pregunta dónde radica una queja y apenas puede quedarse de pie; un <strong>ciudadano molesto</strong> alza la voz porque "lleva un mes esperando una respuesta y nadie le dice nada"; una persona que no habla bien español trae unos documentos; y suena el teléfono con alguien que pregunta por el estado de una actuación. Tu compañero, agotado, murmura: "atiende como puedas y que sigan". Tú te preguntas: ¿a quién atiendo primero? ¿cómo calmo al ciudadano molesto sin pelear? ¿qué hago con la señora mayor? ¿puedo simplemente decirle "eso no es aquí"? ¿y qué puedo contarle a quien llama, si el expediente está sujeto a reserva?</p>'),

    ('Tu manual lo exige: <mark>"Atención al usuario"</mark> es un conocimiento específico del cargo',
     'Tu formato de convocatoria lo exige: <mark>"Atención al usuario"</mark> es un conocimiento común evaluable del cargo'),

    ('<h2 class="sec-title">📖 Atención al Usuario y Servicio al Ciudadano para el Secretario de la PGN</h2>',
     '<h2 class="sec-title">📖 Atención al Usuario y Servicio al Ciudadano para el Técnico en Criminalística de la PGN</h2>'),

    ('ventanilla', 'punto de atención'),
    ('Secretario Procuraduría', 'Técnico en Criminalística'),
]

SEC = aplicar_todas(SEC, R, estricto=True)
LIMPIEZA = [('la punto de atención', 'el punto de atención'), ('una punto de atención', 'un punto de atención'),
            ('Secretario de punto de atención', 'servidor que atiende'),
            ('Secretario en la punto de atención', 'servidor que atiende en el punto de atención'),
            ('Secretario', 'Técnico en Criminalística')]
SEC = aplicar_todas(SEC, LIMPIEZA, estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol('Técnico en Criminalística', 'Técnicos en Criminalística'), estricto=False)   # filtro antifugas final

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre atención al '
              'usuario y servicio al ciudadano. Los contextos son extensos y las cuatro opciones son plausibles. '
              'Al seleccionar una opción verás si acertaste y la explicación.')

P = [
 (2,
  'Usted está en la sede de la Procuraduría organizando los elementos recibidos en un trámite cuando se acerca una señora de 78 años, con bastón, que pregunta dónde radicar una queja. Hay cuatro personas esperando turno que llegaron antes que ella y una de ellas protesta en voz alta: dice que «aquí todos tenemos afán» y que no acepta que la atiendan primero. Un compañero le susurra que evite el problema y respete estrictamente el orden de llegada.',
  '¿Cuál es la actuación correcta frente a la atención preferencial?',
  ['Respetar estrictamente el orden de llegada, porque la igualdad ante la ley impide dar un trato distinto a unas personas frente a otras en el acceso a los servicios de la entidad.',
   'Pedirle a la señora que regrese en un horario de menor afluencia, cuando pueda ser atendida sin generar molestias entre quienes ya estaban esperando su turno en el punto de atención.',
   'Atenderla de manera preferencial y explicar con cortesía a quienes esperan que se trata de un derecho de las personas mayores, no de un privilegio ni de una decisión discrecional.',
   'Atenderla primero sin dar explicación alguna a los demás usuarios, porque el servidor no está obligado a justificar sus decisiones de atención frente a quienes esperan en la fila.'],
  'La atención preferencial para adultos mayores, personas con discapacidad, mujeres gestantes y otros sujetos de especial protección es un derecho reconocido por el CPACA y por el artículo 13 de la Constitución. Explicarlo con cortesía evita el conflicto y educa a quienes esperan.',
  'Ni el orden estricto de llegada, ni aplazar la atención, ni atender sin explicar: la preferencia es un derecho y conviene sustentarla ante los demás usuarios.'),

 (0,
  'Un ciudadano llega alterado porque, según dice, hace un mes presentó una queja y nadie le ha respondido. Habla fuerte, interrumpe y asegura que «aquí nadie trabaja». No amenaza a nadie, pero hay otras personas en la sala y el ambiente se tensiona. Un compañero propone responderle en el mismo tono para «poner orden» y otro sugiere llamar de inmediato al personal de seguridad para que lo retire del lugar.',
  '¿Cuál es el manejo correcto de la situación?',
  ['Mantener la calma, escuchar sin interrumpir, reconocer su molestia, verificar el estado del trámite e informarle con precisión los pasos y los tiempos, dejando constancia de lo informado.',
   'Responder con firmeza en el mismo tono para restablecer el orden en la sala y dejar claro que no será atendido mientras no modifique su actitud frente al personal de la entidad.',
   'Llamar de inmediato al personal de seguridad para que lo retire, porque la alteración del orden en una sede pública justifica por sí sola la interrupción de la atención al usuario.',
   'Prometerle que su respuesta saldrá esta misma semana para que se tranquilice y se retire, y luego gestionar internamente lo que alcance a hacerse con el equipo de la dependencia.'],
  'El protocolo para situaciones difíciles es escuchar activamente, reconocer la emoción, verificar datos reales e informar con precisión. La molestia del usuario no autoriza el maltrato, pero tampoco la promesa falsa.',
  'Ni devolver el tono, ni escalar a seguridad sin necesidad, ni prometer lo que no se puede cumplir. Se escucha, se verifica y se informa con datos ciertos.'),

 (3,
  'Durante un trámite, una persona le pregunta por teléfono a usted, que es Técnico en Criminalística, en qué va la actuación en la que fue citada como testigo y qué encontró la Procuraduría en la entidad. Usted reconoce la voz, sabe que efectivamente es la testigo, y la persona insiste en que «tiene derecho a saber porque es parte del proceso». La llamada entra mientras usted está embalando los elementos y la persona asegura que un funcionario de la entidad «ya le contó algo» y solo quiere confirmarlo.',
  '¿Qué puede informar y qué no?',
  ['Puede informarle todo lo que ha encontrado, porque quien participa en la actuación tiene derecho de acceso pleno a la información que la entidad haya recibido hasta ese momento.',
   'No puede informar absolutamente nada, ni siquiera confirmar la existencia de la actuación, porque toda comunicación con un testigo por fuera del trámite está prohibida por la ley.',
   'Puede informarle los hallazgos de manera general, sin dar cifras ni nombres, de modo que la persona conozca el sentido de la actuación sin acceder a los detalles reservados del caso.',
   'Puede orientarla sobre el trámite y los canales para solicitar información oficial, pero no revelar hallazgos ni contenido sujeto a reserva, ni anticipar conclusiones del informe técnico.'],
  'Informar sobre el trámite no es revelar el contenido. La reserva protege la actuación y los derechos de los involucrados; los hallazgos se comunican por los canales oficiales y por quien tiene competencia.',
  'Ni acceso pleno, ni silencio absoluto, ni «hallazgos en general»: se orienta sobre el trámite y se protege el contenido reservado.'),

 (1,
  'Llega a la sede una persona que no habla español con fluidez y trae documentos en los que, con dificultad, explica que quiere presentar una queja. Un compañero sugiere pedirle que vuelva con alguien que traduzca, porque «así no se puede atender» y porque podría cometerse un error al entender mal lo que pide. Hay fila en el punto de atención y un compañero insiste en que atenderla tomará el doble de tiempo del que la dependencia puede dedicarle esta mañana.',
  '¿Cuál es la actuación correcta?',
  ['Pedirle que regrese acompañada de una persona que traduzca, porque sin una comprensión plena de la solicitud la entidad corre el riesgo de tramitar un asunto distinto al que la persona quiere.',
   'Atenderla con lenguaje claro, apoyos visuales y la ayuda disponible en la entidad, procurando entender su solicitud y dejando constancia de lo recibido, sin exigirle que vuelva acompañada.',
   'Recibirle los documentos sin preguntar nada y darles el trámite que el servidor considere más probable, para no exponerla a una conversación difícil ni hacerla esperar más tiempo del necesario.',
   'Remitirla a una organización social que preste servicios de acompañamiento a población migrante, porque la entidad no cuenta con la obligación legal de atender en otros idiomas.'],
  'El enfoque diferencial obliga a adaptar la atención a las condiciones de la persona. Exigir un traductor como condición de acceso convierte una barrera en un requisito y vulnera el derecho de petición.',
  'Ni condicionar la atención, ni adivinar lo que pide, ni trasladar la obligación a un tercero: se atiende con los apoyos disponibles y se deja constancia.'),

 (2,
  'El jefe le pide a usted revisar el borrador de una comunicación dirigida a un ciudadano. El texto dice: «En atención a la solicitud del epígrafe, se le informa que, surtido el trámite correspondiente y agotadas las instancias pertinentes, la misma fue objeto de la decisión que en derecho correspondía». El ciudadano es una persona mayor sin formación jurídica que preguntó, simplemente, si su queja seguía o no.',
  '¿Qué debe observarse sobre la redacción?',
  ['El texto es adecuado, porque el lenguaje técnico-jurídico otorga precisión a las comunicaciones oficiales y protege a la entidad frente a interpretaciones equivocadas del destinatario.',
   'El texto es adecuado siempre que se anexe copia de las normas aplicables, de modo que el ciudadano pueda consultar por su cuenta el significado de los términos empleados en la respuesta.',
   'El texto incumple el deber de lenguaje claro: debe decir en palabras sencillas qué pasó con la queja, qué sigue y en qué tiempos, sin perder precisión jurídica.',
   'El texto debe reemplazarse por una llamada telefónica, porque las comunicaciones escritas resultan siempre más confusas para las personas sin formación jurídica que las explicaciones verbales.'],
  'El lenguaje claro es un deber de la administración: comunicar de modo que el destinatario encuentre, entienda y use la información. Claridad y precisión jurídica no se oponen.',
  'El tecnicismo no da precisión por sí solo, anexar normas no suple la claridad y la llamada no reemplaza la respuesta escrita.'),

 (0,
  'Una persona se acerca y, con desconfianza, pregunta: «¿esto que le voy a contar queda guardado o cualquiera lo puede ver?». Trae una denuncia sobre hechos que involucran a su jefe en una entidad pública y teme represalias. Un compañero le dice que le prometa confidencialidad absoluta para que se anime a denunciar, y otro, que le advierta que «en el Estado todo es público». La persona añade que un amigo suyo denunció hace años y «se enteró toda la oficina», y que por eso prefiere no dejar nada por escrito si no hay garantías.',
  '¿Qué debe informarle usted?',
  ['Que la información se maneja conforme a la ley: hay datos protegidos y actuaciones con reserva, y debe explicarle el alcance real sin prometer una confidencialidad absoluta que la ley no garantiza.',
   'Que puede estar tranquila porque toda la información que entregue será absolutamente confidencial y nadie, en ninguna circunstancia, podrá acceder a su identidad ni al contenido de la denuncia.',
   'Que en el Estado toda la información es pública por mandato de la Ley de Transparencia, de modo que su denuncia y sus datos personales podrán ser consultados por cualquier ciudadano.',
   'Que no es posible darle ninguna orientación sobre el manejo de la información hasta que formalice la denuncia por escrito y la radique en la oficina correspondiente de la entidad.'],
  'La regla es la publicidad con excepciones legales de reserva, y los datos personales tienen protección propia. Prometer confidencialidad absoluta es faltar a la verdad; afirmar que todo es público, también.',
  'Ni la promesa absoluta, ni el «todo es público», ni negar la orientación: se explica el alcance real de la reserva y de la protección de datos.'),

 (3,
  'La dependencia debe publicar y mantener visible un documento que enuncia los derechos de los usuarios, los medios para garantizarlos y los compromisos de atención. Un compañero sostiene que ese documento «es opcional» y que basta con el manual interno de procedimientos; otro cree que se trata del reglamento disciplinario de la entidad. El jefe quiere zanjar la discusión con fundamento normativo antes de la visita de la oficina de control interno prevista para la próxima semana.',
  '¿De qué documento se trata y qué lo regula?',
  ['Del manual de procedimientos de la dependencia, que es un documento interno de uso exclusivo del personal y que no requiere publicación ni consulta por parte de los usuarios del servicio.',
   'Del reglamento disciplinario interno, que recoge los deberes de los servidores frente a los usuarios y las consecuencias de incumplirlos en la atención presencial, telefónica y virtual.',
   'Del plan anticorrupción y de atención al ciudadano, documento interno que cada entidad elabora de manera facultativa cuando cuenta con puntos de atención presencial abiertos al público.',
   'De la carta de trato digno al usuario, que el artículo 7 del CPACA obliga a elaborar y poner a disposición, con los derechos de los usuarios y los medios para garantizarlos.'],
  'El artículo 7 del CPACA impone a las autoridades el deber de elaborar y mantener disponible la carta de trato digno, con los derechos de los usuarios y los medios dispuestos para ejercerlos. No es opcional.',
  'No es el manual interno, ni el reglamento disciplinario, ni el plan anticorrupción: es la carta de trato digno del artículo 7 del CPACA.'),

 (1,
  'Mientras usted atiende presencialmente a una persona que explica un asunto complejo, el teléfono de la dependencia suena de manera insistente. No hay nadie más disponible en ese momento. Un compañero, desde lejos, le grita que conteste porque «puede ser importante» y la persona que usted atiende se muestra incómoda por la interrupción. Quien llama pregunta además por el estado de un expediente y la persona que usted atiende alcanza a escuchar parte de la conversación desde el escritorio.',
  '¿Cuál es el manejo correcto de los canales de atención?',
  ['Contestar de inmediato el teléfono y pedirle a la persona presente que espere, porque la llamada puede provenir de otra entidad y la comunicación institucional tiene prioridad sobre la atención presencial.',
   'Priorizar a quien está presente, cerrar la atención con claridad y devolver la llamada enseguida, o informar brevemente a quien llama que será atendido en un momento, sin maltratar a ninguno.',
   'Ignorar el teléfono por completo durante toda la atención presencial, porque interrumpir a un usuario que está siendo atendido vulnera su derecho a recibir un servicio continuo y de calidad.',
   'Contestar y resolver la consulta telefónica mientras continúa la atención presencial, de modo que ambos usuarios sean atendidos de manera simultánea y ninguno tenga que esperar su turno.'],
  'El protocolo reconoce que los canales conviven: se protege la atención en curso sin abandonar al que llama. Lo que no cabe es maltratar a uno para atender al otro ni pretender atender a dos a la vez.',
  'Ni interrumpir sin más, ni ignorar el canal telefónico, ni atender en paralelo: se cierra con calidad y se retoma la llamada.'),

 (2,
  'Un ciudadano pide que se le informe de inmediato el resultado de una actuación disciplinaria que involucra a un alcalde. Dice que, como la información es de interés público y el alcalde es una figura pública, «no puede haber reserva». La actuación está en curso y hay pruebas aún no controvertidas por el investigado. El ciudadano agrega que piensa publicar en redes que la entidad «encubre» si no recibe la información hoy mismo, y el jefe pide una respuesta motivada.',
  '¿Cuál es la respuesta correcta?',
  ['Entregar la información solicitada, porque tratándose de un servidor de elección popular prevalece el interés público sobre cualquier reserva aplicable a la actuación administrativa en curso.',
   'Negar la solicitud sin motivación alguna, informándole que la actuación está en curso y que por esa razón no es posible pronunciarse sobre ninguno de los aspectos consultados.',
   'Explicar con motivación que la actuación en curso está sujeta a reserva, indicar qué información sí es pública y señalar el momento procesal en que podrá conocerse el resultado.',
   'Remitir la solicitud al alcalde investigado para que sea él quien autorice o niegue la entrega de la información relacionada con la actuación que se adelanta en su contra.'],
  'La reserva de la actuación protege el debido proceso y la eficacia de la investigación, y no desaparece por la calidad del investigado. Negar sin motivar también es irregular: la negativa se funda y se explica.',
  'Ni entregar por tratarse de una figura pública, ni negar sin motivar, ni trasladar la decisión al investigado.'),

 (0,
  'Usted detecta que, en los últimos meses, varias personas han llegado a la sede buscando radicar quejas que corresponden a otra entidad, porque un aviso desactualizado en la cartelera induce a error. El jefe le pide una propuesta y un compañero sostiene que «eso no es problema nuestro, basta con indicarles de palabra a dónde ir». El aviso lleva meses así, nadie lo ha reportado y el compañero insiste en que proponer cambios «no le corresponde a un técnico».',
  '¿Qué actuación refleja mejor el servicio al ciudadano como política y no solo como trato?',
  ['Proponer la corrección del aviso y una orientación escrita y visible sobre los canales correctos, además de seguir orientando verbalmente, porque el servicio también se diseña y no solo se improvisa.',
   'Continuar orientando de palabra a cada persona que llegue, porque el trato amable resuelve el problema concreto y no corresponde al nivel técnico proponer cambios en la señalización de la sede.',
   'Retirar el aviso de la cartelera sin reemplazarlo, de modo que las personas pregunten directamente en el punto de atención y reciban la orientación verbal de quien esté disponible en el momento.',
   'Dejar constancia del problema en un correo interno y continuar con las funciones propias del cargo, porque la gestión de la señalización corresponde exclusivamente al área administrativa.'],
  'El servicio al ciudadano es política institucional: incluye información veraz y accesible, señalización correcta y mejora continua. Detectar una barrera y proponer su corrección es parte del buen servicio.',
  'La orientación verbal alivia el síntoma, retirar el aviso empeora la información y limitarse a un correo sin propuesta no corrige la causa.'),

 (3,
  'Una persona con discapacidad visual llega a la sede acompañada de un perro guía. Un compañero le indica que el animal no puede entrar por razones de higiene y le sugiere a la persona que espere afuera mientras alguien le ayuda con el trámite desde adentro. El acompañante de otra persona que espera turno protesta y dice que el animal «no debería estar en una oficina pública», mientras la fila avanza con lentitud. Usted es quien está más cerca de la entrada y la persona espera una respuesta.',
  '¿Cuál es la actuación correcta?',
  ['El compañero actuó bien, porque las normas de higiene de las sedes públicas prohíben el ingreso de animales y la entidad ofrece una alternativa razonable al atender el trámite desde adentro.',
   'Debe permitirse el ingreso del animal solo si la persona presenta un certificado veterinario vigente y una credencial que acredite el entrenamiento del perro como animal de asistencia.',
   'Debe atenderse a la persona afuera de la sede, para evitar el conflicto con otros usuarios que puedan sentirse incómodos y garantizar al mismo tiempo la prestación del servicio solicitado.',
   'Debe permitirse el ingreso con su perro guía y brindarle atención preferencial y los apoyos necesarios, porque negarlo constituye una barrera de acceso y un trato discriminatorio.'],
  'El enfoque diferencial y la prohibición de discriminación imponen eliminar barreras de acceso. Un perro guía es un apoyo de la persona, no una mascota, y atender a alguien «afuera» es excluirlo del servicio.',
  'Ni la higiene, ni la exigencia de certificados, ni la atención en la calle justifican una barrera de acceso para una persona con discapacidad.'),

 (1,
  'En una reunión del equipo se discute cómo medir si la dependencia atiende bien. Un integrante propone contar cuántas personas se atienden por día; otro sostiene que la calidad del servicio «no se puede medir» y que depende del ánimo de cada servidor. El jefe pide un criterio que sirva para mejorar y no solo para reportar. El jefe recuerda que la dependencia debe reportar resultados el mes entrante y que el año pasado el informe se armó solo con el número de atenciones.',
  '¿Qué criterio refleja mejor la noción de servicio como política pública?',
  ['Contar únicamente el número de personas atendidas por día, porque es un dato objetivo, verificable y comparable entre dependencias, y permite mostrar resultados concretos ante la dirección.',
   'Combinar indicadores de oportunidad y calidad con la medición de la satisfacción y el análisis de las quejas recibidas, para identificar barreras y corregirlas de manera sostenida.',
   'Confiar en la percepción de cada servidor sobre su propio desempeño, porque quien atiende conoce mejor que nadie las dificultades del servicio y puede juzgar si lo hizo bien o mal.',
   'Medir exclusivamente el tiempo de espera en el punto de atención, dado que la demora es el principal motivo de queja de los usuarios y reducirla mejora automáticamente la percepción del servicio.'],
  'El servicio se gestiona con información: oportunidad, calidad, satisfacción y quejas. Un solo número —personas atendidas o minutos de espera— puede mejorar sin que mejore el servicio real.',
  'Ni un indicador único de volumen o de espera, ni la autopercepción: se combinan medidas de oportunidad, calidad y satisfacción, y se analizan las quejas.'),

 (2,
  'Durante un trámite en una entidad, un funcionario le ofrece a usted un almuerzo «de cortesía» en el casino de la institución, junto con el resto del equipo que acompaña la actuación. Dice que es la práctica habitual con todas las visitas y que rechazarlo sería un desaire. El jefe de la comisión no está presente en ese momento. El funcionario insiste delante de todo el equipo y dice que, si no aceptan, la entidad lo interpretará como un gesto de desconfianza hacia sus servidores.',
  '¿Cómo se relaciona esto con el trato con el usuario y la integridad del servidor?',
  ['Puede aceptarse, porque se trata de una atención de cortesía institucional y no de una dádiva personal, dado que el ofrecimiento se extiende a todo el equipo que participa en el trámite.',
   'Puede aceptarse siempre que se informe después al jefe de la comisión, ya que la comunicación posterior elimina cualquier duda sobre la imparcialidad de los servidores que participaron.',
   'Debe declinarse con cortesía y dejar constancia si resulta pertinente, porque aceptar atenciones de la entidad visitada compromete la apariencia de imparcialidad durante la actuación.',
   'Debe aceptarse para no afectar la relación con la entidad visitada y facilitar la colaboración durante el trámite, siempre que su valor sea moderado y no se repita en otras visitas.'],
  'La imparcialidad no solo debe existir: debe parecerlo. Aceptar atenciones de la entidad que se está examinando compromete esa apariencia y puede ser cuestionado después por los sujetos procesales.',
  'Ni el carácter colectivo, ni el aviso posterior, ni el valor moderado convierten en aceptable una atención de la entidad visitada durante el trámite.'),

 (0,
  'Un ciudadano solicita por escrito que se le informe el nombre del servidor que practicó un trámite en su entidad y los datos de contacto personales de ese servidor, porque quiere «hablar directamente con él». El jefe le pide a usted preparar la respuesta. La solicitud llegó por escrito, con firma y dirección de notificación, y el ciudadano advierte que si no le dan los datos presentará una queja disciplinaria. El jefe pide que la respuesta salga hoy porque el término ya corre.',
  '¿Qué corresponde informar?',
  ['Informar los datos institucionales de contacto y el canal oficial para presentar solicitudes, protegiendo los datos personales del servidor, que no son información pública de la entidad.',
   'Entregar el nombre y los datos personales de contacto del servidor, porque quien ejerce funciones públicas pierde la reserva sobre su información personal durante el ejercicio del cargo.',
   'Negar toda la información solicitada, incluido el canal oficial de contacto, porque cualquier dato relativo a los servidores que intervienen en una actuación está amparado por reserva legal.',
   'Trasladar la solicitud al servidor para que él decida si entrega o no sus datos personales de contacto al ciudadano que lo requiere, dejando constancia de su decisión en el expediente.'],
  'La actuación es institucional: el ciudadano se comunica con la entidad por los canales oficiales. Los datos personales del servidor son información protegida y no se entregan.',
  'Ni entregar datos personales, ni negar el canal oficial, ni dejar la decisión en manos del servidor: se informa el canal institucional y se protegen los datos.'),

 (3,
  'La dependencia recibe una queja escrita contra usted por la forma en que atendió a una persona en un trámite: afirma que usted fue «cortante y grosero». Usted recuerda la situación de otra manera y cree que la persona malinterpretó una explicación técnica. El jefe le pide su versión por escrito. La queja llegó por el canal de PQRSD, tiene término de respuesta y la persona pide además que se le informe qué medidas tomó la entidad frente al servidor.',
  '¿Cuál es la actitud correcta frente a la queja?',
  ['Responder que la queja es infundada y pedir que se archive de inmediato, porque la percepción subjetiva de un usuario no puede convertirse en un reproche a la conducta del servidor.',
   'Abstenerse de responder y esperar a que el jefe resuelva, porque pronunciarse sobre la queja podría interpretarse como una interferencia en el trámite que se adelanta sobre el hecho.',
   'Pedir que se cite al quejoso para aclarar personalmente el malentendido antes de rendir cualquier informe escrito, de modo que el asunto se resuelva sin dejar registro en la dependencia.',
   'Rendir su versión con hechos concretos y verificables, reconocer lo que corresponda y asumir la queja como información útil para mejorar la atención, sin descalificar al usuario.'],
  'La queja es un insumo de mejora y un derecho del usuario. Lo profesional es rendir la versión con hechos, reconocer lo que proceda y ajustar la práctica, sin descalificar a quien se quejó.',
  'Ni descalificar la queja, ni guardar silencio, ni buscar un arreglo informal que evite el registro: se responde con hechos y se aprende del caso.'),
]
