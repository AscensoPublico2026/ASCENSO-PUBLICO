# Abastecer Empresarial S.A.S. — Portafolio comercial

Proyecto de rediseño del portafolio comercial (PDF) de **Abastecer Empresarial S.A.S.** (NIT 902088758-4, Cali, Valle del Cauca). Concepto: *"Un solo aliado para múltiples necesidades de suministro"*.

> Este proyecto es independiente de la plataforma de cursos de Ascenso Público; solo comparte el repositorio.

## Estado (octubre 2026)

| Página | Estado | Archivo |
|---|---|---|
| 1. Portada | Lista para revisión (v7) | `salidas/Portada_Abastecer_v7.pdf` |
| 2. Líneas de suministro | Vista previa (v3); faltan imágenes limpias de Tecnología, Aseo, Promocionales y Temporada | `salidas/Pagina2_v3_vista_previa.pdf` |
| 3. Dotación | Por rediseñar | — |
| 4 a 7. EPP por líneas | Vista previa: 7 líneas (cabeza, visual y facial, auditiva, respiratoria, manos, corporal, calzado de seguridad y laboral) + línea de trabajo en alturas en la pág. 7, 3 productos por línea, colores de cascos, listado de productos principales y botón de WhatsApp con mensaje por línea; recortes ampliados con Real-ESRGAN | `salidas/EPP_por_lineas_pags_4-7.pdf` |
| 8 (y 9). Señalización, incendios y emergencias | Dos propuestas para elegir: **A** en dos páginas (`salidas/Senalizacion_opcionA_pags_8-9.pdf`) y **B** compacta en una página (`salidas/Senalizacion_opcionB_pag_8.pdf`). Si se elige A, renumerar el índice de la pág. 2 (+1 desde Aseo) | `build/build_senalizacion.py` |
| Canecas, contenedores y almacenamiento | Vista previa de una página (`salidas/Canecas_contenedores_vista_previa.pdf`): fotos reales: puntos ecológicos (Protecto) y caneca de pedal, tambor y canastillas (fotos enviadas por Abastecer; confirmar origen) | `build/build_canecas.py` |
| Ergonomía y tecnología (pág. 10) + Estanterías (pág. 11) | Vista previa con ilustraciones referenciales; faltan fotos reales (`salidas/Ergonomia_tecnologia_estanterias_vista_previa.pdf`) | `build/build_ergo_tec.py` |
| Aseo y cafetería y siguientes | Por rediseñar | — | (los números del índice de la página 2 ya contemplan las 3 páginas de EPP) | — |

## Reglas del proyecto (no negociables)

- Sistema de diseño: paleta `#0D1B2A` / `#16823C` / `#F2B705` / gris neutro, tipografía Montserrat, logo original sin deformar (`build/logo_h.png`), cajas con esquinas redondeadas, encabezado y pie.
- Sin precios, descuentos ni precios de catálogos de proveedores.
- Sin afirmar inventario inmediato, plazos de entrega, ahorros, certificaciones, normas ni alianzas oficiales sin evidencia.
- Sin inventar años de experiencia, clientes, sedes, cifras, direcciones, correos ni redes.
- Imágenes que no sean fotos reales de producto: etiqueta **"Imagen referencial"** (o **"Ilustración referencial"**).
- Nota legal al pie: *"Referencias y disponibilidad sujetas a confirmación en la cotización."*
- CTA principal: **SOLICITA TU COTIZACIÓN**. Datos fijos: WhatsApp 350 862 4021 · www.abastecerempresarial.com. Enlaces: `https://wa.me/573508624021` y `https://www.abastecerempresarial.com/`.

## Estructura

```
abastecer-empresarial/
├── build/      scripts (reportlab), logo, recortes de producto (cut/), foto de portada
├── fonts/      Montserrat (licencia OFL)
├── fotos/      imágenes de origen (Gemini) usadas en las páginas
├── salidas/    PDF y PNG de las páginas generadas
└── PROCEDENCIA_IMAGENES.csv
```

## Cómo regenerar

```bash
pip install reportlab pillow numpy opencv-python-headless
cd build
python3 build_portada_v7.py     # -> Portada_Abastecer_v7.pdf
python3 build_pagina2_v3.py     # -> Pagina2_v3_vista_previa.pdf
python3 build_epp_lineas.py     # -> salidas/EPP_por_lineas_pags_4-7.pdf
```

Utilidades: `build_portada_v2.py` (paleta, íconos y funciones comunes), `cut*.py` / `gc2.py` / `auto.py` (recortes de producto desde el catálogo del proveedor).

## Imágenes y licencias

Ver `PROCEDENCIA_IMAGENES.csv`. Puntos importantes:

- **Catálogo de Protecto (2026):** Laura indicó que el proveedor autorizó usar sus imágenes de producto. **Conservar la autorización por escrito.** El PDF del catálogo y sus páginas rasterizadas **no están en el repositorio** (contienen precios, mínimos, correos y direcciones del proveedor).
- **Imágenes de Gemini (IA):** varias muestran marcas reales o el logo deformado; están marcadas como *pendientes de reemplazo*. Para presentación a clientes, usar versiones sin marcas o fotos reales.
- El repositorio es **público**: no subir aquí el catálogo del proveedor, listas de precios ni datos de personas.

## Pendientes

- Imágenes limpias de 3 objetos por línea: Tecnología, Aseo y cafetería, Promocionales y carnés, Temporada y celebraciones.
- Confirmar qué marcas de proveedores están autorizadas para mostrarse.
- Página 3 en adelante (Dotación, EPP, Calzado, Alturas, Señalización, Emergencias…), páginas finales y contraportada.
- Validar números de página del índice y enlazarlos dentro del PDF.
