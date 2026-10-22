# Página 2 v3: grupos de 3 productos (catálogo) + imágenes de Gemini en las líneas restantes
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_pagina2 import *
from PIL import Image

UP = os.path.join(HERE, "..", "fotos") + os.sep
AI = {
    "Temporada y celebraciones": UP + "temporada_gemini.jpg",
    "Promocionales y carnés": UP + "promocionales_gemini.jpg",
    "Tecnología": UP + "tecnologia_gemini.jpg",
    "Aseo y cafetería": UP + "aseo_gemini.jpg",
}
LINES = [
    ("Dotación", ["dot_camibuso.png", "overol.png", "dot_pantalon.png"], ic_dotacion, 3),
    ("EPP", ["epp_orejeras.png", "casco.png", "guantes.png"], ic_epp, 4),
    ("Calzado", ["cal_tenis.png", "bota.png", "cal_botapvc.png"], ic_calzado, 7),
    ("Alturas", ["alt_mosq.png", "alturas.png"], ic_alturas, 7),
    ("Señalización", ["sen_cinta.png", "cono.png", "chaleco.png"], ic_senal, 8),
    ("Emergencias", ["eme_botiquin.png", "extintor.png", "eme_camilla.png"], ic_emerg, 8),
    ("Tecnología", None, ic_tec, 10), ("Mobiliario y ergonomía", ["mob_reposapies.png", "mob_silla.png"], ic_mob, 10), ("Aseo y cafetería", None, ic_aseo, 9),
    ("Promocionales y carnés", None, ic_promo, 11), ("Temporada y celebraciones", None, ic_alim, 9), ("Compras especiales", "icon", ic_compras, 12),
]


def cover_crop(path, tw, th, focus=0.5, scale=3):
    im = Image.open(path).convert("RGB")
    ar = tw / th
    if im.width / im.height > ar:
        nw = int(im.height * ar); x0 = int((im.width - nw) * 0.5); im = im.crop((x0, 0, x0 + nw, im.height))
    else:
        nh = int(im.width / ar); y0 = int((im.height - nh) * focus); im = im.crop((0, y0, im.width, y0 + nh))
    im = im.resize((int(tw * scale), int(th * scale)), Image.LANCZOS)
    p = os.path.join(HERE, "_tile_%d.jpg" % (abs(hash(path)) % 10**6)); im.save(p, quality=92); return p


def build3(out):
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Portafolio comercial - Abastecer Empresarial S.A.S. - Líneas de suministro")
    c.setFillColor(WHITE); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(NAVY); c.rect(0, H - 8, W, 8, stroke=0, fill=1)
    c.setFillColor(YELLOW); c.rect(W * 0.62, H - 8, W * 0.12, 8, stroke=0, fill=1)
    c.setFillColor(GREEN); c.rect(W * 0.74, H - 8, W * 0.26, 8, stroke=0, fill=1)
    lw = 122; lh = lw * 344 / 1400
    c.drawImage(os.path.join(HERE, "logo_h.png"), M, H - 24 - lh, lw, lh, mask="auto")
    t = "PORTAFOLIO COMERCIAL"
    spaced(c, W - M - spaced_w(c, t, "Mont-SemiBold", 6.2, 2.0) + 2.0, H - 40, t, "Mont-SemiBold", 6.2, 2.0, GRAYT)
    c.setStrokeColor(LINE); c.setLineWidth(0.8); c.line(M, H - 66, W - M, H - 66)
    stripe(c, M, H - 94, h=7); spaced(c, M + 20, H - 93, "NUESTRAS LÍNEAS", "Mont-SemiBold", 6.6, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 25); c.drawString(M, H - 126, "Líneas de suministro")
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 9.4)
    c.drawString(M, H - 146, "Un solo aliado para las distintas áreas de tu operación.")

    gap = 10; tw = (CW - 2 * gap) / 3; th = 122; top = H - 164
    for i, (name, files, fn, pg) in enumerate(LINES):
        r, k = divmod(i, 3)
        x = M + k * (tw + gap); y = top - (r + 1) * th - r * gap
        if name in AI:
            c.saveState(); p = c.beginPath(); p.roundRect(x, y, tw, th, 13); c.clipPath(p, stroke=0, fill=0)
            c.drawImage(cover_crop(AI[name], tw, th, focus=0.35 if name != "Aseo y cafetería" else 0.5), x, y, tw, th)
            c.restoreState()
        else:
            c.setFillColor(TILE); c.roundRect(x, y, tw, th, 13, stroke=0, fill=1)
            area = (x + 12, y + 36, tw - 24, th - 48)
            if isinstance(files, list) and files:
                n = len(files); ws = [0.5, 0.5] if n == 2 else [0.31, 0.38, 0.31]
                xx = area[0]
                for j, f in enumerate(files):
                    sw = area[2] * ws[j]
                    fit_image(c, os.path.join(CUT, f), xx + 3, area[1], sw - 6, area[3] * (1.0 if (n == 3 and j == 1) or n == 2 else 0.86))
                    xx += sw
            else:
                c.setFillColor(HexColor("#D5DAE0")); c.circle(x + tw / 2, area[1] + area[3] / 2 + 2, 25, stroke=0, fill=1)
                icon(c, fn, x + tw / 2, area[1] + area[3] / 2 + 2, size=28, color=HexColor("#8E99A6"))
                if files != "icon":
                    spaced(c, x + tw / 2 - spaced_w(c, "FOTO PENDIENTE", "Mont-SemiBold", 5, 1.0) / 2, y + th - 14, "FOTO PENDIENTE", "Mont-SemiBold", 5, 1.0, HexColor("#8E99A6"))
        fw = c.stringWidth(name, "Mont-Bold", 7.8)
        c.setFillColor(WHITE); c.roundRect(x + 10, y + 10, fw + 20, 19, 9.5, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Mont-Bold", 7.8); c.drawString(x + 20, y + 16.2, name)
        lab = f"PÁG. {pg}"; lwid = spaced_w(c, lab, "Mont-SemiBold", 5.8, 1.1)
        if name in AI:
            c.setFillColor(WHITE); c.roundRect(x + tw - 14 - lwid - 10, y + 10, lwid + 22, 19, 9.5, stroke=0, fill=1)
        spaced(c, x + tw - 11 - lwid + 1.1 - (3 if name in AI else 0), y + 16.5, lab, "Mont-SemiBold", 5.8, 1.1, GRAYT)
    gbot = top - 4 * th - 3 * gap

    by = gbot - 78; bh = 56
    c.setFillColor(NAVY); c.roundRect(M, by, CW, bh, 14, stroke=0, fill=1)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 10.5); c.drawString(M + 20, by + bh - 23, "¿No ves lo que necesitas?")
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 8)
    c.drawString(M + 20, by + bh - 38, "Buscamos alternativas para productos fuera del portafolio.")
    bw = 168
    c.setFillColor(YELLOW); c.roundRect(W - M - bw - 14, by + 12, bw, 32, 16, stroke=0, fill=1)
    lab = "SOLICITA TU COTIZACIÓN"; wl = spaced_w(c, lab, "Mont-ExtraBold", 6.8, 1.0)
    spaced(c, W - M - bw - 14 + (bw - wl) / 2 + 0.5, by + 24.4, lab, "Mont-ExtraBold", 6.8, 1.0, NAVY)
    c.linkURL(WA, (W - M - bw - 14, by + 12, W - M - 14, by + 44), relative=0)

    c.setStrokeColor(LINE); c.line(M, 50, W - M, 50)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 5.8)
    c.drawString(M, 36, "Referencias y disponibilidad sujetas a confirmación en la cotización.")
    c.setFillColor(GREEN); c.setFont("Mont-Bold", 7); c.drawRightString(W - M - 14, 36, "WhatsApp 350 862 4021")
    c.linkURL(WA, (W - M - 104, 31, W - M - 14, 44), relative=0)
    c.setFillColor(INK); c.setFont("Mont-Bold", 7.4); c.drawRightString(W - M, 36, "2")
    c.showPage(); c.save()


if __name__ == "__main__":
    build3(os.path.join(HERE, "Pagina2_v3_vista_previa.pdf"))
