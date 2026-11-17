# -*- coding: utf-8 -*-
"""Lectura crítica. Textos originales con preguntas de tesis, inferencia,
intención del autor, supuestos, función de un enunciado y evaluación de
argumentos. Tres opciones, como en el formato oficial."""

LC = "Lectura crítica"

BANCO = [
dict(
    tema="Tesis en un texto argumentativo", ref="DOC-LC",
    refT="Lectura crítica", nivel="intermediate",
    ctx="«Se repite que los niños de hoy no leen. Pero leen mensajes, subtítulos, instrucciones de videojuegos y publicaciones interminables. Lo que ha cambiado no es la cantidad de lectura sino su forma: leen muchísimo y de corrido, y casi nunca vuelven sobre lo leído. El problema no está en el volumen sino en la ausencia de relectura.»",
    q="¿Cuál es la tesis del autor?",
    ops=[
        "Que los niños de hoy leen considerablemente menos que las generaciones que los precedieron en la escuela.",
        "Que el problema no es cuánto leen los niños sino que no releen ni vuelven sobre lo que ya han leído.",
        "Que la lectura en pantalla resulta siempre inferior a la lectura en papel por la forma en que se procesa.",
    ],
    correcta=1,
    expl=[
        "El texto afirma justamente lo contrario: sostiene que leen muchísimo, solo que de otra manera.",
        "Correcto: el autor desplaza el problema de la cantidad a la forma de leer, y lo dice en la última oración.",
        "El texto no compara soportes ni califica uno como inferior al otro en ningún momento.",
    ],
),

dict(
    tema="Inferencia a partir de dos datos", ref="DOC-LC",
    refT="Lectura crítica", nivel="advanced",
    ctx="«En la institución el índice de reprobación bajó del 18 % al 6 % en dos años. En el mismo período, el porcentaje de estudiantes que alcanzaron desempeño superior pasó del 12 % al 5 %. La matrícula y el equipo docente se mantuvieron estables.»",
    q="¿Qué se puede inferir razonablemente de esos dos datos juntos?",
    ops=[
        "Que los estudiantes de desempeño superior se retiraron de la institución durante esos dos años de referencia.",
        "Que la enseñanza mejoró de manera generalizada, como lo demuestra la caída sostenida de la reprobación.",
        "Que los resultados se concentraron en el centro de la escala, lo que podría indicar que bajó la exigencia.",
    ],
    correcta=2,
    expl=[
        "El texto precisa que la matrícula se mantuvo estable, lo que descarta la hipótesis del retiro.",
        "Si la enseñanza hubiera mejorado de forma generalizada, el desempeño superior no debería haber caído.",
        "Correcto: menos reprobados y menos superiores a la vez sugiere un achatamiento de la escala de valoración.",
    ],
),

dict(
    tema="Intención comunicativa", ref="DOC-LC",
    refT="Lectura crítica", nivel="intermediate",
    ctx="«Señores padres de familia: les recordamos que la entrada es a las 6:30 a. m. Después de esa hora el portón se cierra y el estudiante ingresa con registro de retardo. Tres retardos en el mes generan citación al acudiente. Agradecemos su colaboración.»",
    q="¿Cuál es la intención predominante del texto?",
    ops=[
        "Regular una conducta recordando una norma vigente, sus consecuencias y el procedimiento asociado.",
        "Informar a las familias sobre un cambio reciente en el horario de ingreso de los estudiantes al plantel.",
        "Persuadir a los padres de las ventajas formativas que tiene la puntualidad en la vida escolar de sus hijos.",
    ],
    correcta=0,
    expl=[
        "Correcto: enuncia una norma, la hora, la consecuencia y el procedimiento que se activa al reincidir.",
        "El texto no anuncia ningún cambio: usa la palabra «recordamos», que remite a una norma que ya rige.",
        "No argumenta ventajas de ningún tipo: se limita a enunciar la regla y lo que ocurre si se incumple.",
    ],
),

dict(
    tema="Función de un conector", ref="DOC-LC",
    refT="Lectura crítica", nivel="basic",
    ctx="«El colegio adoptó el nuevo material de matemáticas para todos los grupos de sexto grado. Sin embargo, los resultados del primer período no presentaron ninguna variación frente a los del año anterior.»",
    q="¿Qué relación establece el conector «sin embargo»?",
    ops=[
        "Una relación de consecuencia entre la adopción del material y los resultados obtenidos en el período.",
        "Una oposición entre lo que la primera oración hacía esperar y lo que efectivamente ocurrió después.",
        "Una relación de causa, en la que la adopción del material explica el comportamiento de los resultados.",
    ],
    correcta=1,
    expl=[
        "La consecuencia se marcaría con «por lo tanto» o «en consecuencia», no con un conector adversativo.",
        "Correcto: introduce un hecho que contraría la expectativa creada por la primera oración del texto.",
        "Una relación causal se marcaría con «porque» o «debido a», que expresan una idea distinta.",
    ],
),

dict(
    tema="Distinguir hecho de opinión", ref="DOC-LC",
    refT="Lectura crítica", nivel="basic",
    ctx="«El 42 % de los estudiantes de la institución vive a más de una hora de distancia del plantel. Esa cifra explica, sin lugar a dudas, los bajos resultados obtenidos en el área de matemáticas.»",
    q="¿Cómo se clasifican las dos afirmaciones?",
    ops=[
        "La primera es un dato verificable; la segunda es una interpretación presentada como si fuera una certeza.",
        "Las dos son hechos verificables, puesto que ambas se apoyan en información institucional que puede comprobarse.",
        "La primera es una opinión del autor y la segunda, un hecho acreditado por los resultados del área.",
    ],
    correcta=0,
    expl=[
        "Correcto: la expresión «sin lugar a dudas» delata una interpretación que el texto presenta como hecho.",
        "La segunda no es verificable: atribuye una causa sin demostrar la relación entre las dos variables.",
        "Está invertido: la primera es un dato y la segunda, una inferencia causal no demostrada.",
    ],
),

dict(
    tema="Falacia de generalización apresurada", ref="DOC-LC",
    refT="Lectura crítica", nivel="advanced",
    ctx="«Mis tres mejores estudiantes de este año usan el celular para estudiar: consultan videos, resuelven ejercicios en aplicaciones y organizan sus apuntes ahí. Está claro, entonces, que el celular mejora el rendimiento académico de los estudiantes.»",
    q="¿Qué problema tiene ese razonamiento?",
    ops=[
        "El problema es que no cita ninguna fuente académica ni investigación que respalde la afirmación final.",
        "Generaliza desde tres casos elegidos por su buen rendimiento e ignora a quienes usan el celular sin éxito.",
        "El problema es que el uso del celular está prohibido por el manual de convivencia de la mayoría de las instituciones.",
    ],
    correcta=1,
    expl=[
        "La falta de fuente es secundaria frente al error de razonamiento que comete el propio argumento.",
        "Correcto: la muestra es pequeña, está sesgada en la selección y no se contrasta con el caso opuesto.",
        "La eventual prohibición no tiene relación con la validez lógica del argumento que se está evaluando.",
    ],
),

dict(
    tema="Punto de vista del narrador", ref="DOC-LC",
    refT="Lectura crítica", nivel="intermediate",
    ctx="«Entró al salón sin saludar y se sentó al fondo, junto a la ventana. Nadie supo nunca que esa mañana había tenido que dejar a su hermano menor solo en la casa, ni que llevaba dos días sin desayunar.»",
    q="¿Qué tipo de narrador se evidencia?",
    ops=[
        "Un narrador personaje que cuenta desde su propia experiencia lo que le ocurrió esa mañana al entrar al salón.",
        "Un narrador que se dirige directamente al lector para explicarle lo que está ocurriendo en la escena.",
        "Un narrador que conoce lo que los demás personajes ignoran, incluida la vida privada del protagonista.",
    ],
    correcta=2,
    expl=[
        "No hay un «yo» que narre: el texto habla del personaje en tercera persona desde fuera de él.",
        "No hay apelación al lector en ningún momento del fragmento que se presenta.",
        "Correcto: la expresión «nadie supo nunca» revela información a la que ningún personaje tiene acceso.",
    ],
),

dict(
    tema="Función de una referencia externa", ref="DOC-LC",
    refT="Lectura crítica", nivel="advanced",
    ctx="«La repitencia no corrige el aprendizaje: lo posterga. Como ha venido advirtiendo la investigación educativa de las últimas décadas, repetir un año rara vez mejora los resultados del estudiante y sí aumenta de manera significativa su probabilidad de desertar.»",
    q="¿Qué función cumple la referencia a la investigación educativa?",
    ops=[
        "Reconocer una limitación del propio argumento antes de que el lector pueda formularla como objeción.",
        "Respaldar con una autoridad externa la afirmación que el autor acaba de hacer sobre la repitencia.",
        "Introducir una idea opuesta a la del autor para después refutarla con los datos sobre deserción.",
    ],
    correcta=1,
    expl=[
        "El autor no admite ninguna limitación: la referencia refuerza su posición en lugar de matizarla.",
        "Correcto: la cita va en la misma dirección que la tesis y le sirve de apoyo de autoridad.",
        "La investigación citada coincide con el autor, de modo que no funciona como contrargumento.",
    ],
),

dict(
    tema="Significado por el contexto", ref="DOC-LC",
    refT="Lectura crítica", nivel="basic",
    ctx="«La docente acogió la propuesta que le hicieron sus estudiantes sobre el proyecto del período y la incorporó al plan de aula, aunque eso la obligara a reorganizar el trabajo de las tres semanas siguientes.»",
    q="En ese contexto, ¿qué significa «acogió»?",
    ops=[
        "La toleró sin convicción, limitándose a no oponerse a lo que sus estudiantes le estaban proponiendo.",
        "La pospuso para considerarla más adelante, cuando el plan de aula lo permitiera sin tantos ajustes.",
        "La aceptó y la hizo suya, hasta el punto de modificar su planeación para poder incorporarla.",
    ],
    correcta=2,
    expl=[
        "La reorganización de tres semanas de trabajo muestra un compromiso activo, no una tolerancia pasiva.",
        "El texto dice que la incorporó al plan de aula, de modo que no la pospuso para después.",
        "Correcto: la aceptó, la integró a su planeación y asumió el costo de reorganizar su trabajo.",
    ],
),

dict(
    tema="Estructura de un texto expositivo", ref="DOC-LC",
    refT="Lectura crítica", nivel="intermediate",
    ctx="«El texto primero define qué es la evaluación formativa. Luego la contrasta con la evaluación sumativa señalando tres diferencias. Después presenta tres ejemplos tomados de aulas de primaria. Al final enumera las condiciones necesarias para aplicarla.»",
    q="¿Qué estructura organiza ese texto?",
    ops=[
        "Expositiva: definición, contraste, ejemplificación y condiciones de aplicación del concepto tratado.",
        "Argumentativa, con una tesis inicial seguida de la refutación de los contrargumentos que suelen oponérsele.",
        "Narrativa, puesto que presenta los hechos siguiendo el orden cronológico en que fueron sucediendo.",
    ],
    correcta=0,
    expl=[
        "Correcto: la secuencia descrita corresponde a un texto que explica un concepto sin defender una posición.",
        "No hay una tesis que se defienda frente a objeciones: el texto explica, no argumenta a favor de algo.",
        "No se narran hechos que ocurran en el tiempo: se desarrolla un concepto por partes.",
    ],
),

dict(
    tema="Supuesto implícito", ref="DOC-LC",
    refT="Lectura crítica", nivel="advanced",
    ctx="En el acta del consejo académico queda consignada esta propuesta del jefe de área: «Hay que aumentar de cuatro a seis las horas semanales de clase de matemáticas si queremos mejorar los resultados que la institución viene obteniendo en esa área desde hace tres años». Nadie discute el fundamento de la afirmación.",
    q="¿Cuál es el supuesto que sostiene esa afirmación?",
    ops=[
        "Que las matemáticas tienen mayor importancia formativa que las demás áreas del plan de estudios.",
        "Que los docentes de matemáticas de la institución no están suficientemente preparados para enseñar el área.",
        "Que más tiempo de exposición a la asignatura produce por sí solo un mejor aprendizaje del estudiante.",
    ],
    correcta=2,
    expl=[
        "La jerarquía entre áreas no es necesaria para que el argumento funcione como está planteado.",
        "El texto no dice nada sobre la preparación de los docentes ni la pone en cuestión.",
        "Correcto: sin ese supuesto, aumentar las horas no garantizaría ninguna mejora en los resultados.",
    ],
),

dict(
    tema="Ironía", ref="DOC-LC",
    refT="Lectura crítica", nivel="advanced",
    ctx="En la cartelera de la sala de profesores aparece escrito a mano, debajo del cronograma de la semana: «Qué buena idea fue programar la izada de bandera, el simulacro de evacuación y la entrega de boletines el mismo viernes, todo a las diez de la mañana y en el mismo patio».",
    q="¿Cómo debe leerse el enunciado?",
    ops=[
        "Literalmente: el autor elogia la decisión de concentrar las tres actividades en una sola jornada de trabajo.",
        "Irónicamente: el autor critica la programación afirmando lo contrario de lo que realmente piensa.",
        "Como una pregunta retórica cuya respuesta el lector debe construir a partir de los datos dados.",
    ],
    correcta=1,
    expl=[
        "La imposibilidad material de hacer las tres cosas a la vez y en el mismo lugar descarta el elogio literal.",
        "Correcto: la ironía consiste precisamente en afirmar lo contrario de lo que se quiere decir.",
        "No hay forma interrogativa en el enunciado, de modo que no puede tratarse de una pregunta retórica.",
    ],
),

dict(
    tema="Jerarquía entre ideas", ref="DOC-LC",
    refT="Lectura crítica", nivel="intermediate",
    ctx="«La biblioteca escolar cumple tres funciones: resguarda el material de consulta, acompaña los procesos de investigación de los estudiantes y es, muchas veces, el único lugar silencioso de todo el colegio.»",
    q="¿Cuál es la idea principal del enunciado?",
    ops=[
        "Que la biblioteca escolar cumple varias funciones distintas dentro de la vida de la institución.",
        "Que en el colegio hay tanto ruido que la biblioteca termina siendo el único refugio disponible para estudiar.",
        "Que la función principal de la biblioteca es resguardar y conservar el material de consulta.",
    ],
    correcta=0,
    expl=[
        "Correcto: la oración anuncia tres funciones y luego las enumera; esa es la idea que agrupa a las demás.",
        "El silencio es una de las tres funciones que se enumeran, no la idea que organiza el enunciado.",
        "Resguardar el material es apenas la primera de las tres funciones mencionadas en el texto.",
    ],
),

dict(
    tema="Contraargumento", ref="DOC-LC",
    refT="Lectura crítica", nivel="advanced",
    ctx="En una reunión de área sobre la política de tareas de la institución, un docente sostiene lo siguiente: «Las tareas para la casa son necesarias porque refuerzan lo visto en clase y crean hábitos de estudio en los estudiantes». Varios colegas asienten y la coordinadora pide argumentos en contra antes de decidir.",
    q="¿Cuál de las siguientes es un contraargumento y no una simple opinión contraria?",
    ops=[
        "Que a los estudiantes no les gustan las tareas y que por eso muchos de ellos las entregan copiadas o incompletas.",
        "Que el refuerzo ocurre solo si el estudiante tiene en casa las condiciones para hacerlas, y muchos no las tienen.",
        "Que antes tampoco se dejaban tantas tareas y los estudiantes de entonces aprendían igual o mejor.",
    ],
    correcta=1,
    expl=[
        "El agrado de los estudiantes no refuta la premisa sobre el refuerzo ni sobre los hábitos de estudio.",
        "Correcto: señala una condición que el argumento original da por supuesta y muestra su consecuencia.",
        "Apelar al pasado no refuta el argumento: afirma algo distinto sin demostrar la relación.",
    ],
),

dict(
    tema="Coherencia de un párrafo", ref="DOC-LC",
    refT="Lectura crítica", nivel="intermediate",
    ctx="«La planeación de aula orienta el trabajo del docente. Permite anticipar materiales y distribuir los tiempos de cada sesión. El rector viajó el martes a la secretaría de educación. También facilita evaluar si los objetivos propuestos se cumplieron.»",
    q="¿Qué problema tiene el párrafo?",
    ops=[
        "Mezcla de manera incorrecta los tiempos verbales y eso dificulta seguir el hilo de lo que afirma.",
        "Incluye una oración ajena al tema que rompe la coherencia de lo que el párrafo viene desarrollando.",
        "Utiliza demasiados conectores, lo que hace que las ideas queden excesivamente subordinadas entre sí.",
    ],
    correcta=1,
    expl=[
        "El uso de tiempos verbales no es lo que rompe el párrafo: el problema está en el contenido.",
        "Correcto: el viaje del rector no guarda ninguna relación con la planeación de aula.",
        "Apenas aparece un conector en todo el párrafo, de modo que ese no puede ser el problema.",
    ],
),

dict(
    tema="Público destinatario", ref="DOC-LC",
    refT="Lectura crítica", nivel="basic",
    ctx="«Recuerda traer tu cuaderno de apuntes, llegar antes de que suene el timbre y dejar el celular en el casillero antes de entrar al laboratorio. No se permite el ingreso con alimentos ni bebidas de ninguna clase.»",
    q="¿A quién está dirigido el texto?",
    ops=[
        "A los padres de familia, que son quienes deben supervisar el cumplimiento de esas indicaciones.",
        "A los docentes del área, que deben verificar esas condiciones antes de iniciar cada sesión práctica.",
        "A los estudiantes, que son quienes ejecutan las acciones descritas al entrar al laboratorio.",
    ],
    correcta=2,
    expl=[
        "Los padres no son quienes traen el cuaderno ni dejan el celular en el casillero del laboratorio.",
        "Las indicaciones describen acciones de quien ingresa, no de quien supervisa la sesión.",
        "Correcto: el tuteo y las acciones descritas corresponden inequívocamente al estudiante.",
    ],
),

dict(
    tema="Validez de una conclusión", ref="DOC-LC",
    refT="Lectura crítica", nivel="advanced",
    ctx="«Todos los estudiantes que asistieron voluntariamente al refuerzo de los sábados mejoraron su nota en el siguiente período. Por lo tanto, puede afirmarse que el refuerzo de los sábados mejora las notas de quienes lo reciben.»",
    q="¿Qué debilita esa conclusión?",
    ops=[
        "Que las notas escolares no constituyen un indicador válido del aprendizaje real que alcanzan los estudiantes.",
        "Que el texto no precisa cuántos estudiantes asistieron efectivamente al refuerzo de los sábados.",
        "Que al refuerzo asisten voluntariamente los más motivados, de modo que la mejora puede deberse a eso.",
    ],
    correcta=2,
    expl=[
        "Esa objeción es válida en general, pero no es lo que invalida este razonamiento en particular.",
        "El número ayudaría a dimensionar el hallazgo, pero el problema de fondo es el sesgo de selección.",
        "Correcto: no se comparó con quienes no asistieron, y la voluntariedad introduce un sesgo decisivo.",
    ],
),

dict(
    tema="Resumen fiel", ref="DOC-LC",
    refT="Lectura crítica", nivel="intermediate",
    ctx="«La jornada única amplía el tiempo escolar, pero sin alimentación, transporte y docentes suficientes se convierte en más horas de lo mismo. Ampliar el tiempo y no cambiar lo que pasa dentro del aula no mejora el aprendizaje de nadie.»",
    q="¿Cuál es el resumen más fiel?",
    ops=[
        "La jornada única es una política equivocada que debería suspenderse hasta que existan todas las condiciones.",
        "La alimentación escolar es el principal problema que enfrenta hoy la educación pública del país.",
        "Ampliar el tiempo escolar mejora el aprendizaje solo si cambian las condiciones y lo que ocurre en el aula.",
    ],
    correcta=2,
    expl=[
        "El texto no pide suspender la política: señala las condiciones bajo las cuales puede funcionar.",
        "La alimentación es uno de los tres factores que menciona, no el diagnóstico general del sistema.",
        "Correcto: recoge la condición que plantea el texto sin agregarle conclusiones que este no formula.",
    ],
),

]
