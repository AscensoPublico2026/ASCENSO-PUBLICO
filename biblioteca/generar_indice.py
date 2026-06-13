#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera BIBLIOTECA.md (índice legible) a partir de biblioteca.json (fuente de verdad).

Uso:
    python3 biblioteca/generar_indice.py

Cada vez que registres o publiques una guía: edita biblioteca.json y ejecuta este script.
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(BASE, "biblioteca.json")
OUT = os.path.join(BASE, "BIBLIOTECA.md")

EMOJI = {"publicada": "✅", "pendiente": "⬜", "bajo-demanda": "🔁"}
ETIQUETA = {"publicada": "Publicada", "pendiente": "Pendiente", "bajo-demanda": "Bajo demanda"}
ORDEN_BIBLIOTECA = ["Introducción", "General", "Por Nivel", "Funcional", "Por Entidad", "Bonus", "Simulacro Final"]


def dia_str(g):
    d = g.get("dia")
    return str(d) if d is not None else "—"


def link(g):
    if g.get("archivo"):
        return f"[`{g['codigo']}`](../{g['archivo']})"
    return f"`{g['codigo']}`"


def main():
    with open(JSON, encoding="utf-8") as f:
        data = json.load(f)

    guias = data["guias"]
    total = len(guias)
    publicadas = sum(1 for g in guias if g["estado"] == "publicada")

    L = []
    L.append("<!-- ARCHIVO GENERADO AUTOMÁTICAMENTE desde biblioteca.json -->")
    L.append("<!-- No edites este archivo a mano: edita biblioteca.json y ejecuta generar_indice.py -->")
    L.append("")
    L.append("# 📚 Biblioteca de Guías — Ascenso Público")
    L.append("")
    L.append(f"> {data['descripcion']}")
    L.append("")
    L.append(f"**Versión:** {data['version']} · **Actualizado:** {data['actualizado']} · "
             f"**Guías registradas:** {total} · **Publicadas:** {publicadas} ✅")
    L.append("")
    L.append("> 🧱 **Cómo está organizada:** la fuente de verdad es `biblioteca.json`. "
             "Este índice (`BIBLIOTECA.md`) se genera con `generar_indice.py`. "
             "Para añadir o publicar una guía, edita el JSON y regenera el índice.")
    L.append("")

    # --- Resumen general ---
    L.append("## 🗂️ Resumen general")
    L.append("")
    L.append("| Estado | Día | Código | Guía | Biblioteca | Nivel |")
    L.append("|:--:|:--:|---|---|---|---|")
    for g in sorted(guias, key=lambda x: (ORDEN_BIBLIOTECA.index(x["biblioteca"]) if x["biblioteca"] in ORDEN_BIBLIOTECA else 99,
                                          x["dia"] if x["dia"] is not None else 99,
                                          x["codigo"])):
        L.append(f"| {EMOJI.get(g['estado'],'')} | {dia_str(g)} | {link(g)} | {g['titulo']} | "
                 f"{g['biblioteca']} | {g.get('nivel') or '—'} |")
    L.append("")
    L.append(f"**Leyenda:** {EMOJI['publicada']} Publicada · {EMOJI['pendiente']} Pendiente · {EMOJI['bajo-demanda']} Bajo demanda (se crea con la compra)")
    L.append("")

    # --- Detalle por biblioteca ---
    L.append("## 📖 Detalle por categoría y temas")
    L.append("")
    presentes = [b for b in ORDEN_BIBLIOTECA if any(g["biblioteca"] == b for g in guias)]
    for b in presentes:
        L.append(f"### {b}")
        L.append("")
        grupo = [g for g in guias if g["biblioteca"] == b]
        # agrupar por nivel si aplica
        niveles = [n for n in ["Asistencial", "Técnico", "Profesional"] if any(g.get("nivel") == n for g in grupo)]
        sin_nivel = [g for g in grupo if not g.get("nivel")]

        def bloque(items):
            items = sorted(items, key=lambda x: (x["dia"] if x["dia"] is not None else 99, x["codigo"]))
            for g in items:
                cab = f"#### {EMOJI.get(g['estado'],'')} {g['codigo']} · {g['titulo']}"
                L.append(cab)
                meta = []
                meta.append(f"**Día:** {dia_str(g)}")
                meta.append(f"**Estado:** {ETIQUETA.get(g['estado'], g['estado'])}")
                if g.get("simulacro"):
                    meta.append("**Simulacro:** sí")
                if g.get("reutilizable"):
                    meta.append("**Reutilizable:** sí")
                if g.get("archivo"):
                    meta.append(f"**Archivo:** [`{g['archivo']}`](../{g['archivo']})")
                if g.get("aplica_a"):
                    meta.append(f"**Aplica a:** {g['aplica_a']}")
                L.append(" · ".join(meta))
                L.append("")
                L.append("Temas:")
                for t in g["temas"]:
                    L.append(f"- {t}")
                if g.get("nota"):
                    L.append("")
                    L.append(f"> ℹ️ {g['nota']}")
                L.append("")

        if niveles:
            for n in niveles:
                L.append(f"#### 🪜 Nivel {n}")
                L.append("")
                bloque([g for g in grupo if g.get("nivel") == n])
            if sin_nivel:
                bloque(sin_nivel)
        else:
            bloque(grupo)

    # --- Marco de competencias ---
    mc = data.get("marco_competencias_dec_815_2018")
    if mc:
        L.append("## ⚖️ Marco de competencias comportamentales (referencia)")
        L.append("")
        L.append(f"> Fuente: {mc['fuente']}")
        L.append("")
        L.append("**Comunes a todos los niveles:** " + " · ".join(mc["comunes_todos_los_niveles"]) + ".")
        L.append("")
        for nivel, comps in mc["especificas_por_nivel"].items():
            L.append(f"- **{nivel}:** " + " · ".join(comps) + ".")
        L.append("")
        L.append(f"**Formato de prueba:** {mc['formato_prueba']}")
        L.append("")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"OK -> {OUT} ({total} guías, {publicadas} publicadas)")


if __name__ == "__main__":
    main()
