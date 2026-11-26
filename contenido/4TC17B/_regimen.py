# -*- coding: utf-8 -*-
"""Corrige el RÉGIMEN DE CARRERA que heredan las guías de talento humano.

Por qué existe. Las guías de este curso se construyen reutilizando guías
escritas para cargos de la DIAN, que se rigen por la Ley 909 de 2004 y cuyos
concursos los adelanta la CNSC. Los reemplazos de identidad cambian el nombre
del empleo y de la entidad, pero no cambian el RÉGIMEN: quedaban afirmaciones
como «en la Procuraduría, la CNSC es la que organiza el concurso» o «la lista
de elegibles de la CNSC», que son falsas y que además contradicen el eje del
propio curso. La PGN tiene carrera especial (art. 279 de la Constitución y
Decreto Ley 262 de 2000, arts. 183 a 226) y adelanta sus concursos por medio
de su Oficina de Selección y Carrera y su Comisión de Carrera.

Es exactamente lo que la prueba evalúa, y al revés: el distractor típico es
atribuirle el concurso a la CNSC.

Dos clases de corrección:
  1. FALSAS      Afirman que la CNSC administra el concurso, la carrera, la
                 lista de elegibles o las reclamaciones DE LA PGN. Se corrigen.
  2. SIN MATIZ   Son verdaderas del régimen general pero se enuncian como si
                 fueran universales. Se les añade «general», que es lo correcto
                 y además refuerza la distinción que la prueba pregunta.

Las frases que ya contrastan los dos regímenes («la CNSC administra la carrera
general, no la de la PGN») no se tocan: son el contenido que queremos.
"""

# --- 1. Afirmaciones falsas para la PGN -------------------------------------
FALSAS = [
    ('En la Procuraduría, que es una entidad con régimen de carrera administrada por concurso de la CNSC, la mayoría de los empleos profesionales como el tuyo son de carrera.',
     'En la Procuraduría, que tiene <strong>régimen de carrera especial</strong> administrado por la propia entidad (art. 279 de la Constitución y Decreto Ley 262 de 2000), la mayoría de los empleos como el tuyo son de carrera.'),

    ('En la Procuraduría, la CNSC es la que organiza el concurso (incluida la prueba escrita a la que te presentas): define el proceso de selección, las pruebas y el orden de mérito.',
     'En la Procuraduría ese concurso <mark>lo organiza la propia entidad</mark>, no la CNSC: la PGN define el proceso de selección, las pruebas (incluida la prueba escrita a la que te presentas) y el orden de mérito, por medio de su <strong>Oficina de Selección y Carrera</strong> (art. 206 del Decreto Ley 262 de 2000) y de su <strong>Comisión de Carrera</strong>.'),

    ('El <em>concurso</em> que proveerá definitivamente el empleo lo adelanta la <em>CNSC</em>.',
     'El <em>concurso</em> que proveerá definitivamente el empleo lo adelanta <em>la propia Procuraduría</em>, que tiene carrera especial.'),

    ('La calificación y las reclamaciones del concurso las administra la <em>CNSC</em>, no la entidad: la División no puede modificar puntajes ni revisar pruebas.',
     'La calificación y las reclamaciones del concurso las administra la <em>Oficina de Selección y Carrera</em> de la propia Procuraduría, conforme a la convocatoria: la División de Gestión Humana no puede modificar puntajes ni revisar pruebas.'),

    ('Orientas al aspirante sobre el canal y los términos de reclamación ante la CNSC, según la convocatoria',
     'Orientas al aspirante sobre el canal y los términos de reclamación ante la propia Procuraduría, según la convocatoria'),

    ('debe ofertarse a concurso cuando la CNSC lo disponga',
     'debe ofertarse a concurso cuando la entidad lo convoque'),

    ('la única vía es presentarse y superar el concurso que convoque la CNSC',
     'la única vía es presentarse y superar el concurso que convoque la propia Procuraduría'),

    ('el concurso lo adelanta la CNSC, que administra la carrera y hace los procesos de selección',
     'el concurso de la PGN lo adelanta la propia Procuraduría, que administra su carrera especial y hace sus procesos de selección'),

    ('la planeación la hace y publica la entidad; la CNSC administra los concursos sobre esas vacantes',
     'en la PGN la planeación, la convocatoria y los concursos sobre esas vacantes están a cargo de la propia entidad'),

    ('Concurso público de méritos (CNSC)',
     'Concurso público de méritos (en la PGN, de la propia entidad)'),

    # --- FUN-GTH-02
    ('que organiza y adelanta la <mark>Comisión Nacional del Servicio Civil (CNSC)</mark>.',
     'que en las entidades de carrera general organiza y adelanta la <mark>Comisión Nacional del Servicio Civil (CNSC)</mark>. En la Procuraduría, en cambio, lo organiza y adelanta <mark>la propia entidad</mark>, porque tiene carrera especial (art. 279 de la Constitución y Decreto Ley 262 de 2000), por medio de su Oficina de Selección y Carrera y su Comisión de Carrera.'),

    ('lista de elegibles de la CNSC y es nombrado en un empleo de carrera, lo es inicialmente <strong>en período de prueba</strong> (habitualmente de seis meses).',
     'lista de elegibles del concurso y es nombrado en un empleo de carrera, lo es inicialmente <strong>en período de prueba</strong>, que en la PGN es de <strong>cuatro meses</strong> (art. 218 del Decreto Ley 262 de 2000) y en el régimen general de seis.'),

    ('<h4>Concurso CNSC</h4><p>La CNSC convoca, aplica pruebas y evalúa por mérito.',
     '<h4>Concurso PGN</h4><p>La propia Procuraduría convoca, aplica pruebas y evalúa por mérito.'),

    ('La única vía es el concurso de la CNSC; la provisionalidad da, a lo sumo, estabilidad relativa.',
     'La única vía es el concurso que adelanta la propia Procuraduría; la provisionalidad da, a lo sumo, estabilidad relativa.'),

    ('la carrera administrativa y el ingreso por mérito con las listas de elegibles de la CNSC',
     'la carrera administrativa y el ingreso por mérito con las listas de elegibles del concurso'),

    ('el papel de la CNSC, el concurso, las listas de elegibles y el período de prueba',
     'quién adelanta el concurso en la PGN, las listas de elegibles y el período de prueba'),

    ('deben reportarse a la CNSC para una convocatoria',
     'deben reportarse a la Oficina de Selección y Carrera para una convocatoria'),
    ('reportes errados a la CNSC', 'reportes errados'),
    ('proyectas el reporte a la CNSC',
     'proyectas el reporte a la Oficina de Selección y Carrera'),

    ('En la Procuraduría, la CNSC es la que convoca el concurso, define las pruebas (incluida la prueba escrita a la que te presentas), aplica los instrumentos de evaluación y establece el orden de mérito de los aspirantes.',
     'En la Procuraduría es <mark>la propia entidad</mark> la que convoca el concurso, define las pruebas (incluida la prueba escrita a la que te presentas), aplica los instrumentos de evaluación y establece el orden de mérito de los aspirantes, por medio de su Oficina de Selección y Carrera y su Comisión de Carrera.'),
    ('La Ley 909 de 2004 la desarrolla y la CNSC la administra.',
     'La Ley 909 de 2004 desarrolla la carrera general y la CNSC la administra; la de la PGN se rige por el Decreto Ley 262 de 2000 y la administra la propia entidad.'),
    ('dónde consultar las convocatorias de la CNSC',
     'dónde consultar las convocatorias de la Procuraduría'),
    ('prueba escrita de la CNSC', 'prueba escrita de la convocatoria'),

    # --- FUN-CONST-01: enseña bien el art. 130 y lo contradice en seis sitios
    ('por eso organiza el concurso de la Procuraduría',
     'pero el artículo 130 exceptúa expresamente las carreras de carácter especial, y por eso <strong>no</strong> organiza el concurso de la Procuraduría'),
    ('La entidad no administra el concurso ni los puntajes: eso corresponde a la CNSC, órgano autónomo.',
     'En la PGN el concurso y los puntajes los administra la <strong>Oficina de Selección y Carrera</strong> de la propia entidad, no la División de Gestión Humana ni la CNSC.'),
    ('recuerda que la CNSC —no la entidad— maneja los concursos',
     'recuerda que la CNSC maneja los concursos de la carrera general, pero no los de la PGN, que son de la propia entidad (art. 130)'),
    ('la CNSC (autónoma) adelanta los concursos',
     'la CNSC (autónoma) adelanta los concursos de la carrera general, mientras que en la PGN los adelanta la propia entidad'),
    ('órgano autónomo que administra los concursos',
     'órgano autónomo que administra los concursos de la carrera general'),
    ('orientar al canal de reclamación ante la CNSC; la entidad no administra puntajes',
     'orientar al canal de reclamación que fije la convocatoria de la Procuraduría; la División de Gestión Humana no administra puntajes'),
    ('Administra la carrera y adelanta los concursos.',
     'Administra la carrera general y adelanta sus concursos; no las carreras especiales (art. 130).'),
]

# --- 2. Afirmaciones verdaderas del régimen general, enunciadas sin matiz ----
SIN_MATIZ = [
    ('La CNSC convoca y adelanta los concursos de méritos , conforma las listas de elegibles',
     'La CNSC convoca y adelanta los concursos de méritos de la carrera general, conforma las listas de elegibles'),
    ('La CNSC convoca y adelanta los <em>concursos de méritos</em>, conforma las <em>listas de elegibles</em>',
     'La CNSC convoca y adelanta los <em>concursos de méritos de la carrera general</em>, conforma las <em>listas de elegibles</em>'),
    ('la segunda administra la carrera y hace los concursos',
     'la segunda administra la carrera general y hace sus concursos'),
    ('la CNSC administra la carrera y adelanta los concursos',
     'la CNSC administra la carrera general y adelanta sus concursos'),
    ('CNSC concursa y administra carrera', 'CNSC concursa y administra la carrera general'),
    ('la CNSC concursa y administra la carrera', 'la CNSC concursa y administra la carrera general'),
    ('CNSC concursa;', 'CNSC concursa la carrera general;'),
    ('los concursos los adelanta la CNSC; Función Pública fija la política',
     'los concursos de la carrera general los adelanta la CNSC; Función Pública fija la política'),
    ('Comisión Nacional del Servicio Civil; administra y vigila las carreras y adelanta los concursos.',
     'Comisión Nacional del Servicio Civil; administra y vigila la carrera general y adelanta sus concursos. No administra la carrera especial de la PGN.'),
    ('La CNSC convoca y adelanta los <strong>concursos de méritos</strong>, conforma las <strong>listas de elegibles</strong>, administra el registro público de carrera y vigila el cumplimiento de las normas de carrera.',
     'La CNSC convoca y adelanta los <strong>concursos de méritos de la carrera general</strong>, conforma las <strong>listas de elegibles</strong>, administra el registro público de carrera y vigila el cumplimiento de las normas de carrera. No alcanza a las carreras especiales como la de la PGN (art. 130 de la Constitución).'),
    ('CNSC <strong>concursa y administra carrera</strong>',
     'CNSC <strong>concursa y administra la carrera general</strong>'),
    ('Comisión Nacional del Servicio Civil (CNSC)</a> — carrera administrativa y concursos.',
     'Comisión Nacional del Servicio Civil (CNSC)</a> — carrera administrativa general y sus concursos (no la carrera especial de la PGN).'),
    ('listas de elegibles de la CNSC; las',
     'listas de elegibles del concurso de la propia entidad; las'),
    ('propios aplicativos para los',
     'propios aplicativos para los concursos de la carrera general, mientras la PGN usa su propia plataforma (meritoconstruyendoexcelencia.com.co) para los'),
]

TODAS = FALSAS + SIN_MATIZ


# --- 3. Estructura territorial ----------------------------------------------
# La PGN no tiene «direcciones seccionales»: eso es lenguaje de la DIAN, de
# donde vienen las bases. Sus dependencias territoriales son las procuradurías
# regionales, provinciales, distritales y judiciales (Decreto Ley 262 de 2000),
# y el empleo 4TC-17 está en el nivel central, en Bogotá. Decir «la seccional»
# como lugar de trabajo de la aspirante es un error que se nota en la primera
# lectura.
TERRITORIO = [
    ('La Procuraduría General de la Nación tiene nivel central y direcciones seccionales con competencias propias.',
     'La Procuraduría General de la Nación tiene un nivel central y dependencias territoriales —procuradurías regionales, provinciales, distritales y judiciales— con competencias propias.'),
    ('que explica que la Procuraduría tenga un nivel central y direcciones seccionales con competencias propias',
     'que explica que la Procuraduría tenga un nivel central y procuradurías regionales y provinciales con competencias propias'),
    ('una red de direcciones seccionales que ejecutan la gestión en el territorio',
     'una red de procuradurías regionales y provinciales que ejecutan la gestión en el territorio'),
    ('direcciones seccionales', 'procuradurías regionales y provinciales'),
    ('Nivel central y seccionales con competencias repartidas',
     'Nivel central y procuradurías territoriales con competencias repartidas'),
    ('Un director seccional (empleo directivo de libre nombramiento, sin dirección política)',
     'Un procurador regional (empleo directivo de libre nombramiento, sin dirección política)'),
    ('es trasladado a otra seccional', 'es trasladado a otra dependencia'),
    ('de un compañero de otra seccional', 'de un compañero de otra dependencia'),
    ('en el nivel central y otras en la seccional', 'en el nivel central y otras en las procuradurías territoriales'),
    ('corresponde al nivel central y no a la seccional', 'corresponde al nivel central y no a la dependencia'),
    ('no lo resuelves en la seccional "para agilizar"', 'no lo resuelves en tu dependencia "para agilizar"'),
    ('propone resolver en la seccional un asunto', 'propone resolver en tu dependencia un asunto'),
    ('resuelves el asunto en la seccional aunque la competencia sea del nivel central',
     'resuelves el asunto en tu dependencia aunque la competencia sea del nivel central'),
    ('porque si la seccional no puede decidir', 'porque si tu dependencia no puede decidir'),
    ('los vehículos de la seccional', 'los vehículos de la dependencia'),
    ('llegó el lunes 5 a la seccional', 'llegó el lunes 5 a tu dependencia'),
    ('porque la seccional no tiene deber alguno', 'porque tu dependencia no tiene deber alguno'),
    ('que indique que la seccional no es competente', 'que indique que la dependencia no es competente'),
    ('Una empresa radicó en la seccional una reclamación', 'Una empresa radicó en la dependencia una reclamación'),
    ('Dos escritos llegan a la seccional el mismo día', 'Dos escritos llegan a la dependencia el mismo día'),
    ('del ciclo de evaluación de toda la seccional', 'del ciclo de evaluación de toda la dependencia'),
    ('con qué instrumento" en la seccional', 'con qué instrumento" en la dependencia'),
    ('</mark> de la seccional para armar', '</mark> de la dependencia para armar'),
    ('del diagnóstico” de la seccional', 'del diagnóstico” de la dependencia'),
    ('Un equipo de la seccional repite errores', 'Un equipo de la dependencia repite errores'),
    ('reforma a los procesos de la seccional', 'reforma a los procesos de la dependencia'),
    ('evidencias del SG-SST de la seccional', 'evidencias del SG-SST de la dependencia'),
]

# Variantes de cita de una misma norma, para que el curso no la escriba de dos
# formas distintas.
UNIFORMES = [('Acuerdo 02 de 2014', 'Acuerdo 002 de 2014')]

TODAS = TODAS + TERRITORIO + UNIFORMES

# --- 4. Rezagos detectados por scripts/auditar-regimen-carrera.py -----------
REZAGOS = [
    ('su provisión definitiva es por concurso de la CNSC',
     'su provisión definitiva es por el concurso que adelanta la propia Procuraduría'),
    ('hay lista de elegibles vigente de la CNSC para ese empleo',
     'hay lista de elegibles vigente del concurso de la entidad para ese empleo'),
    ('existe lista de elegibles vigente de la CNSC para ese empleo',
     'existe lista de elegibles vigente del concurso de la entidad para ese empleo'),
    ('concurso de la CNSC)', 'concurso de la propia entidad)'),
    ('existe una lista de elegibles vigente de la CNSC para ese mismo empleo',
     'existe una lista de elegibles vigente del concurso de la entidad para ese mismo empleo'),
    ('Existe una lista de elegibles vigente de la CNSC para un empleo de carrera',
     'Existe una lista de elegibles vigente del concurso de la entidad para un empleo de carrera'),
    # Se ancla al punto final para no volver a aplicarse sobre el texto que ya
    # corrigió el par equivalente de FALSAS.
    ('y recuerda que la CNSC maneja los concursos.',
     'y recuerda que la CNSC maneja los concursos de la carrera general, pero no los de la PGN (art. 130).'),
    ('y recuerda que la <strong>CNSC</strong> maneja los concursos.',
     'y recuerda que la <strong>CNSC</strong> maneja los concursos de la carrera general, pero <strong>no</strong> los de la PGN (art. 130).'),
    ('canal de reclamación ante la CNSC y, si procede, sobre la oferta de formación de la ESAP; dejas constancia',
     'canal de reclamación que corresponda —el de la convocatoria de la Procuraduría, si se trata de este concurso— y, si procede, sobre la oferta de formación de la ESAP; dejas constancia'),
    # En la PGN los instrumentos de calificación los adopta su Comisión de
    # Carrera (art. 223) y los factores están en el art. 225 del Decreto Ley
    # 262 de 2000, no en el sistema tipo de la CNSC.
    ('la CNSC es el órgano nacional que administra la carrera y fija el sistema tipo.',
     'la CNSC es el órgano nacional que administra la carrera general y fija su sistema tipo de evaluación, que no alcanza a la carrera especial de la PGN.'),
    ('salen del sistema tipo de EDL de la CNSC que aplica la entidad (o del sistema propio acreditado, si lo hubiera)',
     'salen del sistema que adopte la entidad: en la PGN, los instrumentos los adopta su Comisión de Carrera (art. 223 del Decreto Ley 262 de 2000) y los factores están en el art. 225; en las entidades de carrera general, del sistema tipo de EDL de la CNSC'),
]

ULTIMOS = [
    ('La inscripción en carrera solo procede tras superar el concurso de méritos de la CNSC;',
     'La inscripción en carrera solo procede tras superar el concurso de méritos que adelanta la propia Procuraduría;'),
    ('orientar sobre el concurso de la CNSC',
     'orientar sobre el concurso que adelanta la propia Procuraduría'),
    ('Administra y vigila las carreras; convoca y adelanta concursos;',
     'Administra y vigila la carrera general; convoca y adelanta sus concursos;'),
]

TODAS = TODAS + REZAGOS + ULTIMOS
