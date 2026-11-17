# -*- coding: utf-8 -*-
"""Ejes: Procedimiento administrativo (CPACA). Contratación estatal.
Integridad y conflicto de interés."""

CPA = "Procedimiento administrativo (CPACA)"
CTR = "Contratación estatal"
INT = "Integridad, conflicto de interés y transparencia"

BANCO = [
dict(
    tema="Formas de iniciación de la actuación", ref="PGN-CPA",
    refT="Procedimiento administrativo (CPACA)", nivel="basic",
    ctx="En una capacitación sobre el CPACA, un servidor sostiene que una entidad solo puede iniciar actuaciones administrativas cuando un ciudadano se lo solicita, y que sin solicitud no hay actuación posible. Un compañero replica que la entidad también puede abrir trámites por su cuenta cuando advierte una irregularidad.",
    q="¿Cómo se inician las actuaciones administrativas?",
    ops=[
        "Únicamente a petición de parte interesada, que es quien impulsa el trámite y delimita su objeto desde el comienzo del asunto.",
        "Por quienes ejerciten el derecho de petición, por quienes cumplan un deber legal, o de oficio por las autoridades.",
        "Únicamente de oficio, pues la administración conserva siempre la iniciativa sobre los trámites que adelanta.",
    ],
    correcta=1,
    expl=[
        "La petición de parte no es la única vía; la administración puede y debe actuar de oficio en muchos supuestos.",
        "Correcto: el CPACA prevé esas tres formas de iniciación, que no se excluyen entre sí.",
        "La iniciación de oficio es una de las formas previstas, pero no desplaza al derecho de petición del ciudadano.",
    ],
),

dict(
    tema="Silencio administrativo negativo", ref="PGN-CPA",
    refT="Procedimiento administrativo (CPACA)", nivel="advanced",
    ctx="Venció el término para resolver una petición y la entidad no se pronunció. El peticionario pregunta si eso significa que su solicitud quedó aprobada por el solo paso del tiempo, y si la entidad queda relevada de responderle ahora que el término pasó.",
    q="¿Cuál es la regla general en el CPACA?",
    ops=[
        "El silencio equivale a una decisión favorable al peticionario, que puede exigir su cumplimiento ante la entidad.",
        "La regla general es el silencio administrativo negativo: se entiende negada la petición presentada por el interesado.",
        "El silencio deja sin efectos la petición, de modo que el interesado debe volver a radicarla para reactivar el trámite.",
    ],
    correcta=1,
    expl=[
        "El silencio positivo es excepcional y requiere norma expresa que lo consagre para ese trámite en particular.",
        "Correcto: habilita acudir a la jurisdicción, sin que la autoridad quede relevada de su deber de resolver.",
        "La petición no se anula por el silencio ni obliga al ciudadano a radicarla de nuevo.",
    ],
),

dict(
    tema="Recursos en vía administrativa", ref="PGN-CPA",
    refT="Procedimiento administrativo (CPACA)", nivel="intermediate",
    ctx="Un ciudadano recibió ayer la notificación personal de un acto administrativo de carácter particular que le negó una autorización. Quiere controvertirlo sin acudir todavía a un juez y pregunta de qué recursos dispone dentro de la propia actuación administrativa.",
    q="¿Qué recursos proceden?",
    ops=[
        "Reposición ante quien expidió el acto, apelación ante el superior y queja cuando se rechaza la apelación.",
        "Únicamente el de apelación ante el superior jerárquico, que revisa integralmente la decisión adoptada en primera instancia.",
        "Únicamente la revocatoria directa, que puede solicitarse en cualquier tiempo mientras el acto no haya sido ejecutado.",
    ],
    correcta=0,
    expl=[
        "Correcto: esos son los recursos que el CPACA prevé dentro de la actuación administrativa.",
        "La apelación no es el único recurso disponible: la reposición y la queja también proceden según el caso.",
        "La revocatoria directa no es un recurso sino un mecanismo distinto, con causales y efectos propios.",
    ],
),

dict(
    tema="Revocatoria directa de actos particulares", ref="PGN-CPA",
    refT="Procedimiento administrativo (CPACA)", nivel="advanced",
    ctx="Una entidad detecta que el acto con el que reconoció una prestación a un particular se expidió con base en certificados laborales falsos. El acto está en firme desde hace dos años y creó una situación jurídica concreta a favor del beneficiario, que se niega a dar su consentimiento para revocarlo.",
    q="¿Qué debe tenerse en cuenta?",
    ops=[
        "Puede revocarse en cualquier caso y sin consentimiento, pues la administración conserva la potestad de corregir sus actos.",
        "Nunca puede revocarse sin consentimiento: la entidad debe demandar su propio acto ante la jurisdicción contenciosa.",
        "Se requiere consentimiento del titular, salvo las excepciones legales, entre ellas el acto obtenido por medios ilegales.",
    ],
    correcta=2,
    expl=[
        "La revocatoria sin consentimiento es la excepción y no una potestad general de la administración.",
        "La demanda de lesividad es una vía posible, pero no la única cuando opera una de las excepciones legales.",
        "Correcto: el CPACA exige el consentimiento, y la obtención por medios ilegales es precisamente una de las excepciones.",
    ],
),

dict(
    tema="Notificación por aviso", ref="PGN-CPA",
    refT="Procedimiento administrativo (CPACA)", nivel="intermediate",
    ctx="No fue posible notificar personalmente un acto administrativo de carácter particular. La entidad envió la citación a la dirección que el interesado registró en su solicitud y dejó constancia de que no compareció dentro de los cinco días siguientes a su entrega.",
    q="¿Qué procede?",
    ops=[
        "Publicar el acto en la cartelera de la entidad y entender surtida la notificación el mismo día de la fijación.",
        "Entender notificado el acto con el solo envío de la citación, por haberse remitido a la dirección registrada.",
        "Notificar por aviso, remitiéndolo a la dirección registrada con copia íntegra del acto administrativo.",
    ],
    correcta=2,
    expl=[
        "La cartelera no sustituye la notificación por aviso ni suple la remisión de la copia íntegra del acto.",
        "La citación tiene por objeto que el interesado comparezca; no equivale por sí misma a la notificación.",
        "Correcto: fracasada la notificación personal procede la notificación por aviso, con los efectos que el CPACA señala.",
    ],
),

dict(
    tema="Motivación del acto administrativo", ref="PGN-CPA",
    refT="Procedimiento administrativo (CPACA)", nivel="advanced",
    ctx="Un acto que niega una solicitud de reconocimiento dice únicamente: «no se accede a lo pedido por no cumplir los requisitos». El expediente tiene ciento veinte folios y el interesado aportó siete documentos. El acto está firmado, notificado y señala los recursos procedentes.",
    q="¿Qué defecto tiene?",
    ops=[
        "Falta de motivación suficiente: no indica cuáles requisitos se incumplen ni por qué razón se consideran incumplidos.",
        "Le falta únicamente la firma del funcionario competente, requisito que puede subsanarse mediante acto posterior.",
        "No cita jurisprudencia del Consejo de Estado que respalde la interpretación de los requisitos que se echan de menos en el caso.",
    ],
    correcta=0,
    expl=[
        "Correcto: la motivación es garantía del debido proceso y condición para que el interesado pueda controvertir la decisión.",
        "El acto está firmado, de modo que ese no es el defecto; la brevedad no excusa la ausencia de razones.",
        "No es obligatorio citar jurisprudencia en todo acto administrativo; lo exigible son las razones de la decisión.",
    ],
),

dict(
    tema="Impedimento del funcionario que decide", ref="PGN-CPA",
    refT="Procedimiento administrativo (CPACA)", nivel="advanced",
    ctx="A usted le corresponde decidir una actuación en la que una de las partes es la empresa donde trabaja su cónyuge desde hace seis años. Usted no conoce el asunto en detalle, no tiene interés económico directo y se considera capaz de decidir con objetividad. El término para resolver vence en cuatro días.",
    q="¿Cuál es la conducta correcta?",
    ops=[
        "Decidir con objetividad y dejar constancia en el expediente de que la relación no afecta su criterio profesional.",
        "Declararse impedido ante quien corresponda y abstenerse de actuar mientras se resuelve el impedimento.",
        "Consultarlo verbalmente con el jefe inmediato y continuar con el trámite si él no advierte inconveniente alguno.",
    ],
    correcta=1,
    expl=[
        "La imparcialidad subjetiva no basta: la ley presume el riesgo y exige declararlo formalmente.",
        "Correcto: se manifiestan los hechos y la causal por escrito, y no se actúa mientras la instancia competente decide.",
        "Una autorización verbal no sustituye el trámite formal del impedimento ni sanea la actuación.",
    ],
),

dict(
    tema="Procedimiento administrativo sancionatorio", ref="PGN-CPA",
    refT="Procedimiento administrativo (CPACA)", nivel="advanced",
    ctx="Una entidad sanciona a un particular con una multa y le comunica la decisión mediante oficio. El expediente muestra que no hubo formulación de cargos, ni traslado para descargos, ni período probatorio: el oficio informa la sanción ya adoptada y anuncia el cobro.",
    q="¿Qué le falta al trámite?",
    ops=[
        "Le falta únicamente la publicación de la decisión sancionatoria en el medio oficial que la entidad utiliza para difundir sus actos.",
        "El procedimiento completo: formulación de cargos, descargos, período probatorio y decisión motivada con recursos.",
        "Le falta la aceptación del particular sancionado, sin la cual la multa impuesta no puede hacerse exigible.",
    ],
    correcta=1,
    expl=[
        "La publicación no sanea la ausencia total del procedimiento que debía anteceder a la sanción.",
        "Correcto: el CPACA estructura un procedimiento sancionatorio que garantiza la defensa antes de la decisión.",
        "La aceptación del particular no es un requisito del procedimiento sancionatorio ni convalida su ausencia.",
    ],
),

dict(
    tema="Medios de control contencioso", ref="PGN-CPA",
    refT="Procedimiento administrativo (CPACA)", nivel="intermediate",
    ctx="Un ciudadano fue retirado del servicio mediante un acto administrativo que considera ilegal. Pretende que se anule el acto, que se le reintegre al cargo y que se le paguen los salarios dejados de percibir desde la desvinculación.",
    q="¿Qué medio de control corresponde?",
    ops=[
        "Nulidad simple, que persigue la defensa del orden jurídico frente a actos contrarios a normas superiores.",
        "Reparación directa, que procede frente a los daños causados por hechos, omisiones u operaciones administrativas.",
        "Nulidad y restablecimiento del derecho, que comprende la anulación del acto y el pago de lo dejado de percibir.",
    ],
    correcta=2,
    expl=[
        "La nulidad simple no comprende el restablecimiento del derecho ni la condena al pago de sumas dejadas de percibir.",
        "La reparación directa procede frente a hechos y omisiones, no contra actos administrativos como el del caso.",
        "Correcto: comprende la anulación del acto y el restablecimiento del derecho con la indemnización correspondiente.",
    ],
),

dict(
    tema="Principios de la contratación estatal", ref="PGN-CTR",
    refT="Contratación estatal", nivel="basic",
    ctx="Al evaluar un proceso de selección, usted debe encabezar el concepto con los principios que rigen específicamente la contratación estatal según la Ley 80 de 1993, y distinguirlos de los principios generales de la función administrativa del artículo 209.",
    q="¿Cuáles son los principios propios de la contratación estatal?",
    ops=[
        "Celeridad, eficacia y gratuidad, que orientan el trámite de las actuaciones administrativas ante cualquier entidad.",
        "Transparencia, economía y responsabilidad, junto con el deber de selección objetiva que ordena la Ley 80.",
        "Subsidiariedad, concurrencia y complementariedad, que ordenan las competencias entre los niveles territoriales.",
    ],
    correcta=1,
    expl=[
        "Esos son principios de la actuación administrativa en general, no los específicos del estatuto de contratación.",
        "Correcto: la Ley 80 de 1993 los consagra como principios rectores, con la selección objetiva como deber central.",
        "Esos son principios de la organización territorial y del reparto de competencias, ajenos a la contratación.",
    ],
),

dict(
    tema="Selección objetiva", ref="PGN-CTR",
    refT="Contratación estatal", nivel="advanced",
    ctx="En un proceso de selección el pliego exige acreditar experiencia en tres contratos de un objeto tan específico que, según el estudio del sector, solo un proveedor del mercado nacional puede certificarlos. El pliego se publicó en el plazo legal y el proceso recibió una sola propuesta.",
    q="¿Qué principio se compromete?",
    ops=[
        "La publicidad, porque la restricción contenida en el pliego no fue advertida a los posibles interesados en el proceso.",
        "La economía, en la medida en que un proceso con un solo proponente eleva el costo final de la contratación.",
        "La selección objetiva y la transparencia, por un requisito que restringe artificialmente la pluralidad de oferentes.",
    ],
    correcta=2,
    expl=[
        "El pliego sí fue publicado; publicar un requisito direccionado no subsana el direccionamiento.",
        "El costo no es el problema central: lo que se compromete es la posibilidad misma de que concurran varios oferentes.",
        "Correcto: los requisitos deben ser proporcionados y adecuados al objeto, y no pueden direccionar el proceso.",
    ],
),

dict(
    tema="Supervisión e interventoría", ref="PGN-CTR",
    refT="Contratación estatal", nivel="intermediate",
    ctx="Un supervisor firmó durante seis meses los informes de ejecución de un contrato de obra sin visitar el sitio ni verificar los soportes. Se basó en los reportes que el contratista le enviaba por correo y en las fotografías que este adjuntaba. La obra presenta hoy un avance muy inferior al certificado.",
    q="¿Cuál es el reproche?",
    ops=[
        "El reproche es estrictamente contractual y se resuelve con la liquidación del contrato y el ajuste de los pagos.",
        "El supervisor debe hacer seguimiento técnico, administrativo, financiero, contable y jurídico, y certificar sin verificar lo compromete.",
        "El reproche recae únicamente sobre el ordenador del gasto de la entidad, que autorizó los pagos con base en esas certificaciones falsas.",
    ],
    correcta=1,
    expl=[
        "La responsabilidad excede lo contractual: compromete al supervisor en lo disciplinario, lo fiscal y lo penal.",
        "Correcto: la supervisión es una función de verificación, y certificar sin verificar es de las conductas más sancionadas.",
        "El supervisor responde por sus propias certificaciones, con independencia de quién autorizó el pago.",
    ],
),

dict(
    tema="Urgencia manifiesta", ref="PGN-CTR",
    refT="Contratación estatal", nivel="advanced",
    ctx="Una entidad declara la urgencia manifiesta para contratar directamente un servicio de aseo que venía requiriendo desde hacía catorce meses. El contrato anterior terminó sin que se adelantara el nuevo proceso de selección, pese a que el plan anual de adquisiciones lo tenía previsto desde enero.",
    q="¿Es procedente esa declaratoria?",
    ops=[
        "Sí, siempre que la entidad remita el acto y el expediente a la Contraloría para el control posterior correspondiente.",
        "No: la urgencia manifiesta exige situaciones excepcionales o de fuerza mayor y no cubre fallas de planeación.",
        "Sí, dado que la interrupción del servicio de aseo afecta la continuidad de la prestación y la salubridad de la sede.",
    ],
    correcta=1,
    expl=[
        "El envío a la Contraloría es un control posterior, no una validación de la causal que se invocó.",
        "Correcto: la falta de planeación imputable a la entidad no configura urgencia manifiesta, y su uso indebido es falta gravísima.",
        "La afectación del servicio es consecuencia de la propia omisión de la entidad, que tuvo catorce meses para actuar.",
    ],
),

dict(
    tema="Principio de planeación", ref="PGN-CTR",
    refT="Contratación estatal", nivel="intermediate",
    ctx="El estudio previo de un proceso describe el objeto en términos genéricos, no incluye análisis del sector, no justifica el valor estimado y no identifica riesgos. Está firmado por el jefe de la dependencia solicitante y fue publicado junto con el aviso de convocatoria.",
    q="¿Qué deficiencia hay?",
    ops=[
        "Se incumple el principio de planeación: el estudio previo debe justificar necesidad, objeto, valor estimado y riesgos.",
        "Le falta únicamente la firma del ordenador del gasto, que es quien respalda la destinación de los recursos públicos.",
        "La deficiencia se corrige durante la ejecución mediante una adición que ajuste el valor y precise el alcance del objeto.",
    ],
    correcta=0,
    expl=[
        "Correcto: sin planeación adecuada el proceso nace viciado y se exponen la entidad y los responsables del trámite.",
        "El estudio está firmado por quien lo elaboró; la firma no suple el contenido que falta.",
        "Las adiciones no corrigen una planeación deficiente y, de hecho, suelen ser su consecuencia más visible.",
    ],
),

dict(
    tema="Inhabilidades en contratación", ref="PGN-CTR",
    refT="Contratación estatal", nivel="advanced",
    ctx="Al revisar las propuestas se advierte que el representante legal de uno de los proponentes es hermano del jefe de la dependencia que estructuró el proceso y elaboró el pliego. La propuesta es la mejor calificada técnica y económicamente, y el comité evaluador ya la recomendó.",
    q="¿Qué procede?",
    ops=[
        "Adjudicar conforme a la recomendación del comité e informar después a la Procuraduría para que evalúe la situación.",
        "Verificar el régimen de inhabilidades y de conflicto de interés y actuar en consecuencia antes de adjudicar.",
        "Solicitar al jefe de la dependencia una declaración de imparcialidad y continuar con el trámite de adjudicación.",
    ],
    correcta=1,
    expl=[
        "Adjudicar primero e informar después consolida el vicio y agrava la responsabilidad de quienes intervienen.",
        "Correcto: el parentesco en ciertos grados inhabilita para contratar, y la calidad de la propuesta no sanea una inhabilidad.",
        "Una declaración de imparcialidad no levanta una inhabilidad que la ley establece de manera objetiva.",
    ],
),

dict(
    tema="Liquidación del contrato", ref="PGN-CTR",
    refT="Contratación estatal", nivel="intermediate",
    ctx="Un contrato de suministro terminó hace ocho meses. Quedaron pendientes de definir un saldo a favor del contratista y la devolución de una garantía. No se ha suscrito acta de liquidación ni se ha iniciado la liquidación unilateral, y el supervisor cambió de dependencia.",
    q="¿Qué implica la falta de liquidación oportuna?",
    ops=[
        "Implica que el contrato se entiende prorrogado hasta que las partes definan el balance final de la ejecución.",
        "Implica que el contratista pierde los saldos a su favor por no haber solicitado la liquidación dentro del plazo.",
        "Incumple un deber de la entidad y puede comprometer disciplinaria y fiscalmente a los responsables del trámite.",
    ],
    correcta=2,
    expl=[
        "La terminación del contrato no se convierte en prórroga por el hecho de que la liquidación esté pendiente.",
        "El contratista no pierde sus derechos por la inactividad de la entidad, que es quien tiene el deber de liquidar.",
        "Correcto: la liquidación es obligatoria en los contratos que la requieren y su omisión tiene consecuencias patrimoniales.",
    ],
),

dict(
    tema="Conflicto de interés: definición", ref="PGN-INT",
    refT="Integridad, conflicto de interés y transparencia", nivel="intermediate",
    ctx="Un profesional debe conceptuar sobre una solicitud presentada por una sociedad en la que su hermana tiene una participación del diez por ciento. Él no recibe ningún pago de esa sociedad, no participa en su administración y sostiene que su concepto será estrictamente técnico.",
    q="¿Qué configura un conflicto de interés?",
    ops=[
        "Solamente el interés económico directo y personal del servidor en el asunto sobre el cual debe pronunciarse.",
        "Cualquier situación en que el interés particular, directo o indirecto, pueda influir, o parecer que influye, en la objetividad.",
        "Únicamente la existencia de un pago o de un beneficio económico recibido por el servidor de parte del interesado en la actuación.",
    ],
    correcta=1,
    expl=[
        "El interés indirecto, como el de un pariente cercano, también configura conflicto de interés.",
        "Correcto: lo relevante es el riesgo de afectación de la objetividad, incluso cuando solo exista en apariencia.",
        "Recibir un pago configura cohecho o dádiva, que es un supuesto distinto y considerablemente más grave.",
    ],
),

dict(
    tema="Regalos y atenciones", ref="PGN-INT",
    refT="Integridad, conflicto de interés y transparencia", nivel="intermediate",
    ctx="Un proveedor con contrato vigente envía a su oficina una canasta navideña con productos importados. La tarjeta agradece la colaboración del equipo durante el año. Tres compañeros ya recibieron canastas iguales y dicen que es una costumbre de todos los diciembres.",
    q="¿Cuál es la conducta correcta?",
    ops=[
        "Aceptarla y repartirla entre el equipo de la dependencia, de modo que ningún servidor obtenga un provecho individual.",
        "No aceptarla, devolverla y dejar constancia del hecho ante el superior o el canal institucional previsto.",
        "Aceptarla siempre que su valor comercial no supere el equivalente a un salario mínimo legal mensual vigente.",
    ],
    correcta=1,
    expl=[
        "Repartirla no cambia la naturaleza de la dádiva ni el hecho de que proviene de un contratista en ejecución.",
        "Correcto: rechazar, devolver y documentar protege al servidor, a la entidad y al propio proceso contractual.",
        "No existe un umbral de valor que autorice recibir obsequios de un contratista con contrato vigente.",
    ],
),

dict(
    tema="Deber de denunciar", ref="PGN-INT",
    refT="Integridad, conflicto de interés y transparencia", nivel="advanced",
    ctx="Usted presencia cómo un compañero altera la fecha de un documento que ya forma parte de un expediente. Él le explica que fue un error de digitación de la semana pasada, que así queda corregido y le pide que no comente nada porque está a punto de pensionarse.",
    q="¿Cuál es su deber?",
    ops=[
        "Conversar con él y darle un plazo para que corrija el documento por el conducto formal que corresponda.",
        "Poner los hechos en conocimiento de la autoridad competente, por el canal institucional previsto para ello.",
        "Registrar la observación en una nota personal y esperar a verificar si la conducta vuelve a repetirse más adelante.",
    ],
    correcta=1,
    expl=[
        "Darle un plazo lo convierte a usted en encubridor y permite que la alteración se consolide en el expediente.",
        "Correcto: existe el deber funcional de denunciar las conductas punibles y las posibles faltas de que se tenga conocimiento.",
        "Esperar la reiteración no es una opción: el deber nace con el conocimiento del hecho, no con su repetición.",
    ],
),

dict(
    tema="Transparencia y acceso a la información", ref="PGN-INT",
    refT="Integridad, conflicto de interés y transparencia", nivel="intermediate",
    ctx="Un ciudadano solicita la relación de los contratos suscritos por la entidad en el último año, con su objeto, valor y contratista. El área responsable propone negar la solicitud porque se trata de «información interna» y porque responderla implicaría dos días de trabajo.",
    q="¿Cuál es la regla aplicable?",
    ops=[
        "Toda la información que produce la entidad es reservada, salvo que una norma disponga expresamente lo contrario.",
        "Puede negarse cuando el peticionario no justifica el uso que dará a la información que está solicitando a la entidad pública.",
        "La regla general es la publicidad y el acceso solo puede limitarse por reserva legal expresa, aplicada de forma restrictiva.",
    ],
    correcta=2,
    expl=[
        "La relación es la inversa: la publicidad es la regla general y la reserva, la excepción que debe estar en la ley.",
        "El peticionario no está obligado a justificar el uso que dará a la información pública que solicita.",
        "Correcto: así lo establece la ley de transparencia, y la carga de trabajo no es causal de reserva.",
    ],
),

dict(
    tema="Presión sobre un concepto técnico", ref="PGN-INT",
    refT="Integridad, conflicto de interés y transparencia", nivel="advanced",
    ctx="Su jefe le pide ajustar un concepto técnico para que favorezca a una de las partes. Le dice que así conviene a la entidad, que él responde por la decisión y que usted no tiene por qué complicarse. El concepto debe salir mañana y lleva su firma.",
    q="¿Cómo debe proceder?",
    ops=[
        "Ajustar el concepto conforme a la instrucción recibida y conservar una copia del borrador original por si llega a necesitarla.",
        "Retirarse del caso solicitando que se asigne a otro profesional, sin dejar constancia de la razón de su retiro.",
        "Mantener el concepto conforme a su criterio técnico, dejar constancia escrita de la solicitud y poner el asunto en conocimiento.",
    ],
    correcta=2,
    expl=[
        "Guardar una copia no corrige el documento alterado que queda en el expediente y que lleva su firma.",
        "Retirarse sin dejar constancia deja el caso expuesto a la misma presión con otro profesional.",
        "Correcto: sostener el criterio y documentar es lo que protege la actuación y al propio servidor que la suscribe.",
    ],
),

dict(
    tema="Uso de bienes institucionales", ref="PGN-INT",
    refT="Integridad, conflicto de interés y transparencia", nivel="basic",
    ctx="Un servidor usa el vehículo oficial asignado a su despacho para trasladar un trasteo familiar un sábado. Repone el combustible consumido, el vehículo no sufre daños y nadie más lo necesitaba ese día porque la entidad no presta servicio los fines de semana.",
    q="¿Cómo se valora la conducta?",
    ops=[
        "Es válida porque ocurrió fuera de la jornada laboral y el vehículo no estaba requerido para ninguna comisión oficial.",
        "Constituye uso indebido de bienes del Estado, que están afectos al servicio y no a fines personales.",
        "Es válida en la medida en que el servidor repuso el combustible y devolvió el vehículo en las mismas condiciones.",
    ],
    correcta=1,
    expl=[
        "El horario y la disponibilidad del bien no cambian su destinación, que es el servicio y no el uso particular.",
        "Correcto: la afectación al servicio es el criterio que define la irregularidad, no el día ni el estado del vehículo.",
        "Reponer el combustible no legitima el uso personal de un bien destinado al servicio público.",
    ],
),

dict(
    tema="Prioridad entre tareas que vencen el mismo día", ref="PGN-INT",
    refT="Integridad, conflicto de interés y transparencia", nivel="advanced",
    ctx="El mismo día vencen tres cosas: un término procesal perentorio en un expediente, el informe mensual de gestión que pidió el jefe y una reunión de equipo convocada hace una semana. Usted alcanza a cumplir dos de las tres y el jefe estará en la reunión.",
    q="¿Cuál es el criterio profesional correcto?",
    ops=[
        "Atender primero el término procesal perentorio y gestionar con el jefe la reprogramación de lo demás.",
        "Atender primero el informe de gestión y la reunión, que son los compromisos adquiridos directamente con el superior.",
        "Avanzar parcialmente en las tres, de modo que ninguna quede sin atender y todas registren algún nivel de cumplimiento.",
    ],
    correcta=0,
    expl=[
        "Correcto: se prioriza lo perentorio e irreversible, y se comunica a tiempo en lugar de decidir en silencio.",
        "La jerarquía no desplaza un término legal que no admite prórroga y cuyo incumplimiento puede generar nulidades.",
        "Cumplir las tres a medias garantiza fallar en la que no admite remedio posterior.",
    ],
),

dict(
    tema="Error propio detectado a tiempo", ref="PGN-INT",
    refT="Integridad, conflicto de interés y transparencia", nivel="advanced",
    ctx="Usted advierte que hace una semana envió a otra entidad un oficio con una cifra equivocada, y que esa entidad ya adoptó una decisión con base en ese dato. Nadie lo ha notado, el error no fue intencional y revelarlo quedaría registrado en su hoja de vida.",
    q="¿Cuál es la conducta correcta?",
    ops=[
        "Corregir el archivo interno de la dependencia y dejar el asunto así, dado que el error no fue intencional.",
        "Esperar a que la entidad destinataria lo detecte y, en ese momento, responder explicando cómo se produjo el error en el oficio.",
        "Informar de inmediato por escrito a su superior y a la entidad destinataria, con el dato correcto y las medidas de corrección.",
    ],
    correcta=2,
    expl=[
        "Corregir solo el archivo interno no deshace los efectos de la decisión que ya se adoptó con el dato errado.",
        "Esperar prolonga el daño y convierte un descuido en una omisión deliberada de consecuencias mucho mayores.",
        "Correcto: informar y corregir a tiempo es lo que exige el deber funcional, y suele valorarse como circunstancia de atenuación.",
    ],
),

dict(
    tema="Dato inconsistente antes de firmar", ref="PGN-INT",
    refT="Integridad, conflicto de interés y transparencia", nivel="advanced",
    ctx="Debe firmar hoy el informe consolidado de la dependencia. Al revisarlo encuentra que dos fuentes internas reportan cifras distintas sobre el mismo indicador, con una diferencia del doce por ciento. No alcanza a reconciliarlas antes del vencimiento y el informe alimenta una decisión de otra área.",
    q="¿Qué hace?",
    ops=[
        "Firmar con la cifra más conservadora de las dos, que expone menos a la dependencia ante una eventual verificación.",
        "Reportar el hallazgo, remitir el informe advirtiendo la inconsistencia y el plazo en que se aclarará, y dejar constancia.",
        "Abstenerse de enviar el informe hasta tener plena certeza sobre la cifra, aunque ello implique incumplir el término fijado.",
    ],
    correcta=1,
    expl=[
        "Ser conservador no resuelve el problema: la cifra sigue sin estar verificada y el informe sigue siendo inexacto.",
        "Correcto: transparentar la inconsistencia protege a quien decide con ese informe y a la vez cumple el término.",
        "Dejar vencer el término sin comunicar nada agrega un incumplimiento al problema que ya existía.",
    ],
),

]
