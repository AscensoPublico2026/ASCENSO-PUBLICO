import fitz, os
DOCS = os.path.join(os.path.dirname(__file__), 'documentos')
OUT = os.path.join(os.path.dirname(__file__), '_img')
os.makedirs(OUT, exist_ok=True)
f = [x for x in os.listdir(DOCS) if x.lower().endswith('.pdf')][0]
doc = fitz.open(os.path.join(DOCS, f))
# renderizar paginas escaneadas de diplomas: 7,8,9,10,11,12,13 (0-index 6..12)
for i in range(6, 13):
    pix = doc[i].get_pixmap(dpi=90)
    out = os.path.join(OUT, 'p'+str(i+1)+'.jpg')
    pix.save(out, jpg_quality=68)
    if os.path.getsize(out)/1024/1024 > 4.5:
        pix = doc[i].get_pixmap(dpi=65); pix.save(out, jpg_quality=55)
    print(out, round(os.path.getsize(out)/1024/1024,2),'MB')
