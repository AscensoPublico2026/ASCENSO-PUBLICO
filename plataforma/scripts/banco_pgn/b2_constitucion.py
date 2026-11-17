# -*- coding: utf-8 -*-
"""Eje: Estado, Constitución y estructura del Estado."""

CON = "Estado, Constitución y estructura del Estado"

BANCO = [
dict(
    tema="Fines esenciales del Estado", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="intermediate",
    ctx="Usted proyecta el concepto con el que la Procuraduría sustentará una actuación preventiva ante una entidad que suspendió un programa de atención a población desplazada alegando que el presupuesto se destinó a otra prioridad. El jefe le pide que el concepto arranque por el fundamento constitucional y no por la norma reglamentaria.",
    q="¿Cuál de los siguientes es un fin esencial del Estado según el artículo 2 de la Constitución?",
    ops=[
        "Mantener el equilibrio del presupuesto público por encima de las demás consideraciones de la gestión.",
        "Servir a la comunidad, promover la prosperidad general y garantizar la efectividad de los principios y derechos.",
        "Garantizar la rentabilidad de las empresas del Estado y la sostenibilidad financiera de sus programas.",
    ],
    correcta=1,
    expl=[
        "La disciplina fiscal es un principio relevante del ordenamiento, pero no figura entre los fines esenciales del artículo 2.",
        "Correcto: son los fines que enumera el artículo 2, y por eso la suspensión del programa debe medirse contra ellos y no solo contra el presupuesto.",
        "La rentabilidad no es un fin esencial del Estado y no puede oponerse a la efectividad de los derechos.",
    ],
),

dict(
    tema="Estado social de derecho", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="advanced",
    ctx="En un concepto que usted elabora, debe explicar qué agrega la fórmula «Estado social de derecho» del artículo 1 frente a la noción clásica de Estado de derecho. Un compañero sostiene que la expresión es puramente retórica y que, en la práctica, la administración solo está obligada a cumplir la ley.",
    q="¿Cuál es la diferencia central entre las dos fórmulas?",
    ops=[
        "Que el Estado social de derecho sustituye el principio de legalidad por criterios de equidad material.",
        "Que la fórmula social tiene alcance declarativo y no genera para la administración obligaciones distintas de las que ya impone el Estado de derecho.",
        "Que al sometimiento del poder a la ley se suman obligaciones materiales sobre las condiciones de vida de las personas.",
    ],
    correcta=2,
    expl=[
        "El principio de legalidad no desaparece: se mantiene y se complementa con un contenido prestacional.",
        "La jurisprudencia constitucional le ha dado consecuencias jurídicas concretas y exigibles, de modo que no es retórica.",
        "Correcto: lo social agrega un contenido prestacional y una exigencia de efectividad de los derechos.",
    ],
),

dict(
    tema="Ramas del poder y órganos autónomos", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="basic",
    ctx="Un practicante que acaba de llegar al despacho le pregunta en qué rama del poder público se ubica la Procuraduría General de la Nación. Argumenta que, como adelanta procesos y profiere fallos, debería pertenecer a la Rama Judicial, y que el hecho de que el Procurador sea elegido por el Senado la acercaría más bien al Legislativo.",
    q="¿Cuál es la ubicación correcta de la entidad?",
    ops=[
        "En la Rama Judicial, dada la naturaleza jurisdiccional que la reforma le atribuyó al proceso disciplinario.",
        "En los órganos autónomos e independientes de control, por fuera de las tres ramas del poder público.",
        "En la Rama Ejecutiva, puesto que la actividad que desarrolla constituye materialmente función administrativa.",
    ],
    correcta=1,
    expl=[
        "Adelantar procesos y decidirlos no la incorpora a la Rama Judicial, cuya composición define el artículo 116.",
        "Correcto: junto con la Contraloría y otros, integra los organismos de control, autónomos frente a las tres ramas.",
        "Ejercer función administrativa no convierte a un órgano en parte del Ejecutivo; muchos órganos autónomos la ejercen.",
    ],
),

dict(
    tema="Bloque de constitucionalidad", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="advanced",
    ctx="En una actuación por presuntas violaciones de derechos humanos, el apoderado de la víctima invoca un tratado internacional ratificado por Colombia que reconoce derechos no susceptibles de limitación en los estados de excepción. La entidad investigada responde que ese instrumento no puede aplicarse porque ninguna ley interna lo ha reproducido.",
    q="¿Cómo se integra ese tratado al ordenamiento interno?",
    ops=[
        "Hace parte del bloque de constitucionalidad y sirve como parámetro de interpretación y de control.",
        "Se integra únicamente cuando una ley posterior reproduce su contenido en el ordenamiento nacional.",
        "Obliga solo en el plano internacional y no puede invocarse directamente ante autoridades colombianas.",
    ],
    correcta=0,
    expl=[
        "Correcto: el artículo 93 da prevalencia en el orden interno a los tratados de derechos humanos que prohíben su limitación en estados de excepción.",
        "No se requiere una ley de reproducción: la ratificación y la prevalencia del artículo 93 bastan.",
        "Los tratados ratificados producen efectos internos y son exigibles ante las autoridades nacionales.",
    ],
),

dict(
    tema="Función administrativa y sus principios", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="intermediate",
    ctx="Una entidad exige a los ciudadanos que tramitan un subsidio tres documentos que ella misma expidió y que reposan en sus archivos: el certificado de afiliación, la constancia de residencia y la copia del acto que los incluyó en el programa. El trámite está publicado en la página web y el formulario es gratuito.",
    q="¿Qué principio del artículo 209 de la Constitución se está desconociendo principalmente?",
    ops=[
        "La moralidad, por existir un propósito de favorecer a quienes logran reunir los documentos exigidos.",
        "La economía, que exige adelantar la actuación con el menor desgaste para el ciudadano y la administración.",
        "La imparcialidad, porque la exigencia documental no se aplica por igual a todos los solicitantes del subsidio.",
    ],
    correcta=1,
    expl=[
        "La moralidad supone un propósito torcido que aquí no está acreditado: lo que hay es una exigencia inútil.",
        "Correcto: exigir lo que la entidad ya posee contraría la economía y el deber de no pedir documentos que reposan en la administración.",
        "Nada en el caso indica que la exigencia se aplique de manera desigual entre los solicitantes.",
    ],
),

dict(
    tema="Responsabilidad de los servidores públicos", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="intermediate",
    ctx="En una capacitación dirigida a contratistas y servidores de planta, alguien pregunta si todos responden igual ante la ley. El expositor responde que la entidad siempre asume la responsabilidad y que, en el peor de los casos, el servidor solo responde penalmente.",
    q="¿Qué diferencia establece el artículo 6 de la Constitución?",
    ops=[
        "Unos y otros responden exactamente por lo mismo: por infringir la Constitución y las leyes vigentes.",
        "Los servidores públicos no responden de manera personal, pues la responsabilidad patrimonial recae íntegramente sobre la entidad que los vinculó.",
        "Los particulares responden por infringir la Constitución y la ley; los servidores, además, por omisión o extralimitación.",
    ],
    correcta=2,
    expl=[
        "Existe una diferencia expresa de régimen que esta opción pasa por alto.",
        "La responsabilidad personal del servidor existe y el Estado puede repetir contra él cuando sea condenado.",
        "Correcto: esa es la fórmula del artículo 6, que agrega para el servidor la omisión y la extralimitación en el ejercicio de sus funciones.",
    ],
),

dict(
    tema="Derecho a la igualdad y trato diferenciado", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="advanced",
    ctx="Una entidad establece un turno prioritario de atención para personas mayores de sesenta años, mujeres gestantes y personas con discapacidad. Un usuario presenta queja ante la Procuraduría alegando que el turno preferencial lo discrimina a él, que lleva cuarenta minutos esperando, y pide que se ordene atender por estricto orden de llegada.",
    q="¿Cómo debe resolverse técnicamente ese planteamiento?",
    ops=[
        "No hay vulneración: el artículo 13 ordena promover la igualdad real y adoptar medidas en favor de grupos en debilidad manifiesta.",
        "No hay vulneración: la entidad goza de autonomía administrativa para organizar la prestación del servicio y los turnos como lo estime conveniente.",
        "Hay vulneración, pues cualquier trato diferenciado entre usuarios contraría el derecho a la igualdad del artículo 13.",
    ],
    correcta=0,
    expl=[
        "Correcto: los incisos segundo y tercero del artículo 13 fundamentan las acciones afirmativas en favor de esos grupos.",
        "La autonomía organizativa no es el fundamento de la medida: lo es el mandato constitucional de igualdad material.",
        "La igualdad formal no agota el contenido del artículo 13, que ordena corregir desigualdades de hecho.",
    ],
),

dict(
    tema="Debido proceso administrativo", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="advanced",
    ctx="Una entidad impone una multa a un contratista con fundamento en un informe técnico elaborado por la interventoría. El informe nunca se puso en conocimiento del contratista, que se enteró de su existencia al leer la motivación del acto sancionatorio. La entidad sostiene que se trata de un documento interno de su propia gestión.",
    q="¿Qué garantía se vulneró?",
    ops=[
        "Ninguna, porque el informe de interventoría es un documento de gestión interna de la entidad contratante.",
        "La publicidad, defecto que queda saneado con la notificación personal del acto sancionatorio y con la publicación de su parte resolutiva.",
        "El debido proceso del artículo 29, que se aplica a toda actuación administrativa e incluye controvertir la prueba.",
    ],
    correcta=2,
    expl=[
        "Un documento que sirve de fundamento a la decisión deja de ser puramente interno y debe someterse a contradicción.",
        "Publicar la decisión no sanea la falta de contradicción previa sobre la prueba que la sustenta.",
        "Correcto: el artículo 29 extiende el debido proceso a lo administrativo e incluye el derecho a controvertir las pruebas en contra.",
    ],
),

dict(
    tema="Control de constitucionalidad", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="intermediate",
    ctx="Un ciudadano presenta demanda de inconstitucionalidad contra una ley que modifica el régimen de carrera administrativa. El expediente llega a la Corte Constitucional y usted debe explicar a un grupo de estudiantes en práctica qué papel cumple la Procuraduría dentro de ese trámite.",
    q="¿Cuál es ese papel?",
    ops=[
        "Rendir concepto dentro del proceso de control de constitucionalidad, conforme al artículo 278 de la Constitución.",
        "Decidir sobre la admisión o el rechazo de la demanda cuando esta no cumple los requisitos formales que exige el decreto que regula el trámite.",
        "Representar al Congreso de la República en la defensa de la constitucionalidad de la ley demandada.",
    ],
    correcta=0,
    expl=[
        "Correcto: rendir concepto en los procesos de control de constitucionalidad es una función del Procurador General.",
        "La admisión de la demanda la decide el magistrado sustanciador y no el Ministerio Público.",
        "La defensa de la ley corresponde a quienes intervengan en ese sentido; el Ministerio Público no es apoderado del Congreso.",
    ],
),

dict(
    tema="Descentralización y autonomía territorial", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="intermediate",
    ctx="Un alcalde se niega a aplicar una ley nacional que regula la prestación de un servicio en su municipio. Sostiene que la autonomía territorial del artículo 287 lo faculta para decidir cómo gestionar sus intereses y que la ley invade competencias propias del municipio. El concejo respaldó su posición mediante un acuerdo.",
    q="¿Cuál es la lectura correcta de la autonomía territorial?",
    ops=[
        "La autonomía se ejerce dentro de los límites de la Constitución y la ley, y no habilita a inaplicar la ley nacional.",
        "La autonomía comprende únicamente la gestión presupuestal de los recursos propios y no se extiende a las decisiones administrativas del alcalde.",
        "La autonomía ampara la decisión del alcalde cuando el concejo municipal la respalda mediante un acuerdo.",
    ],
    correcta=0,
    expl=[
        "Correcto: el artículo 287 reconoce la autonomía para la gestión de sus intereses, pero dentro de los límites de la Constitución y la ley.",
        "La autonomía abarca más que lo presupuestal e incluye la gestión administrativa de sus asuntos.",
        "Un acuerdo municipal no puede autorizar la inaplicación de una ley de la República.",
    ],
),

dict(
    tema="Servidores públicos: categorías", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="intermediate",
    ctx="Una entidad vinculó mediante contrato de prestación de servicios a una persona que lleva tres años renovando el contrato y que maneja el archivo de un programa con recursos públicos. Llega una queja por presunta pérdida de documentos y se discute si esa persona puede ser sujeto de control disciplinario.",
    q="¿Cuál es la respuesta correcta según el artículo 123 de la Constitución?",
    ops=[
        "Es servidora pública, pues la duración ininterrumpida del vínculo superó con creces el término que permite el contrato de prestación de servicios.",
        "No es servidora pública ni puede ser objeto de control disciplinario bajo ninguna de las modalidades previstas.",
        "No es servidora pública, pero puede ser disciplinable como particular que administra recursos o ejerce funciones públicas.",
    ],
    correcta=2,
    expl=[
        "La duración del contrato no transforma la naturaleza del vínculo ni confiere la calidad de servidor público.",
        "Sí puede ser disciplinable en los supuestos legales de particulares con funciones públicas o manejo de recursos.",
        "Correcto: los servidores públicos son los miembros de corporaciones públicas, los empleados y los trabajadores del Estado; el contratista es un particular disciplinable en los casos que la ley señala.",
    ],
),

dict(
    tema="Prevalencia del interés general", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="advanced",
    ctx="Un municipio necesita intervenir predios de siete familias para construir una vía que beneficiaría a la mayoría de la población. Las familias se oponen y el alcalde sostiene que el artículo 1 de la Constitución, al consagrar la prevalencia del interés general, lo autoriza a iniciar las obras de inmediato sin más trámite.",
    q="¿Cómo opera el principio de prevalencia del interés general en ese caso?",
    ops=[
        "Orienta la decisión, pero la afectación requiere fundamento legal, proporcionalidad, debido proceso e indemnización.",
        "Permite ejecutar la obra de inmediato, pues el beneficio de la mayoría desplaza el interés particular de los afectados.",
        "Impide afectar la propiedad privada, que solo puede limitarse con el consentimiento expreso de sus titulares.",
    ],
    correcta=0,
    expl=[
        "Correcto: la prevalencia del interés general convive con las garantías individuales y exige proporcionalidad y procedimiento.",
        "Invocar el interés general no habilita a saltarse los procedimientos ni las garantías de los afectados.",
        "Sí es posible afectar la propiedad por motivos de utilidad pública, siguiendo el procedimiento y con indemnización.",
    ],
),

dict(
    tema="Control fiscal y control disciplinario", ref="PGN-CON",
    refT="Estado, Constitución y estructura del Estado", nivel="intermediate",
    ctx="El pago de una obra que nunca se ejecutó genera, por los mismos hechos y contra los mismos funcionarios, un proceso de responsabilidad fiscal ante la Contraloría y una investigación disciplinaria en la Procuraduría. El apoderado de los investigados solicita que una de las dos se archive por violación del non bis in idem.",
    q="¿Puede haber dos actuaciones simultáneas sin vulnerar esa garantía?",
    ops=[
        "No, porque las dos actuaciones recaen sobre los mismos hechos y contra los mismos sujetos, lo que configura un doble juzgamiento prohibido.",
        "Sí: son responsabilidades de naturaleza distinta, con finalidades y efectos diferentes, y pueden concurrir.",
        "No, porque la Contraloría desplaza a la Procuraduría cuando el hecho compromete el patrimonio público.",
    ],
    correcta=1,
    expl=[
        "El non bis in idem opera dentro de una misma naturaleza de responsabilidad, no entre responsabilidades distintas.",
        "Correcto: la fiscal busca resarcir el detrimento patrimonial y la disciplinaria juzga el incumplimiento del deber funcional; son autónomas.",
        "No existe desplazamiento entre órganos de control de distinta naturaleza; cada uno conserva su competencia.",
    ],
),

]
