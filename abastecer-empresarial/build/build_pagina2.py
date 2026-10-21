# Página 2: índice visual de líneas de suministro (6 destacadas con foto + 10 en cinta de íconos)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_portada_v2 import *
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader, simpleSplit

INK = HexColor("#0D1B2A"); GRAYT = HexColor("#5B6B7B"); TILE = HexColor("#F3F3F3"); LINE = HexColor("#E3E6EA")
CUT = os.path.join(HERE, "cut")

BIG = [  # (nombre, archivo, pagina)
    ("Dotación", "overol.png", 3), ("EPP", "casco.png", 4), ("Calzado", "bota.png", 5),
    ("Alturas", "alturas.png", 5), ("Señalización", "cono.png", 6), ("Emergencias", "extintor.png", 6),
]
SMALL = [
    (ic_aseo, "Aseo y cafetería", 7), (ic_tec, "Tecnología", 8), (ic_mob, "Mobiliario", 8),
    (ic_ergo, "Ergonomía", 9), (ic_id, "Identificación", 9), (ic_promo, "Promocionales", 9),
    (ic_estan, "Estanterías", 9), (ic_alim, "Alimentos y otros", 7), (ic_compras, "Compras especiales", 10),
    (ic_mas, "Y más…", 9),
]


def fit_image(c, path, x, y, w, h, shadow=True):
    ir = ImageReader(path); iw, ih = ir.getSize()
    s = min(w / iw, h / ih); dw, dh = iw * s, ih * s
    dx, dy = x + (w - dw) / 2, y + (h - dh) / 2
    if shadow:
        c.saveState(); c.setFillColor(INK)
        for k in range(6):
            c.setFillAlpha(0.025); c.ellipse(dx + dw * (0.12 - k * 0.012), dy - 4 - k * 0.8, dx + dw * (0.88 + k * 0.012), dy + 5 + k * 0.8, stroke=0, fill=1)
        c.restoreState()
    c.drawImage(path, dx, dy, dw, dh, mask="auto")


def build(out):
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Portafolio comercial - Abastecer Empresarial S.A.S. - Líneas de suministro")
    c.setFillColor(WHITE); c.rect(0, 0, W, H, stroke=0, fill=1)
    # banda superior
    c.setFillColor(NAVY); c.rect(0, H - 8, W, 8, stroke=0, fill=1)
    c.setFillColor(YELLOW); c.rect(W * 0.62, H - 8, W * 0.12, 8, stroke=0, fill=1)
    c.setFillColor(GREEN); c.rect(W * 0.74, H - 8, W * 0.26, 8, stroke=0, fill=1)
    # encabezado
    lw = 122; lh = lw * 344 / 1400
    c.drawImage(os.path.join(HERE, "logo_h.png"), M, H - 24 - lh, lw, lh, mask="auto")
    t = "PORTAFOLIO COMERCIAL"
    spaced(c, W - M - spaced_w(c, t, "Mont-SemiBold", 6.2, 2.0) + 2.0, H - 40, t, "Mont-SemiBold", 6.2, 2.0, GRAYT)
    c.setStrokeColor(LINE); c.setLineWidth(0.8); c.line(M, H - 66, W - M, H - 66)

    # título
    stripe(c, M, H - 94, h=7); spaced(c, M + 20, H - 93, "NUESTRAS LÍNEAS", "Mont-SemiBold", 6.6, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 25); c.drawString(M, H - 126, "Líneas de suministro")
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 9.4)
    c.drawString(M, H - 146, "Las líneas con mayor desarrollo en este portafolio, y otras que gestionamos según tu necesidad.")

    # 6 destacadas (3x2)
    gap = 12; tw = (CW - 2 * gap) / 3; th = 182; top = H - 166
    for i, (name, f, pg) in enumerate(BIG):
        r, k = divmod(i, 3)
        x = M + k * (tw + gap); y = top - (r + 1) * th - r * gap
        c.setFillColor(TILE); c.roundRect(x, y, tw, th, 14, stroke=0, fill=1)
        fit_image(c, os.path.join(CUT, f), x + 22, y + 46, tw - 44, th - 66)
        # chip nombre
        t = name; fw = c.stringWidth(t, "Mont-Bold", 8.6)
        c.setFillColor(WHITE); c.roundRect(x + 12, y + 12, fw + 22, 20, 10, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Mont-Bold", 8.6); c.drawString(x + 23, y + 18.3, t)
        # página
        spaced(c, x + tw - 12 - spaced_w(c, f"PÁG. {pg}", "Mont-SemiBold", 6, 1.2) + 1.2, y + th - 19, f"PÁG. {pg}", "Mont-SemiBold", 6, 1.2, GRAYT)
    ytop2 = top - 2 * th - gap

    # También suministramos
    y = ytop2 - 30
    stripe(c, M, y - 1, h=7); spaced(c, M + 20, y, "TAMBIÉN SUMINISTRAMOS", "Mont-SemiBold", 6.6, 1.8, GREEN)
    cols, g2, chh = 5, 8, 44
    cw_ = (CW - g2 * (cols - 1)) / cols
    top2 = y - 14
    for i, (fn, label, pg) in enumerate(SMALL):
        r, k = divmod(i, cols)
        x = M + k * (cw_ + g2); yy = top2 - (r + 1) * chh - r * g2
        c.setFillColor(WHITE); c.setStrokeColor(LINE); c.setLineWidth(0.9); c.roundRect(x, yy, cw_, chh, 10, stroke=1, fill=1)
        c.setFillColor(TILE); c.circle(x + 20, yy + chh / 2, 12.5, stroke=0, fill=1)
        icon(c, fn, x + 20, yy + chh / 2, size=14, color=INK)
        lines = simpleSplit(label, "Mont-SemiBold", 7.2, cw_ - 46)
        c.setFillColor(INK); c.setFont("Mont-SemiBold", 7.2)
        ty = yy + chh / 2 + (3 if len(lines) == 1 else 7) - (0 if len(lines) == 1 else 0)
        for ln in lines:
            c.drawString(x + 38, ty - 5, ln) if len(lines) == 1 else c.drawString(x + 38, ty - 3, ln); ty -= 9
        c.setFillColor(GRAYT); c.setFont("Mont-Medium", 5.6)
        c.drawString(x + 38, yy + 6.5, f"Pág. {pg}")
    ybot = top2 - 2 * chh - g2

    # banda CTA
    by = ybot - 88; bh = 64
    c.setFillColor(NAVY); c.roundRect(M, by, CW, bh, 14, stroke=0, fill=1)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 11); c.drawString(M + 20, by + bh - 26, "¿No ves lo que necesitas?")
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 8.2)
    c.drawString(M + 20, by + bh - 42, "Buscamos alternativas para productos fuera del portafolio.")
    bw = 168
    c.setFillColor(YELLOW); c.roundRect(W - M - bw - 16, by + 16, bw, 32, 16, stroke=0, fill=1)
    lab = "SOLICITA TU COTIZACIÓN"; wl = spaced_w(c, lab, "Mont-ExtraBold", 6.8, 1.0)
    spaced(c, W - M - bw - 16 + (bw - wl) / 2 + 0.5, by + 28.4, lab, "Mont-ExtraBold", 6.8, 1.0, NAVY)
    c.linkURL(WA, (W - M - bw - 16, by + 16, W - M - 16, by + 48), relative=0)

    # pie
    c.setStrokeColor(LINE); c.line(M, 50, W - M, 50)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 5.8)
    c.drawString(M, 36, "Referencias y disponibilidad sujetas a confirmación en la cotización.")
    c.setFillColor(GREEN); c.setFont("Mont-Bold", 7); c.drawRightString(W - M - 14, 36, "WhatsApp 350 862 4021")
    c.linkURL(WA, (W - M - 104, 31, W - M - 14, 44), relative=0)
    c.setFillColor(INK); c.setFont("Mont-Bold", 7.4); c.drawRightString(W - M, 36, "2")
    c.showPage(); c.save()
    return by


if __name__ == "__main__":
    print(build(os.path.join(HERE, "Pagina2_vista_previa.pdf")))
