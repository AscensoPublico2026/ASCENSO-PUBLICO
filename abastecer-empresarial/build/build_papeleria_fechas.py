# Papelería + Aseo y cafetería (una página) y Fechas especiales + Servicio de diseño gráfico (página siguiente).
# Vista previa con ilustraciones vectoriales propias ("Ilustración referencial") hasta tener las fotos de Abastecer.
import os, sys
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_ergo_tec as T  # activa tile2 (acepta ilustraciones) en build_epp_lineas
from build_ergo_tec import *
from reportlab.lib.colors import HexColor, Color

KR = HexColor("#C89B5A"); KR2 = HexColor("#A87B3F"); RD = HexColor("#D93A26"); BL = HexColor("#1F4FA3")
PK = HexColor("#E85D8F"); PU = HexColor("#7A4FB5"); WH = HexColor("#FFFFFF"); PAP = HexColor("#F4F6F8")


def rr(c, x, y, w, h, r, col):
    c.setFillColor(col); c.roundRect(x, y, w, h, r, stroke=0, fill=1)


# ---------- papelería ----------
def ill_resma(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    for k in range(3):
        x = cx - s * 0.36 + k * s * 0.03; y = by + s * 0.02 + k * s * 0.17
        rr(c, x, y, s * 0.66, s * 0.16, s * 0.012, WH)
        c.setStrokeColor(MT); c.setLineWidth(s * 0.004); c.roundRect(x, y, s * 0.66, s * 0.16, s * 0.012, stroke=1, fill=0)
        rr(c, x + s * 0.2, y, s * 0.26, s * 0.16, 0, GN if k != 1 else BL)
        c.setFillColor(WH); c.setFont("Mont-Bold", s * 0.035); c.drawCentredString(x + s * 0.33, y + s * 0.065, "CARTA 75 g")
    c.setStrokeColor(MT); c.setLineWidth(s * 0.004)
    for i in range(5):
        y = by + s * 0.53 + i * s * 0.012; c.line(cx - s * 0.3, y, cx + s * 0.3, y)


def ill_archivo(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    cols = [GN, BL, YL, DK2]
    for k, col in enumerate(cols):
        x = cx - s * 0.38 + k * s * 0.19; w = s * 0.17; h = s * (0.74 - (k % 2) * 0.04)
        rr(c, x, by + s * 0.02, w, h, s * 0.015, col)
        rr(c, x + w * 0.2, by + s * 0.02 + h * 0.62, w * 0.6, h * 0.2, s * 0.01, WH)
        c.setFillColor(DK if col != DK2 else MT); c.circle(x + w / 2, by + s * 0.02 + h * 0.18, w * 0.16, stroke=0, fill=1)
        c.setFillColor(col); c.circle(x + w / 2, by + s * 0.02 + h * 0.18, w * 0.08, stroke=0, fill=1)


def ill_utiles(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    # lápices y bolígrafos en el portalápices
    pens = [(-0.09, 0.62, YL), (-0.03, 0.7, BL), (0.03, 0.66, RD), (0.09, 0.6, GN)]
    for dx, h, col in pens:
        x = cx - s * 0.2 + s * dx
        rr(c, x - s * 0.018, by + s * 0.2, s * 0.036, s * h - s * 0.2, s * 0.01, col)
        P(c, [(x - s * 0.018, by + s * h), (x + s * 0.018, by + s * h), (x, by + s * (h + 0.06))], KR)
    rr(c, cx - s * 0.36, by + s * 0.02, s * 0.32, s * 0.34, s * 0.03, DK2)
    rr(c, cx - s * 0.36, by + s * 0.28, s * 0.32, s * 0.03, 0, DK)
    # cosedora
    rr(c, cx + s * 0.02, by + s * 0.02, s * 0.38, s * 0.07, s * 0.02, DK)
    P(c, [(cx + s * 0.04, by + s * 0.1), (cx + s * 0.4, by + s * 0.12), (cx + s * 0.4, by + s * 0.2), (cx + s * 0.08, by + s * 0.17)], RD)
    rr(c, cx + s * 0.3, by + s * 0.09, s * 0.08, s * 0.06, s * 0.01, MT3)
    # notas adhesivas
    rr(c, cx + s * 0.08, by + s * 0.27, s * 0.22, s * 0.2, s * 0.01, YL)
    rr(c, cx + s * 0.14, by + s * 0.32, s * 0.22, s * 0.2, s * 0.01, HexColor("#8FD3A8"))


# ---------- aseo y cafetería ----------
def ill_aseo(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    # galón
    rr(c, cx - s * 0.4, by + s * 0.02, s * 0.3, s * 0.48, s * 0.05, BL)
    rr(c, cx - s * 0.3, by + s * 0.5, s * 0.1, s * 0.08, s * 0.015, DK)
    c.setStrokeColor(BL); c.setLineWidth(s * 0.03); c.arc(cx - s * 0.38, by + s * 0.34, cx - s * 0.2, by + s * 0.56, 90, 180)
    rr(c, cx - s * 0.37, by + s * 0.12, s * 0.24, s * 0.2, s * 0.02, WH)
    c.setFillColor(BL); c.setFont("Mont-Bold", s * 0.04); c.drawCentredString(cx - s * 0.25, by + s * 0.2, "LIMPIADOR")
    # atomizador
    rr(c, cx - s * 0.06, by + s * 0.02, s * 0.2, s * 0.4, s * 0.05, GN)
    rr(c, cx - s * 0.02, by + s * 0.42, s * 0.12, s * 0.06, s * 0.01, DK)
    P(c, [(cx - s * 0.04, by + s * 0.48), (cx + s * 0.12, by + s * 0.48), (cx + s * 0.12, by + s * 0.56), (cx - s * 0.1, by + s * 0.55)], DK)
    rr(c, cx - s * 0.03, by + s * 0.12, s * 0.14, s * 0.14, s * 0.02, WH)
    # jabón con dosificador
    rr(c, cx + s * 0.18, by + s * 0.02, s * 0.2, s * 0.3, s * 0.05, PK)
    rr(c, cx + s * 0.255, by + s * 0.32, s * 0.05, s * 0.08, 0, MT3)
    rr(c, cx + s * 0.25, by + s * 0.4, s * 0.12, s * 0.035, s * 0.01, MT3)
    rr(c, cx + s * 0.21, by + s * 0.1, s * 0.14, s * 0.1, s * 0.02, WH)


def ill_limpieza(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    # balde
    P(c, [(cx - s * 0.06, by + s * 0.02), (cx + s * 0.34, by + s * 0.02), (cx + s * 0.38, by + s * 0.34), (cx - s * 0.1, by + s * 0.34)], YL)
    rr(c, cx - s * 0.11, by + s * 0.32, s * 0.5, s * 0.04, s * 0.015, HexColor("#D9A400"))
    c.setStrokeColor(MT3); c.setLineWidth(s * 0.012); c.arc(cx - s * 0.06, by + s * 0.2, cx + s * 0.34, by + s * 0.52, 0, 180)
    # trapero
    c.setStrokeColor(KR2); c.setLineWidth(s * 0.03); c.line(cx - s * 0.2, by + s * 0.12, cx - s * 0.08, by + s * 0.95)
    c.setStrokeColor(MT); c.setLineWidth(s * 0.025)
    for k in range(7):
        c.line(cx - s * 0.2, by + s * 0.14, cx - s * 0.34 + k * s * 0.045, by + s * 0.02)
    # escoba
    c.setStrokeColor(GN2); c.setLineWidth(s * 0.03); c.line(cx - s * 0.36, by + s * 0.2, cx - s * 0.42, by + s * 0.95)
    P(c, [(cx - s * 0.46, by + s * 0.02), (cx - s * 0.24, by + s * 0.02), (cx - s * 0.3, by + s * 0.2), (cx - s * 0.42, by + s * 0.2)], RD)
    c.setStrokeColor(HexColor("#A82A1A")); c.setLineWidth(s * 0.006)
    for k in range(6): c.line(cx - s * 0.44 + k * s * 0.035, by + s * 0.03, cx - s * 0.41 + k * s * 0.02, by + s * 0.18)


def ill_cafeteria(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    # tarro de café
    rr(c, cx - s * 0.42, by + s * 0.02, s * 0.26, s * 0.42, s * 0.04, KR2)
    rr(c, cx - s * 0.43, by + s * 0.42, s * 0.28, s * 0.06, s * 0.015, DK)
    rr(c, cx - s * 0.39, by + s * 0.12, s * 0.2, s * 0.18, s * 0.02, WH)
    c.setFillColor(KR2); c.setFont("Mont-Bold", s * 0.045); c.drawCentredString(cx - s * 0.29, by + s * 0.19, "CAFÉ")
    # taza
    rr(c, cx - s * 0.12, by + s * 0.02, s * 0.26, s * 0.24, s * 0.05, WH)
    c.setStrokeColor(MT); c.setLineWidth(s * 0.006); c.roundRect(cx - s * 0.12, by + s * 0.02, s * 0.26, s * 0.24, s * 0.05, stroke=1, fill=0)
    c.setStrokeColor(MT2); c.setLineWidth(s * 0.025); c.arc(cx + s * 0.09, by + s * 0.07, cx + s * 0.22, by + s * 0.2, -90, 180)
    rr(c, cx - s * 0.1, by + s * 0.2, s * 0.22, s * 0.04, s * 0.02, HexColor("#6B4423"))
    c.setStrokeColor(MT2); c.setLineWidth(s * 0.01)
    for dx in (-0.04, 0.02, 0.08):
        p = c.beginPath(); x = cx + s * dx; p.moveTo(x, by + s * 0.28)
        p.curveTo(x - s * 0.03, by + s * 0.33, x + s * 0.03, by + s * 0.36, x, by + s * 0.41); c.drawPath(p, stroke=1, fill=0)
    # vasos desechables apilados
    for k in range(4):
        y = by + s * 0.02 + k * s * 0.06
        P(c, [(cx + s * 0.22, y), (cx + s * 0.38, y), (cx + s * 0.41, y + s * 0.26), (cx + s * 0.19, y + s * 0.26)], WH if k % 2 == 0 else PAP)
        c.setStrokeColor(MT); c.setLineWidth(s * 0.004); c.line(cx + s * 0.19, y + s * 0.26, cx + s * 0.41, y + s * 0.26)
    rr(c, cx + s * 0.205, by + s * 0.12, s * 0.19, s * 0.04, 0, GN)


# ---------- fechas especiales ----------
def ill_ancheta(c, cx, by, s):
    shadow(c, cx, by, s * 0.9)
    # productos dentro
    rr(c, cx - s * 0.28, by + s * 0.3, s * 0.1, s * 0.36, s * 0.02, HexColor("#7A1F2B"))
    rr(c, cx - s * 0.255, by + s * 0.66, s * 0.05, s * 0.08, 0, YL)
    rr(c, cx - s * 0.14, by + s * 0.3, s * 0.18, s * 0.26, s * 0.02, YL)
    rr(c, cx + s * 0.06, by + s * 0.3, s * 0.16, s * 0.3, s * 0.02, GN)
    c.setFillColor(RD); c.circle(cx + s * 0.28, by + s * 0.38, s * 0.07, stroke=0, fill=1)
    c.setFillColor(HexColor("#F08A24")); c.circle(cx - s * 0.02, by + s * 0.6, s * 0.06, stroke=0, fill=1)
    # canasta
    P(c, [(cx - s * 0.42, by + s * 0.38), (cx + s * 0.42, by + s * 0.38), (cx + s * 0.34, by + s * 0.02), (cx - s * 0.34, by + s * 0.02)], KR)
    c.setStrokeColor(KR2); c.setLineWidth(s * 0.008)
    for k in range(1, 6):
        y = by + s * 0.02 + k * s * 0.06; t = k * 0.06 / 0.36
        c.line(cx - s * (0.34 + 0.08 * t), y, cx + s * (0.34 + 0.08 * t), y)
    for k in range(1, 10):
        xb = cx - s * 0.34 + k * s * 0.068; xt = cx - s * 0.42 + k * s * 0.084
        c.line(xb, by + s * 0.02, xt, by + s * 0.38)
    rr(c, cx - s * 0.44, by + s * 0.36, s * 0.88, s * 0.05, s * 0.02, KR2)
    # moño
    P(c, [(cx, by + s * 0.2), (cx - s * 0.14, by + s * 0.28), (cx - s * 0.14, by + s * 0.12)], RD)
    P(c, [(cx, by + s * 0.2), (cx + s * 0.14, by + s * 0.28), (cx + s * 0.14, by + s * 0.12)], RD)
    c.setFillColor(HexColor("#A82A1A")); c.circle(cx, by + s * 0.2, s * 0.03, stroke=0, fill=1)


def ill_mercado(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    # pan, verduras y botella asomando
    rr(c, cx - s * 0.18, by + s * 0.5, s * 0.07, s * 0.3, s * 0.03, HexColor("#E0B070"))
    rr(c, cx + s * 0.1, by + s * 0.5, s * 0.08, s * 0.32, s * 0.02, BL); rr(c, cx + s * 0.12, by + s * 0.82, s * 0.04, s * 0.05, 0, DK)
    for dx, h in ((-0.04, 0.72), (0.0, 0.78), (0.04, 0.7)):
        P(c, [(cx + s * dx, by + s * 0.5), (cx + s * (dx - 0.04), by + s * h), (cx + s * (dx + 0.04), by + s * h)], GN)
    c.setFillColor(RD); c.circle(cx - s * 0.26, by + s * 0.56, s * 0.07, stroke=0, fill=1)
    c.setFillColor(HexColor("#F08A24")); c.circle(cx + s * 0.27, by + s * 0.55, s * 0.065, stroke=0, fill=1)
    # bolsa de mercado
    P(c, [(cx - s * 0.36, by + s * 0.56), (cx + s * 0.36, by + s * 0.56), (cx + s * 0.32, by + s * 0.02), (cx - s * 0.32, by + s * 0.02)], KR)
    rr(c, cx - s * 0.36, by + s * 0.52, s * 0.72, s * 0.05, 0, KR2)
    rr(c, cx - s * 0.16, by + s * 0.16, s * 0.32, s * 0.2, s * 0.03, GN)
    c.setFillColor(WH); c.setFont("Mont-Bold", s * 0.045); c.drawCentredString(cx, by + s * 0.24, "MERCADO")


def ill_regalos(c, cx, by, s):
    shadow(c, cx, by, s * 0.9)
    # globos
    for dx, h, col in ((0.18, 0.8, RD), (0.3, 0.73, YL), (0.08, 0.7, BL)):
        c.setStrokeColor(MT3); c.setLineWidth(s * 0.005); c.line(cx + s * dx, by + s * (h - 0.09), cx + s * 0.14, by + s * 0.42)
        c.setFillColor(col); c.ellipse(cx + s * (dx - 0.07), by + s * (h - 0.09), cx + s * (dx + 0.07), by + s * (h + 0.09), stroke=0, fill=1)
        c.setFillColor(Color(1, 1, 1, alpha=0.45)); c.circle(cx + s * (dx - 0.025), by + s * (h + 0.03), s * 0.015, stroke=0, fill=1)
    # cajas de regalo
    def caja(x, y, w, h, col, cinta):
        rr(c, x, y, w, h, s * 0.01, col)
        rr(c, x - s * 0.015, y + h - s * 0.06, w + s * 0.03, s * 0.06, s * 0.01, col)
        rr(c, x + w / 2 - s * 0.02, y, s * 0.04, h, 0, cinta)
        P(c, [(x + w / 2, y + h), (x + w / 2 - s * 0.08, y + h + s * 0.06), (x + w / 2 - s * 0.08, y + h)], cinta)
        P(c, [(x + w / 2, y + h), (x + w / 2 + s * 0.08, y + h + s * 0.06), (x + w / 2 + s * 0.08, y + h)], cinta)
    caja(cx - s * 0.42, by + s * 0.02, s * 0.32, s * 0.3, GN, YL)
    caja(cx - s * 0.06, by + s * 0.02, s * 0.26, s * 0.22, PU, WH)
    caja(cx - s * 0.36, by + s * 0.38, s * 0.2, s * 0.16, RD, WH)
    # osito de peluche simple
    c.setFillColor(KR)
    c.circle(cx + s * 0.32, by + s * 0.12, s * 0.1, stroke=0, fill=1); c.circle(cx + s * 0.32, by + s * 0.29, s * 0.075, stroke=0, fill=1)
    c.circle(cx + s * 0.265, by + s * 0.35, s * 0.03, stroke=0, fill=1); c.circle(cx + s * 0.375, by + s * 0.35, s * 0.03, stroke=0, fill=1)
    c.setFillColor(HexColor("#E8C9A0")); c.circle(cx + s * 0.32, by + s * 0.27, s * 0.03, stroke=0, fill=1)
    c.setFillColor(DK); c.circle(cx + s * 0.3, by + s * 0.31, s * 0.008, stroke=0, fill=1); c.circle(cx + s * 0.34, by + s * 0.31, s * 0.008, stroke=0, fill=1)


def ill_diseno(c, cx, by, s):
    shadow(c, cx, by, s * 0.85)
    rr(c, cx - s * 0.06, by + s * 0.02, s * 0.12, s * 0.03, s * 0.01, MT3)
    rr(c, cx - s * 0.02, by + s * 0.04, s * 0.04, s * 0.1, 0, MT2)
    rr(c, cx - s * 0.44, by + s * 0.14, s * 0.88, s * 0.56, s * 0.03, DK)
    rr(c, cx - s * 0.41, by + s * 0.17, s * 0.82, s * 0.5, s * 0.01, WH)
    # barra de herramientas
    rr(c, cx - s * 0.41, by + s * 0.17, s * 0.08, s * 0.5, 0, PAP)
    for k, col in enumerate((GN, YL, BL, RD)):
        c.setFillColor(col); c.circle(cx - s * 0.37, by + s * (0.6 - k * 0.09), s * 0.018, stroke=0, fill=1)
    # pieza en diseño: logo + texto
    P(c, [(cx - s * 0.12, by + s * 0.34), (cx + s * 0.0, by + s * 0.58), (cx + s * 0.12, by + s * 0.34)], NAVY)
    P(c, [(cx - s * 0.03, by + s * 0.34), (cx + s * 0.06, by + s * 0.34), (cx + s * 0.04, by + s * 0.42)], GN)
    c.setFillColor(YL); c.wedge(cx - s * 0.06, by + s * 0.3, cx + s * 0.06, by + s * 0.46, 0, 180, stroke=0, fill=1)
    rr(c, cx - s * 0.18, by + s * 0.25, s * 0.36, s * 0.035, s * 0.01, NAVY)
    rr(c, cx - s * 0.12, by + s * 0.21, s * 0.24, s * 0.02, s * 0.01, GN)
    # marco de selección
    c.setStrokeColor(BL); c.setLineWidth(s * 0.004); c.setDash(s * 0.012, s * 0.008)
    c.rect(cx - s * 0.2, by + s * 0.19, s * 0.4, s * 0.42, stroke=1, fill=0); c.setDash()
    for xx, yy in ((-0.2, 0.19), (0.2, 0.19), (-0.2, 0.61), (0.2, 0.61)):
        rr(c, cx + s * xx - s * 0.012, by + s * yy - s * 0.012, s * 0.024, s * 0.024, 0, BL)
    # paleta de color
    for k, col in enumerate((NAVY, GN, YL)):
        rr(c, cx + s * 0.26, by + s * (0.56 - k * 0.07), s * 0.1, s * 0.05, s * 0.01, col)


for _f in (ill_limpieza, ill_mercado, ill_ancheta):
    pass

PAPEL = ("Línea de papelería y útiles de oficina", "Papel, archivo y útiles para el trabajo diario de la oficina.",
         [(ill_resma, "Resmas de papel", None), (ill_archivo, "Archivo y AZ", None), (ill_utiles, "Útiles de oficina", None)],
         ["Resmas de papel carta y oficio", "Carpetas, AZ y archivadores", "Cajas de archivo", "Bolígrafos, lápices y marcadores",
          "Cosedoras, perforadoras y ganchos", "Notas adhesivas y libretas", "Sobres y papel especial", "Cintas, pegantes y tijeras"])
ASEO = ("Línea de aseo y cafetería", "Insumos para mantener limpios tus espacios y atender a tu equipo y visitantes.",
        [(ill_aseo, "Productos de limpieza", None), (ill_limpieza, "Escobas, traperos y baldes", None), (ill_cafeteria, "Cafetería", None)],
        ["Limpiadores y desinfectantes", "Jabones y gel antibacterial", "Papel higiénico y toallas", "Bolsas para basura",
         "Escobas, traperos y baldes", "Paños, esponjas y guantes", "Café, azúcar y aromáticas", "Vasos, mezcladores y servilletas"])
FECHAS = ("Línea de anchetas y fechas especiales", "Regalos y detalles para celebrar con tu equipo, clientes y sus familias.",
          [(ill_ancheta, "Anchetas", None), (ill_mercado, "Mercados empresariales", None), (ill_regalos, "Juguetes, regalos y fiestas", None)],
          ["Anchetas navideñas y corporativas", "Mercados para colaboradores", "Juguetes para hijos de colaboradores", "Regalos y detalles corporativos",
           "Decoración para fiestas y eventos", "Kits para cumpleaños", "Detalles para Día de la Madre y del Padre", "Halloween, amor y amistad y Navidad"])
SERVICIOS = ["Logos e imagen corporativa", "Carnés y papelería corporativa", "Avisos y señalización a la medida",
             "Piezas para redes sociales", "Etiquetas y empaques", "Catálogos, volantes y pendones"]


def bloque_diseno(c, ytop, h=190):
    stripe(c, M, ytop - 9, h=7); spaced(c, M + 20, ytop - 8, "SERVICIO", "Mont-SemiBold", 6.4, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 17); c.drawString(M, ytop - 31, "Servicio de diseño gráfico")
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 8.4); c.drawString(M, ytop - 45, "Diseñamos las piezas de tu empresa y te entregamos el producto listo.")
    gap = 10; tw = (CW - 2 * gap) / 3; top = ytop - 56; y = top - h
    T.tile2(c, M, y, tw, h, ill_diseno, "Diseño de piezas", None)
    x = M + tw + gap; w = CW - tw - gap
    c.setFillColor(NAVY); c.roundRect(x, y, w, h, 13, stroke=0, fill=1)
    stripe(c, x + 18, y + h - 26, h=7)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 12); c.drawString(x + 38, y + h - 26, "Tu idea, lista para producir")
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 8)
    for i, t in enumerate(["Contamos con diseñador gráfico para crear o ajustar las piezas que necesites.",
                           "Cuéntanos tu idea o envíanos una referencia y te proponemos el diseño."]):
        c.drawString(x + 18, y + h - 46 - i * 11.5, t)
    spaced(c, x + 18, y + h - 84, "LO QUE DISEÑAMOS", "Mont-SemiBold", 6, 1.5, YELLOW)
    colw = (w - 36) / 2
    for i, t in enumerate(SERVICIOS):
        col, row = divmod(i, 3); xx = x + 18 + col * colw; yy = y + h - 101 - row * 14
        c.setFillColor(GREEN); c.circle(xx + 2.5, yy + 2.6, 2.1, stroke=0, fill=1)
        c.setFillColor(WHITE); c.setFont("Mont-Medium", 7.8); c.drawString(xx + 9, yy, t)
    bw = 190; bx = x + 18; byb = y + 16
    c.setFillColor(GREEN); c.roundRect(bx, byb, bw, 22, 11, stroke=0, fill=1)
    t = "CUÉNTANOS TU IDEA"; wl = spaced_w(c, t, "Mont-ExtraBold", 6.2, 0.8)
    spaced(c, bx + (bw - wl) / 2 + 0.4, byb + 8, t, "Mont-ExtraBold", 6.2, 0.8, WHITE)
    c.linkURL(WA + "?text=" + quote("Hola, quiero cotizar un servicio de diseño gráfico."), (bx, byb, bx + bw, byb + 22), relative=0)
    return y


def build(out, n1=13):
    c = canvas.Canvas(out, pagesize=(W, H)); c.setTitle("Portafolio - Abastecer Empresarial - Papelería, aseo y cafetería, fechas especiales y diseño")
    page_frame(c, n1)
    section_header(c, "Papelería, aseo y cafetería", "Los insumos del día a día de tu oficina, en un solo proveedor.")
    by = line_block(c, H - 160, 1, *PAPEL, th=150, kicker="OFICINA · 01 DE 02")
    line_block(c, by - 24, 2, *ASEO, th=150, kicker="OFICINA · 02 DE 02")
    c.showPage()
    page_frame(c, n1 + 1)
    section_header(c, "Fechas especiales y diseño", "Celebra con tu equipo y tus clientes, y comunica tu marca con piezas propias.")
    by = line_block(c, H - 160, 1, *FECHAS, th=168, kicker="FECHAS ESPECIALES")
    bloque_diseno(c, by - 24)
    c.showPage(); c.save()


if __name__ == "__main__":
    out = os.path.join(HERE, "..", "salidas", "Papeleria_aseo_fechas_diseno_vista_previa.pdf")
    build(out); print(out)
