# -*- coding: utf-8 -*-
"""Construye los bancos del simulacro completo de pago de la Procuraduría.

Cada nivel comparte el núcleo común del concurso (estructura y funciones de la
PGN, Constitución, mecanismos de protección, integridad) y suma las
competencias de su nivel. Las opciones se barajan con semilla fija para que la
respuesta correcta no quede siempre en la misma posición, y los ejes se
intercalan para que el examen no vaya por bloques.

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
import b6_tecnico, b7_operativo  # noqa: E402

sys.path.insert(0, str(HERE / "banco_docente"))
import d1_lectura, d2_cuantitativo, d3_pedagogia  # noqa: E402
import d4_normatividad, d5_psicotecnica  # noqa: E402

SALIDA = HERE.parent / "data" / "simulacros-pago"


def por_eje(banco, eje):
    return [q for q in banco if q["refT"] == eje]


EST = por_eje(b1_estructura.BANCO, "Estructura y funciones de la PGN")
CON = por_eje(b2_constitucion.BANCO, "Estado, Constitución y estructura del Estado")
DIS = b3_disciplinario.BANCO
MEC = por_eje(b4_mecanismos_funcion.BANCO, "Mecanismos de protección de derechos")
FUN = por_eje(b4_mecanismos_funcion.BANCO, "Función pública y empleo público")
CPA = por_eje(b5_cpaca_contratacion_integridad.BANCO, "Procedimiento administrativo (CPACA)")
CTR = por_eje(b5_cpaca_contratacion_integridad.BANCO, "Contratación estatal")
INT = por_eje(b5_cpaca_contratacion_integridad.BANCO, "Integridad, conflicto de interés y transparencia")


def dis_por_dificultad(*niveles, cuantas):
    """Preguntas de disciplinario del grado de dificultad que pide cada nivel."""
    elegidas = [q for n in niveles for q in DIS if q["nivel"] == n]
    return elegidas[:cuantas]


BANCOS = {
    # Profesional y asesor: el disciplinario completo y la contratación estatal.
    "procuraduria-profesional": [EST, CON, DIS, MEC, FUN, CPA, CTR, INT],
    # Técnico: núcleo común, procedimiento y sustanciación, gestión documental.
    "procuraduria-tecnico": [
        EST, CON, dis_por_dificultad("advanced", "intermediate", cuantas=11),
        MEC, CPA, INT, b6_tecnico.BANCO,
    ],
    # Operativo y administrativo: núcleo común, función pública, atención y archivo.
    "procuraduria-operativo": [
        EST, CON, dis_por_dificultad("basic", "intermediate", cuantas=9),
        MEC, FUN[:11], INT, b7_operativo.BANCO,
    ],
    # Concurso docente: la prueba evalúa aptitudes y competencias básicas,
    # pedagogía, normatividad educativa y casos de aula.
    "docente": [
        d1_lectura.BANCO,
        d2_cuantitativo.BANCO,
        por_eje(d3_pedagogia.BANCO, "Competencias pedagógicas"),
        por_eje(d3_pedagogia.BANCO, "Evaluación del aprendizaje"),
        por_eje(d4_normatividad.BANCO, "Normatividad educativa"),
        por_eje(d4_normatividad.BANCO, "Convivencia escolar"),
        d5_psicotecnica.BANCO,
    ],
}


def barajar(preguntas, semilla):
    """Baraja las opciones de cada pregunta moviendo con ellas su explicación.

    La semilla se deriva del tema de cada pregunta para que dos bloques del
    mismo tamaño no reciban la misma permutación y la respuesta correcta no
    caiga siempre en la misma posición.
    """
    out = []
    for p in preguntas:
        rnd = random.Random(f"{semilla}:{p['tema']}")
        idx = list(range(len(p["ops"])))
        rnd.shuffle(idx)
        q = dict(p)
        q["ops"] = [p["ops"][i] for i in idx]
        q["expl"] = [p["expl"][i] for i in idx]
        q["correcta"] = idx.index(p["correcta"])
        out.append(q)
    return out


def intercalar(bloques, semilla):
    """Reparte los ejes a lo largo del examen en vez de dejarlos en bloque."""
    rnd = random.Random(semilla)
    restantes = [list(b) for b in bloques]
    for b in restantes:
        rnd.shuffle(b)
    orden = []
    while any(restantes):
        for b in restantes:
            if b:
                orden.append(b.pop())
    return orden


def validar(banco, nombre):
    assert len(banco) == 100, f"{nombre}: se esperaban 100 preguntas y hay {len(banco)}"

    repetidos = [t for t, n in Counter(q["tema"] for q in banco).items() if n > 1]
    assert not repetidos, f"{nombre}: temas repetidos {repetidos}"

    for q in banco:
        assert len(q["ops"]) == 4, f"{nombre}: {q['tema']}"
        assert len(q["expl"]) == 4, f"{nombre}: {q['tema']}"
        assert 0 <= q["correcta"] < 4, f"{nombre}: {q['tema']}"
        assert q["nivel"] in ("basic", "intermediate", "advanced"), f"{nombre}: {q['tema']}"
        assert len(q["ctx"]) > 60, f"{nombre}: contexto muy corto en {q['tema']}"
        assert len(set(q["ops"])) == 4, f"{nombre}: opciones repetidas en {q['tema']}"

    dist = Counter(q["correcta"] for q in banco)
    assert max(dist.values()) <= 35, f"{nombre}: respuesta correcta mal distribuida {dict(dist)}"
    return dist


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    for i, (slug, bloques) in enumerate(BANCOS.items()):
        semilla = 20260317 + i * 101
        banco = intercalar([barajar(b, semilla) for b in bloques], semilla + 7)
        dist = validar(banco, slug)
        (SALIDA / f"{slug}.json").write_text(json.dumps(banco, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\n{slug}: {len(banco)} preguntas")
        print("  posición de la correcta:", dict(sorted(dist.items())))
        print("  dificultad:", dict(Counter(q["nivel"] for q in banco)))
        for eje, n in Counter(q["refT"] for q in banco).most_common():
            print(f"    {n:3}  {eje}")


if __name__ == "__main__":
    main()
