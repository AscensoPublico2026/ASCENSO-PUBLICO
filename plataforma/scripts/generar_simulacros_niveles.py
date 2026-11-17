"""Reemplaza el banco de preguntas de los simulacros gratis por nivel con el de
scripts/bancos_simulacro_niveles.py, conservando la plantilla HTML.
Uso: python3 scripts/generar_simulacros_niveles.py
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from bancos_simulacro_niveles import BANCOS  # noqa: E402

BASE = pathlib.Path(__file__).resolve().parent.parent / "public" / "simulacro-gratis"

for nivel, preguntas in BANCOS.items():
    assert len(preguntas) == 20, (nivel, len(preguntas))
    f = BASE / f"{nivel}.html"
    s = f.read_text(encoding="utf-8")
    i = s.index("const preguntas=")
    j = s.index("];", i) + 2
    s = s[:i] + "const preguntas=" + json.dumps(preguntas, ensure_ascii=False) + ";" + s[j:]
    f.write_text(s, encoding="utf-8")
    print("OK", f.name, len(preguntas))
