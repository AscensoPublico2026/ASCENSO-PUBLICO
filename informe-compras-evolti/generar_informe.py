# -*- coding: utf-8 -*-
"""
Generador de informe de compras Evolti (uno por proyecto).

Diseño: la hoja DETALLE es la unica fuente de datos. Todas las hojas de
resumen usan FORMULAS REALES de Excel (SUMAR.SI.CONJUNTO / SUMA / division)
que apuntan al Detalle, de modo que los totales se recalculan solos dentro
de Excel (no son valores "pegados").

Hojas:
  - Resumen (totales, indicadores, obra vs administrativo) -> con formulas
  - Por categoria (Grupo -> Subgrupo anidado) -> con formulas + torta
  - Por proveedor -> con formulas + barras
  - Por estado / legalizacion / solicitud -> con formulas
  - Detalle (fuente) -> datos crudos limpios
"""
import os
from collections import defaultdict, OrderedDict
from datetime import datetime

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import PieChart, BarChart, Reference

BASE = os.path.dirname(__file__)

# ============================================================
# CATALOGO DE CATEGORIZACION DE ITEMS (por palabras clave)
# Se evalua EN ORDEN: la primera regla que coincide gana.
# Asi evitamos falsos positivos (ej: "SOPORTE INVERSOR" -> Estructura, no Inversor).
# Cada regla: (Categoria, [palabras clave que deben aparecer (OR)])
# ============================================================
REGLAS_ITEM = [
    # --- Servicios / logistica (van primero para no confundir con materiales) ---
    ("Viáticos - Alimentación", ["RESTAURANTE", "COMEDOR", "ALIMENTAC", "REFRIGERIO", "CATERING"]),
    ("Viáticos - Hospedaje", ["HOTEL", "HOSPEDAJE", "ALOJAMIENTO"]),
    ("Viáticos - Transporte", ["SERVICIO DE TRANSPORTE", "TRANSPORTE DE PERSONAL", "PASAJE", "TIQUETE", "PEAJE", "COMBUSTIBLE", "GASOLINA"]),
    ("Fletes y transporte de carga", ["FLETE", "TRANSPORTE DE CARGA", "TRANSPORTE DE MATERIAL", "ACARREO", "GRUA", "MONTACARGA"]),
    ("Arriendos e inmuebles", ["ARRIENDO", "ARRENDAMIENTO", "BODEGA"]),
    ("Baños y sanitarios portátiles", ["BAÑO PORTATIL", "BAÑO PORTÁTIL", "LAVAMANOS PORTATIL", "SANITARIO PORTATIL"]),
    ("Alquiler de maquinaria y equipos", ["ALQUILER", "RETROEXCAVADORA", "MEZCLADORA", "POLIPASTO", "WINCHE", "WINCHER", "PLUMA", "ANDAMIO", "SIERRA CIRCULAR", "VIBROCOMPACTADOR"]),
    ("SST y exámenes médicos", ["EXAMEN PERIODICO", "EXAMEN MEDICO", "EXAMEN OCUPACIONAL", "EXAMEN DE ALTURA", "EXÁMEN"]),
    ("EPP (dotación y seguridad)", ["GUANTE", "CASCO", "BOTA", "ARNES", "ARNÉS", "GAFAS", "TAPA OIDO", "OVEROL", "CHALECO", "EPP", "ESLINGA", "LINEA DE VIDA", "PROTECCION AUDITIVA"]),
    ("RETIE / Legalización / Medición", ["RETIE", "CERTIFICAC", "LEGALIZ", "PRUEBAS DE RUTINA", "CALIBRAC", "MEDICION NIVEL", "MEDICIÓN NIVEL", "UPME", "DICTAMEN", "INSPECC"]),
    ("Servicios de obra e ingeniería", ["CONSTRUCCION SET", "CONSTRUCCIÓN SET", "COMISIONAMIENTO", "ENERGIZACION", "ENERGIZACIÓN", "REMOCION DE MATERIAL", "REMOCIÓN DE MATERIAL", "CORTE EN ACRILICO", "CORTE EN ACRÍLICO"]),
    ("Servicios de instalación y montaje", ["INSTALACION", "INSTALACIÓN", "MONTAJE", "MANO DE OBRA", "DESCARGUE", "DESCARGUES", "ARMADO", "TENDIDO"]),

    # --- Equipos principales ---
    ("Transformadores y celdas", ["TRANSFORMADOR", "CELDA PARA TRANSFORMADOR", "CELDA DE"]),
    ("Medidores", ["MEDIDOR"]),
    ("Inversores", ["INVERSOR", "SUN2000", "SIN2000", "SUN 2000"]),
    ("Paneles solares", ["PANEL SOLAR", "MODULO FOTOVOLTAIC", "MÓDULO FOTOVOLTAIC", "MODULO SOLAR", "PANEL FOTOVOLTAIC"]),
    ("Monitoreo y comunicaciones", ["SMARTLOGGER", "SMART LOGGER", "SMARTPS", "SMART POWER SENSOR", "SDONGLE", "DONGLE", "ANALIZADOR DE ENERG", "MODEM", "ROUTER", "WLAN", "JANITZA"]),

    # --- Estructura / soporte ---
    ("Estructura y soportería solar", ["ESTRUCTURA SOLAR", "MESA", "SOPORTE", "GOOMAX", "PLATINA", "PERFIL", "RIEL", "PARAL", "CANAL GALVANIZADO", "TIPO GRANJA", "SUPERBOARD", "MARCOS METALIC", "MARCOS METÁLIC", "ANGULO"]),

    # --- Materiales electricos ---
    ("Cableado y conductores", ["CABLE", "CONDUCTOR", "ALAMBRE", "AWG", "MC4", "CONECTOR", "BORNA", "TERMINAL PREMOLDEADO", "TERMINAL BIMETAL", "CORAZA AMERICANA"]),
    ("Tableros y protecciones", ["TABLERO", "BREAKER", "INTERRUPTOR", "TOTALIZADOR", "BARRAJE", "GABINETE", "DPS", "GUARDAMOTOR", "CONTACTOR", "RELE", "RELÉ", "FUSIBLE", "SUPRESOR"]),
    ("Canalización y tubería", ["TUBO", "TUBERIA", "TUBERÍA", "CONDUIT", "CANALETA", "CANAL ESTRUCTURADO", "DUCTO", "CURVA", "UNION EMT", "TERMINAL EMT", "ADAPTADOR", "COPLA", "BANDEJA", "CONDULETA", "REJIBAND"]),
    ("Cajas de paso y accesorios", ["CAJA DE PASO", "CAJA ", "TAPA", "GRAPA", "CHAZO", "TORNILLO", "TUERCA", "AMARRE", "ABRAZADERA", "PRECINTO"]),
    ("Puesta a tierra", ["PUESTA A TIERRA", "TIERRA", "VARILLA COPPERWELD", "VARILLA SOLIDA DE COBRE", "SOLDADURA EXOTERMICA"]),

    # --- Obra civil ---
    ("Obra civil (concreto, agregados)", ["CEMENTO", "CONCRETO", "ARENA", "GRAVA", "TRITURAC", "TRITURADO", "CRUDO DE RIO", "CRUDO DE RÍO", "SUB BASE", "RECEBO", "MALLA ELECTROSOLDADA", "VARILLA CORRUGADA", "CHIPA DE ACERO", "LADRILLO", "BLOQUE", "TUBO 36", "ANCLAJE", "TABLA", "TABLON", "TABLÓN"]),
    ("Impermeabilización y acabados", ["SIKA", "IMPERMEABILIZ", "VINILO", "PINTURA", "ESTUCO", "PLASTICO NEGRO", "PLÁSTICO NEGRO", "SELLANTE"]),
    ("Cerramiento perimetral", ["CERRAMIENTO", "CERCA", "PORTON", "PORTÓN"]),
    ("Micropilotaje", ["MICROPILOT", "PILOTE", "HINCA", "BARRA ROSCADA", "VARILLA ROSCADA"]),
]

def categorizar_item(nombre):
    up = (nombre or "").upper()
    for cat, kws in REGLAS_ITEM:
        for kw in kws:
            if kw in up:
                return cat
    return "Otros / sin clasificar"

# ---- Paleta de marca ----
NAVY = "0B1F3A"; NAVY2 = "13345C"; GOLD = "C9A227"; GOLD_SOFT = "F3ECCF"
GREY = "F2F4F7"; WHITE = "FFFFFF"; LINE = "D8DEE6"; SUBFILL = "EAF0F6"

thin = Side(style="thin", color=LINE)
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

MONEY_FMT = '#,##0 "COP"'
INT_FMT = '#,##0'
PCT_FMT = '0.0%'

def num(x):
    if x is None or x == "":
        return 0.0
    try:
        return float(x)
    except Exception:
        return 0.0

def clean(x):
    return ("" if x is None else str(x)).strip()

def read_rows(path):
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb.active
    rows = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        if any(c is not None and str(c).strip() != "" for c in r):
            rows.append(list(r[:20]))
    return rows

# ---------- helpers de estilo ----------
def title_cell(ws, cell, text, size=16, color=WHITE, fill=NAVY, align="left"):
    c = ws[cell]; c.value = text
    c.font = Font(bold=True, size=size, color=color)
    c.fill = PatternFill("solid", fgColor=fill)
    c.alignment = Alignment(horizontal=align, vertical="center")

def header_row(ws, row, headers, start_col=1):
    for j, h in enumerate(headers):
        c = ws.cell(row=row, column=start_col + j, value=h)
        c.font = Font(bold=True, color=WHITE, size=11)
        c.fill = PatternFill("solid", fgColor=NAVY2)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDER

def set_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

def money(cell):
    cell.number_format = MONEY_FMT
    cell.alignment = Alignment(horizontal="right")

# ================= construccion de un proyecto =================
def build(project_label, project_sub, filename, out_name):
    path = os.path.join(BASE, filename)
    rows = read_rows(path)
    n_items = len(rows)

    # --- indicadores (solo para tarjetas informativas) ---
    ocs, fechas, provset, grpset = set(), [], set(), set()
    # estructura Grupo -> [subgrupos...] preservando orden por gasto
    grp_val = defaultdict(float)
    sub_val = defaultdict(float)  # (grupo, sub) -> valor  (para ordenar)
    prov_val = defaultdict(float)
    cat_val = defaultdict(lambda: [0.0, 0.0])       # categoria -> [cant, valor]
    catprod_val = defaultdict(lambda: [0.0, 0.0])   # (categoria, producto) -> [cant, valor]
    estados_set, legal_set, tsol_set = OrderedDict(), OrderedDict(), OrderedDict()

    for r in rows:
        (fecha, noOC, noPed, estado, estleg, grupo, subg, prod, cant, precio,
         vtot, tipimp, vimp, quien, prov, tsol, tproy, proy, nofact, sop) = r
        v = num(vtot); q = num(cant)
        if noOC is not None: ocs.add(noOC)
        if isinstance(fecha, datetime): fechas.append(fecha)
        g = clean(grupo) or "(sin grupo)"; s = clean(subg) or "(sin subgrupo)"
        p = clean(prov) or "(sin proveedor)"
        cat = categorizar_item(clean(prod))
        prod_c = clean(prod) or "(sin nombre)"
        grpset.add(g); provset.add(p)
        grp_val[g] += v; sub_val[(g, s)] += v; prov_val[p] += v
        cat_val[cat][0] += q; cat_val[cat][1] += v
        catprod_val[(cat, prod_c)][0] += q; catprod_val[(cat, prod_c)][1] += v
        estados_set[clean(estado) or "(vacío)"] = True
        legal_set[clean(estleg) or "(vacío)"] = True
        tsol_set[clean(tsol) or "(vacío)"] = True

    fmin = min(fechas).date() if fechas else "-"
    fmax = max(fechas).date() if fechas else "-"

    wb = openpyxl.Workbook()

    # ============================================================
    # HOJA DETALLE (fuente de datos) -> se crea primero para referenciarla
    # ============================================================
    wsd = wb.active
    wsd.title = "Detalle"
    wsd.sheet_view.showGridLines = False
    detail_cols = ["Fecha","No OC","No pedido","Estado","Legalización","Grupo","Sub grupo",
                   "Producto / servicio","Cant.","Precio unit.","Valor sin IVA","Tipo impuesto",
                   "IVA","Total con IVA","Solicitó","Proveedor","Tipo solicitud","Tipo proyecto",
                   "No factura","Categoría de ítem"]
    header_row(wsd, 1, detail_cols, start_col=1)
    wsd.freeze_panes = "A2"
    rr = 2
    for r in rows:
        (fecha, noOC, noPed, estado, estleg, grupo, subg, prod, cant, precio,
         vtot, tipimp, vimp, quien, prov, tsol, tproy, proy, nofact, sop) = r
        v = num(vtot); iva = num(vimp)
        cat_item = categorizar_item(clean(prod))
        vals = [fecha, noOC, noPed, clean(estado), clean(estleg),
                clean(grupo) or "(sin grupo)", clean(subg) or "(sin subgrupo)",
                clean(prod), num(cant), num(precio), v, clean(tipimp), iva, None,
                clean(quien), clean(prov) or "(sin proveedor)", clean(tsol),
                clean(tproy), clean(nofact), cat_item]
        for j, val in enumerate(vals, start=1):
            c = wsd.cell(row=rr, column=j, value=val)
            c.border = BORDER
            if j == 1 and isinstance(val, datetime):
                c.number_format = "yyyy-mm-dd"
            if j in (10, 11, 13):
                c.number_format = MONEY_FMT
            if j == 9:
                c.number_format = '#,##0.##'
        # Total con IVA = Valor sin IVA + IVA (FORMULA real)
        c = wsd.cell(row=rr, column=14, value=f"=K{rr}+M{rr}")
        c.number_format = MONEY_FMT; c.border = BORDER
        rr += 1
    last = rr - 1  # ultima fila de datos
    for rx in range(2, rr):
        fill = WHITE if rx % 2 == 0 else GREY
        for cx in range(1, len(detail_cols) + 1):
            wsd.cell(row=rx, column=cx).fill = PatternFill("solid", fgColor=fill)
    set_widths(wsd, [12,8,9,11,12,22,26,42,7,15,16,12,14,16,22,32,13,14,16,28])
    wsd.auto_filter.ref = f"A1:{get_column_letter(len(detail_cols))}{last}"

    # rangos con nombre (referencias absolutas al Detalle)
    RNG_GRUPO   = f"Detalle!$F$2:$F${last}"
    RNG_SUBG    = f"Detalle!$G$2:$G${last}"
    RNG_PROD    = f"Detalle!$H$2:$H${last}"
    RNG_CANT    = f"Detalle!$I$2:$I${last}"
    RNG_VALOR   = f"Detalle!$K$2:$K${last}"
    RNG_IVA     = f"Detalle!$M$2:$M${last}"
    RNG_PROV    = f"Detalle!$P$2:$P${last}"
    RNG_ESTADO  = f"Detalle!$D$2:$D${last}"
    RNG_LEGAL   = f"Detalle!$E$2:$E${last}"
    RNG_TSOL    = f"Detalle!$Q$2:$Q${last}"
    RNG_TPROY   = f"Detalle!$R$2:$R${last}"
    RNG_CAT     = f"Detalle!$T$2:$T${last}"

    TOT_VALOR = f"SUM({RNG_VALOR})"
    TOT_IVA   = f"SUM({RNG_IVA})"

    # ============================================================
    # HOJA RESUMEN
    # ============================================================
    ws = wb.create_sheet("Resumen", 0)
    ws.sheet_view.showGridLines = False
    set_widths(ws, [3, 36, 22, 22, 22, 4])

    title_cell(ws, "B2", "EVOLTI  ·  INFORME DE COMPRAS", size=18); ws.merge_cells("B2:E2")
    title_cell(ws, "B3", project_label, size=13, color=GOLD, fill=NAVY); ws.merge_cells("B3:E3")
    ws["B4"].value = project_sub
    ws["B4"].font = Font(italic=True, size=10, color="5A6472"); ws.merge_cells("B4:E4")
    ws["B5"].value = f"Periodo: {fmin} a {fmax}   ·   Generado: {datetime.now().date()}   ·   Moneda: COP   ·   Cifras calculadas con fórmulas sobre la hoja Detalle"
    ws["B5"].font = Font(size=9, color="5A6472"); ws.merge_cells("B5:E5")

    r = 7
    ws.cell(row=r, column=2, value="TOTALES DEL PROYECTO").font = Font(bold=True, size=12, color=NAVY)
    r += 1
    total_cards = [
        ("VALOR TOTAL (sin IVA)", f"={TOT_VALOR}", GOLD_SOFT),
        ("IVA", f"={TOT_IVA}", GOLD_SOFT),
        ("TOTAL CON IVA", f"={TOT_VALOR}+{TOT_IVA}", GOLD),
    ]
    for label, formula, fill in total_cards:
        ws.cell(row=r, column=2, value=label).font = Font(bold=True, size=11, color=NAVY)
        c = ws.cell(row=r, column=4, value=formula); money(c)
        c.font = Font(bold=True, size=12, color=NAVY)
        for cc in range(2, 5):
            cell = ws.cell(row=r, column=cc)
            cell.fill = PatternFill("solid", fgColor=fill); cell.border = BORDER
        ws.cell(row=r, column=3).fill = PatternFill("solid", fgColor=fill)
        ws.cell(row=r, column=3).border = BORDER
        r += 1

    r += 1
    ws.cell(row=r, column=2, value="INDICADORES").font = Font(bold=True, size=12, color=NAVY)
    r += 1
    indics = [
        ("Órdenes de compra (No OC únicas)", len(ocs)),
        ("Líneas de ítem / compras", f"=COUNTA({RNG_VALOR})"),
        ("Proveedores distintos", len(provset)),
        ("Categorías (Grupos)", len(grpset)),
    ]
    for label, val in indics:
        ws.cell(row=r, column=2, value=label).font = Font(size=11, color=NAVY)
        c = ws.cell(row=r, column=4, value=val); c.number_format = INT_FMT
        c.alignment = Alignment(horizontal="right"); c.font = Font(bold=True, color=NAVY)
        for cc in range(2, 5):
            ws.cell(row=r, column=cc).border = BORDER
        r += 1

    # Obra vs Administrativo (con SUMAR.SI.CONJUNTO)
    r += 1
    ws.cell(row=r, column=2, value="GASTO DE OBRA vs ADMINISTRATIVO").font = Font(bold=True, size=12, color=NAVY)
    r += 1
    header_row(ws, r, ["Concepto", "Valor sin IVA", "IVA", "Total con IVA"], start_col=2)
    r += 1
    oa_start = r
    # OBRA = todo lo que NO es ADMINISTRATIVO ; ADMIN = = ADMINISTRATIVO
    ws.cell(row=r, column=2, value="Gasto de obra")
    ws.cell(row=r, column=3, value=f'=SUMIFS({RNG_VALOR},{RNG_TPROY},"<>ADMINISTRATIVO")')
    ws.cell(row=r, column=4, value=f'=SUMIFS({RNG_IVA},{RNG_TPROY},"<>ADMINISTRATIVO")')
    ws.cell(row=r, column=5, value=f"=C{r}+D{r}")
    r += 1
    ws.cell(row=r, column=2, value="Gasto administrativo")
    ws.cell(row=r, column=3, value=f'=SUMIFS({RNG_VALOR},{RNG_TPROY},"ADMINISTRATIVO")')
    ws.cell(row=r, column=4, value=f'=SUMIFS({RNG_IVA},{RNG_TPROY},"ADMINISTRATIVO")')
    ws.cell(row=r, column=5, value=f"=C{r}+D{r}")
    r += 1
    ws.cell(row=r, column=2, value="TOTAL").font = Font(bold=True, color=NAVY)
    ws.cell(row=r, column=3, value=f"=SUM(C{oa_start}:C{r-1})")
    ws.cell(row=r, column=4, value=f"=SUM(D{oa_start}:D{r-1})")
    ws.cell(row=r, column=5, value=f"=C{r}+D{r}")
    for rx in range(oa_start, r + 1):
        fill = WHITE if (rx - oa_start) % 2 == 0 else GREY
        for cx in range(2, 6):
            cell = ws.cell(row=rx, column=cx)
            cell.border = BORDER
            if cx >= 3: money(cell)
            if rx == r:
                cell.fill = PatternFill("solid", fgColor=GOLD_SOFT)
                cell.font = Font(bold=True, color=NAVY)
            else:
                cell.fill = PatternFill("solid", fgColor=fill)

    # ============================================================
    # HOJA POR CATEGORIA (Grupo -> Subgrupo anidado, con formulas)
    # ============================================================
    ws2 = wb.create_sheet("Por categoría")
    ws2.sheet_view.showGridLines = False
    set_widths(ws2, [3, 30, 34, 18, 16, 18, 11])
    title_cell(ws2, "B2", "GASTO POR CATEGORÍA (GRUPO Y SUBGRUPO)", size=14); ws2.merge_cells("B2:G2")
    ws2["B3"].value = "Cada grupo se abre en sus subgrupos. Los valores son fórmulas SUMAR.SI.CONJUNTO sobre la hoja Detalle."
    ws2["B3"].font = Font(italic=True, size=9, color="5A6472"); ws2.merge_cells("B3:G3")

    hr = 5
    header_row(ws2, hr, ["Grupo", "Subgrupo", "Valor sin IVA", "IVA", "Total con IVA", "% del total"], start_col=2)
    rr = hr + 1
    data_start = rr
    grupo_rows = []  # filas de subtotal de grupo (para el grafico)
    # orden: grupos por gasto desc, y dentro subgrupos por gasto desc
    grupos_ordenados = sorted(grp_val.keys(), key=lambda g: -grp_val[g])
    for g in grupos_ordenados:
        # fila de grupo (subtotal por formula)
        gr = rr
        ws2.cell(row=gr, column=2, value=g).font = Font(bold=True, color=NAVY)
        c = ws2.cell(row=gr, column=4, value=f'=SUMIFS({RNG_VALOR},{RNG_GRUPO},$B{gr})'); money(c); c.font = Font(bold=True, color=NAVY)
        c = ws2.cell(row=gr, column=5, value=f'=SUMIFS({RNG_IVA},{RNG_GRUPO},$B{gr})'); money(c); c.font = Font(bold=True, color=NAVY)
        c = ws2.cell(row=gr, column=6, value=f"=D{gr}+E{gr}"); money(c); c.font = Font(bold=True, color=NAVY)
        c = ws2.cell(row=gr, column=7, value=f"=IF({TOT_VALOR}=0,0,D{gr}/{TOT_VALOR})"); c.number_format = PCT_FMT
        c.alignment = Alignment(horizontal="center"); c.font = Font(bold=True, color=NAVY)
        for cx in range(2, 8):
            cell = ws2.cell(row=gr, column=cx)
            cell.fill = PatternFill("solid", fgColor=GOLD_SOFT); cell.border = BORDER
        grupo_rows.append(gr)
        rr += 1
        # subgrupos de este grupo
        subs = sorted([(s, val) for (gg, s), val in sub_val.items() if gg == g], key=lambda x: -x[1])
        for s, _v in subs:
            ws2.cell(row=rr, column=3, value=s).alignment = Alignment(indent=1)
            c = ws2.cell(row=rr, column=4, value=f'=SUMIFS({RNG_VALOR},{RNG_GRUPO},$B{gr},{RNG_SUBG},$C{rr})'); money(c)
            c = ws2.cell(row=rr, column=5, value=f'=SUMIFS({RNG_IVA},{RNG_GRUPO},$B{gr},{RNG_SUBG},$C{rr})'); money(c)
            c = ws2.cell(row=rr, column=6, value=f"=D{rr}+E{rr}"); money(c)
            c = ws2.cell(row=rr, column=7, value=f"=IF({TOT_VALOR}=0,0,D{rr}/{TOT_VALOR})"); c.number_format = PCT_FMT
            c.alignment = Alignment(horizontal="center")
            for cx in range(2, 8):
                cell = ws2.cell(row=rr, column=cx)
                cell.fill = PatternFill("solid", fgColor=SUBFILL); cell.border = BORDER
            rr += 1
    data_end = rr - 1
    # fila TOTAL
    ws2.cell(row=rr, column=2, value="TOTAL").font = Font(bold=True, color=NAVY)
    # total = suma de las filas de grupo
    grp_sum_valor = "+".join([f"D{gr}" for gr in grupo_rows])
    grp_sum_iva = "+".join([f"E{gr}" for gr in grupo_rows])
    c = ws2.cell(row=rr, column=4, value=f"={grp_sum_valor}"); money(c)
    c = ws2.cell(row=rr, column=5, value=f"={grp_sum_iva}"); money(c)
    c = ws2.cell(row=rr, column=6, value=f"=D{rr}+E{rr}"); money(c)
    c = ws2.cell(row=rr, column=7, value=1.0); c.number_format = PCT_FMT; c.alignment = Alignment(horizontal="center")
    for cx in range(2, 8):
        cell = ws2.cell(row=rr, column=cx)
        cell.fill = PatternFill("solid", fgColor=GOLD); cell.font = Font(bold=True, color=NAVY); cell.border = BORDER

    # grafico torta: solo filas de grupo. Usamos rangos discontinuos via serie de datos manual.
    # openpyxl no soporta rangos discontinuos facilmente; construimos una mini-tabla auxiliar oculta.
    aux_col = 9  # columna I
    ws2.cell(row=hr, column=aux_col, value="_grupo").font = Font(color="FFFFFF")
    ws2.cell(row=hr, column=aux_col + 1, value="_valor").font = Font(color="FFFFFF")
    ar = hr + 1
    for gr in grupo_rows:
        ws2.cell(row=ar, column=aux_col, value=f"=B{gr}")
        ws2.cell(row=ar, column=aux_col + 1, value=f"=D{gr}")
        ar += 1
    aux_end = ar - 1
    # ocultar columnas auxiliares
    ws2.column_dimensions[get_column_letter(aux_col)].hidden = True
    ws2.column_dimensions[get_column_letter(aux_col + 1)].hidden = True
    pie = PieChart(); pie.title = "Distribución por grupo (valor sin IVA)"
    labels = Reference(ws2, min_col=aux_col, min_row=hr + 1, max_row=aux_end)
    data = Reference(ws2, min_col=aux_col + 1, min_row=hr, max_row=aux_end)
    pie.add_data(data, titles_from_data=True); pie.set_categories(labels)
    pie.height = 10; pie.width = 17
    ws2.add_chart(pie, "B" + str(data_end + 3))

    # ============================================================
    # HOJA POR TIPO DE ITEM (categorizacion de lo que se compro)
    # Resumen por categoria + detalle de items (con CANTIDAD) dentro de cada una.
    # Valores por formula SUMAR.SI.CONJUNTO sobre Detalle.
    # ============================================================
    wsi = wb.create_sheet("Por tipo de ítem")
    wsi.sheet_view.showGridLines = False
    set_widths(wsi, [3, 52, 12, 20, 16, 18, 11])
    title_cell(wsi, "B2", "¿QUÉ SE COMPRÓ? — CATEGORIZACIÓN DE ÍTEMS", size=14); wsi.merge_cells("B2:G2")
    wsi["B3"].value = ("Los ítems se agrupan por tipo (transformadores, medidores, inversores, cable, etc.). "
                       "Se muestra la cantidad total y el valor. Cantidades y valores son fórmulas sobre la hoja Detalle.")
    wsi["B3"].font = Font(italic=True, size=9, color="5A6472"); wsi.merge_cells("B3:G3")

    # ---- Tabla A: resumen por categoria ----
    hr = 5
    wsi.cell(row=hr, column=2, value="RESUMEN POR CATEGORÍA").font = Font(bold=True, size=12, color=NAVY)
    hr += 1
    header_row(wsi, hr, ["Categoría de ítem", "Cant. total", "Valor sin IVA", "IVA", "Total con IVA", "% del total"], start_col=2)
    ds = hr + 1; rr = ds
    cats_ordenadas = sorted(cat_val.keys(), key=lambda c: -cat_val[c][1])
    for cat in cats_ordenadas:
        wsi.cell(row=rr, column=2, value=cat)
        c = wsi.cell(row=rr, column=3, value=f'=SUMIFS({RNG_CANT},{RNG_CAT},$B{rr})'); c.number_format = '#,##0.##'; c.alignment = Alignment(horizontal="right")
        c = wsi.cell(row=rr, column=4, value=f'=SUMIFS({RNG_VALOR},{RNG_CAT},$B{rr})'); money(c)
        c = wsi.cell(row=rr, column=5, value=f'=SUMIFS({RNG_IVA},{RNG_CAT},$B{rr})'); money(c)
        c = wsi.cell(row=rr, column=6, value=f"=D{rr}+E{rr}"); money(c)
        c = wsi.cell(row=rr, column=7, value=f"=IF({TOT_VALOR}=0,0,D{rr}/{TOT_VALOR})"); c.number_format = PCT_FMT; c.alignment = Alignment(horizontal="center")
        rr += 1
    de = rr - 1
    wsi.cell(row=rr, column=2, value="TOTAL").font = Font(bold=True, color=NAVY)
    c = wsi.cell(row=rr, column=3, value=f"=SUM(C{ds}:C{de})"); c.number_format = '#,##0.##'; c.alignment = Alignment(horizontal="right")
    c = wsi.cell(row=rr, column=4, value=f"=SUM(D{ds}:D{de})"); money(c)
    c = wsi.cell(row=rr, column=5, value=f"=SUM(E{ds}:E{de})"); money(c)
    c = wsi.cell(row=rr, column=6, value=f"=D{rr}+E{rr}"); money(c)
    c = wsi.cell(row=rr, column=7, value=1.0); c.number_format = PCT_FMT; c.alignment = Alignment(horizontal="center")
    for rx in range(ds, rr + 1):
        fill = WHITE if (rx - ds) % 2 == 0 else GREY
        for cx in range(2, 8):
            cell = wsi.cell(row=rx, column=cx); cell.border = BORDER
            if rx == rr:
                cell.fill = PatternFill("solid", fgColor=GOLD); cell.font = Font(bold=True, color=NAVY)
            else:
                cell.fill = PatternFill("solid", fgColor=fill)
    resumen_total_row = rr

    # torta por categoria de item
    pie2 = PieChart(); pie2.title = "Distribución por tipo de ítem (valor sin IVA)"
    labels = Reference(wsi, min_col=2, min_row=ds, max_row=de)
    data = Reference(wsi, min_col=4, min_row=hr, max_row=de)
    pie2.add_data(data, titles_from_data=True); pie2.set_categories(labels)
    pie2.height = 10; pie2.width = 17
    wsi.add_chart(pie2, "I5")

    # ---- Tabla B: detalle de items por categoria (con cantidades) ----
    rr = resumen_total_row + 3
    wsi.cell(row=rr, column=2, value="DETALLE DE ÍTEMS POR CATEGORÍA").font = Font(bold=True, size=12, color=NAVY)
    rr += 1
    wsi.cell(row=rr, column=2, value="Aquí se ve, por ejemplo, cuántos transformadores, medidores o inversores consumió el proyecto.").font = Font(italic=True, size=9, color="5A6472")
    rr += 1
    header_row(wsi, rr, ["Categoría / Ítem", "Cant.", "Valor sin IVA", "IVA", "Total con IVA"], start_col=2)
    rr += 1
    for cat in cats_ordenadas:
        # encabezado de categoria
        gr = rr
        wsi.cell(row=gr, column=2, value=cat).font = Font(bold=True, color=NAVY)
        c = wsi.cell(row=gr, column=3, value=f'=SUMIFS({RNG_CANT},{RNG_CAT},$B{gr})'); c.number_format = '#,##0.##'; c.alignment = Alignment(horizontal="right"); c.font = Font(bold=True, color=NAVY)
        c = wsi.cell(row=gr, column=4, value=f'=SUMIFS({RNG_VALOR},{RNG_CAT},$B{gr})'); money(c); c.font = Font(bold=True, color=NAVY)
        c = wsi.cell(row=gr, column=5, value=f'=SUMIFS({RNG_IVA},{RNG_CAT},$B{gr})'); money(c); c.font = Font(bold=True, color=NAVY)
        c = wsi.cell(row=gr, column=6, value=f"=D{gr}+E{gr}"); money(c); c.font = Font(bold=True, color=NAVY)
        for cx in range(2, 7):
            cell = wsi.cell(row=gr, column=cx); cell.fill = PatternFill("solid", fgColor=GOLD_SOFT); cell.border = BORDER
        rr += 1
        prods = sorted([(pr, qv) for (cc, pr), qv in catprod_val.items() if cc == cat], key=lambda x: -x[1][1])
        for pr, _qv in prods:
            wsi.cell(row=rr, column=2, value=pr).alignment = Alignment(indent=1, wrap_text=False)
            # SUMIFS por categoria + producto exacto (usamos columna auxiliar de texto)
            c = wsi.cell(row=rr, column=3, value=f'=SUMIFS({RNG_CANT},{RNG_CAT},$B{gr},{RNG_PROD},$B{rr})'); c.number_format = '#,##0.##'; c.alignment = Alignment(horizontal="right")
            c = wsi.cell(row=rr, column=4, value=f'=SUMIFS({RNG_VALOR},{RNG_CAT},$B{gr},{RNG_PROD},$B{rr})'); money(c)
            c = wsi.cell(row=rr, column=5, value=f'=SUMIFS({RNG_IVA},{RNG_CAT},$B{gr},{RNG_PROD},$B{rr})'); money(c)
            c = wsi.cell(row=rr, column=6, value=f"=D{rr}+E{rr}"); money(c)
            for cx in range(2, 7):
                cell = wsi.cell(row=rr, column=cx); cell.fill = PatternFill("solid", fgColor=SUBFILL); cell.border = BORDER
            rr += 1

    # ============================================================
    # HOJA POR PROVEEDOR (con formulas)
    # ============================================================
    ws3 = wb.create_sheet("Por proveedor")
    ws3.sheet_view.showGridLines = False
    set_widths(ws3, [3, 48, 20, 16, 18, 11])
    title_cell(ws3, "B2", "GASTO POR PROVEEDOR", size=14); ws3.merge_cells("B2:F2")
    ws3["B3"].value = "Valores calculados con SUMAR.SI.CONJUNTO sobre la hoja Detalle."
    ws3["B3"].font = Font(italic=True, size=9, color="5A6472"); ws3.merge_cells("B3:F3")
    hr = 5
    header_row(ws3, hr, ["Proveedor", "Valor sin IVA", "IVA", "Total con IVA", "% del total"], start_col=2)
    ds = hr + 1; rr = ds
    for p in sorted(prov_val.keys(), key=lambda x: -prov_val[x]):
        ws3.cell(row=rr, column=2, value=p)
        c = ws3.cell(row=rr, column=3, value=f'=SUMIFS({RNG_VALOR},{RNG_PROV},$B{rr})'); money(c)
        c = ws3.cell(row=rr, column=4, value=f'=SUMIFS({RNG_IVA},{RNG_PROV},$B{rr})'); money(c)
        c = ws3.cell(row=rr, column=5, value=f"=C{rr}+D{rr}"); money(c)
        c = ws3.cell(row=rr, column=6, value=f"=IF({TOT_VALOR}=0,0,C{rr}/{TOT_VALOR})"); c.number_format = PCT_FMT
        c.alignment = Alignment(horizontal="center")
        rr += 1
    de = rr - 1
    ws3.cell(row=rr, column=2, value="TOTAL").font = Font(bold=True, color=NAVY)
    c = ws3.cell(row=rr, column=3, value=f"=SUM(C{ds}:C{de})"); money(c)
    c = ws3.cell(row=rr, column=4, value=f"=SUM(D{ds}:D{de})"); money(c)
    c = ws3.cell(row=rr, column=5, value=f"=C{rr}+D{rr}"); money(c)
    c = ws3.cell(row=rr, column=6, value=1.0); c.number_format = PCT_FMT; c.alignment = Alignment(horizontal="center")
    for rx in range(ds, rr + 1):
        fill = WHITE if (rx - ds) % 2 == 0 else GREY
        for cx in range(2, 7):
            cell = ws3.cell(row=rx, column=cx); cell.border = BORDER
            if rx == rr:
                cell.fill = PatternFill("solid", fgColor=GOLD_SOFT); cell.font = Font(bold=True, color=NAVY)
            else:
                cell.fill = PatternFill("solid", fgColor=fill)
    top_n = min(10, de - ds + 1)
    bar = BarChart(); bar.type = "bar"; bar.title = "Top proveedores (valor sin IVA)"
    labels = Reference(ws3, min_col=2, min_row=ds, max_row=ds + top_n - 1)
    data = Reference(ws3, min_col=3, min_row=hr, max_row=ds + top_n - 1)
    bar.add_data(data, titles_from_data=True); bar.set_categories(labels)
    bar.height = 9; bar.width = 18; bar.legend = None
    ws3.add_chart(bar, "H5")

    # ============================================================
    # HOJA POR ESTADO (con formulas)
    # ============================================================
    ws4 = wb.create_sheet("Por estado")
    ws4.sheet_view.showGridLines = False
    set_widths(ws4, [3, 30, 22, 6, 30, 22])
    title_cell(ws4, "B2", "COMPRAS POR ESTADO Y LEGALIZACIÓN", size=14); ws4.merge_cells("B2:F2")

    def mini_table(ws, top, left, title, keys, rng):
        ws.cell(row=top, column=left, value=title).font = Font(bold=True, size=11, color=NAVY)
        header_row(ws, top + 1, ["Concepto", "Valor sin IVA"], start_col=left)
        r0 = top + 2; rr = r0
        for k in keys:
            ws.cell(row=rr, column=left, value=k)
            c = ws.cell(row=rr, column=left + 1, value=f'=SUMIFS({RNG_VALOR},{rng},{get_column_letter(left)}{rr})')
            money(c)
            rr += 1
        rend = rr - 1
        ws.cell(row=rr, column=left, value="TOTAL").font = Font(bold=True, color=NAVY)
        c = ws.cell(row=rr, column=left + 1, value=f"=SUM({get_column_letter(left+1)}{r0}:{get_column_letter(left+1)}{rend})")
        money(c); c.font = Font(bold=True, color=NAVY)
        for rx in range(r0, rr + 1):
            fill = WHITE if (rx - r0) % 2 == 0 else GREY
            for j in (left, left + 1):
                cell = ws.cell(row=rx, column=j); cell.border = BORDER
                if rx == rr:
                    cell.fill = PatternFill("solid", fgColor=GOLD_SOFT); cell.font = Font(bold=True, color=NAVY)
                else:
                    cell.fill = PatternFill("solid", fgColor=fill)

    mini_table(ws4, 4, 2, "Por estado de la orden", list(estados_set.keys()), RNG_ESTADO)
    mini_table(ws4, 4, 5, "Por estado de legalización", list(legal_set.keys()), RNG_LEGAL)
    base_row = 4 + max(len(estados_set), len(legal_set)) + 5
    mini_table(ws4, base_row, 2, "Por tipo de solicitud", list(tsol_set.keys()), RNG_TSOL)

    # reordenar hojas
    orden = ["Resumen", "Por categoría", "Por tipo de ítem", "Por proveedor", "Por estado", "Detalle"]
    wb._sheets.sort(key=lambda s: orden.index(s.title))

    out_path = os.path.join(BASE, out_name)
    wb.save(out_path)
    print(f"OK -> {out_name}  (filas detalle: {last-1})")
    return out_path


if __name__ == "__main__":
    build(
        "PROYECTO POLARIS 4  —  MINIGRANJAS",
        "Tipo de proyecto: Mini Granjas · Exportación de órdenes de compra",
        "POLARIS 4 - MINIGRANJA.xlsx",
        "INFORME DE COMPRAS - POLARIS 4 (MINIGRANJA).xlsx",
    )
    build(
        "PROYECTO MULTICENTRO  —  TECHOS",
        "Tipo de proyecto: Techo · Exportación de órdenes de compra",
        "MULTICENTRO - TECHOS.xlsx",
        "INFORME DE COMPRAS - MULTICENTRO (TECHOS).xlsx",
    )
