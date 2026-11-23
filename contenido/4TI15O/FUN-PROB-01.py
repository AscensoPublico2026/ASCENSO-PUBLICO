# -*- coding: utf-8 -*-
"""Día 13 · Régimen probatorio disciplinario (Título VI, arts. 147-158 Ley 1952) — 4TI-15."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

META = dict(
    codigo='FUN-PROB-4TI15O-01',
    archivo='FUN-PROB-4TI15O-01-regimen-probatorio-disciplinario.html',
    dia=13,
    titulo_doc='Régimen probatorio disciplinario',
    h1='Régimen probatorio<br>disciplinario',
    kicker='Día 13 · Conocimientos específicos',
    sub='Tu materia, literalmente: el <strong>Título VI de la Ley 1952 de 2019</strong> (arts. 147 a 158). La <strong>necesidad y la carga de la prueba</strong>, la <strong>imparcialidad en su búsqueda</strong>, los <strong>medios de prueba</strong> y la sana crítica, la <strong>libertad probatoria</strong> y sus límites, la <strong>pertinencia, conducencia y utilidad</strong>, la práctica por <strong>comisionado</strong>, la <strong>prueba trasladada</strong>, el <strong>aseguramiento de la prueba</strong> en ejercicio de funciones de policía judicial, el <strong>apoyo técnico</strong> —el artículo que nombra tu trabajo—, la <strong>contradicción</strong>, la <strong>cadena de custodia</strong> y la <strong>inexistencia</strong> de la prueba mal recaudada.',
    badges=['⏱ 110-130 min', '⚖️ Arts. 147-158', '🔍 Prueba'],
    fmeta='Régimen probatorio disciplinario (Ley 1952 de 2019, Título VI, arts. 147 a 158)',
    cargo='Técnico Investigador 4TI-15 (Nivel Técnico)',
    conv='257-2026',
    alerta='Régimen probatorio disciplinario',
)

FUENTE = 'guias/FUN-PROB-3PU17L-01-derecho-probatorio-valoracion.html'
SEC = secciones_mapeadas(FUENTE)

# ---------------------------------------------------------------- módulo nuevo: el mapa del Título VI
MAPA_TITULO_VI = '''<h3><span class="h3-chip">0</span> El mapa del Título VI: los doce artículos que gobiernan tu oficio</h3>
  <p>Antes de entrar en la teoría probatoria conviene fijar el mapa normativo, porque la prueba escrita pregunta por el <strong>número del artículo</strong> tanto como por su contenido. El régimen probatorio del proceso disciplinario es el <strong>Título VI de la Ley 1952 de 2019</strong>, y son doce artículos. Dos de ellos nombran literalmente lo que tú haces.</p>
  <div class="tabla-wrap">
    <table>
      <caption>Título VI, «Pruebas» — Ley 1952 de 2019</caption>
      <thead><tr><th>Art.</th><th>Título</th><th>Qué debes retener</th></tr></thead>
      <tbody>
        <tr><td><strong>147</strong></td><td>Necesidad y carga de la prueba</td><td>Las decisiones se fundan en pruebas legalmente producidas. <mark>La carga de la prueba corresponde al Estado</mark>: el investigado no debe probar su inocencia.</td></tr>
        <tr><td><strong>148</strong></td><td>Imparcialidad del funcionario en la búsqueda de la prueba</td><td>Se investiga <strong>con igual rigor</strong> lo que acredita la falta y lo que la desvirtúa. Se busca la <strong>verdad real</strong>. Caben pruebas de oficio.</td></tr>
        <tr><td><strong>149</strong></td><td>Medios de prueba</td><td>Confesión, testimonio, <strong>peritación</strong>, <strong>inspección disciplinaria</strong> y documentos. Los <strong>indicios</strong> se tienen en cuenta al apreciar. Valoración por <strong>sana crítica</strong>.</td></tr>
        <tr><td><strong>150</strong></td><td>Libertad de pruebas</td><td>La falta y la responsabilidad se demuestran con cualquier medio legalmente reconocido. Libertad de <em>medios</em>, no de <em>métodos</em>.</td></tr>
        <tr><td><strong>151</strong></td><td>Petición y negación de pruebas</td><td>Se niegan las <strong>inconducentes, impertinentes y superfluas</strong>; <strong>no se atienden las practicadas ilegalmente</strong>. El rechazo se motiva.</td></tr>
        <tr><td><strong>152</strong></td><td>Práctica de pruebas por comisionado</td><td>El competente puede <strong>comisionar</strong> a otro servidor o a las personerías. El comisionado no amplía el objeto.</td></tr>
        <tr><td><strong>153</strong></td><td>Práctica de pruebas en el exterior</td><td>Se remite a las normas vigentes sobre pruebas en territorio extranjero.</td></tr>
        <tr><td><strong>154</strong></td><td>Prueba trasladada</td><td>Pruebas válidamente practicadas en otra actuación entran por <strong>copia autorizada</strong>. Los EMP descubiertos por la Fiscalía se admiten <strong>sometidos a contradicción</strong>.</td></tr>
        <tr><td><strong>155</strong></td><td><mark>Aseguramiento de la prueba</mark></td><td>El funcionario competente de la PGN, <strong>en ejercicio de funciones de policía judicial</strong>, toma las medidas necesarias para asegurar los elementos de prueba. <strong>Aquí vive tu cargo.</strong></td></tr>
        <tr><td><strong>156</strong></td><td><mark>Apoyo técnico</mark></td><td>Quien conoce de la actuación puede pedir colaboración técnica <strong>gratuita</strong> a los organismos del Estado. Dentro de la PGN, ese apoyo es la <strong>DNIE</strong>.</td></tr>
        <tr><td><strong>157</strong></td><td>Oportunidad para controvertir la prueba</td><td>Los sujetos procesales pueden controvertirla desde la notificación del auto de apertura o de la orden de vinculación.</td></tr>
        <tr><td><strong>158</strong></td><td><mark>Inexistencia de la prueba</mark></td><td>La recaudada <strong>sin las formalidades sustanciales</strong> o <strong>desconociendo derechos fundamentales</strong> <strong>se tendrá como inexistente</strong>. No «débil»: inexistente.</td></tr>
      </tbody>
    </table>
  </div>
  <h4>Los dos artículos que hay que saber de memoria con su número</h4>
  <p>Si solo pudieras retener dos, serían el <strong>155</strong> y el <strong>158</strong>. El 155 es el fundamento legal de que tú asegures elementos de prueba: lo hace el funcionario competente de la Procuraduría <em>en ejercicio de funciones de policía judicial</em>, que es exactamente la fórmula de tu manual de funciones. El 158 es el precio de hacerlo mal: no una prueba discutible, sino una prueba <strong>inexistente</strong>, que desaparece del expediente junto con el trabajo de todo un día.</p>
  <h4>Inexistencia (art. 158) frente a nulidad de pleno derecho (art. 29 CP): una distinción que se pregunta</h4>
  <p>La Constitución dice, en el artículo 29, que <em>es nula, de pleno derecho, la prueba obtenida con violación del debido proceso</em>. El Código General Disciplinario, en el artículo 158, dice que la prueba recaudada sin formalidades sustanciales o desconociendo derechos fundamentales <em>se tendrá como inexistente</em>. No son fórmulas idénticas y conviene no mezclarlas en una respuesta: la Constitución habla de <strong>nulidad</strong>, el Código de <strong>inexistencia</strong>. El efecto práctico converge —esa prueba no puede fundar ninguna decisión—, pero si una opción atribuye al art. 158 la palabra «nulidad» o al art. 29 la palabra «inexistente», está invirtiendo las fuentes.</p>
  <div class="ojo"><b>👁️ Ojo en la prueba</b><p>Tres pares que la prueba escrita cruza a propósito: <strong>art. 147</strong> (carga del Estado) frente a la idea falsa de que el investigado debe desvirtuar; <strong>art. 152</strong> (comisión, figura procesal) frente a la delegación de funciones de policía judicial; y <strong>art. 158</strong> (inexistencia, Código) frente al <strong>art. 29 CP</strong> (nulidad de pleno derecho, Constitución).</p></div>
  <div class="checkpoint" data-cp="0">
    <div class="cp-q">✋ Punto de control: ¿qué artículo del CGD es el fundamento de que un técnico de la DNIE asegure elementos de prueba?</div>
    <div class="cp-opts">
    <button class="cp-opt" data-ans="0">El art. 149, que enumera los medios de prueba admitidos en el proceso disciplinario.</button>
    <button class="cp-opt" data-ans="1">El art. 155, que dispone que el funcionario competente de la PGN, en ejercicio de funciones de policía judicial, tome las medidas necesarias para asegurar los elementos de prueba.</button>
    <button class="cp-opt" data-ans="0">El art. 158, que establece la inexistencia de la prueba recaudada sin formalidades sustanciales.</button>
    </div>
    <div class="cp-fb"></div>
  </div>

  '''

ROL_TEC = ('<p>Para el <strong>Técnico Investigador 4TI-15</strong> de la DNIE, cuidar la cadena de custodia '
           'significa: documentar quién recolectó el elemento, cuándo, cómo se embaló o resguardó, quién lo tuvo '
           'bajo su control y qué análisis se le hicieron. Cada eslabón debe quedar registrado, y el registro lo '
           'produce usted. Una ruptura en la cadena no siempre ex')

R = [
    ('<h3><span class="h3-chip">1</span> Qué es la prueba y su papel en el proceso</h3>',
     MAPA_TITULO_VI + '<h3><span class="h3-chip">1</span> Qué es la prueba y su papel en el proceso</h3>'),
    ('Para el 3PU-17, cuidar la cadena de custodia significa: documentar quién recolectó el elemento, cuándo, cómo se embaló o resguardó, quién lo tuvo bajo su control y qué análisis se le hicieron. Cada eslabón debe quedar registrado. Una ruptura en la cadena no siempre ex',
     ROL_TEC),
]
SEC = aplicar_todas(SEC, R, estricto=True)
SEC = aplicar_todas(SEC, [
    ('<div class="box ojo"><div class="box-title">👁️ Ojo en la prueba</div>', '<div class="ojo"><b>👁️ Ojo en la prueba</b>'),
    ('<div class="box ojo"><div class="box-title">👀 Ojo en la prueba</div>', '<div class="ojo"><b>👀 Ojo en la prueba</b>'),
    ('Profesional Universitario 3PU-17', 'Técnico Investigador 4TI-15'),
    ('Profesional Universitario, código 3PU-17', 'Técnico Investigador, código 4TI-15'),
    ('Profesional Universitario', 'Técnico Investigador'),
    ('(3PU-17)', '(4TI-15)'), ('3PU-17', '4TI-15'), ('3PU17L', '4TI15O'), ('3PU', '4TI'),
    ('146-2026', '257-2026'),
    ('Procuradurías de Instrucción', 'dependencias que solicitan apoyo técnico'),
    ('Procuraduría de Instrucción', 'Dirección Nacional de Investigaciones Especiales'),
    ('El instructor', 'El servidor que instruye'), ('el instructor', 'el servidor que instruye'),
    ('al instructor', 'al servidor que instruye'), ('del instructor', 'del servidor que instruye'),
    ('un instructor', 'un servidor que instruye'), ('Un instructor', 'Un servidor que instruye'),
    ('instructor', 'servidor que instruye'),
], estricto=False)
SEC = aplicar_todas(SEC, limpieza_rol(), estricto=False)

QUIZ_INTRO = ('Responde estas 15 preguntas de juicio situacional, tipo prueba escrita de la PGN, sobre el régimen '
              'probatorio disciplinario (Título VI de la Ley 1952 de 2019) aplicado al trabajo del Técnico '
              'Investigador: carga de la prueba, imparcialidad en su búsqueda, medios, pertinencia y conducencia, '
              'comisión y delegación, prueba trasladada, aseguramiento, cadena de custodia e inexistencia.')

P = [
 (1,
  'El despacho le delega practicar una prueba técnica. Al rendir el informe, usted documenta que el hecho investigado no pudo acreditarse con el material disponible: la técnica aplicada no arroja un resultado concluyente. El servidor del despacho le dice que, entonces, «lo escriba de forma que al menos quede la sospecha, porque si no el investigado se va libre y todos sabemos lo que pasó». El término vence pasado mañana y usted tiene el borrador listo con el resultado real.',
  '¿Qué principio del régimen probatorio resuelve el caso y cómo debe actuar?',
  ['La libertad probatoria del art. 150 le permite formular el resultado del modo que mejor refleje su convicción técnica, siempre que no afirme hechos que no observó durante la diligencia.',
   'La carga de la prueba corresponde al Estado (art. 147): si el material no alcanza, eso es lo que el informe debe decir, sin insinuaciones; el investigado no tiene que desvirtuar nada.',
   'La sana crítica del art. 149 autoriza a consignar la inferencia que el técnico extrae del conjunto, aunque la técnica aplicada no haya arrojado por sí sola un resultado concluyente.',
   'La imparcialidad del art. 148 obliga a practicar una segunda prueba antes de rendir el informe, de modo que el resultado no dependa de una sola técnica aplicada al material.'],
  'La carga de la prueba corresponde al Estado (art. 147). Si el material no alcanza, el informe lo dice con claridad: el investigado no debe desvirtuar nada, y una insinuación sin soporte es precisamente lo que la carga probatoria prohíbe trasladarle.',
  'Ni la libertad de medios, ni la sana crítica, ni el deber de imparcialidad autorizan a redactar un resultado para que «quede la sospecha». Y decidir practicar otra prueba no le corresponde: eso lo decreta el competente.'),

 (0,
  'Practicando una prueba técnica usted obtiene dos resultados: uno que confirma la hipótesis del despacho y otro que la contradice con igual solidez técnica. El informe debe rendirse mañana. Un compañero le sugiere describir el primero con todo el detalle del método y mencionar el segundo en una línea, «porque el despacho ya tiene su línea y el segundo solo va a generar ruido y devoluciones».',
  '¿Qué exige el artículo 148 del Código General Disciplinario?',
  ['Investigar con igual rigor las circunstancias que acreditan la falta y las que la desvirtúan: los dos resultados se describen con el mismo nivel de detalle y método.',
   'Describir primero el resultado que confirma la hipótesis, por ser el que motivó la actuación, y después el que la contradice, en el orden en que fueron obtenidos durante la diligencia.',
   'Consignar únicamente el resultado que el despacho solicitó verificar, ya que el objeto de la prueba delegada define qué debe contener el informe técnico que se rinde.',
   'Consultar al despacho cuál de los dos resultados prefiere que se desarrolle con mayor detalle, dejando constancia escrita de la orientación que se reciba sobre el punto.'],
  'El art. 148 exige investigar con igual rigor lo que demuestra la falta y lo que la desvirtúa, buscando la verdad real. «Igual rigor» se verifica en el tratamiento: mismo detalle, mismo método, mismo espacio.',
  'Un orden de presentación que privilegia lo favorable, un recorte por el objeto o una consulta sobre «cuál desarrollar» son tres maneras de incumplir el mismo artículo.'),

 (2,
  'El investigado solicitó en sus descargos una prueba técnica sobre un segundo dispositivo y el despacho la decretó. Al delegarle la práctica, el servidor del despacho le dice por teléfono que «con el primero basta, el segundo no aporta nada» y que rinda el informe solo sobre aquel. Usted tiene la delegación escrita, que sí comprende los dos dispositivos, y el término corre. La delegación llegó por correo oficial esta mañana y el dispositivo está bajo custodia de la misma dependencia.',
  '¿Cuál es la actuación correcta?',
  ['Practicar solo el primero conforme a la indicación recibida y consignar en el informe que el segundo se omitió por instrucción verbal del despacho solicitante del apoyo técnico.',
   'Practicar los dos y señalar en el informe que, a su juicio técnico, el segundo dispositivo no aportaba elementos relevantes para el objeto de la prueba decretada por el despacho.',
   'Practicar lo decretado sobre los dos dispositivos y, si existe una razón técnica real para no hacerlo, exponerla por escrito para que el competente resuelva, dejando constancia.',
   'Suspender la práctica y devolver la delegación al despacho para que aclare por escrito el alcance, sin iniciar ninguna actuación mientras esa aclaración no se produzca formalmente.'],
  'La prueba fue decretada y además la pidió la defensa: recortarla de hecho por una indicación verbal equivale a negarla sin motivación, que es justamente lo que el art. 151 prohíbe. Se practica lo decretado y, si hay razón técnica, se expone por escrito.',
  'Omitirla por instrucción verbal es negar sin motivar una prueba de la defensa; valorar si «aportaba» es calificar; y devolver la delegación paraliza una actuación que sí estaba autorizada por escrito.'),

 (3,
  'Un compañero sostiene que, como el art. 150 consagra la libertad de pruebas, la DNIE puede acreditar un hecho «por cualquier vía», incluida una grabación de comunicaciones obtenida sin la autorización que la ley exige, siempre que el contenido sea cierto. El jefe pide precisión porque el punto va a quedar en un documento interno de la Dirección. La duda surgió preparando un documento interno y el jefe quiere la precisión por escrito para todo el grupo de trabajo.',
  '¿Cuál es la precisión correcta?',
  ['Tiene razón: la libertad probatoria del art. 150 permite acreditar la falta con cualquier medio, y la veracidad del contenido sanea el defecto en la forma de obtención del elemento.',
   'Tiene razón parcialmente: la grabación puede incorporarse si se somete a contradicción del investigado, lo que subsana la ausencia de autorización previa para su obtención.',
   'Se equivoca: la libertad de pruebas no existe en el proceso disciplinario, donde la ley exige un medio determinado para cada hecho que pretenda acreditarse en la actuación.',
   'Se equivoca: la libertad opera sobre el medio, no sobre el método; lo recaudado sin formalidades sustanciales o desconociendo derechos fundamentales se tiene como inexistente (art. 158).'],
  'La libertad del art. 150 es de medios, no de métodos. Una grabación es un medio admisible; obtenida sin la autorización legal, el art. 158 la hace inexistente, y la contradicción posterior no subsana el vicio de origen.',
  'Ni la veracidad del contenido ni la contradicción posterior sanean una obtención ilícita; y la libertad probatoria sí existe: lo que no existe es libertad para obtener la prueba como sea.'),

 (1,
  'El despacho le pide que, en su informe técnico sobre un equipo, concluya si el hecho documentado «constituye falta gravísima por uso indebido de bienes del Estado». Usted tiene elementos para describir con precisión el estado del equipo, el método aplicado y lo que el examen arrojó. Un compañero le dice que lo haga, «porque el art. 149 admite la peritación y el perito concluye». El informe se rinde pasado mañana y usted ya tiene redactados el método, los hallazgos y las limitaciones de la técnica.',
  '¿Cuál es la precisión correcta sobre la peritación?',
  ['Su compañero tiene razón: el dictamen pericial del art. 149 incluye la conclusión sobre la calificación del hecho, que es precisamente lo que aporta el conocimiento especializado del perito.',
   'La peritación responde preguntas técnicas —qué muestra el material, con qué método y con qué certeza—, no jurídicas: calificar la falta corresponde al servidor competente, no al perito.',
   'La peritación solo es procedente cuando el competente la decreta expresamente como tal, de modo que un informe técnico de apoyo no constituye peritación y puede incluir conclusiones jurídicas.',
   'La peritación admite conclusiones jurídicas siempre que se formulen como hipótesis y se advierta que no vinculan la decisión que el servidor competente adopte sobre el fondo del asunto.'],
  'El informe técnico se mueve en el terreno de la peritación: dice qué muestra el material, con qué método se estableció y con qué grado de certeza. Cuando cruza a la calificación jurídica deja de ser dictamen y pierde valor justo donde debía tenerlo.',
  'Ni el perito califica, ni el carácter de «apoyo» habilita conclusiones jurídicas, ni formularlas como hipótesis las vuelve admisibles.'),

 (2,
  'La Fiscalía adelanta una investigación penal sobre hechos relacionados con el expediente disciplinario que usted apoya. El despacho quiere incorporar unos elementos materiales probatorios que la Fiscalía descubrió con el escrito de acusación, aunque no se debatieron en juicio. Un compañero afirma que no pueden usarse «porque son de otro proceso y de otra jurisdicción». El expediente penal sigue en curso y el despacho disciplinario tiene un término de instrucción corriendo.',
  '¿Qué dice el régimen de prueba trasladada?',
  ['No pueden incorporarse: la prueba trasladada solo procede entre actuaciones de la misma naturaleza, de modo que un elemento de un proceso penal no sirve en uno disciplinario.',
   'Pueden incorporarse sin ninguna condición adicional, porque fueron recaudados por una autoridad competente dentro de un proceso reglado y gozan de presunción de legalidad.',
   'Pueden trasladarse elementos materiales descubiertos por la Fiscalía aunque no se hayan debatido en juicio, siempre que se sometan a contradicción dentro del proceso disciplinario.',
   'Pueden incorporarse solo después de que el proceso penal termine con sentencia ejecutoriada, momento en el cual la prueba adquiere la firmeza necesaria para ser trasladada.'],
  'El art. 154 permite trasladar pruebas válidamente practicadas en otra actuación mediante copias autorizadas, y admite elementos materiales descubiertos por la Fiscalía aunque no se hayan debatido en juicio, con una condición: que se sometan a contradicción en el proceso disciplinario.',
  'Ni está vedado el traslado entre jurisdicciones, ni entra sin condición alguna, ni hay que esperar a la sentencia penal: la condición es la contradicción.'),

 (0,
  'Al recibir un elemento para examinar, usted advierte que el registro de entrega no identifica quién lo recolectó ni en qué fecha, y que el embalaje no tiene rótulo. La dependencia que lo custodia dice que «siempre se ha entregado así» y que el elemento es sin duda el correcto. El informe debe rendirse en tres días y el examen técnico es posible de practicar. La dependencia no entrega certificación en el acto y su jefe inmediato está fuera de la ciudad hasta mañana.',
  '¿Cuál es la actuación correcta?',
  ['Dejar constancia escrita y detallada de la ruptura documental de la cadena de custodia, informarla al competente y precisar en el informe qué puede y qué no puede sostenerse con ese vacío.',
   'Practicar el examen y rendir el informe sin referirse al punto, dado que la dependencia confirmó la identidad del elemento y el examen técnico pudo realizarse con normalidad.',
   'Rechazar el elemento y devolverlo a la dependencia, porque un elemento sin trazabilidad documental no puede ser objeto de ninguna actuación técnica dentro de la investigación.',
   'Completar el registro de entrega con los datos que la dependencia le indique verbalmente, de modo que la documentación quede regularizada antes de practicar el examen técnico.'],
  'La cadena de custodia garantiza que la prueba valorada es la misma que se recaudó. Ante un eslabón sin registro, lo que corresponde es documentar la ruptura, informarla y precisar el alcance del resultado: ocultarla o completarla de oído la agrava.',
  'Callar el vacío compromete la veracidad; devolver el elemento sin más paraliza una actuación que sí podía adelantarse con el alcance delimitado; y completar el registro con datos de oído crea un documento falso.'),

 (3,
  'El competente comisiona a un servidor de una personería para practicar una prueba en otro municipio y, al mismo tiempo, le delega a usted una prueba técnica en Bogotá sobre el mismo expediente. Un compañero afirma que «comisión y delegación son lo mismo, solo cambia el nombre». El jefe pide la distinción por escrito porque va en un documento interno. Los dos encargos llegaron el mismo día, por escrito, firmados por el mismo servidor competente del despacho.',
  '¿Cuál es la diferencia correcta?',
  ['Son lo mismo en efecto jurídico: ambas trasladan íntegramente la competencia del funcionario que las otorga a quien las recibe, que pasa a actuar como titular de la actuación.',
   'La comisión habilita a practicar cualquier prueba del proceso, mientras la delegación de policía judicial se limita a las pruebas que el delegado considere necesarias para el caso.',
   'La diferencia es de jerarquía: la comisión se otorga a un superior y la delegación a un subalterno, pero el alcance de lo que cada uno puede hacer es exactamente el mismo.',
   'La comisión (art. 152) encarga a otro servidor o a una personería una prueba determinada; la delegación habilita funciones de policía judicial para pruebas técnicas. Ambas son escritas y acotadas a lo encargado.'],
  'Son figuras distintas con un rasgo común decisivo: las dos son derivadas, escritas y acotadas. Ni el comisionado ni el delegado amplían el objeto de lo que se les encargó, y lo que exceda queda expuesto a inexistencia.',
  'Ninguna traslada la titularidad de la actuación, ninguna habilita a practicar «lo que se considere necesario», y la distinción no es de jerarquía sino de figura y de objeto.'),

 (1,
  'Un compañero afirma en una capacitación que, según el artículo 158 del Código General Disciplinario, la prueba obtenida con violación del debido proceso «es nula de pleno derecho». Otro responde que esa expresión es de la Constitución y que el Código usa otra. El jefe pide la precisión exacta porque el punto va en un informe que sale a otra dependencia. El documento sale pasado mañana y el jefe quiere que la cita normativa quede impecable ante la otra dependencia.',
  '¿Cuál es la precisión correcta?',
  ['El art. 158 del Código y el art. 29 de la Constitución usan la misma fórmula, «nula de pleno derecho», de modo que ambas expresiones son intercambiables en cualquier respuesta.',
   'El art. 29 de la Constitución habla de prueba «nula de pleno derecho»; el art. 158 del Código dice que la recaudada sin formalidades sustanciales se tendrá como «inexistente».',
   'El art. 158 del Código habla de nulidad y el art. 29 de la Constitución de inexistencia, por lo que el Código es más exigente que la norma constitucional en materia probatoria.',
   'Ninguna de las dos normas califica la prueba mal obtenida: ambas se limitan a ordenar que el funcionario la aprecie con especial prudencia conforme a las reglas de la sana crítica.'],
  'La Constitución (art. 29) habla de nulidad de pleno derecho; el Código (art. 158), de inexistencia. El efecto converge —esa prueba no funda ninguna decisión—, pero las fórmulas no se intercambian, y la prueba escrita cruza las dos a propósito.',
  'No usan la misma fórmula ni están invertidas, y las dos sí califican la prueba mal obtenida: ninguna se limita a pedir prudencia en la apreciación.'),

 (2,
  'El despacho solicitante le pide apoyo técnico y, al tramitarlo, el área administrativa pregunta si debe gestionarse algún pago o contrato, porque se trata de un servicio especializado. El apoyo lo presta la DNIE a una procuraduría regional dentro de la misma entidad, y el jefe quiere dejar el punto motivado en la respuesta que se enviará. La solicitud llegó por correo oficial y la respuesta debe salir esta semana, firmada por el jefe de la Dirección.',
  '¿Qué dispone el Código sobre el apoyo técnico?',
  ['Que el apoyo técnico entre dependencias requiere un acuerdo interno previo que fije las condiciones y los costos asociados a la prestación del servicio especializado solicitado.',
   'Que el apoyo técnico solo procede cuando la entidad carece de capacidad propia, de modo que debe acreditarse esa carencia antes de solicitarlo a otro organismo del Estado.',
   'Que el servidor que conoce de la actuación puede solicitar la colaboración técnica que estime necesaria a los organismos del Estado, y que esa colaboración es gratuita (art. 156).',
   'Que el apoyo técnico debe canalizarse siempre a través de la Fiscalía General de la Nación, que es la entidad que concentra las capacidades técnico-científicas del Estado.'],
  'El art. 156 permite al servidor que conoce de la actuación pedir la colaboración técnica que considere necesaria a los organismos del Estado, y establece que es gratuita. Dentro de la PGN, ese apoyo técnico es la DNIE.',
  'No hay acuerdo previo ni acreditación de carencia que condicionen el apoyo, y no se canaliza por la Fiscalía: el Código lo prevé directamente y lo declara gratuito.'),

 (0,
  'Usted practica una prueba técnica y, al apreciar el conjunto, advierte que de los hechos documentados se desprende con bastante claridad una conclusión sobre lo que ocurrió. No es un dato que haya medido: es una inferencia que extrae de tres hechos que sí midió. Un compañero le dice que la incluya «porque los indicios son prueba y el art. 149 los admite». El informe debe rendirse en dos días y los tres hechos están medidos, fotografiados y descritos en el acta.',
  '¿Cómo debe tratarse ese razonamiento?',
  ['Consignar con precisión los tres hechos indicadores que usted acreditó y abstenerse de formular la inferencia: los indicios se tienen en cuenta al apreciar las pruebas, y esa apreciación es del competente.',
   'Incluir la inferencia en el informe como conclusión indiciaria, ya que el art. 149 admite expresamente los indicios como medio de prueba dentro del proceso disciplinario.',
   'Incluir la inferencia señalando que se formula con reserva, de modo que el competente disponga del razonamiento técnico sin que la conclusión condicione formalmente su decisión.',
   'Omitir tanto la inferencia como los hechos indicadores, porque mencionar hechos que sugieren una conclusión equivale a formularla de manera implícita en el documento técnico.'],
  'El indicio no es un medio autónomo que usted aporte: usted acredita el hecho indicador y la inferencia la hace quien aprecia las pruebas. Documentar los tres hechos con precisión es exactamente su contribución.',
  'Formular la inferencia —con o sin reserva— es apreciar; y omitir los hechos indicadores priva al competente de los elementos sobre los que esa apreciación debía construirse.'),

 (3,
  'Durante la diligencia, el apoderado del investigado le pide estar presente mientras usted practica la prueba técnica y le anuncia que impugnará el resultado si no se le permite. Usted no tiene instrucción alguna sobre su presencia y el procedimiento técnico que aplicará no la contempla expresamente. La diligencia está en curso y hay un término corriendo. El apoderado insiste en voz alta delante de los demás presentes y el acta todavía no se ha cerrado ni firmado.',
  '¿Cuál es la actuación correcta?',
  ['Permitir su presencia sin más, porque la contradicción es una garantía del investigado y negarla viciaría la prueba que usted está a punto de practicar en la diligencia.',
   'Negar la presencia y continuar, dejando constancia de la solicitud, porque la contradicción se ejerce sobre el resultado del dictamen y no durante su práctica material.',
   'Suspender la diligencia hasta que el competente resuelva la solicitud, para evitar que la prueba quede expuesta a una impugnación posterior por parte de la defensa.',
   'Dejar constancia de la solicitud y del procedimiento aplicado, consultar por el canal al competente sobre la presencia solicitada, y continuar con la prueba conforme a lo que se disponga.'],
  'La oportunidad para controvertir está reconocida (art. 157) pero quién puede estar presente en una diligencia técnica lo define el competente, no el técnico en el momento. Lo correcto es dejar constancia, consultar por el canal y actuar conforme a lo que se disponga.',
  'Decidir por su cuenta que sí o que no resuelve de fondo algo que no le corresponde, y suspender la diligencia por iniciativa propia paraliza una actuación delegada cuando bastaba consultar.'),

 (1,
  'Al revisar un informe técnico que otro servidor rindió, usted advierte que afirma una causa a partir de un método que, según el protocolo, solo permite describir un estado. El informe ya fue remitido, el caso sigue en instrucción y el autor es un compañero cercano. Nadie más lo ha advertido y señalarlo generaría tensión en el grupo. El informe se remitió hace una semana y usted conoce el material porque apoyó la misma diligencia.',
  '¿Qué corresponde hacer, a la luz de la sana crítica?',
  ['No intervenir: la valoración del informe conforme a la sana crítica corresponde al competente, que detectará el exceso cuando aprecie el conjunto del material probatorio.',
   'Poner la observación técnica en conocimiento del superior por escrito, de manera objetiva y referida a la afirmación concreta, para que quien es competente valore su incidencia.',
   'Hablar primero con el compañero para que él mismo rinda una corrección, e informar al superior solo si no lo hace antes de que el despacho adopte una decisión sobre el fondo.',
   'Rendir un informe propio sobre el mismo material con la descripción correcta, de modo que el competente disponga de los dos documentos al momento de valorar la prueba.'],
  'Bajo la sana crítica el peso de un dictamen depende de su consistencia interna: una afirmación que excede lo que el método permite puede sostener una decisión equivocada. Se informa por escrito, objetivamente y referido al punto concreto.',
  'Confiar en que el competente lo detecte deja correr el riesgo; dar primero la oportunidad al compañero también; y rendir un informe sobre material que no le fue delegado excede su rol.'),

 (2,
  'Le delegan asegurar unos elementos en una dependencia donde, según la solicitud, podrían alterarse. Al llegar, el jefe de esa dependencia le dice que no autoriza el ingreso al archivo donde están, que necesita «una orden de juez» y que, mientras tanto, él mismo los resguardará. Usted tiene la delegación escrita del servidor competente de la PGN y el riesgo de alteración es real. La delegación es de hoy, el riesgo fue reportado por escrito y usted está en la sede de la dependencia.',
  '¿Cuál es la actuación correcta?',
  ['Ingresar al archivo amparado en la delegación, ya que el art. 155 habilita a tomar las medidas necesarias para asegurar los elementos y la oposición de un servidor no puede impedirlo.',
   'Aceptar que el jefe de la dependencia resguarde los elementos y dejar constancia de ello, porque así se logra el aseguramiento sin necesidad de forzar el acceso al archivo.',
   'Dejar constancia escrita y detallada de la oposición, del riesgo advertido y de los elementos involucrados, y comunicarlo de inmediato al competente para que disponga lo que corresponda.',
   'Suspender la actuación y archivar la delegación, porque sin autorización de la dependencia que custodia los elementos la medida de aseguramiento carece de eficacia práctica alguna.'],
  'El art. 155 fundamenta el deber de asegurar, pero no convierte al técnico en autoridad para vencer una oposición ni lo habilita a registrar por la fuerza. Lo que protege el caso es documentar la oposición y el riesgo, y comunicarlo de inmediato al competente.',
  'Forzar el acceso excede la delegación; dejar los elementos en manos de quien podría alterarlos desnaturaliza el aseguramiento; y archivar la delegación abandona una actuación que sí tenía vía.'),

 (0,
  'Faltan ocho días para la prueba escrita. En los simulacros usted acierta cuando la pregunta nombra el artículo, pero falla cuando el caso describe la situación sin citarlo: duda entre dos opciones que suenan razonables. Su registro muestra que casi siempre elige la que resuelve el problema práctico y descarta la que documenta y consulta. Lleva un registro de los simulacros resueltos y puede ver exactamente en qué opción cayó cada vez que falló.',
  '¿Cuál es la mejor manera de corregirlo?',
  ['Leer cada caso identificando primero qué regla probatoria está en juego —carga, imparcialidad, licitud, contradicción o aseguramiento— y después qué de eso le corresponde a usted hacer.',
   'Memorizar los doce artículos del Título VI con su número y su título, confiando en que reconocer la norma hará evidente cuál es la conducta correcta en cada caso planteado.',
   'Resolver más simulacros del bloque probatorio hasta que la intuición mejore, dejando el repaso del articulado para los últimos días antes de presentar la prueba escrita.',
   'Concentrarse en los artículos 155 y 158, que son los que más preguntas generan para este cargo, y repasar los demás solo con la tabla del mapa del Título VI de esta guía.'],
  'El error no es de memoria sino de encuadre: casi todos estos casos se resuelven identificando la regla en juego y preguntándose enseguida qué de eso cabe en su rol. Convertirlo en un filtro de dos pasos es lo que hace visible la opción correcta.',
  'Memorizar números no corrige un error de encuadre; repetir simulacros sin cambiar el método repite el error; y concentrarse en dos artículos deja fuera la mayoría de los casos que la prueba plantea.'),
]
