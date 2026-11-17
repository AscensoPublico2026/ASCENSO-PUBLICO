# -*- coding: utf-8 -*-
"""Eje: Derecho disciplinario (Ley 1952 de 2019, reformada por la Ley 2094 de 2021).

Formato oficial de juicio situacional: un caso con datos concretos y tres
opciones de respuesta, todas defendibles. La justificación no va dentro de la
opción sino en la explicación que el aspirante lee al terminar.
"""

DIS = "Derecho disciplinario"

BANCO = [
dict(
    tema="Norma disciplinaria aplicable", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="Al revisar un proyecto de auto, usted encuentra que el sustanciador cita la Ley 734 de 2002 como norma aplicable a una conducta ocurrida en marzo del año pasado. El investigado es un servidor de carrera de una alcaldía y la queja se radicó en agosto. El sustanciador explica que esa es la norma con la que se formó y la que mejor conoce.",
    q="¿Qué estatuto disciplinario debe aplicarse?",
    ops=[
        "La Ley 1952 de 2019, Código General Disciplinario, con la reforma que le introdujo la Ley 2094 de 2021 y la corrección del Decreto 1656.",
        "La Ley 734 de 2002, que conserva su vigencia para los servidores de carrera administrativa de las entidades del orden territorial.",
        "La Ley 1474 de 2011, Estatuto Anticorrupción, que recogió el régimen disciplinario aplicable a los servidores públicos.",
    ],
    correcta=0,
    expl=[
        "Correcto: el Código General Disciplinario rige desde el 29 de marzo de 2022, y la conducta del caso es posterior. La Ley 734 solo se aplica por favorabilidad o a procesos regidos por ella.",
        "La Ley 734 fue derogada por el Código General Disciplinario y no sobrevive para ningún nivel de la administración.",
        "La Ley 1474 es el Estatuto Anticorrupción y algunas de sus disposiciones disciplinarias fueron derogadas; nunca fue el estatuto disciplinario general.",
    ],
),

dict(
    tema="Ilicitud sustancial", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Un servidor diligenció un formato interno de seguimiento con dos días de retraso frente al procedimiento documentado. El trámite al que correspondía se cumplió dentro del término legal, ningún usuario resultó afectado y la finalidad del control se satisfizo igual. La oficina de control interno pide abrir investigación por incumplimiento del procedimiento.",
    q="¿Qué debe analizarse antes de considerar que hay falta disciplinaria?",
    ops=[
        "Si el servidor registra antecedentes disciplinarios que permitan valorar la reiteración de la conducta reprochada.",
        "La ilicitud sustancial, esto es, si la conducta afectó sustancialmente el deber funcional sin justificación.",
        "Si el jefe inmediato presentó queja formal, requisito sin el cual la actuación disciplinaria no puede iniciarse.",
    ],
    correcta=1,
    expl=[
        "Los antecedentes inciden en la graduación de la sanción, no en la existencia misma de la falta.",
        "Correcto: la tipicidad formal no basta. Sin afectación sustancial del deber funcional la conducta no es sustancialmente ilícita.",
        "La acción disciplinaria puede iniciarse de oficio; la queja no es requisito de procedibilidad.",
    ],
),

dict(
    tema="Clasificación de las faltas", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="basic",
    ctx="En la inducción de un grupo de servidores recién posesionados en una procuraduría regional, alguien pregunta cómo se clasifican las faltas disciplinarias y si el dolo es una de esas categorías. El expositor quiere dejar clara la diferencia entre la clasificación de la falta y la forma de culpabilidad.",
    q="¿Cuál es la clasificación que establece el Código General Disciplinario?",
    ops=[
        "Dolosas y culposas, categorías que determinan directamente la sanción que corresponde imponer al investigado.",
        "Formales y sustanciales, según la conducta afecte el procedimiento documentado o el deber funcional propio del servidor investigado.",
        "Gravísimas, graves y leves, categorías que luego se cruzan con la forma de culpabilidad para determinar la sanción aplicable.",
    ],
    correcta=2,
    expl=[
        "El dolo y la culpa son formas de culpabilidad que se analizan después de calificar la falta, no clases de falta.",
        "Esa no es una clasificación legal de las faltas; lo sustancial se refiere a la ilicitud, que es otra categoría.",
        "Correcto: gravísimas, graves y leves. La combinación de esa calificación con la forma de culpabilidad determina la sanción.",
    ],
),

dict(
    tema="Sanción según falta y culpabilidad", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Concluido el juzgamiento, se acreditó que un profesional universitario incurrió en una falta calificada como gravísima, y que lo hizo a título de culpa grave: no hubo dolo ni culpa gravísima. El investigado no tiene antecedentes y reparó parcialmente el daño antes del fallo.",
    q="¿Qué sanción corresponde imponer?",
    ops=[
        "Destitución e inhabilidad general, que es la sanción que el Código prevé para todas las faltas calificadas como gravísimas.",
        "Suspensión en el ejercicio del cargo e inhabilidad especial, por el término que el fallo fije dentro del rango previsto en la ley.",
        "Multa, porque la culpa grave recibe en el Código el mismo tratamiento que las faltas leves cometidas con dolo.",
    ],
    correcta=1,
    expl=[
        "La destitución e inhabilidad general se reserva a las gravísimas dolosas o realizadas con culpa gravísima.",
        "Correcto: la combinación de falta gravísima con culpa conduce a suspensión e inhabilidad especial, igual que la grave dolosa.",
        "La multa corresponde a las faltas leves dolosas; el grado de culpa no modifica la calificación de la falta.",
    ],
),

dict(
    tema="Límites de la inhabilidad general", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="Revisando un proyecto de fallo que impone destitución e inhabilidad general, usted debe verificar que el término esté dentro del marco legal. El proyecto propone veinticinco años con fundamento en la gravedad de la conducta y en el perjuicio causado a la entidad.",
    q="¿Entre qué límites se mueve la inhabilidad general?",
    ops=[
        "Entre uno y cinco años, prorrogables hasta por el doble cuando concurran circunstancias de agravación punitiva en el caso.",
        "Entre treinta días y doce meses, según la gravedad de la falta y los criterios de graduación del Código.",
        "Entre diez y veinte años, término que el fallo debe motivar aplicando los criterios de graduación previstos en el Código.",
    ],
    correcta=2,
    expl=[
        "Ese rango no corresponde a la inhabilidad general y el Código no prevé una prórroga de esa naturaleza.",
        "Ese es el rango de la inhabilidad especial, que acompaña a la suspensión en el ejercicio del cargo.",
        "Correcto: el Código fija la inhabilidad general entre diez y veinte años, de modo que los veinticinco del proyecto exceden el máximo legal.",
    ],
),

dict(
    tema="Sujetos disciplinables particulares", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Un interventor contratado por una entidad para vigilar la construcción de un puente certificó el recibo a satisfacción de obras que, según el informe técnico posterior, nunca se ejecutaron. El interventor es una persona natural vinculada por contrato de prestación de servicios y alega que no es servidor público.",
    q="¿Puede ser sujeto de control disciplinario?",
    ops=[
        "No, mientras no exista sentencia penal condenatoria que acredite la falsedad de las certificaciones que suscribió.",
        "No, porque el régimen disciplinario se aplica únicamente a quienes tienen la calidad de servidores públicos.",
        "Sí: los particulares que cumplen labores de interventoría en contratos estatales son disciplinables.",
    ],
    correcta=2,
    expl=[
        "La acción disciplinaria es autónoma frente a la penal y no depende de una condena previa.",
        "La calidad de servidor no es la única puerta de entrada al control disciplinario.",
        "Correcto: el Código prevé el régimen de los particulares disciplinables e incluye expresamente a interventores y supervisores.",
    ],
),

dict(
    tema="Independencia de la acción disciplinaria", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="El apoderado de un investigado solicita que se suspenda el proceso disciplinario hasta que termine el proceso penal que se adelanta por los mismos hechos. Argumenta que una eventual absolución penal haría desaparecer el fundamento de la actuación disciplinaria y que seguir adelante sería un desgaste.",
    q="¿Procede esa suspensión como regla general?",
    ops=[
        "Sí, siempre que el delito investigado tenga prevista pena privativa de la libertad superior a cuatro años.",
        "No: la acción disciplinaria es autónoma e independiente de la penal, y cada una se adelanta conforme a sus propias reglas.",
        "Sí, porque la decisión penal constituye prejudicialidad y vincula al operador disciplinario en la valoración de la prueba.",
    ],
    correcta=1,
    expl=[
        "La pena prevista para el delito no determina la suspensión del proceso disciplinario.",
        "Correcto: lo que se juzga es distinto —el deber funcional—, de modo que la absolución penal no implica por sí sola la absolución disciplinaria.",
        "No existe prejudicialidad penal general en materia disciplinaria.",
    ],
),

dict(
    tema="Indagación previa: finalidad", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="Llega una queja anónima que describe con detalle un presunto cobro irregular en una oficina de atención, pero no identifica al autor ni aporta fecha exacta. Adjunta una fotografía del aviso de tarifas y el nombre de la dependencia. No es posible saber todavía si la conducta ocurrió.",
    q="¿Qué figura procede?",
    ops=[
        "La indagación previa, que busca verificar la ocurrencia de la conducta e identificar al posible autor.",
        "El archivo de plano de la queja, porque el anonimato impide individualizar al disciplinado y vincularlo al proceso.",
        "La formulación inmediata de pliego de cargos contra el jefe de la dependencia señalada en la queja anónima.",
    ],
    correcta=0,
    expl=[
        "Correcto: esa es exactamente la finalidad de la indagación previa cuando falta identificación del autor o certeza sobre el hecho.",
        "El anonimato no obliga a archivar cuando la queja aporta elementos concretos y verificables, como ocurre aquí.",
        "El pliego de cargos exige prueba que permita formular una imputación concreta contra una persona determinada.",
    ],
),

dict(
    tema="Término de la indagación previa", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Una indagación previa lleva catorce meses abierta sin que se haya adoptado decisión alguna. El expediente registra dos cambios de sustanciador y una solicitud de información a otra entidad que nunca se reiteró. El indagado presenta derecho de petición preguntando en qué va su caso.",
    q="¿Qué problema jurídico hay?",
    ops=[
        "Ninguno: la indagación previa carece de término legal y se extiende hasta que se recauden todos los elementos necesarios.",
        "Se trata de un asunto de gestión interna, sin consecuencia jurídica mientras no se haya formulado pliego de cargos.",
        "Se superó el término máximo de seis meses que el Código fija para la indagación previa, y la etapa se prolongó de manera irregular.",
    ],
    correcta=2,
    expl=[
        "La indagación previa sí tiene un término legal máximo, precisamente para que la etapa no se vuelva indefinida.",
        "La superación del término tiene consecuencias jurídicas y puede comprometer disciplinariamente al instructor.",
        "Correcto: el límite es de seis meses, y prolongarla afecta el debido proceso y la seguridad jurídica del indagado.",
    ],
),

dict(
    tema="Separación entre instrucción y juzgamiento", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="El mismo funcionario que adelantó la investigación, practicó las pruebas y formuló el pliego de cargos pretende ahora dictar el fallo de primera instancia. Sostiene que conoce el expediente mejor que nadie y que el investigado no ha objetado nada al respecto.",
    q="¿Es admisible bajo el Código General Disciplinario reformado?",
    ops=[
        "Sí, siempre que el investigado no formule objeción expresa dentro del término de traslado del pliego de cargos.",
        "No: la reforma garantiza que el funcionario que instruye la actuación no sea el mismo que la juzga y profiere el fallo.",
        "Sí, puesto que la separación entre instrucción y juzgamiento solo rige para las faltas que se califican como gravísimas.",
    ],
    correcta=1,
    expl=[
        "La garantía de imparcialidad no es renunciable por el investigado ni depende de que la objete.",
        "Correcto: la separación entre instrucción y juzgamiento es uno de los ejes de la Ley 2094 de 2021 y desarrolla el debido proceso.",
        "La separación no distingue según la gravedad de la falta: rige para toda la actuación disciplinaria.",
    ],
),

dict(
    tema="Doble instancia y control judicial", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Un servidor sancionado con suspensión e inhabilidad especial pregunta qué posibilidades tiene de controvertir el fallo. Su abogado le dijo que la decisión disciplinaria es definitiva y que lo único que queda es acudir a instancias internacionales.",
    q="¿Qué le explica usted?",
    ops=[
        "Que solo puede acudir al sistema interamericano de derechos humanos, por tratarse de una sanción de un órgano de control.",
        "Que procede la doble instancia dentro de la actuación y el control jurisdiccional ante lo contencioso administrativo.",
        "Que su única alternativa es solicitar la revocatoria directa del fallo ante el Procurador General de la Nación.",
    ],
    correcta=1,
    expl=[
        "El sistema interamericano es subsidiario y exige agotar previamente los recursos internos disponibles.",
        "Correcto: la reforma reforzó la doble instancia y el control jurisdiccional de las sanciones disciplinarias.",
        "La revocatoria directa existe como mecanismo excepcional, pero no es la única vía ni la principal.",
    ],
),

dict(
    tema="Derechos del investigado", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="Un investigado solicita copia íntegra del expediente y pide que se practiquen tres testimonios que, según afirma, demuestran que actuó siguiendo una instrucción escrita de su superior. El sustanciador considera que el expediente es reservado y que las pruebas dilatarían la actuación.",
    q="¿Cómo debe procederse?",
    ops=[
        "Negar ambas solicitudes, pues la reserva del expediente cobija también al investigado hasta el fallo de primera instancia que se profiera.",
        "Conceder el acceso al expediente y negar en bloque las pruebas, para no comprometer el término de la investigación.",
        "Permitir el acceso al expediente y resolver motivadamente la solicitud de pruebas, decretando las que resulten procedentes.",
    ],
    correcta=2,
    expl=[
        "La reserva opera frente a terceros, no frente al sujeto procesal, que necesita el expediente para defenderse.",
        "Negar las pruebas en bloque y sin motivación vulnera el derecho de defensa, por apremiante que sea el término.",
        "Correcto: se decretan las conducentes, pertinentes y útiles, y se niegan las demás con motivación expresa.",
    ],
),

dict(
    tema="Prueba ilícita", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="En el expediente aparece la grabación de una conversación privada del investigado, obtenida por un compañero sin su consentimiento y sin orden judicial. La grabación es el único elemento que acreditaría el acuerdo irregular que se le imputa y su contenido es inequívoco.",
    q="¿Qué debe hacerse con esa prueba?",
    ops=[
        "Excluirla de la actuación por haberse obtenido con violación del debido proceso, sin que pueda fundar la decisión de fondo.",
        "Valorarla junto con el resto del acervo probatorio, dado que acredita de manera inequívoca la ocurrencia de la conducta investigada.",
        "Remitirla a la Fiscalía para que determine su licitud y, mientras tanto, valorarla dentro del proceso disciplinario.",
    ],
    correcta=0,
    expl=[
        "Correcto: el artículo 29 de la Constitución declara nula de pleno derecho la prueba obtenida con violación del debido proceso.",
        "La utilidad probatoria no sanea el origen ilícito, por contundente que resulte el contenido de la grabación.",
        "Remitirla a otra autoridad no la convierte en prueba válida dentro de la actuación disciplinaria.",
    ],
),

dict(
    tema="Presunción de inocencia y carga de la prueba", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="En un proyecto de fallo se lee la siguiente consideración: «como el investigado no logró demostrar que actuó conforme al procedimiento, se impondrá la sanción correspondiente». El expediente contiene dos testimonios contradictorios y ningún documento que acredite la conducta imputada.",
    q="¿Cuál es el error del razonamiento?",
    ops=[
        "Que omitió citar la norma presuntamente infringida junto con la consideración sobre la conducta del investigado.",
        "Que invierte la carga de la prueba y desconoce la presunción de inocencia que ampara al investigado durante toda la actuación.",
        "Que se trata de un defecto de redacción corregible en el fallo de segunda instancia, sin que afecte la validez de la decisión.",
    ],
    correcta=1,
    expl=[
        "La cita de la norma también es necesaria, pero no es el vicio que compromete la decisión.",
        "Correcto: la administración debe demostrar la falta y la responsabilidad, y la duda razonable se resuelve a favor del investigado.",
        "Es un error sustancial sobre las reglas de la prueba, no un problema de forma subsanable.",
    ],
),

dict(
    tema="Caducidad de la acción disciplinaria", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Se recibe una queja por hechos ocurridos hace más de seis años, sin que se hubiera iniciado actuación alguna en ese tiempo. El quejoso aporta documentos de la época y sostiene que apenas ahora conoció la irregularidad. La conducta descrita se agotó en un solo acto.",
    q="¿Qué figura debe analizarse antes de cualquier otra cosa?",
    ops=[
        "La caducidad de la acción disciplinaria, que impide iniciar la actuación transcurrido el término legal.",
        "La prescripción de la sanción disciplinaria, que extingue la posibilidad de hacerla efectiva una vez impuesta.",
        "La cosa juzgada, que impide volver sobre hechos que ya fueron objeto de pronunciamiento de fondo anterior.",
    ],
    correcta=0,
    expl=[
        "Correcto: la caducidad se cuenta desde la ocurrencia de la conducta e impide iniciar la acción, con independencia de cuándo se conoció.",
        "La prescripción de la sanción opera sobre una sanción ya impuesta, supuesto que aquí no se ha presentado.",
        "No hay cosa juzgada si nunca existió una decisión previa sobre estos hechos.",
    ],
),

dict(
    tema="Conductas de ejecución permanente", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Un servidor dejó de rendir un informe obligatorio durante tres años consecutivos. La omisión se mantuvo desde enero del primer año hasta diciembre del tercero, cuando fue trasladado de dependencia. La queja se radica dos años después de ese traslado.",
    q="¿Desde cuándo se cuenta el término para la acción disciplinaria?",
    ops=[
        "Desde el primer día en que debió rendirse el informe, que es el momento en que se configuró el incumplimiento del deber.",
        "Desde la realización del último acto o desde el día en que cesó la conducta, tratándose de una omisión que se prolongó en el tiempo.",
        "Desde que la entidad tuvo conocimiento efectivo de la omisión y estuvo en condiciones de iniciar la actuación.",
    ],
    correcta=1,
    expl=[
        "Tomar solo el primer incumplimiento desconoce que la conducta se prolongó en el tiempo de manera continuada.",
        "Correcto: en las conductas de ejecución permanente o continuada el término corre desde el último acto o desde que cesó.",
        "El momento del conocimiento por parte de la entidad no es el punto de partida que fija la ley.",
    ],
),

dict(
    tema="Faltas gravísimas y solicitud de dádivas", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="Un servidor de una oficina de atención le pide a un usuario doscientos mil pesos para «agilizar» el trámite de un certificado que, según el procedimiento, debía expedirse en cinco días y sin costo adicional. El usuario entrega el dinero y el certificado se expide al día siguiente.",
    q="¿Cómo se califica disciplinariamente la conducta?",
    ops=[
        "Falta grave cometida con culpa, por tratarse de un descuido en la aplicación del procedimiento de atención al usuario del servicio.",
        "Falta gravísima, por tratarse de la solicitud de dádiva o de provecho indebido con ocasión de las funciones del servidor.",
        "No constituye falta disciplinaria, sino exclusivamente un delito cuya investigación corresponde a la Fiscalía General.",
    ],
    correcta=1,
    expl=[
        "No hay descuido alguno: la conducta es deliberada y está dirigida a obtener un provecho personal.",
        "Correcto: pedir o recibir dádivas con ocasión de las funciones está entre las faltas gravísimas del Código.",
        "Es simultáneamente falta disciplinaria y posible delito; las dos vías son autónomas y pueden adelantarse a la vez.",
    ],
),

dict(
    tema="Criterios de graduación de la sanción", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Acreditada la falta y la responsabilidad, debe definirse el monto de la sanción dentro del rango legal. El investigado confesó desde la indagación previa, reparó el daño causado a la entidad antes del fallo y no registra antecedentes disciplinarios en veintidós años de servicio.",
    q="¿Qué criterios resultan pertinentes para graduar la sanción?",
    ops=[
        "Únicamente el salario básico mensual devengado por el investigado al momento de la comisión de la conducta reprochada.",
        "El grado de culpabilidad, el perjuicio causado, los antecedentes, el resarcimiento del daño y la confesión.",
        "El tiempo que tomó la investigación y la carga de trabajo del despacho que adelantó la actuación disciplinaria.",
    ],
    correcta=1,
    expl=[
        "El salario incide en la tasación de la multa, pero no es el único criterio ni opera en las demás sanciones.",
        "Correcto: el Código enumera criterios de atenuación y agravación que deben valorarse y motivarse expresamente en el fallo.",
        "La duración del trámite y la carga del despacho no son criterios legales de graduación de la sanción.",
    ],
),

dict(
    tema="Suspensión provisional del investigado", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="En una investigación por hechos graves, el investigado continúa en su cargo de jefe de oficina, tiene acceso directo al expediente físico que reposa en su dependencia y los tres testigos citados son sus subalternos. Dos de ellos ya manifestaron temor a declarar.",
    q="¿Qué medida prevé el Código para esa situación?",
    ops=[
        "El traslado definitivo del investigado a otra dependencia, para separarlo del expediente y de los testigos citados.",
        "La terminación anticipada de la actuación, mientras se restablecen las condiciones que permitan recaudar la prueba.",
        "La suspensión provisional del investigado, cuando existan serios elementos de juicio sobre la interferencia.",
    ],
    correcta=2,
    expl=[
        "El traslado definitivo no es una medida del proceso disciplinario y comprometería la situación laboral del investigado.",
        "La terminación anticipada no responde al riesgo descrito y dejaría los hechos sin esclarecer.",
        "Correcto: es una medida cautelar excepcional, motivada y temporal, prevista justamente para este tipo de riesgo.",
    ],
),

dict(
    tema="Pliego de cargos: contenido", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Revisa un pliego de cargos que describe con detalle los hechos y relaciona las pruebas recaudadas, pero no indica cuál es la norma presuntamente infringida ni a qué título se imputa la conducta. El sustanciador sostiene que eso se precisará en el fallo, cuando se tenga el panorama completo.",
    q="¿Qué problema tiene ese pliego?",
    ops=[
        "Es deficiente: debe contener la norma presuntamente infringida y la forma de culpabilidad que se imputa al investigado.",
        "Carece únicamente de la firma del funcionario competente, defecto que se subsana con la suscripción posterior del documento.",
        "No tiene problema alguno, pues la descripción detallada de los hechos y la relación de pruebas satisfacen la exigencia legal.",
    ],
    correcta=0,
    expl=[
        "Correcto: sin norma infringida ni forma de culpabilidad el investigado no sabe de qué debe defenderse, y el pliego delimita el juzgamiento.",
        "La firma es un requisito formal adicional, pero no es el defecto que compromete el derecho de defensa.",
        "La narración de los hechos no permite ejercer defensa si no se sabe cuál es la imputación jurídica.",
    ],
),

dict(
    tema="Congruencia entre cargos y fallo", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="El pliego de cargos imputó la conducta a título de culpa grave. Tras los descargos y la práctica de pruebas, el proyecto de fallo la sanciona como dolosa, con el consiguiente agravamiento de la sanción. No se varió el pliego ni se corrió traslado al investigado sobre esa nueva calificación.",
    q="¿Qué principio se desconoce?",
    ops=[
        "La economía procesal, pues variar el pliego habría prolongado innecesariamente una actuación ya suficientemente ilustrada.",
        "El principio de congruencia, conforme al cual el fallo debe corresponder a los cargos que se formularon al investigado.",
        "La publicidad, porque la nueva calificación no fue dada a conocer mediante la notificación oportuna del proyecto de fallo.",
    ],
    correcta=1,
    expl=[
        "La economía procesal no justifica sorprender al investigado con una imputación más gravosa que no pudo controvertir.",
        "Correcto: agravar la imputación exige variar previamente el pliego para permitir la defensa sobre la nueva calificación.",
        "La publicidad se refiere al conocimiento de las actuaciones; aquí lo vulnerado es la congruencia y la defensa.",
    ],
),

dict(
    tema="Archivo por causal de exclusión", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="Concluida la indagación, está demostrado que la conducta ocurrió y que el servidor la ejecutó. También quedó plenamente acreditado, con la orden escrita y el concepto jurídico que la respaldaba, que actuó en estricto cumplimiento de un deber legal que le imponía esa actuación.",
    q="¿Qué decisión procede?",
    ops=[
        "Formular pliego de cargos para que el investigado alegue la causal en la etapa de descargos y esta se valore en el fallo.",
        "Imponer amonestación escrita, por haberse comprobado la ocurrencia material de la conducta objeto de la queja.",
        "Archivar la actuación por estar plenamente acreditada una causal de exclusión de responsabilidad disciplinaria.",
    ],
    correcta=2,
    expl=[
        "Formular cargos cuando la causal ya está plenamente demostrada es un desgaste innecesario y lesivo para el investigado.",
        "Acreditada una causal de exclusión de responsabilidad no hay lugar a sanción alguna, ni siquiera la más leve.",
        "Correcto: demostrada la causal, la decisión que corresponde es el archivo de la actuación.",
    ],
),

dict(
    tema="Queja sin hechos nuevos", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="Un ciudadano presenta por sexta vez la misma queja contra el mismo servidor, por hechos que fueron archivados mediante decisión en firme hace dos años. No aporta pruebas ni hechos nuevos: reitera los mismos documentos y agrega que no está de acuerdo con el archivo anterior.",
    q="¿Cuál es la actuación correcta?",
    ops=[
        "Resolver indicando que los hechos ya fueron objeto de decisión en firme y que no se aportan elementos nuevos.",
        "Iniciar una nueva actuación disciplinaria, pues toda queja ciudadana obliga a abrir investigación por mandato legal.",
        "Dar traslado de la queja al propio servidor señalado, para que sea él quien responda directamente al ciudadano.",
    ],
    correcta=0,
    expl=[
        "Correcto: existiendo decisión en firme y sin hechos ni pruebas nuevas no hay lugar a reabrir la actuación.",
        "No toda queja obliga a abrir investigación: debe valorarse si aporta mérito para iniciar la actuación.",
        "Trasladarle la queja al propio investigado para que la conteste es improcedente y compromete la imparcialidad.",
    ],
),

dict(
    tema="Revelación de información reservada", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="intermediate",
    ctx="Un servidor comparte en un grupo de mensajería con cinco compañeros la identidad de un quejoso cuya protección se había dispuesto, junto con capturas de dos piezas del expediente. El grupo es privado, nadie ajeno a la entidad lo integra y el servidor afirma que lo hizo para pedir una opinión técnica.",
    q="¿Cómo se valora la conducta?",
    ops=[
        "Es irrelevante disciplinariamente, por haberse producido en un canal privado entre servidores de la misma entidad.",
        "Compromete la reserva de la actuación y el deber de custodia de la información que el servidor conoce por razón del cargo.",
        "Solo sería reprochable si la información llegara a publicarse en un medio de comunicación o en una red social de acceso abierto.",
    ],
    correcta=1,
    expl=[
        "El carácter privado del canal no desvirtúa la infracción del deber de reserva ni la exposición del quejoso protegido.",
        "Correcto: el deber se incumple por la divulgación misma, sea cual sea el medio y sea cual sea la intención.",
        "El medio amplifica el daño, pero no es lo que determina la existencia de la falta.",
    ],
),

dict(
    tema="Favorabilidad en materia disciplinaria", ref="PGN-DIS",
    refT="Derecho disciplinario", nivel="advanced",
    ctx="Una conducta ocurrió en 2021, bajo la vigencia de la Ley 734 de 2002, y el proceso se adelanta hoy. Para ese supuesto, la norma actual prevé un tratamiento más benigno: califica la falta en un grado menor y reduce el rango de la sanción aplicable al caso.",
    q="¿Qué norma debe aplicarse?",
    ops=[
        "La vigente al momento de los hechos, en aplicación del principio de irretroactividad de la ley sancionadora.",
        "La norma posterior, por ser la que se encuentra vigente al momento de adoptar la decisión de fondo del asunto.",
        "La más favorable al investigado, en aplicación del principio de favorabilidad propio del derecho sancionador.",
    ],
    correcta=2,
    expl=[
        "La irretroactividad cede ante la favorabilidad, que es una garantía propia del derecho sancionador.",
        "La norma posterior se aplica si resulta más favorable, no por el solo hecho de ser posterior.",
        "Correcto: la favorabilidad rige plenamente en materia disciplinaria y obliga a escoger el tratamiento más benigno.",
    ],
),

]
