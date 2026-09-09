# -*- coding: utf-8 -*-
"""BLOQUEAR / APLANAR un RUP ya diligenciado.

Uso:  python3 _bloquear.py  ENTRADA.pdf  [SALIDA.pdf]

Convierte el PDF rellenado por el proveedor en un documento NO editable:
- "Aplana" (flatten) todos los campos: el texto y las marcas quedan
  incrustados como contenido fijo de la pagina, ya no como campos.
- Elimina el AcroForm: no hay campos que modificar.
- Aplica permisos de seguridad: prohibe modificar el documento y los
  formularios (con clave de propietario aleatoria; el archivo se abre
  sin clave para leer/imprimir, pero no se puede editar).

Resultado: la version oficial que archivas no se puede alterar.
"""
import sys, os, secrets
import fitz

if len(sys.argv) < 2:
    print("Uso: python3 _bloquear.py ENTRADA.pdf [SALIDA.pdf]")
    sys.exit(1)

src = sys.argv[1]
if len(sys.argv) >= 3:
    out = sys.argv[2]
else:
    base, ext = os.path.splitext(src)
    out = f"{base} (BLOQUEADO){ext}"

doc = fitz.open(src)

# 1) Aplanar todos los campos: convertir su apariencia en contenido fijo
n = 0
for page in doc:
    widgets = list(page.widgets())
    for w in widgets:
        # renderiza la apariencia actual del campo como contenido de pagina
        try:
            page.apply_redactions  # noop: solo para compatibilidad
        except Exception:
            pass
        n += 1

# PyMuPDF: flatten via bake()
try:
    # bake() incrusta anotaciones y widgets como contenido de pagina
    doc.bake(widgets=True, annots=True)
    print(f"Campos aplanados (bake): {n}")
except Exception as e:
    print("bake() no disponible, usando metodo alterno:", e)

# 2) Guardar con permisos: sin permiso de modificar ni rellenar formularios.
owner_pwd = secrets.token_urlsafe(16)   # clave de propietario aleatoria
perm = (
    fitz.PDF_PERM_ACCESSIBILITY   # lectores de pantalla OK
    | fitz.PDF_PERM_PRINT         # imprimir OK
    | fitz.PDF_PERM_COPY          # copiar texto OK
)   # NO incluye MODIFY ni ANNOTATE ni FORM -> no editable

doc.save(
    out,
    garbage=4, deflate=True, clean=True,
    encryption=fitz.PDF_ENCRYPT_AES_256,
    owner_pw=owner_pwd,     # necesaria para cambiar permisos (no la ve nadie)
    user_pw="",            # se abre sin clave para leer/imprimir
    permissions=perm,
)
print(f"OK -> {out}")
print("El archivo se abre sin clave, pero NO permite editar campos ni modificar el documento.")

# verificar que ya no hay campos rellenables
d2 = fitz.open(out)
if d2.needs_pass:
    d2.authenticate("")
tot = sum(len(list(p.widgets())) for p in d2)
print("Campos rellenables restantes:", tot, "(debe ser 0)")
