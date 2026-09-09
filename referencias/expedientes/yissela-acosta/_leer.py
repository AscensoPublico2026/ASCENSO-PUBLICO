import pdfplumber, os, sys
DOCS = os.path.join(os.path.dirname(__file__), 'documentos')
target = sys.argv[1] if len(sys.argv) > 1 else ''
files = sorted([f for f in os.listdir(DOCS) if f.lower().endswith('.pdf') and target.lower() in f.lower()])
for f in files:
    try:
        with pdfplumber.open(os.path.join(DOCS, f)) as pdf:
            npages=len(pdf.pages)
            for i,p in enumerate(pdf.pages):
                t=(p.extract_text() or '').strip()
                print(f'\n===== {f} · pág {i+1}/{npages} ({len(t)} chars) =====')
                print(t if t else '(ESCANEADO - sin texto)')
    except Exception as e:
        print('ERROR', f, e)
