# -*- coding: utf-8 -*-
"""Normatividad educativa y convivencia escolar. Tres opciones."""

NOR = "Normatividad educativa"
CON = "Convivencia escolar"

BANCO = [
dict(
    tema="Ley General de Educación", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="basic",
    ctx="En una jornada pedagógica se discute cuál es la norma que organiza el servicio público educativo en Colombia, define sus fines y establece la estructura del servicio por niveles y ciclos. Tres docentes proponen normas distintas.",
    q="¿Cuál es esa norma?",
    ops=[
        "La Ley 1620 de 2013, que organiza el servicio educativo y define los fines de la educación en el país.",
        "La Ley 115 de 1994.",
        "El Decreto 1278 de 2002, que recoge la organización del servicio educativo y el régimen de los docentes.",
    ],
    correcta=1,
    expl=[
        "La Ley 1620 crea el sistema nacional de convivencia escolar, que es una materia distinta.",
        "Correcto: la Ley 115 de 1994 es la Ley General de Educación.",
        "El Decreto 1278 es el estatuto de profesionalización docente, no la norma que organiza el servicio.",
    ],
),

dict(
    tema="Estatuto de profesionalización docente", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="intermediate",
    ctx="Un docente que ingresó por concurso de méritos en 2019 pregunta cuál es el estatuto que rige su carrera. Un compañero con treinta años de servicio le dice que a ambos los rige la misma norma y que el escalafón es idéntico.",
    q="¿Cuál es el estatuto aplicable al docente que ingresó en 2019?",
    ops=[
        "El Decreto 2277 de 1979, que rige a quienes se vincularon al servicio educativo oficial por concurso.",
        "La Ley 115 de 1994, que establece el régimen de carrera aplicable a todos los docentes oficiales del país.",
        "El Decreto 1278 de 2002, que rige a quienes se vinculan a partir de su entrada en vigencia.",
    ],
    correcta=2,
    expl=[
        "El Decreto 2277 rige a los docentes vinculados antes de la vigencia del nuevo estatuto, como el compañero.",
        "La Ley 115 organiza el servicio educativo; el régimen de carrera docente está en los estatutos específicos.",
        "Correcto: quien ingresa por concurso bajo el nuevo régimen queda sujeto al Decreto 1278.",
    ],
),

dict(
    tema="Período de prueba", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="advanced",
    ctx="Una docente gana el concurso y es nombrada en período de prueba en una institución rural. Lleva seis meses, su desempeño ha sido bueno y pregunta qué ocurre cuando ese período termine y si queda automáticamente en carrera.",
    q="¿Qué ocurre al final del período de prueba?",
    ops=[
        "Queda inscrita automáticamente en el escalafón docente una vez cumplido el tiempo mínimo del período.",
        "Se le practica evaluación de desempeño y de competencias; si la supera, queda inscrita en el escalafón.",
        "Debe presentar nuevamente el concurso de méritos para acceder a la inscripción definitiva en el escalafón.",
    ],
    correcta=1,
    expl=[
        "La inscripción no es automática: depende del resultado de la evaluación que cierra el período de prueba.",
        "Correcto: la evaluación condiciona la inscripción en el escalafón docente al término del período de prueba.",
        "No hay que repetir el concurso: el período de prueba es una etapa posterior a haberlo superado.",
    ],
),

dict(
    tema="Proyecto Educativo Institucional", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="intermediate",
    ctx="Una institución revisa el documento que define sus principios, su horizonte institucional, su plan de estudios, su manual de convivencia y su sistema de evaluación. Un docente nuevo pregunta cómo se llama ese documento.",
    q="¿De qué documento se trata?",
    ops=[
        "Del Proyecto Educativo Institucional, que cada establecimiento debe elaborar y poner en práctica.",
        "Del plan de mejoramiento institucional, que recoge las metas y las acciones acordadas para cada vigencia.",
        "Del sistema institucional de evaluación, que articula los criterios y procedimientos de todo el establecimiento.",
    ],
    correcta=0,
    expl=[
        "Correcto: el PEI articula todos esos componentes, conforme a lo que establece la Ley 115.",
        "El plan de mejoramiento se deriva del PEI y recoge acciones concretas, pero no lo reemplaza.",
        "El SIEE es uno de los componentes del PEI, no el documento que agrupa a todos los demás.",
    ],
),

dict(
    tema="Gobierno escolar", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="intermediate",
    ctx="Se va a conformar la instancia superior de participación de la comunidad educativa en la orientación académica y administrativa del establecimiento. Participan representantes de docentes, padres, estudiantes, egresados y sector productivo.",
    q="¿Cuál es esa instancia?",
    ops=[
        "El consejo académico, que orienta el currículo y la organización pedagógica del establecimiento educativo.",
        "El comité escolar de convivencia, que atiende el clima escolar y los derechos de la comunidad educativa.",
        "El consejo directivo, que reúne a los representantes de todos los estamentos de la comunidad educativa.",
    ],
    correcta=2,
    expl=[
        "El consejo académico orienta lo pedagógico y curricular, y lo integran únicamente docentes y directivos.",
        "El comité de convivencia atiende el clima escolar, que es una competencia distinta de la orientación general.",
        "Correcto: el consejo directivo es la instancia de participación y de orientación académica y administrativa.",
    ],
),

dict(
    tema="Personero de los estudiantes", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="basic",
    ctx="Un estudiante de undécimo quiere participar formalmente en la vida institucional y promover el respeto de los derechos de sus compañeros. Pregunta qué figura del gobierno escolar le permite hacerlo y quién la elige.",
    q="¿Qué figura le corresponde?",
    ops=[
        "El contralor municipal, que ejerce el control sobre los recursos que administra la institución educativa.",
        "El personero de los estudiantes, encargado de promover el ejercicio de sus derechos y deberes.",
        "El representante de los docentes, que lleva al consejo directivo las inquietudes de la comunidad educativa.",
    ],
    correcta=1,
    expl=[
        "El contralor municipal no hace parte del gobierno escolar de las instituciones educativas.",
        "Correcto: el personero estudiantil es elegido por los estudiantes y promueve sus derechos y deberes.",
        "El representante de los docentes es elegido por ellos y no corresponde a un estudiante de undécimo.",
    ],
),

dict(
    tema="Límites del manual de convivencia", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="advanced",
    ctx="Un colegio incluye en su manual de convivencia una norma que prohíbe renovar la matrícula a las estudiantes en estado de embarazo. El manual fue aprobado por el consejo directivo y las familias lo firman al matricular.",
    q="¿Es válida esa disposición?",
    ops=[
        "Sí, porque el manual fue aprobado por el consejo directivo y las familias lo aceptan al firmar la matrícula.",
        "Sí, siempre que en el municipio exista otra institución educativa oficial que pueda recibir a la estudiante.",
        "No: el manual no puede contener disposiciones contrarias a la Constitución ni de carácter discriminatorio.",
    ],
    correcta=2,
    expl=[
        "La firma de los padres no convalida una cláusula que desconoce derechos fundamentales de la estudiante.",
        "La existencia de otra institución no justifica excluir a una estudiante del establecimiento donde estudia.",
        "Correcto: excluir por embarazo vulnera el derecho a la educación y a la igualdad, como lo ha señalado la Corte.",
    ],
),

dict(
    tema="Interés superior del niño", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="intermediate",
    ctx="Al resolver un caso que involucra a un estudiante de trece años, el comité debate entre aplicar estrictamente el manual de convivencia, atender lo que piden los padres o considerar lo que más conviene al desarrollo del estudiante.",
    q="¿Cuál es el principio rector según la Ley 1098 de 2006?",
    ops=[
        "La autonomía institucional, que faculta al establecimiento para aplicar su manual de convivencia aprobado.",
        "El interés superior del niño, la niña o el adolescente, con prevalencia de sus derechos sobre los demás.",
        "La voluntad de los padres de familia, que ejercen la representación legal del estudiante menor de edad.",
    ],
    correcta=1,
    expl=[
        "La autonomía institucional cede frente a los derechos prevalentes del menor de edad.",
        "Correcto: el interés superior y la prevalencia de derechos son el eje del Código de Infancia y Adolescencia.",
        "La voluntad de los padres no puede imponerse cuando contraría el interés superior del adolescente.",
    ],
),

dict(
    tema="Corresponsabilidad", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="advanced",
    ctx="Un docente advierte señales de descuido grave en un estudiante de primero: llega sin desayunar, con la misma ropa toda la semana y con marcas que no sabe explicar. Un compañero le dice que eso es asunto exclusivo de la familia.",
    q="¿Qué establece el principio de corresponsabilidad?",
    ops=[
        "Que la familia, la sociedad y el Estado son corresponsables del cuidado y la protección de los menores.",
        "Que la protección del menor de edad corresponde de manera exclusiva a la familia y a sus acudientes.",
        "Que la responsabilidad recae únicamente en el Instituto Colombiano de Bienestar Familiar y sus defensorías.",
    ],
    correcta=0,
    expl=[
        "Correcto: la corresponsabilidad obliga a la escuela a activar la ruta, no a mirar hacia otro lado.",
        "La familia es responsable, pero no de manera exclusiva, y eso es precisamente lo que define el principio.",
        "El ICBF es una de las entidades del sistema de protección, no la única responsable de activarlo.",
    ],
),

dict(
    tema="Plan Individual de Ajustes Razonables", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="advanced",
    ctx="Llega a tercer grado un estudiante con discapacidad. Debe documentarse qué apoyos necesita, qué ajustes se harán en la evaluación y cómo se implementarán durante el año, con la participación de la familia y del docente.",
    q="¿Qué instrumento corresponde?",
    ops=[
        "El observador del estudiante, donde se registra el seguimiento de su proceso durante el año escolar.",
        "El sistema institucional de evaluación, que define los criterios aplicables a todos los estudiantes del plantel.",
        "El Plan Individual de Ajustes Razonables, que recoge la valoración pedagógica y los apoyos requeridos.",
    ],
    correcta=2,
    expl=[
        "El observador registra el seguimiento de convivencia y de proceso, no la planeación de los apoyos.",
        "El SIEE regula la evaluación de todo el establecimiento y no sustituye la planeación individual de apoyos.",
        "Correcto: el PIAR es el instrumento previsto para documentar y planear los ajustes razonables.",
    ],
),

dict(
    tema="Gratuidad educativa", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="intermediate",
    ctx="Una familia manifiesta que no puede matricular a su hija en la institución oficial porque le exigen pagar un valor por concepto de derechos académicos. La estudiante cursará séptimo grado y la familia no tiene cómo pagarlo.",
    q="¿Qué debe tenerse en cuenta?",
    ops=[
        "El cobro procede únicamente en los grados de educación media, no en los de la básica secundaria.",
        "El cobro es legítimo cuando el consejo de padres lo aprueba para atender necesidades de la institución.",
        "La educación en los establecimientos oficiales es gratuita y la matrícula no puede condicionarse a ese pago.",
    ],
    correcta=2,
    expl=[
        "La gratuidad no se limita a un nivel determinado dentro de la educación preescolar, básica y media oficial.",
        "El consejo de padres no puede crear cobros contrarios a la ley ni condicionar el acceso al servicio.",
        "Correcto: condicionar la matrícula a un pago no exigible vulnera el derecho fundamental a la educación.",
    ],
),

dict(
    tema="Asignación académica", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="intermediate",
    ctx="Un docente pregunta quién define su asignación académica para el año siguiente. Él prefiere continuar con los grupos de décimo y undécimo, pero la institución necesita cubrir las horas de sexto por el retiro de una colega.",
    q="¿A quién corresponde definirla?",
    ops=[
        "Al rector, atendiendo las necesidades del servicio y el perfil profesional de cada uno de los docentes.",
        "Al propio docente, que conoce mejor que nadie los grados en los que su desempeño resulta más efectivo.",
        "Al consejo de padres, que representa los intereses de las familias en la organización académica del plantel.",
    ],
    correcta=0,
    expl=[
        "Correcto: la distribución de la asignación académica es una función que corresponde al rector.",
        "La preferencia del docente se escucha y se valora, pero no es ella la que decide la asignación.",
        "El consejo de padres no tiene competencia para definir la asignación académica de los docentes.",
    ],
),

dict(
    tema="Evaluación de desempeño docente", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="intermediate",
    ctx="Un docente regido por el estatuto de profesionalización pregunta con qué periodicidad se evalúa su desempeño, ya que solo recuerda la evaluación que le practicaron al terminar el período de prueba hace cuatro años.",
    q="¿Cuál es la regla?",
    ops=[
        "Una sola vez, al terminar el período de prueba, que es cuando se define su inscripción en el escalafón.",
        "De manera anual, además de la del período de prueba y de las evaluaciones de competencias para ascenso.",
        "Cada cinco años, coincidiendo con los ciclos de evaluación institucional que adelanta la secretaría.",
    ],
    correcta=1,
    expl=[
        "La evaluación del período de prueba no es la única que contempla el estatuto para el docente en carrera.",
        "Correcto: el estatuto prevé evaluación anual de desempeño además de las otras modalidades existentes.",
        "No es quinquenal ni está atada a los ciclos de evaluación institucional de la secretaría de educación.",
    ],
),

dict(
    tema="Reserva de la información del estudiante", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="advanced",
    ctx="Una madre pide al docente que le muestre el observador de otro estudiante, porque cree que ese compañero agredió a su hijo. Insiste en que tiene derecho a saber qué antecedentes tiene quien lastimó a su hijo. El caso ya fue puesto en conocimiento del comité de convivencia y los dos estudiantes están en el mismo curso desde el año pasado.",
    q="¿Qué corresponde?",
    ops=[
        "Entregarle una copia parcial del observador, limitada a los registros relacionados con agresiones anteriores.",
        "Mostrárselo si el rector lo autoriza, dado que la madre tiene un interés legítimo en conocer esa información.",
        "No entregar información del expediente de otro menor y canalizar el caso por el comité de convivencia.",
    ],
    correcta=2,
    expl=[
        "Una copia parcial sigue siendo entrega de información personal de un menor de edad a un tercero.",
        "Una autorización del rector no levanta la protección que ampara los datos de otro estudiante.",
        "Correcto: el caso se atiende por la ruta institucional, que informará a cada familia lo que le concierne.",
    ],
),

dict(
    tema="Debido proceso del estudiante", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="advanced",
    ctx="Un colegio cancela la matrícula de un estudiante el mismo día en que ocurre una falta grave tipificada en el manual de convivencia. No se le escuchó, no presentó descargos y la decisión se comunicó por teléfono a su acudiente.",
    q="¿Qué garantía se desconoció?",
    ops=[
        "Únicamente el derecho de petición, pues la decisión no fue comunicada por escrito al acudiente del estudiante.",
        "El debido proceso: derecho a ser escuchado, a presentar descargos, a decisión motivada y a impugnarla.",
        "Ninguna, dado que la falta está expresamente tipificada en el manual de convivencia del establecimiento.",
    ],
    correcta=1,
    expl=[
        "El derecho de petición no es lo que está en juego: lo vulnerado es el procedimiento que debía seguirse.",
        "Correcto: el debido proceso del artículo 29 se aplica también a las sanciones de carácter escolar.",
        "Que la falta esté tipificada no exime de seguir el procedimiento antes de imponer una sanción.",
    ],
),

dict(
    tema="Áreas obligatorias y fundamentales", ref="DOC-NOR",
    refT="Normatividad educativa", nivel="basic",
    ctx="Al organizar el plan de estudios de la básica, el consejo académico revisa qué áreas debe incluir de manera obligatoria y cuáles puede ofrecer como proyectos transversales o actividades complementarias. La institución tiene veinticinco horas semanales por grado y debe repartirlas sin dejar por fuera ninguna de las áreas que la ley exige.",
    q="¿Cuál de las siguientes es un área obligatoria y fundamental según la Ley 115?",
    ops=[
        "Robótica y pensamiento computacional, que la institución viene ofreciendo desde hace tres años en la básica.",
        "Ciencias sociales, historia, geografía, constitución política y democracia, como una sola área del plan.",
        "Oratoria y expresión oral, que la institución incorporó al plan por decisión del consejo académico anterior.",
    ],
    correcta=1,
    expl=[
        "La robótica puede integrarse al área de tecnología e informática, pero no es un área obligatoria por sí misma.",
        "Correcto: es una de las áreas obligatorias y fundamentales que enumera la Ley General de Educación.",
        "La oratoria no figura entre las áreas obligatorias y fundamentales que establece la ley.",
    ],
),

dict(
    tema="Situaciones tipo I", ref="DOC-CON",
    refT="Convivencia escolar", nivel="intermediate",
    ctx="Dos estudiantes de sexto discuten por un puesto, se dicen apodos y uno empuja al otro. Ninguno resulta lesionado, es la primera vez que ocurre entre ellos y los dos siguen la clase con normalidad después del incidente.",
    q="¿Cómo se clasifica la situación?",
    ops=[
        "Tipo II, porque hubo agresión física entre los dos estudiantes durante el desarrollo de la clase.",
        "Tipo III, dado que el empujón constituye un contacto físico que puede comprometer la integridad del otro.",
        "Tipo I: conflicto esporádico que incide en el clima escolar sin causar daño al cuerpo ni a la salud.",
    ],
    correcta=2,
    expl=[
        "El tipo II exige que la conducta sea repetida y sistemática o que cause daño al cuerpo o a la salud.",
        "El tipo III corresponde a situaciones constitutivas de presuntos delitos, que no es el caso descrito.",
        "Correcto: esporádica, sin daño al cuerpo ni a la salud y sin repetición previa entre los implicados.",
    ],
),

dict(
    tema="Situaciones tipo II", ref="DOC-CON",
    refT="Convivencia escolar", nivel="advanced",
    ctx="Un estudiante lleva dos meses recibiendo burlas diarias de un grupo de compañeros, que además publican montajes suyos en el chat del curso. No ha habido agresión física y el estudiante ha empezado a faltar a clase.",
    q="¿Cómo se clasifica y qué implica?",
    ops=[
        "Tipo III, porque las publicaciones en internet constituyen por sí mismas una conducta de carácter delictivo.",
        "Tipo II: acoso y ciberacoso repetidos y sistemáticos; debe activarse la ruta e informar a las familias.",
        "Tipo I, dado que no se ha producido ninguna agresión física ni lesión que comprometa su salud.",
    ],
    correcta=1,
    expl=[
        "Que ocurra en línea no convierte la conducta en delito por sí misma; eso exige otros elementos.",
        "Correcto: la repetición y la sistematicidad la ubican en tipo II, aunque no configure delito ni haya lesiones.",
        "La repetición durante dos meses la saca del tipo I, que exige que la situación sea esporádica.",
    ],
),

dict(
    tema="Situaciones tipo III", ref="DOC-CON",
    refT="Convivencia escolar", nivel="advanced",
    ctx="Una estudiante de noveno le relata a su docente un hecho que podría constituir un delito contra su integridad y formación sexual, ocurrido fuera del colegio. Le pide que no se lo cuente a nadie y que no llame a su familia.",
    q="¿Cuál es la actuación correcta?",
    ops=[
        "Indagar primero con ella los detalles para establecer si el relato corresponde a un hecho real.",
        "Citar a los acudientes de las partes involucradas para que lleguen a un acuerdo que proteja a la estudiante.",
        "Poner la situación en conocimiento del rector y de las autoridades competentes, garantizando su protección.",
    ],
    correcta=2,
    expl=[
        "Verificar los hechos no corresponde a la escuela y repetir el relato puede revictimizar a la estudiante.",
        "Estos hechos no son conciliables y no se tramitan mediante acuerdos entre las familias involucradas.",
        "Correcto: ante una situación tipo III se reporta de inmediato, sin indagar ni confrontar al presunto agresor.",
    ],
),

dict(
    tema="Comité escolar de convivencia", ref="DOC-CON",
    refT="Convivencia escolar", nivel="intermediate",
    ctx="Una institución debe conformar la instancia encargada de apoyar la convivencia escolar, la promoción de los derechos humanos, sexuales y reproductivos, y la mitigación de la violencia escolar en el establecimiento.",
    q="¿Cuál es esa instancia y quién la preside?",
    ops=[
        "El comité escolar de convivencia, presidido por el rector del establecimiento educativo.",
        "El consejo académico, presidido por el coordinador académico de la jornada en la que se presente el caso.",
        "El consejo de padres de familia, presidido por el padre de familia que la asamblea elija para ese período.",
    ],
    correcta=0,
    expl=[
        "Correcto: la Ley 1620 de 2013 crea el comité escolar de convivencia y lo pone en cabeza del rector.",
        "El consejo académico tiene funciones curriculares y pedagógicas, no de convivencia escolar.",
        "El consejo de padres no cumple esa función ni tiene a su cargo la ruta de atención integral.",
    ],
),

dict(
    tema="Ruta de atención integral", ref="DOC-CON",
    refT="Convivencia escolar", nivel="advanced",
    ctx="El comité de convivencia revisa cómo está operando la ruta de atención integral en la institución. Quiere verificar que no se esté atendiendo solo lo que ya ocurrió y que exista trabajo anterior y posterior a cada caso.",
    q="¿Cuáles son los componentes de la ruta?",
    ops=[
        "Diagnóstico, intervención y cierre, que corresponden a las tres fases del manejo de cada situación.",
        "Promoción, prevención, atención y seguimiento, en ese orden y de manera articulada entre sí.",
        "Denuncia, investigación y sanción, que estructuran el procedimiento frente a cada situación reportada.",
    ],
    correcta=1,
    expl=[
        "Esa secuencia no corresponde a los componentes que define el sistema de convivencia escolar.",
        "Correcto: promoción, prevención, atención y seguimiento son los cuatro componentes de la ruta.",
        "La ruta no es un procedimiento sancionatorio: su enfoque es formativo y de protección.",
    ],
),

dict(
    tema="Agresión del docente al estudiante", ref="DOC-CON",
    refT="Convivencia escolar", nivel="advanced",
    ctx="Un docente, molesto por el desorden en la última hora de la jornada, le grita a un estudiante y lo ridiculiza delante del curso por su forma de hablar. El curso venía indisciplinado desde el inicio de la sesión.",
    q="¿Cómo debe valorarse?",
    ops=[
        "Es una agresión verbal que vulnera la dignidad del estudiante y contraría el deber de respeto del docente.",
        "Es una medida legítima de manejo del aula, que el docente adoptó ante una situación de indisciplina sostenida.",
        "Solo sería reprochable si el estudiante o su familia presentaran una queja formal ante la coordinación.",
    ],
    correcta=0,
    expl=[
        "Correcto: la autoridad pedagógica no autoriza humillar a un estudiante, y puede tener consecuencias disciplinarias.",
        "Gritar y ridiculizar no es una facultad del docente ni una estrategia de manejo del aula.",
        "La falta existe con independencia de que alguien la denuncie o de que la familia reclame.",
    ],
),

dict(
    tema="Consumo de sustancias", ref="DOC-CON",
    refT="Convivencia escolar", nivel="intermediate",
    ctx="Un docente encuentra a un estudiante de décimo consumiendo una sustancia psicoactiva en el baño del colegio. Es la primera vez que ocurre con ese estudiante y el manual contempla la situación como falta grave. El estudiante tiene diecisiete años, buen rendimiento académico y en los últimos dos meses ha faltado a clase con más frecuencia.",
    q="¿Cuál es la actuación institucional adecuada?",
    ops=[
        "Cancelar su matrícula de manera inmediata, dado que el manual tipifica la conducta como falta grave.",
        "Activar la ruta: informar al rector y al comité, comunicar a la familia, remitir a salud y hacer seguimiento.",
        "Manejarlo con reserva entre el docente y el estudiante, para no estigmatizarlo frente al resto de la institución.",
    ],
    correcta=1,
    expl=[
        "La cancelación inmediata desconoce el debido proceso y el enfoque de protección que exige la situación.",
        "Correcto: se activa la ruta con enfoque de salud y protección, entendiendo el consumo como un asunto de cuidado.",
        "Callar deja al estudiante sin la ayuda que necesita y sin el acompañamiento de su familia.",
    ],
),

dict(
    tema="Mediación escolar", ref="DOC-CON",
    refT="Convivencia escolar", nivel="intermediate",
    ctx="Dos estudiantes de octavo llevan tres semanas en conflicto por un malentendido que empezó en un grupo de redes sociales. No ha habido agresiones físicas ni amenazas, pero el curso se dividió en dos bandos. Los dos estudiantes tienen buen rendimiento académico, ninguno registra antecedentes de convivencia y sus familias ya fueron informadas.",
    q="¿Qué estrategia es pertinente?",
    ops=[
        "Suspender a los dos estudiantes durante tres días para que el ánimo del curso se calme y el conflicto ceda.",
        "Trasladar a uno de los dos a otro curso, de modo que la convivencia del grupo pueda normalizarse rápidamente.",
        "Convocar una mediación donde cada uno exponga su versión y se acuerden compromisos verificables.",
    ],
    correcta=2,
    expl=[
        "La suspensión no resuelve el conflicto ni le enseña a nadie a tramitar un desacuerdo de otra manera.",
        "Separarlos atiende el síntoma sin resolver la causa, y el curso sigue dividido en dos bandos.",
        "Correcto: la mediación busca restaurar la relación y generar acuerdos, no imponer un castigo.",
    ],
),

dict(
    tema="Discriminación entre pares", ref="DOC-CON",
    refT="Convivencia escolar", nivel="advanced",
    ctx="Varios estudiantes excluyen sistemáticamente de los trabajos en grupo a un compañero por su origen étnico. Cuando la docente conforma los grupos ellos protestan, y cuando los conforman libremente el compañero siempre queda solo.",
    q="¿Cómo debe actuar la docente?",
    ops=[
        "Asignarle trabajos individuales al estudiante excluido, para evitar que continúe expuesto a esa situación.",
        "Intervenir de inmediato: nombrar la discriminación, activar la ruta y trabajar el tema con todo el curso.",
        "Conversar únicamente con el estudiante excluido para ayudarle a integrarse mejor con sus compañeros.",
    ],
    correcta=1,
    expl=[
        "Aislarlo consolida la exclusión en lugar de corregirla y le transmite que el problema es suyo.",
        "Correcto: se nombra, se activa la ruta y se trabaja con el colectivo, porque la exclusión vulnera la igualdad.",
        "Poner la carga sobre la víctima invierte la responsabilidad de lo que está ocurriendo en el curso.",
    ],
),

dict(
    tema="Registro en el observador", ref="DOC-CON",
    refT="Convivencia escolar", nivel="intermediate",
    ctx="Un docente escribe en el observador del estudiante: «Estudiante problemático, no tiene remedio». No describe ningún hecho, no indica fecha del incidente ni registra acuerdo alguno con el estudiante o su familia.",
    q="¿Qué está mal en ese registro?",
    ops=[
        "El problema es que el registro no fue firmado por el estudiante ni por su acudiente, como exige el formato.",
        "No hay ningún problema: el observador existe justamente para registrar la conducta de cada estudiante.",
        "Califica a la persona en vez de describir un hecho, y un juicio así puede marcar todo su proceso escolar.",
    ],
    correcta=2,
    expl=[
        "La firma es un requisito formal, pero el problema de fondo está en el contenido de lo que se escribió.",
        "El observador registra hechos y acuerdos, no etiquetas sobre la persona del estudiante.",
        "Correcto: debe describir la situación, el contexto, los acuerdos alcanzados y el seguimiento previsto.",
    ],
),

dict(
    tema="Familia que no asiste a las citaciones", ref="DOC-CON",
    refT="Convivencia escolar", nivel="intermediate",
    ctx="Un estudiante acumula cuatro situaciones de convivencia en el período y su familia no ha asistido a ninguna de las tres citaciones enviadas. Las citaciones se enviaron por escrito y se confirmó su recepción por teléfono.",
    q="¿Qué corresponde hacer?",
    ops=[
        "Dejar constancia de cada citación, insistir por los medios disponibles y reportar la posible vulneración.",
        "Suspender al estudiante hasta que sus acudientes se presenten a la institución a atender las citaciones.",
        "Resolver las situaciones internamente sin la familia, dado que ya se agotaron los intentos de vincularla.",
    ],
    correcta=0,
    expl=[
        "Correcto: se documenta, se insiste y se reporta ante la autoridad competente la posible vulneración de derechos.",
        "Suspender al estudiante lo castiga por una omisión que es de los adultos responsables de su cuidado.",
        "Renunciar a vincular a la familia desconoce el principio de corresponsabilidad en la protección del menor.",
    ],
),

dict(
    tema="Prevención en la ruta", ref="DOC-CON",
    refT="Convivencia escolar", nivel="basic",
    ctx="La institución quiere trabajar la convivencia antes de que aparezcan los conflictos: identificar los factores de riesgo del curso, formar en manejo de emociones y fortalecer los acuerdos de aula desde el inicio del año.",
    q="¿A qué componente de la ruta corresponde ese enfoque?",
    ops=[
        "Atención, que agrupa las acciones que se despliegan una vez la situación se ha presentado en la institución.",
        "Seguimiento, que verifica el cumplimiento de los compromisos acordados tras la atención de cada situación.",
        "Prevención, que reúne las acciones orientadas a intervenir sobre los factores de riesgo antes del hecho.",
    ],
    correcta=2,
    expl=[
        "La atención opera cuando la situación ya se presentó, que es justamente lo que la institución quiere evitar.",
        "El seguimiento verifica lo acordado después de la atención, de modo que es posterior y no anterior.",
        "Correcto: la prevención busca intervenir sobre los factores de riesgo antes de que el hecho ocurra.",
    ],
),

dict(
    tema="Confidencialidad del comité", ref="DOC-CON",
    refT="Convivencia escolar", nivel="advanced",
    ctx="Durante la atención de un caso de acoso escolar, un integrante del comité comenta los detalles en la sala de profesores. Todos los presentes son docentes de la institución y varios dan clase al estudiante involucrado.",
    q="¿Qué deber se incumple?",
    ops=[
        "El deber de confidencialidad que rige las actuaciones del comité escolar de convivencia.",
        "El deber de informar oportunamente a los acudientes de los estudiantes que están involucrados en el caso.",
        "Ninguno, puesto que todos los presentes son docentes de la institución y varios atienden al estudiante.",
    ],
    correcta=0,
    expl=[
        "Correcto: la confidencialidad protege a los estudiantes involucrados y evita su estigmatización.",
        "Informar a los acudientes es un deber distinto que se cumple por el canal y en el momento previstos.",
        "Ser docente de la institución no habilita el acceso a los detalles de un caso en curso.",
    ],
),

]
