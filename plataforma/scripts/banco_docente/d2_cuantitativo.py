# -*- coding: utf-8 -*-
"""Razonamiento cuantitativo. Proporciones, porcentajes, promedios, lectura de
datos y estimación, en situaciones de la vida escolar. Tres opciones."""

RC = "Razonamiento cuantitativo"

BANCO = [
dict(
    tema="Porcentaje sobre un total", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="basic",
    ctx="En un curso de 40 estudiantes, 14 no entregaron el trabajo final en la fecha acordada con la docente. De los que entregaron, 9 lo hicieron el mismo día del plazo y el resto con anticipación.",
    q="¿Qué porcentaje del curso no entregó a tiempo?",
    ops=[
        "26 %",
        "35 %",
        "14 %",
    ],
    correcta=1,
    expl=[
        "26 es el número de estudiantes que sí entregaron a tiempo, no un porcentaje del total del curso.",
        "Correcto: 14 dividido entre 40 da 0,35, es decir, el 35 % del curso.",
        "14 es el número de estudiantes, no el porcentaje que representan dentro de los 40 del curso.",
    ],
),

dict(
    tema="Promedio ponderado", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="advanced",
    ctx="En el área, el período se califica así: trabajo en clase 30 %, quices 20 % y evaluación final 50 %. Un estudiante obtuvo 4,0 en trabajo en clase, 3,0 en quices y 3,4 en la evaluación final. La nota mínima aprobatoria es 3,0.",
    q="¿Cuál es su nota definitiva del período?",
    ops=[
        "3,50",
        "3,47",
        "3,40",
    ],
    correcta=0,
    expl=[
        "Correcto: 4,0 × 0,30 más 3,0 × 0,20 más 3,4 × 0,50 da 1,20 más 0,60 más 1,70, es decir, 3,50.",
        "Ese valor no resulta de aplicar la ponderación indicada a las tres notas que obtuvo el estudiante.",
        "3,40 es la nota de la evaluación final aislada, no el resultado de la ponderación del período.",
    ],
),

dict(
    tema="Regla de tres", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="basic",
    ctx="Para una salida pedagógica al museo, el transporte de 25 estudiantes cuesta $750.000. La empresa cobra por estudiante, sin cargo fijo ni mínimo de ocupación, y confirmó por escrito que mantiene la misma tarifa si el grupo crece. La docente debe informar el valor a las familias esta semana.",
    q="Si finalmente van 32 estudiantes, ¿cuánto cuesta el transporte?",
    ops=[
        "$900.000",
        "$1.050.000",
        "$960.000",
    ],
    correcta=2,
    expl=[
        "$900.000 correspondería a un grupo de 30 estudiantes, no a los 32 que finalmente asisten.",
        "$1.050.000 correspondería a 35 estudiantes, siete más de los que confirmaron la salida.",
        "Correcto: $750.000 entre 25 da $30.000 por estudiante, y $30.000 por 32 da $960.000.",
    ],
),

dict(
    tema="Variación porcentual", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="intermediate",
    ctx="La matrícula de la institución pasó de 480 estudiantes en 2025 a 528 en 2026. En el mismo período el número de docentes se mantuvo en 24 y no se abrieron nuevos grupos, de modo que el crecimiento se distribuyó entre los cursos existentes. El rector necesita el dato para sustentar la solicitud de dos plazas nuevas.",
    q="¿Cuál fue el aumento porcentual de la matrícula?",
    ops=[
        "48 %",
        "9,1 %",
        "10 %",
    ],
    correcta=2,
    expl=[
        "48 es el número de estudiantes en que aumentó la matrícula, no el porcentaje que ese aumento representa.",
        "9,1 % resulta de dividir 48 entre 528, que es el valor final; la base de comparación debe ser el inicial.",
        "Correcto: aumentó 48 estudiantes y 48 dividido entre 480 da 0,10, es decir, el 10 %.",
    ],
),

dict(
    tema="Lectura de una tabla de frecuencias", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="intermediate",
    ctx="Terminada la evaluación del segundo período, la docente organiza los resultados del curso en una tabla: desempeño bajo 6 estudiantes, básico 15, alto 12 y superior 7. El curso tiene 40 estudiantes y todos presentaron la evaluación en la fecha prevista. La coordinación le pide el dato para el consejo académico.",
    q="¿Qué porcentaje del curso alcanzó desempeño alto o superior?",
    ops=[
        "47,5 %",
        "52,5 %",
        "30 %",
    ],
    correcta=0,
    expl=[
        "Correcto: 12 más 7 son 19 estudiantes, y 19 entre 40 da 0,475, es decir, el 47,5 %.",
        "52,5 % es el porcentaje que suman los desempeños bajo y básico, que son los dos niveles inferiores.",
        "30 % correspondería únicamente a los 12 estudiantes de desempeño alto dentro del total del curso.",
    ],
),

dict(
    tema="Promedio y dato faltante", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="advanced",
    ctx="Un estudiante lleva cuatro notas en el área: 3,5; 2,8; 4,2 y 3,1. Falta una quinta nota y el estudiante necesita que el promedio de las cinco sea exactamente 3,5 para conservar su cupo en el semillero.",
    q="¿Qué nota necesita obtener en la quinta evaluación?",
    ops=[
        "4,2",
        "3,9",
        "3,5",
    ],
    correcta=1,
    expl=[
        "Con 4,2 el promedio superaría el 3,5 que el estudiante necesita exactamente para conservar el cupo.",
        "Correcto: para promediar 3,5 en cinco notas la suma debe ser 17,5, y las cuatro primeras suman 13,6.",
        "Con 3,5 el promedio quedaría por debajo, porque las cuatro primeras notas suman menos de lo necesario.",
    ],
),

dict(
    tema="Fracción de un total", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="basic",
    ctx="De los 36 estudiantes de un curso, tres cuartas partes asistieron a la jornada de refuerzo del sábado. La docente preparó material individual para cada asistente y sobró una cantidad igual al número de ausentes.",
    q="¿Cuántos estudiantes asistieron?",
    ops=[
        "24 estudiantes",
        "30 estudiantes",
        "27 estudiantes",
    ],
    correcta=2,
    expl=[
        "24 son dos terceras partes de 36, no tres cuartas partes como indica el enunciado.",
        "30 serían cinco sextas partes de 36, una fracción mayor que la que señala el texto.",
        "Correcto: 36 multiplicado por 3 y dividido entre 4 da 27 estudiantes.",
    ],
),

dict(
    tema="Escala y proporción", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="intermediate",
    ctx="En el plano de la institución, 2 centímetros representan 5 metros reales. El plano se está usando para calcular cuánta pintura se necesita para demarcar la cancha y el patio antes de la semana cultural, y el proveedor cobra por metro lineal demarcado.",
    q="Si el patio mide 14 centímetros de largo en el plano, ¿cuánto mide en la realidad?",
    ops=[
        "35 metros",
        "70 metros",
        "28 metros",
    ],
    correcta=0,
    expl=[
        "Correcto: 14 entre 2 da 7, y 7 multiplicado por 5 da 35 metros.",
        "70 metros resulta de multiplicar 14 por 5 sin dividir antes entre los 2 centímetros de la escala.",
        "28 metros correspondería a una escala de 1 centímetro por cada 2 metros, que no es la del plano.",
    ],
),

dict(
    tema="Interpretación de un promedio", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="advanced",
    ctx="El promedio del curso en la última evaluación fue 3,2 sobre 5,0. Con ese dato, una docente concluye que la mayoría de los estudiantes obtuvo una nota cercana a 3,2 y decide no programar actividades de refuerzo para nadie durante las dos semanas que restan del período.",
    q="¿Por qué esa conclusión puede ser falsa?",
    ops=[
        "Porque el promedio aritmético solo resulta confiable cuando se calcula con más de cincuenta datos.",
        "Porque un mismo promedio puede salir de notas concentradas o de notas muy dispersas entre sí.",
        "Porque 3,2 no es una nota válida dentro de la escala de valoración que adopta la institución.",
    ],
    correcta=1,
    expl=[
        "El promedio es válido con cualquier cantidad de datos; el tamaño no es lo que limita su interpretación.",
        "Correcto: la medida de tendencia central no informa nada sobre la dispersión de los resultados.",
        "3,2 es una nota perfectamente válida dentro de cualquier escala numérica de uno a cinco.",
    ],
),

dict(
    tema="Descuentos sucesivos", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="advanced",
    ctx="Una papelería del barrio ofrece 20 % de descuento en los útiles escolares de la lista oficial y, sobre el valor ya rebajado, un 10 % adicional por pago en efectivo. El precio original de la lista completa es $100.000 y varias familias preguntan cuánto deben llevar.",
    q="¿Cuánto se paga al final?",
    ops=[
        "$70.000",
        "$80.000",
        "$72.000",
    ],
    correcta=2,
    expl=[
        "$70.000 resultaría de sumar los dos descuentos como si fueran el 30 % del precio original.",
        "$80.000 es el precio después del primer descuento, antes de aplicar el segundo por pago en efectivo.",
        "Correcto: $100.000 menos 20 % da $80.000, y $80.000 menos 10 % da $72.000.",
    ],
),

dict(
    tema="Razón entre dos cantidades", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="intermediate",
    ctx="La institución atiende 720 estudiantes y su planta docente es de 30 maestros de aula, repartidos entre las dos jornadas. La secretaría pide reportar la razón de estudiantes por docente para el informe anual.",
    q="¿Cuál es esa razón?",
    ops=[
        "24 a 1",
        "20 a 1",
        "36 a 1",
    ],
    correcta=0,
    expl=[
        "Correcto: 720 dividido entre 30 da 24 estudiantes por cada docente de aula.",
        "20 a 1 daría un total de 600 estudiantes para los 30 docentes, menos de los que atiende la institución.",
        "36 a 1 daría 1.080 estudiantes, bastante más de los 720 que la institución tiene matriculados.",
    ],
),

dict(
    tema="Conversión de unidades de tiempo", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="basic",
    ctx="Un área tiene asignadas 5 horas semanales de clase y el calendario académico contempla 38 semanas efectivas de trabajo. El jefe de área necesita el total anual para distribuir el plan de estudios.",
    q="¿Cuántas horas de clase tiene el área en el año?",
    ops=[
        "180 horas",
        "190 horas",
        "200 horas",
    ],
    correcta=1,
    expl=[
        "180 correspondería a 36 semanas efectivas, dos menos de las que contempla el calendario académico.",
        "Correcto: 5 horas multiplicadas por 38 semanas dan 190 horas en el año.",
        "200 correspondería a 40 semanas, dos más de las que el calendario establece como efectivas.",
    ],
),

dict(
    tema="Probabilidad simple", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="intermediate",
    ctx="En una bolsa opaca hay 8 fichas azules, 6 rojas y 6 verdes, preparadas para una actividad de conteo y azar en tercer grado. Las fichas son iguales en tamaño, peso y textura, y cada estudiante saca una sin mirar y la devuelve a la bolsa antes del siguiente turno.",
    q="¿Cuál es la probabilidad de que la ficha sea roja?",
    ops=[
        "1/3",
        "3/10",
        "6/14",
    ],
    correcta=1,
    expl=[
        "1/3 correspondería a que hubiera exactamente el mismo número de fichas de cada uno de los tres colores.",
        "Correcto: hay 20 fichas en total y 6 son rojas; 6/20 se simplifica a 3/10.",
        "6/14 deja por fuera del total las 6 fichas verdes, que también están dentro de la bolsa.",
    ],
),

dict(
    tema="Promedio de dos grupos", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="advanced",
    ctx="El grupo A tiene 20 estudiantes y un promedio de 3,0 en el área. El grupo B tiene 30 estudiantes y un promedio de 4,0. El coordinador necesita el promedio conjunto de los 50 estudiantes para el consejo académico.",
    q="¿Cuál es el promedio de los 50 estudiantes juntos?",
    ops=[
        "3,5",
        "3,75",
        "3,6",
    ],
    correcta=2,
    expl=[
        "3,5 sería el promedio solo si los dos grupos tuvieran exactamente el mismo número de estudiantes.",
        "3,75 sobrestima el peso del grupo B dentro del total de los 50 estudiantes del grado.",
        "Correcto: 20 por 3,0 más 30 por 4,0 da 180, y 180 dividido entre 50 da 3,6.",
    ],
),

dict(
    tema="Estimación razonable", ref="DOC-RC",
    refT="Razonamiento cuantitativo", nivel="intermediate",
    ctx="Se quiere entregar un refrigerio diario a cada estudiante de la institución durante una semana de cinco días. Hay 612 estudiantes matriculados y cada refrigerio cuesta $2.900. El rector necesita una estimación antes de la reunión.",
    q="¿Cuál es la estimación más razonable del costo total de la semana?",
    ops=[
        "Cerca de $9.000.000",
        "Cerca de $1.800.000",
        "Cerca de $18.000.000",
    ],
    correcta=0,
    expl=[
        "Correcto: 612 por $2.900 da cerca de $1.775.000 por día, y por cinco días cerca de $8.875.000.",
        "$1.800.000 corresponde al costo de un solo día de entrega, no al de la semana completa.",
        "$18.000.000 duplica el costo real de la semana y no corresponde a ninguno de los dos cálculos.",
    ],
),

]
