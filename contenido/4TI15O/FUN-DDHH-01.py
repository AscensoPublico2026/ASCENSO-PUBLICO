# -*- coding: utf-8 -*-
"""Día 18 · Derechos Humanos y Derecho Internacional Humanitario — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, secciones, aplicar_todas, limpieza_rol, modulos, armar

META = dict(
    codigo='FUN-DDHH-4TI15O-01',
    archivo='FUN-DDHH-4TI15O-01-derechos-humanos-dih.html',
    dia=18,
    titulo_doc='Derechos Humanos y Derecho Internacional Humanitario',
    h1='Derechos Humanos<br>y DIH',
    kicker='Día 18 · Conocimientos específicos',
    sub='Uno de los <strong>conocimientos específicos</strong> que el formato de convocatoria exige expresamente a su cargo. El <strong>bloque de constitucionalidad</strong> (art. 93), las <strong>obligaciones de respeto y garantía</strong>, la <strong>prohibición absoluta</strong> del artículo 12 de la Constitución y lo que significa para quien obtiene prueba, el <strong>DIH</strong> y sus principios, la diferencia entre una <strong>violación de DDHH</strong> y una <strong>infracción al DIH</strong>, el <strong>control de convencionalidad</strong>, la <strong>justicia transicional</strong> y sus cuatro pilares, la <strong>Ley 1448 de 2011</strong> y el papel del Ministerio Público frente a las víctimas.',
    badges=['⏱ 110-130 min', '🕊️ DDHH y DIH', '⚖️ Bloque'],
    fmeta='Derechos Humanos y Derecho Internacional Humanitario aplicados a la actividad investigativa',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Derechos Humanos y Derecho Internacional Humanitario',
)

FUENTE = 'guias/FUN-DDHH-01-derechos-humanos-dih-justicia-transicional.html'
SEC = secciones_mapeadas(FUENTE)

# del día de Fuerza Pública se toma solo el módulo de DDHH y DIH aplicados
_FP = secciones('guias/FUN-FP-3PU15C-01-fuerza-publica-armas-ddhh-dih.html')[2]
_cab, _mods = modulos(_FP)
FP_DDHH = armar('', _mods, {7}, renumerar=False)
# y los dos módulos sobre el régimen aplicable a la Fuerza Pública y el poder preferente de la PGN,
# porque la DNIE apoya investigaciones que recaen sobre sus miembros
FP_REG = armar('', _mods, {2, 5}, renumerar=False)

# ---------------------------------------------------------------- módulos nuevos
NUEVO_A = '''<h3>Por qué este tema está en tu temario y no es un relleno</h3>
  <p>Cuando un aspirante ve «Derechos Humanos y DIH» en la lista de conocimientos específicos de un cargo técnico de investigación, suele pensar que es un tema de cultura general que alguien añadió para completar. Es exactamente lo contrario. Está ahí por tres razones muy concretas, y las tres se traducen en conductas que la prueba evalúa.</p>
  <div class="flujo">
    <div class="flujo-paso"><div class="fp-n">1</div><div><b>Porque la PGN es, por mandato constitucional, guarda de los derechos humanos</b><p>El Ministerio Público tiene a su cargo la guarda y promoción de los derechos humanos. No es una función anexa de la entidad: es parte de su razón de ser, y quien trabaja en ella la ejerce en lo que hace.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">2</div><div><b>Porque la prueba que usted obtiene puede vulnerar derechos</b><p>Es la razón más práctica. Una diligencia es un acto de poder del Estado sobre personas y sobre sus cosas. Mal hecha, vulnera intimidad, dignidad o defensa. Y lo vulnerado, además, <strong>no sirve</strong>: el art. 158 del Código lo tiene por inexistente.</p></div></div>
    <div class="flujo-paso"><div class="fp-n">3</div><div><b>Porque hay conductas que la PGN investiga y que son violaciones de DDHH o infracciones al DIH</b><p>Cuando el hecho disciplinario consiste en una desaparición, una tortura, una ejecución o un ataque a persona protegida, el marco aplicable no es solo el interno: es también el internacional incorporado por el bloque.</p></div></div>
  </div>
  <div class="box gold">
    <div class="box-title">💡 La idea que ordena el día</div>
    <p>Los derechos humanos funcionan aquí en <strong>dos direcciones</strong>, y conviene no confundirlas. Son el <strong>límite</strong> de su actuación —lo que usted no puede hacer al recolectar prueba— y son también el <strong>objeto</strong> de algunas investigaciones que usted apoya —lo que se investiga—. La prueba escrita juega con las dos: unas preguntas lo ponen como quien podría vulnerar un derecho, otras como quien documenta su vulneración por un tercero.</p>
  </div>

  <h3>El artículo 12 y la prohibición que no admite excepciones</h3>
  <p>Hay un artículo de la Constitución que cualquier persona que obtenga prueba debe tener grabado. El <strong>artículo 12</strong> dispone que <mark>nadie será sometido a desaparición forzada, a torturas ni a tratos o penas crueles, inhumanos o degradantes</mark>. Fíjese en lo que no dice: no dice «salvo en casos graves», ni «salvo cuando la información sea decisiva», ni «salvo con autorización judicial». Es una <strong>prohibición absoluta</strong>, de las poquísimas que el ordenamiento establece sin excepción posible, y que el bloque de constitucionalidad refuerza con la Convención contra la Tortura y otros instrumentos ratificados.</p>
  <h4>Qué significa «absoluta» en la práctica de una diligencia</h4>
  <p>Significa que no existe el cálculo. No hay un escenario —por urgente, por grave, por decisivo que sea el dato— en el que someter a una persona a trato cruel, inhumano o degradante para obtener información sea admisible. Y conviene saber que la prohibición no se limita a la violencia física evidente: cubre también formas de presión que degradan a la persona. Algunas aparecen en casos reales y en preguntas de examen:</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Conducta en una diligencia</th><th>Por qué está prohibida</th></tr></thead>
      <tbody>
        <tr><td>Prolongar deliberadamente una diligencia para «quebrar» a quien la soporta</td><td>Usa el agotamiento como instrumento de presión: es trato degradante, no técnica.</td></tr>
        <tr><td>Negar agua, alimento, uso de servicios sanitarios o atención médica durante una actuación</td><td>Degrada a la persona y la pone en una condición de sometimiento ajena a cualquier fin probatorio legítimo.</td></tr>
        <tr><td>Exponer a una persona ante terceros de modo humillante, o registrar su cuerpo sin necesidad ni título</td><td>Afecta la dignidad y la intimidad, y ninguna necesidad probatoria lo justifica por sí sola.</td></tr>
        <tr><td>Amenazar con consecuencias para obtener una manifestación</td><td>Vicia la voluntad: lo obtenido así es, además, inexistente como prueba.</td></tr>
      </tbody>
    </table>
  </div>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Cuando una pregunta presenta un dato decisivo que solo se obtendría presionando a alguien, no hay ponderación que hacer: <strong>la prohibición es absoluta</strong>. Las opciones que proponen «una presión mínima y proporcionada», «insistir hasta que colabore» o «advertirle las consecuencias de no hablar» son todas incorrectas, por moderadas que suenen.</p></div>
  <div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Una diligencia se extiende y la persona que debe estar presente manifiesta que se siente mal y necesita atención. El servidor del despacho le dice que falta poco y que «si paramos ahora perdemos el día».</p>
    <p><strong>Cómo proceder.</strong> Se atiende la situación de la persona y se deja constancia de lo manifestado, de la hora y de la medida adoptada. Perder una jornada no es comparable con lo que se arriesga: una diligencia practicada mientras se desatiende la condición de quien la soporta queda expuesta a discusión por trato degradante, y con ella todo lo recaudado.</p>
  </div>
  <div class="checkpoint" data-cp="21">
    <div class="cp-q">✋ Punto de control: el dato que falta solo se obtendría presionando al investigado. ¿Qué pondera usted?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">La gravedad de los hechos frente a la intensidad de la presión que sería necesaria.</button>
    <button class="cp-opt" data-ans="1">Nada: el art. 12 establece una prohibición absoluta, sin excepciones y sin ponderación posible.</button>
    <button class="cp-opt" data-ans="0">La utilidad probatoria del dato frente al riesgo de que la prueba sea excluida después.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  <h3>DDHH y DIH: dos marcos que no son lo mismo</h3>
  <p>Es la distinción que más se confunde y la que más preguntas genera. Los dos protegen a las personas, los dos integran el bloque de constitucionalidad y los dos pueden aparecer en una misma investigación. Pero no son el mismo cuerpo normativo, no se aplican en las mismas circunstancias y no se infringen de la misma manera.</p>
  <div class="tabla-wrap">
    <table>
      <caption>Derechos Humanos frente a Derecho Internacional Humanitario</caption>
      <thead><tr><th></th><th>Derechos Humanos</th><th>Derecho Internacional Humanitario</th></tr></thead>
      <tbody>
        <tr><td><strong>Cuándo se aplica</strong></td><td>Siempre, en todo tiempo y lugar.</td><td>En situaciones de conflicto armado, internacional o no internacional.</td></tr>
        <tr><td><strong>A quién obliga</strong></td><td>Principalmente al Estado, que debe respetarlos y garantizarlos.</td><td>A <strong>todas</strong> las partes en el conflicto, estatales y no estatales.</td></tr>
        <tr><td><strong>Qué busca</strong></td><td>Proteger a la persona frente al poder: dignidad, vida, libertad, integridad, debido proceso.</td><td>Limitar los efectos del conflicto: proteger a quien no participa en las hostilidades y restringir medios y métodos.</td></tr>
        <tr><td><strong>Fuentes principales</strong></td><td>Instrumentos internacionales ratificados y la propia Constitución.</td><td>Los cuatro Convenios de Ginebra de 1949 y sus Protocolos adicionales.</td></tr>
        <tr><td><strong>Cómo se llama la conducta</strong></td><td><strong>Violación</strong> de derechos humanos.</td><td><strong>Infracción</strong> al DIH.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>Los principios del DIH que hay que saber nombrar</h4>
  <ul class="lista">
    <li><strong>Distinción.</strong> Debe distinguirse en todo momento entre quienes participan en las hostilidades y quienes no, y entre bienes civiles y objetivos militares. Es el principio matriz: de él se derivan los demás.</li>
    <li><strong>Proporcionalidad.</strong> Está prohibido el ataque del que quepa prever que causará daños a personas o bienes civiles excesivos en relación con la ventaja militar concreta esperada.</li>
    <li><strong>Precaución.</strong> Deben adoptarse todas las medidas posibles para evitar o reducir al mínimo los daños a la población y a los bienes civiles.</li>
    <li><strong>Limitación.</strong> No todo medio ni todo método de guerra es admisible: hay armas y formas de combate prohibidas.</li>
    <li><strong>Humanidad.</strong> Quien está fuera de combate o en poder de una parte debe ser tratado con humanidad, sin distinciones desfavorables.</li>
  </ul>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Dos trampas habituales. La primera: afirmar que <strong>el DIH reemplaza a los derechos humanos</strong> durante un conflicto; no lo hace, ambos se aplican. La segunda: hablar de «violación del DIH» o de «infracción a los derechos humanos» intercambiando los términos. En rigor, los derechos humanos se <strong>violan</strong> y el DIH se <strong>infringe</strong>, y una opción que invierte las palabras es, con frecuencia, la señal de que está mal.</p></div>

  '''

NUEVO_B = '''<h3>El control de convencionalidad y qué significa para ti</h3>
  <p>Del bloque de constitucionalidad se sigue una consecuencia práctica que conviene entender bien, porque suena más complicada de lo que es. El <strong>control de convencionalidad</strong> es el deber de las autoridades de un Estado de aplicar las normas internas <strong>de manera compatible</strong> con los tratados de derechos humanos ratificados y con la interpretación que de ellos han hecho los órganos competentes. Dicho sin tecnicismos: una norma interna no se aplica como si los tratados no existieran.</p>
  <h4>Para un técnico investigador, en qué se traduce</h4>
  <p>No en declarar la inaplicación de nada —eso no es su competencia— sino en una conducta mucho más modesta y muy útil: <strong>advertir cuando el procedimiento que se le pide aplicar choca con una garantía</strong>. Si un protocolo interno, una instrucción o una práctica consolidada de la dependencia conducen a una actuación que vulnera un derecho reconocido en el bloque, la respuesta no es cumplir y callar, ni desobedecer, sino la de siempre en este curso: aplicar lo que sí es compatible, <strong>advertir por escrito</strong> la tensión y dejar constancia para que quien tiene la competencia resuelva.</p>
  <div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Un procedimiento interno de una dependencia prevé que, en diligencias urgentes, se examinen dispositivos personales sin la autorización que la ley exige, «porque el protocolo lo autoriza». El protocolo existe y está firmado.</p>
    <p><strong>Cómo proceder.</strong> Un protocolo interno no puede habilitar lo que la Constitución reserva a autoridad judicial (arts. 15 y 28). Se practica lo que sí es compatible, se advierte por escrito la tensión entre el protocolo y la garantía, y se pide instrucción expresa. Cumplir el protocolo al pie de la letra produciría material inexistente y expondría la actuación completa.</p>
  </div>

  <h3>Conductas que la PGN investiga y que son violaciones de DDHH</h3>
  <p>La otra dirección del tema: no el límite de su actuación, sino su objeto. Hay hechos disciplinarios que son, al mismo tiempo, violaciones graves de derechos humanos, y cuando usted apoya técnicamente una investigación de esa naturaleza hay particularidades que conviene conocer.</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Conducta</th><th>Qué la caracteriza</th><th>Qué exige del apoyo técnico</th></tr></thead>
      <tbody>
        <tr><td><strong>Desaparición forzada</strong></td><td>Privación de la libertad seguida de ocultamiento y negativa a reconocerla o a informar el paradero.</td><td>Documentación rigurosa de registros, tiempos y cadena de responsabilidad; cualquier vacío documental es relevante en sí mismo.</td></tr>
        <tr><td><strong>Tortura y tratos crueles</strong></td><td>Infligir dolor o sufrimiento grave, físico o mental, con un fin determinado.</td><td>Documentación del estado de las personas, de las condiciones y de los tiempos, con especial cuidado en el trato a la víctima durante la diligencia.</td></tr>
        <tr><td><strong>Ejecución extrajudicial</strong></td><td>Privación de la vida por agentes del Estado fuera de los supuestos legalmente admisibles.</td><td>Preservación del lugar y de los elementos, y precisión extrema en la secuencia temporal de lo documentado.</td></tr>
        <tr><td><strong>Violencia sexual</strong></td><td>Conductas de contenido sexual ejercidas sin consentimiento, agravadas cuando median poder o custodia.</td><td>Trato que evite la revictimización, reserva reforzada y documentación que no exija a la víctima repetir su relato ante quien no debe recibirlo.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>Dos reglas específicas cuando hay víctimas en la actuación</h4>
  <ul class="lista">
    <li><strong>No revictimizar.</strong> La víctima no debe repetir su relato una y otra vez ante quien no tiene competencia para recibirlo. Si durante una diligencia una víctima quiere contar lo ocurrido, la conducta es la misma del día anterior —no preguntar, consignar lo manifestado, informar la vía— pero con un cuidado adicional: evitar que la constancia la obligue a detallar lo que corresponde a otra actuación.</li>
    <li><strong>Reserva reforzada.</strong> La identidad y los datos de las víctimas, y con mayor razón los de menores de edad, exigen el máximo cuidado. A la reserva de la actuación se suma la protección de datos del art. 15: un informe técnico no necesita, casi nunca, el nombre completo de una víctima para describir un hallazgo.</li>
  </ul>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>En los casos con víctimas, las opciones correctas suelen ser las que <strong>evitan que la persona tenga que repetir su relato</strong> y las que <strong>protegen su identidad</strong>, incluso cuando otra opción parece más completa o más diligente. «Pedirle que precise los hechos para dejarlo claro en el acta» suena riguroso y es revictimizar.</p></div>

  <h3>Cómo se ve este bloque en la prueba: cinco patrones</h3>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Si el caso dice…</th><th>El patrón es…</th><th>La respuesta correcta…</th></tr></thead>
      <tbody>
        <tr><td>«El dato es decisivo y solo se obtiene presionando»</td><td>Prohibición absoluta (art. 12)</td><td>No pondera: no se presiona, en ningún grado y por ningún motivo.</td></tr>
        <tr><td>«Hay conflicto armado, así que aplica el DIH y no los DDHH»</td><td>Complementariedad</td><td>Los dos marcos se aplican; el DIH no desplaza a los derechos humanos.</td></tr>
        <tr><td>«El protocolo interno lo autoriza»</td><td>Control de convencionalidad</td><td>Aplica lo compatible, advierte por escrito la tensión y pide instrucción.</td></tr>
        <tr><td>«La víctima quiere contar lo que pasó»</td><td>No revictimizar</td><td>No la interroga, consigna lo manifestado sin exigirle detalles e informa la vía.</td></tr>
        <tr><td>«El informe necesita identificar a la víctima»</td><td>Reserva reforzada</td><td>Describe el hallazgo sin datos personales innecesarios; la identificación va por donde corresponde.</td></tr>
      </tbody>
    </table>
  </div>
  <div class="box ok">
    <div class="box-title">🧠 Frase para recordar</div>
    <p>«Los derechos humanos son el límite de lo que puedo hacer y, a veces, el objeto de lo que investigo. En la primera dirección no hay ponderación: hay prohibiciones. En la segunda no hay prisa que justifique revictimizar.»</p>
  </div>
  <div class="fuentes"><div class="fuentes-tag">📚 Fuentes oficiales para profundizar</div>
    <ul class="lista">
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=4125" target="_blank" rel="noopener">Constitución Política de Colombia — arts. 12, 15, 29, 93 y 214</a></li>
      <li><a href="https://www.icrc.org/es/doc/war-and-law/treaties-customary-law/geneva-conventions/overview-geneva-conventions.htm" target="_blank" rel="noopener">Comité Internacional de la Cruz Roja — Los Convenios de Ginebra de 1949 y sus Protocolos</a></li>
      <li><a href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=43043" target="_blank" rel="noopener">Ley 1448 de 2011 — Víctimas y Restitución de Tierras</a></li>
      <li><a href="https://funcionpublica.gov.co/eva/gestornormativo/norma.php?i=90324" target="_blank" rel="noopener">Ley 1952 de 2019 — Código General Disciplinario</a></li>
      <li><a href="https://www.procuraduria.gov.co/" target="_blank" rel="noopener">Procuraduría General de la Nación — sitio oficial</a></li>
    </ul>
  </div>

  '''

NUEVO_C = """<h3>Los Convenios de Ginebra y los Protocolos: qué protege cada uno</h3>
  <p>El DIH convencional se apoya en <strong>cuatro Convenios de Ginebra de 1949</strong> y en sus <strong>Protocolos adicionales</strong>. La prueba pregunta por el reparto, y el reparto es sencillo de retener porque sigue una lógica de a quién protege cada uno.</p>
  <div class="tabla-wrap">
    <table>
      <caption>Los cuatro Convenios de 1949</caption>
      <thead><tr><th>Convenio</th><th>A quién protege</th></tr></thead>
      <tbody>
        <tr><td><strong>I</strong></td><td>Los heridos y enfermos de las fuerzas armadas en campaña.</td></tr>
        <tr><td><strong>II</strong></td><td>Los heridos, enfermos y náufragos de las fuerzas armadas en el mar.</td></tr>
        <tr><td><strong>III</strong></td><td>Los prisioneros de guerra.</td></tr>
        <tr><td><strong>IV</strong></td><td>Las personas civiles en tiempo de guerra.</td></tr>
      </tbody>
    </table>
  </div>
  <p>Hay además una disposición que conviene conocer por su nombre: el <strong>artículo 3 común</strong> a los cuatro Convenios, que fija un mínimo humanitario aplicable a los <strong>conflictos armados no internacionales</strong>. Es la norma que, en un contexto como el colombiano, más se invoca: prohíbe los atentados contra la vida y la integridad, la toma de rehenes, los atentados contra la dignidad personal y las condenas dictadas sin las garantías judiciales indispensables, respecto de quienes no participan directamente en las hostilidades.</p>
  <h4>Los Protocolos adicionales</h4>
  <ul class="lista">
    <li><strong>Protocolo I (1977).</strong> Desarrolla la protección en los conflictos armados <strong>internacionales</strong>, con reglas detalladas sobre la conducción de hostilidades y la protección de la población civil.</li>
    <li><strong>Protocolo II (1977).</strong> Desarrolla la protección en los conflictos armados <strong>no internacionales</strong>: es el complemento del artículo 3 común y el de mayor relevancia práctica en el contexto interno.</li>
    <li><strong>Protocolo III (2005).</strong> Añade un emblema distintivo adicional al de la cruz roja y la media luna roja.</li>
  </ul>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>La confusión que más se explota: asignar el <strong>Protocolo I</strong> a los conflictos no internacionales. Es al contrario — <strong>I: internacionales; II: no internacionales</strong> —, y el artículo 3 común es el mínimo que rige en los no internacionales incluso sin el Protocolo II.</p></div>

  <h3>Personas y bienes protegidos: lo que no puede ser objetivo</h3>
  <p>El principio de distinción se concreta en categorías que el DIH protege de manera especial. Conocerlas con nombre propio es lo que permite reconocer una infracción cuando se documenta un hecho.</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Categoría</th><th>Quiénes o qué</th><th>Qué implica</th></tr></thead>
      <tbody>
        <tr><td><strong>Población civil</strong></td><td>Quien no participa directamente en las hostilidades.</td><td>No puede ser objeto de ataque, ni de actos destinados a sembrar terror. Pierde la protección solo mientras participe directamente.</td></tr>
        <tr><td><strong>Personas fuera de combate</strong></td><td>Heridos, enfermos, náufragos, quien se rinde o está en poder de una parte.</td><td>Trato humano en toda circunstancia, sin distinciones desfavorables.</td></tr>
        <tr><td><strong>Personal sanitario y religioso</strong></td><td>Quien presta asistencia médica o espiritual.</td><td>Protección y respeto; sus unidades, medios de transporte y emblemas también.</td></tr>
        <tr><td><strong>Bienes civiles</strong></td><td>Todo lo que no es objetivo militar.</td><td>No pueden ser atacados ni destruidos sin necesidad militar imperiosa.</td></tr>
        <tr><td><strong>Bienes indispensables para la supervivencia</strong></td><td>Cultivos, cosechas, ganado, instalaciones de agua potable.</td><td>Prohibido atacarlos, destruirlos o inutilizarlos para provocar hambre en la población.</td></tr>
        <tr><td><strong>Bienes culturales y lugares de culto</strong></td><td>Monumentos, obras de arte, lugares de culto.</td><td>Protección especial; no pueden usarse para fines militares.</td></tr>
        <tr><td><strong>Misión médica y bienes sanitarios</strong></td><td>Hospitales, puestos de salud, ambulancias.</td><td>Protección reforzada: atacarlos o impedir su labor es una infracción grave.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>Métodos y medios prohibidos</h4>
  <p>Del principio de limitación se sigue que no todo vale. Entre las prohibiciones que con más frecuencia aparecen en casos reales: la <strong>perfidia</strong> —simular una condición protegida para atacar—, el <strong>uso indebido de emblemas</strong> protectores, los ataques <strong>indiscriminados</strong> —los que no distinguen entre objetivos militares y bienes o personas civiles—, la <strong>toma de rehenes</strong>, el <strong>reclutamiento de menores</strong> y el empleo de armas que causan sufrimientos innecesarios o cuyos efectos no pueden limitarse.</p>
  <div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> Usted apoya técnicamente una investigación disciplinaria por hechos ocurridos durante una operación, en la que resultaron afectadas instalaciones de un puesto de salud. El despacho le pide documentar el estado de las instalaciones y de los elementos hallados.</p>
    <p><strong>Cómo proceder.</strong> Documente con precisión lo que observa: estado de la edificación, señalización y emblemas presentes o ausentes, elementos hallados, ubicación y secuencia temporal. No califique el hecho como infracción al DIH ni como ataque a la misión médica: eso es una calificación jurídica. Lo que su informe debe permitir es precisamente que quien califica tenga con qué hacerlo, y para eso la presencia o ausencia de emblemas y la condición de la instalación son datos decisivos.</p>
  </div>

  <h3>El Sistema Interamericano y por qué aparece en el temario</h3>
  <p>Colombia es parte de la <strong>Convención Americana sobre Derechos Humanos</strong>, y de ella se derivan dos órganos cuyos nombres conviene no confundir, porque la prueba los cruza.</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Órgano</th><th>Qué es</th><th>Qué produce</th></tr></thead>
      <tbody>
        <tr><td><strong>Comisión Interamericana de Derechos Humanos</strong></td><td>Órgano de la OEA que promueve y protege los derechos humanos en la región; recibe peticiones individuales.</td><td>Informes, recomendaciones, medidas cautelares. Puede llevar un caso ante la Corte.</td></tr>
        <tr><td><strong>Corte Interamericana de Derechos Humanos</strong></td><td>Tribunal con función contenciosa y consultiva respecto de los Estados que han aceptado su competencia.</td><td><strong>Sentencias</strong> vinculantes para el Estado parte en el caso, medidas provisionales y opiniones consultivas.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>Qué tiene esto que ver con una diligencia técnica</h4>
  <p>Más de lo que parece. La jurisprudencia interamericana ha fijado estándares sobre cómo deben investigarse las violaciones graves de derechos humanos, y esos estándares son exigencias <strong>sobre la investigación misma</strong>: que sea <strong>diligente</strong> (que se practiquen las pruebas que el caso requiere, sin demoras que hagan perder material), <strong>oportuna</strong> (que se actúe cuando la prueba todavía existe), <strong>imparcial</strong> (que no la conduzcan quienes pueden estar involucrados) y <strong>exhaustiva</strong> (que no se omitan líneas de indagación incómodas). Visto así, es un marco que describe, casi punto por punto, lo que hace bien o mal un técnico investigador.</p>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>No confunda los órganos: la <strong>Comisión</strong> recomienda y puede demandar; la <strong>Corte</strong> juzga y dicta sentencias. Una opción que atribuya sentencias a la Comisión, o que diga que las recomendaciones de la Comisión son sentencias, está mal.</p></div>
  <div class="checkpoint" data-cp="22">
    <div class="cp-q">✋ Punto de control: ¿qué protege el Protocolo adicional II de 1977?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">A los prisioneros de guerra en los conflictos armados internacionales.</button>
    <button class="cp-opt" data-ans="0">A la población civil en los conflictos armados internacionales, desarrollando el Convenio IV.</button>
    <button class="cp-opt" data-ans="1">Desarrolla la protección en los conflictos armados no internacionales, complementando el artículo 3 común.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  """

NUEVO_D = """<h3>Debida diligencia y enfoque diferencial: dos exigencias concretas</h3>
  <p>Cerramos con los dos conceptos que más se piden en la prueba y que más se repiten mal, porque suenan a declaración de principios y son, en realidad, exigencias verificables sobre el trabajo.</p>
  <h4>Debida diligencia: cuatro requisitos, no una actitud</h4>
  <p>Cuando se habla de investigar con <strong>debida diligencia</strong> no se está pidiendo buena voluntad: se están exigiendo cuatro cosas comprobables, y las cuatro se traducen en conducta del técnico.</p>
  <div class="tabla-wrap">
    <table>
      <thead><tr><th>Requisito</th><th>Qué exige</th><th>Cómo lo cumple o lo incumple un técnico</th></tr></thead>
      <tbody>
        <tr><td><strong>Oficiosidad</strong></td><td>Que la investigación se impulse sin esperar que la víctima la empuje.</td><td>Lo cumple advirtiendo por escrito, a tiempo, lo que falta o lo que está por perderse. Lo incumple esperando instrucciones cuando la prueba se desvanece.</td></tr>
        <tr><td><strong>Oportunidad</strong></td><td>Que se actúe cuando la prueba todavía existe.</td><td>Lo cumple documentando el estado inicial antes de manipular y avisando cuando el término no alcanzará. Lo incumple postergando el aviso al día del vencimiento.</td></tr>
        <tr><td><strong>Exhaustividad</strong></td><td>Que no se omitan líneas de indagación, incluidas las incómodas.</td><td>Lo cumple consignando el hallazgo que contradice la hipótesis con el mismo rigor que el que la confirma. Lo incumple describiendo uno en dos páginas y el otro en una línea.</td></tr>
        <tr><td><strong>Imparcialidad</strong></td><td>Que no intervenga quien puede estar comprometido con los hechos.</td><td>Lo cumple manifestando por escrito un vínculo antes de actuar. Lo incumple confiando en que podrá ser imparcial y guardándose el dato.</td></tr>
      </tbody>
    </table>
  </div>
  <p>Observe que los cuatro requisitos reproducen, con otro nombre, exigencias que ya vio en las guías de Objetividad, de régimen probatorio y de procedimiento. No es casualidad: la debida diligencia es el nombre que el derecho internacional le da a lo que el buen oficio técnico hace de todas formas. Saberlo con ese nombre es lo que le permite reconocerlo en una pregunta.</p>
  <h4>Enfoque diferencial: tratar distinto a quien está en situación distinta</h4>
  <p>El <strong>enfoque diferencial</strong> parte de una idea sencilla: la igualdad formal no basta cuando las personas llegan a la actuación en condiciones desiguales. Aplicarlo no es dar un trato privilegiado: es <strong>remover las barreras</strong> que impedirían a alguien participar en igualdad de condiciones. En una diligencia se concreta en cosas muy materiales:</p>
  <ul class="lista">
    <li><strong>Niños, niñas y adolescentes.</strong> Prevalencia de sus derechos, reserva reforzada de su identidad y la regla de no exponerlos a repetir relatos. Un informe técnico casi nunca necesita el nombre de un menor para describir un hallazgo.</li>
    <li><strong>Personas con discapacidad.</strong> Accesibilidad física al lugar de la diligencia, apoyos para la comunicación cuando se requieran, y tiempos que no conviertan la participación en una carga.</li>
    <li><strong>Comunidades étnicas.</strong> Reconocimiento de sus autoridades propias y de su lengua; cuando la actuación toca sus territorios o sus formas de vida, existen garantías específicas, como la consulta previa en los casos que corresponde.</li>
    <li><strong>Víctimas de violencia sexual.</strong> Trato que evite la revictimización, reserva estricta y la regla de que la víctima no repita su relato ante quien no tiene competencia para recibirlo.</li>
    <li><strong>Personas mayores.</strong> Condiciones de la diligencia que atiendan su estado de salud y su autonomía, sin presumir incapacidad.</li>
  </ul>
  <div class="practica"><div class="practica-tag">🧩 En la práctica</div>
    <p><strong>Situación.</strong> En una diligencia debe estar presente una persona con discapacidad auditiva. Nadie previó apoyo para la comunicación y el despacho propone «seguir adelante y dejarlo anotado», porque el término apremia.</p>
    <p><strong>Cómo proceder.</strong> Deje constancia de la circunstancia y de la ausencia del apoyo, informe por el canal antes de continuar y pida instrucción expresa. Practicar la diligencia en condiciones que impiden a la persona comprender y pronunciarse no «se arregla» con una anotación: es precisamente lo que después hará discutible todo lo actuado.</p>
  </div>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>El distractor típico del enfoque diferencial es la opción que <strong>deja constancia de la barrera y continúa igual</strong>. Suena correcta porque documenta, y es incorrecta porque la constancia no remueve la barrera. Cuando la condición de la persona impide su participación efectiva, lo que corresponde es informar y pedir instrucción <strong>antes</strong> de continuar, no después.</p></div>

  """

SEC[2] = SEC[2].rstrip() + '\n\n  ' + NUEVO_A + '\n\n  ' + FP_DDHH + '\n\n  ' + NUEVO_C + '\n\n  ' + FP_REG + '\n\n  ' + NUEVO_D + '\n\n  ' + NUEVO_B + '\n'

SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>', '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>', '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('Profesional Universitario 3PU-15', 'Técnico Investigador 4TI-15'),
    ('Profesional Universitario', 'Técnico Investigador'),
    ('(3PU-15)', '(4TI-15)'), ('3PU-15', '4TI-15'), ('3PU15C', '4TI15O'), ('3PU', '4TI'),
    ('146-2026', '257-2026'), ('112-2026', '257-2026'), ('89-2026', '257-2026'),
    ('El instructor', 'El servidor que instruye'), ('el instructor', 'el servidor que instruye'),
    ('instructor', 'servidor que instruye'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre Derechos '
              'Humanos y Derecho Internacional Humanitario aplicados a la actividad investigativa: bloque de '
              'constitucionalidad, la prohibición absoluta del art. 12, la distinción entre DDHH y DIH y sus '
              'principios, control de convencionalidad, trato a las víctimas y reserva reforzada.')

P = [
 (1,
  'Usted practica una prueba técnica en una investigación disciplinaria por hechos graves. Falta un dato que resolvería el caso y el único que lo tiene es el investigado, que se niega a hablar. El servidor del despacho le sugiere «dejarlo esperando un buen rato en la diligencia, sin agua, a ver si se le suelta la lengua», y le aclara que no se trata de hacerle nada, solo de incomodarlo. La diligencia lleva tres horas y usted tiene el acta abierta.',
  '¿Qué debe ponderar usted?',
  ['La gravedad de los hechos investigados frente a la intensidad de la incomodidad que se generaría, aplicando un criterio de proporcionalidad entre el fin y el medio.',
   'Nada: el artículo 12 de la Constitución establece una prohibición absoluta de tratos crueles, inhumanos o degradantes, sin excepciones y sin ponderación posible.',
   'La utilidad probatoria del dato frente al riesgo de que la prueba sea posteriormente excluida, optando por la alternativa que mejor preserve la actuación.',
   'La voluntariedad de la permanencia del investigado en la diligencia, ya que si puede retirarse cuando quiera no habría propiamente un trato degradante.'],
  'El art. 12 no admite ponderación: no dice «salvo en casos graves» ni «salvo cuando el dato sea decisivo». Usar el agotamiento o la privación de necesidades básicas como instrumento de presión es trato degradante, cualquiera que sea la gravedad del caso.',
  'Las tres opciones restantes proponen un cálculo —proporcionalidad, utilidad, voluntariedad— y el punto es precisamente que aquí no hay cálculo que hacer.'),

 (3,
  'Un compañero sostiene en una capacitación que, cuando hay conflicto armado, «aplica el DIH y los derechos humanos quedan suspendidos». Otro responde que el DIH no existe en Colombia porque no hay guerra declarada. El jefe pide la precisión porque el punto va en un documento interno y varios del grupo presentan la prueba la próxima semana. El documento sale firmado por el jefe de la Dirección y la discusión lleva media hora sin resolverse.',
  '¿Cuál es la precisión correcta?',
  ['El DIH desplaza a los derechos humanos durante el conflicto armado, porque es el régimen especial aplicable a esas situaciones y los dos no pueden regir a la vez.',
   'El DIH solo se aplica en conflictos armados internacionales con declaración formal de guerra, de modo que en el contexto colombiano no tiene aplicación práctica alguna.',
   'Los derechos humanos se suspenden parcialmente durante el conflicto y el DIH cubre lo que queda fuera, repartiéndose así el ámbito de protección entre ambos marcos.',
   'Los dos marcos se aplican: los derechos humanos rigen en todo tiempo y el DIH se añade en situaciones de conflicto armado, incluidos los no internacionales.'],
  'Los dos marcos son complementarios, no excluyentes: los derechos humanos rigen siempre y el DIH se añade en conflicto armado, que puede ser internacional o no internacional —de hecho el artículo 3 común y el Protocolo II están pensados para los segundos—.',
  'Ni el DIH desplaza o suspende los derechos humanos, ni requiere declaración formal de guerra: el artículo 3 común se aplica precisamente a los conflictos armados no internacionales.'),

 (2,
  'Un protocolo interno de una dependencia prevé que, en diligencias urgentes, se examinen los dispositivos personales de los servidores sin la autorización que la ley exige, «porque el protocolo lo autoriza». El protocolo existe, está firmado por el jefe de la dependencia y lleva dos años aplicándose sin que nadie lo cuestione. Le piden practicar una diligencia así mañana. Usted revisó el protocolo y confirmó que no tiene nota de suspensión ni excepción alguna registrada.',
  '¿Cuál es la actuación correcta?',
  ['Aplicar el protocolo, que es la norma interna vigente de la dependencia y goza de presunción de legalidad mientras no sea anulado por autoridad competente.',
   'Negarse a practicar la diligencia y abstenerse de cualquier gestión, porque aplicar un protocolo contrario a la Constitución lo comprometería personalmente.',
   'Practicar lo que sí es compatible con las garantías, advertir por escrito la tensión entre el protocolo y los arts. 15 y 28, y pedir instrucción expresa al competente.',
   'Aplicar el protocolo dejando constancia en el acta de que el examen se practicó sin autorización judicial, para que el competente valore después su validez.'],
  'Es el control de convencionalidad en su versión práctica: un protocolo interno no puede habilitar lo que la Constitución reserva a autoridad judicial. Se aplica lo compatible, se advierte por escrito la tensión y se pide instrucción.',
  'Aplicarlo produce material inexistente, con o sin constancia; y negarse sin encauzar abandona una actuación que podía adelantarse en lo compatible.'),

 (0,
  'En una diligencia, una víctima de violencia sexual presente en el lugar le dice que quiere contarle lo que le ocurrió. Nadie del despacho está allí. Su delegación se refiere al examen de unos documentos. Ella insiste en que ya lo ha contado varias veces y que quiere que quede claro. La diligencia está en curso, hay otras personas en el lugar y el acta sigue abierta sobre la mesa. Es su primera diligencia con una víctima presente y nadie del despacho llega hasta mañana.',
  '¿Cuál es la actuación correcta?',
  ['No formularle preguntas ni pedirle detalles, consignar que manifestó querer rendir su versión, informarle ante quién puede hacerlo, y poner el hecho en conocimiento del competente.',
   'Recibirle el relato completo y detallado y anexarlo al informe, para que no tenga que repetirlo una vez más ante otra autoridad dentro de la misma actuación.',
   'Escucharla sin dejar constancia alguna, dado que recibir versiones excede su delegación y registrar lo dicho podría exponer su identidad en el expediente.',
   'Pedirle que precise los hechos esenciales para dejarlos claros en el acta, limitándose a lo indispensable y evitando entrar en detalles innecesarios del relato.'],
  'Dos reglas se cruzan: no recibir lo que no está delegado y no revictimizar. La conducta correcta consigna que manifestó querer rendir versión, informa la vía y pone en conocimiento, sin pedirle que repita ni detalle su relato.',
  'Recibir el relato completo es actuar fuera de la delegación; «pedirle que precise lo esencial» suena riguroso y es revictimizar; y escucharla sin constancia borra un hecho que el competente debe conocer.'),

 (1,
  'Usted apoya técnicamente una investigación por hechos ocurridos durante una operación en la que resultaron afectadas las instalaciones de un puesto de salud. El despacho le pide documentar el estado de las instalaciones y los elementos hallados, y le pregunta si «hubo un ataque a la misión médica». Usted puede describir la edificación, la señalización y los elementos encontrados. El informe debe rendirse esta semana y usted conserva el registro fotográfico completo de la edificación.',
  '¿Cómo debe redactar el informe?',
  ['Consignando que hubo un ataque a la misión médica, ya que la afectación de un puesto de salud configura objetivamente una infracción al DIH plenamente verificable.',
   'Describiendo el estado de la edificación, la presencia o ausencia de emblemas y señalización, los elementos hallados y la secuencia temporal, sin calificar el hecho.',
   'Describiendo el estado de la edificación y omitiendo lo relativo a emblemas y señalización, por tratarse de elementos cuya valoración es estrictamente jurídica.',
   'Consignando que los hechos «podrían configurar» una infracción al DIH, de modo que el despacho disponga de la calificación como hipótesis técnica de trabajo.'],
  'La presencia o ausencia de emblemas y la condición de la instalación son precisamente los datos decisivos para que quien califica pueda hacerlo. Describirlos es su aporte; calificar el hecho como infracción al DIH, no.',
  'Calificar —con o sin un «podrían»— invade competencia ajena. Y omitir los emblemas suprime el dato técnico más relevante del hallazgo.'),

 (3,
  'Un compañero afirma que la Comisión Interamericana de Derechos Humanos «dicta sentencias contra el Estado» y que la Corte Interamericana «solo emite recomendaciones». El jefe pide la precisión porque el punto aparece en el temario y varios lo tienen confundido. Varios del grupo presentan la prueba la próxima semana y el tema figura en el temario de conocimientos específicos. Dos integrantes del grupo ya escribieron la distinción al revés en el último simulacro.',
  '¿Cuál es la precisión correcta?',
  ['Su compañero tiene razón: la Comisión dicta sentencias vinculantes y la Corte emite recomendaciones de carácter orientador para los Estados parte del sistema.',
   'Ambos órganos dictan sentencias, con la diferencia de que las de la Comisión se refieren a peticiones individuales y las de la Corte a casos de alcance general.',
   'Ninguno de los dos produce decisiones vinculantes: el sistema interamericano opera exclusivamente mediante informes y recomendaciones de carácter político.',
   'Está invertido: la Comisión produce informes, recomendaciones y medidas cautelares, y puede llevar casos ante la Corte; la Corte dicta sentencias vinculantes.'],
  'La Comisión promueve, recibe peticiones, emite informes y recomendaciones y puede llevar un caso ante la Corte. La Corte es el tribunal: dicta sentencias vinculantes para el Estado parte en el caso.',
  'La atribución está exactamente invertida en la primera opción, y el sistema sí produce decisiones vinculantes: las sentencias de la Corte.'),

 (2,
  'En una diligencia debe estar presente una persona con discapacidad auditiva y nadie previó apoyo para la comunicación. El despacho propone «seguir adelante y dejarlo anotado en el acta», porque el término apremia y reprogramar costaría una semana. La persona asiente a todo sin que sea claro que comprende lo que se le explica. La persona asiente a todo sin que sea claro que comprende, y reprogramar costaría una semana completa.',
  '¿Cuál es la actuación correcta?',
  ['Continuar la diligencia dejando constancia detallada de la ausencia del apoyo, de modo que el competente pueda valorar después esa circunstancia al decidir el fondo.',
   'Continuar y, al final, leer el acta despacio y pedirle que la firme, para asegurar que conoció su contenido antes de cerrar formalmente la actuación practicada.',
   'Dejar constancia de la circunstancia y de la ausencia del apoyo, informarlo por el canal antes de continuar y pedir instrucción expresa al servidor competente.',
   'Suspender la diligencia por su propia decisión y devolver la delegación al despacho, para que reprograme la actuación cuando el apoyo pueda ser garantizado.'],
  'El enfoque diferencial exige remover la barrera, no documentarla y seguir. Cuando la condición de la persona impide su participación efectiva, lo que corresponde es informar y pedir instrucción antes de continuar.',
  'Documentar la barrera y continuar es el distractor típico: la constancia no remueve el obstáculo. Y suspender por decisión propia excede su rol cuando bastaba consultar.'),

 (0,
  'Usted debe rendir un informe técnico sobre hallazgos en un caso en el que hay una víctima menor de edad. El formato del informe tiene un campo de identificación de las personas relacionadas y el despacho le pide llenarlo completo, con nombre y documento de la menor. El hallazgo que usted documentó no depende de su identidad. El formato es el institucional vigente y el despacho insiste en que se llene completo antes de remitirlo.',
  '¿Cuál es la actuación correcta?',
  ['Describir el hallazgo sin incorporar datos personales innecesarios de la menor, y advertir por escrito que la identificación debe tramitarse por donde corresponde.',
   'Llenar el campo completo conforme al formato institucional, que es un parámetro de trabajo vigente y de obligatorio cumplimiento en todos los informes de la Dirección.',
   'Llenar el campo con las iniciales de la menor y su número de documento, de modo que el formato quede completo sin revelar el nombre en el cuerpo del informe.',
   'Llenar el campo completo y solicitar que el informe se tramite con reserva especial, de modo que la identificación exista pero el acceso al documento quede restringido.'],
  'La prevalencia de los derechos del menor y la protección de datos del art. 15 exigen el máximo cuidado: si el hallazgo no depende de la identidad, el informe no la necesita. El formato es un parámetro, no una autorización para tratar datos innecesarios.',
  'Un número de documento identifica igual que un nombre; y pedir reserva especial no justifica incorporar un dato que la descripción técnica no requería.'),

 (1,
  'Un compañero sostiene que investigar «con debida diligencia» es una expresión sin contenido concreto, «una forma elegante de decir que hay que hacer bien el trabajo». El jefe quiere que el grupo entienda que no es así, porque el concepto aparece en el temario y tiene consecuencias verificables. El concepto aparece en el temario de la convocatoria y el jefe quiere dejarlo explicado por escrito. La expresión aparece también en los estándares que el despacho cita en sus autos.',
  '¿Qué exige, en concreto, la debida diligencia?',
  ['Exige actuar de buena fe y con el mayor cuidado posible dentro de los recursos disponibles, sin que de ello se deriven obligaciones específicas verificables.',
   'Exige cuatro cosas comprobables: oficiosidad, oportunidad, exhaustividad e imparcialidad, cada una con conductas concretas que pueden cumplirse o incumplirse.',
   'Exige agotar todos los medios de prueba posibles en toda investigación, sin importar su pertinencia, para que no pueda reprocharse ninguna omisión al Estado.',
   'Exige que la investigación la conduzca personal con formación jurídica especializada, condición sin la cual la actuación no satisface el estándar internacional.'],
  'La debida diligencia se descompone en cuatro requisitos verificables, y los cuatro se traducen en conducta del técnico: impulsar sin esperar, actuar cuando la prueba existe, no omitir lo incómodo y apartarse cuando hay un vínculo.',
  'Ni es una actitud sin contenido, ni obliga a agotar pruebas impertinentes —el art. 151 manda negarlas—, ni depende de la formación jurídica de quien investiga.'),

 (3,
  'Durante una diligencia en territorio de una comunidad étnica, sus autoridades propias le manifiestan que la actuación debió consultarse con ellas y le piden que se suspenda. Usted tiene delegación escrita para practicar la prueba y no tiene instrucción alguna sobre el punto. La comunidad no impide físicamente el acceso. Usted llegó con la delegación en mano y la diligencia estaba programada para esta mañana. Las autoridades propias llegaron acompañadas de varios miembros de la comunidad.',
  '¿Cuál es la actuación correcta?',
  ['Continuar con la diligencia amparado en la delegación escrita, dejando constancia de la manifestación de las autoridades propias para que el competente la valore después.',
   'Suspender definitivamente la actuación y archivar la delegación, porque sin consulta previa cualquier diligencia en territorio de comunidades étnicas carece de validez.',
   'Consultar a las autoridades propias el alcance de la diligencia y practicar únicamente aquello en lo que ellas manifiesten su conformidad durante la actuación.',
   'Dejar constancia detallada de la manifestación y de la identidad de las autoridades, informar de inmediato por el canal y pedir instrucción expresa antes de continuar.'],
  'El reconocimiento de las autoridades propias y las garantías específicas de las comunidades étnicas no las resuelve el técnico en el lugar. Se documenta la manifestación, se informa de inmediato y se pide instrucción antes de continuar.',
  'Continuar sin consultar desatiende una garantía que puede ser aplicable; archivar la delegación decide de fondo; y negociar el alcance con la comunidad traslada a un acuerdo informal lo que debe resolver el competente.'),

 (2,
  'Un compañero afirma que el artículo 3 común a los Convenios de Ginebra «solo se aplica si el Estado reconoce que hay conflicto armado». Otro dice que se aplica siempre, incluso en disturbios internos. El jefe pide la precisión porque el punto aparece en el temario y genera confusión. El punto genera confusión en el grupo desde la capacitación anterior y el documento sale esta semana. El punto es el que más se falla en los simulacros del grupo, según el registro del jefe.',
  '¿Cuál es la precisión correcta?',
  ['Se aplica únicamente cuando el Estado reconoce formalmente la existencia de un conflicto armado en su territorio mediante una declaración con efectos jurídicos.',
   'Se aplica en toda circunstancia, incluidos los disturbios internos y las tensiones internas, por tratarse de un mínimo humanitario de alcance universal.',
   'Se aplica en los conflictos armados no internacionales, y su aplicación depende de la situación de hecho y no del reconocimiento formal del conflicto por parte del Estado.',
   'Se aplica solo a las partes estatales del conflicto, ya que los grupos armados no estatales no son signatarios de los Convenios y no quedan obligados por ellos.'],
  'El artículo 3 común es el mínimo humanitario de los conflictos armados no internacionales, y su aplicación depende de la situación de hecho, no de que el Estado la reconozca. Obliga, además, a todas las partes.',
  'Ni depende del reconocimiento estatal, ni cubre los disturbios y tensiones internas —que no son conflicto armado—, ni obliga solo al Estado: el DIH vincula a todas las partes.'),

 (0,
  'El despacho le solicita practicar una prueba técnica en una investigación por hechos atribuidos a miembros de la Fuerza Pública. Un compañero afirma que la PGN no tiene competencia, «porque ellos tienen su propio régimen disciplinario y su propia justicia». El jefe pide la precisión para motivar la actuación. La investigación ya está abierta y el despacho espera el apoyo técnico para la próxima semana. El compañero lo repite con seguridad y dos del grupo le dan la razón en la reunión.',
  '¿Cuál es la precisión correcta?',
  ['Los miembros de la Fuerza Pública tienen regímenes disciplinarios propios, pero la PGN conserva su poder preferente, de modo que puede asumir y el apoyo técnico procede.',
   'La PGN carece de competencia frente a la Fuerza Pública: sus regímenes especiales excluyen la intervención del órgano de control externo en materia disciplinaria.',
   'La PGN solo puede intervenir cuando la justicia penal militar se declara incompetente, momento en el cual el expediente se traslada al órgano de control externo.',
   'La PGN puede intervenir únicamente en casos de violaciones de derechos humanos, y en las demás conductas la competencia es exclusiva de los regímenes especiales.'],
  'Los regímenes disciplinarios especiales de la Fuerza Pública no excluyen el poder preferente de la PGN: por eso el apoyo técnico de la DNIE procede en esas investigaciones.',
  'Ni la competencia está excluida, ni depende de que la justicia penal militar se aparte, ni se limita a los casos de violaciones de derechos humanos.'),

 (3,
  'Usted documenta que en una actuación anterior no se practicó una prueba que el caso requería y que, por el tiempo transcurrido, el material ya no existe. El caso es de hechos graves y el despacho le pide concepto técnico sobre lo que todavía se puede hacer. Un compañero sugiere no mencionar la prueba perdida «porque ya no hay remedio y solo expone a la entidad». El caso es de hechos graves, la actuación anterior fue de hace dos años y usted conserva el expediente completo.',
  '¿Qué corresponde hacer?',
  ['Limitarse a conceptuar sobre lo que aún es posible practicar, sin referirse a la prueba perdida, porque señalar una omisión pasada excede el objeto de la consulta.',
   'Conceptuar sobre lo posible y mencionar la prueba perdida en términos generales, sin precisar cuál era ni cuándo debió practicarse, para no atribuir responsabilidades.',
   'Conceptuar sobre lo posible y, además, señalar quién debió practicar la prueba en su momento, de modo que la omisión quede plenamente identificada en el expediente.',
   'Conceptuar sobre lo que aún es posible y consignar con precisión qué prueba no se practicó, cuándo debió practicarse y por qué ya no es posible, informándolo al competente.'],
  'La oportunidad es uno de los cuatro requisitos de la debida diligencia, y una omisión que hizo perder prueba es información que el competente debe tener. Se documenta con precisión el hecho —qué, cuándo, por qué ya no es posible— sin atribuir responsabilidades.',
  'Omitir o generalizar la pérdida oculta un hecho relevante; y señalar quién debió practicarla es atribuir una conducta, que es valoración del competente.'),

 (1,
  'Un compañero sostiene que las sentencias de la Corte Interamericana «no obligan a Colombia porque son de un tribunal extranjero». El jefe pide la precisión porque el punto está en el temario y el documento sale esta semana a otra dependencia. El documento sale esta semana a otra dependencia y el jefe quiere la cita exacta del instrumento. Un integrante del grupo lo repitió en la última sesión de estudio y nadie lo corrigió.',
  '¿Cuál es la precisión correcta?',
  ['Tiene razón: se trata de un tribunal internacional cuyas decisiones tienen valor orientador, pero no obligan a las autoridades internas de los Estados.',
   'Colombia es parte de la Convención Americana y ha aceptado la competencia de la Corte, de modo que sus sentencias vinculan al Estado en los casos en que es parte.',
   'Las sentencias obligan únicamente cuando el Congreso las incorpora al ordenamiento interno mediante una ley aprobatoria posterior a cada decisión del tribunal.',
   'Las sentencias obligan a todas las autoridades del continente por igual, con independencia de que el Estado respectivo haya aceptado o no la competencia de la Corte.'],
  'La Corte Interamericana no es un tribunal extranjero cualquiera: Colombia es parte de la Convención y aceptó su competencia, de modo que sus sentencias vinculan al Estado en los casos en que es parte.',
  'Ni son meramente orientadoras, ni requieren una ley aprobatoria por cada decisión, ni obligan a Estados que no han aceptado la competencia del tribunal.'),

 (2,
  'Faltan tres días para la prueba. En los simulacros de este bloque usted acierta las preguntas conceptuales, pero falla las que lo ponen en una diligencia con una persona en condición de vulnerabilidad: elige la opción que documenta la barrera y continúa. Su registro muestra ese patrón en cuatro de los últimos seis casos. Lleva un registro de los simulacros resueltos y puede ver exactamente qué opción eligió cada vez que falló.',
  '¿Cuál es la mejor manera de corregirlo?',
  ['Memorizar las categorías del enfoque diferencial y los instrumentos internacionales aplicables a cada una, para identificar con rapidez qué garantía está en juego.',
   'Resolver más simulacros de este bloque hasta que la intuición mejore, dejando el repaso de los conceptos para los días inmediatamente anteriores a la prueba.',
   'Retener que la constancia no remueve la barrera: cuando la condición de la persona impide su participación efectiva, lo correcto es informar y pedir instrucción antes de continuar.',
   'Concentrarse en los casos con víctimas de violencia sexual y menores, que son los que más preguntas generan, y repasar los demás con la tabla de patrones de la guía.'],
  'El error tiene una sola causa: creer que documentar basta. En enfoque diferencial, documentar y seguir deja la barrera en pie; lo que corresponde es informar y pedir instrucción antes de continuar.',
  'Memorizar categorías no corrige la confusión sobre qué hacer; repetir simulacros sin cambiar el criterio repite el error; y concentrarse en dos categorías deja fuera las demás.'),
]
