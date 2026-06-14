#!/usr/bin/env python3
"""
scrape_simo.py
==============
Extrae las convocatorias de SIMO (CNSC) usando un navegador headless (Playwright),
porque SIMO es una aplicación dinámica que se arma con JavaScript y NO se puede
leer con un simple `requests`/`curl`.

QUÉ HACE
--------
1. Abre https://simo.cnsc.gov.co en un navegador real (Chromium).
2. Espera a que cargue el listado de convocatorias "En desarrollo".
3. Extrae cada convocatoria (nombre, entidad, estado/etapa, fecha).
4. (Opcional) Filtra solo las que estén PENDIENTES DE PRUEBA ESCRITA.
5. Guarda el resultado en `convocatorias.json` con el MISMO formato que usa la
   landing (landing/index.html → const CONVOCATORIAS) y también imprime el
   snippet listo para pegar.

IMPORTANTE (léelo)
------------------
- SIMO cambia su HTML con frecuencia. Los SELECTORES marcados con  # AJUSTAR
  deben verificarse contra el sitio real (abre el inspector del navegador).
- Respeta los términos de uso de la CNSC. Este script es para consultar
  información pública, sin sobrecargar el servidor (un solo acceso).
- Ejecuta el navegador en modo visible (headless=False) la primera vez para
  ver qué carga y ajustar los selectores.

USO
---
    pip install -r requirements.txt
    playwright install chromium
    python3 scrape_simo.py                 # headless
    python3 scrape_simo.py --ver            # con navegador visible (para depurar)
    python3 scrape_simo.py --solo-prueba    # filtra pendientes de prueba escrita
"""

import argparse
import json
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Falta Playwright. Ejecuta:  pip install -r requirements.txt && playwright install chromium")

SIMO_URL = "https://simo.cnsc.gov.co/"
# Si conoces la ruta directa al listado de convocatorias, ponla aquí:
SIMO_CONVOCATORIAS_URL = "https://simo.cnsc.gov.co/#/convocatorias"  # AJUSTAR si cambia

# Palabras que sugieren "pendiente de prueba escrita" (para el filtro opcional).
PISTAS_PRUEBA_ESCRITA = [
    "prueba escrita", "pruebas escritas", "aplicación de pruebas",
    "citación a pruebas", "pendiente de pruebas",
]


def clasificar_estado(texto: str) -> tuple[str, str]:
    """Devuelve (estado_css, etiqueta) a partir del texto de etapa de SIMO.
    estado_css debe ser uno de: 'abiertas' | 'cerradas' | 'proxima' (los que estiliza la landing).
    """
    t = (texto or "").lower()
    if "inscrip" in t and ("abiert" in t or "en curso" in t):
        return "abiertas", "Inscripciones abiertas"
    if any(p in t for p in PISTAS_PRUEBA_ESCRITA):
        return "proxima", "Pendiente de prueba escrita"
    if "cerrad" in t or "finaliz" in t:
        return "cerradas", "Inscripciones cerradas"
    # Por defecto, la dejamos como "próxima" (en desarrollo).
    return "proxima", texto.strip()[:40] or "En desarrollo"


def extraer(page):
    """Extrae las tarjetas de convocatoria de la página ya cargada.
    AJUSTAR los selectores según el DOM real de SIMO.
    """
    page.wait_for_load_state("networkidle")
    # Espera defensiva: dale tiempo a que el framework pinte las tarjetas.
    try:
        page.wait_for_selector(".convocatoria, .card, [class*='convocatoria']", timeout=20000)  # AJUSTAR
    except Exception:
        print("⚠️  No se encontró el selector de tarjetas. Revisa el DOM con --ver y ajusta los selectores.")

    tarjetas = page.query_selector_all(".convocatoria, .card, [class*='convocatoria']")  # AJUSTAR
    resultados = []
    for t in tarjetas:
        def texto(sel):
            el = t.query_selector(sel)
            return el.inner_text().strip() if el else ""

        nombre = texto("h3, .titulo, [class*='nombre']")          # AJUSTAR
        entidad = texto(".entidad, [class*='entidad']")            # AJUSTAR
        etapa = texto(".estado, .etapa, [class*='estado']")        # AJUSTAR
        fecha = texto(".fecha, [class*='fecha']") or "Fechas: por confirmar"  # AJUSTAR

        if not nombre:
            continue
        estado_css, etiqueta = clasificar_estado(etapa)
        resultados.append({
            "nombre": nombre,
            "entidad": entidad or "Entidad por confirmar",
            "estado": estado_css,
            "etiqueta": etiqueta,
            "fecha": fecha,
            "_etapa_original": etapa,  # útil para depurar / filtrar; quítalo antes de pegar
        })
    return resultados


def main():
    ap = argparse.ArgumentParser(description="Scraper de convocatorias de SIMO (CNSC).")
    ap.add_argument("--ver", action="store_true", help="Abre el navegador visible (depuración).")
    ap.add_argument("--solo-prueba", action="store_true", help="Filtra solo las pendientes de prueba escrita.")
    ap.add_argument("--salida", default=str(Path(__file__).parent / "convocatorias.json"))
    args = ap.parse_args()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not args.ver)
        page = browser.new_page(locale="es-CO")
        print(f"Abriendo {SIMO_CONVOCATORIAS_URL} ...")
        page.goto(SIMO_CONVOCATORIAS_URL, wait_until="domcontentloaded", timeout=60000)
        datos = extraer(page)
        browser.close()

    if args.solo_prueba:
        datos = [d for d in datos
                 if any(pista in (d["_etapa_original"] or "").lower() for pista in PISTAS_PRUEBA_ESCRITA)]

    # Quita el campo auxiliar antes de exportar.
    limpio = [{k: v for k, v in d.items() if not k.startswith("_")} for d in datos]

    Path(args.salida).write_text(json.dumps(limpio, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n✅ {len(limpio)} convocatorias guardadas en {args.salida}\n")
    print("👉 Pega esto en landing/index.html (reemplazando const CONVOCATORIAS):\n")
    print("const CONVOCATORIAS = " + json.dumps(limpio, ensure_ascii=False, indent=2) + ";")


if __name__ == "__main__":
    main()
