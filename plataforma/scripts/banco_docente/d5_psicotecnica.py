# -*- coding: utf-8 -*-
"""Psicotécnica · casos de aula. Juicio situacional del ejercicio docente."""

PSI = "Psicotécnica · casos de aula"

BANCO = [
dict(
    tema="Estudiante que deja de entregar", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="advanced",
    ctx="Un estudiante que siempre cumplía dejó de entregar trabajos hace tres semanas. En clase se ve distraído, callado y evita el contacto visual. No ha faltado ningún día y sus compañeros dicen que tampoco habla con ellos.",
    q="¿Cuál es la primera actuación?",
    ops=[
        "Registrar las no entregas en el observador y dejar que las notas del período reflejen la situación.",
        "Buscar un momento a solas para preguntarle cómo está, antes de asumir que se trata de desinterés.",
        "Llamar a los acudientes para informarles del incumplimiento y pedirles mayor control sobre las tareas.",
    ],
    correcta=1,
    expl=[
        "Dejar que las notas hablen renuncia a entender qué está ocurriendo con un estudiante que cambió de conducta.",
        "Correcto: un cambio brusco de conducta suele tener una causa fuera del aula, y lo primero es escuchar.",
        "Reclamar a la familia antes de indagar puede empeorar la situación del estudiante en su propia casa.",
    ],
),

dict(
    tema="Dos versiones opuestas", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="advanced",
    ctx="Dos estudiantes dan versiones incompatibles de un incidente ocurrido en el descanso. No hubo testigos, ninguno tiene antecedentes y ambos sostienen su versión con seguridad. El acudiente de uno ya llamó al colegio.",
    q="¿Cómo procede el docente?",
    ops=[
        "Sancionar a los dos estudiantes por igual, dado que no es posible establecer quién dice la verdad sobre lo ocurrido.",
        "Escuchar a los dos por separado, dejar constancia de ambas versiones y remitir el caso a la instancia institucional.",
        "Creer la versión del estudiante cuyo comportamiento histórico ha sido mejor a lo largo del año escolar.",
    ],
    correcta=1,
    expl=[
        "Sancionar a ambos castiga también a quien pueda ser la víctima y no esclarece nada de lo ocurrido.",
        "Correcto: documentar y canalizar, sin erigirse en juez de unos hechos que no presenció.",
        "El antecedente de conducta no constituye prueba de lo que ocurrió en el descanso de hoy.",
    ],
),

dict(
    tema="Reclamo de un acudiente en público", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="intermediate",
    ctx="Una madre llega molesta a la entrega de boletines y cuestiona en voz alta la capacidad del docente delante de otros padres. Reclama por la nota de su hijo, que efectivamente bajó dos décimas frente al período anterior.",
    q="¿Cuál es la respuesta más profesional?",
    ops=[
        "Invitarla a un espacio privado, escuchar su reclamo completo y mostrarle con evidencias cómo se construyó la nota.",
        "Pedirle que presente su reclamo por escrito ante la coordinación y continuar con la entrega de los demás boletines.",
        "Responderle en el mismo tono delante de los padres presentes, para no quedar desautorizado frente al grupo.",
    ],
    correcta=0,
    expl=[
        "Correcto: cambiar de escenario, escuchar y sustentar con evidencias es lo que desactiva el conflicto.",
        "Remitir a un trámite sin escuchar agrava el malestar y deja la impresión de que no hay con qué responder.",
        "Responder en el mismo tono convierte un reclamo individual en una confrontación pública.",
    ],
),

dict(
    tema="Compañero que incumple", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="advanced",
    ctx="Un docente del mismo grado lleva un mes llegando veinte minutos tarde a su primera hora. Los estudiantes de ese curso quedan solos en el salón cada mañana y la semana pasada hubo un incidente entre dos de ellos.",
    q="¿Qué hace usted?",
    ops=[
        "Comentar la situación con los demás docentes del grado para que entre todos le hagan ver el problema.",
        "Abstenerse de intervenir, dado que el control del cumplimiento del horario corresponde a la coordinación académica.",
        "Hablar primero con el compañero y, si la situación continúa, informar a la coordinación de la institución.",
    ],
    correcta=2,
    expl=[
        "Comentarlo con terceros no protege a los estudiantes que quedan solos cada mañana en el salón.",
        "Hay menores de edad sin supervisión y ya ocurrió un incidente: la inacción no es una opción neutral.",
        "Correcto: conversación directa primero y, si persiste, el canal institucional que corresponde.",
    ],
),

dict(
    tema="Cruce de compromisos", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="intermediate",
    ctx="Le asignan una comisión adicional que choca con la entrega de notas del período. Las dos cosas vencen la misma semana y ambas requieren por lo menos dos días completos de trabajo que usted no tiene disponibles. La comisión fue asignada ayer por la secretaría de educación y las notas deben quedar en la plataforma antes del cierre del período.",
    q="¿Cuál es la conducta más adecuada?",
    ops=[
        "Aceptar los dos compromisos y resolverlos como pueda, aunque implique trabajar durante el fin de semana.",
        "Informar a tiempo del cruce, proponer un orden o una fecha alterna y precisar qué puede cumplirse con calidad.",
        "Entregar las notas sin revisarlas con el detalle habitual, de modo que alcance a cumplir con la comisión asignada.",
    ],
    correcta=1,
    expl=[
        "Aceptar en silencio suele terminar en incumplir las dos cosas y en asumir solo el costo de la decisión.",
        "Correcto: anticipar el cruce permite que quien asigna decida con información y que nada quede a la deriva.",
        "Entregar notas sin revisar afecta directamente a los estudiantes y a las decisiones que se toman con ellas.",
    ],
),

dict(
    tema="Error propio frente al curso", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="intermediate",
    ctx="En medio de la clase, un estudiante le hace notar que el procedimiento que usted acaba de explicar en el tablero tiene un error en el segundo paso. Revisa y efectivamente lo tiene. Quedan veinte minutos de sesión.",
    q="¿Cuál es la mejor reacción?",
    ops=[
        "Decir que lo revisará con calma después de clase y continuar con el desarrollo previsto para la sesión.",
        "Sostener lo escrito en el tablero para no perder autoridad y corregirlo discretamente al comienzo de la clase siguiente.",
        "Reconocer el error delante del curso, corregirlo con ellos y agradecer la observación que hizo el estudiante.",
    ],
    correcta=2,
    expl=[
        "Aplazarlo deja a todo el curso con el procedimiento equivocado anotado en sus cuadernos.",
        "Sostener un error que ya fue advertido daña la credibilidad mucho más que admitirlo en el momento.",
        "Correcto: modela la honestidad intelectual y aprovecha el error como contenido de la clase.",
    ],
),

dict(
    tema="Favoritismo percibido", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="advanced",
    ctx="Un grupo de estudiantes le dice que usted siempre llama a participar a los mismos cuatro compañeros. Al revisar sus registros de la última semana, confirma que efectivamente preguntó quince veces y catorce fueron a esos cuatro.",
    q="¿Qué hace?",
    ops=[
        "Explicarles que llama a quienes levantan la mano y animarlos a participar más durante las clases.",
        "Dejar de llamar a esos cuatro estudiantes durante las siguientes semanas para equilibrar la participación.",
        "Tomar en serio la observación y adoptar un mecanismo que distribuya la participación en todo el curso.",
    ],
    correcta=2,
    expl=[
        "La explicación puede ser cierta y aun así el efecto es desigual, como lo confirman sus propios registros.",
        "Excluir a los cuatro cambia una desigualdad por otra y los castiga por participar.",
        "Correcto: el patrón ya está verificado y se corrige con un mecanismo, no con buenas intenciones.",
    ],
),

dict(
    tema="Material que no llega", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="intermediate",
    ctx="Planeó una clase con un laboratorio y el día de la sesión el material no está disponible porque el pedido no llegó. Tiene el salón, los estudiantes y cincuenta y cinco minutos. El objetivo era comprender un fenómeno físico.",
    q="¿Cuál es la mejor respuesta?",
    ops=[
        "Sostener el objetivo con una alternativa preparada —demostración, simulación o trabajo con datos— y reprogramar.",
        "Realizar el laboratorio con los materiales que haya disponibles en el aula, aunque no sean los indicados.",
        "Suspender la actividad prevista y dedicar la sesión a repasar los contenidos de la unidad anterior con los estudiantes.",
    ],
    correcta=0,
    expl=[
        "Correcto: lo que no puede perderse es el objetivo de aprendizaje, no la actividad concreta que se planeó.",
        "Improvisar un laboratorio con materiales no previstos puede ser inseguro y desvirtuar el fenómeno.",
        "Repasar la unidad anterior llena el tiempo pero abandona el objetivo que estaba planeado para la sesión.",
    ],
),

dict(
    tema="Estudiante que interrumpe", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="advanced",
    ctx="Un estudiante interrumpe la clase con chistes cada diez minutos. El curso se ríe y la clase se dispersa. Lleva así todo el período, sus notas bajaron y en las otras asignaturas se comporta de la misma manera. Sus compañeros lo buscan en los descansos y él mismo le ha comentado a otra docente que en la casa nadie le pone atención.",
    q="¿Cuál es la estrategia más efectiva a mediano plazo?",
    ops=[
        "Ignorar las interrupciones hasta que el estudiante se canse y el grupo deje de reaccionar ante ellas.",
        "Poner un límite claro en el momento y buscarlo después a solas para entender y acordar otra forma de participar.",
        "Sacarlo del salón cada vez que interrumpa, de modo que el resto del curso pueda continuar con la clase sin dispersarse.",
    ],
    correcta=1,
    expl=[
        "Ignorarlo mientras el curso se ríe refuerza la conducta, porque el estímulo que la sostiene sigue ahí.",
        "Correcto: límite inmediato más conversación posterior es lo que modifica el patrón de conducta.",
        "Sacarlo repetidamente lo excluye del aprendizaje y no cambia nada de lo que origina la conducta.",
    ],
),

dict(
    tema="Resultados bajos del propio curso", ref="DOC-PSI",
    refT="Psicotécnica · casos de aula", nivel="advanced",
    ctx="Los resultados de su curso en una prueba externa quedaron ocho puntos por debajo de los otros tres cursos del mismo grado. Usted tuvo el mismo número de sesiones y trabajó con el mismo plan de estudios que sus colegas.",
    q="¿Cuál es la actitud profesional?",
    ops=[
        "Cuestionar la validez del instrumento, que no necesariamente refleja lo que se trabajó en el aula durante el año.",
        "Explicar que su curso es el más difícil del grado y que el resultado era previsible dadas sus características.",
        "Analizar los resultados por competencia, identificar qué enseñanza quedó débil y ajustar la planeación siguiente.",
    ],
    correcta=2,
    expl=[
        "Cuestionar la prueba sin analizarla evita la revisión del propio trabajo y desaprovecha la información.",
        "Justificar con las características del grupo cierra la posibilidad de aprender del dato obtenido.",
        "Correcto: el resultado es información sobre la enseñanza, no un veredicto sobre las capacidades del grupo.",
    ],
),

]
