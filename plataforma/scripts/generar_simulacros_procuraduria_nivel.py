"""Simulacros gratis de la Procuraduría por nivel.

Cada uno combina 10 preguntas del núcleo común del concurso (estructura y
funciones de la PGN, disciplinario, mecanismos, derecho de petición) con 10 del
nivel al que aspira el participante. Todas con tres opciones plausibles, el formato oficial de la prueba.

Uso: python3 scripts/generar_simulacros_procuraduria_nivel.py
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from bancos_simulacro_niveles import ASISTENCIAL, TECNICO, PROFESIONAL  # noqa: E402
from generar_simulacro_procuraduria import PREGUNTAS as PGN  # noqa: E402

BASE = HERE.parent / "public" / "simulacro-gratis"

# Del banco de la Procuraduría, las que son núcleo común de cualquier nivel.
TEMAS_NUCLEO = [
    "Acción de cumplimiento: requisito de renuencia",
    "Derecho de petición: término para documentos",
    "Derecho de petición: cuando no se alcanza a responder",
    "Sanciones disciplinarias según la falta",
    "Poder disciplinario preferente",
    "Elección del Procurador General",
    "Quiénes ejercen el Ministerio Público",
    "Habeas corpus",
    "Habeas data",
    "Queja o reclamo",
]
NUCLEO = [p for t in TEMAS_NUCLEO for p in PGN if p["tema"] == t]
assert len(NUCLEO) == 10, len(NUCLEO)


def al_contexto_pgn(preguntas):
    """Ubica los casos genéricos del sector público en la Procuraduría."""
    cambios = [
        ("una entidad pública", "la Procuraduría"),
        ("de la entidad", "de la Procuraduría"),
        ("en la entidad", "en la Procuraduría"),
        ("su entidad", "su despacho"),
        ("la entidad", "la Procuraduría"),
        ("tu entidad", "tu despacho"),
    ]
    out = []
    for p in preguntas:
        q = json.loads(json.dumps(p))
        for campo in ("ctx", "q"):
            for a, b in cambios:
                q[campo] = q[campo].replace(a, b)
        q["refT"] = q["refT"].replace("Competencias del Nivel", "Competencias del nivel")
        out.append(q)
    return out


NIVELES = {
    "procuraduria-operativo": {
        "preguntas": NUCLEO + al_contexto_pgn(ASISTENCIAL),
        "nombre": "Operativo y administrativo",
        "desc": "20 casos para los empleos de auxiliar, citador y oficinista: estructura y funciones de la Procuraduría, derecho de petición, gestión documental, atención al ciudadano y alcance del cargo.",
        "badge": "🧰 Operativo y administrativo",
        "codigo": "SIM-GRATIS-PGN-OPE",
    },
    "procuraduria-tecnico": {
        "preguntas": NUCLEO + al_contexto_pgn(TECNICO),
        "nombre": "Técnico",
        "desc": "20 casos para sustanciadores, técnicos y tecnólogos: núcleo común del concurso, procedimiento, calidad de la información, seguridad y competencias del nivel.",
        "badge": "🛠️ Técnico y sustanciadores",
        "codigo": "SIM-GRATIS-PGN-TEC",
    },
    "procuraduria-profesional": {
        "preguntas": NUCLEO + al_contexto_pgn(PROFESIONAL),
        "nombre": "Profesional y asesor",
        "desc": "20 casos para profesional universitario, asesor y ejecutivo: núcleo común del concurso, conceptos técnicos, conflicto de interés, independencia frente a la jerarquía y liderazgo.",
        "badge": "🎓 Profesional y asesor",
        "codigo": "SIM-GRATIS-PGN-PRO",
    },
}


def main():
    base = (BASE / "procuraduria.html").read_text(encoding="utf-8")
    for slug, cfg in NIVELES.items():
        preguntas = cfg["preguntas"]
        assert len(preguntas) == 20, (slug, len(preguntas))
        s = base
        i = s.index("const preguntas=")
        j = s.index("];", i) + 2
        s = s[:i] + "const preguntas=" + json.dumps(preguntas, ensure_ascii=False) + ";" + s[j:]
        s = s.replace('const NIVEL_ID="procuraduria";', f'const NIVEL_ID="{slug}";')
        s = re.sub(r"<title>.*?</title>",
                   f"<title>Simulacro gratis Procuraduría 2026 · Nivel {cfg['nombre']} — Ascenso Público</title>",
                   s, count=1, flags=re.S)
        s = s.replace("🎁 Simulacro Gratis · Concurso Procuraduría 2026",
                      f"🎁 Simulacro Gratis · Procuraduría 2026 · {cfg['nombre']}")
        s = s.replace("Simulacro Procuraduría<br>Núcleo común",
                      f"Simulacro Procuraduría<br>Nivel {cfg['nombre']}")
        s = re.sub(r"20 preguntas tipo caso sobre la Procuraduría[^<]*", cfg["desc"], s)
        s = s.replace('<span class="badge">⚖️ Procuraduría</span>', f'<span class="badge">{cfg["badge"]}</span>')
        s = s.replace("SIM-GRATIS-PGN", cfg["codigo"])
        (BASE / f"{slug}.html").write_text(s, encoding="utf-8")
        print("OK", slug, len(preguntas))


if __name__ == "__main__":
    main()
