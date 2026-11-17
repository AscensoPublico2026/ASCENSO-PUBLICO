# -*- coding: utf-8 -*-
"""Diagnóstico de equilibrio de un banco: qué opción correcta se queda corta y
cuál se pasa de larga frente a sus distractores.

Uso: python3 scripts/equilibrio.py <modulo> <carpeta>
"""
import importlib
import pathlib
import statistics
import sys

mod, carpeta = sys.argv[1], sys.argv[2]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / carpeta))
banco = importlib.import_module(mod).BANCO

for i, q in enumerate(banco):
    c = len(q["ops"][q["correcta"]])
    otras = [len(o) for k, o in enumerate(q["ops"]) if k != q["correcta"]]
    media = statistics.mean(otras)
    if c < media - 18:
        print(f'CORTA {i} +{media - c:.0f} | {q["ops"][q["correcta"]]}')
    elif c > max(otras):
        k = max((k for k in range(len(q["ops"])) if k != q["correcta"]), key=lambda k: len(q["ops"][k]))
        print(f'LARGA {i} op{k} +{c - len(q["ops"][k]) + 8} | {q["ops"][k]}')

ok = [len(q["ops"][q["correcta"]]) for q in banco]
mal = [len(o) for q in banco for i, o in enumerate(q["ops"]) if i != q["correcta"]]
mas = sum(
    1
    for q in banco
    if len(q["ops"][q["correcta"]]) > max(len(o) for k, o in enumerate(q["ops"]) if k != q["correcta"])
)
print(f"\nratio {statistics.mean(ok) / statistics.mean(mal):.2f} | más larga {mas * 100 // len(banco)} %")
