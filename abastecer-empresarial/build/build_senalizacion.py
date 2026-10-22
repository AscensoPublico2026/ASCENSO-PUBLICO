# Señalización, protección contra incendios y emergencias — dos propuestas:
#   Opción A: dos páginas (8 y 9), mismo formato de las líneas de EPP.
#   Opción B: una sola página (8), bloques compactos.
import os, sys
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_epp_lineas import *  # page_frame, tile, line_block, SOFT, colores, fit_image...
from reportlab.lib.colors import HexColor

RED, YEL, BLUE, GRN = HexColor("#D52B1E"), HexColor("#F7C600"), HexColor("#1F5BB5"), HexColor("#17914A")

SEN = ("Línea de señalización y demarcación", "Avisos, demarcación de áreas y control de tránsito en tus instalaciones.",
       [("sen_sen_cono.png", "Cono vial reflectivo", None), ("sen_sen_chaleco.png", "Chaleco reflectivo", None), ("sen_sen_paleta.png", "Paleta pare y siga", None)],
       ["Avisos en PVC por tipo de señal", "Conos viales reflectivos", "Chalecos reflectivos", "Paletas pare y siga",
        "Cintas de demarcación y peligro", "Cintas antideslizantes", "Señal de piso mojado", "Señalización personalizada"])
INC = ("Línea de protección contra incendios", "Extintores y detección para oficinas, bodegas, vehículos y plantas.",
       [("sen_inc_extintor.png", "Extintor multipropósito", None), ("sen_inc_co2.png", "Extintor de CO₂", None), ("sen_inc_detector.png", "Detector de humo", None)],
       ["Extintores multipropósito", "Extintores de CO₂", "Capacidades de 5 a 30 lb", "Soportes de pared",
        "Bases para extintor", "Señal de ubicación de extintor", "Detectores de humo"])
EME = ("Línea de emergencias y primeros auxilios", "Dotación para brigadas y atención de emergencias.",
       [("sen_eme_botiquin.png", "Botiquín", None), ("sen_eme_camilla.png", "Camilla de inmovilización", None), ("sen_eme_lampara.png", "Lámpara de emergencia", None)],
       ["Botiquines tipo A y B", "Maletas y bolsos para botiquín", "Camillas de inmovilización", "Inmovilizadores de cuello",
        "Lámparas de emergencia", "Kits de control de derrames", "Kits de carretera", "Brazaletes de brigadista"])
LINES3 = [SEN, INC, EME]
TIPOS = [("Prohibición", ["aviso_pro_fumar.png", "aviso_pro_acceso.png"], RED), ("Advertencia", ["aviso_pre_electrico.png", "aviso_pre_piso.png"], YEL),
         ("Obligación", ["aviso_obl_casco.png", "aviso_obl_facial.png"], BLUE), ("Información", ["aviso_inf_salida.png", "aviso_inf_botiquin.png"], GRN)]


def sign_icon(c, kind, cx, cy, s):
    """Pictograma genérico dibujado (no es copia de un aviso del proveedor)."""
    c.saveState()
    if kind == "pro":
        c.setFillColor(WHITE); c.setStrokeColor(RED); c.setLineWidth(s * 0.13); c.circle(cx, cy, s * 0.42, stroke=1, fill=1)
        c.setFillColor(INK); c.rect(cx - s * 0.24, cy - s * 0.04, s * 0.38, s * 0.09, stroke=0, fill=1)
        c.setFillColor(HexColor("#E8752A")); c.rect(cx + s * 0.14, cy - s * 0.04, s * 0.08, s * 0.09, stroke=0, fill=1)
        c.setStrokeColor(RED); c.setLineWidth(s * 0.11); c.line(cx - s * 0.29, cy + s * 0.29, cx + s * 0.29, cy - s * 0.29)
    elif kind == "adv":
        c.setFillColor(YEL); c.setStrokeColor(INK); c.setLineWidth(s * 0.07); c.setLineJoin(1)
        p = c.beginPath(); p.moveTo(cx, cy + s * 0.44); p.lineTo(cx + s * 0.48, cy - s * 0.38); p.lineTo(cx - s * 0.48, cy - s * 0.38); p.close()
        c.drawPath(p, stroke=1, fill=1)
        c.setFillColor(INK); c.roundRect(cx - s * 0.045, cy - s * 0.12, s * 0.09, s * 0.36, s * 0.04, stroke=0, fill=1)
        c.circle(cx, cy - s * 0.24, s * 0.055, stroke=0, fill=1)
    elif kind == "obl":
        c.setFillColor(BLUE); c.circle(cx, cy, s * 0.44, stroke=0, fill=1)
        c.setFillColor(WHITE)
        p = c.beginPath(); p.moveTo(cx - s * 0.25, cy - s * 0.06); p.curveTo(cx - s * 0.25, cy + s * 0.27, cx + s * 0.25, cy + s * 0.27, cx + s * 0.25, cy - s * 0.06); p.close()
        c.drawPath(p, stroke=0, fill=1)
        c.roundRect(cx - s * 0.33, cy - s * 0.14, s * 0.66, s * 0.09, s * 0.04, stroke=0, fill=1)
        c.setFillColor(BLUE); c.rect(cx - s * 0.035, cy - s * 0.04, s * 0.07, s * 0.22, stroke=0, fill=1)
    else:
        c.setFillColor(GRN); c.roundRect(cx - s * 0.44, cy - s * 0.44, s * 0.88, s * 0.88, s * 0.1, stroke=0, fill=1)
        c.setFillColor(WHITE)
        c.rect(cx + s * 0.1, cy - s * 0.28, s * 0.2, s * 0.56, stroke=0, fill=1)
        c.setFillColor(GRN); c.rect(cx + s * 0.14, cy - s * 0.24, s * 0.12, s * 0.48, stroke=0, fill=1)
        c.setFillColor(WHITE)
        p = c.beginPath(); p.moveTo(cx - s * 0.32, cy + s * 0.05); p.lineTo(cx - s * 0.08, cy + s * 0.05); p.lineTo(cx - s * 0.08, cy + s * 0.17)
        p.lineTo(cx + s * 0.06, cy); p.lineTo(cx - s * 0.08, cy - s * 0.17); p.lineTo(cx - s * 0.08, cy - s * 0.05); p.lineTo(cx - s * 0.32, cy - s * 0.05); p.close()
        c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


def tipos_strip(c, ytop, h, title=True):
    """Fichas por tipo de aviso con fotos reales de avisos en PVC (catálogo del proveedor)."""
    if title:
        spaced(c, M, ytop - 8, "AVISOS EN PVC POR TIPO DE SEÑAL", "Mont-SemiBold", 6.2, 1.6, GREEN)
        ytop -= 18
    gap = 10; w = (CW - 3 * gap) / 4
    for i, (name, imgs, col) in enumerate(TIPOS):
        x = M + i * (w + gap); y = ytop - h
        c.setFillColor(TILE); c.roundRect(x, y, w, h, 12, stroke=0, fill=1)
        c.setFillColor(col); c.roundRect(x + 10, y + h - 6, 26, 3.2, 1.6, stroke=0, fill=1)
        if h >= 80:
            ih = (h - 52) / 2
            for k, f in enumerate(imgs):
                fit_image(c, os.path.join(CUT, f), x + 10, y + 30 + (1 - k) * (ih + 5), w - 20, ih, shadow=False)
            c.setFillColor(INK); c.setFont("Mont-Bold", 8.2); c.drawString(x + 12, y + 12, name)
        else:
            fit_image(c, os.path.join(CUT, imgs[0]), x + 8, y + 16, w - 16, h - 26, shadow=False)
            c.setFillColor(INK); c.setFont("Mont-Bold", 6.6); c.drawString(x + 10, y + 6, name)
    return ytop - h


def personalizada(c, ytop, h=58):
    """Banda: señalización a la medida."""
    y = ytop - h
    c.setFillColor(NAVY); c.roundRect(M, y, CW, h, 13, stroke=0, fill=1)
    stripe(c, M + 18, y + h - 20, h=7)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 10.5 if h >= 50 else 9); c.drawString(M + 38, y + h - (21 if h >= 50 else 18), "Señalización a la medida de tu empresa")
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 7.6 if h >= 50 else 6.6)
    c.drawString(M + 18, y + (14 if h >= 50 else 9), "¿Necesitas un aviso que no está en el catálogo? Lo personalizamos con el texto, la medida y el logo que requieras.")
    bw = 132; bx = W - M - bw - 14; byb = y + h - (32 if h >= 50 else 26)
    c.setFillColor(YELLOW); c.roundRect(bx, byb, bw, 20, 10, stroke=0, fill=1)
    t = "COTIZA TU SEÑALIZACIÓN"; wl = spaced_w(c, t, "Mont-ExtraBold", 6.2, 0.8)
    spaced(c, bx + (bw - wl) / 2, byb + 7, t, "Mont-ExtraBold", 6.2, 0.8, NAVY)
    c.linkURL(WA + "?text=" + quote("Hola, quiero cotizar señalización personalizada para mi empresa."), (bx, byb, bx + bw, byb + 20), relative=0)
    return y


def section_header(c, title, sub):
    stripe(c, M, H - 94, h=7); spaced(c, M + 20, H - 93, "LÍNEA DE SUMINISTRO", "Mont-SemiBold", 6.6, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 22); c.drawString(M, H - 122, title)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 9); c.drawString(M, H - 139, sub)


TITLE = "Señalización, incendios y emergencias"
SUB = "Señales, demarcación, extintores y dotación para atender emergencias en tus instalaciones."


def kick(i): return f"SEÑALIZACIÓN Y EMERGENCIAS · {i:02d} DE 03"


def opcion_a(out):
    c = canvas.Canvas(out, pagesize=(W, H)); c.setTitle("Portafolio - Abastecer Empresarial - Señalización, incendios y emergencias (opción A)")
    # pág. 8
    page_frame(c, 8); section_header(c, TITLE, SUB)
    by = line_block(c, H - 160, 1, *SEN, th=160, kicker=kick(1))
    y = tipos_strip(c, by - 24, 138)
    personalizada(c, y - 14)
    c.showPage()
    # pág. 9
    page_frame(c, 9)
    by = line_block(c, H - 84, 2, *INC, th=172, kicker=kick(2))
    line_block(c, by - 34, 3, *EME, th=172, kicker=kick(3))
    c.showPage(); c.save()


def compact_block(c, ytop, i, title, desc, prods, listado):
    stripe(c, M, ytop - 9, h=7)
    spaced(c, M + 20, ytop - 8, kick(i), "Mont-SemiBold", 6.2, 1.7, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 14); c.drawString(M, ytop - 28, title)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 7.6); c.drawString(M, ytop - 40, desc)
    th = 104; ty = ytop - 48 - th
    rw = 172; gap = 8; aw = CW - rw - gap; tw = (aw - 2 * gap) / 3
    for k, (f, name, col) in enumerate(prods):
        tile(c, M + k * (tw + gap), ty, tw, th, f, name, col)
    rx = M + aw + gap
    c.setStrokeColor(LINE); c.setLineWidth(0.8); c.setFillColor(WHITE); c.roundRect(rx, ty, rw, th, 12, stroke=1, fill=1)
    spaced(c, rx + 12, ty + th - 15, "PRODUCTOS PRINCIPALES", "Mont-SemiBold", 5.6, 1.4, GREEN)
    yy = ty + th - 28
    for it in listado[:5]:
        c.setFillColor(GREEN); c.circle(rx + 14, yy + 2.2, 1.8, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Mont-Medium", 6.7); c.drawString(rx + 20, yy, it); yy -= 9.6
    bw = rw - 24; bx = rx + 12; byb = ty + 9
    c.setFillColor(GREEN); c.roundRect(bx, byb, bw, 18, 9, stroke=0, fill=1)
    t = "¿ALGO ESPECÍFICO? PREGÚNTANOS"; wl = spaced_w(c, t, "Mont-ExtraBold", 5.5, 0.6)
    spaced(c, bx + (bw - wl) / 2, byb + 6.4, t, "Mont-ExtraBold", 5.5, 0.6, WHITE)
    c.linkURL(WA + "?text=" + quote(f"Hola, quiero cotizar productos de la {title.lower()}."), (bx, byb, bx + bw, byb + 18), relative=0)
    return ty


def opcion_b(out):
    c = canvas.Canvas(out, pagesize=(W, H)); c.setTitle("Portafolio - Abastecer Empresarial - Señalización, incendios y emergencias (opción B)")
    page_frame(c, 8); section_header(c, TITLE, SUB)
    y = tipos_strip(c, H - 150, 52)
    y = personalizada(c, y - 8, h=40)
    for i, l in enumerate(LINES3, 1):
        y = compact_block(c, y - 16, i, *l) - 2
    c.showPage(); c.save()


if __name__ == "__main__":
    S = os.path.join(HERE, "..", "salidas")
    opcion_a(os.path.join(S, "Senalizacion_opcionA_pags_8-9.pdf"))
    opcion_b(os.path.join(S, "Senalizacion_opcionB_pag_8.pdf"))
    print("ok")
