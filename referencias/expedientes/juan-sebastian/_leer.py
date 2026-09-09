import pdfplumber, os, hashlib, glob

base = os.path.dirname(__file__)
pdfs = sorted(glob.glob(os.path.join(base, "*.pdf")))

print("=== HASHES (para detectar duplicados) ===")
h = {}
for p in pdfs:
    d = hashlib.md5(open(p,'rb').read()).hexdigest()
    h.setdefault(d, []).append(os.path.basename(p))
for d, files in h.items():
    if len(files) > 1:
        print("  DUPLICADO:", files)
print()

for p in pdfs:
    name = os.path.basename(p)
    print("\n" + "="*90)
    print("ARCHIVO:", name)
    print("="*90)
    try:
        with pdfplumber.open(p) as pdf:
            print("Páginas:", len(pdf.pages))
            for i, pg in enumerate(pdf.pages):
                txt = pg.extract_text() or ""
                txt = txt.strip()
                nchars = len(txt)
                nimg = len(pg.images)
                print(f"\n--- pág {i+1}/{len(pdf.pages)} | chars={nchars} | imgs={nimg} ---")
                if nchars == 0:
                    print("   [SIN TEXTO EXTRAÍBLE -> posiblemente escaneada, renderizar a imagen]")
                else:
                    print(txt[:2600])
    except Exception as e:
        print("ERROR:", e)
