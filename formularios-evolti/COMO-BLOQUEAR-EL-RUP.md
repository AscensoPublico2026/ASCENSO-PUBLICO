# RUP EVOLTI — Guía rápida

## Archivos
- **RUP-EVOLTI.pdf** — Formulario rellenable que se envía a los proveedores.
  - Campos de texto y casillas editables (fondo azul clarito).
  - **Firmas por imagen:** en la sección FIRMAS el proveedor hace clic en la
    zona "Clic para insertar firma / sello" y **sube/pega la imagen de su firma
    escaneada** (o el sello). Igual para el Vo. Bo. de EVOLTI.
    > Esto funciona mejor abriendo el PDF con **Adobe Acrobat Reader** (gratuito).

## Cómo dejarlo NO editable (seguridad)
Cuando el proveedor te devuelva el formulario **ya diligenciado y firmado**,
conviértelo en un documento bloqueado antes de archivarlo. Así nadie puede
alterar la información después.

### Uso del script
Requiere tener Python con PyMuPDF (`pip install pymupdf`).

```bash
python3 bloquear-rup.py  "RUP diligenciado del proveedor.pdf"
```

Genera un archivo `... (BLOQUEADO).pdf` que:
- **Aplana** todos los campos: el texto y las firmas quedan fijos en la hoja
  (ya no son campos editables).
- **Aplica permisos**: prohíbe modificar el documento y los formularios.
- Se **abre sin contraseña** para leer e imprimir, pero **no se puede editar**.

Puedes indicar un nombre de salida distinto:
```bash
python3 bloquear-rup.py  "entrada.pdf"  "salida-oficial.pdf"
```

## Nota importante
Un PDF rellenable estándar **no puede auto-bloquearse** cuando el proveedor lo
guarda (eso dependería de que cada proveedor tenga Acrobat Pro). La práctica
correcta —y la que usan los analistas de proveedores— es **bloquearlo tú al
recibirlo**, que es justo lo que hace este script.
