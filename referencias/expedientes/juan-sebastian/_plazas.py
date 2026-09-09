# -*- coding: utf-8 -*-
import pdfplumber, os, glob, re, unicodedata

base = os.path.join(os.path.dirname(__file__), "manuales-vacantes")
pdfs = sorted(glob.glob(os.path.join(base, "*.pdf")))

def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii","ignore").decode()
    return s.lower()

# ciudades y departamentos de interes del aspirante
INTERES = ["pasto","ipiales","popayan","mocoa","puerto asis","cartagena","tumaco",
           "narino","cauca","putumayo","caldas","antioquia","bolivar","valle de aburra"]

# patron: Nombre (n)
patron = re.compile(r"([A-Za-zÁÉÍÓÚÑáéíóúñ\.\- ]+?)\s*\((\d+)\)")

for p in pdfs:
    name = os.path.basename(p)
    with pdfplumber.open(p) as pdf:
        full = "\n".join((pg.extract_text() or "") for pg in pdf.pages)
    # identificacion
    m_den = re.search(r"Denominaci[oó]n del empleo:.*?\n?\s*([A-Za-z ]+?)\s+(\d[A-Z]{2}\s*-\s*\d+)", full)
    m_sal = re.search(r"Asignaci[oó]n b[aá]sica:.*?\$?([\d\.\,]+)", full)
    m_car = re.search(r"cargos:\s*.*?(\d+)\s*\n", full, re.S)
    print("\n" + "="*80)
    print("MANUAL", name)
    # total de cargos: buscar numero suelto grande cerca de "cargos:"
    m_tot = re.search(r"cargos:\s*\n?\s*(\d+)", full) or re.search(r"\n\s*(\d{2,4})\s*\n", full)
    # buscar plazas por ciudad/depto de interes
    print("  Plazas por sede DE INTERÉS (nombre: n):")
    encontrados = {}
    for mm in patron.finditer(full):
        lugar = mm.group(1).strip()
        n = int(mm.group(2))
        ln = norm(lugar)
        for it in INTERES:
            # match por palabra final del lugar
            if ln.endswith(it) or ln == it or (" "+it) in (" "+ln):
                encontrados.setdefault(it, []).append((lugar, n))
    if not encontrados:
        print("    (ninguna sede de interés listada explícitamente)")
    for it in INTERES:
        if it in encontrados:
            for lugar,n in encontrados[it]:
                print(f"    - {lugar}: {n}")
