#!/usr/bin/env python3
"""Crea una copia de una guía adaptada a otro cargo mediante reemplazos de texto.

Uso: python3 scripts/adaptar-guia.py <reglas.json>
reglas.json = {
  "guias": [{"src": "guias/X.html", "dst": "X-AIV-....html", "codigo_src": "X", "codigo_dst": "X-AIV",
             "extra": [["texto viejo", "texto nuevo"], ...]}],
  "comunes": [["texto viejo", "texto nuevo"], ...],     # se aplican en orden
  "regex": [["patron", "reemplazo"], ...],               # después de los comunes
  "fugas": "regex de términos que no deben quedar"
}
Escribe guias/<dst> y plataforma/public/seed-guias/<dst>; reporta las fugas restantes con contexto.
"""
import json, re, sys, html

R = json.load(open(sys.argv[1], encoding="utf-8"))
for g in R["guias"]:
    h = open(g["src"], encoding="utf-8").read()
    for a, b in g.get("extra", []):
        if a not in h:
            print(f"  ⚠ [{g['codigo_dst']}] no encontrado: {a[:70]}")
        h = h.replace(a, b)
    for a, b in R.get("comunes", []):
        h = h.replace(a, b)
    for a, b in R.get("regex", []):
        h = re.sub(a, b, h)
    # código del documento (doc-ref, title, footer) — solo el token exacto
    h = re.sub(r"(?<![A-Z0-9-])" + re.escape(g["codigo_src"]) + r"(?![A-Z0-9-])", g["codigo_dst"], h)
    carpeta = "simulacro" if g["dst"].startswith("SIM-") else "guias"
    open(f"{carpeta}/{g['dst']}", "w", encoding="utf-8").write(h)
    open(f"plataforma/public/seed-guias/{g['dst']}", "w", encoding="utf-8").write(h)
    texto = html.unescape(re.sub(r"<[^>]+>", " ", h))
    fz = [m for m in re.finditer(R["fugas"], texto)]
    print(f"{g['codigo_dst']:20} {len(h)//1000}KB  fugas={len(fz)}")
    for m in fz[:12]:
        print("   ·", re.sub(r"\s+", " ", texto[max(0, m.start() - 90): m.end() + 60]))
