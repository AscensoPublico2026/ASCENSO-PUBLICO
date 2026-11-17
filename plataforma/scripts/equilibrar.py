# -*- coding: utf-8 -*-
"""Muestra las preguntas en las que la opción correcta es la más larga, con la
diferencia frente a la segunda. Sirve para alargar un distractor (nunca para
recortar la respuesta) hasta que elegir la opción más larga deje de funcionar.

Uso: python3 scripts/equilibrar.py <modulo> [carpeta]
"""
import importlib
import pathlib
import sys

mod = sys.argv[1]
carpeta = sys.argv[2] if len(sys.argv) > 2 else "banco_pgn"
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / carpeta))
banco = importlib.import_module(mod).BANCO

malas = 0
for i, q in enumerate(banco):
    largos = sorted(((len(o), k) for k, o in enumerate(q["ops"])), reverse=True)
    if largos[0][1] == q["correcta"]:
        malas += 1
        print(f"[{i}] {q['tema']}  (+{largos[0][0] - largos[1][0]} car sobre la segunda)")
print(f"\n{malas} de {len(banco)} con la correcta más larga ({malas * 100 // len(banco)} %)")
