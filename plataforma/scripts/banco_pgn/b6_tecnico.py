# -*- coding: utf-8 -*-
"""Nivel técnico de la Procuraduría: sustanciación, impulso procesal, gestión
documental y juicio situacional del nivel."""

PRO = "Procedimiento disciplinario y sustanciación"
GES = "Gestión documental y calidad de la información"
JUI = "Juicio situacional del nivel técnico"

BANCO = [
dict(
    tema="Reparto por competencia", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="intermediate",
    ctx="Llega al despacho una queja contra un funcionario cuyo cargo corresponde, por el reparto vigente, a otra dependencia de la Procuraduría. El quejoso vive a cuatro horas del lugar y radicó personalmente el documento. El término para la primera decisión empieza a correr desde hoy.",
    q="¿Qué debe hacer quien la recibe?",
    ops=[
        "Devolverle el documento al quejoso para que lo radique en la dependencia que resulta competente para conocerlo.",
        "Remitirla por competencia a la dependencia que debe conocerla e informar al quejoso de esa remisión.",
        "Tramitarla en el despacho que la recibió, para no hacer perder más tiempo a quien se desplazó hasta la sede.",
    ],
    correcta=1,
    expl=[
        "Devolver el documento traslada al ciudadano una carga que la ley pone en cabeza de la entidad.",
        "Correcto: se remite por competencia y se le informa al quejoso a dónde fue su queja y quién la atenderá.",
        "Tramitar un asunto sin competencia vicia la actuación desde el inicio y obliga a rehacerla después.",
    ],
),

dict(
    tema="Foliación del expediente", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="basic",
    ctx="Al revisar un expediente que va a pasar a decisión, usted encuentra once folios sin numerar, dos folios con el mismo número y tres documentos sueltos dentro de la carpeta que no aparecen en el índice.",
    q="¿Por qué importa corregirlo antes de que el expediente siga su curso?",
    ops=[
        "Porque la foliación da certeza sobre qué pruebas obran en el expediente y en qué orden fueron incorporadas.",
        "Porque el manual de archivo de la entidad establece esa exigencia y la oficina de control interno la verifica.",
        "Porque mejora la presentación del expediente ante la instancia que debe resolver el asunto en segunda instancia.",
    ],
    correcta=0,
    expl=[
        "Correcto: es la garantía de integridad del expediente y la condición para que la prueba pueda controvertirse.",
        "Es una obligación normativa, pero su razón de ser no es la verificación interna sino la integridad de la prueba.",
        "La presentación es lo de menos: lo que está en juego es la certeza sobre el contenido del expediente.",
    ],
),

dict(
    tema="Práctica de una declaración", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="intermediate",
    ctx="Se va a recibir la declaración de un testigo clave en una investigación. El investigado solicita estar presente con su defensor. El testigo manifiesta que preferiría declarar sin la presencia del investigado porque es su jefe directo.",
    q="¿Qué corresponde?",
    ops=[
        "Negarlo en todo caso, pues la reserva de la actuación cobija también al investigado hasta que se le formule el pliego de cargos.",
        "Permitir la presencia del investigado o de su defensor, porque la contradicción de la prueba hace parte del debido proceso.",
        "Permitirlo únicamente si el testigo manifiesta expresamente su consentimiento con la presencia del investigado.",
    ],
    correcta=1,
    expl=[
        "La reserva opera frente a terceros y no frente al sujeto procesal, que necesita controvertir la prueba.",
        "Correcto: poder contrainterrogar es parte del derecho de defensa, sin perjuicio de las medidas de protección del testigo.",
        "El consentimiento del testigo no define las garantías procesales que amparan al investigado.",
    ],
),

dict(
    tema="Notificación personal fallida", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="advanced",
    ctx="Debe notificarse personalmente un auto al investigado. Se le citó a la dirección que él mismo registró y la citación fue entregada hace ocho días, con constancia de recibo. El investigado no compareció dentro del término y el expediente no puede seguir detenido.",
    q="¿Qué procede?",
    ops=[
        "Entender el auto notificado el mismo día en que se envió la citación a la dirección registrada por el investigado.",
        "Suspender la actuación hasta que el investigado comparezca voluntariamente al despacho a notificarse del auto.",
        "Surtir la notificación por el medio subsidiario previsto, dejando constancia de la citación fallida y su fecha.",
    ],
    correcta=2,
    expl=[
        "La citación tiene por objeto que el investigado comparezca; no equivale por sí misma a la notificación.",
        "La inasistencia del investigado no suspende el proceso ni puede paralizar indefinidamente la actuación.",
        "Correcto: fracasada la notificación personal se acude al medio subsidiario, con constancia de lo intentado.",
    ],
),

dict(
    tema="Cómputo de términos", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="intermediate",
    ctx="Un término de tres días para interponer un recurso se notificó un jueves. El viernes siguiente fue festivo y el lunes la sede estuvo cerrada por una jornada de mantenimiento previamente comunicada a los usuarios.",
    q="¿Cómo se cuenta ese término?",
    ops=[
        "En días hábiles, excluyendo sábados, domingos y festivos, y a partir del día hábil siguiente a la notificación.",
        "En días corridos desde el momento mismo de la notificación, incluyendo los sábados, domingos y festivos intermedios.",
        "Desde el día en que el investigado manifieste haber tenido conocimiento efectivo del contenido de la decisión.",
    ],
    correcta=0,
    expl=[
        "Correcto: los términos procesales se cuentan en días hábiles y el día de la notificación no se cuenta.",
        "El cómputo en días corridos solo procede cuando la norma lo dispone expresamente para ese término.",
        "El cómputo no depende de la manifestación del investigado sino de la fecha en que se surtió la notificación.",
    ],
),

dict(
    tema="Pruebas conducentes y pertinentes", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="advanced",
    ctx="El investigado solicita que se reciba declaración a veinte testigos sobre un hecho que ya está acreditado con tres documentos no controvertidos. Según el escrito, los veinte dirían exactamente lo mismo. El término de la investigación vence en un mes.",
    q="¿Cómo debe resolverse la solicitud?",
    ops=[
        "Negarlas todas sin mayor motivación, invocando la economía procesal y el término que resta para la investigación.",
        "Decretar las veinte, dado que toda prueba pedida por la defensa debe practicarse para garantizar la contradicción.",
        "Decretar las necesarias y negar motivadamente las superfluas, explicando por qué el hecho ya está acreditado.",
    ],
    correcta=2,
    expl=[
        "Negar en bloque y sin motivación vulnera el derecho de defensa, por apremiante que sea el término.",
        "El derecho de defensa no obliga a practicar prueba inútil o repetida sobre un hecho ya acreditado.",
        "Correcto: el criterio es la conducencia, la pertinencia y la utilidad, y lo que se niega debe motivarse.",
    ],
),

dict(
    tema="Expediente electrónico y eliminación", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="intermediate",
    ctx="Terminada la digitalización de treinta expedientes, el coordinador propone destruir de inmediato los físicos para liberar el archivo de gestión. Las imágenes quedaron completas y legibles, y el espacio es realmente escaso en la sede.",
    q="¿Qué debe tenerse en cuenta?",
    ops=[
        "Que la eliminación solo procede conforme a las tablas de retención documental y el procedimiento de la entidad.",
        "Que puede destruirse el soporte físico apenas se verifique que la copia digital es fiel e íntegra de todos los folios.",
        "Que los expedientes disciplinarios no pueden digitalizarse y deben conservarse siempre en su soporte original.",
    ],
    correcta=0,
    expl=[
        "Correcto: las tablas de retención y el procedimiento definen qué se conserva, por cuánto tiempo y cómo se elimina.",
        "La digitalización por sí sola no autoriza la eliminación del original, por fiel que sea la copia obtenida.",
        "Sí se pueden digitalizar; lo que está reglado es la eliminación del soporte, no la captura de la imagen.",
    ],
),

dict(
    tema="Información al quejoso", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="basic",
    ctx="Un ciudadano que presentó una queja hace cuatro meses llega preguntando en qué va su trámite. El sustanciador le responde que, como el quejoso no es sujeto procesal, no tiene derecho a información alguna y que debe esperar a que lo citen.",
    q="¿Qué derecho tiene el quejoso?",
    ops=[
        "Tiene los mismos derechos que el investigado, incluido el acceso íntegro al expediente y la facultad de solicitar pruebas.",
        "Tiene derecho a que se le informe el estado del trámite y las decisiones que se adopten, en los términos del procedimiento.",
        "No tiene ningún derecho de información mientras no se le reconozca formalmente la calidad de sujeto procesal.",
    ],
    correcta=1,
    expl=[
        "El quejoso no tiene los mismos derechos del investigado: su rol dentro de la actuación es distinto.",
        "Correcto: se le informa el estado y las decisiones dentro de lo que el procedimiento permite, aunque no sea sujeto procesal.",
        "No ser sujeto procesal no lo deja sin derechos de información sobre el trámite que él mismo promovió.",
    ],
),

dict(
    tema="Corrección de un error formal", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="advanced",
    ctx="Un auto ya notificado tiene equivocado el número de cédula del investigado, aunque el nombre completo, el cargo y los hechos están correctos y no hay riesgo de confusión con otra persona. El error se detecta al preparar la ejecución de la decisión.",
    q="¿Qué procede?",
    ops=[
        "Tachar el dato equivocado en el documento del expediente y escribir al margen el número correcto con firma.",
        "Rehacer la actuación desde el inicio, para que el expediente quede libre de cualquier error en la identificación del investigado.",
        "Corregir el error mediante auto de corrección, notificarlo y dejar constancia de lo ocurrido en el expediente.",
    ],
    correcta=2,
    expl=[
        "Tachar a mano altera el documento y compromete la integridad del expediente y el valor de la prueba.",
        "Rehacer toda la actuación por un error formal que no afecta la identificación es desproporcionado.",
        "Correcto: se trata de un error formal que se corrige con auto de corrección, notificación y constancia.",
    ],
),

dict(
    tema="Acumulación por conexidad", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="advanced",
    ctx="Existen tres quejas separadas contra el mismo servidor por hechos conexos ocurridos entre marzo y mayo del mismo año. Las tres están en indagación previa, en el mismo despacho, y comparten dos de los testigos ya citados.",
    q="¿Qué conviene procesalmente?",
    ops=[
        "Archivar dos de las tres y continuar únicamente con la que describe los hechos de mayor gravedad para el servicio.",
        "Acumularlas en una sola actuación, dado que hay conexidad entre los hechos investigados en cada una de ellas.",
        "Tramitarlas por separado hasta el fallo, para que cada conducta reciba una valoración independiente de las demás.",
    ],
    correcta=1,
    expl=[
        "Archivar quejas válidas sin fundamento legal no procede y deja hechos relevantes sin esclarecer.",
        "Correcto: la acumulación por conexidad permite valorar la conducta de manera integral y evita decisiones contradictorias.",
        "Tres actuaciones paralelas por hechos conexos invitan a decisiones contradictorias y duplican la prueba.",
    ],
),

dict(
    tema="Versión libre y derecho a guardar silencio", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="intermediate",
    ctx="El investigado es citado a rendir versión libre. Comparece acompañado de su defensor y manifiesta que prefiere no declarar. El sustanciador anota en el acta que la negativa se valorará como indicio de responsabilidad.",
    q="¿Qué efecto tiene esa negativa?",
    ops=[
        "Ninguno en su contra: nadie está obligado a declarar contra sí mismo y su silencio no puede valorarse como aceptación.",
        "Se entiende que acepta los hechos descritos en la citación, por no haberlos controvertido al tener la oportunidad.",
        "Se suspende la actuación hasta que el investigado acceda a rendir la versión libre a la que fue citado por el despacho.",
    ],
    correcta=0,
    expl=[
        "Correcto: es una garantía constitucional y la anotación del sustanciador es jurídicamente improcedente.",
        "El silencio no equivale a confesión ni puede leerse como aceptación de los hechos imputados.",
        "El proceso continúa su curso: la negativa a declarar no suspende la actuación.",
    ],
),

dict(
    tema="Informe de sustanciación", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="intermediate",
    ctx="Le encargan preparar el informe con el que el despacho decidirá si archiva o formula cargos. En el expediente hay dos testimonios que favorecen al investigado y un documento que lo compromete. El jefe le pidió que el informe sea breve.",
    q="¿Qué debe contener ese informe?",
    ops=[
        "Un resumen de la versión del quejoso y de las pruebas que respaldan la formulación del pliego de cargos.",
        "Los hechos probados, las pruebas con su folio, las normas presuntamente infringidas y las decisiones posibles.",
        "Su valoración personal sobre la conducta del investigado y sobre la credibilidad que merecen los testigos oídos.",
    ],
    correcta=1,
    expl=[
        "Recoger solo lo que respalda la imputación deja el informe incompleto y puede constituir una falta en sí misma.",
        "Correcto: debe ser completo y objetivo, e incluir expresamente lo que favorece al investigado.",
        "La valoración moral de la persona no es objeto del informe ni del proceso disciplinario.",
    ],
),

dict(
    tema="Trámite de un impedimento", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="advanced",
    ctx="El funcionario que instruye manifiesta por escrito estar impedido por amistad íntima con el investigado. Mientras la instancia competente resuelve, hay dos pruebas decretadas que deben practicarse esta semana y un término que vence el viernes.",
    q="¿Qué ocurre mientras se resuelve el impedimento?",
    ops=[
        "Continúa practicando las pruebas decretadas hasta que le notifiquen la decisión sobre el impedimento manifestado.",
        "Archiva provisionalmente el expediente hasta que se designe al funcionario que deba continuar con la actuación.",
        "Debe abstenerse de actuar y remitir el expediente a quien deba resolver el impedimento que manifestó.",
    ],
    correcta=2,
    expl=[
        "Seguir actuando después de manifestar un impedimento vicia lo que se practique en ese lapso.",
        "El archivo no es la consecuencia de un impedimento: el expediente se remite, no se cierra.",
        "Correcto: abstenerse y remitir es lo que evita que la actuación quede viciada por falta de imparcialidad.",
    ],
),

dict(
    tema="Reserva frente a terceros", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="intermediate",
    ctx="Un periodista pide copia completa de un expediente disciplinario que está en etapa de investigación. Argumenta que se trata de información pública y que el caso es de interés general porque involucra recursos del municipio.",
    q="¿Qué corresponde responder?",
    ops=[
        "Entregarle copia del expediente completo si firma un compromiso de confidencialidad sobre la información que reciba del despacho.",
        "Explicar que la actuación en curso tiene reserva y que el acceso de terceros está limitado, sin perjuicio de informar su estado.",
        "Negar la petición sin explicación, dado que la reserva de la actuación disciplinaria no admite ningún matiz.",
    ],
    correcta=1,
    expl=[
        "Un compromiso privado de confidencialidad no levanta una reserva que la ley establece.",
        "Correcto: se explica la reserva, se entrega lo que sí es público y se motiva la respuesta al peticionario.",
        "Toda negativa debe motivarse: responder sin explicación vulnera el derecho de petición.",
    ],
),

dict(
    tema="Ejecución de la sanción", ref="PGN-PRO",
    refT="Procedimiento disciplinario y sustanciación", nivel="advanced",
    ctx="Queda en firme un fallo que impone suspensión e inhabilidad especial a un servidor de otra entidad. El expediente está completo, el fallo fue notificado y el sancionado ya agotó los recursos. El despacho debe cerrar la actuación.",
    q="¿Qué debe hacerse con la decisión?",
    ops=[
        "Publicarla en la página web de la entidad con los datos completos del sancionado y el detalle de la conducta.",
        "Comunicarla a la entidad nominadora para su ejecución y registrarla en el sistema de sanciones e inhabilidades.",
        "Notificarla al sancionado y archivar el expediente, que es el cierre que corresponde a una actuación que quedó en firme.",
    ],
    correcta=1,
    expl=[
        "La publicación indiscriminada de datos personales no es el procedimiento previsto para ejecutar una sanción.",
        "Correcto: sin comunicación a la nominadora y sin registro, la sanción no produce sus efectos reales.",
        "Notificar y archivar deja la sanción sin ejecución y sin registro en el sistema de inhabilidades.",
    ],
),

dict(
    tema="Tablas de retención documental", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="basic",
    ctx="Un compañero pregunta cuánto tiempo debe conservarse en el archivo de gestión un tipo documental que su dependencia produce cada mes. Dice que en su oficina anterior lo guardaban dos años y que así lo viene haciendo aquí.",
    q="¿Dónde está la respuesta?",
    ops=[
        "En el criterio del jefe de cada dependencia, que conoce la utilidad de cada documento para su propia gestión.",
        "En las tablas de retención documental de la entidad, que fijan tiempos de conservación y disposición final.",
        "En el Código General Disciplinario, que regula la conservación de los expedientes y de los documentos oficiales.",
    ],
    correcta=1,
    expl=[
        "No es una decisión individual de cada jefe ni puede resolverse por la costumbre de otra entidad.",
        "Correcto: las tablas de retención son el instrumento archivístico que define esos tiempos para cada serie.",
        "El Código Disciplinario no regula la conservación documental, que tiene su propio marco normativo.",
    ],
),

dict(
    tema="Documento sin trazabilidad", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="intermediate",
    ctx="En la carpeta compartida de la dependencia aparece un archivo llamado «informe_final_v7_definitivo_ESTE_SI.docx», sin fecha, sin autor y sin número de versión oficial. Hay otros cinco archivos con nombres parecidos y contenidos distintos.",
    q="¿Cuál es el problema de fondo?",
    ops=[
        "Que ocupa espacio innecesario en el servidor y dificulta la administración del almacenamiento de la dependencia.",
        "Que el nombre del archivo no sigue la convención de nomenclatura que la entidad adoptó para sus documentos.",
        "Que no hay trazabilidad: sin autor, fecha ni control de versiones no se sabe cuál es el documento válido.",
    ],
    correcta=2,
    expl=[
        "El espacio de almacenamiento es lo de menos frente a la imposibilidad de identificar el documento vigente.",
        "El nombre es apenas un síntoma: el problema está en la ausencia de autor, fecha y control de versiones.",
        "Correcto: sin trazabilidad el documento no sirve como soporte de nada ni permite establecer quién responde por él.",
    ],
),

dict(
    tema="Digitalización fiel", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="intermediate",
    ctx="Al revisar la digitalización de un expediente, usted encuentra que cuatro folios quedaron cortados en el borde derecho y dos resultan ilegibles por sombra del escáner. El lote ya se cargó al repositorio y el operador cerró la tarea.",
    q="¿Qué debe hacerse?",
    ops=[
        "Repetir la captura de esos folios, porque la copia digital debe ser fiel e íntegra del documento original.",
        "Transcribir a máquina el contenido que alcanza a leerse en esos folios y anexarlo como complemento del archivo.",
        "Dejar el lote como está y advertir en una nota del expediente que seis folios quedaron parcialmente ilegibles.",
    ],
    correcta=0,
    expl=[
        "Correcto: la fidelidad y la integridad son requisitos de la copia; una imagen incompleta no sustituye al documento.",
        "Transcribir sustituye el documento por una interpretación de quien transcribe, lo que no es admisible.",
        "Advertirlo no corrige el defecto cuando repetir la captura es perfectamente posible.",
    ],
),

dict(
    tema="Clasificación de la información", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="advanced",
    ctx="Debe preparar un informe público sobre la atención prestada durante el semestre. La base contiene nombre, cédula, dirección y motivo de consulta de cada persona atendida. El informe se publicará en la página web de la entidad.",
    q="¿Cómo procede?",
    ops=[
        "Publicar la base completa, dado que la información sobre la gestión de la entidad es pública por regla general.",
        "Abstenerse de publicar el informe, para evitar cualquier riesgo asociado al tratamiento de datos personales.",
        "Publicar los datos agregados y excluir o anonimizar la información personal de las personas atendidas.",
    ],
    correcta=2,
    expl=[
        "La publicidad de la gestión no se extiende a los datos personales de los ciudadanos que fueron atendidos.",
        "Negarse a informar del todo incumple el deber de transparencia sobre la gestión de la entidad.",
        "Correcto: se informa la gestión sin exponer a las personas, que es lo que exige la protección de datos.",
    ],
),

dict(
    tema="Correo institucional", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="basic",
    ctx="Un servidor envía desde su correo personal una comunicación oficial a otra entidad, porque el correo institucional estaba lento y el término vencía ese día. La comunicación llegó a tiempo y fue respondida sin inconvenientes.",
    q="¿Qué problema genera esa práctica?",
    ops=[
        "Genera un problema de imagen institucional frente a la entidad destinataria de la comunicación que se envió por ese medio.",
        "La comunicación queda fuera de los canales oficiales y del archivo, sin trazabilidad ni respaldo institucional.",
        "No genera problema alguno, en la medida en que la comunicación llegó dentro del término y fue atendida.",
    ],
    correcta=1,
    expl=[
        "La imagen es secundaria frente al problema de archivo y de prueba que genera la comunicación por fuera del canal.",
        "Correcto: la vía por la que sale una comunicación oficial no es indiferente para su trazabilidad ni para su respaldo.",
        "Que haya llegado a tiempo no corrige la ausencia de registro institucional de la comunicación.",
    ],
),

dict(
    tema="Base de datos con duplicados", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="intermediate",
    ctx="Al consolidar el reporte trimestral usted detecta que la base tiene ciento veinte registros duplicados por errores de digitación en el número de cédula. El reporte se entrega mañana y la cifra total quedaría inflada en un ocho por ciento.",
    q="¿Qué hace antes de reportar?",
    ops=[
        "Reportar las dos cifras, la depurada y la del sistema, y dejar que quien recibe el informe decida cuál de ellas usar.",
        "Reportar el total tal como sale del sistema, que es la fuente oficial de la cual se alimenta el indicador.",
        "Depurar los duplicados con un criterio documentado y reportar la cifra corregida indicando el ajuste realizado.",
    ],
    correcta=2,
    expl=[
        "Entregar dos cifras sin explicar la diferencia traslada el problema a quien lee y no resuelve nada.",
        "Reportar una cifra que se sabe inflada compromete a quien firma, aunque provenga del sistema.",
        "Correcto: depurar con criterio documentado y explicar el ajuste es lo que hace verificable el reporte.",
    ],
),

dict(
    tema="Préstamo de expedientes", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="basic",
    ctx="Un compañero de otra dependencia pide llevarse un expediente del archivo de gestión para consultarlo. Dice que lo necesita para un informe que le pidió su jefe y que lo devuelve mañana sin falta.",
    q="¿Cuál es el procedimiento correcto?",
    ops=[
        "Entregarlo y pedirle que avise por mensaje cuando lo devuelva, para no demorar el informe que debe elaborar.",
        "Negar el préstamo en todo caso, pues los expedientes del archivo de gestión no pueden salir de la dependencia.",
        "Registrar el préstamo en el formato previsto y verificar que la consulta se relacione con sus funciones.",
    ],
    correcta=2,
    expl=[
        "Un aviso informal no deja trazabilidad sobre quién tiene el expediente ni desde cuándo.",
        "La negativa absoluta entorpece el trabajo legítimo de otras dependencias de la entidad.",
        "Correcto: registro del préstamo con fecha de devolución y verificación de la relación con sus funciones.",
    ],
),

dict(
    tema="Copias de seguridad", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="intermediate",
    ctx="Toda la información de un proceso a cargo de la dependencia está en el computador de una sola persona, en carpetas locales sin respaldo en los sistemas institucionales. Esa persona lleva cuatro años en el cargo y nunca ha fallado una entrega.",
    q="¿Cuál es el riesgo principal?",
    ops=[
        "Que la carga de trabajo se concentre en una sola persona y que eso afecte su rendimiento y su bienestar laboral.",
        "Que la información de la entidad dependa de un equipo y de una persona, y se pierda ante un daño o una ausencia.",
        "Que el disco del computador se llene y empiece a afectar el desempeño de las aplicaciones institucionales.",
    ],
    correcta=1,
    expl=[
        "La carga de trabajo es un efecto secundario y no el riesgo que compromete la continuidad del servicio.",
        "Correcto: la información es de la entidad y debe vivir en sus sistemas para garantizar la continuidad.",
        "El almacenamiento no es el problema: el problema es la pérdida de información institucional.",
    ],
),

dict(
    tema="Formatos del sistema de gestión", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="basic",
    ctx="Una dependencia dejó de usar el formato oficial de acta y creó uno propio, porque el oficial «no le sirve» para sus reuniones. El formato propio circula por correo entre los integrantes del equipo desde hace un año.",
    q="¿Cómo debe manejarse?",
    ops=[
        "Usar el formato vigente del sistema de gestión y tramitar su actualización por el canal previsto si no sirve.",
        "Mantener el formato propio, que recoge mejor la información que la dependencia necesita de sus reuniones.",
        "Usar los dos formatos en paralelo, de modo que se cumpla con el sistema de gestión y se conserve la información útil.",
    ],
    correcta=0,
    expl=[
        "Correcto: los formatos paralelos rompen la estandarización, y la mejora se tramita por el canal correspondiente.",
        "Un formato propio al margen del sistema de gestión no tiene respaldo institucional ni trazabilidad.",
        "Duplicar formatos duplica el trabajo y el error, sin resolver el problema que originó el formato propio.",
    ],
),

dict(
    tema="Indicador sin fuente verificable", ref="PGN-GES",
    refT="Gestión documental y calidad de la información", nivel="advanced",
    ctx="Le piden reportar un indicador de cumplimiento que la dependencia viene informando desde hace tres años. Al buscar la fuente, nadie sabe de qué base sale el dato ni cómo se calcula. La cifra reportada ha sido siempre la misma.",
    q="¿Qué hace?",
    ops=[
        "Reportar el mismo valor que se ha venido informando, que es el dato histórico con el que se construyó la serie.",
        "Reportar cero mientras se define la fuente, de modo que quede claro que el indicador no está siendo medido.",
        "Advertir que el indicador no tiene fuente verificable y proponer definir la fuente y el método de cálculo.",
    ],
    correcta=2,
    expl=[
        "Repetir una cifra heredada sin fuente la convierte en responsabilidad de quien la firma hoy.",
        "Reportar cero también es reportar un dato que no corresponde a la realidad de la gestión.",
        "Correcto: señalar el vacío y no respaldar lo que no se puede sustentar es lo que protege al servidor y a la entidad.",
    ],
),

dict(
    tema="Usuario alterado en ventanilla", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="intermediate",
    ctx="Un ciudadano llega a la ventanilla gritando porque lleva tres meses esperando respuesta a una petición. Al verificar el sistema, usted confirma que la petición efectivamente está vencida y sin respuesta desde hace sesenta días. Hay seis personas más en la fila.",
    q="¿Cuál es la actuación correcta?",
    ops=[
        "Pedirle que se retire y que regrese cuando esté más tranquilo, para no afectar la atención de las demás personas de la fila.",
        "Atenderlo en un espacio aparte, verificar el estado real de la petición y darle una respuesta concreta sobre el plazo.",
        "Explicarle que la demora corresponde a otra dependencia e indicarle a dónde debe dirigirse a reclamar.",
    ],
    correcta=1,
    expl=[
        "Pedirle que se retire no resuelve una demora que es real y que es responsabilidad de la entidad.",
        "Correcto: bajar la tensión y resolver el problema de fondo, que en este caso efectivamente existe.",
        "Trasladarle la responsabilidad a otra dependencia deja al ciudadano exactamente donde estaba.",
    ],
),

dict(
    tema="Tarea que excede el manual de funciones", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="advanced",
    ctx="Su jefe le pide proyectar un auto que, según el manual de funciones, corresponde a un cargo del nivel profesional. Usted tiene la formación para hacerlo y el despacho está congestionado. El auto llevaría la firma del profesional responsable.",
    q="¿Qué hace?",
    ops=[
        "Proyectarlo y suscribirlo usted mismo, dado que cuenta con la formación necesaria para elaborar ese tipo de decisión.",
        "Negarse a elaborarlo, puesto que la función no figura entre las que le asigna el manual de funciones de su empleo.",
        "Manifestar por escrito que la función no está en su manual y pedir instrucciones claras sobre en qué calidad actúa.",
    ],
    correcta=2,
    expl=[
        "Suscribir una actuación que no le compete puede comprometer la validez del acto y su propia responsabilidad.",
        "Negarse sin más puede afectar el servicio; lo procedente es aclarar y dejar constancia, no bloquear.",
        "Correcto: aclarar, dejar constancia de en qué calidad apoya y actuar dentro de lo que le corresponde.",
    ],
),

dict(
    tema="Información pedida por un compañero", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="intermediate",
    ctx="Un compañero de otra área le pide por chat los datos de un expediente que no tiene relación con su trabajo. Dice que es por curiosidad, porque conoce al investigado. Usted tiene acceso a esa información por razón de su cargo.",
    q="¿Qué responde?",
    ops=[
        "Enviarle solo una parte de la información, la suficiente para satisfacer su curiosidad sin exponer el expediente completo.",
        "No enviarlos y explicarle que el acceso está atado a las funciones de cada quien, no a la pertenencia a la entidad.",
        "Enviárselos pidiéndole discreción, dado que se trata de un compañero de la misma entidad y del mismo nivel.",
    ],
    correcta=1,
    expl=[
        "Enviar una parte sigue siendo divulgación indebida de información a la que el compañero no debe acceder.",
        "Correcto: el criterio es la necesidad funcional, y conviene decirlo con claridad y sin dramatismo.",
        "Un pacto de discreción no corrige un acceso que desde el principio es indebido.",
    ],
),

dict(
    tema="Carga acumulada por una ausencia", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="advanced",
    ctx="Una compañera se incapacitó por un mes y su carga quedó repartida entre dos personas, incluido usted. Siete expedientes tienen términos que vencen en las próximas dos semanas y usted alcanza a atender cuatro trabajando a ritmo normal.",
    q="¿Cuál es la conducta más profesional?",
    ops=[
        "Hacer inventario de los asuntos y sus términos, priorizar lo perentorio e informar por escrito qué se alcanza.",
        "Avanzar lo que alcance sin informar nada, para no dar la impresión de que se está quejando de la carga adicional.",
        "Solicitar que se le retire toda la carga adicional, que corresponde a un empleo distinto del que usted desempeña.",
    ],
    correcta=0,
    expl=[
        "Correcto: inventario, priorización y aviso oportuno por escrito permiten que el jefe decida con información.",
        "Callar hace que el vencimiento de los términos termine cayendo sobre quien no avisó a tiempo.",
        "Rechazar en bloque la carga adicional no resuelve la continuidad del servicio ni los términos que corren.",
    ],
),

dict(
    tema="Dato errado ya informado", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="advanced",
    ctx="Usted descubre que un dato enviado la semana pasada a una entidad externa estaba equivocado y que esa entidad ya lo usó para adoptar una decisión. El error se originó en la planilla que le entregó otra dependencia.",
    q="¿Qué hace?",
    ops=[
        "Informar de inmediato a su jefe y a la entidad destinataria, enviar el dato correcto y proponer cómo corregir.",
        "Informar a la dependencia que entregó la planilla para que sea ella quien asuma la corrección ante la entidad externa.",
        "Esperar a que la entidad destinataria advierta la inconsistencia y entonces explicar cómo se originó el error.",
    ],
    correcta=0,
    expl=[
        "Correcto: informar, corregir y proponer el remedio es lo que limita el daño que ya se está produciendo.",
        "Buscar el origen del error es útil, pero no sustituye el deber de corregir frente a quien recibió el dato.",
        "Esperar prolonga el daño y elimina la posibilidad de corregir la decisión que ya se adoptó.",
    ],
),

dict(
    tema="Presión para saltarse un paso", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="advanced",
    ctx="Para cumplir la meta del mes, le sugieren registrar como terminados dieciocho trámites a los que todavía les falta el paso de verificación. La meta se mide el viernes y la verificación tomaría dos semanas más.",
    q="¿Cuál es la respuesta correcta?",
    ops=[
        "Registrar la mitad de los trámites, de modo que la meta se aproxime sin comprometer del todo la información.",
        "Registrarlos y llevar aparte un control personal de cuáles quedaron pendientes de verificación para completarlos.",
        "No registrarlos como terminados, informar cuántos están completos y proponer un plan para cerrar los pendientes.",
    ],
    correcta=2,
    expl=[
        "Un punto medio sigue siendo un reporte que no corresponde a la realidad de la gestión.",
        "Un control personal no corrige el registro oficial, que es el que alimenta la información institucional.",
        "Correcto: reportar la realidad y proponer cómo cerrar la brecha, dejando constancia de lo que se le pidió.",
    ],
),

dict(
    tema="Error de un compañero que afecta a un ciudadano", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="intermediate",
    ctx="Detecta que un compañero respondió mal una petición y que el ciudadano quedó con información equivocada sobre el término que tiene para interponer un recurso. La respuesta salió hace tres días y el término vence en diez.",
    q="¿Qué hace primero?",
    ops=[
        "Reportar el hecho a control interno disciplinario, que es la instancia competente para valorar esa conducta.",
        "Corregir usted mismo la información, enviando una comunicación al ciudadano con el término correcto para el recurso.",
        "Avisarle al compañero y al jefe para que la respuesta se corrija cuanto antes y el ciudadano reciba el dato correcto.",
    ],
    correcta=2,
    expl=[
        "Empezar por la vía disciplinaria no corrige a tiempo la información que el ciudadano necesita.",
        "Corregir por fuera del procedimiento genera dos respuestas distintas sobre el mismo asunto.",
        "Correcto: lo urgente es reparar el efecto; la valoración de la conducta viene después y no le corresponde a usted.",
    ],
),

dict(
    tema="Solicitud de un directivo fuera de canal", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="intermediate",
    ctx="Un directivo de otra dependencia le escribe por mensajería instantánea pidiéndole copia de una decisión que aún no ha sido notificada. Dice que la necesita para una reunión de mañana y que después se formaliza la solicitud.",
    q="¿Cómo procede?",
    ops=[
        "Enviársela pidiéndole discreción hasta que la decisión se notifique formalmente a las partes del proceso.",
        "No responder el mensaje y continuar con el trámite normal, dejando que el directivo formalice su solicitud por escrito.",
        "Explicarle que la decisión se entrega una vez notificada y por el canal institucional, e informar a su jefe.",
    ],
    correcta=2,
    expl=[
        "La discreción no convierte en regular una entrega anticipada de una decisión sin notificar.",
        "Ignorar el mensaje deja el asunto sin resolver y sin registro de la solicitud que se recibió.",
        "Correcto: canal institucional, momento procesal correcto y aviso al jefe inmediato de lo ocurrido.",
    ],
),

dict(
    tema="Capacitación obligatoria y carga del día", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="basic",
    ctx="Lo inscriben en una capacitación obligatoria de cuatro horas que coincide con el día de mayor carga de la semana. La capacitación fue programada con quince días de antelación y hace parte del plan institucional.",
    q="¿Cuál es la conducta correcta?",
    ops=[
        "Asistir y organizar previamente con el jefe la redistribución del trabajo de ese día en la dependencia.",
        "No asistir y justificar la inasistencia con la carga de trabajo, que es una necesidad real del servicio.",
        "Pedirle a un compañero que asista en su lugar y le comparta después el material y las conclusiones.",
    ],
    correcta=0,
    expl=[
        "Correcto: la capacitación fue programada con antelación y la carga se coordina, no se usa como excusa.",
        "La capacitación obligatoria no es opcional según la carga del día y hace parte del deber de actualizarse.",
        "Sustituirse sin autorización desvirtúa la programación y el registro de la capacitación.",
    ],
),

dict(
    tema="Instrucciones contradictorias", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="advanced",
    ctx="Su jefe inmediato le ordena por correo una cosa y el coordinador del proceso le indica por el mismo medio exactamente lo contrario. Ambas instrucciones tienen fecha de hoy y ambas exigen ejecución antes del cierre de la semana.",
    q="¿Qué hace?",
    ops=[
        "Cumplir la instrucción de quien tiene mayor jerarquía y archivar el correo del otro como constancia del hecho.",
        "Poner la contradicción por escrito ante los dos, pedir una instrucción única y abstenerse de ejecutar mientras tanto.",
        "Elegir la instrucción que resulte más viable de cumplir en el tiempo disponible y reportar el resultado al cierre de la semana.",
    ],
    correcta=1,
    expl=[
        "Ejecutar en silencio deja la contradicción sin resolver y traslada el riesgo a quien ejecuta.",
        "Correcto: evidenciar la contradicción por escrito y pedir una sola instrucción es lo que protege la actuación.",
        "La viabilidad no es el criterio para escoger entre dos instrucciones que se contradicen.",
    ],
),

dict(
    tema="Firma de un documento no revisado", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="advanced",
    ctx="Le pasan un documento de veintidós páginas para firmar cinco minutos antes de que cierre el término. Quien lo elaboró le asegura que está revisado. Su firma certifica que la información allí consignada corresponde a los registros.",
    q="¿Qué hace?",
    ops=[
        "Firmarlo con base en la revisión de quien lo elaboró y revisarlo con calma al día siguiente para verificar.",
        "Negarse a firmar documentos presentados sobre el cierre del término, como regla general de la dependencia.",
        "Revisar al menos lo que su firma certifica y, si no alcanza, decirlo por escrito y pedir el tiempo mínimo.",
    ],
    correcta=2,
    expl=[
        "Revisar después del término ya no permite corregir lo que se certificó con la firma.",
        "Una negativa general a lo urgente paraliza el servicio y no distingue los casos en que sí se alcanza.",
        "Correcto: quien firma responde por el contenido, y el afán no es una causal de exoneración.",
    ],
),

dict(
    tema="Compañero que incumple el horario", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="advanced",
    ctx="Un compañero del mismo nivel llega sistemáticamente tarde a la atención de la ventanilla y los usuarios esperan de pie en el pasillo sin que nadie los reciba. Lleva un mes así y usted lo ha comentado con él una vez.",
    q="¿Qué hace?",
    ops=[
        "Comentarlo con los demás compañeros de la dependencia para que entre todos le hagan ver el efecto de su conducta.",
        "Abstenerse de intervenir, dado que el control del horario corresponde al jefe inmediato y no a los pares.",
        "Informar a la coordinación, porque hay usuarios sin atención y ya hubo una conversación directa sin resultado.",
    ],
    correcta=2,
    expl=[
        "Comentarlo con terceros no corrige la conducta ni protege a los usuarios que están esperando.",
        "La afectación del servicio al ciudadano no es un asunto indiferente para quien la presencia a diario.",
        "Correcto: hubo conversación directa previa y la situación persiste, de modo que corresponde el canal institucional.",
    ],
),

dict(
    tema="Cruce entre una comisión y un término", ref="PGN-JUI",
    refT="Juicio situacional del nivel técnico", nivel="intermediate",
    ctx="Le asignan una comisión de tres días que coincide con el vencimiento de dos términos procesales en expedientes a su cargo. La comisión se notificó hoy y los términos vencen el miércoles y el jueves de esa misma semana.",
    q="¿Cuál es la conducta más adecuada?",
    ops=[
        "Aceptar la comisión y resolver los términos como pueda durante las noches de los días que dure el desplazamiento.",
        "Informar a tiempo del cruce, proponer un orden o una fecha alterna y precisar qué puede cumplirse con calidad.",
        "Rechazar la comisión por escrito, dado que los términos procesales tienen prelación sobre cualquier otra actividad.",
    ],
    correcta=1,
    expl=[
        "Resolver términos en condiciones improvisadas pone en riesgo la calidad de decisiones que no admiten corrección.",
        "Correcto: anticipar el cruce permite que quien asigna decida con información y que nada quede a la deriva.",
        "Un rechazo sin alternativa no resuelve el problema institucional que generó la asignación.",
    ],
),

]
