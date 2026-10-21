# Portada v5: encabezado limpio + foto completa y clara (sin texto encima) + contenido ordenado debajo
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_portada_v2 import *
from build_portada_v4 import P1, P2, CARDS, poly_path
from reportlab.lib.utils import simpleSplit

HDR = 86                       # alto del encabezado navy
PT = H - HDR                   # borde superior de la foto
YL, YR = PT - 345, PT - 305    # borde inferior de la foto (izq, der)


def make_hero5(photo):
    import numpy as np
    from PIL import Image
    S = 3; wpx = int(W * S); hpt = PT - (YL - 10); hpx = int(hpt * S)
    im = Image.open(photo).convert("RGB")
    sc = wpx / im.width; nh = int(im.height * sc)
    im = im.resize((wpx, nh), Image.LANCZOS)
    y0 = int((nh - hpx) * 0.30); im = im.crop((0, y0, wpx, y0 + hpx))
    a = np.asarray(im).astype(float)
    y = np.linspace(0, 1, hpx)[:, None]
    al = (0.06 + np.clip((y - 0.78) / 0.22, 0, 1) ** 1.4 * 0.42)[:, :, None]   # velo muy leve
    navy = np.array([13, 27, 42], float)
    out = a * (1 - al) + navy * al
    p = os.path.join(HERE, "hero_v7.jpg")
    Image.fromarray(out.astype("uint8")).save(p, quality=93)
    return p


def build5(out, photo):
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Portafolio comercial - Abastecer Empresarial S.A.S.")
    c.setAuthor("Abastecer Empresarial S.A.S."); c.setSubject("Un solo aliado para múltiples necesidades de suministro")
    c.setFillColor(NAVY); c.rect(0, 0, W, H, stroke=0, fill=1)

    # foto
    c.saveState(); c.clipPath(poly_path(c, [(0, PT), (W, PT), (W, YR), (0, YL)]), stroke=0, fill=0)
    c.drawImage(make_hero5(photo), 0, YL - 10, W, PT - (YL - 10)); c.restoreState()
    c.setFillColor(YELLOW); c.drawPath(poly_path(c, [(0, YL), (W, YR), (W, YR - 5), (0, YL - 5)]), stroke=0, fill=1)
    c.setFillColor(GREEN); c.drawPath(poly_path(c, [(0, YL - 5), (W, YR - 5), (W, YR - 10), (0, YL - 10)]), stroke=0, fill=1)
    c.setFillColor(MUTED2); c.setFont("Mont-Medium", 5.8)
    c.drawRightString(W - M, YR - 24, "Imagen referencial")

    # encabezado
    pw_, ph_ = 214, 56; py_ = H - (HDR - ph_) / 2 - ph_ - 0
    py_ = H - 15 - ph_
    c.setFillColor(WHITE); c.roundRect(M, py_, pw_, ph_, 11, stroke=0, fill=1)
    lw = 192; lh = lw * 344 / 1400
    c.drawImage(os.path.join(HERE, "logo_h.png"), M + (pw_ - lw) / 2, py_ + (ph_ - lh) / 2, lw, lh, mask="auto")
    t = "PORTAFOLIO COMERCIAL"
    spaced(c, W - M - spaced_w(c, t, "Mont-SemiBold", 6.4, 2.2) + 2.2, py_ + ph_ / 2 - 2, t, "Mont-SemiBold", 6.4, 2.2, WHITE)

    # titular
    y = YL - 44
    c.setFont("Mont-ExtraBold", 28)
    c.setFillColor(WHITE); c.drawString(M, y, "Un solo aliado para")
    c.setFillColor(YELLOW); c.drawString(M, y - 33, "múltiples necesidades")
    c.setFillColor(WHITE); c.drawString(M, y - 66, "de suministro")

    # Quiénes somos
    y = y - 66 - 34
    stripe(c, M, y - 1, h=7); spaced(c, M + 20, y, "QUIÉNES SOMOS", "Mont-SemiBold", 6.6, 1.8, YELLOW)
    y -= 22
    for i, para in enumerate((P1, P2)):
        c.setFillColor(MUTED if i == 0 else WHITE); c.setFont("Mont-Medium", 9.6)
        for ln in simpleSplit(para, "Mont-Medium", 9.6, CW):
            c.drawString(M, y, ln); y -= 14.4
        y -= 5

    # 4 tarjetas (icono a la izquierda)
    gap, ch = 10, 62
    cw_ = (CW - gap * 3) / 4
    top = y - 2
    for i, (fn, ttl, txt) in enumerate(CARDS):
        x = M + i * (cw_ + gap); yy = top - ch
        c.setFillColor(PANEL); c.setStrokeColor(PANEL_LINE); c.setLineWidth(0.8)
        c.roundRect(x, yy, cw_, ch, 10, stroke=1, fill=1)
        icon(c, fn, x + 12 + 8, yy + ch - 18, size=16, color=YELLOW)
        c.setFillColor(WHITE); c.setFont("Mont-Bold", 8.2); c.drawString(x + 38, yy + ch - 21, ttl)
        c.setFillColor(MUTED); c.setFont("Mont-Medium", 6.6)
        ty = yy + ch - 37
        for ln in simpleSplit(txt, "Mont-Medium", 6.6, cw_ - 22):
            c.drawString(x + 12, ty, ln); ty -= 8.8
    cards_bottom = top - ch

    # esquina inferior
    p = c.beginPath(); p.moveTo(W - 205, 0); p.lineTo(W - 125, 74); p.lineTo(W, 74); p.lineTo(W, 0); p.close()
    c.setFillColor(GREEN); c.drawPath(p, stroke=0, fill=1)
    p = c.beginPath(); p.moveTo(W - 212, 0); p.lineTo(W - 132, 74); p.lineTo(W - 104, 74); p.lineTo(W - 184, 0); p.close()
    c.setFillColor(YELLOW); c.drawPath(p, stroke=0, fill=1)

    # CTA + nota legal
    by = 44
    c.setFillColor(YELLOW); c.roundRect(M, by, 190, 32, 16, stroke=0, fill=1)
    lab = "SOLICITA TU COTIZACIÓN"; wl = spaced_w(c, lab, "Mont-ExtraBold", 7.4, 1.1)
    spaced(c, M + (190 - wl) / 2 + 0.5, by + 12.4, lab, "Mont-ExtraBold", 7.4, 1.1, NAVY)
    c.linkURL(WA, (M, by, M + 190, by + 32), relative=0)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 8.2); c.drawString(M + 204, by + 17, "WhatsApp 350 862 4021")
    c.linkURL(WA, (M + 204, by + 12, M + 204 + 108, by + 26), relative=0)
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 7.2); c.drawString(M + 204, by + 5.5, "abastecerempresarial.com")
    c.linkURL(WEB, (M + 204, by + 2, M + 204 + 100, by + 14), relative=0)
    c.setFillColor(MUTED2); c.setFont("Mont-Medium", 5.8)
    c.drawString(M, 26, "Referencias y disponibilidad sujetas a confirmación en la cotización.")
    c.showPage(); c.save()
    return cards_bottom, by + 32


if __name__ == "__main__":
    print(build5(os.path.join(HERE, "Portada_Abastecer_v7.pdf"), os.path.join(HERE, "bodega_v7.jpg")))
