# -*- coding: utf-8 -*-
"""Día 18 · Talento humano V: capacitación, bienestar y seguridad y salud en el trabajo."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _brenda import base, meta

META = meta(
    codigo='FUN-GTH-4TC17B-05',
    archivo='FUN-GTH-4TC17B-05-capacitacion-bienestar-seguridad-salud-trabajo.html',
    dia=18,
    titulo_doc='Talento humano V: capacitación, bienestar y seguridad y salud en el trabajo',
    h1='Talento humano V<br>Capacitación, bienestar y seguridad y salud en el trabajo',
    kicker='Día 18 · Conocimiento específico',
    sub='Cierra el bloque de talento humano con las tres líneas que desarrollan a las personas y las protegen. Verás el <strong>Plan Institucional de Capacitación</strong> y cómo nace de un diagnóstico de necesidades, la diferencia entre <strong>capacitación y educación formal</strong>, la <strong>inducción y la reinducción</strong>, los <strong>programas de bienestar y estímulos</strong> con criterios objetivos de selección, y el <strong>Sistema de Gestión de la Seguridad y Salud en el Trabajo</strong>: política, matriz de riesgos, <strong>jerarquía de controles</strong>, incidentes y accidentes, el <strong>COPASST</strong> frente al comité de convivencia, el <strong>riesgo psicosocial</strong> y la <strong>reserva de la historia clínica ocupacional</strong>.',
    badges=['⏱ 100-120 min', '🛡️ Desarrollo y SST', '📖 Específico'],
    fmeta='Talento humano V: capacitación, bienestar y SST (Decretos 1083 de 2015 y 1072 de 2015, Resolución 2646 de 2008 y Decreto Ley 262 de 2000)',
    alerta='Talento humano V: capacitación, bienestar y seguridad y salud en el trabajo',
)

MOD_PGN = '''
      <div class="modulo-head"><div class="modulo-n">★</div><h3>Dónde encaja la División de Gestión Humana en el desarrollo y la protección de las personas</h3></div>
      <div class="b-texto">
        <p>Las tres líneas de hoy no son un anexo amable de la gestión del talento humano: en la PGN tienen respaldo normativo expreso y la División es protagonista. El <strong>artículo 63 del Decreto Ley 262 de 2000</strong> las menciona en tres numerales distintos.</p>
        <div class="tabla-wrap"><table>
          <thead><tr><th>Numeral</th><th>Función</th><th>Qué significa en su puesto</th></tr></thead>
          <tbody>
            <tr><td><strong>1</strong></td><td><strong>Asesorar al Secretario General</strong> en políticas y programas para mejorar la <strong>calidad de vida laboral</strong> de los servidores.</td><td>El bienestar no es una iniciativa suelta: es una política que se propone, se sustenta y se somete a quien decide.</td></tr>
            <tr><td><strong>2</strong></td><td>Contribuir al <strong>diseño y aplicación</strong> de los programas de <strong>inducción y reinducción</strong>.</td><td>Usted apoya el diseño, convoca, registra la asistencia, custodia las constancias y mide el resultado.</td></tr>
            <tr><td><strong>9</strong></td><td>Presentar al Secretario General <strong>proyectos de convenios</strong> con entidades públicas o privadas para programas de <strong>desarrollo humano</strong>, para aprobación del Procurador.</td><td>Un convenio de capacitación no lo firma la División: lo <strong>propone</strong>, y lo aprueba el Procurador.</td></tr>
          </tbody>
        </table></div>
        <div class="ojo"><b>Ojo en la prueba:</b> fíjate en los verbos del artículo 63 en estos tres numerales: <mark>asesorar</mark>, <mark>contribuir</mark> y <mark>presentar proyectos</mark>. Ninguno es «decidir» ni «aprobar». Es el mismo límite de todo el curso, aplicado aquí: la División propone y ejecuta, el Secretario General y el Procurador deciden. Una opción que diga que la División «aprueba el plan de bienestar» o «suscribe el convenio de capacitación» es incorrecta.</div>
        <h4>Y una regla que vale por varias preguntas: la reinducción tiene consecuencias de carrera</h4>
        <p>Suele verse la reinducción como un trámite formal. En la PGN no lo es: el <strong>artículo 193 del Decreto Ley 262 de 2000</strong> exige, para participar en un <strong>concurso de ascenso</strong>, haber obtenido al menos el <strong>70 %</strong> en los <strong>cursos de reinducción</strong>, además de una calificación igual o superior al 70 % y de no haber sido sancionado disciplinariamente el año anterior. Es decir: el resultado de la reinducción condiciona el ascenso del servidor. Por eso el registro de asistencia y de resultados que usted custodia no es papeleo: es el soporte de un derecho.</p>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Un servidor le pide copia del resultado de su curso de reinducción del año pasado porque quiere presentarse a un concurso de ascenso. Usted consulta el registro y encuentra que la asistencia quedó documentada, pero que el resultado nunca se cargó. No es un detalle administrativo: sin ese dato, el servidor no puede acreditar el requisito del artículo 193 y podría quedar fuera del concurso. Lo que corresponde es dejar constancia del vacío, informarlo de inmediato por el canal para que se reconstruya con los soportes del propio curso, y mantener al servidor informado de los tiempos. Lo que no corresponde es certificar un porcentaje que el registro no respalda.</p>
          </div>
        </div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> en la PGN la División de Gestión Humana <strong>asesora</strong> al Secretario General en políticas de calidad de vida laboral (art. 63, núm. 1), <strong>contribuye</strong> al diseño y aplicación de la inducción y la reinducción (núm. 2) y <strong>presenta proyectos de convenios</strong> de desarrollo humano para aprobación del Procurador (núm. 9). Propone y ejecuta; no aprueba ni suscribe. Y conserva un registro que tiene efectos de carrera: el resultado de la reinducción es requisito para concursar por ascenso (art. 193).</p></div>
      </div>
'''

SEC = base('guias/FUN-GHI-05-gestion-desarrollo-capacitacion-bienestar-sst.html', MOD_PGN, aviso=False)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el plan de '
              'capacitación, la inducción y la reinducción, los programas de bienestar y estímulos, y el Sistema de '
              'Gestión de la Seguridad y Salud en el Trabajo. Varias ponen a prueba el límite entre proponer y decidir.')

P = [
 (1,
  'El jefe de la División le encarga preparar el Plan Institucional de Capacitación del próximo año y le dice que lo arme «con lo del año pasado, cambiándole las fechas», porque el tiempo apremia. Un compañero propone preguntar en cada dependencia qué cursos les gustaría tomar y armar el plan con las respuestas más repetidas. Usted sabe que hubo dos reorganizaciones durante el año, que entraron veinte servidores nuevos y que la entidad adoptó un sistema de información que casi nadie domina todavía.',
  '¿Cómo debe construirse el plan?',
  ['Replicando el plan del año anterior con las fechas actualizadas, porque su contenido ya fue aprobado por el competente y repetirlo garantiza continuidad y ahorra tiempo de formulación.',
   'A partir de un diagnóstico de necesidades que contraste las competencias requeridas con las existentes, incorporando los cambios del año, y sometiéndolo a quien tiene la competencia para aprobarlo.',
   'Con la consolidación de las preferencias de cursos que manifiesten los servidores de cada dependencia, porque son ellos quienes mejor conocen qué formación necesitan para su trabajo diario.',
   'Con los cursos que ofrezcan gratuitamente las entidades con las que ya existen convenios vigentes, de modo que el plan no comprometa recursos adicionales del presupuesto de la entidad.'],
  'Correcto. El plan nace de un <strong>diagnóstico de necesidades</strong>: qué competencias exige la entidad y cuáles tiene, y la brecha entre las dos. Aquí el diagnóstico es evidente —reorganizaciones, personal nuevo, un sistema que nadie domina—, y un plan que ignore eso será papel. Y lo <strong>aprueba el competente</strong>: la División lo propone.',
  'Copiar el plan anterior lo desconecta de la realidad del año. Las preferencias de los servidores son un insumo, no el plan. Y dejar que la oferta gratuita disponible defina el contenido invierte el orden: primero la necesidad, después cómo atenderla.'),

 (0,
  'Un servidor solicita que la entidad le pague la matrícula de una maestría, argumentando que el programa lo hará mejor profesional y que eso beneficia a la Procuraduría. Añade que un compañero recibió el año pasado «un apoyo parecido» para un diplomado. Le pide a usted que incluya la solicitud en el plan de capacitación del próximo año y que le confirme a vuelta de correo si procede, porque las inscripciones de la maestría cierran este mes y no quiere perder el cupo.',
  '¿Cuál es la orientación correcta?',
  ['Explicarle que la capacitación institucional y la educación formal son cosas distintas, con reglas y fuentes de financiación propias, orientarlo sobre la vía que corresponde a su solicitud y radicarla.',
   'Incluir la solicitud en el plan de capacitación del próximo año, porque toda formación que mejore las competencias del servidor hace parte del objeto del plan institucional de capacitación.',
   'Negar la solicitud de plano porque la entidad nunca financia programas de educación formal y no existe vía alguna por la cual un servidor pueda obtener apoyo para estudios de posgrado.',
   'Confirmarle que procede, porque ya existe el antecedente del diplomado del compañero y negarle el mismo tratamiento vulneraría su derecho a la igualdad frente a situaciones equivalentes.'],
  'Correcto. La <strong>capacitación</strong> institucional desarrolla competencias para el desempeño del empleo y se financia con el plan; la <strong>educación formal</strong> conduce a títulos y tiene reglas y fuentes propias —entre ellas las comisiones de estudio, con sus requisitos—. No son lo mismo, y la vía correcta depende de cuál sea.',
  'Meter una maestría en el PIC confunde los instrumentos. Negar de plano desconoce que sí existen vías para la educación formal. Y el antecedente de un diplomado no crea un derecho: pueden ser figuras distintas y, además, un error anterior no obliga a repetirlo.'),

 (2,
  'Entran cinco servidores nuevos el lunes. El jefe de una dependencia le dice a usted que a los suyos «ya les explicó todo en el puesto» y que no necesitan la inducción institucional, porque lo importante es que empiecen a producir. Otro jefe, en cambio, le pregunta si la inducción incluye lo de su dependencia o solo lo general. Usted tiene a la vista el programa institucional, los registros de asistencia de los últimos ciclos y el cronograma de la jornada que estaba prevista para el miércoles.',
  '¿Qué debe precisar?',
  ['Que la inducción en el puesto de trabajo sustituye a la institucional cuando el jefe acredita por escrito que cubrió los mismos contenidos con el servidor recién vinculado.',
   'Que la inducción institucional es opcional y que basta con entregar al servidor el manual de funciones y el reglamento interno para que se entienda cumplida la obligación de la entidad.',
   'Que la inducción institucional integra al servidor a la entidad —su misión, su estructura, sus deberes y su régimen— y se complementa con la del puesto de trabajo, sin que una sustituya a la otra.',
   'Que la inducción solo procede para quienes ingresan por concurso de méritos, de modo que los servidores nombrados en provisionalidad reciben únicamente la orientación de su jefe inmediato.'],
  'Correcto. Son dos niveles que se complementan: la <strong>institucional</strong> integra al servidor a la entidad —misión, estructura, deberes, régimen disciplinario, seguridad y salud— y la del <strong>puesto de trabajo</strong> lo pone al día en sus funciones concretas. El numeral 2 del artículo 63 encarga a la División contribuir al diseño y aplicación del programa.',
  'La explicación del jefe en el puesto no cubre lo institucional, por buena que sea. Entregar documentos no es inducir. Y la inducción no depende de la forma de vinculación: quien entra a la entidad necesita conocerla.'),

 (3,
  'Un servidor tropieza con un cable suelto en el pasillo, alcanza a sostenerse y no se lesiona. Otro, en la misma semana, resbala en una escalera y requiere atención médica. Un compañero le dice a usted que «el primero no se reporta porque no pasó nada» y que el segundo «lo reporta la EPS, no nosotros». El cable sigue suelto y la escalera no tiene cinta antideslizante desde hace meses, y nadie ha reportado antes ninguna de las dos condiciones por el canal previsto.',
  '¿Cuál es la actuación correcta?',
  ['Reportar únicamente el segundo caso, porque solo allí hubo lesión y el sistema de gestión se ocupa de los eventos que efectivamente causan daño a la salud del trabajador.',
   'No reportar ninguno de los dos y limitarse a solicitar el arreglo del cable y la instalación de la cinta, porque corregir la condición peligrosa es lo que realmente previene futuros eventos.',
   'Reportar ambos como accidentes de trabajo, porque los dos ocurrieron en las instalaciones y durante la jornada, de modo que la calificación del origen corresponde en los dos casos a la ARL.',
   'Reportar los dos por los canales previstos —el primero como incidente y el segundo como accidente—, e impulsar que se investiguen y se corrijan las condiciones peligrosas que los causaron.'],
  'Correcto. La distinción es preguntable y es útil: el <strong>incidente</strong> no produjo lesión pero tuvo el potencial de producirla; el <strong>accidente</strong> sí la produjo. Los dos se reportan e investigan, porque el incidente es la advertencia gratuita que permite evitar el accidente. Y aquí la condición peligrosa sigue activa en los dos casos.',
  'Reportar solo el accidente desperdicia la advertencia. Arreglar el cable sin reportar deja el sistema sin el dato que permite detectar patrones. Y llamar accidente al primero es incorrecto: no hubo lesión, y la clasificación importa para la investigación y las estadísticas.'),

 (3,
  'La entidad va a reconocer un estímulo a los mejores servidores del año. Un directivo le sugiere a usted que incluya en la lista a dos personas de su dependencia «que son muy colaboradoras y se lo merecen», aunque no tengan la mejor calificación. Otro propone sortear el estímulo entre quienes tengan calificación sobresaliente, «para que sea justo». Usted tiene a la vista el procedimiento de estímulos vigente y las calificaciones del ciclo.',
  '¿Cuál es la actuación correcta?',
  ['Incluir a las dos personas que sugiere el directivo, porque la colaboración es un aspecto del desempeño que la calificación formal no siempre alcanza a reflejar con precisión.',
   'Sortear el estímulo entre quienes tengan calificación sobresaliente, porque el azar elimina cualquier sospecha de favoritismo y garantiza un trato igual entre quienes cumplen el requisito.',
   'Dejar que cada dependencia escoja internamente a su candidato, porque son los equipos quienes conocen de cerca el aporte real de cada persona durante el año que termina.',
   'Aplicar los criterios objetivos previstos en el procedimiento vigente, documentar cómo se aplicaron a cada caso, y presentar el resultado al competente, dejando constancia de las dos sugerencias recibidas.'],
  'Correcto. Un estímulo mal otorgado hace más daño que no otorgar ninguno, porque le dice a todo el mundo que lo que cuenta no es el desempeño. Por eso se aplican los <strong>criterios objetivos</strong> del procedimiento, se documenta cómo se aplicaron y se presenta al competente. Las sugerencias recibidas se dejan por escrito.',
  'Incluir a alguien por ser «colaborador» sin respaldo en los criterios es favoritismo. El sorteo renuncia al mérito, que es justamente lo que el estímulo reconoce. Y dejar que cada dependencia escoja reproduce el problema a menor escala.'),

 (2,
  'En un comité, un servidor afirma que la política de seguridad y salud en el trabajo «la define el área de Talento Humano, que para eso maneja el tema». Otro sostiene que la política la define la ARL. El jefe de la División le pide a usted precisar el punto antes de que se asuman compromisos, porque la próxima semana debe actualizarse el documento de política y en el comité hay quien propone que la firme el propio jefe de la División para agilizar.',
  '¿Cuál es la precisión correcta?',
  ['La define el área de Talento Humano, porque es la dependencia que conoce las condiciones de trabajo y administra el sistema de gestión dentro de la estructura de la entidad.',
   'La define la ARL, porque es la entidad especializada en riesgos laborales y asesora técnicamente a la organización en la prevención de accidentes y enfermedades de origen laboral.',
   'La define la alta dirección del empleador, que la suscribe y la comunica; el área de Talento Humano la implementa, la documenta y hace seguimiento, y la ARL asesora técnicamente.',
   'No existe obligación de documentar una política escrita cuando la entidad no desarrolla actividades de riesgo alto, de modo que basta con cumplir las medidas de prevención aplicables.'],
  'Correcto. La <strong>política de SST la define y suscribe la alta dirección</strong>: ese es el compromiso que da sustento a todo el sistema. El área de Talento Humano <strong>implementa</strong>, documenta y hace seguimiento, y la ARL <strong>asesora</strong>. Tres papeles distintos que la pregunta mezcla a propósito.',
  'Ni el área ni la ARL definen la política: una la ejecuta y la otra asesora. Y la obligación de tener una política documentada no depende del nivel de riesgo de la entidad.'),

 (0,
  'Se identificó un riesgo por exposición a ruido en un área de la entidad. Un compañero propone resolverlo entregando protectores auditivos a todos los servidores de esa área y dejar constancia firmada de la entrega. Otro propone poner un aviso que recuerde el uso de los protectores. Usted sabe que el ruido proviene de un equipo específico que podría reubicarse o encerrarse, y que la entrega de los protectores ya se hizo el año pasado sin que el ruido disminuyera.',
  '¿Cuál es el enfoque correcto?',
  ['Aplicar la jerarquía de controles: evaluar primero eliminar o sustituir la fuente, luego los controles de ingeniería y administrativos, y dejar los elementos de protección personal como última medida.',
   'Entregar los protectores auditivos con constancia firmada, porque es la medida más rápida, de menor costo y que traslada al servidor la responsabilidad de protegerse durante la jornada.',
   'Instalar avisos de uso obligatorio en el área, porque la señalización es el control administrativo más eficaz y asegura que el servidor recuerde la medida en el momento de la exposición.',
   'Solicitar a la ARL que califique el riesgo y esperar su concepto antes de adoptar cualquier medida, de modo que la decisión quede respaldada técnicamente por la administradora de riesgos.'],
  'Correcto. La <strong>jerarquía de controles</strong> es el corazón de la prevención: primero <strong>eliminar</strong> o <strong>sustituir</strong> la fuente, luego los controles de <strong>ingeniería</strong> —encerrar, aislar, reubicar el equipo—, después los <strong>administrativos</strong> y, <strong>al final</strong>, los elementos de protección personal. Aquí ya se probó el último escalón y el ruido siguió.',
  'Empezar por el EPP invierte la jerarquía y traslada al servidor un riesgo que la entidad podía reducir en la fuente. Un aviso no reduce el ruido. Y esperar a la ARL no exime: la asesoría no reemplaza la obligación de controlar.'),

 (1,
  'Un jefe le pide a usted que le informe qué dijo el examen médico ocupacional de un servidor de su equipo, porque «necesita saber si puede asignarle una tarea pesada». Le dice que no quiere el documento, solo que le cuente lo esencial. El servidor no sabe de esta conversación y el jefe insiste en que es por el bien de él. Usted tiene acceso al archivo donde reposan los certificados de aptitud, y sabe que existe un canal previsto para este tipo de necesidad.',
  '¿Cuál es la actuación correcta?',
  ['Contarle lo esencial sin entregar el documento, porque el jefe tiene una necesidad legítima de organización del trabajo y una explicación verbal no constituye entrega de información reservada.',
   'Explicarle que la historia clínica ocupacional es reservada y pertenece al trabajador, que lo que la entidad recibe es el certificado de aptitud con recomendaciones, y orientarlo sobre cómo obtenerlo.',
   'Entregarle copia del examen porque es el jefe inmediato del servidor y requiere la información para una decisión de asignación de tareas que hace parte de sus funciones de dirección.',
   'Negarse sin más y no dar ninguna orientación, porque cualquier información relacionada con la salud del servidor está prohibida para el empleador y no existe canal alguno para obtenerla.'],
  'Correcto. La <strong>historia clínica ocupacional es reservada</strong> y pertenece al trabajador: el empleador no accede a ella. Lo que sí recibe es el <strong>certificado de aptitud</strong>, que dice si la persona es apta y con qué recomendaciones o restricciones, sin revelar el diagnóstico. Eso es exactamente lo que el jefe necesita, y tiene canal.',
  'Contar «lo esencial» de un dato de salud es revelarlo. Entregar el examen desconoce la reserva. Y negarse sin orientar deja al jefe sin la información que sí puede tener y al servidor expuesto a una asignación inadecuada.'),

 (3,
  'Al cerrar una capacitación, un compañero le propone medir su éxito con la encuesta de satisfacción que llenan los asistentes al final, y presentar ese promedio como resultado del programa. Le dice que así se ha hecho siempre y que los números salen bien. Usted debe presentar el informe de la capacitación al jefe de la División, que preguntará si la formación sirvió para algo en el trabajo y que además debe sustentar con ese informe el presupuesto del plan del próximo año.',
  '¿Cómo debe plantearse la evaluación?',
  ['Con la encuesta de satisfacción de los asistentes, porque mide directamente la percepción de quienes recibieron la formación y es el indicador más confiable de su calidad.',
   'Con el número de servidores que asistieron frente a los convocados, porque la cobertura es lo que demuestra que el plan de capacitación se ejecutó conforme a lo programado.',
   'Con el porcentaje de ejecución presupuestal del programa, porque permite acreditar ante los organismos de control que los recursos asignados se invirtieron en su totalidad.',
   'Con niveles que vayan más allá de la satisfacción: qué aprendieron los participantes, qué cambió en su trabajo y qué efecto tuvo en los resultados del área, además de la asistencia.'],
  'Correcto. La satisfacción mide si la jornada gustó, no si sirvió. Una evaluación útil avanza por niveles: <strong>reacción</strong>, <strong>aprendizaje</strong>, <strong>transferencia</strong> al puesto de trabajo e <strong>impacto</strong> en los resultados. Solo así el diagnóstico del próximo plan se construye sobre algo real.',
  'La satisfacción, la cobertura y la ejecución presupuestal son indicadores de gestión del programa, no de su efecto. Son necesarios, pero ninguno responde la pregunta que hará el jefe: ¿sirvió?'),

 (2,
  'Dos servidores llegan el mismo día a la División. El primero reporta que un equipo de trabajo opera sin la guarda de seguridad y que ya hubo un susto. El segundo relata que un compañero lo trata de manera irrespetuosa de forma reiterada en las reuniones. Un compañero suyo le dice que ambos casos se llevan al COPASST, «que es el comité que ve todo lo del ambiente de trabajo». Los dos servidores piden saber hoy mismo a dónde va su caso.',
  '¿Cuál es la orientación correcta?',
  ['Ambos casos corresponden al COPASST, porque los dos afectan las condiciones en que se desarrolla el trabajo y ese comité es el encargado de velar por el ambiente laboral de la entidad.',
   'Ambos casos corresponden al comité de convivencia laboral, porque los dos involucran la relación entre las personas y la forma en que se organiza y se vive el trabajo en la dependencia.',
   'El primero corresponde al COPASST, que vigila las condiciones de seguridad y salud; el segundo, al comité de convivencia laboral, que atiende las situaciones de acoso y de conflicto interpersonal.',
   'Ninguno corresponde a un comité: el primero debe tramitarse directamente con la ARL y el segundo, mediante una queja disciplinaria contra el compañero que incurre en el trato irrespetuoso.'],
  'Correcto. Son dos comités con objetos distintos y la prueba los confunde a propósito. El <strong>COPASST</strong> vigila las condiciones de seguridad y salud —una guarda retirada es exactamente su materia—. El <strong>comité de convivencia laboral</strong> atiende las situaciones de acoso y los conflictos interpersonales.',
  'Mandar los dos al mismo comité deja uno de ellos sin la instancia adecuada. Y saltarse los comités para ir a la ARL o a lo disciplinario omite las instancias internas que existen precisamente para prevenir y resolver antes.'),

 (1,
  'La entidad va a aplicar la batería de riesgo psicosocial. Un directivo le pide a usted que, cuando tenga los resultados, le entregue los de su dependencia «persona por persona», para saber quién está mal y poder ayudarlos. Le dice que su intención es buena y que como jefe tiene derecho a conocer el estado de su equipo. La aplicación está programada para la próxima semana, varios servidores han preguntado si los resultados son confidenciales y uno dijo que no responderá con sinceridad si su jefe va a verlos.',
  '¿Cuál es la actuación correcta?',
  ['Entregarle los resultados individuales de su dependencia, porque conocer el estado de cada integrante le permite al jefe adoptar medidas de apoyo oportunas y específicas para cada caso.',
   'Explicarle que los resultados individuales son confidenciales y los custodia el profesional competente, que a la entidad se le entregan datos agregados para definir intervenciones, y anunciarlo así a los servidores.',
   'Entregarle los resultados individuales pero sin los nombres, reemplazándolos por números de orden, de modo que pueda ver la distribución de su equipo sin identificar a ninguna persona concreta.',
   'Suspender la aplicación de la batería hasta que todos los servidores firmen una autorización expresa para que sus resultados individuales puedan compartirse con sus respectivos jefes inmediatos.'],
  'Correcto. Los resultados individuales de la evaluación de riesgo psicosocial son <strong>confidenciales</strong> y los custodia el profesional competente; a la entidad se le entregan <strong>datos agregados</strong> que permiten diseñar intervenciones. Y anunciarlo antes de aplicar la batería no es un detalle: de esa confianza depende que la gente responda con la verdad.',
  'Entregar resultados individuales rompe la confidencialidad y arruina el instrumento. La «seudonimización» en un equipo pequeño no protege a nadie. Y pedir autorizaciones para compartir lo que debe ser confidencial desvirtúa la finalidad de la evaluación.'),

 (0,
  'El jefe de la División le encarga gestionar un convenio con una universidad para capacitar al personal en el nuevo sistema de información. Usted negocia las condiciones, consigue un descuento y la universidad le envía el documento listo para firma. Un compañero le dice que lo firme el jefe de la División «y se despacha hoy mismo», porque la capacitación debe empezar el mes entrante, el cupo está reservado y la universidad advirtió que el descuento solo se mantiene si el documento llega esta semana.',
  '¿Cuál es la actuación correcta?',
  ['Presentar el proyecto de convenio al Secretario General, porque el numeral 9 del artículo 63 así lo dispone y su aprobación corresponde al Procurador General, e informar los tiempos reales del trámite.',
   'Hacer que lo firme el jefe de la División, porque fue la dependencia la que negoció las condiciones y dirige el programa de capacitación al que el convenio está destinado.',
   'Firmarlo usted mismo en calidad de responsable de la gestión, dejando constancia de que las condiciones fueron negociadas y aprobadas verbalmente por el jefe de la División.',
   'Iniciar la capacitación con base en el acuerdo verbal alcanzado con la universidad y formalizar el convenio en paralelo, para no perder el cupo reservado para el mes entrante.'],
  'Correcto. El numeral 9 del artículo 63 es explícito: la División <strong>presenta al Secretario General</strong> los proyectos de convenios de desarrollo humano, <strong>para aprobación del Procurador</strong>. Su trabajo termina en un proyecto bien negociado y presentado a tiempo, con los tiempos reales informados a todos.',
  'Ni el jefe de la División ni usted pueden suscribirlo: la competencia está asignada y no se traslada por urgencia. Y empezar la capacitación sin convenio compromete recursos sin respaldo jurídico.'),

 (2,
  'Un servidor le pide copia del resultado de su curso de reinducción del año pasado, porque quiere presentarse a un concurso de ascenso y debe acreditar el requisito. Usted consulta el registro y encuentra la constancia de asistencia, pero el resultado nunca se cargó al sistema. El servidor le dice que él recuerda haber sacado «como noventa» y le pide que certifique eso, porque la inscripción cierra en cinco días y sin el certificado quedaría fuera del concurso de ascenso.',
  '¿Cuál es la actuación correcta?',
  ['Certificar el porcentaje que el servidor recuerda, dejando constancia de que el dato proviene de su manifestación, para que no pierda la oportunidad de inscribirse dentro del término.',
   'Certificar únicamente la asistencia y no mencionar el resultado, porque es el único dato que el registro respalda y el servidor puede acreditar el requisito con esa constancia.',
   'Dejar constancia del vacío, informarlo de inmediato por el canal para que se reconstruya con los soportes del propio curso, mantener al servidor informado de los tiempos y no certificar un dato sin respaldo.',
   'Explicarle que sin el dato en el sistema el requisito no puede acreditarse y que, por lo tanto, no podrá presentarse al concurso de ascenso en esta oportunidad.'],
  'Correcto. El <strong>artículo 193</strong> exige al menos el <strong>70 %</strong> en los cursos de reinducción para concursar por ascenso: el dato faltante puede costarle el concurso. Por eso no se certifica de memoria ni se deja morir: se documenta el vacío, se informa de inmediato para que se reconstruya con los soportes del curso y se mantiene informado al servidor.',
  'Certificar lo que el servidor recuerda es crear un dato falso en un documento que soporta un derecho. Certificar solo la asistencia no acredita el requisito, que exige un porcentaje. Y cerrarle la puerta sin intentar la reconstrucción le quita una oportunidad por un error de la entidad.'),

 (3,
  'En el comité de la División se discute cómo articular las tres líneas del año: capacitación, bienestar y seguridad y salud en el trabajo. Un servidor propone que cada una se maneje por separado «porque son temas distintos y así nadie se enreda». Otro propone unificarlas en un solo plan sin distinguir objetivos. El jefe le pide a usted una propuesta antes del viernes, porque los tres planes deben presentarse juntos al comité institucional y allí preguntarán cómo se relacionan entre sí.',
  '¿Cuál es el planteamiento correcto?',
  ['Manejar las tres por separado, porque tienen fundamentos normativos distintos y mezclarlas dificulta demostrar el cumplimiento específico de cada obligación ante los organismos de control.',
   'Unificarlas en un solo plan con un presupuesto común, porque las tres buscan el bienestar del servidor y separarlas duplica gestiones, reuniones y reportes sin ningún beneficio práctico.',
   'Priorizar la seguridad y salud en el trabajo y subordinar a ella las otras dos, porque es la única de las tres cuyo incumplimiento acarrea sanciones directas para la entidad empleadora.',
   'Conservar los objetivos y el fundamento propio de cada una, pero articularlas con un ciclo común de planear, hacer, verificar y actuar, y con un diagnóstico que alimente a las tres.'],
  'Correcto. Ni aisladas ni fundidas: <strong>articuladas</strong>. Cada una conserva su objeto y su fundamento normativo, pero comparten el ciclo <strong>PHVA</strong> y se alimentan del mismo diagnóstico. Un riesgo psicosocial detectado por el SG-SST puede atenderse con una acción de bienestar y con una capacitación en manejo del estrés: esa es la articulación.',
  'Manejarlas por separado desaprovecha información que las tres necesitan. Fundirlas borra obligaciones específicas que deben poder acreditarse. Y subordinar dos a la tercera convierte el bienestar y la capacitación en apéndices de la SST.'),

 (1,
  'Un servidor sufre un accidente en las instalaciones un viernes a las 4 de la tarde. El jefe de la División está de vacaciones, el servidor ya fue atendido y se encuentra estable en su casa. Un compañero le dice a usted que el reporte «se hace el lunes, que total ya pasó y el término seguro es de varios días». Otro, que como la persona está bien, «con el registro interno basta». Usted no recuerda con exactitud el término de reporte a la ARL y a la EPS.',
  '¿Cuál es la actuación correcta?',
  ['Esperar al lunes y reportar con el jefe presente, porque un reporte hecho sin su visto bueno podría contener errores que después resulten difíciles de corregir ante la ARL.',
   'Verificar de inmediato el término aplicable, reportar dentro de él a la ARL y a la EPS por los canales previstos, informar a quien esté encargado y dejar constancia de lo actuado.',
   'Registrar el caso internamente y esperar a que el servidor regrese para confirmar con él si desea que el accidente se reporte como de origen laboral ante la administradora de riesgos.',
   'Reportar solo a la EPS, porque fue la entidad que prestó la atención médica, y dejar que sea ella la que traslade la información a la ARL si considera que el origen pudo ser laboral.'],
  'Correcto. El reporte de un accidente de trabajo tiene <strong>término perentorio</strong> y no espera a que el jefe vuelva de vacaciones. Lo que corresponde es verificarlo —no adivinarlo—, reportar dentro de él a la ARL y a la EPS, informar a quien esté encargado y dejar constancia.',
  'Esperar al lunes puede consumir el término y afectar las prestaciones del servidor. El registro interno no reemplaza el reporte. Y el reporte no depende de la voluntad del trabajador ni se delega en la EPS: es una obligación del empleador.'),

]
