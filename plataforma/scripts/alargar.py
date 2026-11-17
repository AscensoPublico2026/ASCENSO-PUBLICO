# -*- coding: utf-8 -*-
"""Lista las preguntas en las que la opción correcta sigue siendo la más larga
y señala qué distractor conviene extender y en cuántos caracteres.

Uso: python3 scripts/alargar.py <modulo> <carpeta>
"""
import importlib
import pathlib
import sys

mod, carpeta = sys.argv[1], sys.argv[2]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / carpeta))
banco = importlib.import_module(mod).BANCO

for i, q in enumerate(banco):
    largos = [len(o) for o in q["ops"]]
    if largos[q["correcta"]] == max(largos):
        k, l = max(((k, len(o)) for k, o in enumerate(q["ops"]) if k != q["correcta"]), key=lambda x: x[1])
        print(f'{i}|{k}|+{largos[q["correcta"]] - l + 8}|{q["ops"][k]}')
