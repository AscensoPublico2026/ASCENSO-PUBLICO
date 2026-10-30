import json, os
D = os.path.dirname(os.path.abspath(__file__))

flash = [
 {"f": "¿El levante cierra el control aduanero?", "b": "No. El levante permite disponer de la mercancía; la declaración sigue sujeta a control posterior hasta su firmeza: 3 años desde la presentación y aceptación, salvo que se notifique antes un REA (Decreto 1165, art. 188)."},
 {"f": "¿Cuáles son las cinco “puertas cerradas” del control posterior?", "b": "Caducidad de la acción sancionatoria, declaración en firme, falta de competencia, mismos hechos ya sancionados o investigados e ineficacia por razones de gestión (Decreto Ley 920, art. 3, parágrafo)."},
 {"f": "¿Qué pasa si el usuario no responde la invitación persuasiva?", "b": "Nada sancionatorio: la no respuesta no ocasiona sanción. Vencido el mes, la seccional puede iniciar el procedimiento; el REA no se expide antes de ese vencimiento (art. 5)."},
 {"f": "¿Qué es mercancía diferente?", "b": "La que, tras la verificación documental o física, no corresponde con la declarada en sus características fundamentales, o tiene omisión total o error en el serial. Un error de digitación que no cambia la naturaleza no la convierte en diferente (Decreto 1165, art. 3)."},
 {"f": "¿Qué diferencia el contrabando del fraude aduanero?", "b": "En el contrabando (art. 319 C.P., más de 50 SMMLV) la mercancía escapa del control; en el fraude aduanero (art. 321 C.P., más de 20 SMMLV, 8 a 12 años) pasa por el control con información falsa para evadir tributos."},
 {"f": "¿Qué naturaleza tiene la aprehensión y qué recurso procede contra ella?", "b": "Es una medida cautelar por causal tipificada del art. 69, con acta. Contra la medida no procede recurso; puede activarse el Comité de Revisión de Aprehensiones, que es potestativo y no es instancia."},
 {"f": "¿Cuáles son los términos del decomiso ordinario?", "b": "Objeción: 15 días hábiles desde la notificación del acta (art. 88). Decisión: 70 días hábiles (art. 90). Reconsideración: 15 días hábiles desde la notificación de la decisión (art. 130)."},
 {"f": "¿Cuánto se paga de la multa al allanarse?", "b": "El 20 % antes de notificar el REA, el 40 % después del REA y antes de la decisión de fondo, y el 60 % dentro del término para recurrir (Decreto Ley 920, art. 24). No reduce intereses ni rescate."},
 {"f": "¿Qué actos profiere el Gestor I?", "b": "Los de trámite, preparatorios y de fondo que su competencia le asigne; los que la norma reserva al jefe de división o al director seccional los proyecta y sustancia para su firma."},
 {"f": "¿Qué acredita la destrucción de una mercancía?", "b": "El acta de la diligencia autorizada y verificada por la autoridad aduanera (Resolución 046 de 2019, arts. 228 y 229). Un certificado privado puede anexarse, pero no la sustituye."}
]

P = []
def q(nivel, tema, ctx, qq, ops, correcta, expl):
    P.append({"nivel": nivel, "tema": tema, "ctx": ctx, "q": qq, "ops": ops, "correcta": correcta, "expl": expl})

# ---------- BÁSICAS ----------
q("b", "Firmeza de la declaración",
 "Un Gestor I del área de fiscalización y liquidación aduanera de una Dirección Seccional recibe una alerta del área de análisis de riesgo: la declaración de importación de un lote de calzado deportivo, presentada y aceptada hace tres años y dos meses, muestra un valor declarado muy inferior a los pagos que el importador giró al exterior. No se notificó requerimiento especial aduanero ni hubo verificación de origen en curso. Las pruebas reunidas son sólidas: facturas del proveedor, extractos de los giros y la contabilidad del importador. El jefe de la división pide al Gestor I que le diga si se puede proyectar el requerimiento especial aduanero esta misma semana.",
 "Con la declaración aceptada hace más de tres años, sin requerimiento especial notificado ni verificación de origen que suspendiera el término, y con pruebas sólidas de subvaloración, ¿qué debe responder y hacer el Gestor I frente a la solicitud de su jefe de proyectar el requerimiento especial aduanero?",
 ["Informar que la declaración está en firme y que la autoridad debe abstenerse de iniciar actuación, proyectar el acta de no inicio y evaluar si los hechos deben ponerse en conocimiento de la Fiscalía.",
  "Proyectar el requerimiento especial aduanero de inmediato, porque la solidez de las pruebas de subvaloración, con facturas, giros y contabilidad, justifica reabrir el término de revisión de la declaración de importación.",
  "Enviar primero una invitación persuasiva al importador, porque su notificación reabre el término de firmeza y permite luego expedir el requerimiento especial con más tiempo."],
 0,
 ["✔ A los tres años sin REA notificado la declaración queda en firme (Decreto 1165, art. 188) y el parágrafo del art. 3 del Decreto Ley 920 ordena no iniciar, dejando acta. Si hay indicios de delito, se denuncia.",
  "Incorrecto. La firmeza no se reabre por la calidad de la prueba: es una puerta cerrada del control posterior.",
  "Incorrecto. La invitación persuasiva no interrumpe ni reabre la firmeza; solo el REA notificado antes de los tres años la interrumpe."])

q("b", "Gestión persuasiva",
 "Una Gestor I proyectó, con la firma de su jefe, una invitación persuasiva para que una importadora de textiles corrigiera una posible inexactitud en el valor de dos declaraciones. La invitación se comunicó por correo electrónico y ya pasó más de un mes sin que la empresa respondiera ni presentara corrección alguna. En la reunión de seguimiento, un compañero propone proyectar una resolución que sancione a la empresa por “desatender a la autoridad” y otro sugiere archivar el caso porque, a su juicio, sin la aceptación del usuario ya no se puede continuar. Las declaraciones fueron aceptadas hace un año y cuatro meses y no hay otras actuaciones sobre los mismos hechos.",
 "Vencido el mes de la invitación persuasiva sin respuesta de la importadora, con declaraciones que aún no están en firme y sin actuaciones previas sobre los mismos hechos, ¿qué debe hacer la Gestor I con el expediente frente a las dos propuestas de sus compañeros?",
 ["Proyectar la resolución sancionatoria por no atender la invitación, porque el silencio del usuario frente a una comunicación oficial de la DIAN constituye una infracción autónoma, distinta de la inexactitud investigada.",
  "Proponer el archivo del expediente, porque la gestión persuasiva exige la aceptación del usuario y, al no obtenerla, la autoridad pierde la competencia para continuar con el caso.",
  "Continuar el procedimiento: la no respuesta no se sanciona y, vencido el plazo, se puede proyectar el requerimiento especial aduanero, verificando antes la firmeza y la caducidad."],
 2,
 ["Incorrecto. El art. 5 del Decreto Ley 920 dispone que la no respuesta a la invitación persuasiva no ocasiona sanción alguna.",
  "Incorrecto. La invitación es una herramienta; si el usuario no acepta ni subsana, la seccional puede iniciar el procedimiento.",
  "✔ Vencido el mes, la autoridad puede continuar con el REA (art. 5, parágrafo 2), revisando antes las fechas de firmeza y caducidad."])

q("b", "Objeción a la aprehensión",
 "La Policía Fiscal y Aduanera dejó a disposición de la Dirección Seccional un camión con licores sin documentos que acreditaran su ingreso legal. El funcionario competente aprehendió la mercancía y el acta se notificó personalmente al transportador el lunes, al terminar la diligencia. El miércoles, el abogado del transportador llama al Gestor I que sustancia el expediente y afirma que tiene “setenta días hábiles para oponerse, porque ese es el plazo de la DIAN”. Pide que le confirme el plazo y le diga si su cliente recuperará la mercancía. El Gestor I tiene a la vista el acta, la constancia de notificación y el cuadro de términos del expediente.",
 "El apoderado cree que dispone de setenta días hábiles para oponerse a la aprehensión y pregunta además si su cliente recuperará los licores. ¿Qué debe responderle el Gestor I que sustancia el expediente, frente al plazo y frente a la pregunta por el resultado?",
 ["Que dispone de setenta días hábiles para objetar, porque el término del interesado coincide con el plazo que tiene la autoridad para expedir la decisión de fondo sobre el decomiso.",
  "Que tiene quince días hábiles desde la notificación del acta para presentar el documento de objeción por escrito, sin anticipar el sentido de la decisión que se adopte.",
  "Que solo podrá oponerse cuando se expida la resolución de decomiso, mediante recurso de reconsideración, y que por ahora la mercancía no admite ninguna discusión."],
 1,
 ["Incorrecto. Los setenta días hábiles son el plazo de la autoridad para decidir (art. 90), no el del interesado.",
  "✔ El art. 88 fija quince días hábiles desde la notificación del acta para el documento de objeción. El Gestor orienta sin comprometer la decisión.",
  "Incorrecto. La objeción procede desde la notificación del acta de aprehensión; la reconsideración es contra la decisión de fondo."])

q("b", "Acta de destrucción",
 "Un importador de equipos médicos recibió un lote defectuoso y el proveedor envió equipos de reemplazo bajo garantía. Para no exportar los defectuosos, el importador constituyó la garantía que exige la norma y obtuvo autorización para destruirlos en una diligencia programada para el jueves, en la que participará un Gestor I del área de fiscalización. El martes, el delegado de la empresa envía al Gestor I un certificado de una empresa gestora de residuos que dice que los equipos ya fueron triturados el lunes, y le pide dar por cumplido el trámite para cancelar la garantía y presentar la declaración de los equipos de reemplazo sin más demoras.",
 "La empresa presenta un certificado privado de la gestora de residuos que afirma que los equipos defectuosos ya se destruyeron, y pide dar por cumplido el trámite antes de la diligencia autorizada para el jueves, con el fin de cancelar la garantía. ¿Cómo debe actuar el Gestor I?",
 ["Aceptar el certificado como prueba suficiente, porque la empresa gestora está autorizada para el manejo de residuos y su constancia acredita ante la autoridad aduanera la destrucción total de los equipos.",
  "Proyectar de inmediato la cancelación de la garantía, porque la finalidad de la norma se cumplió cuando los equipos defectuosos dejaron de existir, sin importar quién lo verificó.",
  "Explicar que la destrucción se acredita con el acta de la diligencia autorizada y verificada por la autoridad, informar a su jefe la novedad y no dar por cumplido el trámite."],
 2,
 ["Incorrecto. Según la doctrina de la DIAN, el acta de la diligencia no puede sustituirse con documentos privados del importador.",
  "Incorrecto. La garantía se cancela al acreditarse la destrucción con el acta; sin verificación de la autoridad, no hay acreditación.",
  "✔ El acta de la diligencia (Resolución 046 de 2019, arts. 228 y 229) es el soporte; la destrucción anticipada sin verificación es una novedad que se informa."])

# ---------- INTERMEDIAS ----------
q("i", "Mercancía diferente",
 "En un operativo planificado por un Gestor I con apoyo de la Policía Fiscal y Aduanera, se verifica una bodega cuyo propietario presenta una declaración de importación con levante que ampara 600 kits de repuestos para motocicleta. Al abrir las cajas, 420 contienen los repuestos descritos y 180 contienen teléfonos celulares nuevos con sus cargadores y seriales. El representante de la empresa sostiene que se trató de un error del agente al digitar la descripción y ofrece presentar una declaración de corrección esa misma tarde. El funcionario competente que dirige la diligencia pide al Gestor I su análisis antes de decidir qué medida adoptar sobre las cajas con teléfonos.",
 "La declaración ampara repuestos para motocicleta, pero 180 de las cajas contienen teléfonos celulares, y el representante alega un simple error de digitación. ¿Qué análisis debe presentar el Gestor I a quien dirige la diligencia antes de que se adopte la medida sobre esas cajas?",
 ["Que las cajas con teléfonos son mercancía diferente, porque cambian sus características fundamentales, y que se documentan e inventarían para que se adopte la medida que permita la causal tipificada.",
  "Que se trata de un error de digitación subsanable, por lo que basta con recibir la declaración de corrección que ofrece el representante y continuar la verificación de los repuestos.",
  "Que procede aplicar el margen de tolerancia, porque el número total de cajas coincide con lo declarado y la diferencia se limita al contenido de una parte de ellas, sin afectar la cantidad total de bultos declarados."],
 0,
 ["✔ Un teléfono no es un repuesto mal descrito: cambia la naturaleza, por lo que es mercancía diferente (Decreto 1165, art. 3). Se documenta y quien dirige aplica la causal del art. 69.",
  "Incorrecto. Solo el error que no altera la naturaleza de la mercancía deja de ser mercancía diferente; aquí la naturaleza cambió.",
  "Incorrecto. La tolerancia del art. 153 del Decreto 1165 aplica solo a mercancías a granel, no a mercancía empacada."])

q("i", "Requerimiento de información",
 "Una Gestor I revisa el expediente de un importador de repuestos a quien se le notificó, durante una visita, un requerimiento de información el día 3 del mes. El requerimiento pedía los contratos con el proveedor, los soportes de los giros al exterior y una copia de una declaración de importación que reposa en los sistemas de la DIAN. El importador no pidió prórroga y respondió el día hábil 22 con los contratos, pero sin los soportes de los giros. Un compañero propone proyectar una sanción por cada documento faltante, incluida la copia de la declaración, y además concluir en el mismo acto que hubo subvaloración porque “quien no entrega es porque esconde”.",
 "La respuesta llegó por fuera del plazo de quince días hábiles, incompleta, y el requerimiento incluía una declaración que la DIAN ya tenía. ¿Qué debe proponer la Gestor I para el trámite sancionatorio del expediente y frente a la conclusión sobre la subvaloración?",
 ["Proyectar una sanción por cada documento no entregado, incluida la copia de la declaración, y declarar en el mismo acto la subvaloración, porque la respuesta incompleta la demuestra.",
  "Proponer el trámite por el requerimiento incumplido solo respecto de lo exigible, excluyendo lo que la DIAN ya poseía, y analizar la subvaloración por separado con sus propias pruebas.",
  "Abstenerse de cualquier actuación, porque al incluir en el requerimiento un documento que la DIAN tenía, el requerimiento completo quedó viciado y no puede producir efecto alguno."],
 1,
 ["Incorrecto. La sanción es por requerimiento incumplido (200 UVT), no por documento; y la respuesta incompleta no prueba por sí sola la subvaloración.",
  "✔ El art. 4 impide exigir lo que la entidad ya posee y sanciona el incumplimiento del requerimiento; la subvaloración exige su propia prueba y trámite.",
  "Incorrecto. Pedir un documento que la DIAN tiene es un exceso respecto de ese documento, pero no anula lo legítimamente exigido."])

q("i", "Fraude aduanero y coordinación",
 "Un Gestor I analiza las importaciones de una comercializadora de autopartes. La declaración más relevante fue aceptada hace dos años y ocho meses. El cruce muestra facturas por la mitad del valor efectivamente girado y giros realizados a través de una sociedad ubicada en un tercer país, sin relación aparente con el proveedor. El jefe de la división pide una propuesta de actuación. Un compañero sugiere enviar todo a la Fiscalía y suspender cualquier trámite aduanero hasta que haya decisión penal, para no duplicar esfuerzos ni arriesgar decisiones contradictorias. Otro propone llamar al gerente de la empresa para preguntarle por los giros antes de decidir.",
 "Con indicios de fraude aduanero, pagos por canales anómalos y una declaración a pocos meses de quedar en firme, ¿qué propuesta de actuación debe presentar el Gestor I a su jefe, frente a las sugerencias de suspender todo o de llamar al gerente?",
 ["Remitir el expediente a la Fiscalía y suspender el trámite aduanero hasta la decisión penal, porque el proceso penal prevalece y evita decisiones contradictorias.",
  "Llamar al gerente para que explique los giros antes de cualquier actuación, porque escuchar al usuario de manera informal garantiza su derecho de defensa desde el inicio.",
  "Continuar la revisión de valor con el REA a tiempo, proyectar la puesta en conocimiento de la Fiscalía y el traslado al área cambiaria, y reportar las señales por el canal con reserva."],
 2,
 ["Incorrecto. Los procesos son independientes (Decreto Ley 920, arts. 11 y 12) y la firmeza seguiría corriendo mientras se espera.",
  "Incorrecto. La defensa se garantiza en el procedimiento formal; una llamada informal puede alertar al investigado y vulnerar la reserva.",
  "✔ Se sigue el trámite administrativo antes de la firmeza, se denuncian los hechos que pueden ser delito, se trasladan los cambiarios y se reporta con reserva."])

q("i", "Inventario y ofrecimiento",
 "Durante una aprehensión de teléfonos celulares, un Gestor I coordina el inventario. El conteo unidad por unidad, verificado por dos personas, arroja 2.160 equipos; el representante de la empresa insiste en que son 1.800 y dos cajas tienen el sello abierto. Al terminar, el representante se acerca y le dice en voz baja que, si el acta queda con 1.800 equipos, “sabrá agradecerle”. Un funcionario de apoyo comenta que anotar 1.800 evitaría discusiones con la empresa. El depósito que recibirá la mercancía está confirmado por escrito y el vehículo de traslado ya llegó.",
 "El conteo verificado arroja 2.160 equipos, el representante afirma que son 1.800 y además insinúa una retribución si el acta registra esa cifra. ¿Qué debe hacer el Gestor I con el inventario y con el ofrecimiento antes de que la mercancía se traslade al depósito?",
 ["Registrar 1.800 equipos para evitar el conflicto y anotar el excedente en un documento aparte, rechazando el ofrecimiento verbalmente sin dejar constancia para no complicar la diligencia.",
  "Registrar los 2.160 equipos contados con constancia de lo manifestado y de las cajas abiertas, rechazar el ofrecimiento, dejarlo consignado e informarlo por el canal establecido.",
  "Suspender el inventario y retirarse de la diligencia hasta que otro funcionario la asuma, porque el ofrecimiento lo inhabilita para seguir actuando en el caso de la empresa."],
 1,
 ["Incorrecto. Alterar el inventario es falsear un documento público, y el ofrecimiento debe quedar documentado e informado.",
  "✔ El inventario refleja el conteo real; el ofrecimiento (posible cohecho por dar u ofrecer, art. 407 C.P.) se rechaza, se consigna y se informa.",
  "Incorrecto. El ofrecimiento rechazado no genera un impedimento que obligue a abandonar la diligencia; dejarla incompleta pone en riesgo la mercancía."])

q("i", "Allanamiento",
 "Una Gestor I sustancia un expediente en el que se notificó, hace ocho días, un requerimiento especial aduanero que propone mayores tributos por diferencia de valor y una multa por la inexactitud. La representante legal de la importadora llama para preguntar si puede “pagar con descuento” y cuánto sería. Dice que un asesor le aseguró que, si paga ya, solo tendría que cancelar el veinte por ciento de la multa y que además se le perdonarían los intereses. La Gestor I tiene a la vista la constancia de notificación del REA, la cuantificación propuesta y el cuadro de términos del expediente.",
 "La representante legal pregunta por la reducción de la multa después de notificado el REA y cree que pagaría solo el veinte por ciento y sin intereses. ¿Qué debe explicarle la Gestor I que sustancia el expediente, sin comprometer el resultado del proceso?",
 ["Que, notificado el REA y antes de la decisión de fondo, puede allanarse pagando el cuarenta por ciento de la multa con escrito y recibo de pago, y que el allanamiento no reduce los intereses.",
  "Que puede pagar solo el veinte por ciento de la multa, porque ese es el porcentaje general del allanamiento, y que con ese pago se entienden también extinguidos los intereses de mora.",
  "Que ya no tiene derecho a reducción, porque el allanamiento solo procede antes de la notificación del REA, y que debe esperar la decisión de fondo para discutir la multa."],
 0,
 ["✔ El art. 24 reduce la multa al 40 % después del REA y antes de la decisión de fondo; se exige escrito y recibo de pago, y no se reducen intereses ni rescate.",
  "Incorrecto. El 20 % aplica solo antes de notificar el REA, y el allanamiento no extingue los intereses de mora.",
  "Incorrecto. El allanamiento procede también después del REA (40 %) y dentro del término para recurrir (60 %)."])

# ---------- AVANZADAS ----------
q("a", "Congruencia del REA",
 "Un Gestor I proyecta la decisión de fondo de un expediente en el que el requerimiento especial aduanero propuso una liquidación oficial de revisión de valor y la sanción por inexactitud. En su respuesta, el importador aportó contratos y extractos que explican parte de la diferencia. Al revisar de nuevo el expediente, un compañero encontró que en la inspección faltaba un documento soporte exigido y propone incluir en la misma decisión la sanción por esa falta, “para aprovechar el acto y no abrir otro expediente”. Faltan veinte días hábiles para que venza el plazo de setenta días para expedir y notificar la decisión, y el jefe pide el proyecto para revisión esta semana.",
 "El REA solo propuso la revisión de valor y la sanción por inexactitud, y ahora se plantea agregar en la decisión una sanción por un documento soporte faltante que no se formuló. ¿Cómo debe proyectar el Gestor I la decisión de fondo que debe expedirse y notificarse en los próximos veinte días?",
 ["Incluir la nueva sanción en la decisión, porque el usuario podrá controvertirla en el recurso de reconsideración y así se respeta su derecho de defensa sin abrir un trámite distinto ni dispersar las pruebas.",
  "Suspender la decisión de fondo hasta notificar un REA complementario que incluya el nuevo cargo, aunque con ello se supere el plazo de setenta días previsto para decidir.",
  "Decidir solo sobre lo planteado en el REA, valorando las pruebas aportadas, y proponer un trámite separado para el nuevo hecho, previa verificación de su firmeza y caducidad."],
 2,
 ["Incorrecto. La decisión debe ser congruente con el REA; sancionar un cargo no planteado vulnera el derecho de defensa, y el recurso no subsana ese vicio.",
  "Incorrecto. Dejar vencer el plazo de setenta días pone en riesgo toda la actuación; el nuevo hecho no exige detener la decisión en curso.",
  "✔ La congruencia limita la decisión a lo propuesto en el REA (art. 110); el hecho nuevo se evalúa en otro trámite si las puertas siguen abiertas."])

q("a", "Competencia para firmar",
 "Un Gestor I terminó el proyecto de decisión de fondo de un decomiso. La resolución interna de competencias asigna la firma de esa decisión al jefe de la división, quien está de vacaciones; la Dirección Seccional designó a una funcionaria para hacer sus veces, pero ella está en una comisión en otra ciudad hasta el viernes. El plazo de setenta días hábiles para decidir y notificar vence el lunes siguiente. Un compañero sugiere al Gestor I que lo firme él mismo, “porque al fin y al cabo el proyecto es suyo y la ficha dice que el Gestor profiere actos de fondo”. El apoderado del interesado ha preguntado dos veces por el estado del proceso.",
 "El plazo para decidir el decomiso vence pronto, el jefe competente está de vacaciones y quien hace sus veces está en comisión hasta el viernes. ¿Qué debe hacer el Gestor I con el proyecto de decisión de fondo que ya terminó y que está listo para firma?",
 ["No firmarlo, porque esa decisión no está dentro de su competencia; remitirlo de inmediato a quien hace las veces del jefe con alerta escrita del vencimiento y preparar la notificación para el día de la firma.",
  "Firmarlo, porque su ficha le permite proferir actos de fondo y la ausencia del jefe justifica que asuma la decisión para evitar el vencimiento del plazo de setenta días hábiles del decomiso.",
  "Esperar al regreso del jefe titular y explicar al apoderado que el plazo se suspende por las vacaciones, ya que la ausencia del funcionario competente interrumpe los términos del proceso."],
 0,
 ["✔ El Gestor profiere los actos de fondo que su competencia le asigne; los reservados a otro cargo los proyecta. Alertar a quien hace las veces y preparar la notificación protege el plazo.",
  "Incorrecto. Un acto expedido sin competencia está viciado; la ficha no traslada competencias que la resolución interna asigna a otro cargo.",
  "Incorrecto. Las vacaciones del funcionario no suspenden los términos del proceso; esperar pondría en riesgo la decisión."])

q("a", "Registro y conservación de la prueba",
 "En una visita de verificación a una bodega, con apoyo de la Policía Fiscal y Aduanera, el Gestor I que participa observa que el contador de la empresa traslada cajas de archivo desde la bodega hacia una oficina contigua, cuyo acceso no está cubierto por el acto que ordenó la diligencia. El representante legal se opone a que se ingrese a la oficina. Un policía sugiere entrar de una vez y un compañero le dice al Gestor I que, como él planificó el operativo, puede ordenar el registro de la oficina en el sitio. El jefe de la división, competente para ordenarlo mediante resolución motivada, está disponible por teléfono.",
 "Hay riesgo de que la documentación contable se pierda, la oficina no está cubierta por el acto de la diligencia y el representante se opone. El jefe competente está disponible por teléfono. ¿Qué debe hacer el Gestor I en ese momento de la diligencia?",
 ["Ordenar en el sitio el registro de la oficina con apoyo de la Policía, porque planificó el operativo y la urgencia de conservar la prueba justifica que asuma esa decisión sin esperar.",
  "Informar de inmediato al jefe y sustentar la necesidad del registro para que lo ordene por resolución motivada, dejar constancia en el acta y proponer medidas para conservar la prueba mientras tanto.",
  "Retirarse de la bodega y dejar constancia de la oposición, porque sin el registro ordenado previamente no es posible adoptar ninguna medida sobre la documentación de la empresa."],
 1,
 ["Incorrecto. El registro exige resolución motivada de quien tiene la competencia, que es indelegable (Decreto Ley 920, art. 3); quien planifica no la adquiere.",
  "✔ Se acude al competente para la resolución motivada, se documenta la oposición y se proponen medidas cautelares para conservar la prueba (art. 7).",
  "Incorrecto. Retirarse sin actuar abandona la prueba; existen medidas cautelares para conservarla mientras decide el competente."])

assert [p["nivel"] for p in P] == list("bbbbiiiiiaaa"), [p["nivel"] for p in P]
json.dump({"flashcards": flash, "preguntas": P}, open(os.path.join(D, "datos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for i, p in enumerate(P, 1):
    L = [len(o) for o in p["ops"]]
    print(i, p["nivel"], "ctx", len(p["ctx"]), "q", len(p["q"]), "ops", L, "c", p["correcta"], "larga" if max(range(3), key=lambda k: L[k]) == p["correcta"] else "")
