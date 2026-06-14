#!/usr/bin/env python3
"""
optimizar_imagenes.py
=====================
Optimiza imágenes para la web (fotos del fundador, alumnos, capturas, etc.):
- Reduce el peso (las fotos de cámara/celular suelen pesar 3-8 MB).
- Genera varios tamaños (responsive) y versión WebP (mucho más liviana).
- Quita metadatos (orientación corregida, sin EXIF de ubicación).

POR QUÉ
-------
Las imágenes pesadas hacen lenta la landing y arruinan la conversión, sobre
todo en celular (tráfico de TikTok). Esto las deja listas para producción.

USO
---
    pip install -r requirements.txt
    python3 optimizar_imagenes.py --in ./originales --out ../brand/fotos

    # Tamaños personalizados y calidad:
    python3 optimizar_imagenes.py --in ./originales --out ../brand/fotos --anchos 1600 1080 640 --calidad 80

SALIDA
------
Por cada imagen `foto.jpg` genera, en la carpeta de salida:
    foto-1600.webp / foto-1600.jpg
    foto-1080.webp / foto-1080.jpg
    foto-640.webp  / foto-640.jpg
Luego en el HTML puedes usarlas con <picture> y srcset.
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Falta Pillow. Ejecuta:  pip install -r requirements.txt")

EXTENSIONES = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def optimizar(origen: Path, destino_dir: Path, anchos: list[int], calidad: int) -> int:
    generadas = 0
    img = Image.open(origen)
    img = ImageOps.exif_transpose(img)  # corrige rotación según EXIF
    if img.mode in ("RGBA", "P", "LA"):
        fondo = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        fondo.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
        img = fondo
    else:
        img = img.convert("RGB")

    base = origen.stem
    for ancho in sorted(set(anchos), reverse=True):
        if ancho >= img.width:
            redim = img.copy()
        else:
            alto = round(img.height * ancho / img.width)
            redim = img.resize((ancho, alto), Image.LANCZOS)
        for ext, params in (
            (".webp", {"quality": calidad, "method": 6}),
            (".jpg", {"quality": calidad, "optimize": True, "progressive": True}),
        ):
            salida = destino_dir / f"{base}-{ancho}{ext}"
            redim.save(salida, **params)
            generadas += 1
            print(f"  → {salida.name}  ({salida.stat().st_size // 1024} KB)")
    return generadas


def main():
    ap = argparse.ArgumentParser(description="Optimizador de imágenes para la landing.")
    ap.add_argument("--in", dest="entrada", required=True, help="Carpeta con las imágenes originales.")
    ap.add_argument("--out", dest="salida", required=True, help="Carpeta de salida.")
    ap.add_argument("--anchos", type=int, nargs="+", default=[1600, 1080, 640], help="Anchos a generar (px).")
    ap.add_argument("--calidad", type=int, default=82, help="Calidad 1-100 (recomendado 78-85).")
    args = ap.parse_args()

    entrada, salida = Path(args.entrada), Path(args.salida)
    if not entrada.is_dir():
        sys.exit(f"No existe la carpeta de entrada: {entrada}")
    salida.mkdir(parents=True, exist_ok=True)

    imagenes = [p for p in sorted(entrada.iterdir()) if p.suffix.lower() in EXTENSIONES]
    if not imagenes:
        sys.exit(f"No se encontraron imágenes en {entrada}")

    total = 0
    for p in imagenes:
        print(f"\n📷 {p.name}")
        try:
            total += optimizar(p, salida, args.anchos, args.calidad)
        except Exception as e:
            print(f"  ⚠️  Error con {p.name}: {e}")
    print(f"\n✅ Listo: {total} archivos generados en {salida}")


if __name__ == "__main__":
    main()
