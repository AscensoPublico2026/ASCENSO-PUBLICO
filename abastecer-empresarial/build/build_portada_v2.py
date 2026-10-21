# Portada v2 (concepto "índice por familias") - Abastecer Empresarial S.A.S.
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "fonts")
for n in ["Regular", "Medium", "SemiBold", "Bold", "ExtraBold"]:
    pdfmetrics.registerFont(TTFont(f"Mont-{n}", os.path.join(FONTS, f"Montserrat-{n}.ttf")))

NAVY, NAVY2 = HexColor("#0D1B2A"), HexColor("#12263A")
PANEL, PANEL_LINE = HexColor("#15293D"), HexColor("#25405A")
TILE_LINE = HexColor("#2F4B66")
GREEN, YELLOW = HexColor("#16823C"), HexColor("#F2B705")
WHITE, MUTED, MUTED2 = HexColor("#FFFFFF"), HexColor("#B8C2CC"), HexColor("#8497A9")
W, H = 595.28, 841.89
M = 36
CW = W - 2 * M
WA = "https://wa.me/573508624021"
WEB = "https://www.abastecerempresarial.com/"


# ---------- utilidades ----------
def spaced(c, x, y, text, font, size, space, color):
    t = c.beginText(x, y); t.setFont(font, size); t.setCharSpace(space); t.setFillColor(color)
    t.textOut(text); t.setCharSpace(0); c.drawText(t)

def spaced_w(c, text, font, size, space):
    return c.stringWidth(text, font, size) + space * len(text)

def stripe(c, x, y, h=8):
    for dx, col in ((0, GREEN), (7, YELLOW)):
        p = c.beginPath(); p.moveTo(x + dx + 2.5, y); p.lineTo(x + dx + 8, y); p.lineTo(x + dx + 5.5, y + h); p.lineTo(x + dx, y + h); p.close()
        c.setFillColor(col); c.drawPath(p, stroke=0, fill=1)

def poly(c, pts, close=True):
    p = c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    if close: p.close()
    c.drawPath(p, stroke=1, fill=0)


# ---------- íconos de línea (rejilla 24x24) ----------
def ic_dotacion(c):
    poly(c, [(8, 21), (3, 17), (5.5, 12.5), (8, 14), (8, 3), (16, 3), (16, 14), (18.5, 12.5), (21, 17), (16, 21)])
    poly(c, [(8, 21), (12, 17.5), (16, 21)], close=False)

def ic_epp(c):
    c.arc(5, 3, 19, 17, 0, 180)
    c.roundRect(2, 7, 20, 3.2, 1.3, stroke=1, fill=0)
    poly(c, [(12, 17), (12, 10.2)], close=False)

def ic_calzado(c):
    poly(c, [(7, 21), (13, 21), (13, 14), (20, 11.5), (21.5, 6.5), (6, 6.5)])
    poly(c, [(4, 4), (22, 4)], close=False)

def ic_alturas(c):
    pth = c.beginPath(); pth.moveTo(6.5, 21); pth.lineTo(6.5, 3); pth.lineTo(12.5, 3)
    pth.curveTo(21.5, 3, 21.5, 21, 12.5, 21); pth.close(); c.drawPath(pth, stroke=1, fill=0)
    poly(c, [(6.5, 15), (10.5, 15)], close=False)
    poly(c, [(6.5, 9), (10.5, 9)], close=False)

def ic_senal(c):
    poly(c, [(12, 21), (19, 4.5), (5, 4.5)])
    poly(c, [(9.1, 14), (14.9, 14)], close=False)
    poly(c, [(7.2, 9.2), (16.8, 9.2)], close=False)
    poly(c, [(3, 4.5), (21, 4.5)], close=False)

def ic_emerg(c):
    c.roundRect(6.5, 3, 9.5, 13, 3, stroke=1, fill=0)
    c.rect(9.5, 16, 3.8, 2.6, stroke=1, fill=0)
    poly(c, [(9.5, 19.5), (9.5, 20.6), (16.5, 20.6)], close=False)
    p = c.beginPath(); p.moveTo(13.5, 17.2); p.curveTo(19, 17.2, 20.5, 14, 19.5, 9.5); c.drawPath(p, stroke=1, fill=0)

def ic_ergo(c):
    c.circle(12, 20.4, 1.9, stroke=1, fill=0)
    for (x, y, w) in [(8.6, 14.6, 6.8), (7.6, 9.4, 7.4), (8.4, 4.2, 7.0)]:
        c.roundRect(x, y, w, 3.2, 1.4, stroke=1, fill=0)

def ic_tec(c):
    c.roundRect(5, 9, 14, 9.5, 1.5, stroke=1, fill=0)
    c.roundRect(2, 5.5, 20, 3.5, 1.2, stroke=1, fill=0)

def ic_mob(c):
    c.roundRect(7, 14.5, 10, 6.5, 2, stroke=1, fill=0)
    c.roundRect(5.5, 10, 13, 3, 1.2, stroke=1, fill=0)
    poly(c, [(12, 10), (12, 6)], close=False)
    poly(c, [(6, 3.5), (12, 6), (18, 3.5)], close=False)

def ic_id(c):
    c.roundRect(5, 3, 14, 18, 2, stroke=1, fill=0)
    poly(c, [(10, 18), (14, 18)], close=False)
    c.circle(12, 13.2, 2.3, stroke=1, fill=0)
    c.arc(8, 5.8, 16, 11.8, 0, 180)

def ic_aseo(c):
    poly(c, [(4.5, 17), (6.5, 5), (14.5, 5), (16.5, 17)])
    c.arc(13.2, 8, 20.5, 15.5, -90, 180)
    p = c.beginPath(); p.moveTo(8, 20); p.curveTo(6.8, 21, 9.2, 22, 8, 23.2); c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath(); p.moveTo(12.5, 20); p.curveTo(11.3, 21, 13.7, 22, 12.5, 23.2); c.drawPath(p, stroke=1, fill=0)

def ic_estan(c):
    poly(c, [(3, 3), (3, 21)], close=False)
    poly(c, [(21, 3), (21, 21)], close=False)
    poly(c, [(3, 3), (21, 3)], close=False)
    poly(c, [(3, 10), (21, 10)], close=False)
    poly(c, [(3, 17), (21, 17)], close=False)
    c.rect(6, 3, 5, 5.5, stroke=1, fill=0)
    c.rect(13, 10, 5, 5, stroke=1, fill=0)
    c.rect(6, 17, 6, 3.6, stroke=1, fill=0)

def ic_alim(c):
    poly(c, [(12, 21), (20, 16.5), (20, 7.5), (12, 3), (4, 7.5), (4, 16.5)])
    poly(c, [(4, 16.5), (12, 12), (20, 16.5)], close=False)
    poly(c, [(12, 12), (12, 3)], close=False)

def ic_promo(c):
    c.rect(4, 3, 16, 10, stroke=1, fill=0)
    c.rect(3, 13, 18, 4, stroke=1, fill=0)
    poly(c, [(12, 3), (12, 17)], close=False)
    p = c.beginPath(); p.moveTo(12, 17); p.curveTo(8, 17, 7, 21.5, 10, 21.5); p.curveTo(12, 21.5, 12, 19, 12, 17); c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath(); p.moveTo(12, 17); p.curveTo(16, 17, 17, 21.5, 14, 21.5); p.curveTo(12, 21.5, 12, 19, 12, 17); c.drawPath(p, stroke=1, fill=0)

def ic_compras(c):
    c.circle(10.5, 13.5, 6.5, stroke=1, fill=0)
    poly(c, [(15.4, 8.6), (21, 3)], close=False)
    poly(c, [(10.5, 10.5), (10.5, 16.5)], close=False)
    poly(c, [(7.5, 13.5), (13.5, 13.5)], close=False)

def ic_mas(c):
    poly(c, [(12, 5), (12, 19)], close=False)
    poly(c, [(5, 12), (19, 12)], close=False)


def icon(c, fn, cx, cy, size=15, color=YELLOW, lw=1.7):
    s = size / 24.0
    c.saveState()
    c.translate(cx - size / 2, cy - size / 2); c.scale(s, s)
    c.setStrokeColor(color); c.setLineWidth(lw); c.setLineCap(1); c.setLineJoin(1)
    fn(c)
    c.restoreState()

def tile(c, x, y, size, fn, color=YELLOW, fill=NAVY):
    c.setFillColor(fill); c.setStrokeColor(TILE_LINE); c.setLineWidth(0.8)
    c.roundRect(x, y, size, size, 7, stroke=1, fill=1)
    icon(c, fn, x + size / 2, y + size / 2, size=size * 0.64, color=color)


# ---------- paneles ----------
def panel(c, x, y, w, h, r=13):
    c.setFillColor(PANEL); c.setStrokeColor(PANEL_LINE); c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, r, stroke=1, fill=1)

def header(c, x, ytop, num, title, accent=False):
    spaced(c, x, ytop - 8, num, "Mont-ExtraBold", 7, 1.6, YELLOW)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 11.5 if not accent else 13)
    c.drawString(x + 22, ytop - 9, title) if False else None
    c.drawString(x, ytop - 24, title)


def build(out):
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Portafolio comercial - Abastecer Empresarial S.A.S.")
    c.setAuthor("Abastecer Empresarial S.A.S."); c.setSubject("Un solo aliado para múltiples necesidades de suministro")

    # fondo
    c.setFillColor(NAVY); c.rect(0, 0, W, H, stroke=0, fill=1)
    p = c.beginPath(); p.moveTo(0, H); p.lineTo(W, H); p.lineTo(W, H - 292); p.lineTo(0, H - 352); p.close()
    c.setFillColor(NAVY2); c.drawPath(p, stroke=0, fill=1)

    # cabecera
    c.setFillColor(WHITE); c.roundRect(M, H - 98, 176, 48, 10, stroke=0, fill=1)
    lw = 160; lh = lw * 344 / 1400
    c.drawImage(os.path.join(HERE, "logo_h.png"), M + 8, H - 98 + (48 - lh) / 2, lw, lh, mask="auto")
    t = "PORTAFOLIO COMERCIAL"
    spaced(c, W - M - spaced_w(c, t, "Mont-SemiBold", 6.4, 2.2) + 2.2, H - 68, t, "Mont-SemiBold", 6.4, 2.2, WHITE)

    # titular
    stripe(c, M, H - 160); spaced(c, M + 20, H - 158, "ABASTECIMIENTO EMPRESARIAL", "Mont-SemiBold", 6.4, 1.8, YELLOW)
    fs = 31
    c.setFont("Mont-ExtraBold", fs)
    c.setFillColor(WHITE); c.drawString(M, H - 198, "Un solo aliado para")
    c.setFillColor(YELLOW); c.drawString(M, H - 234, "múltiples necesidades")
    c.setFillColor(WHITE); c.drawString(M, H - 270, "de suministro")
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 9.6)
    c.drawString(M, H - 303, "Dotación, protección personal, tecnología, mobiliario,")
    c.drawString(M, H - 318, "aseo y mucho más, en una sola cotización.")

    # ---- rejilla de familias ----
    top = H - 372
    total_h = 316
    gap = 11
    lw_ = 250
    rx = M + lw_ + gap; rw = CW - lw_ - gap

    # panel 1 (izquierda, alto)
    panel(c, M, top - total_h, lw_, total_h)
    # barra de acento
    c.setFillColor(YELLOW); c.roundRect(M + 18, top - 19, 22, 3, 1.5, stroke=0, fill=1)
    spaced(c, M + 18, top - 36, "01", "Mont-ExtraBold", 7, 1.6, YELLOW)
    c.setFillColor(WHITE); c.setFont("Mont-Bold", 13); c.drawString(M + 18, top - 53, "Seguridad y dotación")
    spaced(c, M + 18, top - 66, "NUESTRA ESPECIALIZACIÓN", "Mont-SemiBold", 5.8, 1.4, MUTED)
    items1 = [
        (ic_dotacion, "Dotación", "Uniformes y prendas de trabajo"),
        (ic_epp, "EPP", "Cabeza, rostro, oídos, manos y pies"),
        (ic_calzado, "Calzado", "Botas y calzado laboral"),
        (ic_alturas, "Alturas", "Arneses, eslingas y líneas de vida"),
        (ic_senal, "Señalización", "Señales, conos, cintas y chalecos"),
        (ic_emerg, "Emergencias", "Extintores, botiquines y camillas"),
        (ic_ergo, "Ergonomía", "Fajas, rodilleras y accesorios"),
    ]
    y0 = top - 76; pitch = 33.2; ts = 27
    for i, (fn, name, sub) in enumerate(items1):
        yy = y0 - i * pitch - ts
        tile(c, M + 18, yy, ts, fn)
        c.setFillColor(WHITE); c.setFont("Mont-SemiBold", 9.2); c.drawString(M + 18 + ts + 11, yy + 14.2, name)
        c.setFillColor(MUTED2); c.setFont("Mont-Medium", 6.7); c.drawString(M + 18 + ts + 11, yy + 5.2, sub)

    # paneles derecha
    ph = (total_h - 2 * gap) / 3
    fams = [
        ("02", "Oficina y tecnología", [(ic_tec, "Tecnología"), (ic_mob, "Mobiliario"), (ic_id, "Identificación")]),
        ("03", "Instalaciones y operación", [(ic_aseo, "Aseo y cafetería"), (ic_estan, "Estanterías"), (ic_alim, "Alimentos y otros")]),
        ("04", "Corporativo y especiales", [(ic_promo, "Promocionales"), (ic_compras, "Compras especiales"), (ic_mas, "Y más…")]),
    ]
    for k, (num, title, its) in enumerate(fams):
        py = top - (k + 1) * ph - k * gap
        panel(c, rx, py, rw, ph)
        spaced(c, rx + 16, py + ph - 21, num, "Mont-ExtraBold", 7, 1.6, YELLOW)
        c.setFillColor(WHITE); c.setFont("Mont-Bold", 10.8); c.drawString(rx + 34, py + ph - 22, title)
        offs = [0, 77, 157]
        for j, (fn, name) in enumerate(its):
            cx0 = rx + 16 + offs[j]
            tile(c, cx0, py + 29, 27, fn)
            c.setFillColor(WHITE); c.setFont("Mont-SemiBold", 6.9)
            c.drawString(cx0, py + 14.5, name)

    # ---- bloque Compras especiales ----
    ty = top - total_h - 26
    c.setFillColor(YELLOW); c.setFont("Mont-Bold", 9.4); c.drawString(M, ty, "¿No lo ves en la lista?")
    c.setFillColor(MUTED); c.setFont("Mont-Medium", 8.6)
    c.drawString(M + c.stringWidth("¿No lo ves en la lista?  ", "Mont-Bold", 9.4), ty, "Envíanos una descripción, foto, referencia o enlace y buscamos alternativas.")

    # esquina inferior
    p = c.beginPath(); p.moveTo(W - 205, 0); p.lineTo(W - 125, 74); p.lineTo(W, 74); p.lineTo(W, 0); p.close()
    c.setFillColor(GREEN); c.drawPath(p, stroke=0, fill=1)
    p = c.beginPath(); p.moveTo(W - 212, 0); p.lineTo(W - 132, 74); p.lineTo(W - 104, 74); p.lineTo(W - 184, 0); p.close()
    c.setFillColor(YELLOW); c.drawPath(p, stroke=0, fill=1)

    # CTA
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

if __name__ == "__main__":
    build(os.path.join(HERE, "Portada_v2.pdf")); print("ok")
