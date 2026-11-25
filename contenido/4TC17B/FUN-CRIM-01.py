# -*- coding: utf-8 -*-
"""Día 19 · Conocimientos técnicos del área disciplinar aplicados al cargo."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol
from _brenda import IDENTIDAD, CARGO, PLURAL, meta

META = meta(
    codigo='FUN-CRIM-4TC17B-01',
    archivo='FUN-CRIM-4TC17B-01-area-disciplinar-aplicada-cargo.html',
    dia=19,
    titulo_doc='Conocimientos técnicos del área disciplinar aplicados al cargo',
    h1='Conocimientos técnicos<br>del área disciplinar aplicados al cargo',
    kicker='Día 19 · Conocimiento específico',
    sub='El sexto y último conocimiento específico del formato: los <strong>conocimientos técnicos del área disciplinar</strong>. Para un cargo de la División de Gestión Humana eso significa dos cosas muy concretas. Primero, el <strong>marco disciplinario</strong> que te alcanza como servidor y que explica por qué la historia laboral que custodias es la fuente de los antecedentes: qué es una falta, cómo se clasifican, el elemento subjetivo, las sanciones, las <strong>inhabilidades</strong> que de ellas derivan, la <strong>reserva</strong> de la actuación y la <strong>prescripción</strong>. Y segundo, la <strong>mirada técnica</strong> que tu manual te encarga en la función 2: examinar la <strong>pertinencia e idoneidad de los métodos, procedimientos y técnicas</strong> —aplicada a los documentos que pasan por tus manos—.',
    badges=['⏱ 100-120 min', '⚖️ Área disciplinar', '📖 Específico'],
    fmeta='Conocimientos técnicos del área disciplinar aplicados al cargo (Ley 1952 de 2019, Ley 2094 de 2021 y Decreto Ley 262 de 2000)',
    alerta='Conocimientos técnicos del área disciplinar aplicados al cargo',
)

S = secciones_mapeadas('guias/FUN-DIS-4SU11-01-derecho-disciplinario-fundamentos.html')

CIERRE = '''
      <div class="modulo-head"><div class="modulo-n">★</div><h3>La mirada técnica de la función 2: verificar documentos con método</h3></div>
      <div class="b-texto">
        <p>Llegamos al punto donde el nombre del empleo cobra sentido. La función 2 de tu manual te encarga <mark>«examinar los informes que se le asignen, respecto de la pertinencia e idoneidad de los métodos, procedimientos y técnicas utilizadas de acuerdo con su especialidad»</mark>. Esa es, en esencia, una <strong>mirada criminalística</strong>: no preguntarse si la conclusión gusta, sino si el camino para llegar a ella fue el correcto. Y en la División de Gestión Humana se aplica, todos los días, sobre <strong>documentos</strong>.</p>
        <div class="def-panel"><span class="def-label">Concepto</span><p>Verificar un documento no es leerlo: es establecer si <strong>es lo que dice ser</strong> (autenticidad), si <strong>proviene de quien dice provenir</strong> (procedencia), si <strong>acredita lo que se pretende acreditar</strong> (pertinencia) y si <strong>llegó y se conservó sin alteración</strong> (integridad y trazabilidad). Un documento puede ser auténtico y, aun así, no acreditar el requisito; y puede decir exactamente lo que hace falta y estar alterado.</p></div>
        <h4>Las cuatro preguntas que debes hacerle a todo soporte</h4>
        <div class="tabla-wrap"><table>
          <thead><tr><th>Pregunta</th><th>Qué se mira</th><th>Señal de alerta</th></tr></thead>
          <tbody>
            <tr><td><strong>¿Es auténtico?</strong></td><td>Membrete, firma, sello, numeración, coherencia del formato con la época y con la entidad que lo expide.</td><td>Tipografías mezcladas, alineaciones irregulares, un sello impreso sobre el texto y no bajo él, correcciones no salvadas.</td></tr>
            <tr><td><strong>¿De quién proviene?</strong></td><td>Que lo expida quien tiene la facultad de certificar ese hecho: la entidad empleadora, la institución educativa, la autoridad competente.</td><td>Una certificación de experiencia firmada por un particular sin calidad, o un título certificado por quien no lo expidió.</td></tr>
            <tr><td><strong>¿Acredita lo que se pide?</strong></td><td>Que su contenido coincida con el requisito del manual: tiempo, funciones desempeñadas, nivel del programa, fechas.</td><td>Un certificado que acredita vinculación pero no precisa funciones, de modo que no permite establecer si la experiencia es relacionada.</td></tr>
            <tr><td><strong>¿Está íntegro y trazable?</strong></td><td>Foliación continua, índice que corresponde, constancias de recibido, ausencia de folios faltantes o sueltos.</td><td>Saltos en la foliación, documentos sin fecha de radicación, folios agregados después del cierre del expediente.</td></tr>
          </tbody>
        </table></div>
        <div class="ojo"><b>Ojo en la prueba:</b> el límite de siempre, ahora en su versión más delicada. Usted <mark>describe lo que observa</mark>: «la certificación presenta una alineación irregular en la fecha y un sello superpuesto al texto». Lo que <mark>no</mark> hace es afirmar que el documento es falso, ni concluir que alguien cometió un delito. Establecer la falsedad de un documento requiere un peritaje y una decisión que no está en sus manos. Describir sin calificar protege la actuación y protege a la persona, que todavía no ha podido controvertir nada.</div>
        <h4>Por qué la historia laboral es, también, una pieza del área disciplinar</h4>
        <p>El vínculo entre tu dependencia y lo disciplinario no es teórico. La <strong>historia laboral</strong> que usted conforma y custodia es la fuente de la que salen los <strong>antecedentes</strong> del servidor: las sanciones anotadas, las inhabilidades derivadas de ellas y las constancias que después se certifican. De ahí tres consecuencias prácticas:</p>
        <div class="flujo">
          <div class="flujo-item"><strong>1. Integridad</strong><br>Un folio perdido puede borrar un antecedente o, al contrario, dejar sin soporte una anotación</div>
          <div class="flujo-item"><strong>2. Reserva</strong><br>La anotación de una sanción es un dato personal de impacto severo: su divulgación indebida daña a la persona</div>
          <div class="flujo-item"><strong>3. Oportunidad</strong><br>Las inhabilidades derivadas de una sanción tienen término: certificar mal puede impedir o permitir indebidamente una vinculación</div>
        </div>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Verificando los requisitos de una persona nombrada, usted encuentra una certificación de estudios en la que la fecha de expedición está en una tipografía distinta del resto del documento y el número de registro no sigue el formato de la institución. Lo correcto no es afirmar que el documento es falso ni archivarlo como si nada: es <strong>describir con precisión lo observado</strong> en su constancia escrita —qué elementos presentan la irregularidad y en qué consisten—, <strong>consignar que el requisito no queda acreditado</strong> con ese soporte, y <strong>poner el hecho en conocimiento del competente</strong>, que decidirá si se requiere a la institución educativa, si se compulsan copias o ambas cosas. Usted describió; la calificación y la compulsa son de otro.</p>
          </div>
        </div>
        <div class="checkpoint" data-correcta="2">
          <div class="cp-tag">✅ Checkpoint 1</div>
          <p class="cp-q">Usted examina un certificado de experiencia y observa que el sello aparece impreso <em>sobre</em> el texto y no debajo, y que la fecha está en una tipografía distinta. ¿Qué debe consignar en su constancia?</p>
          <div class="cp-op">Que el documento es falso y que debe compulsarse copia a la Fiscalía de inmediato.</div>
          <div class="cp-op">Que el documento presenta irregularidades, sin precisar cuáles, para no comprometer a nadie.</div>
          <div class="cp-op">Que el sello está superpuesto al texto y la fecha en tipografía distinta, y que el requisito no queda acreditado con ese soporte.</div>
          <div class="cp-op">Nada: establecer la autenticidad de un documento no es función del nivel técnico.</div>
          <div class="cp-fb">Correcto: la <strong>tercera</strong>. Se describe <mark>exactamente lo observado</mark> y se concluye sobre lo único que a usted le corresponde concluir: si el requisito queda o no acreditado con ese soporte. Declarar la falsedad exige peritaje y decisión de otro; «irregularidades» sin precisar no sirve a nadie; y callar compromete la veracidad de la constancia.</div>
        </div>
        <div class="checkpoint" data-correcta="1">
          <div class="cp-tag">✅ Checkpoint 2</div>
          <p class="cp-q">Un certificado es auténtico, lo expidió la entidad facultada y está íntegro, pero no precisa las funciones que la persona desempeñó. ¿Qué falla?</p>
          <div class="cp-op">La autenticidad, porque un documento sin detalle de funciones no puede considerarse genuino.</div>
          <div class="cp-op">La pertinencia: el documento es válido, pero no acredita que la experiencia sea relacionada con el empleo.</div>
          <div class="cp-op">La procedencia, porque quien lo expidió no tenía facultad para certificar ese hecho concreto.</div>
          <div class="cp-op">La integridad, porque un certificado incompleto equivale a un documento alterado en su contenido.</div>
          <div class="cp-fb">Correcto: la <strong>segunda</strong>. Es la distinción que más se confunde. Un documento puede ser <mark>auténtico y aun así no acreditar</mark> lo que se necesita. Aquí no hay problema de autenticidad, procedencia ni integridad: hay un problema de <strong>pertinencia</strong>, y la consecuencia práctica es que el requisito no queda acreditado.</div>
        </div>
        <div class="checkpoint" data-correcta="3">
          <div class="cp-tag">✅ Checkpoint 3</div>
          <p class="cp-q">¿Para qué sirve, en términos disciplinarios, la historia laboral que usted custodia?</p>
          <div class="cp-op">Para nada en materia disciplinaria: es un expediente exclusivamente administrativo de la dependencia.</div>
          <div class="cp-op">Para que el jefe inmediato consulte libremente el comportamiento histórico de cada servidor.</div>
          <div class="cp-op">Para reemplazar el expediente disciplinario cuando este no esté disponible en la actuación.</div>
          <div class="cp-op">Es la fuente de los antecedentes del servidor: allí reposan las sanciones anotadas y de ahí salen las certificaciones.</div>
          <div class="cp-fb">Correcto: la <strong>cuarta</strong>. La historia laboral es la <mark>fuente de los antecedentes</mark>, y de ahí se derivan tres cuidados: <strong>integridad</strong> (un folio perdido borra o deja sin soporte una anotación), <strong>reserva</strong> (es un dato personal de impacto severo) y <strong>oportunidad</strong> (las inhabilidades tienen término). No reemplaza el expediente disciplinario ni está abierta a consulta libre.</div>
        </div>
        <div class="checkpoint" data-correcta="0">
          <div class="cp-tag">✅ Checkpoint 4</div>
          <p class="cp-q">La función 2 de su manual le encarga examinar la «pertinencia e idoneidad de los métodos, procedimientos y técnicas». ¿Qué significa eso en la práctica?</p>
          <div class="cp-op">Verificar si el camino seguido fue el correcto, con independencia de si la conclusión parece razonable.</div>
          <div class="cp-op">Verificar si la conclusión del informe es acertada y corregirla cuando no lo sea.</div>
          <div class="cp-op">Decidir si el informe se acepta o se rechaza y ordenar que se repita cuando haga falta.</div>
          <div class="cp-op">Calificar jurídicamente los hechos que el informe describe, para orientar al competente.</div>
          <div class="cp-fb">Correcto: la <strong>primera</strong>. Examinar el método es preguntarse <mark>si el camino fue el correcto</mark>, no si el resultado gusta. Que la conclusión parezca razonable no sanea un procedimiento que no fue el establecido. Y las otras tres opciones cruzan la línea: corregir conclusiones, decidir sobre el informe o calificar jurídicamente no son suyas.</div>
        </div>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Le asignan examinar un informe sobre la revisión de cincuenta historias laborales. La conclusión es que «el 94 % cumple los requisitos de archivo». Al mirar el método, usted encuentra que la muestra fueron doce carpetas, que quien las escogió fue el propio autor del informe y que no se explica con qué criterio. Su examen no discute el 94 %: dice que <strong>no es posible verificar la idoneidad del método</strong> porque la selección de la muestra no está explicada y las exclusiones no están justificadas, y que ese vacío debe subsanarse. Esa observación vale más que cualquier opinión suya sobre el porcentaje.</p>
          </div>
        </div>
        <div class="practica">
          <div class="practica-head">🗂️ En la práctica</div>
          <div class="practica-body">
            <p>Un exservidor pide una certificación de antecedentes para un proceso de selección. En su historia laboral aparece una sanción anotada hace cuatro años. Usted <strong>no decide</strong> si eso lo inhabilita —esa valoración es de quien adelanta el proceso de selección y de la norma que lo rige—, pero sí es responsable de que la certificación diga <strong>exactamente lo que los registros muestran</strong>: qué sanción, de qué fecha, en qué acto consta y si está en firme. Ni una palabra de más, ni una de menos. Una certificación que omite la anotación es falsa; una que la describe mal puede cerrarle una puerta que la ley ya le había abierto.</p>
          </div>
        </div>
        <div class="ojo"><b>Ojo en la prueba:</b> no confundas el <mark>registro de una sanción</mark> con la <mark>inhabilidad</mark> que de ella deriva. Son dos cosas con reglas y términos propios: el registro deja constancia histórica del hecho; la inhabilidad es el efecto que impide ocupar ciertos empleos o participar en ciertos procesos, y tiene su propia duración. Una pregunta clásica mezcla las dos para hacerte decir que «la anotación inhabilita de por vida». Y recuerda el art. 193 del Decreto Ley 262 de 2000: para concursar por <strong>ascenso</strong> se exige no haber sido sancionado disciplinariamente <strong>el año anterior</strong>.</div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> los conocimientos técnicos del área disciplinar, en este cargo, tienen dos caras. Una es el <strong>marco disciplinario</strong> que te alcanza como servidor y que explica el valor de la historia laboral como fuente de antecedentes. La otra es la <strong>mirada técnica</strong> de la función 2: examinar la pertinencia e idoneidad del método, aplicada a los documentos, con cuatro preguntas —autenticidad, procedencia, pertinencia, integridad—. Y con el límite de siempre: <strong>describir lo observado, no calificarlo</strong>, y poner el hecho en conocimiento del competente.</p></div>
        <div class="box ok"><div class="box-title">💡 Idea clave del día</div><p><strong>Idea clave:</strong> criminalística, en tu puesto, no significa laboratorio: significa <strong>método</strong>. La pregunta que define el oficio es siempre la misma —«¿cómo sé que esto es lo que dice ser?»— y la respuesta correcta nunca es «porque parece». Es porque lo verifiqué contra una fuente, lo describí con precisión y dejé constancia de lo que encontré.</p></div>
        <div class="box ojo"><div class="box-title">🗣️ Frase para recordar</div><p>«Describe lo que ves, no lo que concluyes. La falsedad la declara otro; el registro preciso de lo observado lo haces tú. — Día 19»</p></div>
        <div class="fuentes">
          <h4>📚 Fuentes para verificar</h4>
          <ul>
            <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=90324" target="_blank" rel="noopener">Ley 1952 de 2019</a> — Código General Disciplinario.</li>
            <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=166369" target="_blank" rel="noopener">Ley 2094 de 2021</a> — reforma al Código General Disciplinario.</li>
            <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=40618" target="_blank" rel="noopener">Decreto Ley 262 de 2000</a> — funciones de la División de Gestión Humana (art. 63).</li>
            <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981" target="_blank" rel="noopener">Ley 1581 de 2012</a> — protección de datos personales.</li>
          </ul>
        </div>
      </div>
'''
S[2] = S[2] + CIERRE
SEC = aplicar_todas(S, IDENTIDAD + [
    ('4SU-11', '4TC-17'), ('4SU11', '4TC17'),
    ('Convocatoria 288-2026', 'Convocatoria 285-2026'), ('288-2026', '285-2026'),
    ('Resolución 243 de 2026', 'Resolución 212 de 2026'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(CARGO, PLURAL), estricto=False)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el marco '
              'disciplinario que te alcanza como servidor, los antecedentes y la reserva, y la verificación técnica '
              'de documentos. Recuerda el límite: describir lo observado no es calificarlo.')

P = [
 (1,
  'Verificando los requisitos de una persona nombrada, usted advierte que en la certificación de estudios la fecha de expedición aparece en una tipografía distinta del resto del documento y que el número de registro no sigue el formato que usa esa institución en los demás certificados que reposan en la División. Un compañero le dice que escriba en la constancia que «el documento es falso» y otro, que no mencione nada porque «no es perito y podría equivocarse». La posesión está programada para pasado mañana.',
  '¿Cuál es la actuación correcta?',
  ['Consignar en la constancia que el documento es falso y poner los hechos en conocimiento del competente, para que compulse copias a la Fiscalía antes de que la posesión se surta.',
   'Describir con precisión los elementos observados, consignar que el requisito no queda acreditado con ese soporte y poner el hecho en conocimiento del competente, sin calificar el documento.',
   'No mencionar la irregularidad y limitarse a consignar que el documento fue aportado, porque establecer la autenticidad de un certificado excede la competencia técnica de la División.',
   'Llamar directamente a la institución educativa para confirmar si el certificado es auténtico y, según lo que respondan verbalmente, decidir si se consigna o no la observación en la constancia.'],
  'Correcto. Su función 2 es examinar la <strong>pertinencia e idoneidad</strong> de los métodos y las técnicas: eso le permite <strong>describir lo observado</strong> con precisión —la tipografía, el formato del registro— y concluir que el requisito <strong>no queda acreditado con ese soporte</strong>. Afirmar la falsedad exige un peritaje y una decisión que no son suyos.',
  'Declarar falso un documento es calificar, y expone a la persona antes de que pueda controvertir nada. Callar lo observado compromete la veracidad de la constancia y puede habilitar una posesión viciada. Y una confirmación telefónica informal no es una verificación: no deja soporte y no sustituye el requerimiento formal.'),

 (3,
  'Una entidad externa solicita por escrito que la Procuraduría certifique si un exservidor tiene sanciones disciplinarias anotadas, para un proceso de selección que esa entidad adelanta. Un compañero le dice que no se responda «porque eso es reservado» y otro, que se entregue copia completa del expediente disciplinario que reposa en la historia laboral. La solicitud viene firmada por el jefe de talento humano de la entidad solicitante, no adjunta autorización del exservidor y este no ha sido informado de la consulta.',
  '¿Cuál es la actuación correcta?',
  ['No responder, porque toda la información disciplinaria está amparada por reserva absoluta y ninguna entidad externa puede acceder a datos de un servidor que ya no está vinculado.',
   'Entregar copia completa del expediente disciplinario, porque la solicitud proviene de una entidad pública con una finalidad legítima y entre entidades del Estado no opera la reserva.',
   'Responder con los datos que el exservidor autorice, previa consulta telefónica con él, y entregar únicamente aquello sobre lo que manifieste su conformidad en esa conversación.',
   'Radicar la solicitud, verificar qué puede certificarse con los registros de la entidad y bajo qué condiciones, responder de fondo dentro del término con esa distinción y dejar constancia.'],
  'Correcto. Hay dos cosas distintas: lo que la entidad <strong>puede certificar</strong> sobre sus propios registros y lo que está <strong>amparado por reserva</strong>. La respuesta correcta hace esa distinción, de manera motivada, y se da dentro del término. Ni silencio ni entrega indiscriminada.',
  'La reserva no es absoluta ni desaparece entre entidades públicas: la anotación de una sanción es un dato personal de impacto severo. Y una autorización telefónica no es una autorización del titular en los términos que exige el tratamiento de datos.'),

 (0,
  'Al conformar una historia laboral, usted encuentra que entre el folio 47 y el 49 no está el 48, que el índice menciona un documento que no aparece y que hay tres hojas sueltas sin foliar al final de la carpeta. Un compañero propone refoliar todo desde el principio para que quede continuo y archivar las sueltas donde «parezca que van». El expediente debe remitirse al archivo central el viernes y soporta dos certificaciones que ya fueron expedidas con base en él.',
  '¿Cuál es la actuación correcta?',
  ['Dejar constancia escrita y detallada de cada hallazgo, no alterar la foliación existente ni ubicar documentos por criterio propio, e informarlo por el canal para que el competente disponga.',
   'Refoliar la carpeta completa desde el folio uno e incorporar las hojas sueltas en el orden cronológico que corresponda, de modo que el expediente quede íntegro antes de su remisión.',
   'Remitir el expediente como está y advertir verbalmente al archivo central, porque la responsabilidad de la conformación recae en quien integró la carpeta y no en quien la remite.',
   'Retirar las hojas sueltas y el índice inconsistente, y remitir únicamente los folios numerados, de modo que el expediente que llegue al archivo central no contenga documentos irregulares.'],
  'Correcto. La <strong>trazabilidad</strong> es lo que hace confiable un expediente, y refoliar borra precisamente la huella del problema. Lo que corresponde es <strong>documentar cada hallazgo</strong> —qué folio falta, qué menciona el índice, cuántas hojas sueltas hay—, no alterar nada por criterio propio e informar.',
  'Refoliar y acomodar destruye la evidencia de lo que faltaba. Advertir verbalmente no deja registro. Y retirar documentos es una depuración que no le corresponde y que podría eliminar soportes de un derecho.'),

 (2,
  'Un servidor le pide a usted que le explique por qué en su certificación de antecedentes aparece una anotación de hace seis años, si él «ya cumplió la sanción». Añade que esa anotación le está impidiendo participar en un proceso de selección en otra entidad y pide que se la borren. Está visiblemente angustiado, dice que no entiende por qué lo siguen castigando y el plazo de inscripción al proceso de la otra entidad cierra el viernes.',
  '¿Cuál es la actuación correcta?',
  ['Retirar la anotación de la historia laboral, porque la sanción ya fue cumplida y mantener el registro después del cumplimiento constituye una sanción adicional no prevista en la ley.',
   'Explicarle que la anotación es permanente y definitiva, de modo que no existe ninguna vía para su supresión y deberá convivir con ella durante el resto de su vida laboral.',
   'Explicarle que el registro y la inhabilidad derivada tienen reglas y términos propios, verificar qué muestran los registros de la entidad, orientarlo sobre el canal formal y radicar su solicitud.',
   'Expedirle una certificación en la que se omita la anotación y se haga constar únicamente que la sanción fue cumplida, para que pueda participar en el proceso de selección de la otra entidad.'],
  'Correcto. El <strong>registro</strong> de una sanción y la <strong>inhabilidad</strong> que de ella deriva no son lo mismo y tienen reglas y términos propios. Lo que corresponde es verificar qué muestran los registros, orientarlo sobre el canal y radicar su solicitud para que el competente la resuelva de fondo.',
  'Retirar la anotación por su cuenta altera un registro que soporta efectos jurídicos. Decirle que es definitiva sin verificar es informarle mal en un asunto que le afecta gravemente. Y expedir una certificación que omita la anotación es expedir un documento falso.'),

 (1,
  'En el comité de la División se discute si una conducta de un servidor debe reportarse. Un compañero sostiene que «si uno reporta y resulta que no era nada, queda mal con el equipo». Otro, que solo debe reportarse lo que uno tenga plenamente probado. Usted observó un hecho concreto y verificable, no un rumor: un documento de una historia laboral fue retirado de la carpeta sin registro de préstamo y devuelto dos días después con una enmendadura en la fecha.',
  '¿Cuál es la conducta correcta?',
  ['Guardar silencio hasta tener certeza de lo ocurrido, porque reportar un hecho que luego resulta inocuo puede afectar injustamente a un compañero y deteriorar el ambiente del equipo.',
   'Poner el hecho observado en conocimiento del competente, describiéndolo tal como ocurrió y sin atribuir responsabilidad a nadie, y dejar constancia de lo reportado y de su fecha.',
   'Averiguar primero entre los compañeros quién pudo haber retirado el documento y, solo si identifica al responsable, reportarlo con su nombre al jefe de la División por escrito.',
   'Corregir la enmendadura y restablecer el documento a su estado original, dejando una anotación interna, para que el expediente quede en orden antes de que alguien lo advierta.'],
  'Correcto. El deber es <strong>reportar el hecho observado</strong>, no la conclusión: se describe lo que ocurrió, con precisión y sin atribuir responsabilidad, y se deja constancia. Reportar no es acusar: es activar a quien sí tiene competencia para verificar.',
  'Callar hasta tener certeza deja activo un riesgo sobre un expediente. Investigar por cuenta propia excede su rol y puede contaminar lo que después deba verificarse. Y «corregir» la enmendadura destruye la evidencia del hecho.'),

 (0,
  'Al revisar un informe técnico que le asignaron para examinar, usted encuentra que la conclusión es razonable pero que el procedimiento descrito no corresponde al que la entidad tiene establecido para ese tipo de verificación: se omitió un paso y se usó una fuente distinta de la prevista. El autor del informe le dice que «el resultado es el mismo» y que señalar el método solo generaría un retrabajo inútil. El informe va a soportar una decisión que afecta a una persona concreta.',
  '¿Cuál es la observación correcta?',
  ['Consignar que el método y el procedimiento utilizados no corresponden a los establecidos, describir en qué difieren y dejar esa observación en el examen, con independencia de la conclusión.',
   'Avalar el informe porque la conclusión es razonable, ya que lo que importa es el resultado y el procedimiento es un medio cuya variación no afecta la validez de lo concluido.',
   'Rechazar el informe en su totalidad y ordenar que se repita completo con el procedimiento establecido, porque un informe con método irregular carece de todo valor para la entidad.',
   'Consignar únicamente que se omitió un paso, sin mencionar el cambio de fuente, porque ese segundo aspecto es una decisión técnica del autor que no corresponde revisar a quien examina.'],
  'Correcto. Su función 2 es exactamente esta: examinar la <strong>pertinencia e idoneidad de los métodos, procedimientos y técnicas</strong>. Que la conclusión parezca razonable no sanea un método que no fue el establecido, y su examen debe decirlo. Decidir qué hacer con esa observación es de otro.',
  'Avalar por el resultado vacía de contenido su función. Rechazar y ordenar repetir es una decisión que no le corresponde adoptar. Y omitir el cambio de fuente deja fuera del examen justo lo que el examen debía mirar.'),

 (3,
  'Una servidora que está siendo investigada disciplinariamente por otra dependencia solicita en la División copia completa de su historia laboral. Un compañero le dice que no se le entregue «porque está investigada y podría usarla para defenderse». Otro, que se consulte primero con la dependencia que adelanta la investigación antes de entregar nada. La servidora es la titular de esa historia laboral y la necesita para preparar su defensa dentro del término que le concedieron.',
  '¿Cuál es la actuación correcta?',
  ['No entregarla mientras dure la investigación, porque el acceso a su historia laboral podría interferir con la actuación disciplinaria que otra dependencia adelanta en su contra.',
   'Consultar primero con la dependencia que investiga y entregar únicamente lo que esa dependencia autorice, para no afectar el curso de la actuación disciplinaria en trámite.',
   'Entregar la historia laboral completa de inmediato y sin ninguna verificación, porque la titular tiene derecho absoluto de acceso a todos los documentos que la entidad conserve sobre ella.',
   'Radicar la solicitud, verificar la identidad de la titular y qué documentos tienen reserva frente a terceros pero no frente a ella, y responder de fondo dentro del término con esa distinción.'],
  'Correcto. Frente al <strong>titular del dato</strong> la lógica se invierte: el habeas data le da derecho a conocer la información que sobre ella reposa, y <strong>estar investigada no se lo quita</strong> —al contrario, el debido proceso lo refuerza—. Lo que se verifica es su identidad y qué documentos tienen reserva por involucrar a terceros.',
  'Negar el acceso «porque podría defenderse» es exactamente lo contrario del debido proceso. Supeditar la entrega a lo que autorice otra dependencia traslada una decisión que no es suya. Y entregar sin verificar identidad ni reserva de terceros tiene el problema opuesto.'),

 (2,
  'Un jefe de dependencia le pide a usted que incluya en la hoja de vida de un servidor una anotación sobre un llamado de atención verbal que le hizo la semana pasada por llegar tarde dos veces. Le dice que quiere que «quede el antecedente» por si la conducta se repite, y que lo redacte usted mismo con sus palabras. No hay actuación disciplinaria, ni acto administrativo, ni decisión de autoridad competente alguna: solo una conversación entre el jefe y el servidor, sin registro.',
  '¿Cuál es la actuación correcta?',
  ['Incluir la anotación con la fecha del llamado de atención, porque el jefe inmediato es quien conoce la conducta del servidor y tiene interés legítimo en que quede registrada.',
   'Incluir la anotación pero en una carpeta interna de la dependencia y no en la historia laboral oficial, de modo que el jefe conserve el registro sin afectar el expediente formal.',
   'Explicarle que en la historia laboral solo se incorporan los documentos y actos que la norma prevé, y que una anotación de sanción requiere decisión en firme de autoridad competente.',
   'Negarse e informar el hecho a la oficina de control interno disciplinario, porque la solicitud del jefe podría constituir en sí misma una falta disciplinaria que debe investigarse.'],
  'Correcto. La historia laboral no es un cuaderno de apuntes: solo se incorpora lo que la norma prevé, y una <strong>anotación de sanción</strong> requiere una decisión <strong>en firme</strong> de autoridad competente. Un llamado verbal no es una sanción, y registrarlo así le crearía al servidor un antecedente que nunca existió.',
  'Incluirla a secas crea un antecedente sin fundamento. Guardarla en una carpeta paralela es peor: un registro oculto sobre una persona, fuera de todo control. Y denunciar de inmediato al jefe desborda la situación: lo que corresponde primero es explicarle por qué no procede.'),

 (1,
  'Durante la conformación de un expediente usted advierte que dos documentos fueron radicados con una diferencia de un día pero están foliados en orden inverso, y que un tercero tiene fecha posterior a la del cierre del expediente. Un compañero le dice que son detalles menores de archivo y que «nadie revisa eso». El expediente soporta el reconocimiento de una prestación que ya fue pagada, y el servidor podría controvertir el valor reconocido dentro del término.',
  '¿Por qué importa y qué corresponde hacer?',
  ['Son en efecto detalles formales de archivo que no afectan el fondo: basta con corregir el orden de la foliación para que el expediente quede presentable antes de su remisión.',
   'Importa porque el orden y las fechas son lo que permite reconstruir qué se tuvo a la vista y cuándo: debe dejarse constancia de las inconsistencias e informarse al competente, sin alterar nada.',
   'Importa pero la corrección es automática: debe reemplazarse el documento con fecha posterior por uno que tenga la fecha correcta, de modo que la cronología del expediente quede coherente.',
   'No importa en este caso porque el expediente ya cumplió su finalidad al soportar el reconocimiento, de modo que las inconsistencias no tienen efecto práctico sobre la prestación reconocida.'],
  'Correcto. El orden y las fechas de un expediente no son estética: son lo que permite reconstruir <strong>qué se tuvo a la vista y cuándo</strong>, que es justamente lo que se discute si alguien controvierte el reconocimiento. Se deja constancia, se informa y no se altera nada por criterio propio.',
  'Reordenar la foliación borra la inconsistencia sin explicarla. Reemplazar un documento por otro con «la fecha correcta» es falsear el expediente. Y decir que ya no importa desconoce que un reconocimiento puede revisarse después.'),

 (0,
  'Un compañero le comenta, en voz baja y al final de la tarde, que escuchó que un servidor de otra dependencia «está siendo investigado disciplinariamente» y le pregunta si usted puede confirmarlo consultando la historia laboral desde su usuario. Dice que no quiere detalles, solo saber si es cierto, porque va a trabajar con esa persona en un proyecto y quiere estar prevenido. Nadie ha solicitado esa información por el canal institucional.',
  '¿Cuál es la actuación correcta?',
  ['No consultar ni confirmar nada, explicarle que la información de la actuación y de la historia laboral está protegida y que el acceso al sistema se tiene por razón de las funciones.',
   'Confirmarle únicamente si existe o no la investigación, sin dar detalles, porque la sola existencia de una actuación no constituye por sí misma información sujeta a reserva legal.',
   'Consultar la historia laboral y, si confirma la investigación, informarlo al jefe del proyecto para que valore si esa persona debe participar en el equipo que se está conformando.',
   'Remitirlo a la oficina de control interno disciplinario para que allí le confirmen el dato, dejando constancia de que la División no entregó información sobre el servidor consultado.'],
  'Correcto. Dos límites se cruzan: la <strong>reserva</strong> de la actuación disciplinaria y el hecho de que el acceso al sistema se tiene <strong>por razón de las funciones y para ellas</strong>. Consultar por curiosidad —aun ajena— ya es usar el acceso para un fin que no es el suyo, y la consulta queda registrada a su nombre.',
  'Un «sí o no» revela exactamente lo que está protegido. Convertirse en informante ante un jefe que nada ha pedido por el canal agrava el asunto. Y remitirlo a control interno para que le confirmen un dato reservado solo traslada la solicitud improcedente.'),

 (2,
  'Al examinar un informe que le asignaron, usted no está seguro de si el método empleado es el adecuado, porque corresponde a una técnica que no domina y sobre la que no ha recibido capacitación. El término para rendir su examen vence mañana y no hay nadie en la División que domine esa técnica. Un compañero le dice que «avale y ya, que nadie va a revisar» y otro, que escriba que el método es inadecuado «por si acaso, así queda cubierto». El informe soporta una decisión que ya está en curso.',
  '¿Cuál es la actuación correcta?',
  ['Avalar el informe y dejar una nota interna que advierta que el método no fue verificado, de modo que la responsabilidad quede delimitada si posteriormente surge alguna objeción.',
   'Consignar que el método es inadecuado, porque ante la duda es preferible una observación de más que una de menos y así se protege la actuación de la entidad frente a terceros.',
   'Consignar con precisión el alcance de su examen y declarar expresamente el límite: qué pudo verificar y qué no, por qué, e informar por el canal para que se disponga lo pertinente.',
   'Solicitar una prórroga del término hasta capacitarse en la técnica correspondiente, porque rendir un examen sobre un método que no se domina carecería de todo valor técnico.'],
  'Correcto. Reconocer y <strong>declarar el límite</strong> del propio examen es parte del rigor, no una debilidad: se consigna qué se pudo verificar, qué no y por qué, y se informa para que se disponga lo pertinente. Eso es exactamente lo que hace útil un examen técnico.',
  'Avalar sin verificar es afirmar sin respaldo. Consignar que el método es inadecuado «por si acaso» es lo mismo al revés: una afirmación sin fundamento que puede perjudicar a alguien. Y pedir prórroga para capacitarse no resuelve un término que vence mañana.'),

 (3,
  'Un servidor le pregunta si una sanción disciplinaria que le impusieron hace tres años le impide participar en el concurso de ascenso que la entidad acaba de convocar. Un compañero le dice que «cualquier sanción inhabilita de por vida para ascender» y otro, que «las sanciones no tienen nada que ver con los concursos internos». El servidor necesita decidir si se inscribe, el plazo cierra esta semana y usted tiene acceso a los registros que permiten verificar la fecha exacta de la sanción.',
  '¿Cuál es la orientación correcta?',
  ['Que cualquier sanción disciplinaria inhabilita de manera permanente para participar en concursos de ascenso, de modo que no tiene sentido que se inscriba en el proceso convocado.',
   'Que las sanciones disciplinarias no tienen incidencia alguna en los concursos internos, de modo que puede inscribirse sin verificar nada sobre su situación disciplinaria anterior.',
   'Que debe consultar directamente con la oficina de control interno disciplinario, porque la División no tiene competencia para pronunciarse sobre los efectos de una sanción en un concurso.',
   'Que el artículo 193 del Decreto Ley 262 de 2000 exige, para el ascenso, no haber sido sancionado disciplinariamente el año anterior, además de calificación y reinducción mínimas del 70 %.'],
  'Correcto. El <strong>artículo 193</strong> es concreto: para concursar por ascenso se exige calificación <strong>igual o superior al 70 %</strong>, <strong>no haber sido sancionado disciplinariamente el año anterior</strong> y al menos <strong>70 %</strong> en los cursos de reinducción. Una sanción de hace tres años no encaja en esa exigencia temporal, pero el dato debe verificarse contra los registros.',
  'Ni inhabilita de por vida ni es irrelevante: la norma fija una ventana temporal concreta. Y remitirlo a otra oficina cuando la División es la que administra la información de carrera y apoya a la Comisión de Carrera lo deja dando vueltas con el plazo corriendo.'),

 (1,
  'Al cerrar una historia laboral de un servidor que se retiró, usted debe decidir qué documentos se conservan y por cuánto tiempo. Un compañero propone depurar y eliminar «lo que ya no sirve» para ahorrar espacio, y otro, conservarlo todo indefinidamente «por si acaso». La Tabla de Retención Documental de la dependencia prevé tiempos específicos para esta serie, y uno de los documentos de la carpeta no encaja con claridad en ninguna de las subseries previstas.',
  '¿Cuál es la actuación correcta?',
  ['Depurar los documentos que a su juicio ya no tengan utilidad y dejar constancia de lo eliminado, de modo que el expediente conserve solo lo esencial y se optimice el espacio de archivo.',
   'Aplicar los tiempos y las disposiciones que la Tabla de Retención Documental prevé para esa serie, y consultar por el canal cualquier caso que no encaje, dejando constancia de la consulta.',
   'Conservarlo todo indefinidamente, porque una historia laboral puede necesitarse en cualquier momento y eliminar cualquier documento genera un riesgo que no compensa el ahorro de espacio.',
   'Consultar al propio servidor retirado qué documentos desea que se conserven, porque es el titular de la información y tiene derecho a decidir sobre el destino de sus propios datos.'],
  'Correcto. La <strong>Tabla de Retención Documental</strong> es el instrumento que decide qué se conserva, por cuánto y qué se hace al final: no es criterio propio ni gusto personal. Y cuando un caso no encaja, se consulta por el canal y se deja constancia, que es lo que después demuestra que no se improvisó.',
  'Depurar por criterio propio puede eliminar el soporte de un derecho. Conservarlo todo indefinidamente desconoce el instrumento y satura el archivo. Y el titular tiene derechos sobre sus datos, pero no define los tiempos de retención documental de una entidad pública.'),

 (0,
  'Una dependencia le remite para examen un informe cuya conclusión coincide exactamente con lo que su jefe había anticipado en una reunión. Al revisarlo, usted encuentra que la muestra documental analizada fue seleccionada por quien elaboró el informe, sin criterio explicado, y que se excluyeron cuatro expedientes sin justificación. El jefe le pregunta si lo avala, le recuerda que hay prisa y menciona que la conclusión «ya se sabía desde el principio».',
  '¿Qué debe consignar?',
  ['Que el informe no explica el criterio de selección de la muestra ni justifica las exclusiones, lo que impide verificar la idoneidad del método, y que ese vacío debe subsanarse.',
   'Que el informe es adecuado porque su conclusión coincide con lo que la dependencia ya había establecido por otras vías, lo que confirma la consistencia del resultado obtenido.',
   'Que el informe debe rehacerse íntegramente con una muestra aleatoria que incluya la totalidad de los expedientes, porque cualquier selección introduce un sesgo inaceptable.',
   'Que el informe es válido pero debe anexarse una nota que advierta que la muestra fue seleccionada por el autor, para que el lector valore ese aspecto si lo considera relevante.'],
  'Correcto. Una muestra sin criterio explicado y con exclusiones sin justificar hace <strong>imposible verificar la idoneidad del método</strong>, y eso es precisamente lo que su examen debe decir. Que la conclusión coincida con lo esperado no es una validación: es, si acaso, una razón más para mirar el método con cuidado.',
  'Avalar por la coincidencia del resultado es el sesgo exacto que la objetividad busca evitar. Exigir que se analice la totalidad desconoce que el muestreo es legítimo cuando está justificado. Y una nota al pie no sustituye la observación sobre el método.'),

 (2,
  'Usted debe redactar la constancia de una verificación en la que encontró tres soportes correctos y uno con una irregularidad evidente. Un compañero le sugiere escribir «la documentación aportada presenta serias deficiencias que evidencian un manejo negligente por parte del interesado». Otro propone escribir solo «la documentación fue revisada», sin más. El interesado podrá recurrir lo que se decida con base en esa constancia.',
  '¿Cómo debe redactarse?',
  ['Con la fórmula que propone el primero, porque describe con claridad la gravedad de lo encontrado y le permite al competente dimensionar la situación antes de adoptar su decisión.',
   'Con la fórmula que propone el segundo, porque una constancia debe limitarse a dejar registro de que la actuación se surtió, sin entrar en valoraciones sobre los documentos revisados.',
   'Enumerando qué documento se revisó, qué acredita cada uno, cuál presenta la irregularidad y en qué consiste exactamente, sin adjetivos ni atribución de conductas a ninguna persona.',
   'Describiendo la irregularidad encontrada y omitiendo los tres soportes correctos, porque lo relevante para la decisión es el documento que impide tener por cumplido el requisito.'],
  'Correcto. Dos defectos opuestos y una sola salida. Los <strong>adjetivos</strong> («serias deficiencias», «manejo negligente») reemplazan el dato y además atribuyen una conducta; el <strong>«fue revisada»</strong> no dice nada. Lo correcto es enumerar: qué se revisó, qué acredita cada documento, cuál falla y en qué consiste la falla.',
  'La primera fórmula califica a la persona, que ni siquiera ha podido controvertir. La segunda deja al competente sin elementos para decidir. Y omitir los soportes correctos sesga la constancia: el competente necesita el cuadro completo.'),
]
