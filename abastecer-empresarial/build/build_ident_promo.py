# Identificación (carnés y porta carnés) + Promocionales y personalizados (una página).
# Fotos enviadas por Abastecer: 4 recortadas para la línea de identificación y 1 foto de ambiente para promocionales.
import os, sys
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_epp_lineas import *
from reportlab.lib.colors import HexColor

ID_TITLE = "Línea de carnés e identificación"
ID_DESC = "Carnés impresos con tu marca y porta carnés para cada tipo de uso en oficina, planta y obra."
ID_PRODS = [("id_carne.png", "Carnés impresos"), ("id_brazo.png", "Porta carné de brazo"),
            ("id_cinta.png", "Porta carné de cinta"), ("id_yoyo.png", "Porta carné con yoyo")]
ID_LIST = ["Carnés impresos a full color", "Diseño con tu marca y datos", "Porta carné de brazo",
           "Cintas para colgar al cuello", "Porta carné con yoyo retráctil", "Fundas y estuches porta carné"]

PR_TITLE = "Línea de productos promocionales y personalizados"
PR_DESC = "Artículos con tu marca para clientes, colaboradores y eventos."
PR_LIST = ["Mugs, termos y botellas", "Libretas, agendas y carpetas", "Bolígrafos y resaltadores",
           "Gorras, morrales y bolsos", "Sombrillas y abanicos", "Llaveros, USB y más"]


def section_header(c, title, sub):
    stripe(c, M, H - 94, h=7); spaced(c, M + 20, H - 93, "LÍNEA DE SUMINISTRO", "Mont-SemiBold", 6.6, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 22); c.drawString(M, H - 122, title)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 9); c.drawString(M, H - 139, sub)


def head(c, ytop, kicker, title, desc):
    stripe(c, M, ytop - 9, h=7); spaced(c, M + 20, ytop - 8, kicker, "Mont-SemiBold", 6.4, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 17); c.drawString(M, ytop - 31, title)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 8.4); c.drawString(M, ytop - 45, desc)


def wa_button(c, x, y, w, label, msg, h=21):
    c.setFillColor(GREEN); c.roundRect(x, y, w, h, h / 2, stroke=0, fill=1)
    wl = spaced_w(c, label, "Mont-ExtraBold", 6, 0.8)
    spaced(c, x + (w - wl) / 2 + 0.4, y + 7.6, label, "Mont-ExtraBold", 6, 0.8, WHITE)
    c.linkURL(WA + "?text=" + quote(msg), (x, y, x + w, y + h), relative=0)


def bloque_identificacion(c, ytop, th=172):
    head(c, ytop, "IDENTIFICACIÓN · 01 DE 02", ID_TITLE, ID_DESC)
    gap = 10; n = len(ID_PRODS); tw = (CW - (n - 1) * gap) / n; ty = ytop - 56 - th
    for k, (f, name) in enumerate(ID_PRODS):
        tile(c, M + k * (tw + gap), ty, tw, th, f, name, None)
    bh = 72; by = ty - 10 - bh; tw3 = (CW - 2 * gap) / 3; lw_ = tw3 * 2 + gap
    c.setStrokeColor(LINE); c.setLineWidth(0.8); c.setFillColor(WHITE); c.roundRect(M, by, lw_, bh, 12, stroke=1, fill=1)
    spaced(c, M + 14, by + bh - 17, "PRODUCTOS PRINCIPALES", "Mont-SemiBold", 6, 1.6, GREEN)
    rows = (len(ID_LIST) + 1) // 2; colw = (lw_ - 28) / 2; y0 = by + bh - 32
    for i, it in enumerate(ID_LIST):
        col, row = divmod(i, rows); xx = M + 14 + col * colw; yy = y0 - row * 13.2
        c.setFillColor(GREEN); c.circle(xx + 2.5, yy + 2.6, 2.1, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Mont-Medium", 7.6); c.drawString(xx + 9, yy, it)
    cx = M + lw_ + gap
    c.setFillColor(SOFT); c.roundRect(cx, by, tw3, bh, 12, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont("Mont-Bold", 8.2); c.drawString(cx + 12, by + bh - 19, "Carnés con tu diseño")
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 6.5)
    c.drawString(cx + 12, by + bh - 31, "Envíanos el logo y los datos de tu")
    c.drawString(cx + 12, by + bh - 40, "personal y nosotros los elaboramos.")
    wa_button(c, cx + 12, by + 9, tw3 - 24, "COTIZA TUS CARNÉS", "Hola, quiero cotizar carnés y porta carnés.")
    return by


def bloque_promocionales(c, ytop, ybot=62):
    head(c, ytop, "PROMOCIONALES · 02 DE 02", PR_TITLE, PR_DESC)
    top = ytop - 56; h = top - ybot
    pw = min(h * 1495 / 1052, CW * 0.6); ph = pw * 1052 / 1495; py = top - ph
    # foto de ambiente con esquinas redondeadas
    c.saveState(); p = c.beginPath(); p.roundRect(M, py, pw, ph, 13); c.clipPath(p, stroke=0, fill=0)
    c.drawImage(os.path.join(CUT, "promo_mesa.jpg"), M, py, pw, ph); c.restoreState()
    # panel de texto
    x = M + pw + 10; w = CW - pw - 10
    c.setFillColor(NAVY); c.roundRect(x, py, w, ph, 13, stroke=0, fill=1)
    stripe(c, x + 14, py + ph - 24, h=7)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 10.5); c.drawString(x + 34, py + ph - 24, "Tu marca en todo")
    lines = ["Manejamos una amplia variedad de", "productos promocionales y", "personalizados. Pregúntanos por el",
             "que requieras o envíanos una foto", "y con gusto te lo cotizamos."]
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 7.4)
    for i, t in enumerate(lines): c.drawString(x + 14, py + ph - 44 - i * 10.4, t)
    spaced(c, x + 14, py + ph - 108, "LOS MÁS PEDIDOS", "Mont-SemiBold", 5.8, 1.5, YELLOW)
    for i, t in enumerate(PR_LIST):
        yy = py + ph - 123 - i * 11.6
        c.setFillColor(GREEN); c.circle(x + 16.5, yy + 2.5, 2, stroke=0, fill=1)
        c.setFillColor(WHITE); c.setFont("Mont-Medium", 7.2); c.drawString(x + 23, yy, t)
    wa_button(c, x + 14, py + 12, w - 28, "ENVÍANOS TU FOTO", "Hola, quiero cotizar productos promocionales personalizados.")
    return py


def build(out, num=12):
    c = canvas.Canvas(out, pagesize=(W, H)); c.setTitle("Portafolio - Abastecer Empresarial - Identificación y promocionales")
    page_frame(c, num)
    section_header(c, "Identificación y promocionales", "Carnés, porta carnés y artículos personalizados con la imagen de tu empresa.")
    by = bloque_identificacion(c, H - 160)
    bloque_promocionales(c, by - 22)
    c.showPage(); c.save()


if __name__ == "__main__":
    out = os.path.join(HERE, "..", "salidas", "Identificacion_promocionales_vista_previa.pdf")
    build(out); print(out)
