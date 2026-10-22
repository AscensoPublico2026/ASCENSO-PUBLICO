# Línea de canecas, contenedores y almacenamiento (vista previa de una página).
# Fotos reales: puntos ecológicos (catálogo Protecto); caneca de pedal, tambor y canastillas (fotos enviadas por Abastecer).
# Las funciones ill_* quedan como respaldo (ilustraciones referenciales) por si falta alguna foto.
import os, sys
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_epp_lineas import *
from reportlab.lib.colors import HexColor, Color

G1, G2 = HexColor("#16823C"), HexColor("#0F6A30")
GR1, GR2 = HexColor("#9AA5B1"), HexColor("#7D8894")
BL1, BL2 = HexColor("#1F5BB5"), HexColor("#17468C")
YL1 = HexColor("#F2B705")

TITLE = "Línea de canecas, contenedores y almacenamiento"
DESC = "Puntos ecológicos, canecas, tambores y canastillas para separar residuos y organizar tus espacios."
LISTA = ["Puntos ecológicos de 2, 3 y 4 canecas", "Canecas de pedal", "Canecas con tapa vaivén", "Canecas sin tapa y papeleras",
         "Tambores plásticos con tapa", "Baldes plásticos", "Canastillas caladas y cerradas", "Cajas y contenedores organizadores"]


def shadow(c, cx, y, w):
    c.saveState(); c.setFillColor(INK)
    for k in range(6):
        c.setFillAlpha(0.03); c.ellipse(cx - w / 2 - k, y - 4 - k * 0.6, cx + w / 2 + k, y + 4 + k * 0.6, stroke=0, fill=1)
    c.restoreState()


def poly_fill(c, pts, col):
    p = c.beginPath(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    p.close(); c.setFillColor(col); c.drawPath(p, stroke=0, fill=1)


def ill_caneca(c, cx, by, s):
    """Caneca con tapa vaivén."""
    shadow(c, cx, by, s * 0.75)
    w0, w1, h = s * 0.62, s * 0.72, s * 0.78
    poly_fill(c, [(cx - w0 / 2, by), (cx + w0 / 2, by), (cx + w1 / 2, by + h), (cx - w1 / 2, by + h)], G1)
    poly_fill(c, [(cx + w0 / 2 - s * 0.1, by), (cx + w0 / 2, by), (cx + w1 / 2, by + h), (cx + w1 / 2 - s * 0.1, by + h)], G2)
    c.setFillColor(G2); c.roundRect(cx - w1 / 2 - s * 0.03, by + h - s * 0.02, w1 + s * 0.06, s * 0.07, s * 0.03, stroke=0, fill=1)
    p = c.beginPath(); p.moveTo(cx - w1 / 2, by + h + s * 0.05)
    p.curveTo(cx - w1 / 2, by + h + s * 0.33, cx + w1 / 2, by + h + s * 0.33, cx + w1 / 2, by + h + s * 0.05); p.close()
    c.setFillColor(G1); c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(HexColor("#0B4F24")); c.roundRect(cx - s * 0.16, by + h + s * 0.1, s * 0.32, s * 0.07, s * 0.03, stroke=0, fill=1)
    # etiqueta de reciclaje
    c.setFillColor(WHITE); c.roundRect(cx - s * 0.17, by + h * 0.32, s * 0.3, s * 0.24, s * 0.03, stroke=0, fill=1)
    c.setStrokeColor(G1); c.setLineWidth(s * 0.025)
    r = s * 0.06; ccx, ccy = cx - s * 0.02, by + h * 0.32 + s * 0.12
    for a in (90, 210, 330):
        c.arc(ccx - r, ccy - r, ccx + r, ccy + r, a, 85)


def ill_balde(c, cx, by, s):
    """Balde plástico con asa."""
    shadow(c, cx, by, s * 0.7)
    w0, w1, h = s * 0.56, s * 0.76, s * 0.62
    c.setStrokeColor(GR2); c.setLineWidth(s * 0.035)
    c.arc(cx - w1 / 2 + s * 0.02, by + h - s * 0.32, cx + w1 / 2 - s * 0.02, by + h + s * 0.42, 15, 150)
    poly_fill(c, [(cx - w0 / 2, by), (cx + w0 / 2, by), (cx + w1 / 2, by + h), (cx - w1 / 2, by + h)], BL1)
    poly_fill(c, [(cx + w0 / 2 - s * 0.09, by), (cx + w0 / 2, by), (cx + w1 / 2, by + h), (cx + w1 / 2 - s * 0.09, by + h)], BL2)
    c.setFillColor(BL2); c.roundRect(cx - w1 / 2 - s * 0.03, by + h - s * 0.03, w1 + s * 0.06, s * 0.08, s * 0.035, stroke=0, fill=1)
    for k in (0.22, 0.42):
        c.setFillColor(Color(1, 1, 1, alpha=0.18)); c.rect(cx - (w0 + (w1 - w0) * k) / 2 + s * 0.02, by + h * k, (w0 + (w1 - w0) * k) - s * 0.04, s * 0.025, stroke=0, fill=1)
    c.setFillColor(GR1); c.circle(cx - w1 / 2 + s * 0.02, by + h - s * 0.06, s * 0.03, stroke=0, fill=1)
    c.circle(cx + w1 / 2 - s * 0.02, by + h - s * 0.06, s * 0.03, stroke=0, fill=1)


def ill_canastilla(c, cx, by, s):
    """Canastilla plástica calada en perspectiva simple."""
    shadow(c, cx, by, s * 0.95)
    w, h, d = s * 0.92, s * 0.48, s * 0.14
    x0 = cx - w / 2
    poly_fill(c, [(x0 + d, by + h + d * 0.7), (x0 + w + d * 0.4, by + h + d * 0.7), (x0 + w, by + h), (x0, by + h)], HexColor("#0B4F24"))
    poly_fill(c, [(x0 + w, by), (x0 + w + d * 0.4, by + d * 0.7), (x0 + w + d * 0.4, by + h + d * 0.7), (x0 + w, by + h)], G2)
    c.setFillColor(G1); c.roundRect(x0, by, w, h, s * 0.03, stroke=0, fill=1)
    # calado
    c.setFillColor(HexColor("#0B4F24"))
    cols, rows = 7, 3; mx, my = s * 0.06, s * 0.1
    cw = (w - 2 * mx) / cols; rh = (h - my - s * 0.05) / rows
    for i in range(cols):
        for j in range(rows):
            c.roundRect(x0 + mx + i * cw + cw * 0.18, by + s * 0.05 + j * rh + rh * 0.2, cw * 0.64, rh * 0.6, s * 0.012, stroke=0, fill=1)
    # asas
    c.setFillColor(HexColor("#0B4F24"))
    c.roundRect(x0 + s * 0.06, by + h - s * 0.085, s * 0.16, s * 0.05, s * 0.02, stroke=0, fill=1)
    c.roundRect(x0 + w - s * 0.22, by + h - s * 0.085, s * 0.16, s * 0.05, s * 0.02, stroke=0, fill=1)


def tile_ill(c, x, y, w, h, fn, name):
    c.setFillColor(TILE); c.roundRect(x, y, w, h, 13, stroke=0, fill=1)
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 5.4); c.drawRightString(x + w - 10, y + h - 13, "Ilustración referencial")
    s = min(w * 0.62, h - 62)
    fn(c, x + w / 2, y + 44, s)
    fw = c.stringWidth(name, "Mont-Bold", 7.4)
    c.setFillColor(WHITE); c.roundRect(x + 10, y + 10, fw + 20, 19, 9.5, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont("Mont-Bold", 7.4); c.drawString(x + 20, y + 16.4, name)


def build(out, num=9):
    c = canvas.Canvas(out, pagesize=(W, H)); c.setTitle("Portafolio - Abastecer Empresarial - Canecas, contenedores y almacenamiento")
    page_frame(c, num)
    stripe(c, M, H - 94, h=7); spaced(c, M + 20, H - 93, "LÍNEA DE SUMINISTRO", "Mont-SemiBold", 6.6, 1.8, GREEN)
    c.setFillColor(INK); c.setFont("Mont-ExtraBold", 21); c.drawString(M, H - 122, "Canecas, contenedores y almacenamiento")
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 9); c.drawString(M, H - 139, DESC)
    gap = 10; tw = (CW - 2 * gap) / 3
    # puntos ecológicos (fotos reales)
    y = H - 166
    spaced(c, M, y, "PUNTOS ECOLÓGICOS", "Mont-SemiBold", 6.2, 1.6, GREEN)
    th = 236; ty = y - 10 - th
    for k, (f, n) in enumerate([("ase_pe_2.png", "Punto ecológico de 2 canecas"), ("ase_pe_3.png", "Punto ecológico de 3 canecas"), ("ase_pe_4.png", "Punto ecológico de 4 canecas")]):
        tile(c, M + k * (tw + gap), ty, tw, th, f, n, None)
    # canecas, baldes y canastillas (ilustraciones)
    y = ty - 24
    spaced(c, M, y, "CANECAS, TAMBORES Y CANASTILLAS", "Mont-SemiBold", 6.2, 1.6, GREEN)
    th2 = 196; ty2 = y - 10 - th2
    for k, (f, n) in enumerate([("ase_caneca_pedal.png", "Caneca de pedal"), ("ase_tambor.png", "Tambor plástico con tapa"), ("ase_canastillas.png", "Canastillas plásticas")]):
        tile(c, M + k * (tw + gap), ty2, tw, th2, f, n, None)
    # listado + llamado (igual que EPP)
    bh = 84; by = ty2 - 12 - bh; lw_ = tw * 2 + gap
    c.setStrokeColor(LINE); c.setLineWidth(0.8); c.setFillColor(WHITE); c.roundRect(M, by, lw_, bh, 12, stroke=1, fill=1)
    spaced(c, M + 14, by + bh - 17, "PRODUCTOS PRINCIPALES", "Mont-SemiBold", 6, 1.6, GREEN)
    rows = 4; colw = (lw_ - 28) / 2
    for i, it in enumerate(LISTA):
        col, row = divmod(i, rows); xx = M + 14 + col * colw * 1.12; yy = by + bh - 32 - row * 13.2
        c.setFillColor(GREEN); c.circle(xx + 2.5, yy + 2.6, 2.1, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Mont-Medium", 7.6); c.drawString(xx + 9, yy, it)
    cx = M + lw_ + gap
    c.setFillColor(SOFT); c.roundRect(cx, by, tw, bh, 12, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont("Mont-Bold", 8.2); c.drawString(cx + 12, by + bh - 19, "¿Necesitas algo específico")
    c.drawString(cx + 12, by + bh - 29.5, "de esta línea?")
    c.setFillColor(GRAYT); c.setFont("Mont-Medium", 6.5); c.drawString(cx + 12, by + bh - 42, "Consúltanos tamaños, colores y capacidades.")
    bw = tw - 24; bx = cx + 12; byb = by + 10
    c.setFillColor(GREEN); c.roundRect(bx, byb, bw, 21, 10.5, stroke=0, fill=1)
    t = "PREGÚNTANOS POR WHATSAPP"; wl = spaced_w(c, t, "Mont-ExtraBold", 6, 0.8)
    spaced(c, bx + (bw - wl) / 2 + 0.4, byb + 7.6, t, "Mont-ExtraBold", 6, 0.8, WHITE)
    c.linkURL(WA + "?text=" + quote("Hola, quiero cotizar canecas, puntos ecológicos o contenedores."), (bx, byb, bx + bw, byb + 21), relative=0)
    c.showPage(); c.save()


if __name__ == "__main__":
    out = os.path.join(HERE, "..", "salidas", "Canecas_contenedores_vista_previa.pdf")
    build(out); print(out)
