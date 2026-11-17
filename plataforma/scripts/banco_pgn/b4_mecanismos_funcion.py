# -*- coding: utf-8 -*-
"""Ejes: Mecanismos de protección de derechos. Función pública y empleo público."""

MEC = "Mecanismos de protección de derechos"
FUN = "Función pública y empleo público"

BANCO = [
dict(
    tema="Tutela: subsidiariedad", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="advanced",
    ctx="Una ciudadana de sesenta y dos años acude a la procuraduría provincial. Un fondo le negó el reconocimiento pensional mediante acto administrativo notificado hace un mes. Ella recibe una pensión de su cónyuge, no alega carencia de recursos ni afectación de su salud, y quiere interponer tutela de inmediato.",
    q="¿Qué le orienta usted sobre la procedencia de la tutela?",
    ops=[
        "Que la tutela procede en todo caso cuando se discute un derecho pensional, por su conexidad con el mínimo vital de la persona.",
        "Que debe esperar a que termine el proceso ante la jurisdicción contenciosa y acudir a la tutela solo contra la sentencia.",
        "Que la tutela es subsidiaria y cede ante la acción de nulidad y restablecimiento del derecho, que es el medio idóneo.",
    ],
    correcta=2,
    expl=[
        "La conexidad con el mínimo vital debe acreditarse en cada caso, y aquí la ciudadana percibe otro ingreso.",
        "No hay que agotar el proceso: la tutela como mecanismo transitorio opera antes, si hay perjuicio irremediable.",
        "Correcto: procede cuando no existe otro medio idóneo, o como mecanismo transitorio ante un perjuicio irremediable que aquí no se alega.",
    ],
),

dict(
    tema="Tutela: término para fallar", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="basic",
    ctx="Su despacho recibe el traslado de una tutela instaurada contra una entidad territorial. El jefe pregunta de cuánto tiempo dispone el juez para resolverla, porque quiere programar el concepto del Ministerio Público sin que llegue tarde al expediente.",
    q="¿Cuál es el término de la acción de tutela?",
    ops=[
        "Diez días siguientes a la solicitud, término dentro del cual el juez debe practicar pruebas y resolver sobre el amparo.",
        "Treinta días hábiles contados a partir del auto que admite la solicitud de amparo presentada por el accionante.",
        "Tres meses, término dentro del cual el juez debe practicar las pruebas y resolver sobre el amparo solicitado.",
    ],
    correcta=0,
    expl=[
        "Correcto: el artículo 86 de la Constitución fija un término máximo de diez días, lo que explica la urgencia del concepto.",
        "Ese término no corresponde a la tutela, cuyo trámite es preferente y sumario por mandato constitucional.",
        "Tres meses desconoce por completo la naturaleza preferente y sumaria que la Constitución le imprime a la acción.",
    ],
),

dict(
    tema="Acción popular", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="intermediate",
    ctx="Una comunidad denuncia que el vertimiento de una planta de beneficio está contaminando la quebrada que abastece el acueducto veredal. Nadie ha enfermado todavía, no hay perjuicio patrimonial cuantificado y lo que la comunidad pide es que el vertimiento cese y se recupere la fuente hídrica.",
    q="¿Cuál es el mecanismo judicial idóneo?",
    ops=[
        "La acción de grupo, que permite reclamar la indemnización de los perjuicios sufridos por los habitantes de la vereda.",
        "La acción popular, que permite ordenar que cese el vertimiento y que se recupere la fuente hídrica afectada.",
        "La acción de tutela, por tratarse de la amenaza de un derecho fundamental de los miembros de la comunidad afectada.",
    ],
    correcta=1,
    expl=[
        "La acción de grupo busca la reparación de un daño ya causado, y aquí lo que se pide es que cese la amenaza.",
        "Correcto: protege derechos e intereses colectivos como el ambiente sano, y permite ordenar que cese la vulneración.",
        "La tutela protege derechos fundamentales individuales; el interés en juego aquí es de naturaleza colectiva.",
    ],
),

dict(
    tema="Acción de grupo", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="intermediate",
    ctx="Cincuenta familias sufrieron daños en sus viviendas por el rompimiento de una tubería de un acueducto municipal. Todas resultaron afectadas por la misma causa, en el mismo evento, y cada una cuantificó sus perjuicios con avalúos independientes. Buscan que el municipio las indemnice.",
    q="¿Qué acción corresponde?",
    ops=[
        "La acción popular, dado que el número de familias afectadas convierte el asunto en un interés de naturaleza colectiva.",
        "La acción de grupo, que permite reclamar la indemnización de los perjuicios derivados de una misma causa común.",
        "La acción de cumplimiento, para que se ordene al municipio ejecutar las obras de mantenimiento que tenía pendientes.",
    ],
    correcta=1,
    expl=[
        "La acción popular previene o hace cesar la vulneración de un derecho colectivo, pero no indemniza daños individuales.",
        "Correcto: un número plural de personas, una causa común y una pretensión indemnizatoria identifican la acción de grupo.",
        "La acción de cumplimiento no tiene finalidad indemnizatoria y exige el incumplimiento de una norma o acto concreto.",
    ],
),

dict(
    tema="Habeas corpus", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="basic",
    ctx="Una persona lleva cuarenta y ocho horas retenida en una estación sin haber sido puesta a disposición de autoridad judicial. Su familia acude a la personería municipal, que a su vez consulta a la procuraduría provincial sobre el mecanismo que debe invocarse de inmediato.",
    q="¿Qué mecanismo procede?",
    ops=[
        "La acción de tutela, por tratarse de la vulneración del derecho fundamental a la libertad personal del retenido.",
        "El habeas corpus, que debe resolverse en treinta y seis horas por cualquier juez ante quien se presente la solicitud.",
        "El derecho de petición dirigido a la autoridad que practicó la retención, para que informe su fundamento legal.",
    ],
    correcta=1,
    expl=[
        "Para la libertad personal el ordenamiento prevé un mecanismo específico y más expedito que la tutela.",
        "Correcto: el artículo 30 de la Constitución lo prevé para la privación ilegal de la libertad y debe resolverse en treinta y seis horas.",
        "El derecho de petición no es el mecanismo para recuperar la libertad de una persona retenida ilegalmente.",
    ],
),

dict(
    tema="Habeas data", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="intermediate",
    ctx="Un ciudadano descubre que en una base de datos de una entidad pública figura una anotación que lo reporta como sancionado, cuando la sanción fue revocada hace tres años. Pide que se corrija el registro y que se informe la corrección a quienes consultaron el dato.",
    q="¿Qué derecho está ejerciendo?",
    ops=[
        "El derecho a la intimidad, que impide la circulación de información personal sin autorización previa del titular.",
        "El habeas data: conocer, actualizar y rectificar las informaciones recogidas sobre él en bancos de datos.",
        "El derecho de acceso a los documentos públicos, que le permite consultar la información que produce la entidad.",
    ],
    correcta=1,
    expl=[
        "La intimidad es un derecho conexo, pero no comprende por sí misma la facultad de rectificar un dato erróneo.",
        "Correcto: es el contenido del artículo 15 de la Constitución e incluye la corrección del registro inexacto.",
        "El acceso a documentos públicos se refiere a la información de la entidad, no a los datos propios del solicitante.",
    ],
),

dict(
    tema="Acción de cumplimiento: objeto", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="intermediate",
    ctx="Una ley ordenó a las entidades territoriales expedir un reglamento dentro de los seis meses siguientes a su vigencia. Han pasado dos años y una alcaldía no lo ha expedido. Un ciudadano quiere forzar a la administración a cumplir ese mandato y ya le reclamó por escrito sin obtener respuesta.",
    q="¿Qué acción procede?",
    ops=[
        "La acción de cumplimiento, dirigida a que la alcaldía expida el acto que la ley le ordenó dentro de un plazo concreto.",
        "La acción de tutela, por la omisión de la autoridad y la afectación que esa inactividad produce en los habitantes.",
        "La acción de repetición, dirigida contra el alcalde que omitió expedir el reglamento dentro del plazo señalado.",
    ],
    correcta=0,
    expl=[
        "Correcto: su objeto es hacer efectivo el cumplimiento de una norma con fuerza material de ley o de un acto administrativo.",
        "La tutela protege derechos fundamentales, no el cumplimiento de normas consideradas en abstracto.",
        "La repetición se dirige contra el servidor que con su conducta causó una condena patrimonial al Estado.",
    ],
),

dict(
    tema="Acción de cumplimiento: requisito de renuencia", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="advanced",
    ctx="Un ciudadano quiere radicar hoy mismo una acción de cumplimiento contra una alcaldía que no expidió un acto que una ley le ordenaba. El plazo de la ley venció hace ocho meses. El ciudadano no ha dirigido ninguna solicitud previa a la alcaldía y considera que el vencimiento del plazo es prueba suficiente.",
    q="¿Qué le orienta hacer primero?",
    ops=[
        "Radicar de una vez la acción, porque el vencimiento del plazo legal acredita por sí mismo el incumplimiento de la autoridad.",
        "Reclamar primero por escrito a la alcaldía el cumplimiento del deber legal, y acudir al juez ante la renuencia.",
        "Presentar una acción popular, dado que la expedición del reglamento beneficiaría a toda la comunidad del municipio.",
    ],
    correcta=1,
    expl=[
        "El vencimiento del plazo no reemplaza la constitución en renuencia, que es un requisito de procedibilidad de la acción.",
        "Correcto: la Ley 393 de 1997 exige reclamar antes a la autoridad; si se ratifica o no responde en diez días, queda habilitada la vía judicial.",
        "La acción popular protege derechos e intereses colectivos; aquí lo que se busca es el cumplimiento de un deber legal concreto.",
    ],
),

dict(
    tema="Derecho de petición: términos", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="intermediate",
    ctx="Llega a la ventanilla una petición en la que un ciudadano solicita copia de cuatro actas del comité de contratación de la entidad. No pide concepto ni interpretación de normas: solo las copias. El funcionario de turno pregunta si debe contarle quince o treinta días.",
    q="¿Cuál es el término general para responder una petición de documentos e información?",
    ops=[
        "Quince días hábiles, que es el término general aplicable a las peticiones en interés particular o general.",
        "Diez días hábiles siguientes a su recepción, que es el término que el CPACA fija para la entrega de documentos.",
        "Treinta días hábiles, por tratarse de información que debe recopilarse en varias dependencias de la entidad.",
    ],
    correcta=1,
    expl=[
        "Quince días hábiles corresponde a las peticiones en interés particular o general, que es una categoría distinta.",
        "Correcto: el CPACA fija diez días hábiles para las peticiones de documentos e información como la del caso.",
        "Treinta días hábiles corresponde a las consultas sobre materias a cargo de la entidad, no a la entrega de copias.",
    ],
),

dict(
    tema="Petición: imposibilidad de responder a tiempo", ref="PGN-MEC",
    refT="Mecanismos de protección de derechos", nivel="advanced",
    ctx="Faltan dos días para que venza el término de una petición que exige consolidar información de cinco dependencias. Tres ya respondieron; las otras dos avisaron que necesitan una semana más. El coordinador propone esperar a tener todo y responder cuando esté completo.",
    q="¿Cuál es la actuación correcta?",
    ops=[
        "Responder con la información de las tres dependencias que ya contestaron y archivar la petición como atendida.",
        "Informar al peticionario antes del vencimiento, explicando los motivos y señalando el plazo razonable.",
        "Esperar a tener la información completa y responder cuando se consolide, dejando constancia del motivo del retraso.",
    ],
    correcta=1,
    expl=[
        "Una respuesta parcial presentada como definitiva no satisface el derecho de petición, que exige respuesta de fondo.",
        "Correcto: el CPACA obliga a informar antes del vencimiento, con los motivos de la demora y el nuevo plazo en que se responderá.",
        "Dejar vencer el término sin informar vulnera el derecho de petición, por más que después se deje constancia.",
    ],
),

dict(
    tema="Mérito como principio de la función pública", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="basic",
    ctx="Queda en vacancia definitiva un empleo de carrera administrativa en una entidad. El jefe de talento humano propone nombrar al servidor con mayor antigüedad en la dependencia, que conoce bien el cargo y lleva once años en la entidad, para evitar el desgaste de un concurso.",
    q="¿Cuál es la regla general del artículo 125 de la Constitución?",
    ops=[
        "La promoción del servidor con mayor antigüedad y mejor evaluación del desempeño dentro de la misma dependencia.",
        "El concurso público de méritos, que es el mecanismo por el cual se proveen los empleos de carrera administrativa.",
        "La libre designación por parte del nominador, que responde por el acierto de la escogencia que realice.",
    ],
    correcta=1,
    expl=[
        "La antigüedad no sustituye el concurso ni confiere derecho preferente a ocupar el empleo en vacancia definitiva.",
        "Correcto: los empleos en los órganos y entidades del Estado son de carrera, salvo las excepciones constitucionales y legales.",
        "La libre designación corresponde a los empleos de libre nombramiento y remoción, que son la excepción.",
    ],
),

dict(
    tema="Encargo y provisionalidad", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="advanced",
    ctx="Una entidad debe proveer transitoriamente un empleo de carrera en vacancia definitiva mientras se surte el concurso. En la planta hay dos servidores de carrera del grado inmediatamente inferior que cumplen los requisitos y tienen evaluación sobresaliente. El jefe prefiere nombrar en provisionalidad a una persona externa de su confianza.",
    q="¿Cuál es el orden que impone el principio de mérito?",
    ops=[
        "Considerar primero el encargo de servidores de carrera que cumplan requisitos, y solo después la provisionalidad.",
        "Nombrar directamente en provisionalidad a la persona que el nominador considere más idónea para desempeñar el empleo.",
        "Celebrar un contrato de prestación de servicios mientras la Comisión Nacional del Servicio Civil surte el concurso.",
    ],
    correcta=0,
    expl=[
        "Correcto: el encargo tiene prelación sobre el nombramiento provisional y es un derecho de los servidores de carrera.",
        "Saltar al nombramiento provisional sin agotar el encargo desconoce los derechos de quienes están en carrera.",
        "Un contrato de prestación de servicios no puede usarse para desempeñar funciones permanentes de un empleo de planta.",
    ],
),

dict(
    tema="Inhabilidades e incompatibilidades", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="intermediate",
    ctx="Un aspirante va a ser nombrado en un empleo del nivel asesor. Al verificar antecedentes se advierte que fue sancionado disciplinariamente con destitución hace tres años, con inhabilidad general de doce años. El aspirante alega que ya cumplió la destitución y que el cargo al que aspira es de menor jerarquía que el anterior.",
    q="¿Qué procede?",
    ops=[
        "Nombrarlo en un empleo de menor jerarquía o sin manejo directo de recursos, para no afectar su derecho al trabajo.",
        "Abstenerse de nombrarlo mientras esté vigente la inhabilidad general de doce años impuesta en el fallo sancionatorio.",
        "Nombrarlo, dado que transcurrieron tres años desde la sanción y la destitución ya se hizo efectiva en su momento.",
    ],
    correcta=1,
    expl=[
        "La inhabilidad no se gradúa por la jerarquía del empleo ni admite condiciones que permitan eludirla.",
        "Correcto: la inhabilidad general corre por el término impuesto y le impide ejercer cargos públicos mientras esté vigente.",
        "La inhabilidad corre por el término del fallo, que es de doce años, y no por un plazo distinto.",
    ],
),

dict(
    tema="Declaración de bienes y rentas", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="basic",
    ctx="Una persona fue seleccionada en un concurso y alista los documentos para tomar posesión de un empleo del nivel técnico en una entidad. Pregunta si debe presentar declaración de bienes y rentas, dado que no va a manejar dinero ni a ordenar gastos.",
    q="¿Qué obligación tiene en esa materia?",
    ops=[
        "Presentarla únicamente al momento del retiro del servicio, para efectos del control patrimonial de la entidad.",
        "Presentarla antes de la posesión y actualizarla periódicamente mientras permanezca en el servicio.",
        "Ninguna, salvo que el empleo implique manejo de recursos públicos o facultad para ordenar el gasto de la entidad.",
    ],
    correcta=1,
    expl=[
        "También se exige al ingreso, no solo al retiro: la declaración inicial es la línea de base del control patrimonial.",
        "Correcto: se presenta antes de la posesión, se actualiza periódicamente y también al momento del retiro.",
        "La obligación no depende del manejo directo de recursos ni del nivel del empleo que se va a desempeñar.",
    ],
),

dict(
    tema="Evaluación del desempeño", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="intermediate",
    ctx="Un jefe califica a los once servidores de carrera de su dependencia con la nota máxima. No aplicó los instrumentos, no concertó compromisos al inicio del período y no documentó evidencias. Explica que todos trabajaron bien y que quería evitar conflictos en el equipo.",
    q="¿Cómo se valora esa conducta?",
    ops=[
        "Es una decisión discrecional del evaluador, que conoce el desempeño de su equipo mejor que cualquier instrumento.",
        "Es correcta si la dependencia cumplió las metas institucionales fijadas para el período que se está evaluando.",
        "Desnaturaliza la evaluación del desempeño y puede comprometer disciplinariamente al evaluador.",
    ],
    correcta=2,
    expl=[
        "La evaluación del desempeño no es discrecional: está reglada y exige instrumentos, concertación y evidencias.",
        "El cumplimiento de metas debe demostrarse mediante el instrumento de evaluación, no presumirse del resultado global.",
        "Correcto: la evaluación produce efectos en la permanencia y en los derechos de carrera, y debe sustentarse en evidencias.",
    ],
),

dict(
    tema="Situaciones administrativas", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="intermediate",
    ctx="Una servidora de carrera debe ausentarse ocho semanas por una incapacidad médica derivada de una cirugía programada. El jefe pregunta cómo debe registrarse esa ausencia y si puede descontarse del período de vacaciones pendiente para no afectar la planta.",
    q="¿Qué figura corresponde?",
    ops=[
        "Una comisión de servicios, que ampara la ausencia del servidor por causas ajenas a su voluntad durante el período.",
        "Una licencia por enfermedad, con los efectos laborales y prestacionales que la ley le atribuye.",
        "El descuento de las vacaciones pendientes, con el fin de no afectar la disponibilidad de la planta de personal.",
    ],
    correcta=1,
    expl=[
        "La comisión de servicios implica cumplir funciones propias del empleo fuera de la sede habitual de trabajo.",
        "Correcto: la incapacidad médica da lugar a una licencia, que es una situación administrativa reglada y distinta de las vacaciones.",
        "Las vacaciones tienen causa y finalidad distintas y no pueden usarse para cubrir una incapacidad médica.",
    ],
),

dict(
    tema="Retiro del servicio en carrera", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="advanced",
    ctx="Un servidor de carrera con nueve años en la entidad es desvinculado mediante un acto que invoca escuetamente la facultad discrecional del nominador y la necesidad del servicio. Su última evaluación fue satisfactoria, no tiene sanciones disciplinarias y el empleo no fue suprimido.",
    q="¿Qué objeción jurídica hay?",
    ops=[
        "El retiro es válido si la entidad reconoce y paga la indemnización que corresponde por la desvinculación del servidor.",
        "La objeción es de forma: bastaba con citar en el acto la norma que atribuye la facultad discrecional al nominador.",
        "Los servidores de carrera solo pueden retirarse por las causales legales, y el acto debe ser motivado.",
    ],
    correcta=2,
    expl=[
        "El pago de una indemnización no legaliza un retiro que carece de causal legal; la estabilidad no se compensa con dinero.",
        "No es un defecto meramente formal: lo que falta es la causal sustancial que habilite el retiro del servidor.",
        "Correcto: la estabilidad es la esencia de la carrera, y la discrecionalidad opera sobre los empleos de libre nombramiento y remoción.",
    ],
),

dict(
    tema="Deberes del servidor público", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="basic",
    ctx="Faltan cinco minutos para el cierre de la jornada y llega un usuario con un trámite que toma tres minutos y que el servidor puede resolver con la información que tiene a mano. El servidor le dice que vuelva mañana porque ya va a cerrar.",
    q="¿Qué deber está en juego?",
    ops=[
        "Ninguno: el horario de atención delimita la obligación del servidor y el usuario llegó sobre el cierre de la jornada.",
        "El deber de reserva, que obliga al servidor a no atender trámites fuera de las condiciones previstas en el procedimiento.",
        "El deber de cumplir con diligencia el servicio y atender a quienes acuden dentro del horario establecido.",
    ],
    correcta=2,
    expl=[
        "El horario organiza el servicio, pero no exime del deber de atender a quien llega dentro de él.",
        "El deber de reserva se refiere al manejo de la información que el servidor conoce por razón del cargo.",
        "Correcto: atender con diligencia a los usuarios dentro del horario es un deber funcional expreso del servidor público.",
    ],
),

dict(
    tema="Prohibición de participación en política", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="advanced",
    ctx="En plena campaña electoral, un servidor de una entidad pública publica en sus redes personales una invitación a votar por un candidato. Las fotografías fueron tomadas en su oficina, con el logo institucional visible al fondo, y las publicó un sábado fuera del horario laboral.",
    q="¿Cómo se valora la conducta?",
    ops=[
        "Está amparada por la libertad de expresión, que no admite restricciones por la condición de servidor público del autor.",
        "Compromete la prohibición de participar en política y el uso de bienes y espacios oficiales con fines proselitistas.",
        "Es válida por haberse publicado fuera del horario laboral y en un perfil personal que el servidor administra.",
    ],
    correcta=1,
    expl=[
        "La libertad de expresión del servidor tiene límites funcionales específicos previstos en la Constitución y la ley.",
        "Correcto: el ordenamiento restringe la participación política de ciertos servidores y prohíbe usar bienes oficiales con ese fin.",
        "Usar bienes y espacios oficiales con fines proselitistas no se legitima por el horario ni por el carácter del perfil.",
    ],
),

dict(
    tema="Capacitación y plan institucional", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="basic",
    ctx="Una entidad define su plan institucional de capacitación para la vigencia. La propuesta inicial repite íntegramente el plan del año anterior y concentra los cupos en el nivel directivo, sin que se haya levantado un diagnóstico de necesidades por dependencia.",
    q="¿Cuál es el criterio orientador?",
    ops=[
        "Responder a las necesidades del diagnóstico institucional y a las competencias requeridas en cada empleo.",
        "Concentrar la oferta en el nivel directivo, cuyas decisiones tienen mayor impacto sobre el funcionamiento de la entidad.",
        "Mantener la continuidad del plan del año anterior, que ya fue aprobado y ejecutado sin observaciones de control interno.",
    ],
    correcta=0,
    expl=[
        "Correcto: el plan debe construirse sobre un diagnóstico de necesidades y sobre las competencias que cada empleo exige.",
        "Restringir la capacitación al nivel directivo no responde al propósito institucional ni al derecho de los demás servidores.",
        "Repetir el plan desconoce el diagnóstico de la vigencia y convierte un instrumento de gestión en un trámite.",
    ],
),

dict(
    tema="Acoso laboral", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="advanced",
    ctx="Una servidora reporta que su jefe la descalifica públicamente en las reuniones de equipo desde hace cuatro meses y que le asigna tareas ajenas a su cargo después de cada desacuerdo. Hay tres correos que lo documentan y dos compañeros dispuestos a declarar lo que presenciaron.",
    q="¿Cuál es la ruta institucional?",
    ops=[
        "Sugerirle que converse directamente con su jefe y que, si la situación no mejora, considere solicitar un traslado.",
        "Trasladarla a otra dependencia de manera inmediata, para separarla del jefe y evitar que los hechos continúen.",
        "Activar el comité de convivencia laboral y, si los hechos lo ameritan, la vía disciplinaria contra el jefe señalado.",
    ],
    correcta=2,
    expl=[
        "Pedirle que lo resuelva sola la expone frente a quien ejerce la conducta y desconoce el deber institucional de actuar.",
        "Trasladar a quien reporta puede constituir una revictimización y, además, no corrige la conducta denunciada.",
        "Correcto: el comité de convivencia es la instancia preventiva, sin perjuicio de las medidas de protección frente a represalias.",
    ],
),

dict(
    tema="Trabajo en casa y deberes funcionales", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="intermediate",
    ctx="Un servidor autorizado para trabajar en casa no reporta avances desde hace dos semanas, no responde los canales institucionales durante la jornada y entregó con retraso los tres últimos productos. Sostiene que la modalidad le permite organizar su tiempo como mejor le convenga.",
    q="¿Qué debe entenderse?",
    ops=[
        "Que la modalidad cambia el lugar de la prestación, pero no los deberes funcionales ni la disponibilidad en la jornada.",
        "Que la flexibilidad propia de la modalidad releva al servidor del cumplimiento estricto del horario y de los reportes.",
        "Que procede la terminación inmediata del vínculo laboral por el incumplimiento reiterado de las obligaciones del cargo.",
    ],
    correcta=0,
    expl=[
        "Correcto: cambia el lugar de trabajo, no el contenido de los deberes, y su incumplimiento puede ser disciplinable.",
        "La flexibilidad no suprime la jornada ni el deber de reportar: la entidad puede exigir el cumplimiento fuera de la sede.",
        "La terminación inmediata del vínculo desconoce el debido proceso que ampara al servidor.",
    ],
),

dict(
    tema="Orden del superior contraria a la ley", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="advanced",
    ctx="Su jefe le ordena por escrito suscribir una certificación de cumplimiento sobre unas actividades que usted sabe que no se ejecutaron. El correo precisa que él asume la responsabilidad y que la certificación es necesaria para tramitar un pago que vence el viernes.",
    q="¿Qué debe hacer?",
    ops=[
        "Suscribir la certificación y guardar copia del correo del jefe, que acredita quién impartió la orden y con qué propósito.",
        "Abstenerse de suscribirla, manifestar por escrito las razones de su objeción y dejar constancia de lo ocurrido.",
        "Cumplir la orden amparado en la obediencia debida, que traslada la responsabilidad a quien la impartió por escrito.",
    ],
    correcta=1,
    expl=[
        "Firmar una certificación que no corresponde a la realidad consuma la falta, aunque después se exhiba quién la ordenó.",
        "Correcto: objetar motivadamente y dejar constancia es la conducta funcionalmente correcta frente a una orden ilegal.",
        "La obediencia debida no ampara la ejecución de una conducta manifiestamente ilegal ni traslada la responsabilidad.",
    ],
),

dict(
    tema="Nómina paralela", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="advanced",
    ctx="Una dependencia cubre desde hace cuatro años funciones permanentes de su planta mediante contratos de prestación de servicios sucesivos con las mismas seis personas. Cumplen horario, reciben instrucciones directas del coordinador y usan los equipos de la entidad. Los contratistas están conformes con el arreglo.",
    q="¿Cuál es el problema jurídico?",
    ops=[
        "El problema es exclusivamente presupuestal, y se corrige trasladando el gasto al rubro de servicios personales indirectos.",
        "No hay problema: el contrato de prestación de servicios es una forma válida de flexibilizar la planta de personal.",
        "Se desnaturaliza el contrato de prestación de servicios y se configura la figura conocida como nómina paralela.",
    ],
    correcta=2,
    expl=[
        "No es solo presupuestal: lo que se compromete es el régimen del empleo público y el principio de mérito.",
        "La flexibilización no puede lograrse desconociendo la estructura del empleo público ni la naturaleza del contrato.",
        "Correcto: esa figura está proscrita por la jurisprudencia y puede tener consecuencias disciplinarias y fiscales.",
    ],
),

dict(
    tema="Tratamiento de datos personales", ref="PGN-FUN",
    refT="Función pública y empleo público", nivel="intermediate",
    ctx="Para preparar un informe que debe entregar el lunes, un servidor descarga a su computador personal una base con nombre, cédula, dirección y diagnóstico de ochocientos ciudadanos atendidos por la entidad. El computador no tiene cifrado y es compartido con su familia.",
    q="¿Cómo se valora la conducta?",
    ops=[
        "Es aceptable mientras el servidor borre el archivo una vez elaborado y entregado el informe a la dependencia solicitante.",
        "Compromete los deberes de custodia y el régimen de protección de datos personales de los ciudadanos atendidos.",
        "Solo sería irregular si la información llegara efectivamente a filtrarse o a ser consultada por un tercero ajeno.",
    ],
    correcta=1,
    expl=[
        "El borrado posterior no elimina el riesgo ya creado durante el tiempo en que el archivo estuvo fuera de control.",
        "Correcto: la información sensible debe tratarse en los sistemas institucionales y con las medidas de seguridad previstas.",
        "La infracción está en el tratamiento inseguro de los datos, no en que el daño llegue a materializarse.",
    ],
),

]
