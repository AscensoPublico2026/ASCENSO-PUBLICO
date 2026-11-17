"""Publica las guías generales (Estado y función pública, relación
Estado-ciudadano y marco institucional) en public/guias-gratis/ como material
gratuito: añade una franja superior de Ascenso Público y quita la numeración
por día, que solo tiene sentido dentro de la ruta de 21 días del curso.

Uso: python3 scripts/generar_guias_gratis.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "public" / "seed-guias"
DST = ROOT / "public" / "guias-gratis"
DST.mkdir(exist_ok=True)

# (archivo origen, archivo destino, nombre, día que ocupa en la ruta del curso)
GUIAS = [
    ("INTRO-00-presentacion-curso.html", "como-funciona-un-concurso-cnsc.html", "Cómo funciona un concurso de la CNSC", 1),
    ("GEN-01-estado-funcion-publica.html", "estado-y-funcion-publica.html", "Estado y Función Pública", 2),
    ("GEN-02-relacion-estado-ciudadano.html", "relacion-estado-ciudadano.html", "Relación Estado-Ciudadano", 3),
    ("GEN-03-marco-institucional.html", "marco-institucional.html", "Marco Institucional", 4),
]

FRANJA = """
<div id="ap-franja-gratis" style="position:sticky;top:0;z-index:9999;background:#0a2a5e;color:#fff;font-family:system-ui,-apple-system,'Segoe UI',sans-serif;padding:10px 16px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:center;box-shadow:0 4px 18px rgba(0,0,0,.25);font-size:14px;line-height:1.35">
  <span style="background:#e8a33d;color:#0a2a5e;font-weight:800;border-radius:999px;padding:2px 10px;font-size:12px;letter-spacing:.05em">GUÍA GRATIS</span>
  <span>Esta es una de las guías generales de la <b>ruta de 21 días</b> de Ascenso Público. En el curso, el resto se arma con el manual de funciones de <b>tu cargo</b>.</span>
  <a href="/simulacro" style="color:#0a2a5e;background:#f6c56b;font-weight:800;border-radius:10px;padding:6px 12px;text-decoration:none">Haz el simulacro gratis</a>
  <a href="/#precio" style="color:#fff;border:1.5px solid #f6c56b;font-weight:700;border-radius:10px;padding:5px 12px;text-decoration:none">Ver el curso</a>
</div>
"""


def sin_dias(s: str, n: int) -> str:
    """Quita la numeración por día: la guía gratis se lee suelta, no en el plan."""
    exactos = [
        (f"Día {n} de 21", "Guía general gratis"),
        (f"Día {n} · Biblioteca General", "Biblioteca General · Guía gratis"),
        (f"¿Qué dominarás en el Día {n}?", "¿Qué dominarás en esta guía?"),
        (f"Tienes el Día {n} dominado", "Tienes esta guía dominada"),
        (f"Finalizar Día {n}", "Finalizar guía"),
        (f"¡Completaste el Día {n} y la Biblioteca General!", "¡Completaste la guía y la Biblioteca General!"),
        (f"¡Completaste el Día {n}!", "¡Completaste la guía!"),
        (f"Completaste el Día {n}:", "Completaste la guía:"),
        (f"Has completado el Día {n}.", "Has completado la guía."),
        (f"Has completado todo el contenido del Día {n}.", "Has completado todo el contenido de la guía."),
        ("el método de 4 pasos del Día 1", "el método de 4 pasos"),
        (f"Listo para el Día {n + 1}.", "Listo para la siguiente guía."),
        ("Mañana avanzas", "En el curso avanzas"),
        ("Guías funcionales (Días 9–20).", "Guías funcionales del curso."),
        ("Guías por nivel (Días 5–8).", "Guías por nivel del curso."),
        ("Llega al simulacro final (Día 21)", "Llega al simulacro final del curso"),
        ("Mañana:", "Siguiente guía:"),
        ("último día del módulo general", "última guía del módulo general"),
        ("el último día de la Biblioteca General", "la última de la Biblioteca General"),
    ]
    for a, b in exactos:
        s = s.replace(a, b)

    patrones = [
        (r"Conecta con el Día \d+", "Antes de empezar"),
        (r"Repaso del Día \d+", "Repaso de otra guía"),
        (r"\(Días \d+ a \d+\)", "(el módulo general)"),
        (r"A partir del Día \d+ (?:comienzan|inician)", "En el curso, después del módulo general, comienzan"),
        (r"<strong>Día \d+</strong>", "<strong>el curso</strong>"),
        (r"en el Día \d+", "en la Biblioteca General"),
        (r"del Día \d+", "de esta guía"),
        (r"el Día \d+", "esta guía"),
        (r"tu Día \d+", "lo aprendido"),
        (r"este Día \d+", "esta guía"),
        (r"Día \d+\s*[:·]\s*", ""),
        (r"\(Día \d+\)", ""),
        (r"Día \d+", "esta guía"),
    ]
    for pat, rep in patrones:
        s = re.sub(pat, rep, s)
    return s


for src, dst, nombre, dia in GUIAS:
    s = (SRC / src).read_text(encoding="utf-8")
    s = sin_dias(s, dia)
    s = re.sub(r"<title>.*?</title>",
               f"<title>Guía gratis: {nombre} · Concursos de mérito — Ascenso Público</title>",
               s, count=1, flags=re.S)
    s = s.replace("<head>", '<head>\n<meta name="robots" content="index,follow">', 1)
    s = re.sub(r"(<body[^>]*>)", r"\1" + FRANJA, s, count=1)
    assert "Día " not in s, dst
    (DST / dst).write_text(s, encoding="utf-8")
    print("OK", dst)
