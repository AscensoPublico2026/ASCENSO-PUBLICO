"""Genera public/simulacro-gratis/docente.html desde la plantilla del simulacro
profesional, con el banco de banco_simulacro_docente.py.
Uso: python3 scripts/generar_simulacro_docente.py
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from banco_simulacro_docente import DOCENTE  # noqa: E402

BASE = pathlib.Path(__file__).resolve().parent.parent / "public" / "simulacro-gratis"
s = (pathlib.Path(__file__).resolve().parent / "plantillas" / "simulacro.html").read_text(encoding="utf-8")
i = s.index("const preguntas=")
j = s.index("];", i) + 2
s = s[:i] + "const preguntas=" + json.dumps(DOCENTE, ensure_ascii=False) + ";" + s[j:]
s = s.replace('const NIVEL_ID="profesional";', 'const NIVEL_ID="docente";')
s = re.sub(r"<title>.*?</title>",
           "<title>Simulacro gratis Concurso Docente 2026 — Ascenso Público</title>",
           s, count=1, flags=re.S)
s = s.replace("🎁 Simulacro Gratis · Nivel Profesional", "🎁 Simulacro Gratis · Concurso Docente 2026")
s = s.replace("Simulacro CNSC Gratis<br>Nivel Profesional", "Simulacro Concurso<br>Docente 2026")
s = s.replace(
    "20 preguntas de juicio situacional tipo CNSC sobre el Estado, la función pública y las competencias del nivel profesional. Mide tu preparación para la prueba escrita y descubre qué reforzar.",
    "20 preguntas sobre lectura crítica, razonamiento cuantitativo, pedagogía, normatividad educativa, convivencia escolar y casos de aula. Mide tu preparación para la prueba eliminatoria del concurso docente.")
s = s.replace('<span class="badge">🎓 Nivel Profesional</span>', '<span class="badge">👩‍🏫 Docentes</span>')
s = s.replace("como en la prueba real de la CNSC", "como en la prueba escrita del concurso")
s = s.replace("SIM-GRATIS-PRO", "SIM-GRATIS-DOC")
(BASE / "docente.html").write_text(s, encoding="utf-8")
print("OK docente.html", len(DOCENTE))
