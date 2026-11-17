# -*- coding: utf-8 -*-
"""Competencias pedagógicas y evaluación del aprendizaje. Tres opciones."""

PED = "Competencias pedagógicas"
EVA = "Evaluación del aprendizaje"

BANCO = [
dict(
    tema="Saberes previos", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="Al empezar una unidad sobre fracciones en cuarto grado, la docente nota que doce de los treinta estudiantes sostienen que un medio es menor que un cuarto, «porque cuatro es más que dos». Lo explican con seguridad y entre ellos se dan la razón. La unidad está planeada para seis sesiones y la evaluación del período incluye comparación de fracciones.",
    q="¿Cuál es la actuación pedagógica más pertinente?",
    ops=[
        "Partir de esa idea previa y confrontarla con material concreto para que descubran la contradicción.",
        "Repetir la definición formal de fracción hasta que el grupo logre memorizarla y aplicarla correctamente.",
        "Asignar veinte ejercicios de comparación de fracciones para la casa y revisarlos en la siguiente sesión.",
    ],
    correcta=0,
    expl=[
        "Correcto: el conflicto cognitivo es lo que permite reconstruir una concepción errónea que el estudiante cree coherente.",
        "La repetición no desmonta una idea previa que para el estudiante tiene sentido y que sus pares confirman.",
        "Más ejercicios resueltos con la idea equivocada consolidan el error en lugar de corregirlo.",
    ],
),

dict(
    tema="Objetivo de aprendizaje", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="advanced",
    ctx="Una docente redacta en su planeador el objetivo de la clase de ciencias naturales sobre el ciclo del agua. Duda entre varias formulaciones y quiere que el objetivo le permita después verificar si la clase funcionó o no. La coordinación académica revisa los planeadores cada mes y observa que muchos objetivos están redactados como actividades.",
    q="¿Cuál de estas formulaciones es un objetivo de aprendizaje y no una actividad?",
    ops=[
        "Ver el video sobre el ciclo del agua y tomar apuntes de las ideas principales que allí se presentan.",
        "Explicar con sus propias palabras las fases del ciclo del agua y dar un ejemplo de cada una de ellas.",
        "Resolver la guía de la página 42 del texto y socializar las respuestas en la última parte de la sesión.",
    ],
    correcta=1,
    expl=[
        "Ver un video y tomar apuntes es lo que hace el estudiante, no lo que se espera que aprenda.",
        "Correcto: nombra lo que el estudiante será capaz de hacer y permite verificar si lo logró.",
        "Resolver una guía es una tarea; el aprendizaje que persigue no queda enunciado en ninguna parte.",
    ],
),

dict(
    tema="Enseñanza diferenciada", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="advanced",
    ctx="En un mismo curso de segundo grado hay ocho estudiantes que leen con fluidez y comprenden lo que leen, y seis que aún decodifican palabra por palabra. Los demás están en puntos intermedios. La docente tiene una sola hora diaria de lenguaje.",
    q="¿Qué estrategia responde mejor a esa diversidad?",
    ops=[
        "Dividir el curso en dos grupos permanentes según su nivel de lectura y trabajar con cada uno por separado.",
        "Enseñar al nivel promedio del curso, que es donde se ubica la mayoría de los estudiantes del grupo.",
        "Proponer una misma tarea con distintos niveles de complejidad y apoyo, sobre el mismo aprendizaje.",
    ],
    correcta=2,
    expl=[
        "Separar de forma permanente por nivel segrega y termina bajando las expectativas sobre el grupo más rezagado.",
        "Enseñar al promedio deja por fuera a los dos extremos, que son catorce de los estudiantes del curso.",
        "Correcto: es la lógica de los ajustes razonables; todos trabajan el mismo aprendizaje con apoyos diferentes.",
    ],
),

dict(
    tema="Zona de desarrollo próximo", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="Un estudiante no logra resolver solo un problema de proporcionalidad. Cuando la docente le hace dos preguntas orientadoras —qué está comparando y qué pasa si duplica una de las cantidades— lo resuelve completo y explica su procedimiento.",
    q="¿Qué describe esa situación?",
    ops=[
        "Que la docente le está dando la respuesta de manera indirecta a través de las preguntas que formula.",
        "Que el contenido está dentro de su zona de desarrollo próximo: lo alcanza con ayuda que luego se retira.",
        "Que el estudiante todavía no está preparado para ese contenido y conviene volver a él más adelante.",
    ],
    correcta=1,
    expl=[
        "Orientar con preguntas que el estudiante debe responder no equivale a darle la respuesta.",
        "Correcto: lo que hoy hace con ayuda mañana lo hará solo, y ese es el sentido del andamiaje.",
        "Que necesite ayuda no significa que no esté preparado: significa que necesita mediación.",
    ],
),

dict(
    tema="Preguntas que promueven pensamiento", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="Al cerrar la lectura de un cuento en quinto grado, la docente quiere formular una pregunta que obligue a pensar sobre la historia y no solo a recordar sus datos. Dispone de diez minutos antes del timbre. El cuento trabajaba la decisión de un personaje que abandona su casa, y durante la lectura varios estudiantes manifestaron opiniones contrarias.",
    q="¿Cuál cumple mejor ese propósito?",
    ops=[
        "¿Cómo se llamaba el personaje principal y en qué ciudad ocurría la historia que acabamos de leer?",
        "¿Qué habría cambiado en la historia si el personaje hubiera tomado la decisión contraria al final?",
        "¿En qué página aparece el momento en que el personaje decide marcharse de la casa de su abuela?",
    ],
    correcta=1,
    expl=[
        "Recuperar un nombre y un lugar es memoria literal: no exige comprender la lógica del relato.",
        "Correcto: obliga a razonar sobre causas y consecuencias dentro de la lógica interna de la historia.",
        "Ubicar una página verifica que el estudiante tenga el libro abierto, no que haya comprendido.",
    ],
),

dict(
    tema="Clima de aula frente al error", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="Un estudiante responde mal delante del curso y cinco compañeros se ríen abiertamente. El estudiante se pone rojo, baja la mirada y no vuelve a levantar la mano durante el resto de la clase, pese a que la docente formula otras cuatro preguntas al grupo en los minutos siguientes.",
    q="¿Cuál es la respuesta docente más adecuada?",
    ops=[
        "Llamar la atención del estudiante por no haber estudiado el tema que se trabajó la sesión anterior.",
        "Detener la burla, reconocer el intento y usar la respuesta equivocada para avanzar con todo el grupo.",
        "Continuar la clase sin referirse a las risas, para no darle más importancia de la que realmente tiene.",
    ],
    correcta=1,
    expl=[
        "Culpar al estudiante agrava su exposición y confirma ante el grupo que equivocarse se castiga.",
        "Correcto: protege al estudiante y convierte el error en material de aprendizaje para todo el curso.",
        "Ignorar las risas autoriza la burla y enseña que equivocarse tiene un costo social en ese salón.",
    ],
),

dict(
    tema="Secuencia didáctica", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="advanced",
    ctx="Una docente planea enseñar el concepto de densidad en séptimo grado. Dispone de tres sesiones, tiene recipientes, agua, aceite y objetos de distinto material, y el grupo no ha trabajado el concepto antes. El plan de área exige que al final de la unidad los estudiantes puedan predecir si un objeto flotará en un líquido determinado.",
    q="¿Cuál es la secuencia didáctica más coherente?",
    ops=[
        "Dictar la definición y la fórmula, resolver ejercicios y cerrar con el experimento como actividad final.",
        "Experiencia con objetos que flotan y se hunden, discusión de hipótesis, formalización y aplicación.",
        "Definición formal del concepto, deducción de la fórmula, ejercicios de aplicación y evaluación escrita.",
    ],
    correcta=1,
    expl=[
        "Dejar el experimento como premio final desaprovecha su valor para construir el concepto desde la experiencia.",
        "Correcto: va de la experiencia a la formalización y cierra con transferencia a casos nuevos.",
        "Empezar por la definición formal deja el concepto sin anclaje en ninguna experiencia del estudiante.",
    ],
),

dict(
    tema="Transferencia del aprendizaje", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="advanced",
    ctx="Los estudiantes resuelven correctamente los veinte ejercicios de porcentajes del libro, pero cuando se les pide calcular el descuento de una prenda en una situación de compra simulada, la mayoría no sabe por dónde empezar.",
    q="¿Qué indica esa situación?",
    ops=[
        "Que aprendieron un procedimiento asociado al formato del ejercicio, pero no comprendieron el concepto.",
        "Que el tema de porcentajes resulta demasiado complejo para la edad y el grado en que se está trabajando.",
        "Que no estudiaron lo suficiente y que conviene repetir la unidad completa desde el comienzo del tema.",
    ],
    correcta=0,
    expl=[
        "Correcto: es la diferencia entre ejecutar un algoritmo conocido y comprender el concepto que lo sustenta.",
        "El dominio de los veinte ejercicios desmiente que el tema exceda las posibilidades del grupo.",
        "El desempeño en los ejercicios muestra que sí estudiaron: lo que falta es transferencia, no estudio.",
    ],
),

dict(
    tema="Retroalimentación efectiva", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="advanced",
    ctx="Una estudiante entrega un ensayo con ideas valiosas y bien documentadas, pero sin estructura argumentativa: los párrafos no se conectan y la tesis aparece recién al final. Es el primer ensayo que escribe en su vida escolar.",
    q="¿Cuál es la retroalimentación más útil?",
    ops=[
        "Escribir «mejorar redacción y estructura» al final del texto y asignar una calificación de tres sobre cinco.",
        "Reescribir dos párrafos del ensayo con la estructura correcta para que ella vea cómo debería quedar.",
        "Señalar dos ideas valiosas, mostrar con un ejemplo cómo se ordena un párrafo y pedir que reescriba uno.",
    ],
    correcta=2,
    expl=[
        "Un comentario genérico no indica qué cambiar ni cómo hacerlo, y la nota sola no comunica nada.",
        "Reescribirlo por ella le quita la oportunidad de aprender a hacerlo con sus propias ideas.",
        "Correcto: reconoce lo logrado, muestra el camino y pide una acción concreta de mejora.",
    ],
),

dict(
    tema="Trabajo colaborativo", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="En un trabajo en grupo de cuatro integrantes, uno hizo la investigación, el documento y la presentación, y los otros tres firmaron. Es la tercera vez en el período que ocurre con los mismos estudiantes. El estudiante que hizo todo no se queja, pero sus notas en las demás áreas empezaron a bajar durante el mismo período.",
    q="¿Qué faltó en el diseño de la actividad?",
    ops=[
        "Faltó que la docente conformara los grupos en lugar de permitir que los estudiantes los eligieran libremente.",
        "Faltó interdependencia y responsabilidad individual: roles, productos por integrante y evaluación del aporte.",
        "Faltó reducir el tamaño de los grupos, porque cuatro integrantes permiten que algunos pasen desapercibidos.",
    ],
    correcta=1,
    expl=[
        "Elegir los grupos no garantiza por sí solo que todos aporten al producto final del trabajo.",
        "Correcto: sin esas dos condiciones el trabajo en grupo se convierte en el trabajo de uno solo.",
        "El tamaño ayuda, pero no resuelve la ausencia de responsabilidad individual sobre el resultado.",
    ],
),

dict(
    tema="Uso pedagógico del error", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="Al revisar la evaluación, la docente detecta que dieciséis de los treinta estudiantes cometieron exactamente el mismo error en la operación con números negativos: invirtieron el signo al restar. Los otros catorce resolvieron bien el ejercicio y la docente tiene dos sesiones antes de la evaluación acumulativa del período.",
    q="¿Qué conviene hacer?",
    ops=[
        "Llevar el error al tablero sin señalar a nadie, reconstruir el razonamiento y mostrar dónde se quiebra.",
        "Marcarlo como incorrecto en cada evaluación y continuar con el tema siguiente del plan de estudios.",
        "Repetir toda la unidad desde el principio, dado que más de la mitad del curso no alcanzó el objetivo.",
    ],
    correcta=0,
    expl=[
        "Correcto: un error compartido por media clase es información sobre la enseñanza y se trabaja colectivamente.",
        "Marcarlo y seguir deja intacto el razonamiento equivocado, que reaparecerá en los temas siguientes.",
        "Repetir todo desperdicia lo que sí se comprendió y no ataca el punto exacto donde falla el razonamiento.",
    ],
),

dict(
    tema="Motivación externa", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="advanced",
    ctx="Un docente premia con una décima adicional cada tarea entregada a tiempo. Durante dos períodos las entregas superan el noventa por ciento. Al suspender el premio en el tercer período, las entregas caen a la mitad en dos semanas. El docente tiene el mismo grupo desde el año pasado y las entregas nunca habían bajado de esa forma en tan poco tiempo.",
    q="¿Qué muestra esa situación?",
    ops=[
        "Que la décima resultaba insuficiente como incentivo y que convenía aumentarla para sostener el hábito.",
        "Que la motivación construida fue externa y desaparece con la recompensa que la sostenía artificialmente.",
        "Que los estudiantes de ese curso carecen de hábitos de estudio y de compromiso con su propio proceso.",
    ],
    correcta=1,
    expl=[
        "Aumentar la recompensa profundizaría la dependencia en lugar de corregir el problema de fondo.",
        "Correcto: nunca se conectó la tarea con un propósito que el estudiante valorara por sí mismo.",
        "Atribuirlo a la falta de compromiso evita mirar cómo fue diseñada la motivación durante dos períodos.",
    ],
),

dict(
    tema="Planeación y contexto", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="Un docente nuevo llega a una institución rural y aplica tal cual la planeación que usaba en un colegio urbano: los ejemplos son de centros comerciales y transporte masivo, y las tareas suponen acceso a internet en casa.",
    q="¿Cuál es el riesgo principal?",
    ops=[
        "Que los estudiantes rurales no alcancen los estándares porque el contexto les impone mayores limitaciones.",
        "Que la secretaría de educación observe la planeación por no corresponder al modelo pedagógico institucional.",
        "Que los ejemplos y las tareas no dialoguen con la realidad de sus estudiantes y el contenido pierda sentido.",
    ],
    correcta=2,
    expl=[
        "Suponer que no pueden alcanzarlos es una expectativa baja que termina cumpliéndose por sí sola.",
        "La observación administrativa es secundaria frente al problema pedagógico que se está describiendo.",
        "Correcto: contextualizar no es bajar el nivel; es hacer el contenido significativo para quien aprende.",
    ],
),

dict(
    tema="Educación inclusiva", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="advanced",
    ctx="Llega al curso un estudiante con discapacidad cognitiva. Un compañero docente sugiere ubicarlo al fondo del salón con actividades distintas de las del resto, para que avance a su ritmo sin interrumpir la clase. La familia aportó el diagnóstico y la institución ya cuenta con el acompañamiento del equipo de apoyo de la secretaría de educación.",
    q="¿Qué debe primar?",
    ops=[
        "La inclusión real: participa de la misma clase con los ajustes razonables que requiera, no en trabajo aparte.",
        "La remisión a una institución de educación especial, donde recibirá la atención que su condición demanda.",
        "La sugerencia del compañero, que permite al estudiante avanzar a su propio ritmo sin presión del grupo.",
    ],
    correcta=0,
    expl=[
        "Correcto: los apoyos se ajustan sin sacar al estudiante de la experiencia común, y eso queda en su plan individual.",
        "La remisión automática desconoce el derecho a la educación inclusiva en el aula regular.",
        "Un trabajo paralelo y apartado al fondo del salón es exclusión dentro del aula, no atención a su ritmo.",
    ],
),

dict(
    tema="Fluidez y comprensión lectora", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="En segundo grado, siete estudiantes leen en voz alta con fluidez y buena entonación, pero al preguntarles de qué trataba el texto no logran responder ni identificar a los personajes principales. Los mismos siete estudiantes obtienen buenos resultados en los dictados y en las pruebas de ortografía que aplica la docente.",
    q="¿Qué indica ese desempeño?",
    ops=[
        "Que necesitan aumentar su velocidad lectora para liberar atención y poder concentrarse en el contenido.",
        "Que decodifican correctamente pero no comprenden, y hay que enseñar explícitamente estrategias de comprensión.",
        "Que leen bien y que el problema está en la atención que prestan mientras realizan la lectura en voz alta.",
    ],
    correcta=1,
    expl=[
        "Aumentar la velocidad agravaría el problema: ya decodifican rápido y aun así no comprenden.",
        "Correcto: decodificación y comprensión son procesos distintos y ambos deben enseñarse de manera deliberada.",
        "Reducirlo a un asunto de atención ignora un problema real de comprensión lectora que debe trabajarse.",
    ],
),

dict(
    tema="Rol del docente en el aprendizaje activo", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="Una docente organiza una indagación en la que los estudiantes formulan hipótesis sobre qué hace que una planta crezca más rápido y diseñan cómo ponerlas a prueba. Dos grupos se estancan a los quince minutos. Los otros cuatro grupos avanzan bien y faltan veinte minutos para que termine la sesión y deba hacerse la puesta en común.",
    q="¿Cuál es su papel durante la actividad?",
    ops=[
        "Observar sin intervenir en ningún momento, para no influir en los resultados que obtengan los grupos.",
        "Dar la respuesta correcta a los grupos estancados, de modo que puedan avanzar y aprovechar la sesión.",
        "Mediar: hacer preguntas que tensionen las hipótesis y conducir la puesta en común hacia el concepto.",
    ],
    correcta=2,
    expl=[
        "La no intervención deja el aprendizaje al azar y abandona a los grupos que se estancan.",
        "Dar la respuesta anula el propósito de la indagación justo en el momento más productivo del proceso.",
        "Correcto: aprendizaje activo no significa ausencia del docente, sino mediación deliberada y oportuna.",
    ],
),

dict(
    tema="Expectativas del docente", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="advanced",
    ctx="Un docente comenta en la sala de profesores que «de ese curso no se puede esperar mucho» y que por eso les deja talleres de transcripción mientras avanza con los otros grupos del mismo grado. El grado tiene cuatro cursos y los otros tres vienen trabajando el proyecto de escritura que él reemplazó por la transcripción.",
    q="¿Por qué es problemático?",
    ops=[
        "Porque los grupos cambian de un año a otro y la valoración que hoy hace puede no corresponder mañana.",
        "Porque no resulta prudente comentar el desempeño de los cursos en espacios compartidos con otros docentes.",
        "Porque sus expectativas influyen en lo que propone y en lo que los estudiantes terminan creyendo de sí mismos.",
    ],
    correcta=2,
    expl=[
        "La rotación de los cursos no es lo que está en juego: el efecto ya se está produciendo este año.",
        "La discreción importa, pero el problema de fondo no es dónde lo dijo sino qué está haciendo en clase.",
        "Correcto: la expectativa baja se traduce en menos exigencia y se convierte en profecía autocumplida.",
    ],
),

dict(
    tema="Tiempo efectivo de clase", ref="DOC-PED",
    refT="Competencias pedagógicas", nivel="intermediate",
    ctx="De los 55 minutos de clase, 15 se van en organizar el salón, pasar asistencia y esperar a que todos saquen los materiales. Ocurre en cada una de las cinco sesiones semanales del área, de modo que el curso pierde más de una hora de trabajo efectivo cada semana del calendario escolar.",
    q="¿Qué conviene hacer?",
    ops=[
        "Instalar rutinas de entrada que los estudiantes ejecuten solos para recuperar tiempo de enseñanza.",
        "Solicitar la ampliación de la jornada escolar, de modo que el área disponga de más tiempo efectivo.",
        "Eliminar el registro de asistencia, que es lo que más tiempo consume al comienzo de cada sesión.",
    ],
    correcta=0,
    expl=[
        "Correcto: las rutinas automatizadas recuperan más de una hora semanal sin añadir una sola hora a la jornada.",
        "Alargar la jornada sin corregir la rutina arrastra el mismo desperdicio a un horario más extenso.",
        "El registro de asistencia es una obligación del docente y no puede suprimirse por razones de tiempo.",
    ],
),

dict(
    tema="Evaluación formativa", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="intermediate",
    ctx="A mitad de la unidad, la docente aplica una actividad corta de diez minutos, no la califica, revisa los resultados esa misma tarde y con base en ellos reorganiza las tres sesiones que faltan. Dos de los cinco objetivos de la unidad quedaron claramente flojos y la docente decide dedicarles una sesión adicional antes de cerrar.",
    q="¿Qué tipo de evaluación es?",
    ops=[
        "Diagnóstica, porque recoge información sobre lo que los estudiantes saben antes de continuar con la unidad.",
        "Sumativa, porque mide lo que los estudiantes han aprendido hasta ese punto del desarrollo de la unidad.",
        "Formativa: informa la enseñanza y el aprendizaje mientras el proceso todavía puede ajustarse.",
    ],
    correcta=2,
    expl=[
        "La diagnóstica se aplica antes de iniciar la unidad, no a mitad de camino con el proceso en marcha.",
        "La sumativa busca certificar un resultado al cierre, y aquí la docente no califica ni cierra nada.",
        "Correcto: se aplica durante el proceso y su propósito es ajustarlo mientras todavía hay tiempo.",
    ],
),

dict(
    tema="Escala de valoración nacional", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="basic",
    ctx="El consejo académico revisa el sistema institucional de evaluación. El Decreto 1290 de 2009 permite que cada establecimiento defina su propia escala, siempre que pueda equipararse con la escala nacional. La propuesta sobre la mesa es adoptar una escala de uno a diez, y una docente pregunta cómo se haría la equivalencia.",
    q="¿Cuáles son las categorías de esa escala nacional?",
    ops=[
        "Excelente, bueno, aceptable e insuficiente, que es la nomenclatura tradicional de los boletines escolares.",
        "Desempeño superior, desempeño alto, desempeño básico y desempeño bajo, en ese orden descendente.",
        "Aprobado y reprobado, categorías con las que se certifica la promoción al final de cada período académico.",
    ],
    correcta=1,
    expl=[
        "Esas categorías no corresponden a la escala nacional que establece el decreto.",
        "Correcto: superior, alto, básico y bajo son los cuatro niveles de la escala nacional.",
        "La escala nacional tiene cuatro niveles y no se reduce a una decisión binaria de promoción.",
    ],
),

dict(
    tema="Criterios de promoción", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="advanced",
    ctx="Un padre de familia pregunta con cuántas áreas reprobadas pierde el año su hijo. Dice que en el colegio anterior eran tres y que supone que la regla es la misma en todo el país por tratarse de una norma nacional.",
    q="¿Qué responde el docente?",
    ops=[
        "Que los criterios de promoción los define cada establecimiento en su sistema institucional de evaluación.",
        "Que la norma nacional fija en tres el número de áreas reprobadas con las que un estudiante pierde el año.",
        "Que la decisión corresponde al docente de cada área según el desempeño que el estudiante haya mostrado.",
    ],
    correcta=0,
    expl=[
        "Correcto: desde el Decreto 1290 el SIEE de cada institución define esos criterios, dentro del marco del decreto.",
        "La norma nacional no fija un número único de áreas: eso fue justamente lo que el decreto dejó a cada institución.",
        "La decisión de promoción es institucional y colegiada, no individual de cada docente de área.",
    ],
),

dict(
    tema="Evaluar y calificar", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="advanced",
    ctx="En una reunión de área, un docente afirma que evaluar y calificar son exactamente lo mismo y que toda evaluación debe terminar en una nota registrada en la plataforma. Varios colegas asienten. La coordinadora pregunta entonces qué pasa con las actividades que se trabajan en clase y que nunca se registran en la plataforma.",
    q="¿Cómo se le aclara?",
    ops=[
        "Evaluar corresponde al docente de aula y calificar es una función que ejerce la institución educativa.",
        "Evaluar es recoger e interpretar información para tomar decisiones; calificar es asignarle un valor a eso.",
        "Calificar es un proceso más riguroso que evaluar, porque exige instrumentos y escalas previamente definidas.",
    ],
    correcta=1,
    expl=[
        "Ambas acciones corresponden al docente dentro del marco institucional; no se reparten entre dos actores.",
        "Correcto: la calificación es un momento posible de la evaluación, no su equivalente ni su consecuencia obligada.",
        "El rigor no distingue los dos conceptos: una evaluación formativa puede ser rigurosa y no producir nota.",
    ],
),

dict(
    tema="Criterios conocidos de antemano", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="intermediate",
    ctx="Al entregar las notas de una exposición, ocho estudiantes alegan que no sabían que se iba a calificar el manejo del tiempo, que pesó el treinta por ciento. El docente lo había definido pero no lo comunicó. La exposición pesaba el cuarenta por ciento del período y varios estudiantes dedicaron el tiempo a preparar el contenido y no el manejo del tiempo.",
    q="¿Qué debió hacerse?",
    ops=[
        "Promediar esa nota con otra actividad del período para compensar el efecto sobre los estudiantes que reclamaron.",
        "Entregar los criterios de evaluación antes de la actividad, de modo que los estudiantes pudieran prepararse.",
        "Repetir la exposición de todo el curso aplicando esta vez los criterios que fueron comunicados previamente.",
    ],
    correcta=1,
    expl=[
        "Compensar con otra nota no corrige el problema de fondo, que es haber evaluado con criterios ocultos.",
        "Correcto: los criterios se comparten antes, no después; el estudiante tiene derecho a saber cómo se le evalúa.",
        "Repetir la actividad completa es desproporcionado: lo que falló fue la comunicación, no la exposición.",
    ],
),

dict(
    tema="Autoevaluación", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="intermediate",
    ctx="La docente incluye la autoevaluación del estudiante dentro del proceso del período, con una rúbrica que el estudiante usa para valorar su propio trabajo frente a criterios conocidos desde el inicio. Algunos estudiantes se valoran muy por debajo de lo que la docente observa y otros, muy por encima de lo que su trabajo muestra.",
    q="¿Cuál es su propósito pedagógico?",
    ops=[
        "Aligerar la carga de calificación del docente, que puede apoyarse en la valoración que hace cada estudiante.",
        "Desarrollar la capacidad del estudiante de valorar su proceso y decidir cómo mejorar lo que le falta.",
        "Permitir que los estudiantes con bajo desempeño mejoren su nota con la valoración que hacen de sí mismos.",
    ],
    correcta=1,
    expl=[
        "La autoevaluación no sustituye la valoración del docente ni se introduce para reducir su trabajo.",
        "Correcto: forma la metacognición y la autonomía, que es lo que el estudiante se lleva más allá de la nota.",
        "No es un mecanismo para compensar notas: es un ejercicio de valoración frente a criterios explícitos.",
    ],
),

dict(
    tema="Rúbrica", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="advanced",
    ctx="Una docente quiere evaluar un proyecto de escritura de manera que la nota no dependa de su impresión general ni varíe según el orden en que revise los trabajos. Son treinta textos de dos páginas cada uno. Los textos se evalúan en dos momentos del período y la docente quiere además que los estudiantes sepan de antemano qué se espera de ellos.",
    q="¿Qué instrumento conviene?",
    ops=[
        "Una prueba de selección múltiple sobre reglas de ortografía y uso de conectores en textos argumentativos.",
        "Una rúbrica con criterios explícitos y niveles de desempeño descritos para cada uno de esos criterios.",
        "Un registro de asistencia a las sesiones de trabajo del proyecto, que evidencia el compromiso del estudiante.",
    ],
    correcta=1,
    expl=[
        "Una prueba de ortografía evalúa algo distinto del proyecto de escritura que la docente quiere valorar.",
        "Correcto: la rúbrica hace explícitos los criterios, reduce la subjetividad y permite retroalimentar.",
        "La asistencia no dice nada sobre la calidad del texto que el estudiante produjo.",
    ],
),

dict(
    tema="Evaluación diagnóstica", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="basic",
    ctx="Antes de iniciar la unidad sobre sistemas de ecuaciones, la docente aplica una actividad de quince minutos sobre operaciones con enteros y despeje de variables, que son los prerrequisitos del tema. Es la primera vez que la docente trabaja con ese grupo y el año anterior el área estuvo seis semanas sin titular.",
    q="¿Qué función cumple esa evaluación?",
    ops=[
        "Diagnóstica: identifica los saberes previos y las dificultades con que el grupo entra a la unidad.",
        "Sumativa, dado que certifica el dominio de los contenidos que se trabajaron en la unidad anterior.",
        "Clasificatoria, porque permite organizar a los estudiantes en grupos según el nivel que demuestren.",
    ],
    correcta=0,
    expl=[
        "Correcto: se aplica al inicio y su resultado orienta cómo se planea la unidad que va a comenzar.",
        "Certificar lo aprendido corresponde a la evaluación sumativa, que se aplica al cierre de un proceso.",
        "Clasificar de forma permanente a los estudiantes es contrario al propósito de una evaluación diagnóstica.",
    ],
),

dict(
    tema="Actividades de apoyo", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="intermediate",
    ctx="Un estudiante termina el período con desempeño bajo en matemáticas. Faltan dos períodos para cerrar el año y el estudiante asiste regularmente a clase. El SIEE de la institución contempla actividades de apoyo. La dificultad está concentrada en operaciones con fraccionarios, que son prerrequisito de los dos períodos que vienen.",
    q="¿Qué corresponde según la lógica del Decreto 1290?",
    ops=[
        "Promoverlo de todas formas, para no afectar su autoestima ni su permanencia en el sistema educativo.",
        "Adelantar actividades de apoyo orientadas a superar las debilidades, con la valoración que de allí resulte.",
        "Aplicar nuevamente la misma evaluación del período hasta que el estudiante logre obtener un resultado aprobatorio.",
    ],
    correcta=1,
    expl=[
        "Promover sin que supere las debilidades posterga el problema y lo traslada al grado siguiente.",
        "Correcto: la evaluación debe ser continua y orientada a la mejora, y el decreto obliga a prever esas actividades.",
        "Repetir la misma prueba no corrige el aprendizaje no logrado: solo mide otra vez lo mismo.",
    ],
),

dict(
    tema="Validez de un instrumento", ref="DOC-EVA",
    refT="Evaluación del aprendizaje", nivel="advanced",
    ctx="Para evaluar la comprensión de un texto narrativo, un docente aplica una prueba de veinte preguntas. Dieciséis preguntan fechas, nombres de personajes y lugares; cuatro piden interpretar las acciones del protagonista.",
    q="¿Qué problema tiene el instrumento?",
    ops=[
        "El instrumento resulta demasiado extenso para el tiempo del que disponen los estudiantes en la sesión.",
        "Las preguntas deberían formularse de manera oral para evaluar mejor la comprensión del texto narrativo.",
        "No es válido para su propósito: mide memoria literal y no comprensión, que es lo que dice evaluar.",
    ],
    correcta=2,
    expl=[
        "La extensión no es lo que compromete el instrumento: con cinco preguntas tendría el mismo problema.",
        "La modalidad oral no corregiría el tipo de pregunta, que seguiría siendo de recuperación literal.",
        "Correcto: la validez es la correspondencia entre lo que se quiere medir y lo que el instrumento mide.",
    ],
),

]
