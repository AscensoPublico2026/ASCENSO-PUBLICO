# -*- coding: utf-8 -*-
"""Día 17 · Investigación criminal II: proceso penal, actos urgentes, entrevista y declaración — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol, modulos, armar

META = dict(
    codigo='FUN-INV-4TI15O-02',
    archivo='FUN-INV-4TI15O-02-proceso-penal-entrevista-declaracion.html',
    dia=17,
    titulo_doc='Investigación criminal II: proceso penal, entrevista y declaración',
    h1='Investigación criminal II<br>Proceso, entrevista y declaración',
    kicker='Día 17 · Conocimientos específicos',
    sub='El <strong>sistema penal acusatorio</strong> y sus etapas, los <strong>roles</strong> de cada interviniente, la <strong>objetividad de la Fiscalía</strong>, el <strong>principio de oportunidad</strong> y las salidas alternas, el <strong>papel del Ministerio Público</strong> en el proceso penal, la diferencia entre la <strong>prueba penal y la disciplinaria</strong>, los <strong>actos urgentes</strong> y —el bloque más práctico— la <strong>entrevista y la declaración</strong>: qué son, en qué se diferencian, quién puede recibirlas y qué hace un técnico cuando alguien quiere hablar durante una diligencia.',
    badges=['⏱ 110-130 min', '⚖️ Proceso penal', '🗣️ Entrevista'],
    fmeta='Investigación criminal II: proceso penal, actos urgentes, entrevista y declaración',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Investigación criminal II: proceso penal, entrevista y declaración',
)

FUENTE = 'guias/FUN-INT-03-intervencion-penal-procesal-penal.html'
SEC = secciones_mapeadas(FUENTE)

# se incorporan del día 16 solo los módulos que allí se dejaron fuera: proceso penal y prueba
from _lib import secciones as _sec
_PEN = _sec('guias/FUN-PEN-3PU17L-02-derecho-penal-procesal-penal.html')[2]
_cab, _mods = modulos(_PEN)
EXTRA = armar('', _mods, {8, 9, 10}, renumerar=False)

# ---------------------------------------------------------------- módulo nuevo
ENTREVISTA = '''<h3>Entrevista y declaración: qué son, quién las recibe y qué hace usted</h3>
  <p>Este es el bloque donde más se equivoca quien llega al cargo sin haberlo estudiado, porque la situación es cotidiana: usted está practicando una prueba técnica y <strong>alguien quiere hablar</strong>. Un servidor que explica, un testigo que recuerda algo, el propio investigado que «quiere contarlo todo». Saber qué es cada figura y quién puede recibirla es lo que evita arruinar tanto la diligencia como la declaración.</p>
  <div class="tabla-wrap">
    <table>
      <caption>Las figuras y su lugar</caption>
      <thead><tr><th>Figura</th><th>Qué es</th><th>Quién la recibe</th><th>Qué hace el Técnico Investigador</th></tr></thead>
      <tbody>
        <tr><td><strong>Entrevista</strong></td><td>Acto de investigación en el que se recoge lo que una persona dice saber sobre los hechos. No se rinde bajo juramento ni ante el juez.</td><td>El servidor con competencia o quien esté expresamente comisionado o delegado para ello.</td><td>No la recibe por iniciativa propia. Si está delegada, la practica conforme a lo encargado y la documenta.</td></tr>
        <tr><td><strong>Declaración / testimonio</strong></td><td>Medio de prueba: declaración de quien conoce los hechos, con las formalidades que la ley exige.</td><td>El funcionario competente dentro de la actuación, con las garantías del caso.</td><td>Puede apoyarla técnicamente; no la recibe ni valora su credibilidad.</td></tr>
        <tr><td><strong>Versión libre</strong></td><td>Garantía del investigado: la oportunidad de dar su versión en el proceso disciplinario.</td><td>El servidor competente, por el procedimiento previsto.</td><td>La encauza: informa cuál es la vía y deja constancia de que la persona manifestó querer rendirla.</td></tr>
        <tr><td><strong>Manifestación espontánea</strong></td><td>Lo que alguien dice por su cuenta durante una diligencia, sin que se le pregunte.</td><td>Nadie la «recibe»: ocurre.</td><td><mark>La consigna en el acta</mark> tal como fue hecha, sin calificarla ni profundizar con preguntas.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>La regla práctica: encauzar, no recibir</h4>
  <p>Cuando alguien quiere hablar durante una diligencia que usted practica, la conducta correcta tiene tres movimientos y se repite siempre igual:</p>
  <div class="flujo">
    <div class="flujo-paso"><div class="fp-n">1</div><div><b>No preguntar</b><p>No formular preguntas dirigidas a obtener información sobre los hechos: eso convertiría la conversación en una entrevista que usted no tiene delegada.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">2</div><div><b>Consignar lo dicho</b><p>Dejar constancia en el acta de la manifestación, <strong>tal como fue hecha</strong>, sin resumirla a su manera, sin calificarla y sin valorar su credibilidad.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">3</div><div><b>Informar la vía</b><p>Indicar a la persona ante quién y por qué procedimiento puede rendir su versión, y poner el hecho en conocimiento del competente.</p></div></div>
  </div>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Dos distractores inseparables de este tema. El primero: <strong>recibir la declaración «para que no se pierda»</strong> —suena diligente y es actuar fuera de la delegación—. El segundo, su reflejo: <strong>no dejar ninguna constancia</strong> «porque no corresponde» —suena prudente y borra del expediente un hecho que el competente debía conocer—. La respuesta correcta casi siempre está en el medio: no recibir, pero sí consignar.</p></div>
  <h4>Por qué no es un formalismo</h4>
  <p>Una declaración recibida por quien no tenía competencia ni delegación no solo es inútil: puede contaminar lo que sí estaba bien hecho. Si la defensa demuestra que el técnico interrogó a su representado durante una diligencia técnica, sin las garantías del caso y sin título para hacerlo, la discusión deja de ser sobre lo que el examen arrojó y pasa a ser sobre la regularidad de toda la actuación. El art. 158 del Código vuelve a asomar: lo recaudado desconociendo derechos fundamentales <strong>se tendrá como inexistente</strong>.</p>
  <h4>Actos urgentes: cuándo la demora sí cuesta la prueba</h4>
  <p>El otro extremo del tema es igual de importante. Hay situaciones en las que esperar equivale a perder: material que se está alterando, un registro que se sobrescribe, un elemento que está por salir del lugar. Ahí la pregunta no es si actuar, sino <strong>qué de lo que haría falta está dentro de lo que usted puede hacer</strong>. La respuesta práctica tiene dos partes: se ejecuta lo que la delegación ya autoriza —asegurar, documentar, individualizar— y se informa <strong>de inmediato</strong> lo que la excede, dejando constancia del riesgo advertido y de la hora. Lo que nunca es correcto es el atajo: ampliar el objeto por cuenta propia invocando la urgencia.</p>
  <div class="checkpoint" data-cp="9">
    <div class="cp-q">✋ Punto de control: durante una diligencia el investigado le dice que quiere contarle lo que pasó. ¿Qué hace?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">Recibe la manifestación por escrito y la anexa al informe, para que la información no se pierda.</button>
    <button class="cp-opt" data-ans="1">No le formula preguntas, consigna en el acta lo que manifestó tal como lo dijo, le informa ante quién puede rendir su versión y lo pone en conocimiento del competente.</button>
    <button class="cp-opt" data-ans="0">Lo escucha sin dejar constancia, porque recibir versiones no está dentro del objeto de su delegación.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  '''

SEC[2] = SEC[2].rstrip() + '\n\n  ' + EXTRA + '\n\n  ' + ENTREVISTA + '\n'

SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>', '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>', '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('Profesional Universitario 3PU-17', 'Técnico Investigador 4TI-15'),
    ('Profesional Universitario, código 3PU-17', 'Técnico Investigador, código 4TI-15'),
    ('Profesional Universitario', 'Técnico Investigador'),
    ('(3PU-17)', '(4TI-15)'), ('3PU-17', '4TI-15'), ('3PU17L', '4TI15O'), ('3PU', '4TI'),
    ('146-2026', '257-2026'), ('112-2026', '257-2026'),
    ('dictamen contable', 'dictamen técnico'), ('peritaje contable', 'peritaje técnico'),
    ('Procuradurías de Instrucción', 'dependencias que solicitan apoyo técnico'),
    ('Procuraduría de Instrucción', 'Dirección Nacional de Investigaciones Especiales'),
    ('El instructor', 'El servidor que instruye'), ('el instructor', 'el servidor que instruye'),
    ('al instructor', 'al servidor que instruye'), ('del instructor', 'del servidor que instruye'),
    ('un instructor', 'un servidor que instruye'), ('Un instructor', 'Un servidor que instruye'),
    ('instructor', 'servidor que instruye'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)

ACTA = '''<h3>El acta que resiste la contradicción: técnica de documentación</h3>
  <p>Todo lo anterior converge en un documento: el acta. Y el acta tiene un destino previsible: alguien la va a leer buscando el punto por donde atacarla. Documentar con técnica no es escribir bonito, es escribir de modo que lo consignado <strong>siga en pie</strong> cuando la defensa lo examine. Estas son las reglas que lo logran, y valen para cualquier especialidad técnica.</p>
  <h4>Las seis reglas del acta</h4>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Regla</th><th>Qué significa</th><th>Qué evita</th></tr></thead>
      <tbody>
        <tr><td><strong>1. Identifique todo</strong></td><td>Fecha, hora de inicio y de cierre, lugar exacto, quiénes intervienen con nombre y calidad, y el título de la actuación (la delegación).</td><td>Que se discuta si la diligencia ocurrió como se dice, o si quien actuó tenía con qué.</td></tr>
        <tr><td><strong>2. Describa, no concluya</strong></td><td>«La carpeta presenta la cubierta doblada en el borde inferior derecho», no «la carpeta está deteriorada».</td><td>Que el lector tenga que confiar en su apreciación en lugar de verificar un hecho.</td></tr>
        <tr><td><strong>3. Mida lo medible</strong></td><td>Cantidades, dimensiones, folios, seriales, horas. Si no se pudo medir, se dice que no se pudo y por qué.</td><td>Los adjetivos que suenan a dato y no lo son: «numerosos», «evidente», «considerable».</td></tr>
        <tr><td><strong>4. Consigne lo dicho textualmente</strong></td><td>Lo que alguien manifiesta se consigna como lo dijo, entre comillas si es posible, no resumido a su manera.</td><td>Que se discuta si el acta refleja lo manifestado o la interpretación de quien escribía.</td></tr>
        <tr><td><strong>5. Registre lo que no salió</strong></td><td>Lo que no se pudo hacer, lo que faltaba, lo que se desvió del plan, con su causa.</td><td>Que un vacío no explicado parezca una omisión deliberada o una pérdida.</td></tr>
        <tr><td><strong>6. Cierre y haga firmar</strong></td><td>Lectura, oportunidad de observaciones, firma de los intervinientes y constancia de quien se niegue a firmar.</td><td>Que el acta aparezca como un documento unilateral que nadie pudo controvertir.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>La regla 4 en detalle: por qué el resumen es peligroso</h4>
  <p>Resumir lo que alguien dijo parece una cortesía con el lector y es, casi siempre, una fuente de problemas. Cuando usted escribe «el servidor manifestó que desconocía el procedimiento», está traduciendo: puede que haya dicho que <em>no recordaba</em> el procedimiento, o que <em>nadie se lo había explicado</em>, o que <em>lo conocía pero no se aplicaba en su oficina</em>. Las tres cosas son distintas y la diferencia puede ser decisiva al valorar la culpabilidad. Consignar textualmente no es desconfianza del lector: es dejar que la valoración la haga quien debe hacerla, con el material real.</p>
  <h4>Cuando la versión cambia: contradicciones</h4>
  <p>Ocurre con frecuencia: una persona dice algo que contradice lo que dijo antes, por escrito o en la misma diligencia. La tentación es ordenar el relato, elegir la versión «buena» o pedir a la persona que aclare cuál sostiene. Las tres son errores:</p>
  <ul class="lista">
    <li><strong>Las dos versiones se consignan completas</strong>, en el orden en que se produjeron, sin jerarquizar su credibilidad.</li>
    <li><strong>No se interroga para resolver la contradicción</strong>: hacerlo convierte la constancia en un interrogatorio que usted no tiene delegado.</li>
    <li><strong>Se deja constancia de la contradicción como hecho</strong> —«al folio 12 obra manifestación escrita en sentido distinto»— y se pone en conocimiento del competente, que es quien valorará.</li>
  </ul>
  <div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Un servidor presente en la diligencia afirma que el equipo nunca salió de la oficina. Usted tiene a la vista un registro de salida firmado por él tres semanas antes. Él insiste y se altera.</p>
    <p><strong>Cómo proceder.</strong> Consignar textualmente lo que afirma, consignar la existencia y el contenido del registro de salida como hecho documental, y no confrontarlo ni pedirle que explique la diferencia. La contradicción queda documentada, que es exactamente lo que el competente necesita; resolverla no es su trabajo, y hacerlo convertiría la diligencia en un interrogatorio sin título.</p>
  </div>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Cuando un caso le presente una contradicción, descarte las opciones que proponen «aclarar con la persona», «pedirle que precise» o «confrontarla con el documento». Todas suenan rigurosas y todas son interrogatorio. La correcta consigna las dos versiones y deja la valoración a quien corresponde.</p></div>

  '''
SEC[2] = SEC[2].rstrip() + "\n\n  " + ACTA + "\n"

TECNICAS = '''<h3>Tres técnicas que sirven en cualquier especialidad</h3>
  <p>El formato de la convocatoria pide «procedimientos en investigación criminal» sin especificar un área, y el manual habla de actividades «técnicas y técnico científicas» en plural. Como la especialidad concreta varía, conviene dominar las tres técnicas que no dependen de ella y que aparecen en cualquier apoyo: la observación documentada, la verificación documental y el análisis de información.</p>
  <h4>1. Observación documentada</h4>
  <p>Es la más básica y la que más se hace mal. Observar, en sentido técnico, no es mirar: es registrar un estado de modo que otro pueda reconstruirlo sin haber estado. Tiene tres exigencias. <strong>Sistematicidad</strong>: se recorre el objeto o el lugar en un orden definido —del conjunto al detalle— y no según lo que llame la atención. <strong>Separación entre dato y apreciación</strong>: se consigna lo que se ve, no lo que se concluye de ello; «hay rastros de apertura en el precinto» es un dato, «el precinto fue manipulado» es una conclusión. Y <strong>fijación</strong>: lo observado queda en un soporte —descripción, medición, fotografía— en el momento, porque el estado inicial existe una sola vez.</p>
  <h4>2. Verificación documental</h4>
  <p>Consiste en establecer si un documento dice lo que se afirma que dice y si es consistente consigo mismo y con los demás. Tres comprobaciones ordenan el trabajo y responden tres preguntas distintas:</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Comprobación</th><th>Pregunta que responde</th><th>Hallazgo típico</th></tr></thead>
      <tbody>
        <tr><td><strong>Integridad</strong></td><td>¿Está completo? ¿La foliación corresponde? ¿Falta algo?</td><td>Folios faltantes, numeración interrumpida, anexos anunciados y ausentes.</td></tr>
        <tr><td><strong>Consistencia interna</strong></td><td>¿El documento se contradice a sí mismo?</td><td>Una fecha anterior a la del hecho que narra, cifras que no suman, firmas de quien no figura en el encabezado.</td></tr>
        <tr><td><strong>Consistencia externa</strong></td><td>¿Concuerda con los otros documentos y registros?</td><td>Un acta que afirma una entrega que el registro de salida no muestra, dos documentos con el mismo número.</td></tr>
      </tbody>
    </table>
  </div>
  <p>Note que ninguna de las tres le pide concluir que alguien falsificó algo. Las tres producen <strong>hallazgos descriptivos</strong>, que es exactamente lo que su informe debe contener.</p>
  <h4>3. Análisis de información</h4>
  <p>Cuando el material es un volumen de datos —registros de acceso, movimientos, listados, trazas— la técnica consiste en hacerlos comparables y después buscar lo que no encaja. En la práctica: se <strong>normaliza</strong> (mismo formato de fecha, mismos nombres de campo, duplicados identificados), se <strong>cruza</strong> (un registro contra otro que debería coincidir) y se <strong>describe la discrepancia</strong> con su magnitud. La trampa de este trabajo es la inferencia prematura: un cruce que arroja una diferencia es un hallazgo; afirmar por qué existe esa diferencia ya es una explicación, y la explicación la construye quien valora.</p>
  <div class="box ok">
    <div class="box-title">✅ El hilo común de las tres</div>
    <p>Las tres técnicas producen lo mismo: <strong>hechos descritos, con el método que permitió establecerlos y los límites de ese método</strong>. Ninguna produce conclusiones jurídicas, y ninguna necesita producirlas para ser decisiva. Si domina esa forma de trabajar, la especialidad concreta que le asignen será un detalle operativo: el criterio es el mismo.</p>
  </div>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Las preguntas de técnica suelen enfrentar <strong>una opción que describe el hallazgo</strong> con <strong>otra que lo explica</strong>. La segunda siempre parece más completa y más útil. Es el distractor: explicar la causa de una discrepancia es valorar, y valorar no le corresponde.</p></div>

  '''
SEC[2] = SEC[2].rstrip() + "\n\n  " + TECNICAS + "\n"

PATRONES = '''<h3>Ocho patrones de pregunta de este bloque, con su respuesta</h3>
  <p>Cierre el día con esto, porque es lo que va a reconocer en la prueba. Las preguntas de investigación criminal de una convocatoria como la suya se repiten en ocho formas. Si identifica el patrón, la opción correcta aparece casi sola.</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Si el caso dice…</th><th>El patrón es…</th><th>La respuesta correcta hace…</th></tr></thead>
      <tbody>
        <tr><td>«Alguien quiere contarle lo que pasó»</td><td>Encauzar sin recibir</td><td>No pregunta, consigna lo manifestado tal como se dijo, informa la vía y pone en conocimiento.</td></tr>
        <tr><td>«Lo dicho contradice lo escrito»</td><td>Contradicción</td><td>Consigna las dos versiones completas, sin jerarquizar credibilidad ni confrontar a la persona.</td></tr>
        <tr><td>«Si no actúa ahora, se pierde»</td><td>Acto urgente</td><td>Ejecuta lo que la delegación ya autoriza, informa de inmediato lo que la excede y deja constancia de la hora.</td></tr>
        <tr><td>«Aproveche que está allá»</td><td>Ampliación del objeto</td><td>No amplía. Documenta lo observado y pide la ampliación por escrito.</td></tr>
        <tr><td>«Esto es un delito, mándelo a la Fiscalía»</td><td>Compulsa de copias</td><td>Describe sin calificar y pone en conocimiento del competente, que decide la compulsa.</td></tr>
        <tr><td>«La Fiscalía archivó, archive usted»</td><td>Independencia de las acciones</td><td>Continúa: el objeto y el estándar de cada actuación son distintos.</td></tr>
        <tr><td>«Explique por qué hay esa diferencia»</td><td>Inferencia prematura</td><td>Describe la discrepancia y su magnitud; no explica la causa.</td></tr>
        <tr><td>«Firme usted, que el jefe no está»</td><td>Proyectar no es decidir</td><td>No firma. Remite el proyecto por el canal e informa por escrito el riesgo del término.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>El denominador común</h4>
  <p>Mire la columna de la derecha completa y verá que las ocho respuestas son variaciones de una sola conducta: <mark>hacer lo que el título autoriza, documentar con precisión todo lo demás y poner en conocimiento de quien decide</mark>. No es una regla de examen: es la descripción de cómo trabaja un técnico investigador competente. Y es la razón por la que las opciones que «resuelven el problema» —recibir la declaración, ampliar el examen, remitir a la Fiscalía, firmar el auto, explicar la diferencia— son casi siempre los distractores: resuelven el problema invadiendo una competencia ajena.</p>
  <div class="box gold">
    <div class="box-title">💡 Idea clave del día</div>
    <p>El proceso penal y las técnicas de investigación se estudian, en este cargo, para <strong>reconocer y documentar</strong>, no para investigar delitos ni para interrogar. La frontera es nítida: usted asegura, observa, verifica, analiza y describe; otro pregunta, valora, califica y decide. Un técnico que entiende esa frontera produce prueba utilizable; uno que la cruza produce una discusión sobre la regularidad de su propia actuación.</p>
  </div>
  <div class="box ok">
    <div class="box-title">🧠 Frase para recordar</div>
    <p>«No pregunto: consigno lo que me dicen. No explico: describo lo que encuentro. No remito: pongo en conocimiento. No confronto: dejo las dos versiones. Y lo que mi título no autoriza, lo informo por escrito en el momento mismo en que lo veo venir, no cuando ya es tarde para que alguien haga algo con eso.»</p>
  </div>

  '''
SEC[2] = SEC[2].rstrip() + "\n\n  " + PATRONES + "\n"

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el proceso '
              'penal y la actividad de investigación: etapas y roles del sistema acusatorio, objetividad de la '
              'Fiscalía, principio de oportunidad, papel del Ministerio Público, prueba penal frente a prueba '
              'disciplinaria, actos urgentes, y entrevista, declaración y versión libre.')

P = [
 (1,
  'Usted practica una prueba técnica delegada en una dependencia. Mientras trabaja, un servidor que presenció los hechos se le acerca y empieza a contarle con detalle lo que, según él, ocurrió realmente. Nadie del despacho está presente. Su delegación se refiere al examen de dos equipos y no incluye recibir entrevistas ni declaraciones. El servidor habla con ganas y dice que después no va a querer repetirlo. Es su primera diligencia en esa dependencia y el acta sigue abierta sobre la mesa.',
  '¿Cuál es la actuación correcta?',
  ['Escucharlo con atención y no dejar ninguna constancia, porque recibir versiones excede el objeto de su delegación y registrarlas podría dar a la conversación un valor que no tiene.',
   'No formularle preguntas, consignar en el acta lo que manifestó tal como lo dijo, informarle ante quién puede rendir su versión y poner el hecho en conocimiento del competente.',
   'Recibirle una manifestación escrita y firmada en ese momento, para que la información no se pierda, y anexarla al informe técnico como soporte del contexto de los hechos.',
   'Pedirle que espere y llamar al despacho para que autorice verbalmente la entrevista, practicándola en ese momento si la autorización se obtiene antes de terminar la diligencia.'],
  'La conducta correcta está en el medio de los dos errores típicos: no se recibe —eso sería una entrevista sin título— pero sí se consigna, porque callarlo borraría del expediente un hecho que el competente debe conocer.',
  'Escuchar sin dejar constancia pierde el hecho; recibir una manifestación escrita es actuar fuera de la delegación; y una autorización verbal no sustituye la delegación escrita para una actuación distinta.'),

 (0,
  'Durante una diligencia, un servidor afirma que el equipo nunca salió de la oficina. Usted tiene a la vista un registro de salida firmado por él tres semanas antes. Él insiste, se altera y le pide que no deje constancia de lo que dijo. Hay dos testigos presentes y el acta sigue abierta. La diligencia fue delegada esta mañana y el registro de salida está a la vista de los presentes. Usted conoce al servidor de apoyos anteriores y nunca había tenido un incidente con él.',
  '¿Cómo debe proceder?',
  ['Consignar textualmente lo que afirma, consignar la existencia y el contenido del registro de salida como hecho documental, y no confrontarlo ni pedirle que explique la diferencia.',
   'Confrontarlo con el registro de salida y consignar su explicación, de modo que la contradicción quede resuelta en el acta antes de que la diligencia se cierre formalmente.',
   'Consignar únicamente el registro de salida, que es el documento objetivo, y omitir la manifestación por ser contraria a lo que la prueba documental ya acredita en el expediente.',
   'Atender su petición y no consignar la manifestación, dejando únicamente constancia del registro de salida y de que el servidor estuvo presente durante toda la diligencia.'],
  'Las dos versiones se consignan completas, sin jerarquizar credibilidad y sin confrontar. La contradicción documentada es exactamente lo que el competente necesita; resolverla convertiría la diligencia en un interrogatorio sin título.',
  'Confrontarlo es interrogar; omitir su manifestación o atender su petición de no registrarla suprime un hecho que ocurrió y que el competente debe conocer.'),

 (3,
  'Un compañero sostiene que el Ministerio Público «no tiene nada que hacer» en el proceso penal y que la PGN solo actúa en lo disciplinario. Otro afirma que el agente del Ministerio Público puede acusar junto con la Fiscalía. El jefe pide la precisión para un documento interno, porque varios del grupo van a presentar la prueba. Varios del grupo presentan la prueba la próxima semana y el documento sale firmado por el jefe de la Dirección.',
  '¿Cuál es la precisión correcta?',
  ['El Ministerio Público no interviene en el proceso penal: su función se limita al control disciplinario y a la vigilancia de la conducta oficial de los servidores públicos.',
   'El agente del Ministerio Público ejerce la acción penal junto con la Fiscalía cuando los hechos involucran a servidores públicos en ejercicio de sus funciones.',
   'El Ministerio Público interviene únicamente en la etapa de juicio oral, como garante del debido proceso, y no en las etapas anteriores del proceso penal acusatorio.',
   'El Ministerio Público interviene en el proceso penal en defensa del orden jurídico, del patrimonio público y de los derechos y garantías fundamentales, sin ejercer la acción penal.'],
  'La intervención del Ministerio Público en el proceso penal es una función constitucional propia: defiende el orden jurídico, el patrimonio público y los derechos fundamentales. Lo que no hace es ejercer la acción penal, que es de la Fiscalía.',
  'Ni está ausente del proceso penal, ni acusa junto con la Fiscalía, ni su intervención se limita al juicio oral.'),

 (2,
  'Usted analiza un volumen de registros de acceso a un sistema y, al cruzarlos con los horarios de la dependencia, encuentra una diferencia de once ingresos que no corresponden a ninguna jornada laboral registrada. El despacho le pide que el informe explique por qué ocurrieron esos ingresos. Usted puede describir la discrepancia y su magnitud con precisión, pero no establecer su causa. El informe debe rendirse pasado mañana y el cruce quedó documentado en una hoja de cálculo con sus fórmulas.',
  '¿Cómo debe redactar el informe?',
  ['Explicando la causa más probable de los ingresos conforme a su experiencia técnica, y advirtiendo que se trata de una hipótesis sujeta a verificación posterior del despacho.',
   'Omitiendo la discrepancia del informe, dado que no es posible explicarla y consignarla sin explicación podría inducir a conclusiones erróneas sobre la conducta investigada.',
   'Describiendo la discrepancia, su magnitud y el método del cruce, con las limitaciones de ese método, sin explicar la causa, que es una valoración del competente.',
   'Describiendo la discrepancia y solicitando al despacho que amplíe el objeto del apoyo para que usted pueda establecer la causa antes de que el informe sea rendido.'],
  'Un cruce que arroja una diferencia es un hallazgo; afirmar por qué existe es una explicación, y la explicación la construye quien valora. El informe aporta la discrepancia, su magnitud, el método y sus límites.',
  'Explicar la causa —aun como hipótesis— es la inferencia prematura que este bloque enseña a evitar; omitir la discrepancia compromete la veracidad; y pedir ampliación no es necesario para rendir lo que ya se estableció.'),

 (1,
  'Durante una diligencia usted advierte que un registro está siendo sobrescrito en ese momento desde un equipo de la oficina y que, si no actúa, la información anterior se perderá. Su delegación autoriza asegurar y examinar los equipos de ese área. El despacho no responde llamadas y no hay nadie más de la PGN en el lugar. Usted está solo con un compañero, la delegación escrita está en su poder y el proceso continúa en la pantalla.',
  '¿Cuál es la actuación correcta?',
  ['Esperar la respuesta del despacho antes de cualquier actuación material, porque una medida adoptada sin instrucción expresa podría exponer lo actuado a exclusión posterior.',
   'Asegurar de inmediato los equipos comprendidos en la delegación, documentando la hora, el estado en que los halló y el riesgo advertido, e informarlo por escrito en cuanto sea posible.',
   'Ordenar al servidor que está usando el equipo que detenga la operación y permanezca en el lugar hasta que el despacho responda, dejando constancia de la instrucción impartida.',
   'Grabar la pantalla del equipo mientras se sobrescribe el registro, para dejar evidencia audiovisual del hecho, y abstenerse de intervenir sobre los equipos sin instrucción expresa.'],
  'Se ejecuta lo que la delegación ya autoriza —asegurar los equipos del área— documentando la hora y el riesgo, y se informa en cuanto sea posible. Esperar cuando la prueba se está perdiendo es perderla.',
  'Impartir instrucciones a un servidor ajeno excede su rol; y limitarse a grabar renuncia a la medida que su delegación sí autorizaba.'),

 (3,
  'Un compañero sostiene que la prueba practicada en el proceso penal sirve tal cual en el disciplinario, «porque es la misma prueba y ya fue recaudada por una autoridad». El jefe pide la precisión porque el despacho quiere incorporar unos elementos de una investigación penal en curso. La investigación penal lleva cuatro meses y el despacho disciplinario tiene un término corriendo. El despacho quiere incorporar los elementos esta misma semana, antes de evaluar el expediente.',
  '¿Cuál es la precisión correcta?',
  ['Sirve tal cual: una prueba recaudada por autoridad competente conserva su valor en cualquier actuación, sin que se requiera trámite adicional para incorporarla al expediente.',
   'No sirve en ningún caso: cada actuación debe recaudar su propia prueba, porque los estándares de una y otra jurisdicción son incompatibles entre sí y no admiten traslado.',
   'Sirve solo cuando el proceso penal haya terminado con sentencia ejecutoriada, momento en el cual la prueba adquiere la firmeza necesaria para ser trasladada a otra actuación.',
   'Puede trasladarse lo descubierto por la Fiscalía y no debatido en juicio, sometiéndolo a contradicción en el proceso disciplinario; si la penal sigue en curso, se pide al fiscal del caso.'],
  'El traslado es posible y tiene una condición que define todo: la contradicción dentro del proceso disciplinario. Y si la investigación penal está en curso, los elementos se piden al fiscal del caso, que decide qué puede entregar sin afectarla.',
  'Ni entra sin trámite, ni está vedado el traslado, ni hay que esperar la sentencia: la condición es la contradicción.'),

 (0,
  'Al redactar el acta de una diligencia, usted debe consignar lo que un servidor manifestó. Él dijo textualmente: «eso no lo sabía, a mí nunca me explicaron ese procedimiento». Un compañero le sugiere escribir «el servidor manifestó que desconocía el procedimiento», que es más breve y dice lo mismo. El acta se cierra hoy y los dos testigos presentes escucharon la frase completa. Usted debe cerrar el acta antes de salir de la dependencia, que ya está en horario de cierre.',
  '¿Cuál es la precisión correcta sobre la técnica de documentación?',
  ['Debe consignarse textualmente: el resumen traduce y pierde la diferencia entre no saber, no recordar y no haber sido informado, que puede ser decisiva al valorar la culpabilidad.',
   'El resumen es preferible porque hace el acta más legible, siempre que refleje fielmente el sentido de lo manifestado y no altere la sustancia de lo que la persona expresó.',
   'Debe consignarse el resumen y, además, anexar una grabación de la manifestación, de modo que el texto sea breve y el contenido completo quede siempre disponible para el lector.',
   'Es indiferente, porque la valoración de lo manifestado corresponde al servidor competente y la forma de consignarlo no incide en el resultado de esa valoración jurídica.'],
  '«No lo sabía porque nunca me lo explicaron» y «desconocía el procedimiento» no son lo mismo: el primero atribuye una causa a un tercero. Consignar textualmente deja que la valoración la haga quien debe hacerla, con el material real.',
  'El resumen siempre traduce; una grabación no suple el texto del acta ni siempre es procedente; y la forma de consignar sí incide: es lo único que el valorador tendrá.'),

 (2,
  'El despacho le pide practicar una prueba técnica y, además, «indagar discretamente» con los compañeros del investigado qué saben del asunto, porque así se gana tiempo antes de ordenar testimonios. La delegación escrita se refiere al examen de un archivo digital. El servidor del despacho insiste en que es solo para orientar la investigación. La solicitud llegó por teléfono esta mañana y la diligencia está programada para pasado mañana.',
  '¿Cuál es la actuación correcta?',
  ['Hacer las averiguaciones de manera informal y sin dejar constancia, dado que no constituyen entrevistas formales y solo buscan orientar el trabajo del despacho solicitante.',
   'Hacer las averiguaciones y consignar en el informe lo que recoja, señalando que se obtuvo de manera informal y a solicitud verbal del despacho durante el apoyo técnico.',
   'No hacerlas: practicar lo delegado, dejar constancia escrita de la solicitud recibida e informar que recoger versiones requiere delegación y las garantías del procedimiento.',
   'Consultar al jefe inmediato y proceder conforme a lo que indique verbalmente, dejando anotación en el informe de la orientación recibida sobre las averiguaciones solicitadas.'],
  'Recoger versiones, con o sin el nombre de entrevista, requiere título y garantías. Lo correcto es practicar lo delegado, dejar la solicitud por escrito e informar por qué no procede así.',
  'Averiguar informalmente es precisamente lo que el procedimiento prohíbe, con o sin constancia; y una indicación verbal del jefe no suple la delegación ni las garantías del procedimiento.'),

 (1,
  'En la verificación documental de un expediente usted encuentra que un acta está fechada el 14 de mayo y narra un hecho ocurrido el 19 de mayo. Nada más en el documento explica la diferencia. El despacho espera el informe esta semana y le pregunta si el acta «es falsa». El expediente está en instrucción y usted conserva fotografías de las dos páginas del acta. El acta hace parte del material que usted debía verificar por delegación escrita del competente.',
  '¿Cómo debe responder en el informe?',
  ['Señalando que el acta es falsa, ya que una fecha anterior al hecho que narra es objetivamente imposible y constituye por sí misma una irregularidad documental verificable.',
   'Consignando el hallazgo de consistencia interna —la fecha del acta y la del hecho narrado— sin calificarlo, y poniéndolo en conocimiento del competente para lo de su cargo.',
   'Consignando el hallazgo y añadiendo que la causa más probable es un error de digitación, de modo que el competente disponga de una explicación técnica razonable del hecho.',
   'Omitiendo el hallazgo, dado que no es posible establecer la causa de la diferencia y consignarla podría sugerir una falsedad que el examen técnico no permite afirmar.'],
  'La verificación documental produce hallazgos descriptivos: aquí, una inconsistencia interna entre dos fechas. Calificarla como falsedad o explicarla como error de digitación son, ambas, valoraciones que no le corresponden.',
  'Afirmar falsedad excede el rol; proponer la causa es inferencia prematura; y omitir el hallazgo compromete la veracidad del informe.'),

 (3,
  'Un compañero afirma que el principio de oportunidad permite a la Fiscalía archivar cualquier caso y que, por eso, no vale la pena documentar bien un hallazgo penal. El jefe pide la precisión porque la idea está circulando en el grupo y afecta la calidad de los informes. La idea viene circulando desde la semana pasada y ya se nota en la calidad de dos informes del grupo. Dos informes del grupo salieron la semana pasada con hallazgos descritos de manera muy escueta.',
  '¿Cuál es la precisión correcta?',
  ['Tiene razón: el principio de oportunidad otorga a la Fiscalía una facultad discrecional de archivo que hace irrelevante la calidad del soporte documental del hallazgo.',
   'El principio de oportunidad no existe en el ordenamiento colombiano: toda noticia criminal debe ser investigada hasta su terminación mediante sentencia o preclusión.',
   'El principio de oportunidad solo aplica a delitos querellables, de modo que en los delitos contra la administración pública la Fiscalía siempre debe adelantar la investigación.',
   'Es una excepción reglada al deber de perseguir, con causales definidas y control judicial; y la calidad del soporte es lo que permite decidir con fundamento, no lo contrario.'],
  'El principio de oportunidad es una excepción reglada —con causales definidas y control judicial—, no una facultad discrecional de archivo. Y precisamente por ser reglada, la calidad del soporte es lo que permite decidir con fundamento.',
  'Ni es discrecional, ni es inexistente, ni se limita a los delitos querellables. Y en ningún caso la calidad del informe técnico es irrelevante.'),

 (0,
  'Al observar el estado de un elemento antes de recolectarlo, usted advierte un rastro de apertura en el precinto. El despacho le pregunta si el precinto fue manipulado. Usted puede describir con precisión el rastro, su ubicación y sus características, y fotografiarlo. Hay tres personas presentes y el elemento todavía no se ha recolectado ni embalado. Es la primera vez que usted encuentra un precinto en ese estado y el despacho pregunta por teléfono.',
  '¿Cómo debe consignarlo?',
  ['«El precinto presenta un rastro de apertura en el extremo superior, con las siguientes características y dimensiones…», acompañado de fotografía y medición, sin afirmar que fue manipulado.',
   '«El precinto fue manipulado», porque un rastro de apertura es un signo inequívoco y afirmarlo en esos términos permite al despacho actuar con la celeridad que el caso exige.',
   '«El precinto presenta signos de posible manipulación», fórmula que describe el hallazgo y, a la vez, advierte al despacho de cuál es su significado más probable.',
   '«El precinto se encontró en estado irregular», una descripción general que evita comprometer el informe con una afirmación categórica que el examen no permite sostener.'],
  'La separación entre dato y apreciación es el núcleo de la observación técnica: el rastro de apertura es un dato; la manipulación es una conclusión. Se describe el rastro, se mide y se fotografía.',
  '«Fue manipulado» y «signos de posible manipulación» concluyen, con distinto grado. Y «estado irregular» es un adjetivo que suena a dato y no lo es: no permite a nadie verificar qué se observó.'),

 (2,
  'La diligencia se desvió del programa metodológico: de cinco equipos previstos, dos están fuera de la sede en reparación y uno fue dado de baja hace un mes. Usted puede examinar hoy los dos restantes. El despacho no responde y el término vence pasado mañana. Usted ya levantó el acta de lo encontrado en la sede y conserva los soportes que la dependencia le entregó. El programa metodológico lo acordó usted mismo con el despacho hace dos semanas, por escrito.',
  '¿Cuál es la actuación correcta?',
  ['Suspender la diligencia y reprogramarla para cuando los cinco equipos estén disponibles, de modo que el informe pueda rendirse sobre el objeto completo de la delegación.',
   'Examinar los dos disponibles y rendir el informe sin aludir a los otros tres, para que el resultado se refiera únicamente a lo que efectivamente pudo examinarse.',
   'Examinar los dos disponibles, consignar con precisión qué ocurrió con los otros tres y con qué soporte, y precisar en el informe qué puede y qué no puede sostenerse.',
   'Examinar los dos disponibles y solicitar al despacho una ampliación del término antes de rendir el informe, para incluir después los otros tres en el mismo documento.'],
  'Se hace lo que sí es posible, se documenta con precisión lo que no y se informa. Una diligencia que se apartó del plan y lo explicó sigue siendo utilizable; una que se apartó y no lo dijo queda a merced de la contradicción.',
  'Suspender pierde lo que sí se podía hacer; omitir los tres equipos presenta el resultado como más completo de lo que es; y esperar una ampliación que nadie ha concedido arriesga el término.'),

 (1,
  'El despacho le solicita el informe para mañana y, al revisarlo, usted advierte que en un apartado escribió que el servidor «ocultó» un documento. Lo que usted documentó es que el documento no estaba en la carpeta donde debía estar y que no hay constancia de su salida. El informe no ha sido remitido. El informe está impreso y listo para firma, y el despacho lo espera a primera hora. El apartado está en la página cuatro del informe y usted conserva el acta de la verificación.',
  '¿Qué debe corregir?',
  ['Nada: «ocultó» describe el resultado de la verificación documental y es la forma más clara de comunicar al despacho lo que el examen efectivamente estableció.',
   'Sustituir «ocultó» por la descripción de lo verificado —el documento no obra en la carpeta y no hay constancia de salida— sin atribuir una conducta ni una intención.',
   'Mantener «ocultó» y añadir una nota aclarando que la atribución de la conducta corresponde al servidor competente y no al técnico que elaboró el informe.',
   'Sustituir «ocultó» por «presuntamente ocultó», de modo que la afirmación quede matizada sin obligarlo a reescribir el apartado completo del informe técnico.'],
  '«Ocultó» atribuye una conducta y una intención; lo verificado es que el documento no obra donde debía y que no hay constancia de salida. Esa descripción es más útil, porque es verificable.',
  'Mantenerlo con una nota o matizarlo con «presuntamente» sigue atribuyendo la conducta: el problema no es el grado de certeza, es que la atribución no le corresponde.'),

 (3,
  'Un testigo que usted debe atender en una diligencia pide que su identidad no quede en el acta porque teme represalias. Usted no tiene instrucción sobre el punto y el procedimiento exige identificar a los intervinientes. La diligencia está en curso y el testigo insiste en que, de lo contrario, no dirá nada. Nadie más de la PGN está presente y el acta todavía no se ha cerrado ni leído a los intervinientes. El testigo habla en voz baja para que los demás presentes no lo escuchen pedirlo.',
  '¿Cuál es la actuación correcta?',
  ['Acceder a la petición y consignar lo manifestado sin identificar a la persona, porque proteger al testigo prevalece sobre la formalidad de la identificación en el acta.',
   'Negarse y consignar la identidad de todos modos, dejando constancia de la petición, porque el procedimiento no admite excepciones y la protección no es asunto del técnico.',
   'Consignar la identidad en un documento separado que se remita aparte al despacho, de modo que el acta quede sin el dato y la identificación exista en otro soporte.',
   'Explicar que el procedimiento exige identificar a los intervinientes y que las medidas de protección las dispone el competente, y dejar constancia de la petición y del temor manifestado.'],
  'Las medidas de protección no las concede el técnico, pero el temor manifestado es un hecho relevante que debe llegar a quien puede disponerlas. Se explica, se deja constancia y se pone en conocimiento.',
  'Omitir la identidad por decisión propia altera el procedimiento; negarse sin encauzar el temor desatiende un hecho que el competente debe conocer; y repartir el dato en dos documentos crea una irregularidad adicional.'),

 (2,
  'Faltan cuatro días para la prueba. En los simulacros de este bloque usted reconoce bien las etapas del proceso penal, pero falla los casos de diligencia: elige la opción que «resuelve» la situación —recibir la declaración, confrontar al testigo, explicar la discrepancia, ampliar el examen—. Su registro muestra ese patrón en siete de los últimos diez casos. Lleva un registro de los simulacros resueltos y puede ver exactamente qué opción eligió cada vez que falló.',
  '¿Cuál es la mejor manera de corregirlo?',
  ['Memorizar las etapas del proceso penal y los roles de cada interviniente, porque dominar el marco hará evidente qué corresponde hacer en cada situación concreta de diligencia.',
   'Resolver más simulacros de este bloque hasta que la intuición mejore, dejando el repaso de las técnicas de documentación para los días previos a la presentación de la prueba.',
   'Aplicar el denominador común de los ocho patrones: hacer lo que el título autoriza, documentar lo demás y poner en conocimiento de quien decide. Lo que «resuelve» el problema suele invadir competencia ajena.',
   'Concentrarse en los casos de entrevista y declaración, que son los que más preguntas generan en este bloque, y repasar lo demás con la tabla de patrones de esta guía.'],
  'Las siete opciones que usted eligió comparten la misma falla: resuelven el problema invadiendo una competencia ajena. El denominador común de los ocho patrones es el filtro que las descarta de entrada.',
  'Dominar las etapas no corrige la confusión de roles; repetir simulacros sin cambiar el criterio repite el error; y concentrarse en un solo patrón deja fuera los otros siete.'),
]
