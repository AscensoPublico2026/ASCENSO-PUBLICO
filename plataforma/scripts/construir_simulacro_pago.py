# -*- coding: utf-8 -*-
"""Construye el banco del simulacro de pago de la Procuraduría (nivel profesional).

Toma los cinco bloques temáticos, baraja las opciones de cada pregunta con una
semilla fija (para que la respuesta correcta no quede siempre en la misma
posición), intercala los ejes y valida el resultado.

Uso: python3 scripts/construir_simulacro_pago.py
"""
import json
import pathlib
import random
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "banco_pgn"))

import b1_estructura, b2_constitucion, b3_disciplinario  # noqa: E402
import b4_mecanismos_funcion, b5_cpaca_contratacion_integridad  # noqa: E402

BLOQUES = [
    b1_estructura.BANCO,
    b2_constitucion.BANCO,
    b3_disciplinario.BANCO,
    b4_mecanismos_funcion.BANCO,
    b5_cpaca_contratacion_integridad.BANCO,
]

SALIDA = HERE.parent / "data" / "simulacros-pago" / "procuraduria-profesional.json"


def barajar(preguntas):
    """Baraja las opciones de cada pregunta moviendo con ellas su explicación."""
    rnd = random.Random(20260317)
    out = []
    for p in preguntas:
        idx = list(range(len(p["ops"])))
        rnd.shuffle(idx)
        q = dict(p)
        q["ops"] = [p["ops"][i] for i in idx]
        q["expl"] = [p["expl"][i] for i in idx]
        q["correcta"] = idx.index(p["correcta"])
        out.append(q)
    return out


def intercalar(bloques):
    """Reparte los ejes a lo largo del examen en vez de dejarlos en bloque."""
    rnd = random.Random(76_2026)
    restantes = [list(b) for b in bloques]
    for b in restantes:
        rnd.shuffle(b)
    orden = []
    while any(restantes):
        for b in restantes:
            if b:
                orden.append(b.pop())
    return orden


def main():
    todas = [q for b in BLOQUES for q in b]
    assert len(todas) == 100, f"Se esperaban 100 preguntas y hay {len(todas)}"

    temas = [q["tema"] for q in todas]
    repetidos = [t for t, n in Counter(temas).items() if n > 1]
    assert not repetidos, f"Temas repetidos: {repetidos}"

    for q in todas:
        assert len(q["ops"]) == 4, q["tema"]
        assert len(q["expl"]) == 4, q["tema"]
        assert 0 <= q["correcta"] < 4, q["tema"]
        assert q["nivel"] in ("basic", "intermediate", "advanced"), q["tema"]
        assert len(q["ctx"]) > 60, f"Contexto muy corto: {q['tema']}"
        assert len(set(q["ops"])) == 4, f"Opciones repetidas: {q['tema']}"

    banco = intercalar([barajar(b) for b in BLOQUES])

    dist = Counter(q["correcta"] for q in banco)
    assert max(dist.values()) <= 35, f"Respuesta correcta mal distribuida: {dict(dist)}"

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(banco, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"{len(banco)} preguntas -> {SALIDA}")
    print("Posición de la respuesta correcta:", dict(sorted(dist.items())))
    print("Por eje:", dict(Counter(q["refT"] for q in banco)))
    print("Por dificultad:", dict(Counter(q["nivel"] for q in banco)))
    print("Primeros ejes del examen:", [q["refT"][:18] for q in banco[:6]])


if __name__ == "__main__":
    main()
