import json
fl = [
 {"f": "¿Qué ajuste ordena el art. 260-3 ET cuando el precio o margen del contribuyente queda fuera del rango de plena competencia?", "b": "Se toma como precio o margen de plena competencia la mediana del rango."},
 {"f": "¿Cómo se entrega la documentación comprobatoria de precios de transferencia (art. 260-5 ET)?", "b": "Se presenta de oficio, en los plazos y condiciones que fije el decreto; se conserva y se pone a disposición de la DIAN."},
 {"f": "¿Qué pasa con las operaciones con jurisdicciones no cooperantes si el contribuyente no alcanza los topes?", "b": "Quedan sometidas al régimen de precios de transferencia de todos modos (art. 260-7, par. 2 ET)."},
 {"f": "¿Cuál es la firmeza de la declaración de renta de un contribuyente sujeto a precios de transferencia?", "b": "Cinco años desde el vencimiento del plazo para declarar (Ley 2010 de 2019; Oficio DIAN 9219 de 2026)."},
 {"f": "¿Cuándo se gravan las rentas pasivas de una entidad controlada del exterior?", "b": "En el año en que la ECE las obtiene, en cabeza del residente con participación ≥ 10 %, aunque no se distribuyan (arts. 883-886 ET)."},
 {"f": "¿Tiene Colombia convenio para evitar la doble imposición con Noruega?", "b": "No. Antes de invocar un CDI hay que verificar que exista y esté vigente."},
 {"f": "¿Qué diferencia el lavado de activos de la financiación del terrorismo?", "b": "En el lavado (art. 323 C.P.) el problema es el origen ilícito; en la FT (art. 345 C.P.) es el destino, con recursos que pueden ser lícitos."},
 {"f": "¿Qué hace la UIAF y qué hace la Fiscalía?", "b": "La UIAF (Ley 526 de 1999) hace inteligencia financiera: recibe, centraliza y analiza. La Fiscalía investiga y acusa penalmente."},
 {"f": "¿Qué estándar exige el reporte de operación sospechosa?", "b": "Sospecha razonada, basada en señales convergentes sin explicación plausible; no exige certeza ni prueba plena, ni tiene monto mínimo."},
 {"f": "¿Qué no puede hacer el Gestor I frente a un ROS?", "b": "Informar al reportado (reserva, Ley 1121 de 2006), suspender por ello la fiscalización o firmar actos que corresponden al jefe."},
]
P = []
def q(nivel, tema, ctx, qq, ops, correcta, expl):
    P.append(dict(nivel=nivel, tema=tema, ctx=ctx, q=qq, ops=ops, correcta=correcta, expl=expl))

q("b","Ajuste a la mediana",
 "Una Gestora I de la división de fiscalización revisa el estudio de precios de transferencia de una distribuidora de repuestos que compra toda su mercancía a su casa matriz en el exterior. El estudio aplica el método de márgenes transaccionales con el margen operacional sobre ventas. La distribuidora obtuvo un margen del 0,8 %, mientras que el rango intercuartil de distribuidores independientes comparables va del 3,1 % al 7,5 %, con una mediana del 5,2 %. La gestora verificó que los comparables son adecuados y que el análisis funcional describe bien a un distribuidor de riesgo limitado. Su jefe le pide que deje listo el cálculo del ajuste para el proyecto de requerimiento especial.",
 "La gestora debe definir a qué valor llevar el margen de la distribuidora en el proyecto que entregará a su jefe. Según el régimen de precios de transferencia vigente, ¿cuál es el cálculo que debe incluir en el proyecto de requerimiento especial?",
 ["Llevar el margen al 3,1 %, que es el límite inferior del rango, porque ese es el valor de plena competencia más favorable al contribuyente y reduce el riesgo de que el acto se caiga.",
  "Llevar el margen a la mediana del rango (5,2 %), porque el resultado del contribuyente está por fuera del rango y así lo ordena el art. 260-3 ET, con la motivación técnica del ajuste.",
  "Llevar el margen al 7,5 %, que es el límite superior del rango, porque el contribuyente no demostró su plena competencia y debe asumir el escenario de mayor utilidad."],
 1,
 ["Incorrecto. El art. 260-3 ET no ordena ajustar al extremo inferior; cuando el resultado queda fuera del rango, el valor de plena competencia es la mediana.",
  "✔ Correcto. Fuera del rango se ajusta a la mediana; la gestora prepara el cálculo y su sustento técnico para el proyecto que firmará quien tenga la competencia.",
  "Incorrecto. Ajustar al extremo superior no tiene base normativa; la regla es la mediana del rango, no el valor más alto."])

q("b","Jurisdicciones no cooperantes",
 "Un Gestor I recibe para estudio el expediente de una comercializadora de textiles con patrimonio bruto de 40.000 UVT e ingresos brutos de 30.000 UVT. La sociedad paga intereses y honorarios a una vinculada domiciliada en una jurisdicción incluida en el decreto vigente de jurisdicciones no cooperantes, de baja o nula imposición. No presentó declaración informativa ni documentación comprobatoria. En la visita, su revisor fiscal afirma que, como la empresa no llega a los topes de 100.000 UVT de patrimonio ni de 61.000 UVT de ingresos, no tenía ninguna obligación de precios de transferencia y pide que así quede consignado en el acta.",
 "El Gestor I debe dejar consignada en el acta y en su informe la posición de la administración sobre las obligaciones de la comercializadora frente a los pagos a esa vinculada. ¿Cuál es la posición jurídicamente correcta que debe registrar?",
 ["Que las operaciones con sujetos ubicados en jurisdicciones no cooperantes quedan sometidas al régimen aunque no se superen los topes, por lo cual procede analizar las sanciones del art. 260-11 ET.",
  "Que el revisor fiscal tiene razón, porque los topes de patrimonio e ingresos son la condición para cualquier obligación del régimen, de modo que solo cabe verificar la retención en la fuente.",
  "Que la sociedad estaba obligada solo a la declaración informativa, pero no a la documentación comprobatoria, porque esta se entrega únicamente cuando la DIAN la requiere."],
 0,
 ["✔ Correcto. El art. 260-7, par. 2 ET somete esas operaciones al régimen sin importar los topes, y el art. 260-11 sanciona la falta de documentación y de declaración informativa.",
  "Incorrecto. Los topes no aplican a las operaciones con jurisdicciones no cooperantes, que tienen un régimen reforzado de documentación y deducibilidad.",
  "Incorrecto. La documentación comprobatoria se presenta de oficio en los plazos del decreto (art. 260-5 ET), no solo cuando la DIAN la pide."])

q("b","Reserva del ROS",
 "Una Gestora I adelanta la fiscalización de una importadora de electrodomésticos. Hace dos semanas elevó por el conducto interno de la DIAN un reporte de operación sospechosa porque los giros al exterior van a un tercero distinto del proveedor, la empresa no tiene bodega y sus compras se multiplicaron por veinte en un año. Hoy, en una reunión para revisar los soportes de costos solicitados en un requerimiento ordinario, el representante legal le pregunta directamente si la empresa “fue reportada a la UIAF por lavado”, porque un banco le cerró una cuenta y él cree que la DIAN tuvo algo que ver.",
 "La gestora debe responder a la pregunta del representante legal sin afectar ni la actuación administrativa en curso ni el sistema de prevención. Teniendo en cuenta la reserva del reporte y el objeto del requerimiento ya notificado, ¿cuál es la respuesta que corresponde a su función y a las normas aplicables?",
 ["Confirmarle que existe un reporte, explicándole que es solo preventivo y que no implica acusación, para que confíe en el proceso y colabore con la entrega de los soportes pedidos.",
  "Suspender la reunión y remitir el expediente a la Fiscalía, porque la pregunta muestra que el contribuyente sospecha del reporte y la actuación administrativa ya no puede seguir.",
  "No confirmar ni negar la existencia de reportes, explicarle el objeto del requerimiento notificado y continuar la revisión de los soportes, dejando constancia de la reunión."],
 2,
 ["Incorrecto. La Ley 1121 de 2006 prohíbe informar al reportado que su caso se comunicó a la UIAF; confirmarlo, aunque sea con buena intención, rompe la reserva.",
  "Incorrecto. El reporte no suspende la actuación administrativa, y la DIAN no remite a la Fiscalía por esa razón; los procesos siguen en paralelo.",
  "✔ Correcto. La gestora guarda la reserva del ROS, mantiene el objeto de la actuación notificada y deja trazabilidad, sin detener el proceso."])

q("b","Convenios para evitar la doble imposición",
 "Un Gestor I revisa los pagos al exterior de una empresa de ingeniería que contrató asistencia técnica con una sociedad noruega. La empresa aplicó una retención en la fuente reducida y, en la respuesta a un requerimiento ordinario, explica que lo hizo “en virtud del convenio para evitar la doble imposición entre Colombia y Noruega”. Adjunta un certificado de residencia fiscal de la sociedad noruega expedido por la autoridad tributaria de ese país y un concepto de una firma de abogados. El jefe de división le pide al Gestor I que analice si la tarifa reducida tiene soporte y le presente su conclusión.",
 "El Gestor I debe establecer si la retención reducida aplicada por la empresa tiene fundamento jurídico antes de proyectar cualquier actuación. Considerando los soportes aportados por la empresa y los convenios vigentes, ¿cuál es el análisis correcto que debe presentar a su jefe?",
 ["Que la tarifa reducida es procedente, porque el certificado de residencia fiscal expedido por la autoridad noruega es el único requisito que exigen los convenios para aplicar sus beneficios.",
  "Que no hay soporte convencional, porque Colombia no tiene CDI vigente con Noruega; la retención debe revisarse con la tarifa de la ley interna y proyectarse la actuación que corresponda.",
  "Que la tarifa es procedente si la firma de abogados ratifica su concepto por escrito, porque la existencia de un convenio puede acreditarse con la opinión de un experto en derecho tributario."],
 1,
 ["Incorrecto. El certificado de residencia sirve para aplicar un convenio existente; si el CDI no existe, no hay beneficio que aplicar.",
  "✔ Correcto. Colombia no tiene CDI con Noruega; sin convenio vigente rige la tarifa interna, y el Gestor I sustenta la propuesta de corrección.",
  "Incorrecto. La existencia de un tratado se verifica en su ley aprobatoria y su vigencia, no con conceptos de particulares."])

q("i","Entidades controladas del exterior",
 "Una Gestora I investiga a un empresario residente en Colombia que es dueño del 35 % de una sociedad constituida en el exterior. Según la información del Registro Único de Beneficiarios Finales y los estados financieros obtenidos por intercambio de información, el 92 % de los ingresos de esa sociedad corresponde a intereses de préstamos y regalías por una marca, y en los últimos tres años no ha distribuido dividendos. El empresario no incluyó ninguna renta de esa sociedad en sus declaraciones de renta. Su contador alega que “mientras la sociedad no reparta utilidades, en Colombia no hay nada que declarar” y que el control lo tiene otro socio con el 65 %.",
 "La gestora debe definir el tratamiento de las rentas de la sociedad del exterior para el informe y el proyecto de actuación que entregará a su jefe. Frente a los dos argumentos del contador, el del momento de realización y el de la falta de control mayoritario, ¿cuál es el análisis correcto?",
 ["Que el contador tiene razón en cuanto al momento, porque los ingresos de fuente extranjera de un residente solo se realizan cuando la sociedad reparte dividendos, aunque sí debe declarar la inversión como activo.",
  "Que el régimen no aplica porque el empresario no es el socio mayoritario, de modo que solo procede verificar que la participación aparezca en la declaración de activos en el exterior.",
  "Que el empresario, residente con participación igual o superior al 10 % en una ECE controlada por residentes, debe reconocer su parte de las rentas pasivas en el año en que la sociedad las obtuvo."],
 2,
 ["Incorrecto. El régimen ECE existe precisamente para gravar las rentas pasivas en el año en que la entidad las obtiene, sin esperar la distribución (art. 886 ET).",
  "Incorrecto. El art. 883 ET obliga a quien tenga el 10 % o más; no exige ser mayoritario, siempre que la entidad esté controlada por residentes.",
  "✔ Correcto. Con ingresos pasivos superiores al 80 % todas las rentas se tratan como pasivas, y el residente con 10 % o más debe declararlas en proporción a su participación."])

q("i","Información del exterior",
 "Un Gestor I recibe, por el canal interno de la autoridad competente, información del intercambio automático (CRS) que muestra que un médico residente en Colombia tiene una cuenta en el exterior con un saldo equivalente a 4.000 millones de pesos, no incluida en su declaración de renta ni en su declaración de activos en el exterior. Un compañero de otra área, que conoce al médico, le sugiere que le envíe la información a su correo personal para que “aclare el asunto sin tanto trámite”. Otro compañero opina que esa información no puede usarse en ningún proceso porque es confidencial y solo sirve para estadística.",
 "El Gestor I debe decidir cómo usar la información recibida para avanzar en la investigación, respetando las reglas del intercambio y el derecho de defensa. Frente a las dos opiniones de sus compañeros, ¿cuál es la actuación que corresponde a su función de profesional de fiscalización?",
 ["Usarla como insumo para orientar la investigación, proyectar el requerimiento o emplazamiento que corresponda e incorporarla formalmente al expediente si se usará como prueba, sin difundirla fuera del proceso.",
  "Abstenerse de usarla en el proceso, porque la confidencialidad del intercambio automático impide que la información recibida sirva para modificar una declaración, y archivarla con el resto de los reportes.",
  "Enviarle al médico por correo personal la copia del reporte recibido, porque así se le garantiza el derecho de defensa de inmediato y se evita un trámite largo que congestiona la división."],
 0,
 ["✔ Correcto. La información orienta la investigación y, incorporada con las formalidades, puede ser prueba controvertible; se maneja por canales institucionales y con reserva.",
  "Incorrecto. La confidencialidad limita a quién se revela y para qué se usa, pero no impide su uso tributario dentro del proceso con las formalidades legales.",
  "Incorrecto. Reenviar el reporte por correo personal rompe la confidencialidad y la reserva; el derecho de defensa se garantiza dentro del proceso, no por canales informales."])

q("i","Señales de alerta",
 "Una Gestora I revisa a una importadora de alimentos con dieciocho años de operación, setenta empleados y un historial de cumplimiento estable. Encuentra una declaración de importación de aceite con un valor 11 % inferior al precio de referencia del mes. Al pedir explicación mediante un requerimiento ordinario, la empresa aporta la factura del proveedor, el contrato marco con descuento por volumen anual y los pagos canalizados al mismo proveedor, todo coherente con sus compras de años anteriores. Un compañero insiste en que “toda subvaloración es lavado” y en que hay que reportarla a la UIAF de inmediato para cubrirse.",
 "La gestora debe decidir qué hacer con la alerta inicial después de recibir la explicación y los soportes de la empresa. Frente a la insistencia de su compañero en reportar de inmediato, ¿cuál es la actuación que refleja el criterio profesional esperado de un Gestor I?",
 ["Reportar la operación a la UIAF por precaución, porque cualquier diferencia frente al precio de referencia obliga a hacerlo sin importar la explicación que aporte el contribuyente.",
  "Documentar la explicación y los soportes, descartar la alerta con constancia en el expediente y continuar la verificación de valor en el marco de la actuación que corresponda.",
  "Informarle a la empresa que quedó bajo observación por posible lavado, para que en adelante ajuste sus precios a los de referencia y evite un reporte futuro a la UIAF."],
 1,
 ["Incorrecto. El ROS exige sospecha razonada; una señal aislada con explicación comercial soportada no la configura.",
  "✔ Correcto. No todo lo inusual es sospechoso: la gestora documenta por qué descarta la alerta y sigue con la verificación administrativa.",
  "Incorrecto. Comunicar al contribuyente una supuesta observación por lavado es improcedente y expone información del sistema de prevención."])

q("i","Firmeza en precios de transferencia",
 "Un Gestor I recibe en julio de 2026 un expediente de una sociedad sujeta al régimen de precios de transferencia. La declaración de renta del año gravable 2021 se presentó a tiempo y el plazo para declarar venció en abril de 2022. El análisis muestra que los pagos por servicios a una vinculada del exterior están por fuera del rango de plena competencia. Un compañero opina que la declaración ya quedó en firme porque pasaron tres años; otro dice que las declaraciones de los contribuyentes del régimen quedan en firme a los seis años; un tercero sostiene que nunca quedan en firme si hubo errores en la declaración informativa.",
 "El Gestor I debe establecer si todavía es posible proyectar el requerimiento especial para proponer el ajuste. Según la norma vigente sobre firmeza para estos contribuyentes, ¿cuál es la conclusión correcta que debe dejar en su informe al jefe de división?",
 ["Que la declaración quedó en firme en abril de 2025, porque la firmeza general de tres años aplica a todos los contribuyentes, incluidos los sujetos al régimen de precios de transferencia.",
  "Que la declaración nunca queda en firme mientras existan errores en la declaración informativa, por lo que no hay ninguna urgencia en notificar el requerimiento especial.",
  "Que la firmeza es de cinco años desde el vencimiento del plazo, hasta abril de 2027, de modo que el requerimiento especial debe notificarse antes de esa fecha."],
 2,
 ["Incorrecto. Los contribuyentes del régimen de precios de transferencia tienen una firmeza especial de cinco años, no la general de tres.",
  "Incorrecto. No existe una regla de firmeza indefinida por errores en la declaración informativa; esas fallas se sancionan por el art. 260-11 ET.",
  "✔ Correcto. Con la Ley 2010 de 2019 la firmeza es de cinco años; vencido el plazo en abril de 2022, la DIAN puede actuar hasta abril de 2027."])

q("i","Listas restrictivas",
 "Una Gestora I adelanta la verificación de una solicitud de devolución de saldo a favor de una exportadora de flores. Al consultar a los socios y al beneficiario final reportado en el RUB, encuentra que el nombre de uno de los socios coincide con el de una persona designada en una lista del Consejo de Seguridad de las Naciones Unidas. La fecha de nacimiento y la nacionalidad coinciden, pero en la lista no figura número de documento. Además, la exportadora fue creada hace siete meses, no tiene cultivos propios y sus exportaciones se multiplicaron por diez en el último trimestre.",
 "La gestora debe decidir cómo proceder frente a la coincidencia en la lista, que no es concluyente, y frente a las demás circunstancias de la exportadora. ¿Cuál es la actuación que corresponde a su función de investigación y reporte?",
 ["Verificar la identidad con los datos disponibles, dejar constancia de la consulta y, por las señales convergentes, elevar el reporte por el conducto interno mientras continúa la verificación de la devolución.",
  "Descartar la coincidencia porque la lista no trae número de documento, y continuar el trámite de la devolución como cualquier otro, ya que sin identificación plena no hay riesgo que analizar.",
  "Llamar al socio para preguntarle si es la persona designada en la lista, de modo que pueda aclarar la homonimia antes de cualquier reporte y así se respete su derecho al buen nombre."],
 0,
 ["✔ Correcto. Verifica sin prejuzgar, documenta y, con señales convergentes, reporta con reserva sin detener la verificación de la devolución.",
  "Incorrecto. La falta de número de documento no descarta la coincidencia; con fecha, nacionalidad y otras señales debe verificarse y elevarse.",
  "Incorrecto. Consultar al socio sobre la lista lo alerta y puede comprometer el reporte; la verificación se hace con las fuentes institucionales."])

q("a","Servicios intragrupo",
 "Un Gestor I tiene asignada la investigación de una filial colombiana de un grupo de cosméticos. La filial paga a su matriz un cargo anual por “servicios de gestión estratégica” equivalente al 4,5 % de sus ventas; el rango intercuartil de cargos por servicios similares entre independientes va del 2 % al 6 %. El estudio de la filial concluye que está dentro del rango. Sin embargo, al revisar el expediente no aparecen entregables, informes, actas, correos ni registros de horas que muestren la prestación, y los gerentes locales dicen en la visita que toman sus decisiones sin intervención de la matriz. Su jefe le pide un proyecto para la siguiente etapa.",
 "El Gestor I debe preparar la siguiente actuación con base en lo hallado y dentro de la competencia que le asignaron. Teniendo en cuenta que el estudio del contribuyente ubica el cargo dentro del rango, ¿cuál es el enfoque correcto para el proyecto que entregará a su jefe?",
 ["Cerrar la investigación sobre este punto, porque el cargo está dentro del rango intercuartil y, según el art. 260-3 ET, ese resultado demuestra por sí solo que la operación es de plena competencia.",
  "Proyectar el requerimiento de prueba de la prestación efectiva del servicio y, si no se acredita, sustentar la propuesta de desconocer el cargo, porque en servicios intragrupo se exige prestación y valor de mercado.",
  "Ajustar el cargo a la mediana del rango (4 %) en el proyecto de requerimiento especial, porque cuando no hay prueba del servicio el art. 260-3 ordena llevar el valor al punto central de los comparables."],
 1,
 ["Incorrecto. En servicios intragrupo estar dentro del rango no basta: el art. 260-3, par. 2 exige además probar que el servicio se prestó.",
  "✔ Correcto. Se exige la prueba de la prestación; sin ella, el pago no tiene sustento. El Gestor I proyecta la actuación dentro de su competencia y la sustenta.",
  "Incorrecto. La mediana se usa cuando el valor está fuera del rango; aquí el problema no es el precio sino la falta de prueba de que el servicio existió."])

q("a","Procesos paralelos",
 "Una Gestora I adelanta una fiscalización aduanera y cambiaria a una comercializadora de calzado. Encuentra sobrefacturación sistemática del 200 %, giros a una sociedad en otra jurisdicción que no es el proveedor de las facturas y una empresa sin empleados creada hace cuatro meses. Ya elevó el reporte de operación sospechosa por el conducto interno. Su coordinador le sugiere “congelar” el expediente administrativo hasta que la Fiscalía actúe, para no interferir, y pedirle al banco que bloquee las cuentas de la empresa mientras tanto. La gestora tiene asignada la proyección de los actos del proceso.",
 "La gestora debe definir cómo seguir con el expediente después de haber elevado el reporte, frente a las sugerencias de su coordinador. Teniendo en cuenta el alcance de la DIAN y el de su propio cargo, ¿cuál es la actuación correcta dentro de su competencia?",
 ["Suspender la actuación administrativa y solicitar al banco el bloqueo preventivo de las cuentas de la empresa, porque una vez reportada la operación la DIAN debe asegurar los recursos hasta que la Fiscalía asuma formalmente el caso.",
  "Esperar a que la UIAF le confirme si el caso será trasladado a la Fiscalía, y solo entonces decidir si continúa la fiscalización, para evitar decisiones contradictorias entre las autoridades.",
  "Continuar la fiscalización aduanera y cambiaria y proyectar los actos que correspondan, porque el reporte no la suspende, y advertir a su coordinador que el bloqueo de cuentas no es competencia de la DIAN."],
 2,
 ["Incorrecto. El reporte no suspende la actuación administrativa y la DIAN no ordena bloqueos por sospecha de lavado; eso corresponde a las autoridades del proceso penal o de extinción de dominio.",
  "Incorrecto. La fiscalización no depende de la respuesta de la UIAF; esperar pone en riesgo los términos y deja de cumplir la función administrativa.",
  "✔ Correcto. Los procesos son paralelos: la gestora sigue con su actuación, proyecta los actos y no promueve medidas para las que la DIAN no tiene competencia."])

q("a","Integridad y alcance del cargo",
 "Un Gestor I terminó el análisis de un caso de precios de transferencia y de una ECE de los socios de una constructora, y elevó un reporte de operación sospechosa por señales convergentes de lavado en una importadora del mismo grupo. Un viernes, el jefe de división está en vacaciones sin encargo designado y el término para notificar el requerimiento especial vence en tres semanas. Ese día, el asesor de la constructora le ofrece al Gestor I “una bonificación” si el requerimiento “no sale” y le sugiere que, como él conoce el caso, lo firme el mismo para cerrarlo de una vez con una propuesta favorable.",
 "El Gestor I debe actuar al mismo tiempo frente al ofrecimiento del asesor y frente al trámite del requerimiento especial, cuyo término sigue corriendo. ¿Cuál es la actuación que respeta la ley penal, el régimen disciplinario y el alcance de su cargo?",
 ["Rechazar el ofrecimiento, dejar constancia, informar y denunciar el cohecho por dar u ofrecer, y dejar listo el proyecto para que lo firme el funcionario competente o quien sea encargado antes del vencimiento.",
  "Rechazar el ofrecimiento sin dejar constancia escrita para no complicar el caso y firmar él mismo el requerimiento especial, porque es quien mejor conoce el expediente y el término se vencería si espera el regreso del jefe de división.",
  "Aceptar la bonificación para usarla como prueba del intento de soborno, informar luego al jefe a su regreso y aplazar el requerimiento especial hasta tener resuelto el tema disciplinario."],
 0,
 ["✔ Correcto. Rechaza y denuncia el cohecho (art. 407 C.P.) y respeta la competencia: proyecta el acto y gestiona la firma de quien está facultado dentro del término.",
  "Incorrecto. Sin constancia no hay trazabilidad del ofrecimiento, y firmar un acto reservado al jefe sin competencia lo expone a nulidad.",
  "Incorrecto. Recibir el dinero, aun con la intención de usarlo como prueba, compromete al servidor; y aplazar el acto pone en riesgo el término."])

json.dump({"flashcards": fl, "preguntas": P}, open("datos.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
for i,p in enumerate(P,1):
    L=[len(o) for o in p["ops"]]
    print(i,p["nivel"],len(p["ctx"]),len(p["q"]),L,"c",p["correcta"],"larga" if max(range(3),key=lambda k:L[k])==p["correcta"] else "")
