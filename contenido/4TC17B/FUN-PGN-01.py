# -*- coding: utf-8 -*-
"""Día 5 · Estructura y funciones de la PGN y la División de Gestión Humana — Técnico en Criminalística 4TC-17."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-PGN-4TC17B-01',
    archivo='FUN-PGN-4TC17B-01-estructura-pgn-gestion-humana.html',
    dia=5,
    titulo_doc='Estructura y Funciones de la PGN y la División de Gestión Humana',
    h1='Estructura y Funciones de la PGN<br>y la División de Gestión Humana',
    kicker='Día 5 · Conocimientos comunes',
    sub='La <strong>estructura, organización y funciones de la Procuraduría General de la Nación</strong> es un conocimiento común exigido por el formato de convocatoria. Aquí verás qué es la PGN y de dónde viene su autoridad, sus <strong>tres funciones misionales</strong> (preventiva, disciplinaria y de intervención), el <strong>poder disciplinario preferente</strong>, la estructura del nivel central y de las procuradurías territoriales, las dependencias de apoyo y, con detalle propio, la <strong>Secretaría General</strong> y la <strong>División de Gestión Humana</strong>: dónde están en la estructura, qué funciones les asignan los <strong>artículos 62 y 63 del Decreto Ley 262 de 2000</strong>, cómo se reparten competencias entre las dos y por qué la División es la dependencia donde se ubica el <strong>Técnico en Criminalística 4TC-17</strong>.',
    badges=['⏱ 95-115 min', '🏛️ Régimen PGN', '👥 Gestión Humana'],
    fmeta='Estructura y Funciones de la PGN y de la División de Gestión Humana (Decreto Ley 262 de 2000, arts. 2, 62 y 63)',
    cargo='Técnico en Criminalística 4TC-17 (Nivel Técnico)',
    conv='285-2026',
    alerta='Estructura de la PGN y la División de Gestión Humana',
)

SEC = secciones_mapeadas('guias/FUN-PGN-6CI04-01-estructura-funciones-pgn.html')

MOD6 = '''<div class="modulo-head"><div class="modulo-n">6</div><h3>La Secretaría General y la División de Gestión Humana: tu dependencia</h3></div>
    <div class="b-texto">
      <p>Este módulo merece atención especial porque describe <mark>la dependencia donde se ubica tu cargo</mark>. El <strong>artículo 2 del Decreto Ley 262 de 2000</strong>, que fija la estructura orgánica de la entidad, ubica en el <strong>nivel central</strong>, bajo el numeral <strong>1.6</strong>, a la <strong>Secretaría General</strong>, y debajo de ella sus tres divisiones:</p>
      <div class="tabla-wrap"><table>
        <tr><th>Numeral</th><th>Dependencia</th><th>De qué responde</th></tr>
        <tr><td>1.6</td><td><strong>Secretaría General</strong></td><td>Dirige y coordina el soporte administrativo, humano y financiero de toda la entidad. El Secretario General depende directamente del Procurador General.</td></tr>
        <tr><td><strong>1.6.1</strong></td><td><strong>División de Gestión Humana ★</strong></td><td>Administra el talento humano: hojas de vida, nómina, prestaciones, novedades y situaciones administrativas. <strong>Aquí se ubica tu cargo.</strong></td></tr>
        <tr><td>1.6.2</td><td>División Administrativa</td><td>Bienes y servicios, inventarios, seguridad industrial, programa de compras.</td></tr>
        <tr><td>1.6.3</td><td>División Financiera</td><td>Presupuesto, contabilidad y tesorería.</td></tr>
      </table></div>
      <div class="ojo"><b>Ojo en la prueba:</b> esta es una confusión que los distractores explotan. La División de Gestión Humana <mark>no depende del Despacho del Procurador General</mark> ni es una entidad descentralizada con personería propia: es una <strong>división del nivel central que depende de la Secretaría General</strong> (art. 2, núm. 1.6.1). La dependencia que sí está adscrita al Despacho del Procurador, y que el artículo 10 regula, es la <strong>Dirección Nacional de Investigaciones Especiales</strong>. Son cosas distintas, y una pregunta puede jugar precisamente con el parecido del nombre «criminalística».</div>
      <div class="def-panel"><span class="def-label">Concepto</span><p>La <strong>División de Gestión Humana</strong> es la dependencia del nivel central, adscrita a la <strong>Secretaría General</strong>, que administra el talento humano de la Procuraduría: conserva las hojas de vida, la nómina, los salarios y las prestaciones; expide certificaciones; tramita las novedades y situaciones administrativas; verifica requisitos y posesiona en el nivel central; elabora las nóminas; y prepara, para la firma del Procurador General, los actos administrativos de personal, incluidos los de retiro. Sus funciones están en el <strong>artículo 63</strong>.</p></div>
      <h4>Las 14 funciones del artículo 63, agrupadas para recordarlas</h4>
      <div class="tabla-wrap"><table>
        <tr><th>Bloque</th><th>Numerales</th><th>Qué comprende</th></tr>
        <tr><td><strong>Desarrollo humano</strong></td><td>1, 2, 9</td><td>Asesorar al Secretario General en políticas de calidad de vida laboral; contribuir a la <strong>inducción y reinducción</strong>; presentar proyectos de convenios para programas de desarrollo humano (los aprueba el Procurador).</td></tr>
        <tr><td><strong>Registro y certificación</strong></td><td>3, 4</td><td><strong>Conservar las hojas de vida, la nómina, los salarios y las prestaciones</strong> del personal vinculado y <strong>expedir certificaciones</strong>; elaborar los formatos de la actualización anual de la <strong>declaración de bienes y rentas</strong>.</td></tr>
        <tr><td><strong>Novedades y situaciones</strong></td><td>5, 6</td><td><strong>Tramitar novedades y situaciones administrativas</strong>, incluida la afiliación a <strong>EPS y fondos de pensiones</strong>, y <strong>preparar los actos para la firma del Procurador</strong>, incluidos los de retiro; <strong>conceder permisos de estudio que no superen dos horas diarias</strong>, con visto bueno del jefe inmediato.</td></tr>
        <tr><td><strong>Ingreso</strong></td><td>7, 8</td><td><strong>Verificar los requisitos de los nombrados y emitir concepto escrito antes de la posesión</strong>; <strong>posesionar</strong> a los servidores del nivel central en empleos profesionales, técnicos, administrativos y operativos.</td></tr>
        <tr><td><strong>Nómina</strong></td><td>10</td><td><strong>Elaborar las nóminas</strong> con apoyo de la Oficina de Sistemas.</td></tr>
        <tr><td><strong>Coordinación y carrera</strong></td><td>11, 12, 13</td><td><strong>Supervisar</strong> la gestión humana en los niveles territoriales; apoyar a la <strong>Comisión de Carrera</strong>; coordinar y vigilar la <strong>elección de los representantes de los servidores en la Comisión de Personal</strong>.</td></tr>
        <tr><td><strong>Cláusula de cierre</strong></td><td>14</td><td>Las demás que le asignen la ley y el Procurador General.</td></tr>
      </table></div>
      <h4>Quién decide qué: la tabla que más se pregunta</h4>
      <p>El artículo 62 (Secretaría General) y el 63 (División de Gestión Humana) se reparten competencias que se parecen mucho. Confundirlas, en el trabajo, significa tramitar ante quien no puede decidir y devolver el expediente al punto de partida. En la prueba, significa perder la pregunta.</p>
      <div class="tabla-wrap"><table>
        <tr><th>Asunto</th><th>Quién</th><th>Norma</th></tr>
        <tr><td>Permiso de estudio <strong>hasta</strong> 2 horas diarias</td><td><strong>División de Gestión Humana</strong></td><td>art. 63, núm. 6</td></tr>
        <tr><td>Permiso de estudio de <strong>más</strong> de 2 horas diarias</td><td>Secretaría General</td><td>art. 62, núm. 6</td></tr>
        <tr><td>Vacaciones, licencias y comisiones de servicio</td><td>Secretaría General</td><td>art. 62, núm. 6</td></tr>
        <tr><td>Prestaciones sociales, viáticos y gastos de viaje</td><td>Secretaría General</td><td>art. 62, núm. 7</td></tr>
        <tr><td>Posesión de los niveles directivo, asesor y ejecutivo</td><td>Secretaría General</td><td>art. 62, núm. 5</td></tr>
        <tr><td>Posesión en el nivel central de empleos profesionales, técnicos, administrativos y operativos</td><td><strong>División de Gestión Humana</strong></td><td>art. 63, núm. 8</td></tr>
        <tr><td>Concepto previo de requisitos, antes de la posesión</td><td><strong>División de Gestión Humana</strong></td><td>art. 63, núm. 7</td></tr>
        <tr><td>Elaboración de la nómina</td><td><strong>División de Gestión Humana</strong> + Oficina de Sistemas</td><td>art. 63, núm. 10</td></tr>
        <tr><td>Acto administrativo de retiro</td><td><strong>Proyecta</strong> la División · <strong>firma</strong> el Procurador</td><td>art. 63, núm. 5</td></tr>
      </table></div>
      <div class="ojo"><b>Ojo en la prueba:</b> la frontera es <mark>las dos horas</mark>. Un permiso de estudio de dos horas diarias lo concede la División; de dos horas y media, la Secretaría General. Y fíjate en el verbo: la División <strong>prepara</strong> y <strong>proyecta</strong> los actos de personal, pero quien los <strong>firma</strong> es el Procurador General. Cuando una opción diga que la División «expide» o «firma» el acto de retiro, desconfía.</div>
      <h4>Cómo llega el trabajo a tus manos</h4>
      <div class="flujo">
        <div class="flujo-item"><strong>1. Solicitud</strong><br>Un servidor, un jefe de dependencia o una procuraduría territorial radica una solicitud de personal (nombramiento, novedad, certificación, permiso)</div>
        <div class="flujo-item"><strong>2. Reparto</strong><br>La División asigna el trámite y lo registra en el control de correspondencia</div>
        <div class="flujo-item"><strong>3. Verificación</strong><br>Se revisan los soportes frente a los requisitos de la norma y del manual</div>
        <div class="flujo-item"><strong>4. Proyección</strong><br>Se proyecta el acto o la constancia «según los modelos y procedimientos establecidos»</div>
        <div class="flujo-item"><strong>5. Firma y archivo</strong><br>Firma el competente, se notifica o comunica y el documento se archiva en la historia laboral</div>
      </div>
      <div class="practica">
        <div class="practica-head">🗂️ En la práctica</div>
        <div class="practica-body">
          <p>Una Procuraduría Provincial informa que un servidor de su planta fue nombrado en un empleo del nivel técnico en Bogotá. La solicitud llega a la División de Gestión Humana. El Técnico en Criminalística 4TC-17 <strong>verifica los requisitos</strong> del nombrado contra el manual específico de funciones —estudios, experiencia, antecedentes—, deja la <strong>constancia escrita</strong> que exige el numeral 7 del artículo 63, <strong>proyecta</strong> el acta de posesión conforme al modelo, y una vez surtida la posesión <strong>archiva</strong> todo en la historia laboral y registra la novedad para que entre a la nómina. Él verificó, proyectó y registró; <strong>posesionar</strong> es de la División como dependencia, y la <strong>decisión</strong> del nombramiento fue del Procurador.</p>
        </div>
      </div>
      <div class="acordeon">
        <details class="acc"><summary>🔎 ¿Por qué el talento humano está bajo la Secretaría General y no en una dirección propia?</summary><div class="acc-body"><p>Porque el Decreto Ley 262 de 2000 agrupó en la Secretaría General los tres soportes transversales de la entidad: el <strong>humano</strong> (División de Gestión Humana), el <strong>administrativo</strong> (División Administrativa) y el <strong>financiero</strong> (División Financiera). Esa agrupación tiene una lógica práctica: casi ningún trámite de personal se agota en uno solo de los tres. Un nombramiento necesita el soporte humano que verifica requisitos, el financiero que confirma la disponibilidad presupuestal y, muchas veces, el administrativo que dota el puesto de trabajo. Tenerlos bajo un mismo jefe es lo que permite que el trámite no se fragmente.</p></div></details>
        <details class="acc"><summary>🔎 ¿La División de Gestión Humana manda sobre el personal de las procuradurías territoriales?</summary><div class="acc-body"><p><strong>Supervisa</strong>, que no es lo mismo que administrar directamente. El numeral 11 del artículo 63 le encarga «supervisar la administración de gestión humana en los niveles territoriales»: fija el criterio, verifica que se aplique de manera homogénea y resuelve las dudas, pero la operación cotidiana ocurre en cada sede. Esa distinción explica por qué a la División llegan consultas de todo el país sobre cómo tramitar una situación administrativa.</p></div></details>
        <details class="acc"><summary>🔎 ¿Qué es la Comisión de Carrera y qué es la Comisión de Personal?</summary><div class="acc-body"><p>No son lo mismo y la División se relaciona con las dos de manera distinta. A la <strong>Comisión de Carrera</strong> le presta «apoyo humano y logístico» (núm. 12): es la instancia del régimen especial de carrera de la PGN. Frente a la <strong>Comisión de Personal</strong>, su tarea es <strong>coordinar y vigilar la elección de los representantes de los servidores</strong> (núm. 13); es decir, garantiza que los servidores puedan elegir a quienes los representan. En ninguno de los dos casos la División sustituye a la comisión: la apoya y garantiza su conformación.</p></div></details>
      </div>
      <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> la División de Gestión Humana es el numeral 1.6.1 del artículo 2 del Decreto Ley 262 de 2000: una división del nivel central que depende de la <strong>Secretaría General</strong>, junto con la Administrativa y la Financiera. Sus 14 funciones están en el <strong>artículo 63</strong> y se agrupan en desarrollo humano, registro y certificación, novedades y situaciones administrativas, ingreso, nómina, coordinación y carrera. Reparte competencias con la Secretaría General (art. 62): la frontera de los permisos de estudio son <strong>dos horas diarias</strong>, y los actos de personal los <strong>proyecta</strong> la División pero los <strong>firma</strong> el Procurador General. Es la dependencia donde se ubica el Técnico en Criminalística 4TC-17.</p></div>
    </div>
  </div>

  '''

MOD7 = '''<div class="modulo-head"><div class="modulo-n">7</div><h3>Dónde encaja el Técnico en Criminalística 4TC-17 en este mapa institucional</h3></div>
    <div class="b-texto">
      <p>Con el mapa completo, ubiquemos tu cargo. El <strong>Técnico en Criminalística 4TC-17</strong> es un empleo del <strong>nivel técnico</strong> adscrito a la <strong>División de Gestión Humana</strong>, con ubicación en Bogotá y vinculado al proceso de <strong>Talento Humano</strong>. Y conviene decirlo sin rodeos, porque es la clave de toda tu preparación: el empleo <em>se llama</em> «Técnico en Criminalística», pero la plaza ofertada está en Gestión Humana, y por eso los <strong>conocimientos específicos</strong> que la convocatoria evalúa son <mark>gestión del talento humano y CPACA</mark>, con la criminalística como «conocimientos técnicos del área disciplinar».</p>
      <div class="ojo"><b>Ojo en la prueba:</b> el numeral 8 del formato de convocatoria es explícito: las pruebas evalúan los conocimientos <mark>previstos en el Manual Específico de Funciones</mark> para el empleo ofertado. No el que sugiere el nombre del cargo, sino el que el manual lista. Si estudias solo criminalística, estudias el renglón menos probable de la prueba.</div>
      <h4>Tu aporte a las funciones misionales, sin rodeos</h4>
      <p>Las tres funciones misionales de la PGN —preventiva, disciplinaria y de intervención— las ejercen las dependencias misionales. Tu cargo no está en ninguna de ellas: está en el <strong>soporte</strong>. Eso no lo vuelve menor, y la razón es simple de ver:</p>
      <div class="tabla-wrap"><table>
        <tr><th>Función misional</th><th>¿La ejerce el 4TC-17?</th><th>Su relación con tu trabajo</th></tr>
        <tr><td><strong>Preventiva</strong></td><td>No directamente</td><td>Quien la ejerce es un servidor que debe estar bien nombrado, con sus requisitos verificados y su situación administrativa en orden. Eso lo produce tu dependencia.</td></tr>
        <tr><td><strong>Disciplinaria</strong></td><td>No directamente</td><td>Igual: sin servidores posesionados en forma, la actuación disciplinaria es vulnerable. Además, la historia laboral es la fuente de los antecedentes del propio servidor.</td></tr>
        <tr><td><strong>De intervención</strong></td><td>No</td><td>La ejercen los agentes del Ministerio Público designados para ello.</td></tr>
        <tr><td><strong>Soporte de talento humano</strong></td><td><strong>Sí, de manera principal</strong></td><td>Preparas, verificas, tramitas, registras y proyectas los actos de personal que hacen posible que las tres funciones anteriores tengan quién las ejerza.</td></tr>
      </table></div>
      <h4>Las ocho funciones de tu manual, leídas como límites</h4>
      <div class="tabla-wrap"><table>
        <tr><th>Lo que sí hace tu cargo</th><th>Lo que no le corresponde</th></tr>
        <tr><td>Preparar y verificar los soportes de los trámites de personal frente a los requisitos de la norma y del manual</td><td>Declarar cumplido un requisito que los soportes no acreditan</td></tr>
        <tr><td><strong>Proyectar</strong> los actos administrativos de personal «según los modelos y procedimientos establecidos»</td><td><strong>Firmar</strong> esos actos: la firma es del competente (Procurador o Secretaría General, según el asunto)</td></tr>
        <tr><td><strong>Examinar informes</strong> en cuanto a la pertinencia e idoneidad de los métodos, procedimientos y técnicas de su especialidad</td><td>Calificar jurídicamente el asunto o resolver el fondo de la situación de personal</td></tr>
        <tr><td>Llevar el <strong>control de la correspondencia</strong> y apoyar el <strong>archivo</strong>, en especial el de las historias laborales</td><td>Decidir sobre el acceso de terceros a los datos personales que ese archivo contiene</td></tr>
      </table></div>
      <div class="flujo">
        <div class="flujo-item"><strong>Procurador General</strong><br>Nombra, retira y firma los actos de personal de su competencia</div>
        <div class="flujo-item"><strong>Secretario General</strong><br>Dirige el soporte humano; reconoce prestaciones, vacaciones, licencias y comisiones</div>
        <div class="flujo-item"><strong>Jefe de la División</strong><br>Dirige el trámite, posesiona en el nivel central, concede permisos de hasta dos horas</div>
        <div class="flujo-item"><strong>Técnico en Criminalística ★</strong><br>Verifica soportes, tramita novedades, proyecta actos, registra y archiva</div>
      </div>
      <div class="box ok">
        <div class="box-title">✅ Tu aporte es decisivo, y tiene un límite claro</div>
        <p>De la exactitud de tu verificación depende que un nombramiento se sostenga, que una prestación se reconozca sobre la base correcta y que una nómina pague lo que debe pagar. Un requisito dado por cumplido sin soporte puede costar la nulidad del acto; un día mal contado, dinero mal liquidado. Pero su trabajo termina en el <strong>proyecto y la constancia</strong>: no decide la situación de personal, no reconoce derechos, no posesiona por su cuenta y no firma. Ese límite no le resta importancia: es lo que mantiene su producto dentro del terreno técnico, que es precisamente donde tiene valor.</p>
      </div>
      <div class="ojo"><b>Ojo en la prueba:</b> muchas preguntas situacionales de este perfil ponen a prueba exactamente esa frontera. Cuando una opción propone que el técnico <mark>decida, reconozca, autorice o firme</mark>, casi siempre es incorrecta, por muy eficaz que parezca. La conducta esperada es verificar, dejar el proyecto listo con sus soportes, informar al competente y dejar constancia.</div>
      <div class="acordeon">
        <details class="acc"><summary>🔎 ¿Y entonces para qué sirve la criminalística en este empleo?</summary><div class="acc-body"><p>Para dos cosas reales. La primera: el manual exige «conocimientos técnicos del área disciplinar», y la prueba puede preguntarlos, aunque sea un renglón entre seis. La segunda, más de fondo: la función 2 de tu manual te encarga <strong>examinar informes respecto de la pertinencia e idoneidad de los métodos, procedimientos y técnicas de su especialidad</strong>. Esa es una mirada técnica —¿se aplicó el método correcto?, ¿el procedimiento era el idóneo?— que se ejerce también sobre documentos y soportes. Verificar la autenticidad de un título, advertir la alteración de una certificación o detectar una foliación inconsistente es, en el fondo, el mismo hábito de rigor. Por eso el Día 19 trabaja la criminalística aplicada a tu puesto, no en abstracto.</p></div></details>
        <details class="acc"><summary>🔎 ¿Qué significa que el empleo sea de planta global?</summary><div class="acc-body"><p>Que la ubicación inicial —Bogotá, en la División de Gestión Humana— no es inamovible. Conforme al numeral 34 del artículo 7 del Decreto Ley 262 de 2000, los cargos de la planta globalizada pueden ser distribuidos y reubicados en diferentes especialidades, sedes y dependencias según las necesidades del servicio, en cualquier tiempo durante el período de prueba o después de cumplido. El formato de convocatoria lo advierte expresamente. En la práctica: podrías terminar apoyando la gestión humana de una sede territorial, o un área distinta, sin que eso sea un traslado irregular.</p></div></details>
        <details class="acc"><summary>🔎 ¿Trabajas solo para la División de Gestión Humana?</summary><div class="acc-body"><p>Trabajas <em>desde</em> la División, pero tu usuario interno cambia con cada trámite: puede ser un servidor que pide una certificación, un jefe de dependencia que necesita un encargo, una procuraduría territorial que consulta cómo tramitar una situación administrativa, o la Secretaría General que requiere los soportes de un reconocimiento. Por eso debes entender la estructura completa de la entidad: para saber quién te pide, con qué competencia y a quién debe llegar el resultado.</p></div></details>
      </div>
    </div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> el Técnico en Criminalística 4TC-17 pertenece al nivel técnico y trabaja desde la División de Gestión Humana, en el proceso de Talento Humano. Su aporte es el soporte técnico de la gestión del personal: verifica requisitos y soportes, tramita novedades, proyecta actos administrativos «según los modelos establecidos», examina informes en cuanto al método y la técnica de su especialidad, y lleva el control de la correspondencia y el archivo de las historias laborales. No decide la situación de personal, no reconoce derechos y no firma. Y aunque el empleo se llame «Criminalística», los conocimientos específicos que la prueba evalúa son los del manual: talento humano y CPACA.</p></div>
  </div>

  '''

R = [
    ('<p>Otro dato institucional relevante de tu convocatoria es el número de plazas disponibles y la asignación salarial: la Convocatoria 90-2026 ofrece <strong>39 plazas</strong> para el cargo de Citador 6CI-04, dentro de la modalidad de Planta Global, con una asignación salarial de <strong>$3.120.457</strong> vigente para el año 2025. Para acceder a estas plazas, el manual exige una aprobación de 2 años de educación básica secundaria, sin requerir experiencia laboral previa, lo que hace de este cargo una puerta de entrada accesible a la carrera especial de la Procuraduría para muchas personas que buscan su primera oportunidad en el sector público.</p>',
     '<p>Otro dato institucional relevante de tu convocatoria es el número de plazas y la asignación salarial: la <strong>Convocatoria 285-2026</strong> (Versión 3, Resolución 212 de 2026) ofrece <strong>una (1) plaza</strong> de <strong>Técnico en Criminalística, código 4TC-17</strong>, en <strong>Planta Global</strong> con ubicación inicial en <strong>Bogotá</strong>, adscrita a la <strong>División de Gestión Humana</strong> y vinculada al proceso de <strong>Talento Humano</strong>, con una asignación básica de <strong>$8.972.318</strong> (vigencia 2025). En requisitos, el manual pide <strong>tres (3) años de educación superior y curso específico en el área relacionada</strong>, <strong>o</strong> <strong>título de formación técnica profesional</strong> en áreas relacionadas con las funciones del cargo o con los procesos de la dependencia, más curso específico; y en experiencia, <strong>no requiere</strong> <strong>o</strong> <strong>un (1) año de experiencia relacionada</strong>, según la alternativa de estudio que se acredite. Que sea una sola plaza cambia la estrategia: no basta con superar el mínimo, hay que quedar de primero en la lista de elegibles.</p>'),
    ('<p>La modalidad de "Planta Global" merece una breve aclaración adicional: significa que las 39 plazas no están necesariamente atadas, de forma fija y permanente, a una única dependencia específica, sino que la entidad tiene flexibilidad para distribuir y, en algunos casos, reubicar a quienes ocupan estos cargos según las necesidades del servicio en las distintas dependencias que hemos recorrido en esta guía.',
     '<p>La modalidad de "Planta Global" merece una breve aclaración adicional: significa que la plaza no está necesariamente atada, de forma fija y permanente, a una única dependencia específica, sino que la entidad tiene flexibilidad para distribuir y, en algunos casos, reubicar a quienes ocupan estos cargos según las necesidades del servicio en las distintas dependencias que hemos recorrido en esta guía (numeral 34 del artículo 7 del Decreto Ley 262 de 2000).'),
    ('dónde encaja el trabajo del Citador</mark> dentro de esa enorme maquinaria institucional. Con ese mapa claro, cada oficio que repartas y cada trámite que hagas tendrán sentido dentro de un todo que entiendes, no solo direcciones sueltas que memorizas.',
     'dónde encaja el trabajo del Técnico en Criminalística</mark> dentro de esa enorme maquinaria institucional. Con ese mapa claro, cada apoyo técnico que prestes y cada trámite que practiques tendrán sentido dentro de un todo que entiendes, y no serán tareas sueltas que ejecutas sin ver el conjunto.'),
    ('Dónde encaja exactamente el <strong>Citador</strong> en esta estructura, y por qué su labor conecta a todas las dependencias entre sí y con el ciudadano.',
     'Dónde encaja exactamente el <strong>Técnico en Criminalística</strong> en esta estructura, y por qué la División de Gestión Humana presta su capacidad técnica a todas las dependencias.'),
    ('La prueba evalúa este tema porque un Citador que confunde una Procuraduría Delegada Disciplinaria con una Preventiva, o que no sabe qué hace la División de Documentación, dif',
     'La prueba evalúa este tema porque un Técnico en Criminalística que confunde una Procuraduría Delegada Disciplinaria con una Preventiva, o que no sabe de quién depende su propia Dirección, dif'),
    ('Tu cargo de Citador pertenece, precisamente, a ese engranaje de apoyo: no decides en ninguna de las tres funciones misionales, pero tu trabajo de cor',
     'Tu cargo de Técnico en Criminalística pertenece, precisamente, a la función disciplinaria: no decides el fondo de ninguna actuación, pero tu trabajo de cor'),
    ('compites por el cargo de Citador, código y grado <strong>6CI-04</strong>, nivel jerárquico Operativo',
     'compites por el cargo de Técnico en Criminalística, código y grado <strong>4TC-17</strong>, nivel jerárquico Técnico'),
    ('Citador', 'Técnico en Criminalística'),
    ('6CI-04', '4TC-17'),
    ('90-2026', '285-2026'),
]
SEC = aplicar_todas(SEC, R, estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol('Técnico en Criminalística', 'Técnicos en Criminalística'), estricto=False)   # filtro antifugas final

partes = SEC[2].split('<div class="modulo">')
assert len(partes) == 10, f'se esperaban 10 bloques y hay {len(partes)}'
partes[6] = MOD6
partes[7] = MOD7
SEC[2] = '<div class="modulo">'.join(partes)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre la estructura y '
              'las funciones de la Procuraduría y de la División de Gestión Humana. Los contextos '
              'son extensos y las cuatro opciones son plausibles. Al seleccionar una opción verás si acertaste y la explicación.')

P = [
 (1,
  'Una Procuraduría Provincial tiene dudas sobre cómo tramitar la licencia no remunerada de un servidor de su sede y consulta a la División de Gestión Humana. En la dependencia hay dos lecturas: un servidor sostiene que, al consultar, la Provincial pierde el asunto y la División debe tramitar directamente todas las novedades de esa sede; otro cree que la División debe negarse a responder, porque la administración del personal territorial no es asunto suyo.',
  '¿Cuál es la lectura correcta del papel de la División de Gestión Humana en ese escenario?',
  ['La Provincial pierde la gestión al consultar: desde ese momento la División asume la administración del personal de esa sede, tramita sus novedades y responde por ellas ante la Secretaría General.',
   'La División <strong>supervisa</strong> la administración de gestión humana en los niveles territoriales (art. 63, núm. 11): fija el criterio y resuelve la consulta, y la operación del trámite sigue en la Provincial.',
   'La División debe negarse, porque sus funciones se agotan en el personal del nivel central y orientar a una sede territorial sobre un trámite de personal excede lo que el artículo 63 le asigna.',
   'La División debe remitir la consulta a la Procuraduría Auxiliar para Asuntos Disciplinarios, que es la dependencia encargada de coordinar los asuntos que involucran a varias áreas de la entidad.'],
  'El numeral 11 del artículo 63 del Decreto Ley 262 de 2000 encarga a la División <strong>supervisar</strong> la administración de gestión humana en los niveles territoriales. Supervisar es fijar el criterio, verificar que se aplique de manera homogénea y resolver las dudas; no es absorber la operación. El trámite se surte en la Provincial con la orientación recibida.',
  'Ni la Provincial pierde el trámite, ni la División debe negarse a orientar —supervisar incluye resolver la consulta—, ni el asunto se canaliza por la Procuraduría Auxiliar, que no es una instancia de talento humano.'),

 (3,
  'Un practicante pregunta de quién depende la División de Gestión Humana. Un servidor responde que del Despacho del Procurador General, «porque él firma los actos de personal»; otro, que es una entidad adscrita con autonomía administrativa y presupuestal propia; y un tercero, que depende del Instituto de Estudios del Ministerio Público. La discusión no es académica: de la ubicación depende por qué línea sube una consulta, quién resuelve un conflicto de criterio entre dependencias y ante quién responde la División por sus trámites. Usted les propone resolverlo leyendo la norma que fija la estructura orgánica de la entidad.',
  'Conforme al Decreto Ley 262 de 2000, ¿cuál es la ubicación correcta de la División de Gestión Humana?',
  ['Depende directamente del Despacho del Procurador General, que es quien firma los actos administrativos de personal, de modo que la División recibe de él sus instrucciones sin intermediación alguna.',
   'Es una entidad adscrita a la Procuraduría, con personería jurídica, autonomía administrativa y presupuesto propio, lo que le permite definir por sí misma la política de talento humano de la entidad.',
   'Depende del Instituto de Estudios del Ministerio Público, que es el encargado de la formación y la capacitación de los servidores dentro de la estructura de la entidad.',
   'Es una división del nivel central que depende de la <strong>Secretaría General</strong>, junto con la División Administrativa y la División Financiera, conforme al numeral 1.6.1 del artículo 2.'],
  'El artículo 2 del Decreto Ley 262 de 2000 la ubica en el numeral <strong>1.6.1</strong>: una de las tres divisiones del nivel central que dependen de la <strong>Secretaría General</strong> (1.6), con la Administrativa (1.6.2) y la Financiera (1.6.3). Que el Procurador firme algunos actos de personal no la hace depender de su Despacho: la línea jerárquica pasa por el Secretario General, que es quien depende directamente de él.',
  'No depende del Despacho del Procurador —esa es la posición de la Dirección Nacional de Investigaciones Especiales, art. 10—, no es una entidad con personería propia y no pertenece al IEMP.'),

 (2,
  'En una reunión, un servidor afirma que «la Procuraduría solo sanciona» y que la función preventiva «es publicidad institucional». Otro sostiene que la función de intervención consiste en que la entidad demande a los servidores ante los jueces. El jefe le pide a usted explicar las tres funciones misionales, porque el informe técnico que prepara el equipo será usado en una actuación preventiva.',
  '¿Cuál explicación distingue correctamente las tres funciones?',
  ['Las tres son la misma actividad con nombres distintos según la dependencia que la ejerza, de modo que prevenir, investigar y conceptuar son etapas sucesivas de un único procedimiento.',
   'La preventiva y la de intervención corresponden a la Defensoría del Pueblo y a las personerías, mientras la PGN se limita a la función disciplinaria sobre los servidores públicos.',
   'La preventiva actúa antes del daño advirtiendo y acompañando; la disciplinaria investiga y sanciona la conducta del servidor; y la de intervención hace comparecer al Ministerio Público ante las autoridades judiciales y administrativas.',
   'La preventiva impone medidas cautelares, la disciplinaria formula cargos y la de intervención ejecuta las sanciones impuestas, de modo que las tres se aplican en ese orden dentro del mismo proceso.'],
  'Son tres funciones autónomas: prevenir antes del daño, disciplinar la conducta ya ocurrida e intervenir ante autoridades en defensa del orden jurídico, los derechos y el patrimonio público. Pueden concurrir sobre hechos conexos.',
  'No son etapas de un mismo procedimiento, la PGN sí ejerce las tres y la intervención no consiste en ejecutar sanciones.'),

 (0,
  'Una entidad territorial alega que su oficina de control interno disciplinario ya está tramitando el caso y que, por eso, la Procuraduría «no puede meterse». El expediente lleva dos años sin movimiento y hay riesgo de prescripción. El equipo debe explicar en el informe por qué la Procuraduría sí puede actuar. El informe debe explicar la base normativa de la actuación y el jefe advierte que la entidad ya anunció que controvertirá cualquier intervención de la Procuraduría en ese expediente.',
  '¿Qué figura constitucional fundamenta esa posibilidad?',
  ['El poder disciplinario preferente (art. 277 num. 6): la PGN puede desplazar a la oficina de control interno disciplinario y asumir directamente el conocimiento del proceso.',
   'El control fiscal preferente, que permite a la Procuraduría asumir las investigaciones de la Contraloría cuando esta no actúa con el trámite debida en los casos de mayor impacto.',
   'La función de intervención, que faculta a la Procuraduría para comparecer dentro del proceso disciplinario interno de la entidad como sujeto procesal con facultades de impulso.',
   'La vigilancia administrativa ordinaria, que obliga a la entidad a remitir el expediente a la Procuraduría cuando la actuación supera los dos años sin decisión de fondo del asunto.'],
  'El poder disciplinario preferente del artículo 277 numeral 6 permite a la PGN asumir el conocimiento de procesos que adelantan las oficinas de control interno disciplinario, con la motivación que corresponda.',
  'No existe un control fiscal preferente de la PGN, la intervención no opera dentro del proceso disciplinario interno y no hay remisión automática por el paso del tiempo.'),

 (1,
  'Dos servidores radican el mismo día una solicitud de permiso para estudiar: uno pide dos horas diarias y el otro, tres. Ambos traen el visto bueno de su jefe inmediato. Un compañero le dice que los dos permisos los concede la División, «porque los permisos de estudio son de Gestión Humana»; otro, que los dos debe reconocerlos la Secretaría General, «porque toda licencia es de allá».',
  'Conforme a los artículos 62 y 63 del Decreto Ley 262 de 2000, ¿cómo se reparte la competencia?',
  ['Los dos permisos los concede la División de Gestión Humana, porque el artículo 63 le asigna los permisos de estudio sin distinguir la cantidad de horas que el servidor solicite.',
   'El de dos horas lo concede la División de Gestión Humana (art. 63, núm. 6) y el de tres lo reconoce la Secretaría General (art. 62, núm. 6): la frontera está en que el permiso no supere las dos horas diarias.',
   'Los dos los reconoce la Secretaría General, porque el artículo 62 le atribuye las vacaciones, las licencias, las comisiones y los permisos, y la División solo prepara los proyectos para su firma.',
   'Ninguno de los dos puede concederse con el solo visto bueno del jefe inmediato: ambos requieren además el concepto previo de la Oficina de Planeación sobre el impacto en el servicio.'],
  'El numeral 6 del artículo 63 faculta a la División para conceder los permisos de estudio «que no superen dos horas diarias», con visto bueno del jefe inmediato; el numeral 6 del artículo 62 deja en la Secretaría General los de más de dos horas, junto con vacaciones, licencias y comisiones de servicio. Dos horas exactas están dentro de la competencia de la División; dos horas y media, ya no.',
  'Ni los dos son de la División, ni los dos son de la Secretaría General, ni se exige un concepto de Planeación que la norma no prevé: lo que reparte la competencia es el límite de las dos horas diarias.'),

 (3,
  'Un servidor nuevo cree que las procuradurías regionales y provinciales «son entidades independientes» y que, por eso, la División de Gestión Humana no puede prestarles apoyo sin un convenio. Otro sostiene que el apoyo solo procede para las procuradurías delegadas del nivel central. El jefe pide claridad porque acaba de llegar una solicitud de una Provincial. La solicitud llegó firmada por el procurador provincial, con el objeto del apoyo definido, y el término del expediente empieza a correr contra la dependencia solicitante.',
  '¿Cuál es la afirmación correcta?',
  ['Las procuradurías territoriales son entidades independientes y el apoyo entre ellas y el nivel central requiere la celebración previa de un convenio interadministrativo de cooperación.',
   'El apoyo técnico de la División de Gestión Humana solo procede para las procuradurías delegadas del nivel central, porque son las únicas que pertenecen a la misma estructura orgánica de la Dirección.',
   'El apoyo procede únicamente cuando el Procurador General lo ordena caso por caso, de modo que una solicitud directa de una Provincial debe devolverse sin trámite por falta de competencia.',
   'Las procuradurías territoriales son dependencias de la misma entidad y la División de Gestión Humana presta apoyo técnico-científico a las dependencias que lo soliciten, sin necesidad de convenio alguno.'],
  'Regionales, distritales y provinciales son dependencias de la PGN desconcentradas en el territorio, no entidades distintas. El numeral 2 del artículo 10 habla de apoyo a «las dependencias» sin restringirlo al nivel central.',
  'No son entidades independientes, el apoyo no se limita a las delegadas y no exige orden caso por caso del Procurador General.'),

 (2,
  'Llega una solicitud para proyectar el acto de una comisión de servicios. Al revisarla, usted advierte que la firma el coordinador de un grupo interno de trabajo y no el jefe de la dependencia, y que no viene el soporte de la disponibilidad presupuestal de los viáticos. Un compañero propone proyectar de una vez el acto para no perder tiempo, porque el viaje es la semana entrante; otro, devolver la solicitud sin más. Reprogramar el viaje tendría costo para la entidad.',
  '¿Qué corresponde hacer antes de proyectar el acto?',
  ['Nada en particular: la División proyecta los actos que se le soliciten y verificar quién firma la solicitud y su respaldo presupuestal corresponde exclusivamente a la dependencia solicitante.',
   'Basta verificar que la solicitud tenga número de radicado y una firma legible de algún superior del servidor, requisitos formales suficientes para proyectar el acto dentro del término.',
   'Verificar que la solicitud provenga de quien puede hacerla y que estén los soportes exigidos, requerir por escrito lo que falte informando el impacto en la fecha, y dejar constancia de lo advertido.',
   'Debe devolverse la solicitud de plano y sin trámite, porque un coordinador de grupo interno nunca puede impulsar una comisión de servicios y la petición es jurídicamente inexistente.'],
  'La verificación previa es precisamente la función del técnico: un acto proyectado sobre una solicitud de quien no podía hacerla, o sin el respaldo presupuestal de los viáticos, nace viciado y el pago queda sin soporte. Advertirlo por escrito, requerir lo que falta e informar el impacto en la fecha protege el acto, la entidad y su propio trabajo.',
  'Ni ignorar el punto, ni limitarse al radicado y una firma cualquiera, ni devolver de plano sin dar oportunidad de subsanar: se verifica, se requiere lo que falta por escrito y se deja constancia.'),

 (0,
  'Un ciudadano pregunta en la sede si la Procuraduría es la entidad que debe recuperar unos recursos públicos que, según él, se perdieron en un contrato. Un servidor le responde que sí, que «la Procuraduría recupera el dinero»; otro, que debe acudir a la Fiscalía porque «todo lo de plata es delito». El ciudadano insiste en que ya pasaron dos años desde los hechos y que quiere saber ante quién debe insistir para recuperar el dinero perdido en el contrato.',
  '¿Cuál es la orientación correcta sobre las competencias?',
  ['La recuperación de los recursos y la responsabilidad fiscal corresponden a la Contraloría; la PGN examina la conducta del servidor y, si hay indicios de delito, se compulsa a la Fiscalía.',
   'La Procuraduría recupera los recursos mediante el proceso disciplinario, porque la sanción incluye la orden de reintegro del valor perdido a cargo del servidor responsable del contrato.',
   'La Fiscalía concentra todo el asunto, porque cualquier pérdida de recursos públicos constituye un delito y las demás autoridades deben esperar el resultado del proceso penal.',
   'El ciudadano debe acudir primero a la entidad contratante para que ella recupere el dinero, y solo si no lo hace puede presentar la queja ante los órganos de control del Estado.'],
  'Cada responsabilidad tiene su autoridad: fiscal en la Contraloría, disciplinaria en la PGN y penal en la Fiscalía. Son autónomas y pueden concurrir sobre el mismo hecho.',
  'La PGN no recupera recursos, la Fiscalía no concentra todas las vías y no hay que agotar primero a la entidad contratante.'),

 (1,
  'En la dependencia se discute qué significa que la PGN tenga «régimen especial de carrera». Un servidor afirma que la entidad puede nombrar libremente a su personal porque «no está sujeta a concurso»; otro cree que aplica la Ley 909 de 2004 con algunas modificaciones. La discusión surge porque la dependencia debe explicar el punto en una jornada de inducción y el jefe quiere que la respuesta quede sustentada en la norma que rige la entidad.',
  '¿Cuál es la afirmación correcta sobre el régimen de carrera de la PGN?',
  ['La entidad puede nombrar libremente a su personal porque el régimen especial la exime de los concursos de méritos previstos para el régimen general de carrera administrativa.',
   'La PGN tiene su propio sistema especial de carrera (Decretos Ley 262, 263 y 264 de 2000) y administra sus concursos: el ingreso se hace por mérito, pero no bajo las reglas de la CNSC.',
   'La PGN aplica la Ley 909 de 2004 con modificaciones menores, de modo que sus concursos los administra la Comisión Nacional del Servicio Civil con reglas adaptadas a su estructura.',
   'La PGN carece de régimen propio y por eso cada convocatoria define libremente sus reglas, sin sujeción a una norma previa que regule el ingreso, la permanencia y el retiro del servicio.'],
  'El régimen especial no elimina el mérito: lo organiza con reglas propias. La entidad convoca y administra el concurso conforme a sus decretos ley y a la resolución de convocatoria.',
  'Ni nombramiento libre, ni aplicación de la Ley 909 con la CNSC, ni ausencia de regulación.'),

 (3,
  'Durante una capacitación, un asistente sostiene que el Técnico en Criminalística 4TC-17 «participa en las tres funciones misionales por igual». Otro afirma que no participa en ninguna y que, por eso, su trabajo es irrelevante para la misión de la entidad. El facilitador pide precisión, porque la pregunta suele aparecer en las pruebas de este perfil, y recuerda que en convocatorias anteriores aparecieron opciones que atribuían al cargo funciones de intervención ante jueces y que varios aspirantes cayeron en ellas.',
  '¿Cómo se relaciona el cargo con las funciones misionales?',
  ['Participa en las tres por igual, porque el apoyo de talento humano se requiere indistintamente en las actuaciones preventivas, disciplinarias y de intervención ante autoridades judiciales.',
   'No participa en ninguna, y por eso su trabajo es ajeno a la misión: se limita a tareas instrumentales cuya calidad no incide en el ejercicio de las funciones constitucionales de la entidad.',
   'Participa principalmente en la función de intervención, porque las certificaciones laborales que expide se presentan ante autoridades judiciales en defensa del orden jurídico y del patrimonio público.',
   'No ejerce ninguna de las tres de manera directa: su cargo es de <strong>soporte</strong> y hace posible que la entidad tenga servidores bien vinculados para ejercerlas, sin intervenir ante autoridades judiciales.'],
  'El manual vincula el empleo al proceso de <strong>Talento Humano</strong>, en la División de Gestión Humana: es un cargo de soporte, no misional. Pero soporte no es irrelevancia: sin servidores bien nombrados, con requisitos verificados y situación administrativa en orden, la entidad no tiene con quién ejercer sus funciones. La intervención ante autoridades la ejercen los agentes del Ministerio Público designados para ello.',
  'Ni las tres por igual, ni la intervención, ni «ninguna y por eso irrelevante»: el cargo es de soporte al talento humano, y de su rigor depende que quienes ejercen las funciones misionales estén debidamente vinculados.'),

 (2,
  'Llega a la Dirección un oficio en el que una Procuraduría Delegada pide apoyo técnico y, además, solicita que el informe «concluya si la conducta del servidor constituye falta gravísima». El jefe le pide a usted preparar la respuesta al oficio. El oficio llegó esta mañana, el término del expediente corre y la delegada insiste en que necesita el informe «con conclusión jurídica incluida» para decidir la próxima semana.',
  '¿Qué corresponde responder sobre el alcance del apoyo?',
  ['Aceptar la solicitud completa, porque la delegada es la dependencia competente y puede definir el contenido del informe técnico que requiere para sustentar su decisión en el expediente.',
   'Rechazar la solicitud en su totalidad, porque incluir una petición improcedente vicia el requerimiento y obliga a la delegada a presentarlo nuevamente en debida forma ante la Dirección.',
   'Atender el apoyo técnico y precisar que el informe se limitará a hechos, metodología y resultados, porque calificar la falta corresponde al funcionario competente del expediente.',
   'Atender la solicitud y emitir la calificación pedida, siempre que el informe advierta que se trata de una opinión técnica que no vincula a la delegada al momento de adoptar su decisión.'],
  'El informe técnico aporta hechos, método y resultados verificables. Calificar la falta es una valoración jurídica que corresponde a quien instruye y decide: incluirla contamina el producto técnico.',
  'Ni aceptar la calificación, ni rechazar todo el requerimiento, ni emitirla «como opinión no vinculante».'),

 (0,
  'Un servidor de otra dependencia le comenta que la Procuraduría «ya no puede investigar a nadie» después de la Ley 2094 de 2021, porque «todo pasó a la justicia». Otro sostiene que la reforma no cambió nada. Usted debe precisar el punto antes de continuar con el apoyo técnico de un expediente disciplinario en curso. El servidor insiste delante del equipo y pide que se suspenda el apoyo técnico hasta aclarar el punto.',
  '¿Cuál es el efecto central de la Ley 2094 de 2021 sobre la función disciplinaria de la PGN?',
  ['La PGN conserva la función disciplinaria y la reforma reforzó las garantías: separó instrucción y juzgamiento, garantizó la doble conformidad y previó control judicial de las decisiones.',
   'La función disciplinaria pasó íntegramente a la Fiscalía General de la Nación, de modo que la Procuraduría conserva solo las funciones preventiva y de intervención ante autoridades.',
   'La reforma no produjo ningún cambio: la Procuraduría sigue concentrando instrucción y juzgamiento en el mismo funcionario y sin previsión de control judicial sobre sus decisiones.',
   'La reforma eliminó la posibilidad de sancionar a cualquier servidor público, de modo que las actuaciones disciplinarias en curso deben archivarse por pérdida de competencia sancionatoria.'],
  'La Ley 2094 de 2021 ajustó el procedimiento a los estándares interamericanos: separación entre quien instruye y quien juzga, doble conformidad frente a la sanción y control judicial de ciertas decisiones. La competencia disciplinaria se mantiene.',
  'La función no pasó a la Fiscalía, la reforma sí cambió el procedimiento y no eliminó la potestad sancionatoria.'),

 (1,
  'El equipo recibe una solicitud de apoyo de la Defensoría del Pueblo. Un servidor sostiene que la División de Gestión Humana solo puede apoyar a dependencias de la Procuraduría y que la solicitud debe devolverse; otro cree que debe tramitarse como si viniera de una entidad externa, mediante convenio. La solicitud viene firmada por un defensor regional, describe el objeto del apoyo y la Dirección debe responder esta semana si lo asume o no.',
  '¿Qué dice el artículo 10 sobre el alcance del apoyo técnico-científico?',
  ['El apoyo se limita a las dependencias de la Procuraduría, de modo que cualquier solicitud externa debe devolverse e indicarle a la entidad que contrate un perito particular.',
   'El apoyo se presta a las demás dependencias de la PGN y también a los otros órganos del Ministerio Público, de modo que una solicitud de la Defensoría del Pueblo tiene cabida.',
   'El apoyo puede prestarse a cualquier entidad del Estado que lo solicite, siempre que medie un convenio interadministrativo que defina las condiciones técnicas y económicas del servicio.',
   'El apoyo solo procede cuando el Procurador General lo autoriza expresamente para cada solicitud, incluso si proviene de una dependencia interna de la propia Procuraduría General.'],
  'El numeral 2 del artículo 10 menciona expresamente a las demás dependencias de la PGN y a los demás órganos del Ministerio Público, que son la Defensoría del Pueblo y las personerías.',
  'No se limita a la PGN, no se extiende a cualquier entidad mediante convenio y no exige autorización caso por caso.'),

 (3,
  'En una discusión sobre la estructura territorial, un servidor afirma que las procuradurías judiciales «son juzgados especializados de la Procuraduría». Otro sostiene que son lo mismo que las provinciales, solo que con otro nombre. La precisión importa porque el equipo debe remitir una parte del asunto a la dependencia que corresponde y una confusión obligaría a repetir el trámite completo.',
  '¿Cuál es la precisión correcta sobre las procuradurías judiciales?',
  ['Son juzgados especializados dentro de la estructura de la Procuraduría, con competencia para decidir los procesos disciplinarios de mayor complejidad en cada distrito judicial del país.',
   'Son equivalentes a las procuradurías provinciales y la diferencia es solo de denominación histórica, pues ambas adelantan los mismos procesos disciplinarios en su respectiva jurisdicción.',
   'Son dependencias del Consejo Superior de la Judicatura adscritas funcionalmente a la Procuraduría para efectos del control disciplinario de los funcionarios de la rama judicial.',
   'Son dependencias de la PGN que ejercen la función de intervención ante las autoridades judiciales, actuando como agentes del Ministerio Público en los procesos que la ley señala.'],
  'Las procuradurías judiciales ejercen la intervención ante jueces y tribunales como agentes del Ministerio Público. No juzgan, no son provinciales con otro nombre y no pertenecen a la rama judicial.',
  'No son juzgados, no equivalen a las provinciales y no dependen del Consejo Superior de la Judicatura.'),

 (2,
  'El jefe de la División le encarga adelantar el trámite de un encargo que debe quedar surtido hoy. Al revisar, usted encuentra que falta el certificado de antecedentes disciplinarios del servidor. La persona se niega a aportarlo «porque eso lo consigue la entidad» y el jefe de su dependencia presiona para que el encargo quede en firme antes de las cinco. Un compañero sugiere proyectar y firmar el acto usted mismo «para no frenar el servicio» y otro, dar por cumplido el requisito y anexar el certificado después. El jefe de la División no contesta el teléfono en ese momento.',
  '¿Cuál es el alcance correcto de su rol en ese momento?',
  ['El encargo que le hizo el jefe lo habilita a firmar el acto en su ausencia, porque quien recibe un trámite para adelantarlo recibe con él la facultad de cerrarlo cuando la urgencia del servicio lo exige.',
   'Puede dar por cumplido el requisito y dejar constancia de que el certificado se anexará después, poniéndolo luego en conocimiento del jefe para que lo valide cuando regrese.',
   'Puede verificar, requerir el soporte y dejar el acto proyectado con la constancia de lo que falta; declarar cumplido el requisito o firmar el acto no está en sus manos y debe informarlo al competente.',
   'El trámite debe suspenderse por completo y devolverse al jefe de la dependencia solicitante, porque mientras el servidor no aporte el certificado no hay actuación posible ni constancia que dejar.'],
  'Su función es <strong>preparar, verificar y proyectar</strong> (funciones 1 y 3 del manual): puede requerir el soporte —que, además, la entidad sí puede consultar— y dejar el acto listo con la constancia de lo que falta. Pero <strong>declarar cumplido</strong> un requisito sin soporte y <strong>firmar</strong> el acto son del competente, y asumirlo expondría el encargo a nulidad.',
  'Ni firmar en ausencia del jefe, ni dar por cumplido lo que no está acreditado, ni paralizar el trámite sin dejar nada: se verifica, se requiere, se deja el proyecto con su constancia y se informa.'),
]
