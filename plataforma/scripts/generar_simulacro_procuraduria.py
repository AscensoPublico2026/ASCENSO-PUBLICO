"""Genera public/simulacro-gratis/procuraduria.html a partir de la plantilla del
simulacro profesional, con un banco propio de 20 preguntas del núcleo común del
concurso de la Procuraduría ("Mérito Construyendo Excelencia").

Las preguntas son originales, tipo juicio situacional, con distractores
plausibles (la opción "casi correcta" que se salta un paso, confunde términos
o mecanismos). Uso: python3 scripts/generar_simulacro_procuraduria.py
"""
import json
import pathlib
import re

BASE = pathlib.Path(__file__).resolve().parent.parent / "public" / "simulacro-gratis"
PLANTILLA = pathlib.Path(__file__).resolve().parent / "plantillas" / "simulacro.html"
DESTINO = BASE / "procuraduria.html"

R_PGN = ("PGN-EST", "Estructura y funciones de la Procuraduría")
R_DIS = ("PGN-DIS", "Derecho disciplinario (Ley 1952 de 2019 y Ley 2094 de 2021)")
R_MEC = ("PGN-MEC", "Mecanismos de protección de derechos")
R_CIU = ("PGN-CIU", "Relación con el ciudadano y derecho de petición")
R_COM = ("PGN-COM", "Competencias comportamentales")
R_DOC = ("PGN-DOC", "Gestión documental y ofimática")


def P(nivel, tema, ref, ctx, q, ops, correcta, expl):
    assert len(ops) == 3 and len(expl) == 3 and 0 <= correcta < 3
    return {"nivel": nivel, "tema": tema, "ref": ref[0], "refT": ref[1], "ctx": ctx, "q": q,
            "ops": ops, "correcta": correcta, "expl": expl}


PREGUNTAS = [
P("advanced", "Acción de cumplimiento: requisito de renuencia", R_MEC,
  "Usted trabaja en una procuraduría provincial. Un ciudadano le cuenta que una ley ordenó a la alcaldía de su municipio expedir un reglamento dentro de un plazo que venció hace ocho meses, y que la alcaldía no lo ha hecho. No ha dirigido ninguna solicitud previa a la administración y quiere demandar de inmediato ante el juez.",
  "Teniendo en cuenta lo que exige la Ley 393 de 1997, ¿qué le orienta hacer primero?",
  ["Radicar de una vez la acción de cumplimiento, porque el plazo de la ley ya venció y eso basta para acreditar el incumplimiento.",
   "Pedir primero por escrito a la alcaldía que cumpla el deber legal y acudir al juez si se ratifica o no contesta.",
   "Presentar una acción popular, dado que el reglamento beneficiaría a toda la comunidad del municipio y no solo a él."],
  1,
  ["El vencimiento del plazo no reemplaza la constitución en renuencia, que es un requisito de procedibilidad de la acción.",
   "Correcto: la ley exige reclamar antes a la autoridad; si esta se ratifica o guarda silencio en diez días, queda habilitada la vía judicial.",
   "La acción popular protege derechos e intereses colectivos; aquí lo que se persigue es el cumplimiento de un deber legal concreto."]),

P("intermediate", "Derecho de petición: término para documentos", R_CIU,
  "Llega a la ventanilla una petición en la que un ciudadano solicita copia de cuatro actas del comité de contratación. No pide concepto ni interpretación de normas: solo las copias. El funcionario de turno duda entre contarle quince o treinta días hábiles para responder.",
  "¿Cuál es el término general para responder una petición de documentos e información?",
  ["Quince días hábiles, que es el término general aplicable a las peticiones presentadas en interés particular o general.",
   "Treinta días hábiles, por tratarse de documentos que deben recopilarse en varias dependencias de la entidad.",
   "Diez días hábiles siguientes a su recepción."],
  2,
  ["Quince días hábiles corresponde a las peticiones en interés particular o general, que son una categoría distinta.",
   "Treinta días hábiles corresponde a las consultas sobre materias a cargo de la entidad, no a la entrega de copias.",
   "Correcto: el CPACA fija diez días hábiles para las peticiones de documentos e información como la del caso."]),

P("advanced", "Derecho de petición: cuando no se alcanza a responder", R_CIU,
  "Faltan dos días para que venza el término de una petición que exige consolidar información de cinco dependencias. Tres ya respondieron; las otras dos avisaron que necesitan una semana más. El coordinador propone esperar a tener todo y responder cuando el informe esté completo.",
  "¿Cuál es la actuación correcta?",
  ["Informar al peticionario antes del vencimiento, explicando los motivos y señalando el plazo razonable en que se responderá.",
   "Responder con la información de las tres dependencias que ya contestaron y registrar la petición como atendida.",
   "Esperar a tener la información completa y responder cuando se consolide, dejando constancia del motivo del retraso."],
  0,
  ["Correcto: el CPACA obliga a informar antes del vencimiento, con los motivos de la demora y el nuevo plazo de respuesta.",
   "Una respuesta parcial presentada como definitiva no satisface el derecho de petición, que exige respuesta de fondo.",
   "Dejar vencer el término sin informar vulnera el derecho de petición, por más que después se deje constancia."]),

P("advanced", "Sanciones disciplinarias según la falta", R_DIS,
  "Concluido el juzgamiento, se acreditó que un servidor incurrió en una falta calificada como gravísima y que lo hizo a título de culpa grave: no hubo dolo ni culpa gravísima. El investigado no tiene antecedentes y reparó parcialmente el daño antes del fallo.",
  "¿Qué sanción corresponde imponer?",
  ["Destitución e inhabilidad general, que es la sanción que el Código prevé para todas las faltas calificadas como gravísimas.",
   "Suspensión en el ejercicio del cargo e inhabilidad especial, por el término que fije el fallo dentro del rango legal.",
   "Multa, porque la culpa grave recibe en el Código el mismo tratamiento que las faltas leves cometidas con dolo."],
  1,
  ["La destitución e inhabilidad general se reserva a las gravísimas dolosas o realizadas con culpa gravísima.",
   "Correcto: la combinación de falta gravísima con culpa conduce a suspensión e inhabilidad especial.",
   "La multa corresponde a las faltas leves dolosas; el grado de culpa no modifica la calificación de la falta."]),

P("advanced", "Poder disciplinario preferente", R_PGN,
  "La oficina de control interno disciplinario de una alcaldía adelanta desde hace cinco meses una investigación contra el secretario de infraestructura. Ya practicó ocho testimonios y el expediente está en etapa de pruebas. La Procuraduría comunica que asume el conocimiento del asunto.",
  "¿Qué efecto produce esa comunicación sobre la actuación de la alcaldía?",
  ["La oficina queda desplazada, remite el expediente a la Procuraduría y se abstiene de continuar conociendo el asunto.",
   "La oficina conserva la competencia y la Procuraduría pasa a vigilar su trámite mediante informes periódicos.",
   "Lo actuado por la oficina queda sin efectos y la investigación debe rehacerse íntegramente ante la Procuraduría."],
  0,
  ["Correcto: la competencia se desplaza y lo actuado válidamente se remite, de modo que los testimonios no se pierden.",
   "El poder preferente no se agota en pedir informes: implica asumir el conocimiento del asunto y decidirlo.",
   "Las pruebas practicadas con las formalidades legales conservan su validez; repetirlas sería un desgaste innecesario."]),

P("advanced", "Separación entre instrucción y juzgamiento", R_DIS,
  "El mismo funcionario que adelantó la investigación, practicó las pruebas y formuló el pliego de cargos pretende ahora dictar el fallo de primera instancia. Sostiene que conoce el expediente mejor que nadie y que el investigado no ha objetado nada al respecto.",
  "¿Es admisible bajo el Código General Disciplinario reformado?",
  ["Sí, siempre que el investigado no formule objeción expresa dentro del traslado del pliego de cargos.",
   "Sí, puesto que la separación entre instrucción y juzgamiento solo rige para las faltas calificadas como gravísimas.",
   "No: la reforma garantiza que quien instruye la actuación no sea quien la juzga y profiere el fallo."],
  2,
  ["La garantía de imparcialidad no es renunciable por el investigado ni depende de que este la objete.",
   "La separación no distingue según la gravedad de la falta: rige para toda la actuación disciplinaria.",
   "Correcto: es uno de los ejes de la Ley 2094 de 2021 y desarrolla el debido proceso."]),

P("intermediate", "Elección del Procurador General", R_PGN,
  "Una periodista prepara una nota sobre el próximo relevo en la Procuraduría y le pide confirmar el procedimiento. En su borrador escribió que el Presidente designa al Procurador de una lista que le envía la Corte Constitucional, para un período de cinco años prorrogable.",
  "¿Cuál es el procedimiento que establece el artículo 276 de la Constitución?",
  ["Lo elige el Senado para un período de cuatro años, de terna del Presidente, la Corte Suprema y el Consejo de Estado.",
   "Lo elige el Congreso en pleno para un período de cuatro años, por mayoría calificada y sin terna previa de postulantes.",
   "Lo designa el Presidente de la República para un período de cuatro años, en ejercicio de su facultad nominadora."],
  0,
  ["Correcto: Senado, cuatro años y terna integrada por el Presidente, la Corte Suprema de Justicia y el Consejo de Estado.",
   "La elección corresponde al Senado y no al Congreso en pleno, y sí existe una terna previa de tres postulantes.",
   "La designación directa por el Ejecutivo comprometería la independencia del órgano de control."]),

P("intermediate", "Quiénes ejercen el Ministerio Público", R_PGN,
  "En la inducción de los contratistas nuevos, el expositor afirma que el Ministerio Público es únicamente la Procuraduría General de la Nación y que las personerías municipales son dependencias de las alcaldías. Un asistente pregunta entonces a quién acude un ciudadano que no puede desplazarse a la capital del departamento.",
  "¿Qué precisión corresponde hacer?",
  ["La Procuraduría ejerce el Ministerio Público junto con la Contraloría General de la República y las contralorías territoriales.",
   "La Procuraduría, la Defensoría del Pueblo y las personerías distritales y municipales integran el Ministerio Público.",
   "La Procuraduría ejerce el Ministerio Público y la Defensoría y las personerías son entidades de apoyo sin esa condición."],
  1,
  ["El control fiscal es una función distinta y las contralorías conforman una rama de control separada.",
   "Correcto: el artículo 118 de la Constitución lo integra con esas tres, y por eso el ciudadano puede acudir a su personería.",
   "Es el error del expositor: deja al ciudadano sin la puerta de entrada más cercana, que es la personería municipal."]),

P("basic", "Habeas corpus", R_MEC,
  "Una persona lleva cuarenta y ocho horas retenida en una estación sin haber sido puesta a disposición de autoridad judicial. Su familia acude a la personería municipal, que a su vez consulta a la procuraduría provincial sobre el mecanismo que debe invocarse de inmediato.",
  "¿Qué mecanismo procede?",
  ["La acción de tutela, por tratarse de la vulneración del derecho fundamental a la libertad personal del retenido.",
   "El derecho de petición dirigido a la autoridad que practicó la retención, para que informe su fundamento legal.",
   "El habeas corpus, que debe resolverse en treinta y seis horas por el juez ante quien se presente la solicitud."],
  2,
  ["Para la libertad personal el ordenamiento prevé un mecanismo específico y más expedito que la tutela.",
   "El derecho de petición no es el mecanismo para recuperar la libertad de una persona retenida ilegalmente.",
   "Correcto: el artículo 30 de la Constitución lo prevé para la privación ilegal o prolongada de la libertad."]),

P("intermediate", "Habeas data", R_MEC,
  "Un ciudadano descubre que en una base de datos de una entidad pública figura una anotación que lo reporta como sancionado, cuando la sanción fue revocada hace tres años. Pide que se corrija el registro y que la corrección se informe a quienes consultaron el dato.",
  "¿Qué derecho está ejerciendo?",
  ["El derecho a la intimidad, que impide la circulación de información personal sin autorización previa del titular.",
   "El habeas data: conocer, actualizar y rectificar las informaciones recogidas sobre él en bancos de datos.",
   "El derecho de acceso a los documentos públicos, que le permite consultar la información que produce la entidad."],
  1,
  ["La intimidad es un derecho conexo, pero no comprende por sí misma la facultad de rectificar un dato erróneo.",
   "Correcto: es el contenido del artículo 15 de la Constitución e incluye la corrección del registro inexacto.",
   "El acceso a documentos públicos se refiere a la información de la entidad, no a los datos propios del solicitante."]),

P("basic", "Término para fallar una tutela", R_MEC,
  "Su despacho recibe el traslado de una tutela instaurada contra una entidad territorial. El jefe pregunta de cuánto tiempo dispone el juez para resolverla, porque quiere programar el concepto del Ministerio Público sin que llegue tarde al expediente.",
  "¿Cuál es el término de la acción de tutela?",
  ["Treinta días hábiles contados a partir del auto que admite la solicitud de amparo presentada por el accionante.",
   "Diez días siguientes a la solicitud, dentro de los cuales el juez practica pruebas y resuelve sobre el amparo.",
   "Tres meses, término dentro del cual el juez debe vincular a los interesados y decidir sobre la protección."],
  1,
  ["Ese término no corresponde a la tutela, cuyo trámite es preferente y sumario por mandato constitucional.",
   "Correcto: el artículo 86 de la Constitución fija un término máximo de diez días, lo que explica la urgencia.",
   "Tres meses desconoce por completo la naturaleza preferente y sumaria que la Constitución le imprime."]),

P("intermediate", "Atención a un ciudadano molesto", R_COM,
  "Un ciudadano llega a la ventanilla gritando porque lleva tres meses esperando respuesta a una petición. Al verificar el sistema, usted confirma que la petición está vencida y sin respuesta desde hace sesenta días. Hay seis personas más en la fila.",
  "¿Cuál es la actuación correcta?",
  ["Atenderlo en un espacio aparte, verificar el estado real de la petición y darle una respuesta concreta sobre el plazo.",
   "Pedirle que se retire y que regrese cuando esté más tranquilo, para no afectar la atención de las demás personas.",
   "Explicarle que la demora corresponde a otra dependencia e indicarle a dónde debe dirigirse a presentar su reclamo."],
  0,
  ["Correcto: bajar la tensión y resolver el problema de fondo, que en este caso efectivamente existe.",
   "Pedirle que se retire no resuelve una demora real que es responsabilidad de la entidad.",
   "Trasladarle la responsabilidad a otra dependencia deja al ciudadano exactamente donde estaba."]),

P("advanced", "Trabajo en equipo bajo presión", R_COM,
  "Una compañera se incapacitó por un mes y su carga quedó repartida entre dos personas, incluido usted. Siete expedientes tienen términos que vencen en las próximas dos semanas y usted alcanza a atender cuatro trabajando a ritmo normal.",
  "¿Cuál es la conducta más profesional?",
  ["Avanzar lo que alcance sin informar nada, para no dar la impresión de que se está quejando de la carga adicional.",
   "Solicitar que se le retire toda la carga adicional, que corresponde a un empleo distinto del que usted desempeña.",
   "Hacer inventario de los asuntos y sus términos, priorizar lo perentorio e informar por escrito qué se alcanza."],
  2,
  ["Callar hace que el vencimiento de los términos termine cayendo sobre quien no avisó a tiempo.",
   "Rechazar en bloque la carga adicional no resuelve la continuidad del servicio ni los términos que corren.",
   "Correcto: inventario, priorización y aviso oportuno permiten que el jefe decida con información."]),

P("basic", "Instrumento que fija los tiempos de conservación", R_DOC,
  "Un compañero pregunta cuánto tiempo debe conservarse en el archivo de gestión un tipo documental que su dependencia produce cada mes. Dice que en su oficina anterior lo guardaban dos años y que así lo viene haciendo aquí desde que llegó.",
  "¿Dónde está la respuesta?",
  ["En el criterio del jefe de cada dependencia, que conoce la utilidad de cada documento para su propia gestión.",
   "En el Código General Disciplinario, que regula la conservación de los expedientes y los documentos oficiales.",
   "En las tablas de retención documental de la entidad, que fijan tiempos de conservación y disposición final."],
  2,
  ["No es una decisión individual de cada jefe ni puede resolverse por la costumbre de otra entidad.",
   "El Código Disciplinario no regula la conservación documental, que tiene su propio marco normativo.",
   "Correcto: las tablas de retención son el instrumento archivístico que define esos tiempos para cada serie."]),

P("intermediate", "Queja o reclamo", R_CIU,
  "Un ciudadano manifiesta en la ventanilla su inconformidad porque considera que un servidor lo atendió de manera descortés y porque, además, el trámite que vino a hacer no se le prestó en el tiempo que la entidad anuncia en su carta de trato digno.",
  "¿Cómo se clasifican esas dos manifestaciones?",
  ["Las dos son quejas, puesto que ambas expresan la inconformidad del ciudadano frente al servicio recibido.",
   "La primera es una queja contra la conducta del servidor; la segunda, un reclamo por la prestación del servicio.",
   "Las dos son reclamos, dado que en ambos casos lo que se cuestiona es la forma en que la entidad presta el servicio."],
  1,
  ["No son equivalentes: una apunta a la conducta de una persona y la otra, a la prestación del servicio.",
   "Correcto: la queja se dirige contra la conducta de un servidor y el reclamo, contra la prestación del servicio.",
   "La inconformidad por el trato recibido de un servidor corresponde a una queja, no a un reclamo."]),

P("advanced", "Impedimento por conflicto de interés", R_DIS,
  "A usted le corresponde decidir una actuación en la que una de las partes es la empresa donde trabaja su cónyuge desde hace seis años. Usted no tiene interés económico directo, se considera capaz de decidir con objetividad y el término para resolver vence en cuatro días.",
  "¿Cuál es la conducta correcta?",
  ["Declararse impedido ante quien corresponda y abstenerse de actuar mientras se resuelve el impedimento.",
   "Decidir con objetividad y dejar constancia en el expediente de que la relación no afecta su criterio profesional.",
   "Consultarlo verbalmente con el jefe inmediato y continuar si él no advierte inconveniente en que usted decida."],
  0,
  ["Correcto: se manifiestan los hechos y la causal por escrito, y no se actúa mientras la instancia competente decide.",
   "La imparcialidad subjetiva no basta: la ley presume el riesgo y exige declararlo formalmente.",
   "Una autorización verbal no sustituye el trámite formal del impedimento ni sanea la actuación."]),

P("intermediate", "Negar información reservada", R_CIU,
  "Un periodista pide copia completa de un expediente disciplinario que está en etapa de investigación. Argumenta que se trata de información pública y que el caso es de interés general porque involucra recursos de un municipio.",
  "¿Qué corresponde responder?",
  ["Negar la petición sin explicación, dado que la reserva de la actuación disciplinaria no admite ningún matiz.",
   "Explicar que la actuación en curso tiene reserva y que el acceso de terceros está limitado, e informar su estado.",
   "Entregarle el expediente completo si firma un compromiso de confidencialidad sobre la información que reciba."],
  1,
  ["Toda negativa debe motivarse: responder sin explicación vulnera el derecho de petición del solicitante.",
   "Correcto: se explica la reserva, se entrega lo que sí es público y se motiva la respuesta al peticionario.",
   "Un compromiso privado de confidencialidad no levanta una reserva que la ley establece."]),

P("intermediate", "Regalos de un contratista", R_COM,
  "Un proveedor con contrato vigente envía a su oficina una canasta navideña con productos importados. La tarjeta agradece la colaboración del equipo durante el año y tres compañeros ya recibieron canastas iguales, que según dicen es la costumbre de todos los diciembres.",
  "¿Cuál es la conducta correcta?",
  ["Aceptarla y repartirla entre el equipo de la dependencia, de modo que ningún servidor obtenga un provecho individual.",
   "Aceptarla siempre que su valor comercial no supere el equivalente a un salario mínimo legal mensual vigente.",
   "No aceptarla, devolverla y dejar constancia del hecho ante el superior o el canal institucional previsto."],
  2,
  ["Repartirla no cambia la naturaleza de la dádiva ni el hecho de que proviene de un contratista en ejecución.",
   "No existe un umbral de valor que autorice recibir obsequios de un contratista con contrato vigente.",
   "Correcto: rechazar, devolver y documentar protege al servidor, a la entidad y al proceso contractual."]),

P("advanced", "Prioridades con dos urgencias", R_COM,
  "El mismo día vencen tres cosas: un término procesal perentorio en un expediente, el informe mensual de gestión que pidió el jefe y una reunión de equipo convocada hace una semana. Usted alcanza a cumplir dos de las tres y el jefe estará en la reunión.",
  "¿Cuál es el criterio profesional correcto?",
  ["Atender primero el informe de gestión y la reunión, que son los compromisos adquiridos directamente con el superior.",
   "Avanzar parcialmente en las tres, de modo que las tres queden atendidas y registren algún nivel de cumplimiento.",
   "Atender primero el término procesal perentorio y gestionar con el jefe la reprogramación de lo demás."],
  2,
  ["La jerarquía no desplaza un término legal que no admite prórroga y cuyo incumplimiento puede generar nulidades.",
   "Cumplir las tres a medias garantiza fallar justamente en la que no admite remedio posterior.",
   "Correcto: se prioriza lo perentorio e irreversible y se comunica, en lugar de decidir en silencio."]),

P("intermediate", "Excel: contar con una condición", R_DOC,
  "En una hoja de cálculo, la columna B tiene el estado de cada uno de los 300 expedientes de la dependencia: «En trámite», «Archivado» o «Fallado». Le piden saber cuántos están archivados y el reporte se entrega en una hora.",
  "¿Qué función resuelve ese conteo?",
  ["CONTAR.SI, indicando el rango de la columna B y el criterio «Archivado» entre comillas.",
   "CONTAR, indicando el rango de la columna B, que devuelve el número de celdas con contenido dentro del rango.",
   "SUMAR.SI, indicando el rango de la columna B y el criterio «Archivado» para obtener el total de registros."],
  0,
  ["Correcto: CONTAR.SI cuenta las celdas de un rango que cumplen una condición, que es exactamente lo que se pide.",
   "CONTAR cuenta celdas con contenido numérico y no permite filtrar por el texto del estado del expediente.",
   "SUMAR.SI suma valores de un rango según una condición; aquí no hay valores que sumar sino registros que contar."]),
]


def main():
    assert len(PREGUNTAS) == 20, len(PREGUNTAS)
    s = PLANTILLA.read_text(encoding="utf-8")
    i = s.index("const preguntas=")
    j = s.index("];", i) + 2
    s = s[:i] + "const preguntas=" + json.dumps(PREGUNTAS, ensure_ascii=False) + ";" + s[j:]
    s = s.replace('const NIVEL_ID="profesional";', 'const NIVEL_ID="procuraduria";')
    # Textos de la página
    s = re.sub(r"<title>.*?</title>", "<title>Simulacro gratis Procuraduría 2026 · Núcleo común — Ascenso Público</title>", s, count=1, flags=re.S)
    s = s.replace("🎁 Simulacro Gratis · Nivel Profesional", "🎁 Simulacro Gratis · Concurso Procuraduría 2026")
    s = s.replace("Simulacro CNSC Gratis<br>Nivel Profesional", "Simulacro Procuraduría<br>Núcleo común")
    s = s.replace(
        "20 preguntas de juicio situacional tipo CNSC sobre el Estado, la función pública y las competencias del nivel profesional. Mide tu preparación para la prueba escrita y descubre qué reforzar.",
        "20 preguntas tipo caso sobre la Procuraduría, derecho disciplinario, mecanismos de protección, atención al ciudadano, gestión documental y competencias comportamentales. Mide tu preparación para la prueba escrita del concurso «Mérito Construyendo Excelencia».")
    s = s.replace('<span class="badge">🎓 Nivel Profesional</span>', '<span class="badge">⚖️ Procuraduría</span>')
    s = s.replace("como en la prueba real de la CNSC", "como en la prueba escrita del concurso")
    s = s.replace("igual que en el examen oficial", "igual que en el examen real")
    s = s.replace("SIM-GRATIS-PRO", "SIM-GRATIS-PGN")
    s = s.replace("Material independiente, no afiliado a la CNSC", "Material independiente, no afiliado a la Procuraduría ni a la Universidad de Antioquia")
    DESTINO.write_text(s, encoding="utf-8")
    print("OK", DESTINO)


if __name__ == "__main__":
    main()
