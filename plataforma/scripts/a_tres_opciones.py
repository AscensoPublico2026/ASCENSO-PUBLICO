# -*- coding: utf-8 -*-
"""Convierte un banco de cuatro opciones al formato oficial de tres.

Recibe, por cada pregunta, el índice del distractor que se elimina: el más
débil, es decir, el que nadie marcaría. Reescribe el módulo conservando los
textos y ajusta el índice de la respuesta correcta.

Uso: python3 scripts/a_tres_opciones.py <modulo> <carpeta> <indices separados por coma>
"""
import importlib
import pathlib
import pprint
import sys

mod, carpeta, crudo = sys.argv[1], sys.argv[2], sys.argv[3]
quitar = [int(x) for x in crudo.split(",")]

base = pathlib.Path(__file__).resolve().parent / carpeta
sys.path.insert(0, str(base))
banco = importlib.import_module(mod).BANCO

assert len(quitar) == len(banco), f"{len(quitar)} índices para {len(banco)} preguntas"

salida = []
for q, fuera in zip(banco, quitar):
    assert fuera != q["correcta"], f"no se puede quitar la respuesta correcta en «{q['tema']}»"
    n = dict(q)
    n["ops"] = [o for i, o in enumerate(q["ops"]) if i != fuera]
    n["expl"] = [e for i, e in enumerate(q["expl"]) if i != fuera]
    n["correcta"] = q["correcta"] - (1 if q["correcta"] > fuera else 0)
    salida.append(n)

ruta = base / f"{mod}.py"
texto = ruta.read_text(encoding="utf-8")
cabeza = texto[: texto.index("BANCO = [")]
cuerpo = pprint.pformat(salida, width=118, sort_dicts=False)
ruta.write_text(cabeza + "BANCO = " + cuerpo + "\n", encoding="utf-8")
print(f"{mod}: {len(salida)} preguntas a tres opciones")
