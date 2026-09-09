import pdfplumber, os, sys
DOCS = os.path.join(os.path.dirname(__file__), 'documentos')
files = sorted([f for f in os.listdir(DOCS) if f.lower().endswith('.pdf')])
mode = sys.argv[1] if len(sys.argv)>1 else 'map'
NL = chr(10)
for f in files:
    path = os.path.join(DOCS, f)
    with pdfplumber.open(path) as pdf:
        n=len(pdf.pages)
        if mode=='map':
            print('ARCHIVO:', f, '| paginas:', n)
            for i,p in enumerate(pdf.pages):
                t=(p.extract_text() or '').strip()
                est=str(len(t))+'c' if t else 'ESCANEADO'
                first = t.split(NL)[0][:55] if t else ''
                print('  p'+str(i+1)+': '+est+' | '+first)
        else:
            lo,hi=(int(x) for x in mode.split('-'))
            for i in range(lo-1,min(hi,n)):
                t=(pdf.pages[i].extract_text() or '')
                print(NL+'===== p'+str(i+1)+' ====='); print(t)
