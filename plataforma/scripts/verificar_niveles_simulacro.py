# -*- coding: utf-8 -*-
"""Verifica los simulacros gratis publicados:

1. Que el nivel de cada uno esté registrado en la API de leads. Si falta uno, la
   API responde «Nivel inválido» y el lead se pierde sin que nadie se entere.
2. Que el banco embebido sea coherente: tres opciones, una explicación por
   opción y la clave dentro del rango.
3. Que el barajado de opciones se derive del número real de opciones. Un
   `barajar([0,1,2,3])` con preguntas de tres opciones pinta una opción vacía.

Uso: python3 scripts/verificar_niveles_simulacro.py
"""
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
HTML = RAIZ / "public" / "simulacro-gratis"
API = RAIZ / "app" / "api" / "simulacro" / "lead" / "route.ts"

OPCIONES = 3
errores = []

publicados = set()
for f in sorted(HTML.glob("*.html")):
    texto = f.read_text(encoding="utf-8")
    m = re.search(r'const NIVEL_ID="([^"]+)"', texto)
    if m:
        publicados.add(m.group(1))

    if "barajar([0,1,2,3])" in texto or "barajar([0, 1, 2, 3])" in texto:
        errores.append(f"{f.name}: baraja un número fijo de opciones; usa p.ops.map")

    i = texto.find("const preguntas=")
    if i < 0:
        errores.append(f"{f.name}: no tiene banco embebido")
        continue
    banco = json.loads(texto[i + len("const preguntas="):texto.index("];", i) + 1])
    for n, q in enumerate(banco, 1):
        if len(q["ops"]) != OPCIONES:
            errores.append(f"{f.name} p{n}: {len(q['ops'])} opciones, se esperan {OPCIONES}")
        if len(q["expl"]) != len(q["ops"]):
            errores.append(f"{f.name} p{n}: {len(q['expl'])} explicaciones para {len(q['ops'])} opciones")
        if not 0 <= q["correcta"] < len(q["ops"]):
            errores.append(f"{f.name} p{n}: clave {q['correcta']} fuera de rango")

fuente = API.read_text(encoding="utf-8")
bloque = fuente[fuente.index("const NOMBRE_NIVEL"):fuente.index("};", fuente.index("const NOMBRE_NIVEL"))]
registrados = set(re.findall(r'^\s*"?([a-z0-9-]+)"?\s*:', bloque, re.M))

faltan = publicados - registrados
sobran = registrados - publicados

for n in sorted(faltan):
    print(f"FALTA en la API: {n} — sus leads se perderían", file=sys.stderr)
for n in sorted(sobran):
    print(f"Registrado sin simulacro publicado: {n}")

for e in errores:
    print(e, file=sys.stderr)

print(f"{len(publicados)} simulacros publicados, {len(registrados)} niveles en la API")
sys.exit(1 if faltan or errores else 0)
