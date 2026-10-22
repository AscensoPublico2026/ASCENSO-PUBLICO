# EPP por líneas (páginas 4, 5 y 6): cada línea con 3 productos y llamado a cotizar lo que no aparece
import os, sys
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_pagina2 import *
from reportlab.lib.colors import HexColor

SOFT = HexColor("#EEF6F0")

LINEAS = [
    ("Línea de protección para la cabeza", "Cascos y accesorios para obra, planta y trabajo al aire libre.",
     [("epp_cab_casco_amarillo.png", "Casco de seguridad"), ("epp_cab_casco_blanco.png", "Casco con ajuste ratchet"), ("epp_cab_pava.png", "Pava con cubrenuca")],
     "barbuquejos, alerones, monjas, pasamontañas y gorras"),
    ("Línea de protección visual y facial", "Gafas, monogafas y caretas contra impacto, salpicaduras y partículas.",
     [("epp_vis_gafa.png", "Gafas de seguridad"), ("epp_vis_monogafa.png", "Monogafas"), ("epp_vis_careta.png", "Careta facial")],
     "lentes claros u oscuros, visores de repuesto y caretas para soldador"),
    ("Línea de protección auditiva", "Control del ruido en planta, obra y operación de maquinaria.",
     [("epp_aud_copa.png", "Protector tipo copa"), ("epp_aud_insercion.png", "Tapa oídos de inserción"), ("epp_aud_espuma.png", "Tapa oídos en espuma")],
     "protectores para casco y presentaciones por caja"),
    ("Línea de protección respiratoria", "Respiradores y tapabocas para polvos, gases y vapores.",
     [("epp_res_doble.png", "Respirador de doble filtro"), ("epp_res_uno.png", "Respirador de un filtro"), ("epp_res_n95.png", "Tapabocas N95")],
     "filtros, cartuchos, prefiltros y tapabocas desechables"),
    ("Línea de protección para manos", "Guantes para manipulación, químicos, calor y trabajo pesado.",
     [("epp_man_vaqueta.png", "Guantes en vaqueta"), ("epp_man_nitrilo.png", "Guantes de nitrilo"), ("epp_man_carnaza.png", "Guantes en carnaza")],
     "guantes anticorte, de impacto, para soldador, desechables y mangas"),
    ("Línea de protección corporal", "Prendas de protección para procesos, químicos y ambientes húmedos.",
     [("epp_cor_tyvek.png", "Traje desechable tipo Tyvek"), ("epp_cor_delantal.png", "Delantal en vaqueta"), ("epp_cor_impermeable.png", "Conjunto impermeable")],
     "delantales, fajas, rodilleras, capas y overoles"),
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
    # pie
    c.setStrokeColor(LINE); c.line(M, 50, W - M, 50)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 5.8)
    c.drawString(M, 36, "Referencias y disponibilidad sujetas a confirmación en la cotización.")
    c.setFillColor(GREEN); c.setFont("Mont-Bold", 7); c.drawRightString(W - M - 14, 36, "WhatsApp 350 862 4021")
    c.linkURL(WA, (W - M - 104, 31, W - M - 14, 44), relative=0)
    c.setFillColor(INK); c.setFont("Mont-Bold", 7.4); c.drawRightString(W - M, 36, str(num))


def line_block(c, ytop, idx, title, desc, prods, mas, th=160):
    # encabezado de la línea
    stripe(c, M, ytop - 9, h=7)
    lab = f"EPP · {idx:02d} DE {len(LINEAS):02d}"
    spaced(c, M + 20, ytop - 8, lab, "Mont-SemiBold", 6.4, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 17.5); c.drawString(M, ytop - 32, title)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 8.6); c.drawString(M, ytop - 47, desc)
    # 3 productos
    gap = 10; tw = (CW - 2 * gap) / 3; ty = ytop - 60 - th
    for k, (f, name) in enumerate(prods):
        x = M + k * (tw + gap)
        c.setFillColor(TILE); c.roundRect(x, ty, tw, th, 13, stroke=0, fill=1)
        fit_image(c, os.path.join(CUT, f), x + 16, ty + 38, tw - 32, th - 52)
        fw = c.stringWidth(name, "Mont-Bold", 7.6)
        c.setFillColor(WHITE); c.roundRect(x + 10, ty + 10, fw + 20, 19, 9.5, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Mont-Bold", 7.6); c.drawString(x + 20, ty + 16.2, name)
    # llamado: ¿necesitas algo específico?
    bw = 104
    sub = simpleSplit(f"Si no lo ves aquí, pregúntanos. También cotizamos {mas}.", "Mont-Medium", 7.2, CW - 44 - bw - 34)
    bh = 34 + 9 * len(sub); by = ty - 10 - bh
    c.setFillColor(SOFT); c.roundRect(M, by, CW, bh, 12, stroke=0, fill=1)
    c.setFillColor(GREEN); c.circle(M + 24, by + bh / 2, 11, stroke=0, fill=1)
    c.setFillColor(WHITE); c.setFont("Mont-ExtraBold", 13); c.drawCentredString(M + 24, by + bh / 2 - 4.6, "?")
    c.setFillColor(INK); c.setFont("Mont-Bold", 9.2); c.drawString(M + 44, by + bh - 19, "¿Necesitas algo específico de esta línea?")
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 7.2)
    for i, ln in enumerate(sub): c.drawString(M + 44, by + bh - 31 - 9 * i, ln)
    bx = W - M - bw - 12; byb = by + (bh - 22) / 2
    c.setFillColor(GREEN); c.roundRect(bx, byb, bw, 22, 11, stroke=0, fill=1)
    t = "PREGÚNTANOS"; wl = spaced_w(c, t, "Mont-ExtraBold", 6.6, 1.0)
    spaced(c, bx + (bw - wl) / 2 + 0.5, byb + 7.6, t, "Mont-ExtraBold", 6.6, 1.0, WHITE)
    msg = f"Hola, quiero cotizar productos de la {title.lower()}."
    c.linkURL(WA + "?text=" + quote(msg), (bx, byb, bx + bw, byb + 22), relative=0)
    return by


def build(out, first_page=4):
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Portafolio comercial - Abastecer Empresarial S.A.S. - Elementos de protección personal (EPP)")
    pairs = [LINEAS[i:i + 2] for i in range(0, len(LINEAS), 2)]
    n = 0
    for p, pair in enumerate(pairs):
        page_frame(c, first_page + p)
        y = H - 82
        if p == 0:
            stripe(c, M, H - 94, h=7); spaced(c, M + 20, H - 93, "LÍNEA DE SUMINISTRO", "Mont-SemiBold", 6.6, 1.8, GREEN)
            c.setFillColor(INK); c.setFont("Mont-ExtraBold", 22); c.drawString(M, H - 124, "Elementos de protección personal (EPP)")
            c.setFillColor(GRAYT); c.setFont("Mont-Medium", 9.4)
            c.drawString(M, H - 146, "Organizados por línea de protección. Cotizamos referencias, tallas y marcas según tu necesidad.")
            c.setStrokeColor(LINE); c.line(M, H - 162, W - M, H - 162)
            y = H - 180
        for l in pair:
            n += 1
            by = line_block(c, y, n, *l, th=160 if p == 0 else 196)
            y = by - (30 if p == 0 else 46)
        c.showPage()
    c.save()


if __name__ == "__main__":
    out = os.path.join(HERE, "..", "salidas", "EPP_por_lineas_pags_4-6.pdf")
    build(out)
    print(out)
