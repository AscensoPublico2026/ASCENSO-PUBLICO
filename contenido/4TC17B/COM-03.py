# -*- coding: utf-8 -*-
"""Día 8 · Objetividad (Nivel B) — 4TC-17."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='4TC17B-COM-03',
    archivo='4TC17B-COM-03-objetividad.html',
    dia=8,
    titulo_doc='Objetividad',
    h1='Objetividad',
    kicker='Día 8 · Competencias comportamentales',
    sub='La tercera competencia <strong>por perfil</strong> del <strong>Técnico en Criminalística 4TC-17</strong>, exigida en <strong>Nivel B</strong>: analizar, documentar y presentar los resultados de las verificaciones técnicas <strong>con base en hechos verificables</strong>, sin dejarse arrastrar por relaciones personales, presiones jerárquicas o de terceros, prisa, rumores ni por la propia hipótesis. Para un cargo que produce soportes documentales, la objetividad no es una virtud decorativa: es lo que hace que el informe técnico pueda sostener una decisión.',
    badges=['⏱ 95-115 min', '🧭 Nivel B', '🧠 Comportamental'],
    fmeta='Objetividad (competencia por perfil, Nivel B)',
    cargo='Técnico en Criminalística 4TC-17 (Nivel Técnico)',
    conv='285-2026',
    alerta='Objetividad',
)

FUENTE = 'guias/4SU11-COM-03-objetividad.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- bloques nuevos
NARR = (
    '<p>Imagina que te delegan practicar una verificación técnica en un caso en el que, casualmente, conoces '
    'de vista a una de las personas involucradas. O imagina que el despacho que pidió el apoyo, apurado '
    'por un término, te sugiere «no profundizar tanto» en un hallazgo que complica la hipótesis que ya '
    'tenía. O que, después de tres trámites parecidas, entras a la cuarta convencido de que vas a '
    'encontrar lo mismo. Las tres situaciones ponen a prueba la competencia central de hoy: tu capacidad '
    'de practicar, documentar y presentar verificaciones técnicas con <mark>objetividad</mark>, basándote '
    'únicamente en lo que los hechos y los elementos realmente acreditan.</p>\n'
    '    <p>Hoy vas a dominar <strong>Objetividad</strong>, la tercera y última competencia por perfil de '
    'tu empleo, exigida en <mark>nivel B</mark>. Para un <strong>Técnico en Criminalística</strong> que '
    'recolecta soportes documentales, elabora informes técnicos y los presenta ante la autoridad que '
    'solicitó el apoyo, esta competencia es la más delicada de todas: de tu imparcialidad al observar, '
    'medir, describir y consignar depende directamente el valor de la prueba que el servidor competente '
    'usará para decidir.</p>'
)

OBJ1_LI = (
    '<li>La definición y el alcance de <strong>Objetividad</strong> (nivel B) en tu función de apoyo '
    'técnico y de recolección de soportes documentales.</li>'
)

MOD1_H4 = (
    '<h4>Cómo se traduce en tu función concreta de apoyo técnico</h4>\n'
    '      <p>Recuerda tus funciones centrales: establecer con la dependencia solicitante la '
    '<strong>metodología</strong> del apoyo, practicar las verificaciones técnicas por delegación, '
    '<strong>elaborar informes técnicos</strong>, <strong>presentar las pruebas practicadas y sus '
    'anexos</strong> ante la autoridad que las solicitó y proyectar autos y conceptos para la firma del '
    'servidor competente. Cada una de esas funciones descansa en un análisis previo: qué se observó, qué '
    'acredita cada elemento, qué permite y qué no permite afirmar la técnica aplicada. Objetividad es la '
    'garantía de que ese análisis refleja fielmente lo que el material realmente muestra, y no lo que '
    'sería más cómodo, más rápido o más conveniente que mostrara.</p>\n'
    '      <p>En un informe técnico la falta de objetividad casi nunca aparece como una mentira abierta. '
    'Aparece así:</p>\n'
    '      <ul class="lista">\n'
    '        <li>Un hallazgo desfavorable a la hipótesis del despacho que queda descrito en dos líneas, '
    'mientras el favorable ocupa dos páginas.</li>\n'
    '        <li>Una limitación de la técnica aplicada que no se menciona, de modo que el resultado '
    'parece más concluyente de lo que es.</li>\n'
    '        <li>Un adjetivo que califica donde debería haber una medida: «evidente deterioro» en lugar '
    'de la descripción y la medición del deterioro.</li>\n'
    '        <li>Un orden de presentación que pone primero lo que confirma y al final, en letra pequeña, '
    'lo que relativiza.</li>\n'
    '      </ul>'
)

MOD1_DELICADA = (
    '<h4>Por qué esta competencia es la más "delicada" de tu perfil</h4>\n'
    '      <p>Recuerda la regla de oro de tu rol: <strong>apoyas, no decides</strong>. Describes hechos, '
    'metodología y resultados; no calificas la falta ni atribuyes responsabilidad. Eso, lejos de reducir '
    'el peso de la objetividad, lo aumenta: un sesgo en tu informe no queda «contenido» en un error de '
    'trámite, porque el servidor competente decidirá <em>con base en tu informe</em>. Si el informe '
    'sobredimensiona un hallazgo, omite una limitación de la técnica o describe con adjetivos lo que '
    'debía medir, el sesgo viaja hasta la decisión final y, muchas veces, nadie puede detectarlo después: '
    'quien decide no estuvo en el trámite. Tú sí.</p>\n'
    '      <p>Por eso la prueba de la convocatoria insiste tanto en esta competencia para cargos '
    'técnicos de investigación: eres la única persona que vio el hecho en el momento en que podía ser '
    'observado. Lo que no quede documentado con exactitud, no vuelve.</p>'
)

MOD_CONFIRMACION = (
    '<h4>El sesgo de confirmación: cuando el resultado no favorece la hipótesis</h4>\n'
    '      <p>Hay un sesgo que no proviene de una presión externa ni de un vínculo personal, sino de la '
    'propia mente de quien investiga: el <strong>sesgo de confirmación</strong>. Consiste en buscar, '
    'notar y recordar con más facilidad lo que confirma la hipótesis con la que se entró, y en pasar por '
    'encima de lo que la contradice. No requiere mala fe; de hecho, suele operar precisamente en quien '
    'está convencido de hacer bien su trabajo.</p>\n'
    '      <p>En el trabajo técnico se reconoce por síntomas concretos. Si te ves en alguno, no es una '
    'falla de carácter: es la señal de que toca volver a los datos.</p>\n'
    '      <div class="tabla-wrap"><table>\n'
    '        <tr><th>Síntoma</th><th>Qué está pasando</th><th>Qué hacer</th></tr>\n'
    '        <tr><td>«Esto ya lo vi tres veces, va a salir lo mismo»</td><td>Está decidiendo el '
    'resultado antes de practicar la prueba.</td><td>Aplicar la metodología completa al caso concreto, '
    'sin acortar pasos por familiaridad.</td></tr>\n'
    '        <tr><td>Un dato que no encaja y se atribuye a «un error de medición»</td><td>Está '
    'descartando lo que contradice la hipótesis sin verificarlo.</td><td>Verificar y, si no se puede, '
    'consignar el dato y la imposibilidad de verificarlo.</td></tr>\n'
    '        <tr><td>El hallazgo favorable se describe en detalle; el desfavorable, en una línea</td>'
    '<td>El sesgo se trasladó a la redacción, no al dato.</td><td>Dar a cada hallazgo el espacio que '
    'corresponde a su peso técnico, no a su conveniencia.</td></tr>\n'
    '        <tr><td>«El despacho ya sabe lo que va a encontrar»</td><td>Está adoptando como propia la '
    'hipótesis de otro.</td><td>Recordar que la hipótesis del despacho no es un resultado: es lo que su '
    'prueba debe poner a prueba.</td></tr>\n'
    '      </table></div>\n'
    '      <div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div><p>Cuando una pregunta '
    'describe un hallazgo que <strong>contradice</strong> lo que el despacho esperaba, la opción correcta '
    'casi siempre consiste en <strong>consignarlo igual</strong>, con el mismo rigor que lo favorable, y '
    'ponerlo en conocimiento del competente. Las opciones que proponen «verificarlo otra vez antes de '
    'mencionarlo», «consultarlo informalmente primero» o «dejarlo para un informe posterior» suenan '
    'prudentes y son, todas, formas de filtrar la información.</p></div>'
)

MOD_COMPLETITUD = (
    '<h4>Presentar las pruebas practicadas: completitud y límites de la técnica</h4>\n'
    '      <p>Una de tus funciones es <strong>presentar las pruebas practicadas y sus anexos</strong> '
    'ante la autoridad que solicitó el apoyo. Esa presentación es un acto de objetividad, no un trámite '
    'de entrega. Un informe objetivo deja ver tres cosas que un informe sesgado esconde:</p>\n'
    '      <div class="flujo">\n'
    '        <div class="flujo-paso"><div class="fp-n">1</div><div><b>Qué se hizo y cómo</b><p>La '
    'metodología aplicada, en términos que permitan a otro técnico entender el procedimiento y, en su '
    'caso, repetirlo.</p></div></div>\n'
    '        <div class="flujo-paso"><div class="fp-n">2</div><div><b>Qué resultó, completo</b><p>Todos '
    'los hallazgos, favorables y desfavorables a cualquier hipótesis, con el mismo nivel de detalle y '
    'sin adjetivos que reemplacen la medición.</p></div></div>\n'
    '        <div class="flujo-paso"><div class="fp-n">3</div><div><b>Qué no permite concluir</b><p>Las '
    'limitaciones de la técnica, del estado del material o de las condiciones de el trámite. Un '
    'informe que no declara sus límites invita a leerlo como más concluyente de lo que es.</p></div></div>\n'
    '      </div>\n'
    '      <p>Declarar una limitación no debilita tu trabajo: lo hace utilizable. Un informe que dice '
    '«con la muestra disponible y la técnica aplicada no es posible determinar X» es mucho más valioso '
    'para quien decide que uno que calla el punto y deja que el lector suponga.</p>'
)

R = [
    # --- sección 0
    ('<p>Imagina que te asignan proyectar un concepto sobre un caso en el que, casualmente, conoces de vista a una de las partes involucradas. O imagina que tu jefe, apurado por un plazo, te sugiere "no profundizar tanto" en una prueba que complica la conclusión que él prefiere. Estas situaciones ponen a prueba la competencia central de hoy: tu capacidad de proyectar conceptos y providencias con <mark>objetividad</mark>, basándote únicamente en los hechos y las pruebas del expediente, sin dejarte llevar por relaciones personales, presiones externas o preferencias propias.</p>',
     NARR),
    ('<p>Hoy vas a dominar <strong>Objetividad</strong>, la tercera y última competencia específica de tu perfil, exigida en <mark>nivel B</mark>. Para un Sustanciador que apoya la proyección de conceptos, providencias y recursos bajo supervisión, esta competencia es, en muchos sentidos, la más delicada de todas: de tu imparcialidad al analizar hechos y pruebas depende directamente la calidad y la justicia del borrador que tu jefe finalmente revisará y firmará.</p>',
     ''),
    ('<li>La definición y el alcance de <strong>Objetividad</strong> (nivel B) en tu función de apoyo en sustanciación.</li>',
     OBJ1_LI),
    # --- sección 2: módulo 1
    ('<h4>Cómo se traduce en tu función concreta de apoyo en sustanciación</h4>\n      <p>Recuerda que tu función 1 —apoyar en la proyección de conceptos, providencias, solicitudes, constancias y recursos— implica redactar borradores sustantivos que tu jefe revisa y firma. Esa redacción exige, de tu parte, un análisis previo de los hechos y las pruebas del expediente: qué dice cada declaración, qué acredita cada documento, cómo se relacionan entre sí. Objetividad es la garantía de que ese análisis previo —el que sostiene tu proyecto— refleja fielmente lo que el expediente realmente dice, sin añadir ni omitir elementos según tu propia conveniencia o la de un tercero.</p>',
     MOD1_H4),
    ('<h4>Por qué esta competencia es la más "delicada" de proyectar bajo supervisión</h4>',
     MOD1_DELICADA + '\n      <h4>__VIEJO_DELICADA__</h4>'),
    # --- bloques nuevos
    ('<h4>El riesgo de las inferencias razonables pero no verificadas</h4>',
     MOD_CONFIRMACION + '\n      <h4>El riesgo de las inferencias razonables pero no verificadas</h4>'),
    ('<div class="modulo-n">7</div><h3>Objetividad y aplicación consistente de criterios</h3></div>\n    <div class="b-texto">',
     '<div class="modulo-n">7</div><h3>Objetividad y aplicación consistente de criterios</h3></div>\n    <div class="b-texto">\n      ' + MOD_COMPLETITUD),
]
SEC = aplicar_todas(SEC, R, estricto=True)
SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>',
     '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('(4SU-11)', '(4TC-17)'),
    ('4SU-11', '4TC-17'),
    ('apoyo en sustanciación', 'apoyo técnico'),
    ('en sustanciación', 'en el apoyo técnico'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol('Técnico en Criminalística', 'Técnicos en Criminalística'), estricto=False)   # filtro antifugas final
# el h4 original de "más delicada" quedó duplicado por el bloque nuevo: se elimina el sobrante
for n in SEC:
    SEC[n] = SEC[n].replace('\n      <h4>__VIEJO_DELICADA__</h4>', '')

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre Objetividad '
              '(Nivel B) en el trabajo real de un Técnico en Criminalística de la División de Gestión Humana: hechos frente a suposiciones, '
              'imparcialidad ante vínculos, presiones jerárquicas y de terceros, prisa, rumores y consistencia de '
              'criterio. Los contextos son extensos y las cuatro opciones son plausibles.')

P = [
 (2,
  'Le encargan verificar los soportes de experiencia de una persona nombrada antes de su posesión. El jefe que impulsa el nombramiento le había anticipado su lectura: que la experiencia «alcanza de sobra». Al revisar, usted encuentra dos cosas: una certificación que sí acredita dieciocho meses de experiencia relacionada, y otra —la que completaría el tiempo exigido— que corresponde a un contrato cuyo objeto no guarda relación con las funciones del empleo. El término para rendir la constancia vence mañana y el jefe le comenta, de paso, que «el asunto está bastante claro».',
  '¿Cómo debe redactar la constancia?',
  ['Consignar el soporte que sí acredita y mencionar el otro de manera general, para no desorientar al jefe con un dato que podría exigir una revisión adicional de la hoja de vida.',
   'Consignar solo el soporte que acredita y comentar verbalmente el otro al jefe, de modo que sea él quien decida si corresponde pedir una certificación complementaria.',
   'Consignar los dos soportes con el mismo nivel de detalle, describiendo qué acredita cada uno y qué requisito queda o no acreditado, sin calificar a nadie ni concluir más de lo que los documentos respaldan.',
   'Pedir una ampliación del término para confirmar el segundo soporte antes de rendir la constancia, porque incluir un dato desfavorable sin confirmarlo podría afectar la claridad del trámite.'],
  'La objetividad se mide justamente cuando lo que usted encuentra contradice la lectura de quien impulsa el trámite: el dato desfavorable se consigna con el mismo rigor que el favorable, describiendo qué acredita cada documento. Decidir si se pide una certificación adicional o si el requisito se tiene por cumplido no es del técnico.',
  'Mencionar «de manera general», comentarlo solo verbalmente o aplazar la constancia para «confirmar» son tres formas de filtrar un dato desfavorable. La constancia debe reflejar todo lo verificado, con su alcance y sus límites.'),

 (0,
  'Le asignan verificar los requisitos de una persona nombrada que resulta ser el esposo de una compañera de otra dependencia con la que usted comparte almuerzo casi a diario y a la que considera amiga. No existe parentesco entre usted y el nombrado, y nadie en la División conoce esa amistad. La posesión está programada para pasado mañana y el grupo está corto de personal. Usted se siente capaz de actuar con imparcialidad.',
  '¿Cuál es la actuación correcta?',
  ['Poner el vínculo en conocimiento por escrito de su jefe antes de iniciar, describiendo la relación y dejando que quien es competente decida si procede o no su participación en el trámite.',
   'Adelantar el trámite normalmente, ya que no hay parentesco con el nombrado y la amistad es con una tercera persona que no es la interesada en el trámite en curso.',
   'Adelantar el trámite y, al final, consignar en la constancia que existe una amistad con la esposa del nombrado, para que el competente valore la información al momento de decidir.',
   'Comentarlo verbalmente a su compañera de grupo para que revise con usted los soportes, de modo que haya un segundo par de ojos que pueda respaldar la imparcialidad de su actuación.'],
  'La imparcialidad que protege la competencia no es solo la real, sino también la aparente: lo que corresponde es manifestar el vínculo por escrito y antes de actuar, y dejar la decisión a quien es competente. Sentirse capaz de ser imparcial no reemplaza la manifestación.',
  'Un vínculo indirecto —con alguien cercano al interesado— sí amerita manifestación, y hacerlo después de actuar o solo de palabra no cumple su función: la finalidad es que otro decida antes de que usted intervenga.'),

 (3,
  'Su jefe inmediato revisa el borrador de su informe técnico y le pide dos cambios. El primero: cambiar el orden de los apartados y unificar la redacción al formato institucional. El segundo: suprimir el párrafo donde usted describe que la técnica aplicada no permite determinar la antigüedad del daño, «porque esa frase le quita fuerza al informe y el despacho va a devolverlo pidiendo aclaraciones». Ambos cambios se le piden en la misma conversación y con tono cordial.',
  '¿Cómo debe proceder?',
  ['Aceptar los dos cambios, porque provienen del superior que revisa y firma la remisión del informe, y la decisión sobre el contenido final corresponde a quien tiene esa competencia.',
   'Rechazar los dos cambios y remitir el informe en su versión original, dejando constancia escrita de que se le pidió modificarlo, para proteger la integridad de la prueba practicada.',
   'Aceptar los dos cambios y, por separado, informar el hecho a la Dirección, de modo que quede un registro de la presión recibida sin entrar en conflicto directo con su jefe inmediato.',
   'Aceptar el cambio de orden y formato, y exponer por escrito por qué la limitación de la técnica debe permanecer, dejando constancia de su análisis y del alcance real del resultado.'],
  'Hay que distinguir la instrucción legítima de forma —orden, formato, redacción— de la presión que afecta el fondo. La primera se acata; la segunda se objeta por escrito con el sustento técnico, dejando constancia del análisis propio.',
  'Aceptar todo suprime una limitación que condiciona la lectura del resultado; rechazar todo desconoce una instrucción legítima de forma; y acatar y «reportar por detrás» no protege el informe, que saldría igual sin la limitación.'),

 (1,
  'Faltan dos horas para el cierre de la jornada y usted debe rendir hoy el informe de un trámite practicada esta mañana. Ha hecho tres trámites similares este mes, con resultados parecidos. Para ganar tiempo, un compañero le sugiere partir del informe del caso anterior, cambiar los datos de identificación y los valores medidos, y conservar el resto del análisis, «porque el procedimiento fue idéntico y así no se reescribe lo mismo tres veces».',
  '¿Cuál es la conducta objetiva?',
  ['Reutilizar el informe anterior cambiando datos y valores, ya que la metodología aplicada fue efectivamente la misma y el análisis general es válido para los tres casos practicados.',
   'Elaborar el informe sobre el caso concreto, y si el tiempo no alcanza para hacerlo con rigor, informar por escrito la limitación de tiempo y pedir el ajuste del plazo por el canal.',
   'Rendir hoy una versión resumida del informe, con los datos esenciales, y complementarla mañana con el análisis completo, de modo que el término se cumpla sin sacrificar el rigor.',
   'Usar el informe anterior como plantilla y advertir al despacho que, por el tiempo disponible, el análisis puede requerir una revisión posterior si surgen observaciones al documento.'],
  'Reciclar el análisis de un caso parecido es una de las formas más frecuentes de sesgo: da por supuesto el resultado antes de examinar este caso. Si la prisa impide el rigor, lo que corresponde es informar la limitación por escrito, no recortar el análisis.',
  'Cambiar datos sobre un análisis anterior traslada conclusiones de otro caso a este; y una «versión resumida» o un informe con revisión pendiente entregan al despacho un documento que no refleja todavía lo que la prueba acredita.'),

 (2,
  'Mientras usted revisa los soportes de su reclamación, un servidor se le acerca aparte y le dice que quiere «explicarle su versión» para que la tenga en cuenta en la constancia. Añade que ya ha hablado con otros servidores de la entidad, que su caso es injusto y que lo único que pide es que usted «no se deje llevar por lo que dice la carpeta». Usted está solo en ese momento y la revisión aún no ha terminado. Su jefe inmediato está en una reunión y los demás integrantes del grupo salieron a otro trámite administrativa.',
  '¿Qué corresponde hacer?',
  ['Escuchar su versión sin comprometerse a nada y no consignarla, ya que oírla no afecta la objetividad y negarse podría leerse como un trato descortés hacia el servidor.',
   'Escuchar su versión y consignarla en la constancia como manifestación del interesado, para que el servidor competente conozca todo antes de adoptar cualquier decisión.',
   'No recibir la versión por esa vía, informarle que sus manifestaciones debe presentarlas por escrito dentro del trámite, y dejar constancia del acercamiento ocurrido.',
   'Suspender de inmediato la revisión y devolver la carpeta, para evitar cualquier contacto adicional que pudiera comprometer la imparcialidad de la verificación que está haciendo.'],
  'Un contacto directo del interesado, por fuera del trámite escrito, se encauza: se informa cuál es la vía y se deja constancia del acercamiento. Ni se recibe la versión por fuera del procedimiento ni se abandona la tarea asignada.',
  'Oír la versión «sin consignarla» deja un contacto sin registro, y consignarla como si hubiera sido presentada dentro del trámite le da un cauce que no tuvo. Devolver la carpeta, por su parte, incumple la tarea asignada sin necesidad.'),

 (1,
  'En el grupo circula un comentario: que la persona cuyos requisitos usted está verificando «ya tuvo un problema con un título en otra entidad». Nadie precisa la fuente. El dato explicaría bien una inconsistencia que usted encontró en una certificación y le resulta tentador mencionarlo en la constancia como antecedente que da contexto al hallazgo. La hoja de vida que usted tiene no contiene ninguna referencia a ese supuesto antecedente. La constancia debe rendirse en dos días y esa inconsistencia es, hasta ahora, el dato más llamativo que usted documentó.',
  '¿Cómo debe actuar?',
  ['Incluir el antecedente señalando que se trata de información no confirmada, de modo que el competente pueda verificarlo y valorar si guarda relación con la inconsistencia hallada.',
   'No incluirlo ni usarlo como base del análisis, y limitarse a lo que los documentos examinados y la verificación efectivamente acreditan en este trámite concreto.',
   'Verificar el rumor consultando informalmente a servidores de la otra entidad y, si se confirma, incorporarlo a la constancia como contexto de la inconsistencia que usted documentó.',
   'Comentarlo verbalmente a su jefe sin dejarlo por escrito, para que decida si pide una verificación adicional sin que el rumor quede registrado en la carpeta.'],
  'Un rumor no es un hecho verificable y no entra a la verificación, ni como dato ni como «contexto» ni con la etiqueta de no confirmado; además, un dato así sobre una persona que no lo ha podido controvertir afecta sus derechos. La constancia se limita a lo que los documentos acreditan.',
  'Etiquetarlo como «no confirmado» no lo vuelve admisible: ya quedó sembrado en el documento. Y verificarlo por su cuenta o pasarlo verbalmente son maneras de darle curso a información cuya fuente usted no conoce.'),

 (3,
  'Usted debe documentar un hallazgo que, en su lectura, «es evidente». Al redactar la constancia, escribe: «se observó una hoja de vida notoriamente incompleta y claramente atribuible al descuido del servidor». Al releer, nota que no consignó cuáles documentos faltan, ni frente a qué requisito del manual los echó de menos, ni en qué estado recibió la carpeta. La constancia debe salir hoy y el párrafo, tal como está, se entiende perfectamente. Nadie ha revisado todavía el borrador y usted es la única persona que revisó la carpeta.',
  '¿Qué debe corregir?',
  ['Nada sustancial: basta añadir cómo hizo la revisión, porque la descripción de lo incompleto es comprensible y refleja fielmente lo que usted observó al examinar la carpeta.',
   'Suavizar la redacción cambiando «claramente atribuible» por «posiblemente atribuible», de modo que la afirmación quede prudente sin obligarlo a reescribir todo el apartado.',
   'Mantener la redacción y añadir al final una nota aclarando que atribuir el descuido corresponde al servidor competente y no al técnico que hizo la verificación.',
   'Reescribir el párrafo enumerando qué documentos faltan, frente a qué requisito del manual, y en qué estado recibió la carpeta, y suprimir la atribución de culpa, que no corresponde a la constancia.'],
  'Dos defectos de objetividad en un párrafo: adjetivos («notoriamente incompleta») que reemplazan el dato concreto, y una atribución de culpa que excede el rol del técnico. Se corrige enumerando qué falta y frente a qué requisito, consignando el estado en que recibió la carpeta y suprimiendo la atribución.',
  'Decir cómo revisó no arregla los adjetivos; suavizar a «posiblemente atribuible» sigue atribuyendo; y una nota al final no neutraliza una atribución ya escrita en el cuerpo del documento.'),

 (0,
  'Dos trámites de la misma naturaleza llegan a su grupo en la misma semana: dos reconocimientos de prima. Uno es de un servidor del nivel asistencial; el otro, de un directivo cuyo nombre ha aparecido en prensa. Para el segundo, el jefe pide «especial cuidado». Usted advierte que, sin proponérselo, está aplicando al trámite del directivo un nivel de verificación mayor: contrasta cada soporte con la norma, documenta más detalladamente y revisa dos veces el proyecto, mientras que al otro le aplicó el procedimiento estándar.',
  '¿Qué revela esa diferencia y qué corresponde hacer?',
  ['Revela una inconsistencia de criterio: el estándar de rigor debe ser el mismo en ambos, por lo que corresponde elevar el del primer trámite al nivel que usted aplicó en el del directivo.',
   'No revela un problema: la mayor exposición pública del segundo trámite justifica objetivamente un control más estricto, porque un error allí tendría consecuencias institucionales mayores.',
   'Revela un exceso en el trámite del directivo: lo correcto es volver al procedimiento estándar en ambos, porque añadir controles no previstos retrasa los reconocimientos sin respaldo normativo.',
   'Revela una instrucción del jefe que usted debe acatar, aplicando mayor rigor donde se le pidió y el estándar habitual en los demás trámites asignados a su grupo de trabajo.'],
  'La consistencia es una forma de objetividad: el rigor no puede depender del nivel jerárquico del interesado, y menos cuando lo que está en juego es un derecho prestacional igual para los dos. Detectada la diferencia, lo que corresponde es nivelar hacia arriba, no justificar el doble estándar ni rebajar el trámite visible.',
  'Justificar el doble estándar por la exposición pública es exactamente el sesgo que la competencia busca evitar, y «volver al estándar» en ambos desaprovecha que el mayor rigor sí era posible. La instrucción de cuidado no autoriza tratar peor los demás trámites.'),

 (2,
  'Al final de una jornada larga, con dos trámites ya cerrados, le piden uno tercero que no estaba programado: liquidar el tiempo de servicio de un retiro, tarea sencilla pero que exige precisión en el conteo de días y en la aplicación de los factores salariales. Usted está cansado, sabe que el procedimiento lo domina y calcula que puede terminarlo en media hora. Nadie más del grupo está disponible y la historia laboral debe devolverse hoy al archivo. El archivo de gestión cierra en cuarenta minutos y el jefe del grupo ya salió de la División.',
  '¿Cuál es la actuación objetiva?',
  ['Hacer la liquidación confiando en que domina el procedimiento, ya que la experiencia compensa el cansancio y la devolución de la carpeta no admite aplazamiento alguno.',
   'Negarse a hacerla y dejar constancia del cansancio, de modo que la responsabilidad por el aplazamiento recaiga en quien asignó un trámite al final de la jornada.',
   'Informar por el canal la situación y el riesgo que el cansancio supone para la exactitud del conteo, y actuar conforme a lo que se disponga, dejando constancia de la condición en que se hizo.',
   'Hacer la liquidación y anotar al final que se realizó en condiciones de fatiga, para que el competente valore ese factor si las cifras llegaran a ser cuestionadas después.'],
  'La fatiga es un riesgo real para la exactitud —y un error de días o de factores salariales se traduce en dinero mal liquidado—, y la objetividad incluye reconocer los límites propios. Lo esperado no es ni asumir el riesgo en silencio ni negarse de plano: es informar la situación por el canal, actuar conforme a lo dispuesto y dejar constancia.',
  'Confiar en la experiencia no elimina el riesgo de error en un conteo; negarse sin más traslada el problema; y advertirlo solo al final pone en duda la liquidación cuando ya está hecha y el pago puede estar en curso.'),

 (1,
  'Debe reportar al jefe el avance de los apoyos asignados. En uno de ellos usted cometió un error: envió un elemento a la dependencia equivocada y la devolución tomó dos días, lo que retrasó el trámite. El retraso no afectó ningún término. En el mismo reporte debe informar el desempeño de un compañero en un trámite conjunta en la que, a su juicio, el compañero fue descuidado con el registro de los elementos. El reporte es escrito, lo lee el jefe de grupo y queda en el expediente interno de seguimiento de los apoyos del mes.',
  '¿Cómo debe elaborar el reporte?',
  ['Informar el retraso sin precisar su causa, ya que ningún término se vio afectado, y describir con detalle el descuido del compañero, que sí puede comprometer la trazabilidad de los elementos.',
   'Informar su propio error con sus causas y consecuencias reales, y describir la conducta del compañero en hechos concretos y verificables, sin calificaciones sobre su desempeño general.',
   'Informar solo lo relativo al avance de los apoyos, sin mencionar ni su error ni la conducta del compañero, y plantear ambos temas verbalmente en la próxima reunión del grupo.',
   'Informar su propio error con detalle y omitir lo del compañero, para no exponerlo en un reporte escrito y darle primero la oportunidad de corregir su manejo de los registros.'],
  'La objetividad en los reportes internos corta en dos direcciones: no minimizar el error propio ni exagerar o calificar el ajeno. Lo propio se informa con causas y consecuencias reales; lo del compañero, en hechos concretos y verificables, sin juicios sobre su desempeño.',
  'Omitir la causa del error propio es minimizarlo; describir al compañero con calificaciones excede lo observado; y callar ambos puntos deja sin registro un hecho que afecta la trazabilidad de los elementos.'),

 (3,
  'Recibe una instrucción escrita ambigua: «revisar los soportes recibidos y determinar si proceden». Los soportes corresponden a tres solicitudes de naturaleza distinta —una comisión, una licencia no remunerada y un encargo— y la instrucción no precisa si debe revisarlas todas, ni qué se entiende por «proceden» en cada caso. Revisar las tres toma el triple de tiempo. La instrucción proviene de otra dependencia y el término es corto. Usted ya invirtió media jornada en organizar los soportes y esa dependencia no responde llamadas desde ayer.',
  '¿Qué corresponde hacer?',
  ['Revisar únicamente la solicitud que a su juicio resulte más urgente de las tres y consignar en la constancia, con su justificación, la razón por la cual limitó el alcance de la revisión que hizo.',
   'Revisar las tres solicitudes aplicando el criterio más amplio posible, para cubrir cualquier interpretación de la instrucción y evitar una devolución de la constancia por insuficiencia.',
   'Rendir la constancia advirtiendo que la instrucción era ambigua y que, por ello, no fue posible revisar nada, y solicitar que se precise el alcance para una nueva asignación.',
   'Pedir por escrito la precisión del alcance a quien dio la instrucción, informar el impacto en el término y, mientras se aclara, adelantar lo común a cualquier lectura.'],
  'Ante una instrucción que admite dos lecturas, el criterio propio no sustituye la aclaración: se pide la precisión por escrito, se informa el impacto en el término y se avanza en lo que no depende de la interpretación. Así no se decide por el otro ni se paraliza el trabajo.',
  'Elegir «la más urgente» es decidir el alcance por cuenta propia; cubrir «cualquier interpretación» puede consumir el término en trabajo no pedido; y devolver el asunto sin revisar nada paraliza el trámite cuando sí había avance posible.'),

 (0,
  'Lleva tres semanas apoyando un caso complejo. Hoy advierte que su informe, ya avanzado, se apoya en una afirmación que usted tomó como cierta al comienzo: que el equipo examinado era el mismo que aparece en el inventario de la dependencia. Al revisar, ve que nadie verificó la coincidencia de los seriales y que el registro de recepción no los consigna. El informe debe entregarse en dos días y rehacer la verificación implicaría solicitar otra vez el elemento.',
  '¿Cuál es la actuación objetiva?',
  ['Dejar constancia de que la identidad del elemento no está verificada, informarla por el canal al competente y precisar en el informe qué conclusiones quedan condicionadas por ese vacío.',
   'Mantener la afirmación inicial, ya que la cadena de entrega fue continua y no existe ningún indicio de que el elemento examinado sea distinto al que figura en el inventario.',
   'Suprimir del informe toda referencia al inventario y presentar el análisis sobre «el elemento examinado», sin vincularlo a ningún registro, para que el vacío no afecte el resultado.',
   'Entregar el informe en el plazo y, en paralelo, solicitar el elemento para verificar los seriales, de modo que la verificación se incorpore después como anexo complementario.'],
  'Una inferencia razonable pero no verificada, descubierta tarde, se declara: se deja constancia del vacío, se informa al competente y se precisa qué conclusiones quedan condicionadas. Reconocerlo a tiempo es parte de la competencia, no una falla.',
  'Mantener la afirmación por ausencia de indicios en contra es exactamente una inferencia no verificada; borrar la referencia al inventario esconde el problema; y entregar primero y verificar después deja circular un informe con una base que usted ya sabe incierta.'),

 (2,
  'Dos personas solicitan en el mismo día información sobre el estado del apoyo técnico en sus respectivos casos. La primera es cordial, explica bien su situación y usted siente simpatía por ella. La segunda llega alterada, eleva la voz y cuestiona el trabajo de la Dirección. Ambas tienen la misma calidad procesal y piden exactamente lo mismo. Usted dispone de poco tiempo y nadie más está atendiendo en ese momento. Las dos esperan en el mismo punto de atención y pueden oír lo que usted responde a la otra persona.',
  '¿Cuál es la actuación correcta?',
  ['Atender primero y con más detalle a la primera, porque su actitud permite una comunicación más eficaz, y remitir a la segunda al canal escrito para que su solicitud quede formalizada.',
   'Atender primero a la segunda para contener su alteración y evitar que el malestar escale, y luego a la primera, que por su actitud comprensiva puede esperar sin mayor dificultad.',
   'Dar a las dos el mismo trato y la misma información, conforme a su calidad procesal y al canal previsto, sin que la actitud de cada una altere el contenido ni el alcance de la respuesta.',
   'Atenderlas juntas explicando una sola vez el procedimiento aplicable, de modo que ninguna pueda considerar que recibió un trato distinto al de la otra persona que solicitó lo mismo.'],
  'El trato objetivo e igualitario no depende de la actitud del usuario: a igual calidad procesal e igual solicitud, igual información y igual canal. La simpatía y la incomodidad son, las dos, formas de sesgo.',
  'Privilegiar a quien resulta agradable y relegar a quien incomoda —o lo contrario— altera el contenido o el orden por razones ajenas al caso. Y atenderlas juntas desconoce que cada una tiene derecho a información de su propio proceso.'),

 (1,
  'Usted registra la inconformidad que un servidor expresa sobre la liquidación de sus vacaciones: afirma que no se le contaron dos años de servicio y que nadie le explicó el cálculo. Usted revisó la carpeta y sabe que esos dos años corresponden a una licencia no remunerada que la norma no computa, y que el cálculo le fue entregado por escrito. Debe dejar el registro de la inconformidad para su trámite. El servidor insiste en que quede constancia exacta de lo que dijo y pide copia del registro que usted elabore.',
  '¿Cómo debe hacer el registro?',
  ['Registrar la inconformidad corrigiendo los puntos inexactos, de modo que quien la tramite reciba una versión ajustada a lo que efectivamente muestra la historia laboral.',
   'Registrar textualmente lo que el servidor manifiesta, sin corregirlo ni calificarlo, y dejar por separado la constancia de lo que muestran los soportes y el cálculo entregado.',
   'Registrar solo la parte de la inconformidad que resulta verificable y omitir las afirmaciones que usted sabe equivocadas, para no trasladar información errónea a quien deba resolverla.',
   'Explicar primero al servidor por qué sus afirmaciones son equivocadas y registrar la inconformidad únicamente si, después de esa explicación, decide mantenerla en los mismos términos.'],
  'El registro objetivo de una inconformidad consigna lo que el servidor manifiesta, tal como lo manifiesta, y deja aparte la constancia de lo que muestran los soportes. Corregir o filtrar su versión convierte el registro en una valoración que no le corresponde —y el derecho a que su petición se tramite como la formuló no depende de que usted la considere acertada—.',
  'Corregir u omitir partes de lo manifestado altera la petición del servidor; y condicionar el registro a que acepte una explicación suya convierte su propia lectura en filtro de acceso al trámite. Orientarlo sobre el cálculo es correcto; condicionar el registro, no.'),

 (3,
  'Compara dos informes suyos sobre casos equivalentes: uno de hace seis meses y otro reciente. En el primero consignó una limitación de la técnica aplicada; en el segundo, con el mismo procedimiento y un material en condiciones parecidas, no la consignó. No recuerda por qué. El informe reciente ya fue remitido, está en el expediente y nadie ha observado nada. Usted conserva los dos informes en su carpeta de trabajo y puede comparar, línea por línea, el apartado de metodología de cada uno.',
  '¿Qué corresponde hacer?',
  ['Nada: el informe reciente ya fue remitido, no ha sido observado y una corrección posterior sobre un documento aceptado podría restar credibilidad a su trabajo técnico ante el despacho.',
   'Aplicar de aquí en adelante el criterio del informe más reciente, que es el más ágil, y mantener la uniformidad hacia el futuro sin revisar lo que ya fue remitido al expediente.',
   'Anotar la diferencia en su propia bitácora de trabajo, para no repetirla, y revisar únicamente si en el futuro algún despacho formula una observación sobre el informe reciente.',
   'Informar por escrito la omisión al competente, para que valore su incidencia en el caso, y unificar su criterio hacia adelante aplicando la declaración de límites en todos los casos.'],
  'La consistencia en el tiempo también es objetividad, y una omisión que condiciona la lectura de un resultado no se deja pasar porque nadie la haya notado: se informa al competente para que valore su incidencia y se unifica el criterio hacia adelante.',
  'El silencio deja en el expediente un informe que parece más concluyente de lo que es. Y «unificar hacia el futuro» con el criterio menos riguroso, o anotarlo solo en su bitácora, consolida precisamente la omisión.'),
]
