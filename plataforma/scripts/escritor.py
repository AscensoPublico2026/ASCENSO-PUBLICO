# -*- coding: utf-8 -*-
"""Serializa un banco de preguntas a Python legible, con cada texto en una
sola línea. pprint parte las cadenas largas en varios trozos concatenados, lo
que impide hacer reemplazos de texto sobre el archivo."""


def volcar(banco) -> str:
    def cadena(t: str) -> str:
        return '"' + t.replace("\\", "\\\\").replace('"', '\\"') + '"'

    partes = ["BANCO = ["]
    for q in banco:
        partes.append("dict(")
        partes.append(f"    tema={cadena(q['tema'])}, ref={cadena(q['ref'])},")
        partes.append(f"    refT={cadena(q['refT'])}, nivel={cadena(q['nivel'])},")
        partes.append(f"    ctx={cadena(q['ctx'])},")
        partes.append(f"    q={cadena(q['q'])},")
        partes.append("    ops=[")
        for o in q["ops"]:
            partes.append(f"        {cadena(o)},")
        partes.append("    ],")
        partes.append(f"    correcta={q['correcta']},")
        partes.append("    expl=[")
        for e in q["expl"]:
            partes.append(f"        {cadena(e)},")
        partes.append("    ],")
        partes.append("),")
        partes.append("")
    partes.append("]")
    return "\n".join(partes) + "\n"
