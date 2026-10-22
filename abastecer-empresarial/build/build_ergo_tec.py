# Ergonomía + Tecnología (una página) y Estanterías (página siguiente). Vista previa con
# fotos enviadas por Abastecer (recortadas y compuestas); las ilustraciones vectoriales quedan de respaldo.
import os, sys
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_epp_lineas as E
from build_epp_lineas import *
from build_canecas import shadow, poly_fill
from build_senalizacion import personalizada
from reportlab.lib.colors import HexColor, Color

DK, DK2 = HexColor("#1B2733"), HexColor("#2C3A48")
MT, MT2, MT3 = HexColor("#C9D0D7"), HexColor("#A9B3BD"), HexColor("#8A95A1")
GN, GN2 = HexColor("#16823C"), HexColor("#0F6A30")
YL = HexColor("#F2B705"); OR = HexColor("#E8752A")
SCR = HexColor("#1D3A5A")
MAXW = 1e9


def P(c, pts, col): poly_fill(c, pts, col)


# ---------- ilustraciones ----------
def ill_silla(c, cx, by, s):
    shadow(c, cx, by + s * 0.02, s * 0.7)
    # base estrella y ruedas
    c.setStrokeColor(MT3); c.setLineWidth(s * 0.035); c.setLineCap(1)
    for dx, dy in ((-0.34, 0.03), (-0.17, -0.0), (0.0, 0.05), (0.17, -0.0), (0.34, 0.03)):
        c.line(cx, by + s * 0.12, cx + s * dx, by + s * (0.05 + dy))
    c.setFillColor(DK)
    for dx in (-0.34, -0.17, 0.0, 0.17, 0.34):
        c.circle(cx + s * dx, by + s * 0.045, s * 0.032, stroke=0, fill=1)
    c.setFillColor(MT2); c.rect(cx - s * 0.025, by + s * 0.12, s * 0.05, s * 0.2, stroke=0, fill=1)
    # asiento
    c.setFillColor(DK); c.roundRect(cx - s * 0.27, by + s * 0.3, s * 0.54, s * 0.09, s * 0.04, stroke=0, fill=1)
    c.setFillColor(DK2); c.roundRect(cx - s * 0.27, by + s * 0.34, s * 0.54, s * 0.05, s * 0.025, stroke=0, fill=1)
    # brazos
    c.setFillColor(MT3)
    for sx in (-1, 1):
        c.rect(cx + sx * s * 0.25 - s * 0.015, by + s * 0.39, s * 0.03, s * 0.12, stroke=0, fill=1)
        c.setFillColor(DK); c.roundRect(cx + sx * s * 0.25 - s * 0.07, by + s * 0.5, s * 0.14, s * 0.035, s * 0.015, stroke=0, fill=1); c.setFillColor(MT3)
    # espaldar en malla
    c.setFillColor(MT2); c.rect(cx - s * 0.02, by + s * 0.38, s * 0.04, s * 0.1, stroke=0, fill=1)
    c.setFillColor(DK); c.roundRect(cx - s * 0.22, by + s * 0.46, s * 0.44, s * 0.46, s * 0.1, stroke=0, fill=1)
    c.setFillColor(DK2); c.roundRect(cx - s * 0.19, by + s * 0.49, s * 0.38, s * 0.40, s * 0.08, stroke=0, fill=1)
    c.setStrokeColor(HexColor("#3D4E60")); c.setLineWidth(s * 0.006)
    for k in range(1, 9):
        x = cx - s * 0.19 + k * s * 0.38 / 9; c.line(x, by + s * 0.51, x, by + s * 0.87)
    # soporte lumbar
    c.setFillColor(GN); c.roundRect(cx - s * 0.13, by + s * 0.56, s * 0.26, s * 0.05, s * 0.025, stroke=0, fill=1)
    # cabecero
    c.setFillColor(MT2); c.rect(cx - s * 0.015, by + s * 0.9, s * 0.03, s * 0.05, stroke=0, fill=1)
    c.setFillColor(DK); c.roundRect(cx - s * 0.13, by + s * 0.94, s * 0.26, s * 0.08, s * 0.035, stroke=0, fill=1)


def ill_base_portatil(c, cx, by, s):
    shadow(c, cx, by, s * 0.8)
    # soporte de aluminio
    P(c, [(cx - s * 0.38, by + s * 0.02), (cx + s * 0.38, by + s * 0.02), (cx + s * 0.3, by + s * 0.05), (cx - s * 0.3, by + s * 0.05)], MT3)
    c.setStrokeColor(MT2); c.setLineWidth(s * 0.03)
    c.line(cx - s * 0.2, by + s * 0.04, cx - s * 0.05, by + s * 0.3); c.line(cx + s * 0.2, by + s * 0.04, cx + s * 0.25, by + s * 0.2)
    # bandeja inclinada
    P(c, [(cx - s * 0.42, by + s * 0.18), (cx + s * 0.4, by + s * 0.32), (cx + s * 0.4, by + s * 0.35), (cx - s * 0.42, by + s * 0.21)], MT)
    # portátil
    P(c, [(cx - s * 0.36, by + s * 0.22), (cx + s * 0.34, by + s * 0.34), (cx + s * 0.34, by + s * 0.37), (cx - s * 0.36, by + s * 0.25)], DK2)
    P(c, [(cx - s * 0.36, by + s * 0.25), (cx - s * 0.3, by + s * 0.78), (cx + s * 0.4, by + s * 0.86), (cx + s * 0.34, by + s * 0.37)], DK)
    P(c, [(cx - s * 0.32, by + s * 0.29), (cx - s * 0.27, by + s * 0.74), (cx + s * 0.36, by + s * 0.81), (cx + s * 0.31, by + s * 0.39)], SCR)
    c.setFillColor(YL); c.setFillAlpha(0.9)
    P(c, [(cx - s * 0.22, by + s * 0.6), (cx + s * 0.02, by + s * 0.63), (cx + s * 0.02, by + s * 0.66), (cx - s * 0.22, by + s * 0.63)], YL)
    P(c, [(cx - s * 0.23, by + s * 0.5), (cx + s * 0.2, by + s * 0.55), (cx + s * 0.2, by + s * 0.58), (cx - s * 0.23, by + s * 0.53)], GN)
    c.setFillAlpha(1)


def ill_reposapies(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    c.setFillColor(MT3); c.roundRect(cx - s * 0.36, by + s * 0.02, s * 0.72, s * 0.06, s * 0.03, stroke=0, fill=1)
    c.setStrokeColor(MT2); c.setLineWidth(s * 0.04)
    c.line(cx - s * 0.28, by + s * 0.06, cx - s * 0.2, by + s * 0.2); c.line(cx + s * 0.28, by + s * 0.06, cx + s * 0.22, by + s * 0.34)
    P(c, [(cx - s * 0.42, by + s * 0.16), (cx + s * 0.42, by + s * 0.32), (cx + s * 0.42, by + s * 0.38), (cx - s * 0.42, by + s * 0.22)], DK)
    P(c, [(cx - s * 0.42, by + s * 0.22), (cx + s * 0.42, by + s * 0.38), (cx + s * 0.36, by + s * 0.42), (cx - s * 0.46, by + s * 0.26)], DK2)
    c.setStrokeColor(HexColor("#3D4E60")); c.setLineWidth(s * 0.012)
    for k in range(1, 8):
        t = k / 8
        x0 = cx - s * 0.44 + t * s * 0.84; c.line(x0, by + s * (0.235 + t * 0.16), x0 + s * 0.04, by + s * (0.245 + t * 0.16))
    c.setFillColor(GN); c.roundRect(cx - s * 0.08, by + s * 0.04, s * 0.16, s * 0.025, s * 0.012, stroke=0, fill=1)


def ill_portatil(c, cx, by, s):
    shadow(c, cx, by, s * 0.9)
    P(c, [(cx - s * 0.46, by + s * 0.03), (cx + s * 0.46, by + s * 0.03), (cx + s * 0.38, by + s * 0.09), (cx - s * 0.38, by + s * 0.09)], MT2)
    c.setFillColor(MT3); c.rect(cx - s * 0.46, by + s * 0.02, s * 0.92, s * 0.015, stroke=0, fill=1)
    c.setFillColor(DK); c.roundRect(cx - s * 0.36, by + s * 0.09, s * 0.72, s * 0.48, s * 0.03, stroke=0, fill=1)
    c.setFillColor(SCR); c.rect(cx - s * 0.33, by + s * 0.12, s * 0.66, s * 0.42, stroke=0, fill=1)
    c.setFillColor(YL); c.rect(cx - s * 0.26, by + s * 0.42, s * 0.2, s * 0.035, stroke=0, fill=1)
    c.setFillColor(GN); c.rect(cx - s * 0.26, by + s * 0.34, s * 0.34, s * 0.03, stroke=0, fill=1)
    c.setFillColor(MT); c.rect(cx - s * 0.26, by + s * 0.27, s * 0.26, s * 0.025, stroke=0, fill=1)
    c.setFillColor(HexColor("#2B4D73")); c.rect(cx + s * 0.1, by + s * 0.2, s * 0.17, s * 0.24, stroke=0, fill=1)


def ill_impresora(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    c.setFillColor(WHITE); c.setStrokeColor(MT); c.setLineWidth(s * 0.01)
    c.rect(cx - s * 0.2, by + s * 0.5, s * 0.4, s * 0.2, stroke=1, fill=1)  # papel entrada
    c.setFillColor(DK2); c.roundRect(cx - s * 0.42, by + s * 0.08, s * 0.84, s * 0.44, s * 0.05, stroke=0, fill=1)
    c.setFillColor(DK); c.roundRect(cx - s * 0.42, by + s * 0.08, s * 0.84, s * 0.12, s * 0.04, stroke=0, fill=1)
    c.setFillColor(MT3); c.rect(cx - s * 0.3, by + s * 0.25, s * 0.6, s * 0.03, stroke=0, fill=1)
    c.setFillColor(WHITE); P(c, [(cx - s * 0.24, by + s * 0.27), (cx + s * 0.24, by + s * 0.27), (cx + s * 0.3, by + s * 0.05), (cx - s * 0.3, by + s * 0.05)], WHITE)
    c.setFillColor(MT);
    for k in range(3): c.rect(cx - s * 0.18, by + s * (0.2 - k * 0.045), s * (0.3 - k * 0.06), s * 0.012, stroke=0, fill=1)
    c.setFillColor(HexColor("#0E1620")); c.roundRect(cx + s * 0.18, by + s * 0.38, s * 0.16, s * 0.08, s * 0.015, stroke=0, fill=1)
    c.setFillColor(GN); c.circle(cx + s * 0.22, by + s * 0.42, s * 0.015, stroke=0, fill=1)
    c.setFillColor(YL); c.circle(cx + s * 0.27, by + s * 0.42, s * 0.015, stroke=0, fill=1)


def ill_perifericos(c, cx, by, s):
    shadow(c, cx, by, s * 0.95)
    # teclado
    P(c, [(cx - s * 0.48, by + s * 0.05), (cx + s * 0.22, by + s * 0.05), (cx + s * 0.18, by + s * 0.3), (cx - s * 0.44, by + s * 0.3)], DK)
    c.setFillColor(DK2)
    for r in range(4):
        for k in range(10):
            x = cx - s * 0.44 + r * s * 0.01 + k * s * 0.062; y = by + s * (0.08 + r * 0.055)
            c.roundRect(x, y, s * 0.05, s * 0.04, s * 0.008, stroke=0, fill=1)
    c.setFillColor(DK2); c.roundRect(cx - s * 0.3, by + s * 0.075, s * 0.3, s * 0.035, s * 0.01, stroke=0, fill=1)
    # mouse
    c.setFillColor(DK); c.ellipse(cx + s * 0.27, by + s * 0.04, cx + s * 0.45, by + s * 0.3, stroke=0, fill=1)
    c.setStrokeColor(DK2); c.setLineWidth(s * 0.01); c.line(cx + s * 0.36, by + s * 0.2, cx + s * 0.36, by + s * 0.3)
    c.setFillColor(GN); c.roundRect(cx + s * 0.35, by + s * 0.22, s * 0.02, s * 0.05, s * 0.01, stroke=0, fill=1)
    # cámara web
    c.setFillColor(MT3); c.rect(cx - s * 0.02, by + s * 0.36, s * 0.04, s * 0.1, stroke=0, fill=1)
    c.setFillColor(DK); c.roundRect(cx - s * 0.16, by + s * 0.45, s * 0.32, s * 0.14, s * 0.07, stroke=0, fill=1)
    c.setFillColor(SCR); c.circle(cx, by + s * 0.52, s * 0.05, stroke=0, fill=1)
    c.setFillColor(HexColor("#4A79A8")); c.circle(cx - s * 0.015, by + s * 0.535, s * 0.015, stroke=0, fill=1)
    c.setFillColor(GN); c.circle(cx + s * 0.11, by + s * 0.52, s * 0.012, stroke=0, fill=1)


def ill_estanteria(c, cx, by, s, beam=MT3, up=HexColor("#4F5D6B"), boxes=True, levels=5, wf=0.62):
    w = min(s * wf, MAXW); h = s * 0.95; x0 = cx - w / 2
    shadow(c, cx, by, w * 1.05)
    c.setFillColor(up)
    c.rect(x0, by, s * 0.03, h, stroke=0, fill=1); c.rect(x0 + w - s * 0.03, by, s * 0.03, h, stroke=0, fill=1)
    c.setFillColor(Color(0, 0, 0, alpha=0.08)); c.rect(x0 + s * 0.03, by, w - s * 0.06, h, stroke=0, fill=1)
    cols = [GN, MT, YL, DK2, HexColor("#D9DEE4")]
    for i in range(levels):
        y = by + s * 0.03 + i * (h - s * 0.06) / (levels - 1)
        c.setFillColor(beam); c.rect(x0, y, w, s * 0.03, stroke=0, fill=1)
        if boxes and i < levels - 1:
            xx = x0 + s * 0.05; k = i
            while xx < x0 + w - s * 0.16:
                bw = s * (0.11 + 0.05 * ((k * 7) % 3) / 2); bh = (h - s * 0.06) / (levels - 1) * (0.55 + 0.25 * ((k * 5) % 3) / 2)
                if xx + bw > x0 + w - s * 0.05: break
                c.setFillColor(cols[k % len(cols)]); c.roundRect(xx, y + s * 0.03, bw, bh, s * 0.01, stroke=0, fill=1)
                c.setFillColor(Color(1, 1, 1, alpha=0.5)); c.rect(xx + bw * 0.3, y + s * 0.03 + bh * 0.62, bw * 0.4, bh * 0.1, stroke=0, fill=1)
                xx += bw + s * 0.025; k += 1


def ill_est_bodega(c, cx, by, s):
    ill_estanteria(c, cx, by, s, beam=OR, up=HexColor("#1F4F8F"), levels=4, wf=0.78)


def ill_est_medida(c, cx, by, s):
    ww = min(s * 0.92 * 0.6, MAXW - 24)
    ill_estanteria(c, cx - 10, by + 8, s * 0.92, boxes=False, levels=5, wf=0.6)
    c.setStrokeColor(GN); c.setFillColor(GN); c.setLineWidth(1.2)
    x = cx - 10 + ww / 2 + 12; y0, y1 = by + 8, by + 8 + s * 0.87
    c.line(x, y0, x, y1)
    for yy, d in ((y0, 1), (y1, -1)):
        P(c, [(x, yy), (x - 3, yy + d * 6), (x + 3, yy + d * 6)], GN)
    y = by; xa, xb = cx - 10 - ww / 2, cx - 10 + ww / 2
    c.line(xa, y, xb, y)
    for xx, d in ((xa, 1), (xb, -1)):
        P(c, [(xx, y), (xx + d * 6, y + 3), (xx + d * 6, y - 3)], GN)


# ---------- integración con los bloques del EPP ----------
for _f in (ill_estanteria, ill_est_bodega, ill_est_medida): _f.tall = True
_tile = E.tile


def tile2(c, x, y, w, h, f, name, colors):
    if not callable(f):
        return _tile(c, x, y, w, h, f, name, colors)
    c.setFillColor(TILE); c.roundRect(x, y, w, h, 13, stroke=0, fill=1)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 5.4); c.drawRightString(x + w - 10, y + h - 13, "Ilustración referencial")
    global MAXW
    MAXW = w - 40
    s = (h - 74) if getattr(f, 'tall', False) else min(w * 0.86, h - 60)
    f(c, x + w / 2, y + 46, s)
    fs = 7.4
    while c.stringWidth(name, "Mont-Bold", fs) > w - 40: fs -= 0.2
    fw = c.stringWidth(name, "Mont-Bold", fs)
    c.setFillColor(WHITE); c.roundRect(x + 10, y + 10, fw + 20, 19, 9.5, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont("Mont-Bold", fs); c.drawString(x + 20, y + 16.4, name)


E.tile = tile2

ERGO = ("Línea de ergonomía para la oficina", "Elementos que mejoran la postura y la comodidad en el puesto de trabajo.",
        [("erg_sillas.png", "Sillas ergonómicas", None), ("erg_bases.png", "Bases para portátil y pantalla", None), ("erg_reposapies.png", "Reposapiés ergonómico", None)],
        ["Sillas ergonómicas", "Pad mouse ergonómicos", "Bases para portátil", "Bases y brazos para pantalla", "Reposapiés"])
TEC = ("Línea de tecnología y periféricos", "Equipos y accesorios para el trabajo diario en oficina y operación.",
       [("tec_portatil.png", "Equipos de cómputo portátiles", None), ("tec_impresora.png", "Impresoras y tintas", None), ("tec_perifericos.png", "Teclados, mouse y cámaras web", None)],
       ["Equipos de cómputo portátiles", "Teclados y mouse", "Cámaras web", "Parlantes y micrófonos",
        "Impresoras", "Repuestos y consumibles de impresora", "Módems y routers wifi / ethernet", "Cables y adaptadores"])
EST = ("Línea de estanterías", "Estanterías para oficinas, archivos y bodegas, en diferentes tamaños y capacidades.",
       [("est_oficina.png", "Estantería para oficina y archivo", None), ("est_bodega.png", "Estantería para bodega", None), ("est_medida.png", "Estantería a la medida", None)],
       ["Estanterías metálicas por niveles", "Estanterías para archivo", "Estanterías para bodega",
        "Entrepaños y niveles adicionales", "Estanterías a la medida", "Diferentes tamaños y materiales"])


def section_header(c, title, sub):
    stripe(c, M, H - 94, h=7); spaced(c, M + 20, H - 93, "LÍNEA DE SUMINISTRO", "Mont-SemiBold", 6.6, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 22); c.drawString(M, H - 122, title)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 9); c.drawString(M, H - 139, sub)


def build(out, n1=10):
    c = canvas.Canvas(out, pagesize=(W, H)); c.setTitle("Portafolio - Abastecer Empresarial - Ergonomía, tecnología y estanterías")
    page_frame(c, n1)
    section_header(c, "Ergonomía y tecnología", "Todo lo que necesita el puesto de trabajo: comodidad, equipos y accesorios.")
    by = line_block(c, H - 160, 1, *ERGO, th=150, kicker="OFICINA · 01 DE 02")
    line_block(c, by - 24, 2, *TEC, th=150, kicker="OFICINA · 02 DE 02")
    c.showPage()
    page_frame(c, n1 + 1)
    section_header(c, "Estanterías y almacenamiento", "Soluciones para ordenar oficinas, archivos y bodegas.")
    by = line_block(c, H - 160, 1, *EST, th=300, kicker="ESTANTERÍAS")
    personalizada_est(c, by - 26, h=86)
    c.showPage(); c.save()


def personalizada_est(c, ytop, h=74):
    y = ytop - h
    c.setFillColor(NAVY); c.roundRect(M, y, CW, h, 13, stroke=0, fill=1)
    stripe(c, M + 18, y + h - 24, h=7)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 12); c.drawString(M + 38, y + h - 24, "Estanterías a la medida de tu espacio")
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 8.2)
    c.drawString(M + 18, y + 30, "Cuéntanos las medidas, el número de niveles, la carga que necesitas y el material, y te cotizamos")
    c.drawString(M + 18, y + 17, "una estantería con el tamaño y el material personalizados para tu oficina o bodega.")
    return y


if __name__ == "__main__":
    out = os.path.join(HERE, "..", "salidas", "Ergonomia_tecnologia_estanterias_vista_previa.pdf")
    build(out); print(out)
