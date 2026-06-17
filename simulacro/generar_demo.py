# Script para generar el simulacro demo completo
# Solo necesito agregar las preguntas al HTML base ya creado

preguntas = []

# PREGUNTA 1
preguntas.append({
    "num": 1,
    "nivel": "basica",
    "tema": "Recepción y verificación",
    "contexto": """
        <p>Eres el técnico de almacén del INDERVALLE y llega un proveedor con un pedido de 100 cajas de insumos deportivos amparado en un contrato vigente. El transportador trae mucho afán: te entrega la factura por las 100 cajas, te asegura que "todo viene completo y en buen estado" y te pide que le firmes el recibido de una vez para seguir su ruta.</p>
        <p>En la bodega tienes espacio suficiente y unos 20 minutos disponibles para revisar. Tu jefe no está en la oficina en este momento, pero sabes que la recepción de bienes es parte de tus funciones rutinarias. El proveedor insiste en que firmes ya, porque "tiene otras entregas pendientes y se le hace tarde".</p>
        <p>Sabes que tu responsabilidad sobre los bienes comienza desde el momento en que firmas el acta de recepción. <span class="enfasis">¿Cómo procedes?</span></p>
    """,
    "opciones": [
        "Firmar el recibido por las 100 cajas confiando en la factura y en la palabra del proveedor, ya que hay un contrato vigente y el transportador tiene afán legítimo de continuar su ruta.",
        "Verificar la cantidad y el estado físico de las cajas contra el contrato y la factura, y firmar el acta solo por lo que esté conforme, dejando constancia escrita de cualquier novedad o faltante.",
        "Recibir físicamente todas las cajas para no demorar al transportador y dejar la verificación detallada y el registro formal para cuando tengas menos carga de trabajo.",
        "Aceptar las cajas en el almacén pero no firmar ningún documento hasta que tu jefe inmediato venga personalmente a autorizar el ingreso y revisar la entrega."
    ],
    "correcta": 1,  # índice 0-based
    "explicaciones": [
        {
            "titulo": "Por qué es incorrecta",
            "texto": """
                <p>El contrato y la factura indican lo que <strong>DEBERÍA</strong> llegar según el acuerdo, no lo que realmente está ingresando físicamente al almacén. Si firmas sin verificar y posteriormente se descubren faltantes, daños o diferencias en las especificaciones, la responsabilidad recae directamente sobre ti como receptor de los bienes.</p>
                <p>El afán de un tercero (el transportador) no releva tu deber de control y verificación. Además, la existencia de un contrato no garantiza que el proveedor cumpla exactamente lo pactado: por eso existe el proceso de recepción.</p>
                <div class="norma"><strong>Norma aplicable:</strong> Ley 87 de 1993 (Sistema de Control Interno), Régimen de Contabilidad Pública — CGN.</div>
            """
        },
        {
            "titulo": "Por qué es la correcta",
            "texto": """
                <p>La recepción de bienes públicos exige verificar contra el soporte (contrato, orden de compra o factura) antes de firmar el acta de ingreso, y el documento debe reflejar con exactitud lo que realmente ingresó. Tienes el tiempo necesario (20 minutos) y el espacio disponible, por lo que no hay impedimento técnico para cumplir con el procedimiento.</p>
                <p>Si algo no está conforme (faltantes, daños, diferencias en especificaciones), debes dejarlo por escrito en el acta: así proteges el patrimonio público, estableces claramente la responsabilidad del proveedor y te blindas ante cualquier futura verificación o auditoría.</p>
                <div class="norma"><strong>Principio rector:</strong> Artículo 209 de la Constitución Política (transparencia, moralidad y responsabilidad).</div>
            """
        },
        {
            "titulo": "Por qué es incorrecta",
            "texto": """
                <p>Separar la recepción física del registro y la verificación formal abre la puerta a descuadres y genera un vacío de trazabilidad. Si después de "recibir" físicamente las cajas (sin verificar ni documentar) se descubre que falta algo o hay daños, no podrás demostrar en qué estado llegaron ni cuántas ingresaron realmente.</p>
                <p>La carga de trabajo no justifica posponer un control esencial: el registro y la verificación SON parte del acto de recibir, no son trámites que se hacen "después con calma".</p>
                <div class="norma"><strong>Error común:</strong> Creer que "recibir" es solo dejar entrar físicamente los bienes y que el papeleo puede esperar.</div>
            """
        },
        {
            "titulo": "Por qué es incorrecta",
            "texto": """
                <p>Escalar al jefe inmediato una tarea rutinaria que está claramente dentro de tus funciones es quedarte corto en tu rol y entorpece innecesariamente el funcionamiento del área. La recepción de un pedido ordinario amparado en un contrato vigente es exactamente el tipo de actividad que un técnico de almacén debe ejecutar de manera autónoma.</p>
                <p>El nivel técnico tiene la capacidad y la obligación de verificar y recibir bienes; lo que SÍ debe informar al jefe son las novedades, irregularidades o decisiones que excedan su competencia.</p>
                <div class="norma"><strong>Alcance del cargo:</strong> Decreto 1083 de 2015 — el nivel técnico ejecuta actividades técnicas y de apoyo; verificar ingresos es precisamente eso.</div>
            """
        }
    ],
    "clave": "La CNSC evalúa si entiendes que el soporte (acta de recepción) debe reflejar la <strong>REALIDAD</strong> de lo recibido, no lo que 'debería' haber llegado. La presión externa NO justifica saltarse la verificación.",
    "reforzar": [
        "FUN-ALM-02: Recepción y Verificación de Bienes",
        "GEN-01: Estado y Función Pública",
        "TEC-ESP-02: Alcance del Cargo Técnico"
    ]
})

print(f"✓ {len(preguntas)} pregunta(s) definida(s)")
