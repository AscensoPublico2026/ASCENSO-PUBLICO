# -*- coding: utf-8 -*-
"""Día 5 · Estructura y funciones de la PGN y la DNIE — Técnico Investigador 4TI-15."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-PGN-4TI15O-01',
    archivo='FUN-PGN-4TI15O-01-estructura-pgn-investigaciones-especiales.html',
    dia=5,
    titulo_doc='Estructura y Funciones de la PGN y la DNIE',
    h1='Estructura y Funciones de la PGN<br>y la Dirección Nacional de Investigaciones Especiales',
    kicker='Día 5 · Conocimientos comunes',
    sub='La <strong>estructura, organización y funciones de la Procuraduría General de la Nación</strong> es un conocimiento común exigido por el formato de convocatoria. Aquí verás qué es la PGN y de dónde viene su autoridad, sus <strong>tres funciones misionales</strong> (preventiva, disciplinaria y de intervención), el <strong>poder disciplinario preferente</strong>, la estructura del nivel central y de las procuradurías territoriales, las dependencias de apoyo y, con detalle propio, la <strong>Dirección Nacional de Investigaciones Especiales</strong>: qué es, de quién depende, qué funciones le asigna el <strong>artículo 10 del Decreto Ley 262 de 2000</strong> y por qué es la dependencia donde se ubica el <strong>Técnico Investigador 4TI-15</strong>.',
    badges=['⏱ 95-115 min', '🏛️ Régimen PGN', '🔬 DNIE'],
    fmeta='Estructura y Funciones de la PGN y la Dirección Nacional de Investigaciones Especiales (Decreto Ley 262 de 2000)',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Estructura de la PGN y la DNIE',
)

SEC = secciones_mapeadas('guias/FUN-PGN-6CI04-01-estructura-funciones-pgn.html')

MOD6 = '''<div class="modulo-head"><div class="modulo-n">6</div><h3>La Dirección Nacional de Investigaciones Especiales: tu dependencia</h3></div>
    <div class="b-texto">
      <p>Este módulo merece atención especial porque describe <mark>la dependencia donde se ubica tu cargo</mark>. La <strong>Dirección Nacional de Investigaciones Especiales (DNIE)</strong> está regulada en el <strong>artículo 10 del Decreto Ley 262 de 2000</strong> y pertenece al <strong>nivel central</strong> de la entidad, adscrita al <strong>Despacho del Procurador General</strong>. Esa ubicación no es un dato decorativo: explica de quién recibe las asignaciones, ante quién responde y por qué sus actuaciones pueden alcanzar cualquier territorio del país.</p>
      <div class="def-panel"><span class="def-label">Concepto</span><p>La <strong>DNIE</strong> es la dependencia de la Procuraduría que adelanta las indagaciones e investigaciones disciplinarias que le asigna o delega el Procurador General, presta <strong>asesoría y apoyo técnico-científico</strong> a las demás dependencias de la entidad y a los otros órganos del Ministerio Público, y <strong>ejerce funciones de policía judicial</strong>.</p></div>
      <h4>Las funciones del artículo 10, una por una</h4>
      <div class="tabla-wrap"><table>
        <tr><th>#</th><th>Función</th><th>Qué significa en la práctica</th></tr>
        <tr><td>1</td><td>Adelantar las <strong>indagaciones preliminares e investigaciones disciplinarias</strong> que le asigne o delegue el Procurador General.</td><td>La DNIE no escoge sus casos: los recibe por asignación o delegación del Procurador General.</td></tr>
        <tr><td>2</td><td>Prestar <strong>asesoría y apoyo técnico-científico</strong> a las dependencias de la PGN y a los demás órganos del Ministerio Público.</td><td>Aquí entra tu cargo: una delegada, una regional o una provincial pide apoyo y la Dirección lo asigna.</td></tr>
        <tr><td>3</td><td><strong>Informar periódicamente</strong> al Procurador General sobre el estado de las investigaciones, y de inmediato cuando la gravedad de los hechos lo exija.</td><td>La información fluye hacia arriba con corte periódico y con alertas cuando el caso lo amerita.</td></tr>
        <tr><td>4</td><td><strong>Coordinar las seccionales</strong> regionales que llegue a crear el Procurador General.</td><td>Permite desplegar la capacidad técnica fuera de Bogotá cuando se decida crearlas.</td></tr>
        <tr><td>5</td><td><strong>Ejercer funciones de policía judicial</strong> y participar, previa designación del Procurador General, en <strong>comisiones conjuntas</strong> con la Fiscalía, funcionarios judiciales, la Contraloría y otros funcionarios con funciones de policía judicial.</td><td>Es el fundamento de la función 5 de tu manual: practicar pruebas técnicas asegurando los elementos, previa delegación.</td></tr>
        <tr><td>6</td><td>Las demás funciones que le <strong>asigne o delegue</strong> el Procurador General.</td><td>Cláusula de cierre: siempre dentro del marco de la Dirección.</td></tr>
      </table></div>
      <div class="ojo"><b>Ojo en la prueba:</b> hay dos ideas que conviene no mezclar. La DNIE <mark>investiga</mark> cuando el Procurador General se lo asigna o delega, y además <mark>apoya técnicamente</mark> a otras dependencias que conservan su propio caso. En el segundo escenario —el más frecuente para un técnico investigador— la Dirección no se queda con el expediente: aporta la prueba técnica y la entrega a quien pidió el apoyo.</div>
      <h4>Cómo llega el trabajo a tus manos</h4>
      <div class="flujo">
        <div class="flujo-item"><strong>1. Solicitud</strong><br>Una dependencia (delegada, regional, provincial o la propia Dirección) requiere apoyo técnico para un expediente</div>
        <div class="flujo-item"><strong>2. Asignación</strong><br>La Dirección asigna el apoyo a un servidor de la especialidad que el caso exige</div>
        <div class="flujo-item"><strong>3. Metodología</strong><br>Se acuerda con la dependencia qué se busca, con qué técnica y en qué orden</div>
        <div class="flujo-item"><strong>4. Práctica</strong><br>Se practica la prueba técnica y se aseguran los elementos con cadena de custodia</div>
        <div class="flujo-item"><strong>5. Informe</strong><br>Se elabora el informe técnico y se presenta con sus anexos a quien pidió el apoyo</div>
      </div>
      <div class="practica">
        <div class="practica-head">🗂️ En la práctica</div>
        <div class="practica-body">
          <p>Una Procuraduría Provincial investiga a un servidor por el manejo irregular de unos bienes y pide apoyo técnico. La DNIE asigna el caso. El técnico investigador acuerda la metodología con la Provincial, realiza la verificación, asegura los elementos recaudados con su registro de cadena de custodia y entrega el informe técnico con sus anexos <strong>a la Provincial</strong>, que es la dependencia que conserva el expediente y la que decidirá. La DNIE aportó la técnica; la decisión sigue siendo de quien instruye.</p>
        </div>
      </div>
      <h4>La Procuraduría Auxiliar para Asuntos Disciplinarios</h4>
      <p>Junto a la DNIE conviene conocer la <strong>Procuraduría Auxiliar para Asuntos Disciplinarios</strong>, que apoya y coordina aspectos específicos del ejercicio de la función disciplinaria dentro de la entidad. No la confundas con la Dirección: la Auxiliar acompaña la función disciplinaria en su conjunto, mientras la DNIE investiga por asignación y aporta la capacidad técnico-científica y de policía judicial.</p>
      <div class="acordeon">
        <details class="acc"><summary>🔎 ¿Por qué una dependencia nacional de investigaciones especiales?</summary><div class="acc-body"><p>Algunos procesos disciplinarios exigen recursos de investigación que una dependencia territorial no tiene: análisis técnicos, verificaciones en terreno, aseguramiento de evidencia con cadena de custodia, trabajo conjunto con otras autoridades. Concentrar esa capacidad en una dirección del nivel central permite un manejo riguroso y homogéneo en todo el país, y poner esa capacidad al servicio de cualquier dependencia que la necesite.</p></div></details>
        <details class="acc"><summary>🔎 ¿La DNIE puede actuar con otras autoridades?</summary><div class="acc-body"><p>Sí. El numeral 5 del artículo 10 prevé que, <strong>previa designación del Procurador General</strong>, participe en comisiones que investiguen conjuntamente con la Fiscalía General de la Nación, con funcionarios judiciales, con la Contraloría y con otros servidores que tengan funciones de policía judicial. Es trabajo coordinado, no absorción de competencias: cada autoridad conserva la suya.</p></div></details>
      </div>
      <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> la Dirección Nacional de Investigaciones Especiales es una dependencia del nivel central adscrita al Despacho del Procurador General (art. 10 del Decreto Ley 262 de 2000). Adelanta las investigaciones que le asignan o delegan, presta apoyo técnico-científico a las dependencias de la PGN y a los demás órganos del Ministerio Público, informa al Procurador General, coordina las seccionales que se creen, ejerce funciones de policía judicial y participa en comisiones conjuntas previa designación. Es la dependencia donde se ubica el Técnico Investigador 4TI-15.</p></div>
    </div>
  </div>

  '''

MOD7 = '''<div class="modulo-head"><div class="modulo-n">7</div><h3>Dónde encaja el Técnico Investigador en este mapa institucional</h3></div>
    <div class="b-texto">
      <p>Con el mapa completo, ubiquemos tu cargo. El <strong>Técnico Investigador 4TI-15</strong> es un empleo del <strong>nivel técnico</strong> adscrito a la <strong>Dirección Nacional de Investigaciones Especiales</strong>, con ubicación inicial en Bogotá y vinculado al <strong>proceso disciplinario</strong>. Su propósito, según el manual, es <mark>apoyar las actividades técnicas, técnico científicas y administrativas de investigación para la recolección de material probatorio</mark> que soporte las investigaciones de la entidad.</p>
      <p>Dicho de otro modo: de las tres funciones misionales de la PGN, tu cargo trabaja sobre todo para la <strong>disciplinaria</strong>, y lo hace aportando algo que las demás dependencias no siempre tienen: <strong>capacidad técnica para producir y asegurar prueba</strong>. Cuando una delegada necesita verificar un dato que exige método, cuando hay que asegurar unos documentos con cadena de custodia o cuando se requiere un informe que resista la contradicción del investigado, ahí entra el técnico investigador.</p>
      <div class="tabla-wrap"><table>
        <tr><th>Función misional</th><th>¿Participa el Técnico Investigador?</th><th>Cómo</th></tr>
        <tr><td><strong>Disciplinaria</strong></td><td>Sí, de manera principal</td><td>Practica pruebas técnicas, recauda y asegura elementos, elabora informes y proyecta documentos para la firma del competente.</td></tr>
        <tr><td><strong>Preventiva</strong></td><td>De manera indirecta</td><td>El apoyo técnico puede sustentar actuaciones preventivas de otras dependencias cuando así se le solicite.</td></tr>
        <tr><td><strong>De intervención</strong></td><td>No</td><td>La intervención ante autoridades judiciales y administrativas la ejercen los agentes del Ministerio Público designados para ello.</td></tr>
      </table></div>
      <h4>La línea de trabajo: quién pide, quién asigna, quién decide</h4>
      <div class="flujo">
        <div class="flujo-item"><strong>Procurador General</strong><br>Asigna o delega las investigaciones y designa para comisiones conjuntas</div>
        <div class="flujo-item"><strong>Director Nacional</strong><br>Dirige la Dirección, distribuye el trabajo y delega las funciones de policía judicial</div>
        <div class="flujo-item"><strong>Técnico Investigador ★</strong><br>Acuerda metodología, practica la prueba técnica, asegura elementos e informa</div>
        <div class="flujo-item"><strong>Dependencia solicitante</strong><br>Recibe el informe con sus anexos y adopta la decisión dentro de su expediente</div>
      </div>
      <div class="box ok">
        <div class="box-title">✅ Tu aporte es decisivo, y tiene un límite claro</div>
        <p>La calidad de la prueba que usted recaude determina si un caso se sostiene o se cae. Pero su trabajo termina en el <strong>informe técnico</strong>: no califica la falta, no gradúa la sanción, no declara responsabilidades y no firma la decisión de fondo. Ese límite no le resta importancia: es lo que mantiene su producto dentro del terreno técnico, que es precisamente donde tiene valor.</p>
      </div>
      <div class="ojo"><b>Ojo en la prueba:</b> muchas preguntas situacionales de este perfil ponen a prueba exactamente esa frontera. Cuando una opción propone que el técnico <mark>califique, decida, sancione o capture</mark>, casi siempre es incorrecta, por muy eficaz que parezca. La conducta esperada es documentar, asegurar, informar y dejar la decisión a quien le corresponde.</div>
      <div class="acordeon">
        <details class="acc"><summary>🔎 ¿Qué significa que el empleo sea de planta global?</summary><div class="acc-body"><p>Que la ubicación inicial —Bogotá, en la DNIE— no es inamovible. Conforme al numeral 34 del artículo 7 del Decreto Ley 262 de 2000, los cargos de la planta globalizada pueden ser distribuidos y reubicados en diferentes especialidades, sedes y dependencias según las necesidades del servicio, en cualquier tiempo durante el período de prueba o después de cumplido. El formato de convocatoria lo advierte expresamente.</p></div></details>
        <details class="acc"><summary>🔎 ¿El técnico investigador trabaja solo con la DNIE?</summary><div class="acc-body"><p>Trabaja <em>desde</em> la DNIE, pero su cliente interno cambia con cada caso: puede ser una Procuraduría Delegada, una Regional, una Provincial o la propia Dirección. Por eso la función 2 del manual habla de prestar apoyo «a las dependencias que lo soliciten». Esa es también la razón por la que debe entender la estructura completa de la entidad: para saber quién le pide, con qué competencia y a quién debe entregar el resultado.</p></div></details>
      </div>
    </div>
        <div class="box info"><div class="box-title">🧭 Síntesis del módulo</div><p><strong>Síntesis del módulo:</strong> el Técnico Investigador 4TI-15 pertenece al nivel técnico y trabaja desde la Dirección Nacional de Investigaciones Especiales para la función disciplinaria de la entidad. Su aporte es la prueba técnica: acuerda la metodología con quien pide el apoyo, practica, asegura los elementos con cadena de custodia, elabora el informe y proyecta documentos para la firma del funcionario competente. No califica la falta ni decide el fondo, y su empleo pertenece a la planta global, de modo que puede ser reubicado según las necesidades del servicio.</p></div>
  </div>

  '''

R = [
    ('dónde encaja el trabajo del Citador</mark> dentro de esa enorme maquinaria institucional. Con ese mapa claro, cada oficio que repartas y cada diligencia que hagas tendrán sentido dentro de un todo que entiendes, no solo direcciones sueltas que memorizas.',
     'dónde encaja el trabajo del Técnico Investigador</mark> dentro de esa enorme maquinaria institucional. Con ese mapa claro, cada apoyo técnico que prestes y cada diligencia que practiques tendrán sentido dentro de un todo que entiendes, y no serán tareas sueltas que ejecutas sin ver el conjunto.'),
    ('Dónde encaja exactamente el <strong>Citador</strong> en esta estructura, y por qué su labor conecta a todas las dependencias entre sí y con el ciudadano.',
     'Dónde encaja exactamente el <strong>Técnico Investigador</strong> en esta estructura, y por qué la Dirección Nacional de Investigaciones Especiales presta su capacidad técnica a todas las dependencias.'),
    ('La prueba evalúa este tema porque un Citador que confunde una Procuraduría Delegada Disciplinaria con una Preventiva, o que no sabe qué hace la División de Documentación, dif',
     'La prueba evalúa este tema porque un Técnico Investigador que confunde una Procuraduría Delegada Disciplinaria con una Preventiva, o que no sabe de quién depende su propia Dirección, dif'),
    ('Tu cargo de Citador pertenece, precisamente, a ese engranaje de apoyo: no decides en ninguna de las tres funciones misionales, pero tu trabajo de cor',
     'Tu cargo de Técnico Investigador pertenece, precisamente, a la función disciplinaria: no decides el fondo de ninguna actuación, pero tu trabajo de cor'),
    ('compites por el cargo de Citador, código y grado <strong>6CI-04</strong>, nivel jerárquico Operativo',
     'compites por el cargo de Técnico Investigador, código y grado <strong>4TI-15</strong>, nivel jerárquico Técnico'),
    ('Citador', 'Técnico Investigador'),
    ('6CI-04', '4TI-15'),
    ('90-2026', '257-2026'),
]
SEC = aplicar_todas(SEC, R, estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)   # filtro antifugas final

partes = SEC[2].split('<div class="modulo">')
assert len(partes) == 10, f'se esperaban 10 bloques y hay {len(partes)}'
partes[6] = MOD6
partes[7] = MOD7
SEC[2] = '<div class="modulo">'.join(partes)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre la estructura y '
              'las funciones de la Procuraduría y de la Dirección Nacional de Investigaciones Especiales. Los contextos '
              'son extensos y las cuatro opciones son plausibles. Al seleccionar una opción verás si acertaste y la explicación.')

P = [
 (1,
  'Una Procuraduría Provincial adelanta una investigación disciplinaria y necesita verificar técnicamente unos registros que la entidad investigada entregó en medio digital. El procurador provincial llama a la Dirección Nacional de Investigaciones Especiales y pide apoyo. En la dependencia hay dudas: un servidor sostiene que, al pedir apoyo, la Provincial pierde el expediente y la DNIE asume la investigación completa; otro cree que la DNIE debe negarse porque el caso no se lo asignó el Procurador General.',
  '¿Cuál es la lectura correcta del papel de la DNIE en ese escenario?',
  ['La Provincial pierde la competencia al solicitar el apoyo: desde ese momento la Dirección asume la investigación, adopta las decisiones del expediente y responde por su resultado final.',
   'La DNIE presta asesoría y apoyo técnico-científico a las dependencias que lo soliciten (num. 2 del art. 10): aporta la prueba técnica y la entrega, y la Provincial conserva su expediente.',
   'La DNIE debe negarse porque solo puede actuar en las investigaciones que le asigne o delegue el Procurador General, de modo que el apoyo técnico a otras dependencias excede sus funciones.',
   'La DNIE debe remitir la solicitud a la Procuraduría Auxiliar para Asuntos Disciplinarios, que es la dependencia encargada de coordinar el apoyo entre las distintas áreas de la entidad.'],
  'El numeral 2 del artículo 10 del Decreto Ley 262 de 2000 asigna a la DNIE prestar asesoría y apoyo técnico-científico a las demás dependencias de la PGN y a los otros órganos del Ministerio Público. El apoyo no traslada la competencia: el expediente sigue en la Provincial.',
  'Ni la Provincial pierde el caso, ni la DNIE debe negarse, ni el apoyo se canaliza por la Procuraduría Auxiliar.'),

 (3,
  'Un practicante pregunta de quién depende la Dirección Nacional de Investigaciones Especiales. Un servidor responde que de la Procuraduría Delegada para la Fuerza Pública, porque «maneja temas de policía judicial»; otro, que es una entidad adscrita con autonomía administrativa y presupuestal propia; y un tercero, que depende del Instituto de Estudios del Ministerio Público.',
  'Conforme al Decreto Ley 262 de 2000, ¿cuál es la ubicación correcta de la DNIE?',
  ['Depende de la Procuraduría Delegada para la Fuerza Pública, porque las funciones de policía judicial de la entidad se concentran en esa delegada y de allí se distribuyen a las demás áreas.',
   'Es una entidad adscrita a la Procuraduría, con personería jurídica, autonomía administrativa y presupuesto propio, lo que le permite definir por sí misma las investigaciones que adelanta.',
   'Depende del Instituto de Estudios del Ministerio Público, que es el encargado de la formación y de la investigación científica aplicada dentro de la estructura de la entidad.',
   'Es una dependencia del nivel central adscrita al Despacho del Procurador General, de quien recibe las asignaciones y delegaciones y ante quien informa sobre el estado de las investigaciones.'],
  'La DNIE está en el nivel central, en el Despacho del Procurador General. Esa dependencia directa explica que reciba de él las asignaciones, las delegaciones y las designaciones para comisiones conjuntas, y que le informe periódicamente.',
  'No depende de una delegada sectorial, no es una entidad con personería propia y no pertenece al IEMP.'),

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
   'El control fiscal preferente, que permite a la Procuraduría asumir las investigaciones de la Contraloría cuando esta no actúa con la diligencia debida en los casos de mayor impacto.',
   'La función de intervención, que faculta a la Procuraduría para comparecer dentro del proceso disciplinario interno de la entidad como sujeto procesal con facultades de impulso.',
   'La vigilancia administrativa ordinaria, que obliga a la entidad a remitir el expediente a la Procuraduría cuando la actuación supera los dos años sin decisión de fondo del asunto.'],
  'El poder disciplinario preferente del artículo 277 numeral 6 permite a la PGN asumir el conocimiento de procesos que adelantan las oficinas de control interno disciplinario, con la motivación que corresponda.',
  'No existe un control fiscal preferente de la PGN, la intervención no opera dentro del proceso disciplinario interno y no hay remisión automática por el paso del tiempo.'),

 (1,
  'Al preparar una actuación conjunta, surge la pregunta de si el equipo de la DNIE puede trabajar con la Fiscalía en una misma diligencia. Un servidor sostiene que está prohibido porque son autoridades distintas; otro, que puede hacerse siempre que el Director lo autorice internamente; y un tercero, que la PGN quedaría subordinada a la Fiscalía durante esa actuación.',
  'Conforme al numeral 5 del artículo 10 del Decreto Ley 262 de 2000, ¿qué es lo correcto?',
  ['Está prohibido: cada autoridad debe practicar sus propias diligencias por separado, de modo que la actuación conjunta vicia lo recaudado y compromete la autonomía de los órganos.',
   'La DNIE puede participar en comisiones que investiguen conjuntamente con la Fiscalía y otras autoridades, previa designación del Procurador General, conservando cada entidad su competencia.',
   'Puede hacerse con la sola autorización interna del Director Nacional, porque la coordinación operativa entre autoridades es un asunto administrativo que no requiere designación superior.',
   'Puede hacerse, pero durante la comisión la Procuraduría queda subordinada a la dirección de la Fiscalía, que es la autoridad titular de la acción penal y dirige la investigación conjunta.'],
  'El numeral 5 prevé expresamente la participación en comisiones conjuntas con la Fiscalía, funcionarios judiciales, la Contraloría y otros servidores con funciones de policía judicial, previa designación del Procurador General. Es coordinación, no subordinación.',
  'Ni está prohibido, ni basta la autorización interna, ni la PGN queda subordinada: se requiere designación del Procurador General y cada autoridad conserva su competencia.'),

 (3,
  'Un servidor nuevo cree que las procuradurías regionales y provinciales «son entidades independientes» y que, por eso, la DNIE no puede prestarles apoyo sin un convenio. Otro sostiene que el apoyo solo procede para las procuradurías delegadas del nivel central. El jefe pide claridad porque acaba de llegar una solicitud de una Provincial. La solicitud llegó firmada por el procurador provincial, con el objeto del apoyo definido, y el término del expediente empieza a correr contra la dependencia solicitante.',
  '¿Cuál es la afirmación correcta?',
  ['Las procuradurías territoriales son entidades independientes y el apoyo entre ellas y el nivel central requiere la celebración previa de un convenio interadministrativo de cooperación.',
   'El apoyo técnico de la DNIE solo procede para las procuradurías delegadas del nivel central, porque son las únicas que pertenecen a la misma estructura orgánica de la Dirección.',
   'El apoyo procede únicamente cuando el Procurador General lo ordena caso por caso, de modo que una solicitud directa de una Provincial debe devolverse sin trámite por falta de competencia.',
   'Las procuradurías territoriales son dependencias de la misma entidad y la DNIE presta apoyo técnico-científico a las dependencias que lo soliciten, sin necesidad de convenio alguno.'],
  'Regionales, distritales y provinciales son dependencias de la PGN desconcentradas en el territorio, no entidades distintas. El numeral 2 del artículo 10 habla de apoyo a «las dependencias» sin restringirlo al nivel central.',
  'No son entidades independientes, el apoyo no se limita a las delegadas y no exige orden caso por caso del Procurador General.'),

 (2,
  'El equipo recibe un expediente y advierte que el investigado es un servidor de una entidad del orden nacional, pero que la queja fue radicada en una Procuraduría Provincial. Un servidor propone practicar de una vez la prueba técnica solicitada para no perder tiempo; otro, devolver la solicitud sin más. El apoyo fue solicitado para la semana entrante y cualquier demora en aclarar el punto obligaría a reprogramar la diligencia con la entidad ya citada.',
  '¿Qué debe verificarse antes de practicar el apoyo técnico?',
  ['Nada en particular: la DNIE presta el apoyo que se le solicite y la verificación de la competencia corresponde exclusivamente a la dependencia que tiene a su cargo el expediente.',
   'Debe verificarse únicamente que el expediente tenga número de radicado y que la solicitud venga firmada por el jefe de la dependencia, requisitos formales suficientes para prestar el apoyo.',
   'Conviene verificar que la solicitud provenga de la dependencia competente y que el objeto del apoyo esté definido, y dejar constancia de cualquier duda, porque una actuación viciada afecta la prueba.',
   'Debe devolverse la solicitud de plano, porque los servidores del orden nacional solo pueden ser investigados por las procuradurías delegadas del nivel central y nunca por una provincial.'],
  'La competencia es presupuesto de validez: una prueba practicada en una actuación adelantada por quien no es competente puede verse afectada. Advertirlo y dejar constancia protege el trabajo técnico y el expediente.',
  'Ni ignorar el punto, ni limitarse a los requisitos formales, ni devolver de plano: se verifica, se advierte y se deja constancia.'),

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
  'Durante una capacitación, un asistente sostiene que el Técnico Investigador «participa en las tres funciones misionales por igual». Otro afirma que no participa en ninguna porque es un cargo de apoyo. El facilitador pide precisión, porque la pregunta suele aparecer en las pruebas de este perfil. El facilitador recuerda que en las pruebas anteriores aparecieron opciones que atribuían al cargo funciones de intervención ante jueces, y que varios aspirantes cayeron en ellas.',
  '¿Cómo se relaciona el cargo con las funciones misionales?',
  ['Participa en las tres por igual, porque el apoyo técnico puede requerirse indistintamente en actuaciones preventivas, disciplinarias y de intervención ante autoridades judiciales.',
   'No participa en ninguna función misional, porque su empleo es de apoyo administrativo y su trabajo se limita a tareas instrumentales dentro de la operación diaria de la dependencia.',
   'Participa principalmente en la función de intervención, porque el informe técnico que elabora se presenta ante autoridades judiciales en defensa del orden jurídico y del patrimonio público.',
   'Participa principalmente en la disciplinaria, aportando prueba técnica; puede apoyar indirectamente lo preventivo, y no ejerce la intervención ante autoridades judiciales.'],
  'El manual vincula el empleo al proceso disciplinario y el propósito es recolectar material probatorio. La intervención ante autoridades la ejercen los agentes del Ministerio Público designados para ello.',
  'Ni las tres por igual, ni ninguna, ni la intervención: el eje es la función disciplinaria.'),

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
  'El equipo recibe una solicitud de apoyo de la Defensoría del Pueblo. Un servidor sostiene que la DNIE solo puede apoyar a dependencias de la Procuraduría y que la solicitud debe devolverse; otro cree que debe tramitarse como si viniera de una entidad externa, mediante convenio. La solicitud viene firmada por un defensor regional, describe el objeto del apoyo y la Dirección debe responder esta semana si lo asume o no.',
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
  'El Director Nacional delega en usted las funciones de policía judicial para practicar una prueba técnica en una entidad. Durante la diligencia, un servidor de la entidad se niega a entregar un equipo y usted considera que podría estar ocultando información. Un compañero sugiere retenerlo por obstrucción y otro, requisar las oficinas para encontrar la información. La diligencia está en curso, hay testigos presentes y el jefe no contesta el teléfono en ese momento.',
  '¿Cuál es el alcance correcto de esa delegación?',
  ['La delegación habilita a practicar cualquier acto urgente de investigación, incluidas requisas y retenciones, porque las funciones de policía judicial no admiten distinciones según el órgano.',
   'La delegación permite retener a quien obstruya la diligencia hasta que entregue lo requerido, dejando constancia escrita del hecho y poniéndolo después en conocimiento de la autoridad.',
   'La delegación habilita a practicar la prueba técnica y asegurar los elementos conforme al procedimiento; la negativa se documenta y se informa, sin asumir facultades penales que no se tienen.',
   'La delegación carece de efectos si no la autoriza previamente un juez de control de garantías, de modo que la diligencia debe suspenderse hasta obtener esa autorización judicial expresa.'],
  'Las funciones de policía judicial de la PGN son especiales y acotadas a la práctica de pruebas dentro de su ámbito. No confieren competencia penal general: no habilitan capturas, retenciones ni requisas por iniciativa propia.',
  'Ni facultades penales plenas, ni retención del renuente, ni suspensión por falta de autorización judicial: se documenta la negativa y se informa.'),
]
