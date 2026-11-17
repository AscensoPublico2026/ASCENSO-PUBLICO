# -*- coding: utf-8 -*-
"""Eje 1: Estructura y funciones de la PGN.

Estilo del banco: el caso ocupa un párrafo con datos concretos, algunos
irrelevantes a propósito. Las cuatro opciones son acciones defendibles, de
largo parecido y sin su propia justificación adentro: el porqué va en la
explicación, que es lo que el comprador lee al terminar.
"""

EST = "Estructura y funciones de la PGN"

BANCO = [
dict(
    tema="Quién integra el Ministerio Público", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="intermediate",
    ctx="En la inducción de los contratistas nuevos de una procuraduría regional, el expositor afirma que el Ministerio Público es la Procuraduría General de la Nación y que las personerías municipales son dependencias de las alcaldías. Un asistente le pregunta entonces a quién debe acudir un ciudadano de un municipio apartado que no tiene cómo desplazarse a la capital del departamento, y el expositor responde que no tiene otra alternativa que esperar la visita de la regional.",
    q="¿Qué precisión corresponde hacer sobre la composición del Ministerio Público?",
    ops=[
        "La Procuraduría ejerce el Ministerio Público junto con la Contraloría General de la República y las contralorías territoriales.",
        "La Procuraduría, la Defensoría del Pueblo y las personerías distritales y municipales integran el Ministerio Público.",
        "La Procuraduría ejerce el Ministerio Público y la Defensoría y las personerías son entidades de apoyo sin esa condición.",
    ],
    correcta=1,
    expl=[
        "El control fiscal es una función distinta y las contralorías conforman una rama de control separada; no integran el Ministerio Público.",
        "Correcto: el artículo 118 de la Constitución lo integra con esas tres entidades, y por eso el ciudadano del caso puede acudir a la personería de su propio municipio.",
        "Es el error del expositor: deja al ciudadano sin la puerta de entrada más cercana, que es justamente la personería municipal.",
    ],
),

dict(
    tema="Elección del Procurador General", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="intermediate",
    ctx="Una periodista prepara una nota sobre el próximo relevo en la Procuraduría y le pide a usted, que trabaja en la entidad, que le confirme el procedimiento. En su borrador escribió que el Presidente designa al Procurador de una lista que le envía la Corte Constitucional, para un período de cinco años prorrogable. Quiere publicar esa misma tarde.",
    q="¿Cuál es el procedimiento que establece el artículo 276 de la Constitución?",
    ops=[
        "Lo elige el Senado para un período de cuatro años, de terna del Presidente, la Corte Suprema y el Consejo de Estado.",
        "Lo elige el Congreso en pleno para un período de cuatro años, por mayoría calificada y sin terna previa.",
        "Lo designa el Presidente de la República para un período de cuatro años, en ejercicio de la facultad nominadora que le reconoce la Constitución.",
    ],
    correcta=0,
    expl=[
        "Correcto: Senado, cuatro años y terna integrada por el Presidente, la Corte Suprema de Justicia y el Consejo de Estado.",
        "La elección corresponde al Senado y no al Congreso en pleno, y sí existe terna previa de tres postulantes.",
        "La designación directa por el Ejecutivo comprometería la independencia del órgano de control frente a los sujetos que vigila.",
    ],
),

dict(
    tema="Las tres funciones misionales de la PGN", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="intermediate",
    ctx="La secretaría de educación de un municipio advierte que el operador del programa de alimentación escolar viene entregando raciones por debajo del gramaje contratado en tres instituciones rurales. Todavía no hay queja de ningún padre de familia, el contrato está vigente y faltan cuatro meses para su terminación. La secretaría pide acompañamiento a la procuraduría provincial.",
    q="¿A cuál de las funciones misionales de la Procuraduría corresponde atender esa solicitud?",
    ops=[
        "A la función de intervención, que se ejerce ante autoridades judiciales y administrativas dentro de procesos en curso.",
        "A la función disciplinaria, que se activa frente a conductas ya ocurridas y presuntamente constitutivas de falta.",
        "A la función preventiva y de control de gestión, orientada a evitar que la irregularidad se consolide o se repita.",
    ],
    correcta=2,
    expl=[
        "La intervención supone un proceso ya iniciado en el que el Ministerio Público actúa como sujeto procesal; aquí no lo hay.",
        "La función disciplinaria puede activarse después, pero lo que la secretaría pide es que el daño no termine de producirse.",
        "Correcto: quedan cuatro meses de ejecución y la advertencia oportuna puede corregir el gramaje antes de que el perjuicio se consume.",
    ],
),

dict(
    tema="Poder disciplinario preferente", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="advanced",
    ctx="La oficina de control interno disciplinario de una alcaldía adelanta desde hace cinco meses una investigación contra el secretario de infraestructura por el colapso de una obra. Ya practicó ocho testimonios y tiene el expediente en etapa de pruebas. La Procuraduría comunica que asume el conocimiento del asunto en ejercicio del poder preferente.",
    q="¿Qué efecto produce esa comunicación sobre la actuación de la alcaldía?",
    ops=[
        "La oficina conserva la competencia y la Procuraduría pasa a ejercer vigilancia sobre su trámite mediante informes periódicos.",
        "La oficina queda desplazada, remite el expediente a la Procuraduría y se abstiene de continuar conociendo el asunto.",
        "Lo actuado por la oficina queda sin efectos y la investigación debe rehacerse íntegramente ante la Procuraduría.",
    ],
    correcta=1,
    expl=[
        "El poder preferente no se agota en pedir informes: implica asumir el conocimiento del asunto y decidirlo.",
        "Correcto: la competencia se desplaza y lo actuado válidamente se remite, de modo que los ocho testimonios no se pierden.",
        "Las pruebas practicadas con las formalidades legales conservan su validez; repetirlas sería un desgaste innecesario.",
    ],
),

dict(
    tema="Vigilancia sobre funcionarios de elección popular", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="advanced",
    ctx="En una capacitación sobre control disciplinario, el alcalde de un municipio sostiene que la Procuraduría carece de competencia sobre él porque fue elegido por voto popular y solo responde ante sus electores. Agrega que cualquier actuación en su contra tendría que pasar antes por autorización del Consejo de Estado.",
    q="¿Cuál es la respuesta técnicamente correcta?",
    ops=[
        "La Procuraduría puede vigilarlo únicamente cuando la conducta investigada constituya además una conducta punible.",
        "La Procuraduría carece de competencia sobre los servidores de elección popular, que responden políticamente ante la ciudadanía que los eligió.",
        "La Procuraduría ejerce vigilancia superior de la conducta de quienes desempeñan funciones públicas, incluidos los de elección popular.",
    ],
    correcta=2,
    expl=[
        "La falta disciplinaria es autónoma frente al delito y no depende de que la conducta tenga relevancia penal.",
        "El numeral 6 del artículo 277 de la Constitución no excluye a los servidores de elección popular de esa vigilancia.",
        "Correcto: la Constitución los menciona de manera expresa. Discusión distinta es el régimen de garantías y de control judicial aplicable a las sanciones que se les imponen.",
    ],
),

dict(
    tema="Funciones que el Procurador ejerce directamente", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="advanced",
    ctx="En su despacho se discute si una actuación puede delegarse en un procurador delegado o si corresponde al Procurador General ejercerla personalmente. El asunto involucra a un funcionario que, según el expediente, desconoció de manera manifiesta una norma constitucional al adjudicar un contrato, y hay presión mediática para resolver en la semana.",
    q="Según el artículo 278 de la Constitución, ¿cuál de estas funciones ejerce directamente el Procurador General?",
    ops=[
        "Adelantar las indagaciones previas que se abran contra funcionarios del nivel directivo en todo el país.",
        "Desvincular del cargo al funcionario que infrinja manifiestamente la Constitución o la ley, previa audiencia y decisión motivada.",
        "Representar judicialmente a la Nación en los procesos contractuales en los que se discuta la validez de una adjudicación celebrada por una entidad.",
    ],
    correcta=1,
    expl=[
        "Las indagaciones previas las adelantan los despachos competentes según el reparto, no el Procurador en persona.",
        "Correcto: es una de las funciones que el artículo 278 le reserva, y la audiencia previa y la motivación son requisitos de su ejercicio, por más presión que haya.",
        "La representación judicial de la Nación corresponde a las entidades y a la Agencia Nacional de Defensa Jurídica del Estado.",
    ],
),

dict(
    tema="Defensoría del Pueblo y dirección del Procurador", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="intermediate",
    ctx="Un ciudadano acude a una procuraduría provincial porque la Defensoría del Pueblo de su departamento no ha atendido su solicitud de representación judicial. Pregunta si la Procuraduría puede obligar a la Defensoría a atenderlo o si se trata de dos entidades sin ninguna relación entre sí.",
    q="¿Cuál es la relación que establece la Constitución entre las dos entidades?",
    ops=[
        "La Defensoría ejerce sus funciones de manera autónoma, bajo la suprema dirección del Procurador General de la Nación.",
        "La Defensoría del Pueblo es una dependencia interna de la Procuraduría y su titular es nombrado y removido libremente por el Procurador General.",
        "Son entidades sin relación jerárquica alguna, cada una adscrita a una rama distinta del poder público.",
    ],
    correcta=0,
    expl=[
        "Correcto: el artículo 281 señala que el Defensor ejerce sus funciones bajo la suprema dirección del Procurador General.",
        "La Defensoría no es una dependencia de la Procuraduría y el Defensor del Pueblo es elegido por la Cámara de Representantes.",
        "Ambas integran el Ministerio Público, de modo que sí existe una relación, y ninguna pertenece a las tres ramas del poder.",
    ],
),

dict(
    tema="Competencia territorial de las procuradurías", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="intermediate",
    ctx="Llega una queja contra el tesorero de un municipio de nueve mil habitantes por presuntas irregularidades en el recaudo del impuesto predial durante la vigencia pasada. El municipio tiene personería y queda a dos horas de la capital del departamento. El quejoso pide que el caso lo lleve directamente una delegada en Bogotá.",
    q="En la estructura territorial de la Procuraduría, ¿qué dependencia conoce en principio de ese tipo de asuntos?",
    ops=[
        "La personería municipal, que ejerce el Ministerio Público en el municipio y desplaza a la Procuraduría en estos casos.",
        "La procuraduría provincial, que ejerce sus funciones en el ámbito de los municipios de su circunscripción.",
        "La procuraduría delegada correspondiente, por tratarse de un asunto de manejo de recursos públicos territoriales.",
    ],
    correcta=1,
    expl=[
        "La personería ejerce el Ministerio Público en el municipio, pero no desplaza a la Procuraduría ni excluye su competencia.",
        "Correcto: las provinciales operan en el ámbito municipal dentro de su circunscripción y las regionales en el departamental.",
        "Las delegadas tienen competencias especializadas y de instancia; no son el primer destino de una queja municipal.",
    ],
),

dict(
    tema="Instituto de Estudios del Ministerio Público", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="basic",
    ctx="En la planeación institucional del próximo año se propone un programa de formación dirigido a personeros municipales recién posesionados, acompañado de una línea de investigación sobre el ejercicio del control disciplinario en municipios de sexta categoría. Se discute qué dependencia debe liderarlo.",
    q="¿Qué dependencia de la Procuraduría tiene esa vocación?",
    ops=[
        "La Procuraduría Auxiliar para Asuntos Disciplinarios, que apoya la unificación de criterios y la formación de los servidores en esa materia.",
        "La Secretaría General, de la cual dependen los asuntos administrativos y de talento humano de la entidad.",
        "El Instituto de Estudios del Ministerio Público, encargado de la capacitación, la investigación y la divulgación académica.",
    ],
    correcta=2,
    expl=[
        "La Procuraduría Auxiliar cumple funciones de apoyo y de conceptualización disciplinaria, no de formación académica.",
        "La Secretaría General administra la entidad, pero el encargo académico y de investigación no está en su cabeza.",
        "Correcto: el IEMP es el brazo académico y de formación del Ministerio Público, e incluye a los personeros entre sus destinatarios.",
    ],
),

dict(
    tema="Función de intervención", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="intermediate",
    ctx="En un proceso de nulidad y restablecimiento del derecho que cursa ante un juez administrativo, un agente del Ministerio Público solicita intervenir. La entidad demandada ya tiene apoderado y el demandante, que fue retirado del servicio, pregunta si el agente va a defenderlo a él o a la entidad.",
    q="¿Cuál es el fundamento y el alcance de esa intervención?",
    ops=[
        "Acompañar la posición del demandante, por ser el extremo débil de la relación procesal frente al Estado.",
        "Representar a la entidad demandada, de modo que el Estado comparezca al proceso con una sola defensa coordinada.",
        "Defender el orden jurídico, el patrimonio público y los derechos y garantías fundamentales en el proceso.",
    ],
    correcta=2,
    expl=[
        "El Ministerio Público no toma partido por una de las partes: su intervención es objetiva y puede favorecer a cualquiera.",
        "El agente no es apoderado de la entidad; esa representación corresponde a quien la entidad designe.",
        "Correcto: ese es el objeto de la función de intervención, y por eso su concepto puede coincidir o no con el de las partes.",
    ],
),

dict(
    tema="Informe anual al Congreso", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="basic",
    ctx="Le piden consolidar las cifras de su dependencia para el informe periódico que el Procurador General debe rendir por mandato constitucional. El plazo interno vence en dos semanas y el formato exige desagregar las actuaciones preventivas de las disciplinarias.",
    q="¿Ante quién rinde el Procurador General ese informe anual de gestión?",
    ops=[
        "Ante el Presidente de la República, como jefe de la administración pública.",
        "Ante la Corte Constitucional, que ejerce el control de las actuaciones del Ministerio Público.",
        "Ante el Congreso de la República, conforme al artículo 277 de la Constitución.",
    ],
    correcta=2,
    expl=[
        "El Procurador no es subordinado del Ejecutivo y rendirle cuentas comprometería la autonomía del órgano de control.",
        "La Corte Constitucional ejerce el control de constitucionalidad de las normas, no recibe el informe de gestión.",
        "Correcto: el deber de rendir anualmente informe de su gestión al Congreso está en el artículo 277.",
    ],
),

dict(
    tema="Alcance de la función preventiva", ref="PGN-EST",
    refT="Estructura y funciones de la PGN", nivel="advanced",
    ctx="Revisando el expediente contractual de una entidad, usted advierte que el estudio previo de un proceso que se adjudica en ocho días no justifica la necesidad del bien que se va a comprar y que el análisis del sector se limita a una cotización. No hay adjudicación, no hay contrato firmado y no se ha causado ningún perjuicio patrimonial.",
    q="¿Cuál es la actuación propia de la función preventiva en ese momento?",
    ops=[
        "Emitir una advertencia o requerimiento preventivo sobre el riesgo detectado, con constancia, antes de la adjudicación.",
        "Abrir investigación disciplinaria contra el ordenador del gasto por la falta que se configurará al momento de adjudicar con ese estudio previo.",
        "Guardar silencio hasta la firma del contrato, momento en el cual la conducta será susceptible de reproche.",
    ],
    correcta=0,
    expl=[
        "Correcto: ese es el sentido de lo preventivo, y los ocho días que faltan son justamente la ventana para que la entidad corrija.",
        "No puede investigarse disciplinariamente una falta que aún no se ha cometido; la conducta reprochable todavía no existe.",
        "Esperar a que el daño se produzca equivale a renunciar a la función preventiva, que es precisamente lo que se le encomienda.",
    ],
),

]
