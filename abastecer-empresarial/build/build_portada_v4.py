# Portada v4: foto hero de bodega + velo + corte diagonal + Quiénes somos + 4 tarjetas
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_portada_v2 import *
from reportlab.lib.utils import simpleSplit, ImageReader

P1 = ("Abastecer Empresarial S.A.S. es una empresa colombiana dedicada al suministro de productos "
      "para empresas, instituciones y organizaciones.")
P2 = ("Atendemos los requerimientos de todas las áreas de tu operación con un solo aliado: desde dotación y "
      "seguridad y salud en el trabajo, hasta aseo, tecnología, mobiliario y mucho más.")
CARDS = [
    (ic_estan, "Variedad", "Otras necesidades de abastecimiento empresarial."),
    (ic_epp, "Especialización", "Dotación, EPP y suministros de SST."),
    (ic_compras, "Búsqueda", "Alternativas para productos fuera del portafolio."),
    (ic_id, "Cotización", "Según las necesidades de cada cliente."),
]
YL, YR = H - 470, H - 425      # borde inferior de la foto (izq, der)


def poly_path(c, pts):
    p = c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    p.close(); return p



def make_hero(photo):
    import numpy as np
    from PIL import Image
    S = 3; wpx = int(W * S); hpt = H - YL + 10; hpx = int(hpt * S)
    im = Image.open(photo).convert("RGB")
    sc = hpx / im.height; nw = int(im.width * sc)
    im = im.resize((nw, hpx), Image.LANCZOS)
    x0 = int((nw - wpx) * 0.52); im = im.crop((x0, 0, x0 + wpx, hpx))
    a = np.asarray(im).astype(float)
    y = np.linspace(0, 1, hpx)[:, None]          # 0 arriba, 1 abajo
    bot = np.clip((y - 0.30) / 0.70, 0, 1) ** 1.3 * 0.90   # sube desde el corte
    top = np.clip(1 - y / 0.28, 0, 1) ** 1.6 * 0.55
    al = np.clip(0.26 + bot + top, 0, 0.93)[:, :, None]
    navy = np.array([13, 27, 42], float)
    out = a * (1 - al) + navy * al
    p = os.path.join(HERE, "hero_veil.jpg")
    Image.fromarray(out.astype("uint8")).save(p, quality=92)
    return p

def build4(out, photo):
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Portafolio comercial - Abastecer Empresarial S.A.S.")
    c.setAuthor("Abastecer Empresarial S.A.S."); c.setSubject("Un solo aliado para múltiples necesidades de suministro")
    c.setFillColor(NAVY); c.rect(0, 0, W, H, stroke=0, fill=1)

    # foto recortada al polígono
    area = [(0, H), (W, H), (W, YR), (0, YL)]
    c.saveState(); c.clipPath(poly_path(c, area), stroke=0, fill=0)
    c.drawImage(make_hero(photo), 0, YL - 10, W, H - YL + 10)
    c.restoreState()

    # franjas del corte diagonal
    d = YR - YL
    c.setFillColor(YELLOW); c.drawPath(poly_path(c, [(0, YL), (W, YR), (W, YR - 5), (0, YL - 5)]), stroke=0, fill=1)
    c.setFillColor(GREEN); c.drawPath(poly_path(c, [(0, YL - 5), (W, YR - 5), (W, YR - 10), (0, YL - 10)]), stroke=0, fill=1)

    # cabecera
    c.setFillColor(WHITE); c.roundRect(M, H - 98, 176, 48, 10, stroke=0, fill=1)
    lw = 160; lh = lw * 344 / 1400
    c.drawImage(os.path.join(HERE, "logo_h.png"), M + 8, H - 98 + (48 - lh) / 2, lw, lh, mask="auto")
    t = "PORTAFOLIO COMERCIAL"
    spaced(c, W - M - spaced_w(c, t, "Mont-SemiBold", 6.4, 2.2) + 2.2, H - 68, t, "Mont-SemiBold", 6.4, 2.2, WHITE)

    # titular sobre la foto
    c.setFont("Mont-ExtraBold", 36)
    c.setFillColor(WHITE); c.drawString(M, YL + 112, "Un solo aliado para")
    c.setFillColor(YELLOW); c.drawString(M, YL + 72, "múltiples necesidades")
    c.setFillColor(WHITE); c.drawString(M, YL + 32, "de suministro")
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 5.8)
    s = "Imagen referencial"; c.drawRightString(W - M, YR + 8, s)

    # Quiénes somos
    y = YL - 44
    stripe(c, M, y - 1, h=7); spaced(c, M + 20, y, "QUIÉNES SOMOS", "Mont-SemiBold", 6.6, 1.8, YELLOW)
    y -= 26
    for i, para in enumerate((P1, P2)):
        c.setFillColor(MUTED if i == 0 else WHITE); c.setFont("Mont-Medium", 10.2)
        for ln in simpleSplit(para, "Mont-Medium", 10.2, CW):
            c.drawString(M, y, ln); y -= 16
        y -= 7

    # 4 tarjetas
    gap, ch = 10, 96
    cw_ = (CW - gap * 3) / 4
    top = y - 6
    for i, (fn, ttl, txt) in enumerate(CARDS):
        x = M + i * (cw_ + gap); yy = top - ch
        c.setFillColor(PANEL); c.setStrokeColor(PANEL_LINE); c.setLineWidth(0.8)
        c.roundRect(x, yy, cw_, ch, 10, stroke=1, fill=1)
        icon(c, fn, x + 22, yy + ch - 24, size=19, color=YELLOW)
        c.setFillColor(WHITE); c.setFont("Mont-Bold", 8.6); c.drawString(x + 12, yy + ch - 50, ttl)
        c.setFillColor(MUTED); c.setFont("Mont-Medium", 6.9)
        ty = yy + ch - 63
        for ln in simpleSplit(txt, "Mont-Medium", 6.9, cw_ - 22):
            c.drawString(x + 12, ty, ln); ty -= 9.4

    # esquina inferior
    p = c.beginPath(); p.moveTo(W - 205, 0); p.lineTo(W - 125, 74); p.lineTo(W, 74); p.lineTo(W, 0); p.close()
    c.setFillColor(GREEN); c.drawPath(p, stroke=0, fill=1)
    p = c.beginPath(); p.moveTo(W - 212, 0); p.lineTo(W - 132, 74); p.lineTo(W - 104, 74); p.lineTo(W - 184, 0); p.close()
    c.setFillColor(YELLOW); c.drawPath(p, stroke=0, fill=1)

    # CTA + nota legal
    by = 46
    c.setFillColor(YELLOW); c.roundRect(M, by, 190, 32, 16, stroke=0, fill=1)
    lab = "SOLICITA TU COTIZACIÓN"; wl = spaced_w(c, lab, "Mont-ExtraBold", 7.4, 1.1)
    spaced(c, M + (190 - wl) / 2 + 0.5, by + 12.4, lab, "Mont-ExtraBold", 7.4, 1.1, NAVY)
    c.linkURL(WA, (M, by, M + 190, by + 32), relative=0)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 8.2); c.drawString(M + 204, by + 17, "WhatsApp 350 862 4021")
    c.linkURL(WA, (M + 204, by + 12, M + 204 + 108, by + 26), relative=0)
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 7.2); c.drawString(M + 204, by + 5.5, "abastecerempresarial.com")
    c.linkURL(WEB, (M + 204, by + 2, M + 204 + 100, by + 14), relative=0)
    c.setFillColor(MUTED2); c.setFont("Mont-Medium", 5.8)
    c.drawString(M, 28, "Referencias y disponibilidad sujetas a confirmación en la cotización.")
    c.showPage(); c.save()
    return yy


if __name__ == "__main__":
    print(build4(os.path.join(HERE, "Portada_Abastecer_v4.pdf"), os.path.join(HERE, "bodega_hero.jpg")))
