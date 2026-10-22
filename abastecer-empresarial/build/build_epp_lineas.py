# EPP por líneas (páginas 4, 5 y 6): cada línea con 3 productos, listado de productos principales
# y llamado a cotizar lo que no aparece. Recortes mejorados con Real-ESRGAN (realesr-general-x4v3) + rembg.
import os, sys
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_pagina2 import *
from reportlab.lib.colors import HexColor

SOFT = HexColor("#EEF6F0")
SW = {"blanco": "#FFFFFF", "amarillo": "#F5C800", "azul": "#1F4FA3", "verde": "#1E9A4B", "rojo": "#D93A26", "gris": "#8C8C8C"}

# (título, descripción, [(imagen, nombre, colores)], listado de productos principales)
LINEAS = [
    ("Línea de protección para la cabeza", "Cascos y accesorios para obra, planta y trabajo al aire libre.",
     [("epp_cas_cert.png", "Casco tipo I certificado", ["blanco", "amarillo", "azul", "verde", "rojo", "gris"]),
      ("epp_cas_ratchet.png", "Casco tipo I con ratchet", ["blanco", "amarillo", "azul"]),
      ("epp_cas_tipo2.png", "Casco tipo II", ["blanco", "amarillo", "azul"])],
     ["Casco tipo I certificado", "Casco tipo I con ratchet", "Casco tipo II", "Casco para alturas y rescate",
      "Barbuquejo de 3 y 4 puntos", "Alerones en jean", "Monjas y pasamontañas", "Gorras en dril y malla"]),
    ("Línea de protección visual y facial", "Gafas, monogafas y caretas contra impacto, salpicaduras y partículas.",
     [("epp_gafas_trio.png", "Gafas tricolor, B105 y Spy", None), ("epp_monogafa.png", "Monogafas", None), ("epp_careta.png", "Careta para esmerilar", None)],
     ["Gafas tricolor, B105 y Spy", "Lente claro u oscuro", "Monogafas", "Gafas de laboratorio",
      "Careta para esmerilar", "Careta guadañadora", "Visores y acetatos de repuesto", "Caretas para soldador"]),
    ("Línea de protección auditiva", "Control del ruido en planta, obra y operación de maquinaria.",
     [("epp_aud_copa.png", "Protector tipo copa", None), ("epp_aud_insercion.png", "Tapa oídos de inserción con estuche", None), ("epp_aud_espuma.png", "Tapa oídos en espuma", None)],
     ["Protector auditivo tipo copa", "Protector auditivo para casco", "Tapa oídos de inserción con estuche", "Tapa oídos en espuma"]),
    ("Línea de protección respiratoria", "Respiradores y tapabocas para polvos, gases y vapores.",
     [("epp_res_doble.png", "Respirador de doble filtro", None), ("epp_res_uno.png", "Respirador de un filtro", None), ("epp_res_n95.png", "Tapabocas N95", None)],
     ["Respirador de doble filtro", "Respirador de un filtro", "Máscaras media cara y cara completa", "Filtros y cartuchos",
      "Prefiltros y retenedores", "Tapabocas N95", "Tapabocas desechables", "Tapabocas industriales"]),
    ("Línea de protección para manos", "Guantes para manipulación, corte, calor y trabajo pesado.",
     [("epp_man_vaqueta.png", "Guantes en vaqueta", None), ("epp_man_anticorte.png", "Guantes anticorte", None), ("epp_man_carnaza.png", "Guantes en carnaza", None)],
     ["Guantes en vaqueta", "Guantes anticorte", "Guantes en carnaza", "Guantes de nitrilo",
      "Guantes de impacto", "Guantes para soldador", "Guantes de hilaza con puntos", "Mangas en carnaza y vaqueta"]),
    ("Línea de protección corporal", "Prendas de protección para procesos, químicos y ambientes húmedos.",
     [("epp_cor_tyvek.png", "Traje desechable tipo Tyvek", None), ("epp_cor_delantal.png", "Delantal en vaqueta", None), ("epp_cor_impermeable.png", "Conjunto impermeable", None)],
     ["Trajes desechables tipo Tyvek", "Delantales en vaqueta, carnaza y PVC", "Conjuntos impermeables", "Capas y gabardinas",
      "Overoles", "Fajas lumbares", "Rodilleras y canilleras", "Zapatones en PVC"]),
]


def page_frame(c, num):
    c.setFillColor(WHITE); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(NAVY); c.rect(0, H - 8, W, 8, stroke=0, fill=1)
    c.setFillColor(YELLOW); c.rect(W * 0.62, H - 8, W * 0.12, 8, stroke=0, fill=1)
    c.setFillColor(GREEN); c.rect(W * 0.74, H - 8, W * 0.26, 8, stroke=0, fill=1)
    lw = 122; lh = lw * 344 / 1400
    c.drawImage(os.path.join(HERE, "logo_h.png"), M, H - 24 - lh, lw, lh, mask="auto")
    t = "PORTAFOLIO COMERCIAL"
    spaced(c, W - M - spaced_w(c, t, "Mont-SemiBold", 6.2, 2.0) + 2.0, H - 40, t, "Mont-SemiBold", 6.2, 2.0, GRAYT)
    c.setStrokeColor(LINE); c.setLineWidth(0.8); c.line(M, H - 66, W - M, H - 66)
    c.setStrokeColor(LINE); c.line(M, 50, W - M, 50)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 5.8)
    c.drawString(M, 36, "Referencias y disponibilidad sujetas a confirmación en la cotización.")
    c.setFillColor(GREEN); c.setFont("Mont-Bold", 7); c.drawRightString(W - M - 14, 36, "WhatsApp 350 862 4021")
    c.linkURL(WA, (W - M - 104, 31, W - M - 14, 44), relative=0)
    c.setFillColor(INK); c.setFont("Mont-Bold", 7.4); c.drawRightString(W - M, 36, str(num))


def tile(c, x, y, w, h, f, name, colors):
    c.setFillColor(TILE); c.roundRect(x, y, w, h, 13, stroke=0, fill=1)
    top_pad = 24 if colors else 12
    fit_image(c, os.path.join(CUT, f), x + 12, y + 36, w - 24, h - 36 - top_pad)
    if colors:
        r = 3.6; cx = x + 14
        c.setFillColor(GRAYT); c.setFont("Mont-SemiBold", 5.4); c.drawString(cx, y + h - 15.5, "COLORES")
        cx += c.stringWidth("COLORES", "Mont-SemiBold", 5.4) + 7
        for col in colors:
            c.setFillColor(HexColor(SW[col])); c.setStrokeColor(HexColor("#C9CED4")); c.setLineWidth(0.6)
            c.circle(cx + r, y + h - 13.6, r, stroke=1, fill=1); cx += 2 * r + 3.2
    fs = 7.4
    while c.stringWidth(name, "Mont-Bold", fs) > w - 40: fs -= 0.2
    fw = c.stringWidth(name, "Mont-Bold", fs)
    c.setFillColor(WHITE); c.roundRect(x + 10, y + 10, fw + 20, 19, 9.5, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont("Mont-Bold", fs); c.drawString(x + 20, y + 16.4, name)


def line_block(c, ytop, idx, title, desc, prods, listado, th):
    stripe(c, M, ytop - 9, h=7)
    spaced(c, M + 20, ytop - 8, f"EPP · {idx:02d} DE {len(LINEAS):02d}", "Mont-SemiBold", 6.4, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 17); c.drawString(M, ytop - 31, title)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 8.4); c.drawString(M, ytop - 45, desc)
    gap = 10; tw = (CW - 2 * gap) / 3; ty = ytop - 56 - th
    for k, (f, name, colors) in enumerate(prods):
        tile(c, M + k * (tw + gap), ty, tw, th, f, name, colors)
    # listado de productos principales + llamado
    bh = 84; by = ty - 10 - bh
    lw_ = tw * 2 + gap
    c.setStrokeColor(LINE); c.setLineWidth(0.8); c.setFillColor(WHITE); c.roundRect(M, by, lw_, bh, 12, stroke=1, fill=1)
    spaced(c, M + 14, by + bh - 17, "PRODUCTOS PRINCIPALES", "Mont-SemiBold", 6, 1.6, GREEN)
    rows = (len(listado) + 1) // 2; colw = (lw_ - 28) / 2; lh_ = 13.2
    y0 = by + bh - 32
    for i, it in enumerate(listado):
        col, row = divmod(i, rows)
        xx = M + 14 + col * colw; yy = y0 - row * lh_
        c.setFillColor(GREEN); c.circle(xx + 2.5, yy + 2.6, 2.1, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Mont-Medium", 7.6); c.drawString(xx + 9, yy, it)
    # llamado
    cx = M + lw_ + gap; cw_ = tw
    c.setFillColor(SOFT); c.roundRect(cx, by, cw_, bh, 12, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont("Mont-Bold", 8.2)
    c.drawString(cx + 12, by + bh - 19, "¿Necesitas algo específico")
    c.drawString(cx + 12, by + bh - 29.5, "de esta línea?")
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 6.5)
    c.drawString(cx + 12, by + bh - 42, "Si no lo ves en el listado, pregúntanos.")
    bw = cw_ - 24; bx = cx + 12; byb = by + 10
    c.setFillColor(GREEN); c.roundRect(bx, byb, bw, 21, 10.5, stroke=0, fill=1)
    t = "PREGÚNTANOS POR WHATSAPP"; wl = spaced_w(c, t, "Mont-ExtraBold", 6, 0.8)
    spaced(c, bx + (bw - wl) / 2 + 0.4, byb + 7.6, t, "Mont-ExtraBold", 6, 0.8, WHITE)
    msg = f"Hola, quiero cotizar productos de la {title.lower()}."
    c.linkURL(WA + "?text=" + quote(msg), (bx, byb, bx + bw, byb + 21), relative=0)
    return by


def build(out, first_page=4):
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Portafolio comercial - Abastecer Empresarial S.A.S. - Elementos de protección personal (EPP)")
    n = 0
    for p in range(0, len(LINEAS), 2):
        page_frame(c, first_page + p // 2)
        y = H - 84
        if p == 0:
            stripe(c, M, H - 94, h=7); spaced(c, M + 20, H - 93, "LÍNEA DE SUMINISTRO", "Mont-SemiBold", 6.6, 1.8, GREEN)
            c.setFillColor(INK); c.setFont("Mont-ExtraBold", 22); c.drawString(M, H - 122, "Elementos de protección personal (EPP)")
            c.setFillColor(GRAYT); c.setFont("Mont-Medium", 9)
            c.drawString(M, H - 139, "Organizados por línea de protección. Cotizamos referencias, tallas y marcas según tu necesidad.")
            y = H - 160
        th = 150 if p == 0 else 172
        for l in LINEAS[p:p + 2]:
            n += 1
            by = line_block(c, y, n, *l, th=th)
            y = by - (24 if p == 0 else 34)
        c.showPage()
    c.save()


if __name__ == "__main__":
    out = os.path.join(HERE, "..", "salidas", "EPP_por_lineas_pags_4-6.pdf")
    build(out)
    print(out)
