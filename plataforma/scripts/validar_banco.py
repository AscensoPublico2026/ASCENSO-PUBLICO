# -*- coding: utf-8 -*-
"""Validador de calidad de los bancos de preguntas.

Detecta las pistas que permiten acertar sin saber el tema:

1. La opción correcta más larga que las demás. Si la correcta es siempre la
   más extensa, basta con elegir la más larga para aprobar.
2. Palabras absolutas («siempre», «nunca», «todo») concentradas en las
   opciones falsas: la regla de descarte más conocida de los concursos.
3. Opciones que llevan su propia justificación («porque…», «ya que…»): solo
   la correcta suele tenerla, y eso la delata.
4. Casos demasiado cortos para ser de juicio situacional.

Uso: python3 scripts/validar_banco.py [archivo.json ...]
"""
import json
import pathlib
import re
import statistics
import sys

ABSOLUTOS = re.compile(
    r"\b(siempre|nunca|jam[áa]s|todos?|todas?|ninguno|ninguna|"
    r"de plano|absolutamente|en ning[úu]n caso|cualquier cosa)\b",
    re.I,
)
JUSTIFICA = re.compile(r"\b(porque|ya que|puesto que|dado que|debido a que)\b", re.I)

# Umbrales. El banco tiene que pasarlos para publicarse.
MAX_CORRECTA_MAS_LARGA = 0.45   # con tres opciones, el azar da 33 %
RATIO_LARGO = (0.80, 1.25)      # largo medio correcta / largo medio falsas
MAX_ABS_SESGO = 0.15            # diferencia de absolutos entre falsas y correctas
MIN_CTX = 180                   # caracteres mínimos del caso
MIN_CTX_MEDIA = 260             # promedio mínimo del caso de juicio situacional

# En lectura crítica y razonamiento cuantitativo el estímulo es el texto o los
# datos, no un caso laboral, y alargarlos solo agregaría relleno. Esos ejes se
# miden contra el mínimo por pregunta, no contra el promedio.
EJES_BREVES = {"Lectura crítica", "Razonamiento cuantitativo"}
OPCIONES = 3                    # formato oficial PJS de la CNSC: A, B y C
MAX_POSICION = 0.45             # ninguna letra puede concentrar más
MAX_RACHA = 3                   # ni repetirse más veces seguidas


def validar(ruta: pathlib.Path) -> list[str]:
    banco = json.loads(ruta.read_text(encoding="utf-8"))
    n = len(banco)
    fallos = []

    distintas = {len(q["ops"]) for q in banco}
    if distintas != {OPCIONES}:
        fallos.append(
            f"el formato oficial de juicio situacional usa {OPCIONES} opciones; "
            f"este banco tiene {sorted(distintas)}"
        )

    posiciones = [q["correcta"] for q in banco]
    for letra in range(max(posiciones) + 1):
        cuota = posiciones.count(letra) / n
        if cuota > MAX_POSICION:
            fallos.append(
                f"la letra {chr(65 + letra)} concentra el {cuota:.0%} de las respuestas correctas"
            )
    racha = maxima = 1
    for a, b in zip(posiciones, posiciones[1:]):
        racha = racha + 1 if a == b else 1
        maxima = max(maxima, racha)
    if maxima > MAX_RACHA:
        fallos.append(f"hay {maxima} respuestas correctas seguidas en la misma letra")

    largo_ok = [len(q["ops"][q["correcta"]]) for q in banco]
    largo_mal = [len(o) for q in banco for i, o in enumerate(q["ops"]) if i != q["correcta"]]
    if not largo_mal:
        return fallos
    ratio = statistics.mean(largo_ok) / statistics.mean(largo_mal)

    def unica_mas_larga(q):
        largos = sorted((len(o) for o in q["ops"]), reverse=True)
        return len(q["ops"][q["correcta"]]) == largos[0] > largos[1]

    mas_larga = sum(1 for q in banco if unica_mas_larga(q))
    if mas_larga / n > MAX_CORRECTA_MAS_LARGA:
        fallos.append(
            f"la opción correcta es la más larga en {mas_larga} de {n} preguntas "
            f"({mas_larga * 100 // n} %); el máximo admitido es {int(MAX_CORRECTA_MAS_LARGA * 100)} %"
        )
    if not RATIO_LARGO[0] <= ratio <= RATIO_LARGO[1]:
        fallos.append(
            f"la opción correcta mide {ratio:.2f} veces lo que miden las falsas "
            f"({statistics.mean(largo_ok):.0f} contra {statistics.mean(largo_mal):.0f} caracteres)"
        )

    abs_ok = sum(1 for q in banco if ABSOLUTOS.search(q["ops"][q["correcta"]])) / n
    abs_mal = sum(
        1 for q in banco for i, o in enumerate(q["ops"]) if i != q["correcta"] and ABSOLUTOS.search(o)
    ) / (n * (OPCIONES - 1))
    if abs_mal - abs_ok > MAX_ABS_SESGO:
        fallos.append(
            f"palabras absolutas concentradas en las opciones falsas "
            f"({abs_mal:.0%} de las falsas contra {abs_ok:.0%} de las correctas)"
        )

    just_ok = sum(1 for q in banco if JUSTIFICA.search(q["ops"][q["correcta"]])) / n
    just_mal = sum(
        1 for q in banco for i, o in enumerate(q["ops"]) if i != q["correcta"] and JUSTIFICA.search(o)
    ) / (n * (OPCIONES - 1))
    if just_ok - just_mal > MAX_ABS_SESGO:
        fallos.append(
            f"la opción correcta lleva su propia justificación más a menudo que las falsas "
            f"({just_ok:.0%} contra {just_mal:.0%}); la justificación va en la explicación"
        )

    cortos = [q["tema"] for q in banco if len(q["ctx"]) < MIN_CTX]
    if cortos:
        fallos.append(f"{len(cortos)} casos por debajo de {MIN_CTX} caracteres, p. ej. «{cortos[0]}»")

    situacionales = [q for q in banco if q["refT"] not in EJES_BREVES]
    media_ctx = statistics.mean(len(q["ctx"]) for q in situacionales)
    if media_ctx < MIN_CTX_MEDIA:
        fallos.append(
            f"los casos de juicio situacional promedian {media_ctx:.0f} caracteres; el mínimo es {MIN_CTX_MEDIA}"
        )

    return fallos


def main():
    rutas = [pathlib.Path(a) for a in sys.argv[1:]] or sorted(
        (pathlib.Path(__file__).resolve().parent.parent / "data" / "simulacros-pago").glob("*.json")
    )
    total = 0
    for ruta in rutas:
        fallos = validar(ruta)
        if fallos:
            total += len(fallos)
            print(f"\n{ruta.stem}")
            for f in fallos:
                print(f"  ✗ {f}")
        else:
            print(f"{ruta.stem}: sin pistas detectadas")
    if total:
        print(f"\n{total} problemas de calidad. El banco no está listo para venderse.")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
