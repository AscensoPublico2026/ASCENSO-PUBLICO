# -*- coding: utf-8 -*-
"""Comprueba que todo simulacro gratis publicado tenga su nivel registrado en la
API de leads. Si falta uno, la API responde «Nivel inválido» y el lead se pierde
sin que nadie se entere.

Uso: python3 scripts/verificar_niveles_simulacro.py
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
HTML = RAIZ / "public" / "simulacro-gratis"
API = RAIZ / "app" / "api" / "simulacro" / "lead" / "route.ts"

publicados = set()
for f in sorted(HTML.glob("*.html")):
    m = re.search(r'const NIVEL_ID="([^"]+)"', f.read_text(encoding="utf-8"))
    if m:
        publicados.add(m.group(1))

fuente = API.read_text(encoding="utf-8")
bloque = fuente[fuente.index("const NOMBRE_NIVEL"):fuente.index("};", fuente.index("const NOMBRE_NIVEL"))]
registrados = set(re.findall(r'^\s*"?([a-z0-9-]+)"?\s*:', bloque, re.M))

faltan = publicados - registrados
sobran = registrados - publicados

for n in sorted(faltan):
    print(f"FALTA en la API: {n} — sus leads se perderían", file=sys.stderr)
for n in sorted(sobran):
    print(f"Registrado sin simulacro publicado: {n}")

print(f"{len(publicados)} simulacros publicados, {len(registrados)} niveles en la API")
sys.exit(1 if faltan else 0)
