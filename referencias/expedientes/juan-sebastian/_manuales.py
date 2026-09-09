import pdfplumber, os, glob

base = os.path.join(os.path.dirname(__file__), "manuales-vacantes")
pdfs = sorted(glob.glob(os.path.join(base, "*.pdf")))

for p in pdfs:
    name = os.path.basename(p)
    print("\n" + "#"*95)
    print("MANUAL:", name)
    print("#"*95)
    with pdfplumber.open(p) as pdf:
        print("Páginas:", len(pdf.pages))
        for i, pg in enumerate(pdf.pages):
            txt = (pg.extract_text() or "").strip()
            print(f"\n----- pág {i+1}/{len(pdf.pages)} | chars={len(txt)} -----")
            print(txt if txt else "[SIN TEXTO -> renderizar]")
