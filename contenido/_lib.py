# -*- coding: utf-8 -*-
"""Utilidades para los archivos de contenido de las guías PGN.

secciones(path)  -> {0: html, 1: html, …} con el interior de cada <section data-sec="n">.
aplicar(html, R) -> aplica una lista de reemplazos [(viejo, nuevo), …] y avisa si alguno no estaba.
falta(html, R)   -> lista los reemplazos que no se encontraron (para depurar sin escribir).
"""
import re, sys


def secciones(path):
    s = open(path, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'<section class="section[^"]*" data-sec="(\d+)">(.*?)\n</section>', s, re.S):
        out[int(m.group(1))] = m.group(2).strip('\n')
    return out


def falta(texto, R):
    return [a for a, _ in R if a not in texto]


def aplicar(texto, R, estricto=True, etiqueta=''):
    f = falta(texto, R)
    if f:
        print(f'⚠️  {etiqueta}: {len(f)} reemplazo(s) sin coincidencia:', file=sys.stderr)
        for x in f:
            print('    -', x[:110].replace('\n', ' '), file=sys.stderr)
        if estricto:
            raise SystemExit(1)
    for a, b in R:
        texto = texto.replace(a, b)
    return texto


def aplicar_todas(SEC, R, estricto=False):
    """Aplica los reemplazos sobre todas las secciones; exige que cada uno aparezca al menos una vez."""
    usados = {a: False for a, _ in R}
    for n in SEC:
        for a, b in R:
            if a in SEC[n]:
                usados[a] = True
                SEC[n] = SEC[n].replace(a, b)
    sin = [a for a, u in usados.items() if not u]
    if sin:
        print(f'⚠️  {len(sin)} reemplazo(s) sin coincidencia en ninguna sección:', file=sys.stderr)
        for x in sin:
            print('    -', x[:110].replace('\n', ' '), file=sys.stderr)
        if estricto:
            raise SystemExit(1)
    return SEC


def secciones_mapeadas(path, mapa=None):
    """Devuelve las secciones renumeradas al molde de 10 secciones (0-8 de contenido).
    Por defecto convierte el molde de 11 secciones (8 = flashcards, 9 = resumen, 10 = simulacro)."""
    S = secciones(path)
    if mapa is None:
        mapa = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 9: 8} if 10 in S else {n: n for n in range(9)}
    return {dst: S[src] for src, dst in mapa.items() if src in S}


def limpieza_rol(cargo='Técnico Investigador', plural='Técnicos Investigadores'):
    """Reemplazos de seguridad: borra todo rastro del cargo de la guía de origen
    (auxiliar / secretarial / ventanilla / sustanciador) y arregla la concordancia
    que esos reemplazos pueden romper. Se aplica SIEMPRE con estricto=False,
    después de los reemplazos de contenido, como último filtro antifugas.
    No toca 'Procuraduría Auxiliar para Asuntos Disciplinarios' (dependencia real)."""
    return [
        # proteger nombres propios de dependencias
        ('Procuraduría Auxiliar', '@@PAUX@@'),
        # cargos ajenos
        ('auxiliares administrativos', plural), ('auxiliares', plural),
        ('Auxiliares', plural), ('auxiliar administrativo', cargo),
        ('auxiliar', cargo), ('Auxiliar', cargo),
        ('apoyo secretarial', 'apoyo técnico'), ('secretarial', 'técnico'),
        ('profesional sustanciador', '@@PSUST@@'),
        ('Sustanciadores', plural), ('Sustanciadora', cargo), ('Sustanciador', cargo),
        ('@@PSUST@@', 'profesional sustanciador'),
        ('ventanillas', 'puntos de atención'), ('ventanilla', 'punto de atención'),
        ('Secretaria Procuraduría', cargo), ('Secretario Procuraduría', cargo),
        ('Secretarias', plural), ('Secretarios', plural),
        ('Secretaria', cargo), ('Secretario', cargo),
        # concordancia que los reemplazos anteriores pueden romper
        ('la punto de atención', 'el punto de atención'),
        ('una punto de atención', 'un punto de atención'),
        ('las puntos de atención', 'los puntos de atención'),
        ('unas puntos de atención', 'unos puntos de atención'),
        ('una ' + cargo, 'un ' + cargo), ('la ' + cargo + ' ', 'el ' + cargo + ' '),
        ('Una ' + cargo, 'Un ' + cargo),
        ('ti misma', 'ti mismo'), ('tú misma', 'tú mismo'), ('usted misma', 'usted mismo'),
        # restituir nombres propios
        ('@@PAUX@@', 'Procuraduría Auxiliar'),
    ]


def modulos(html):
    """Parte el HTML de una sección de Desarrollo en (encabezado, [(n_h3, html_del_modulo), …]).

    Sirve para repartir los módulos de una guía base entre dos guías nuevas sin duplicar
    contenido: `cabeza, mods = modulos(SEC[2])` y luego se arma cada guía con los que le tocan.
    """
    import re as _re
    cortes = [m.start() for m in _re.finditer(r'(?:<!--\s*M[ÓO]DULO[^>]*-->\s*)?<h3[ >]', html)]
    if not cortes:
        return html, []
    cabeza = html[:cortes[0]]
    partes = []
    for i, ini in enumerate(cortes):
        fin = cortes[i + 1] if i + 1 < len(cortes) else len(html)
        partes.append((i + 1, html[ini:fin]))
    return cabeza, partes


def armar(cabeza, partes, cuales, renumerar=True):
    """Reconstruye una sección de Desarrollo con los módulos elegidos, renumerando los chips."""
    import re as _re
    elegidos = [p for n, p in partes if n in cuales]
    if renumerar:
        out = []
        for i, p in enumerate(elegidos, 1):
            p = _re.sub(r'<span class="h3-chip">[^<]*</span>', f'<span class="h3-chip">{i}</span>', p, count=1)
            out.append(p)
        elegidos = out
    return cabeza + ''.join(elegidos)
