# -*- coding: utf-8 -*-
"""
Generador de informe de compras Evolti (uno por proyecto).
Lee la exportacion de ordenes de compra y produce un Excel con:
  - Portada / Resumen ejecutivo
  - Obra vs Administrativo
  - Por categoria (Grupo)
  - Por proveedor
  - Por estado / legalizacion
  - Detalle completo
  - Graficos (torta categorias, barras proveedores, barras obra/admin)
"""
import os
from collections import defaultdict
from datetime import datetime

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, NamedStyle
from openpyxl.utils import get_column_letter
from openpyxl.chart import PieChart, BarChart, Reference

BASE = os.path.dirname(__file__)

# ---- Paleta de marca (navy / dorado) ----
NAVY = "0B1F3A"
NAVY2 = "13345C"
GOLD = "C9A227"
GOLD_SOFT = "F3ECCF"
GREY = "F2F4F7"
WHITE = "FFFFFF"
LINE = "D8DEE6"

thin = Side(style="thin", color=LINE)
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

MONEY_FMT = '#,##0 "COP"'
INT_FMT = '#,##0'
PCT_FMT = '0.0%'

COLS = ["Fecha de registro","No OC","No de pedido","Estado","Estado de legalizacion",
        "Grupo","Sub grupo","Nombre del producto o servicio","Cantidad","Precio",
        "Vlr total","Tipo de impuesto","Vlr impuesto","Nombre de quien realiza la orden",
        "Seleccione el proveedor","Tipo de solicitud","Tipo de proyecto","Proyecto",
        "No de factura","Soporte de factura"]

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

# ---------- estilos de celda ----------
def title_cell(ws, cell, text, size=16, color=WHITE, fill=NAVY, align="left"):
    c = ws[cell]
    c.value = text
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

def zebra(ws, r0, r1, c0, c1):
    for r in range(r0, r1 + 1):
        fill = WHITE if (r - r0) % 2 == 0 else GREY
        for c in range(c0, c1 + 1):
            cell = ws.cell(row=r, column=c)
            cell.fill = PatternFill("solid", fgColor=fill)
            cell.border = BORDER

def set_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

# ================= construccion de un proyecto =================
def build(project_label, project_sub, filename, out_name):
    path = os.path.join(BASE, filename)
    rows = read_rows(path)

    # --- agregaciones ---
    total_valor = total_iva = 0.0
    n_items = len(rows)
    ocs = set()
    fechas = []

    grupos = defaultdict(lambda: [0.0, 0.0])       # grupo -> [valor, iva]
    provs = defaultdict(lambda: [0.0, 0.0])
    estados = defaultdict(float)
    legal = defaultdict(float)
    tiposol = defaultdict(float)
    tipoproy = defaultdict(lambda: [0.0, 0.0])     # OBRA / ADMINISTRATIVO

    for r in rows:
        (fecha, noOC, noPed, estado, estleg, grupo, subg, prod, cant, precio,
         vtot, tipimp, vimp, quien, prov, tsol, tproy, proy, nofact, sop) = r
        v = num(vtot); iva = num(vimp)
        total_valor += v; total_iva += iva
        if noOC is not None: ocs.add(noOC)
        if isinstance(fecha, datetime): fechas.append(fecha)
        grupos[clean(grupo) or "(sin grupo)"][0] += v
        grupos[clean(grupo) or "(sin grupo)"][1] += iva
        provs[clean(prov) or "(sin proveedor)"][0] += v
        provs[clean(prov) or "(sin proveedor)"][1] += iva
        estados[clean(estado) or "(vacío)"] += v
        legal[clean(estleg) or "(vacío)"] += v
        tiposol[clean(tsol) or "(vacío)"] += v
        tp = clean(tproy).upper()
        cat = "ADMINISTRATIVO" if tp == "ADMINISTRATIVO" else "OBRA"
        tipoproy[cat][0] += v
        tipoproy[cat][1] += iva

    total_con_iva = total_valor + total_iva
    fmin = min(fechas).date() if fechas else "-"
    fmax = max(fechas).date() if fechas else "-"

    wb = openpyxl.Workbook()

    # ---------------- HOJA 1: RESUMEN ----------------
    ws = wb.active
    ws.title = "Resumen"
    ws.sheet_view.showGridLines = False
    set_widths(ws, [3, 34, 22, 22, 22, 4])

    title_cell(ws, "B2", "EVOLTI  ·  INFORME DE COMPRAS", size=18)
    ws.merge_cells("B2:E2")
    title_cell(ws, "B3", f"{project_label}", size=13, color=GOLD, fill=NAVY)
    ws.merge_cells("B3:E3")
    ws["B4"].value = project_sub
    ws["B4"].font = Font(italic=True, size=10, color="5A6472")
    ws.merge_cells("B4:E4")
    ws["B5"].value = f"Periodo: {fmin}  a  {fmax}    ·    Generado: {datetime.now().date()}    ·    Moneda: COP"
    ws["B5"].font = Font(size=9, color="5A6472")
    ws.merge_cells("B5:E5")

    # tarjetas de totales
    r = 7
    cards = [
        ("VALOR TOTAL (sin IVA)", total_valor, MONEY_FMT, GOLD_SOFT),
        ("IVA", total_iva, MONEY_FMT, GOLD_SOFT),
        ("TOTAL CON IVA", total_con_iva, MONEY_FMT, GOLD),
    ]
    ws[f"B{r}"].value = "TOTALES DEL PROYECTO"
    ws[f"B{r}"].font = Font(bold=True, size=12, color=NAVY)
    r += 1
    for label, val, fmt, fill in cards:
        ws.cell(row=r, column=2, value=label).font = Font(bold=True, size=11, color=NAVY)
        c = ws.cell(row=r, column=4, value=val)
        c.number_format = fmt
        c.font = Font(bold=True, size=12, color=NAVY)
        c.alignment = Alignment(horizontal="right")
        for cc in range(2, 5):
            cell = ws.cell(row=r, column=cc)
            cell.fill = PatternFill("solid", fgColor=fill)
            cell.border = BORDER
        ws.cell(row=r, column=3).fill = PatternFill("solid", fgColor=fill)
        ws.cell(row=r, column=3).border = BORDER
        r += 1

    r += 1
    ws.cell(row=r, column=2, value="INDICADORES").font = Font(bold=True, size=12, color=NAVY)
    r += 1
    indics = [
        ("Órdenes de compra (No OC únicas)", len(ocs), INT_FMT),
        ("Líneas de ítem / compras", n_items, INT_FMT),
        ("Proveedores distintos", len(provs), INT_FMT),
        ("Categorías (Grupos)", len(grupos), INT_FMT),
    ]
    for label, val, fmt in indics:
        ws.cell(row=r, column=2, value=label).font = Font(size=11, color=NAVY)
        c = ws.cell(row=r, column=4, value=val); c.number_format = fmt
        c.alignment = Alignment(horizontal="right"); c.font = Font(bold=True, color=NAVY)
        for cc in range(2, 5):
            ws.cell(row=r, column=cc).border = BORDER
        r += 1

    # Obra vs administrativo
    r += 1
    ws.cell(row=r, column=2, value="GASTO DE OBRA vs ADMINISTRATIVO").font = Font(bold=True, size=12, color=NAVY)
    r += 1
    header_row(ws, r, ["Concepto", "Valor sin IVA", "IVA", "Total con IVA"], start_col=2)
    r += 1
    oa_start = r
    for cat in ["OBRA", "ADMINISTRATIVO"]:
        v, iva = tipoproy.get(cat, [0.0, 0.0])
        ws.cell(row=r, column=2, value=("Gasto de obra" if cat=="OBRA" else "Gasto administrativo"))
        for j, val in enumerate([v, iva, v + iva], start=3):
            c = ws.cell(row=r, column=j, value=val); c.number_format = MONEY_FMT
            c.alignment = Alignment(horizontal="right")
        r += 1
    # fila total
    ws.cell(row=r, column=2, value="TOTAL").font = Font(bold=True, color=NAVY)
    for j, val in enumerate([total_valor, total_iva, total_con_iva], start=3):
        c = ws.cell(row=r, column=j, value=val); c.number_format = MONEY_FMT
        c.font = Font(bold=True, color=NAVY); c.alignment = Alignment(horizontal="right")
    zebra(ws, oa_start, r, 2, 5)
    ws.cell(row=oa_start + 2, column=2).font = Font(bold=True, color=NAVY)  # keep TOTAL bold
    # re-apply bold on total row after zebra
    for j in range(2, 6):
        ws.cell(row=r, column=j).font = Font(bold=True, color=NAVY)
        ws.cell(row=r, column=j).fill = PatternFill("solid", fgColor=GOLD_SOFT)

    # ---------------- HOJA 2: POR CATEGORIA ----------------
    ws2 = wb.create_sheet("Por categoría")
    ws2.sheet_view.showGridLines = False
    set_widths(ws2, [3, 40, 20, 18, 20, 12])
    title_cell(ws2, "B2", "GASTO POR CATEGORÍA (GRUPO)", size=14)
    ws2.merge_cells("B2:F2")
    hr = 4
    header_row(ws2, hr, ["Categoría (Grupo)", "Valor sin IVA", "IVA", "Total con IVA", "% del total"], start_col=2)
    data_start = hr + 1
    rr = data_start
    for g, (v, iva) in sorted(grupos.items(), key=lambda x: -x[1][0]):
        ws2.cell(row=rr, column=2, value=g)
        c = ws2.cell(row=rr, column=3, value=v); c.number_format = MONEY_FMT
        c = ws2.cell(row=rr, column=4, value=iva); c.number_format = MONEY_FMT
        c = ws2.cell(row=rr, column=5, value=v + iva); c.number_format = MONEY_FMT
        c = ws2.cell(row=rr, column=6, value=(v / total_valor if total_valor else 0)); c.number_format = PCT_FMT
        rr += 1
    data_end = rr - 1
    # total
    ws2.cell(row=rr, column=2, value="TOTAL").font = Font(bold=True, color=NAVY)
    for j, val in [(3, total_valor), (4, total_iva), (5, total_con_iva)]:
        c = ws2.cell(row=rr, column=j, value=val); c.number_format = MONEY_FMT; c.font = Font(bold=True, color=NAVY)
    c = ws2.cell(row=rr, column=6, value=1.0); c.number_format = PCT_FMT; c.font = Font(bold=True, color=NAVY)
    zebra(ws2, data_start, rr, 2, 6)
    for j in range(2, 7):
        ws2.cell(row=rr, column=j).fill = PatternFill("solid", fgColor=GOLD_SOFT)
        ws2.cell(row=rr, column=j).font = Font(bold=True, color=NAVY)
    for rx in range(data_start, rr + 1):
        for cx in range(3, 6):
            ws2.cell(row=rx, column=cx).alignment = Alignment(horizontal="right")
        ws2.cell(row=rx, column=6).alignment = Alignment(horizontal="center")

    # grafico torta categorias
    pie = PieChart()
    pie.title = "Distribución por categoría (valor sin IVA)"
    labels = Reference(ws2, min_col=2, min_row=data_start, max_row=data_end)
    data = Reference(ws2, min_col=3, min_row=hr, max_row=data_end)
    pie.add_data(data, titles_from_data=True)
    pie.set_categories(labels)
    pie.height = 9; pie.width = 16
    ws2.add_chart(pie, "H4")

    # ---------------- HOJA 3: POR PROVEEDOR ----------------
    ws3 = wb.create_sheet("Por proveedor")
    ws3.sheet_view.showGridLines = False
    set_widths(ws3, [3, 48, 20, 18, 20, 12])
    title_cell(ws3, "B2", "GASTO POR PROVEEDOR", size=14)
    ws3.merge_cells("B2:F2")
    hr = 4
    header_row(ws3, hr, ["Proveedor", "Valor sin IVA", "IVA", "Total con IVA", "% del total"], start_col=2)
    ds = hr + 1; rr = ds
    prov_sorted = sorted(provs.items(), key=lambda x: -x[1][0])
    for p, (v, iva) in prov_sorted:
        ws3.cell(row=rr, column=2, value=p)
        c = ws3.cell(row=rr, column=3, value=v); c.number_format = MONEY_FMT
        c = ws3.cell(row=rr, column=4, value=iva); c.number_format = MONEY_FMT
        c = ws3.cell(row=rr, column=5, value=v + iva); c.number_format = MONEY_FMT
        c = ws3.cell(row=rr, column=6, value=(v / total_valor if total_valor else 0)); c.number_format = PCT_FMT
        rr += 1
    de = rr - 1
    ws3.cell(row=rr, column=2, value="TOTAL").font = Font(bold=True, color=NAVY)
    for j, val in [(3, total_valor), (4, total_iva), (5, total_con_iva)]:
        c = ws3.cell(row=rr, column=j, value=val); c.number_format = MONEY_FMT; c.font = Font(bold=True, color=NAVY)
    c = ws3.cell(row=rr, column=6, value=1.0); c.number_format = PCT_FMT; c.font = Font(bold=True, color=NAVY)
    zebra(ws3, ds, rr, 2, 6)
    for j in range(2, 7):
        ws3.cell(row=rr, column=j).fill = PatternFill("solid", fgColor=GOLD_SOFT)
        ws3.cell(row=rr, column=j).font = Font(bold=True, color=NAVY)
    for rx in range(ds, rr + 1):
        for cx in range(3, 6):
            ws3.cell(row=rx, column=cx).alignment = Alignment(horizontal="right")
        ws3.cell(row=rx, column=6).alignment = Alignment(horizontal="center")

    # grafico barras top 10 proveedores
    top_n = min(10, de - ds + 1)
    bar = BarChart(); bar.type = "bar"; bar.title = "Top proveedores (valor sin IVA)"
    labels = Reference(ws3, min_col=2, min_row=ds, max_row=ds + top_n - 1)
    data = Reference(ws3, min_col=3, min_row=hr, max_row=ds + top_n - 1)
    bar.add_data(data, titles_from_data=True); bar.set_categories(labels)
    bar.height = 9; bar.width = 18; bar.legend = None
    ws3.add_chart(bar, "H4")

    # ---------------- HOJA 4: POR ESTADO ----------------
    ws4 = wb.create_sheet("Por estado")
    ws4.sheet_view.showGridLines = False
    set_widths(ws4, [3, 30, 22, 6, 30, 22])
    title_cell(ws4, "B2", "COMPRAS POR ESTADO Y LEGALIZACIÓN", size=14)
    ws4.merge_cells("B2:F2")

    def mini_table(ws, top, left, title, d):
        ws.cell(row=top, column=left, value=title).font = Font(bold=True, size=11, color=NAVY)
        header_row(ws, top + 1, ["Concepto", "Valor sin IVA"], start_col=left)
        r0 = top + 2; rr = r0
        for k, v in sorted(d.items(), key=lambda x: -x[1]):
            ws.cell(row=rr, column=left, value=k)
            c = ws.cell(row=rr, column=left + 1, value=v); c.number_format = MONEY_FMT
            c.alignment = Alignment(horizontal="right")
            rr += 1
        ws.cell(row=rr, column=left, value="TOTAL").font = Font(bold=True, color=NAVY)
        c = ws.cell(row=rr, column=left + 1, value=sum(d.values())); c.number_format = MONEY_FMT
        c.font = Font(bold=True, color=NAVY); c.alignment = Alignment(horizontal="right")
        zebra(ws, r0, rr, left, left + 1)
        for j in (left, left + 1):
            ws.cell(row=rr, column=j).fill = PatternFill("solid", fgColor=GOLD_SOFT)
            ws.cell(row=rr, column=j).font = Font(bold=True, color=NAVY)

    mini_table(ws4, 4, 2, "Por estado de la orden", estados)
    mini_table(ws4, 4, 5, "Por estado de legalización", legal)
    mini_table(ws4, 4 + max(len(estados), len(legal)) + 5, 2, "Por tipo de solicitud", tiposol)

    # ---------------- HOJA 5: DETALLE ----------------
    ws5 = wb.create_sheet("Detalle")
    ws5.sheet_view.showGridLines = False
    detail_cols = ["Fecha","No OC","No pedido","Estado","Legalización","Grupo","Sub grupo",
                   "Producto / servicio","Cant.","Precio unit.","Valor sin IVA","Tipo impuesto",
                   "IVA","Total con IVA","Solicitó","Proveedor","Tipo solicitud","Tipo proyecto",
                   "No factura"]
    header_row(ws5, 1, detail_cols, start_col=1)
    ws5.freeze_panes = "A2"
    rr = 2
    for r in rows:
        (fecha, noOC, noPed, estado, estleg, grupo, subg, prod, cant, precio,
         vtot, tipimp, vimp, quien, prov, tsol, tproy, proy, nofact, sop) = r
        v = num(vtot); iva = num(vimp)
        vals = [fecha, noOC, noPed, clean(estado), clean(estleg), clean(grupo), clean(subg),
                clean(prod), num(cant), num(precio), v, clean(tipimp), iva, v + iva,
                clean(quien), clean(prov), clean(tsol), clean(tproy), clean(nofact)]
        for j, val in enumerate(vals, start=1):
            c = ws5.cell(row=rr, column=j, value=val)
            c.border = BORDER
            if j == 1 and isinstance(val, datetime):
                c.number_format = "yyyy-mm-dd"
            if j in (10, 11, 13, 14):
                c.number_format = MONEY_FMT
            if j == 9:
                c.number_format = '#,##0.##'
        rr += 1
    # zebra + column widths detalle
    for rx in range(2, rr):
        fill = WHITE if rx % 2 == 0 else GREY
        for cx in range(1, len(detail_cols) + 1):
            ws5.cell(row=rx, column=cx).fill = PatternFill("solid", fgColor=fill)
    widths = [12, 8, 9, 10, 12, 20, 18, 42, 7, 15, 16, 12, 14, 16, 22, 30, 13, 14, 16]
    set_widths(ws5, widths)
    ws5.auto_filter.ref = f"A1:{get_column_letter(len(detail_cols))}{rr-1}"

    out_path = os.path.join(BASE, out_name)
    wb.save(out_path)
    print(f"OK -> {out_name}")
    print(f"   valor sin IVA = {total_valor:,.0f} | IVA = {total_iva:,.0f} | total = {total_con_iva:,.0f}")
    print(f"   OBRA = {tipoproy['OBRA'][0]:,.0f} (sin IVA) | ADMIN = {tipoproy['ADMINISTRATIVO'][0]:,.0f} (sin IVA)")
    return total_valor, total_iva, total_con_iva


if __name__ == "__main__":
    build(
        "PROYECTO POLARIS 4  —  MINIGRANJAS",
        "Tipo de proyecto: Mini Granjas · Exportación de órdenes de compra",
        "POLARIS 4 - MINIGRANJA.xlsx",
        "INFORME DE COMPRAS - POLARIS 4 (MINIGRANJA).xlsx",
    )
    print()
    build(
        "PROYECTO MULTICENTRO  —  TECHOS",
        "Tipo de proyecto: Techo · Exportación de órdenes de compra",
        "MULTICENTRO - TECHOS.xlsx",
        "INFORME DE COMPRAS - MULTICENTRO (TECHOS).xlsx",
    )
