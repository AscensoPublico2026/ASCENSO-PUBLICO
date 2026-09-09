# -*- coding: utf-8 -*-
"""Consolida todos los manuales de funciones dispersos en expedientes/ dentro de
una biblioteca central referencias/manuales-funciones/, sin duplicar.
Normaliza el nombre a NNN-2026.pdf. Si el mismo codigo aparece en varios lados,
se queda con el de mayor tamano (suele ser el mas completo) y verifica por hash."""
import os, re, glob, hashlib, shutil

DEST = "referencias/manuales-funciones"
os.makedirs(DEST, exist_ok=True)

def md5(p):
    h = hashlib.md5()
    with open(p,"rb") as f:
        for c in iter(lambda: f.read(8192), b""): h.update(c)
    return h.hexdigest()

def normaliza(fname):
    # extrae el numero de convocatoria del nombre; admite "100", "100-2026", "01-2026"
    base = os.path.basename(fname).replace(".pdf","")
    m = re.match(r"^(\d{1,3})", base.strip())
    if not m: return None
    num = m.group(1).zfill(2)  # 1 -> 01
    return f"{num}-2026.pdf"

fuentes = sorted(glob.glob("referencias/expedientes/*/manuales-vacantes/*.pdf"))
registro = {}  # codigo -> (ruta_origen, tamano)
for f in fuentes:
    code = normaliza(f)
    if not code:
        print("  ??? no reconozco codigo en:", f); continue
    size = os.path.getsize(f)
    if code not in registro or size > registro[code][1]:
        registro[code] = (f, size)

copiados, ya = 0, 0
for code, (src, size) in sorted(registro.items()):
    dst = os.path.join(DEST, code)
    if os.path.exists(dst) and md5(dst) == md5(src):
        ya += 1; continue
    shutil.copy2(src, dst)
    copiados += 1
    print(f"  + {code}  (desde {src.split('/')[2]}, {size//1024} KB)")

print(f"\nTOTAL manuales unicos en biblioteca: {len(registro)}")
print(f"Copiados/actualizados: {copiados} | Ya estaban iguales: {ya}")
print("\nCodigos en biblioteca:", ", ".join(sorted(registro.keys())))
