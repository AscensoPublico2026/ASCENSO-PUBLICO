import fitz, os, sys

base = os.path.dirname(__file__)
img_dir = os.path.join(base, "_img")
os.makedirs(img_dir, exist_ok=True)

# archivo -> lista de páginas (1-indexed) a renderizar. [] = todas
targets = {
    "6_Cédula _ciudadanía.pdf": [],
    "7_Libreta_Militar.pdf": [],
    "9_Certificados_Academicos.pdf": [],
    "10_Tarjeta_Profesional.pdf": [],
    "Diplomado Derecho Laboral.pdf": [],
    "certificado electoral.pdf": [],
    "DIPLOMADO CONSTRUCCIÓN DE PAZ Y DDHH.pdf": [],
    "DIPLOMADO EN POLÍTICAS PÚBLICAS.pdf": [],
    "13_Certificaciones laborales.pdf": [1,2,3,14,15,17,18,19,20,21,22,23],
}

for fname, pages in targets.items():
    path = os.path.join(base, fname)
    if not os.path.exists(path):
        print("NO EXISTE:", fname); continue
    doc = fitz.open(path)
    plist = pages if pages else list(range(1, len(doc)+1))
    slug = fname.replace(".pdf","").replace(" ","_").replace("(","").replace(")","")
    for pno in plist:
        page = doc[pno-1]
        # zoom hasta que quede <5MB, empezando alto
        for zoom in (3.0, 2.5, 2.0, 1.5, 1.2):
            pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
            out = os.path.join(img_dir, f"{slug}__p{pno}.png")
            pix.save(out)
            if os.path.getsize(out) < 5*1024*1024:
                break
        print(f"{out}  ({os.path.getsize(out)//1024} KB, zoom {zoom})")
    doc.close()
print("DONE")
