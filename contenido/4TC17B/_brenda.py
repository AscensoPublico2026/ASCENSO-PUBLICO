# -*- coding: utf-8 -*-
"""Piezas compartidas del curso Técnico en Criminalística 4TC-17 (Conv. 285-2026).

base(ruta, extra=None) -> SEC listas para usar: toma las secciones de una guía base
genérica de gestión humana, le añade (si se pasa) un módulo propio al Desarrollo y
aplica el reenfoque de identidad al cargo y a la dependencia de Brenda.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _lib import secciones_mapeadas, aplicar_todas, limpieza_rol

CARGO = 'Técnico en Criminalística'
PLURAL = 'Técnicos en Criminalística'

# la guía base está escrita para un «Gestor I» de una seccional de la DIAN
IDENTIDAD = [
    ('una Dirección Seccional de la DIAN', 'la División de Gestión Humana de la Procuraduría General de la Nación'),
    ('la Dirección Seccional de la DIAN', 'la División de Gestión Humana de la Procuraduría General de la Nación'),
    ('Dirección Seccional de la DIAN', 'División de Gestión Humana de la Procuraduría General de la Nación'),
    ('de la DIAN', 'de la Procuraduría'),
    ('la DIAN', 'la Procuraduría'),
    ('DIAN', 'Procuraduría General de la Nación'),
    ('Gestor I del área de Talento Humano', 'Técnico en Criminalística 4TC-17 de la División de Gestión Humana'),
    ('Gestor I del proceso de Talento Humano', 'Técnico en Criminalística 4TC-17 del proceso de Talento Humano'),
    ('Gestor I de Talento Humano', 'Técnico en Criminalística 4TC-17'),
    ('Gestor I', 'Técnico en Criminalística 4TC-17'),
    ('la Seccional', 'la División'),
    ('Seccional', 'División'),
    # La denominación del empleo es gramaticalmente masculina («el Técnico en
    # Criminalística»), aunque la aspirante sea mujer. Mezclar las dos formas
    # se lee como un descuido, así que se unifica.
    ('La Técnico en Criminalística', 'El Técnico en Criminalística'),
    ('la Técnico en Criminalística', 'el Técnico en Criminalística'),
    ('una Técnico en Criminalística', 'un Técnico en Criminalística'),
]

# aviso que se repite en todo el bloque de talento humano: la PGN tiene carrera especial
AVISO_CARRERA = (
    '<div class="ojo"><b>Ojo en la prueba:</b> lo que sigue es el <strong>régimen general</strong> del '
    'empleo público (Ley 909 de 2004 y Decreto 1083 de 2015), que debes dominar porque el formato de '
    'convocatoria lo exige. Pero recuerda lo del Día 14: la PGN tiene <mark>carrera especial</mark> '
    '(art. 279 de la Constitución y Decretos Ley 262, 263 y 264 de 2000) y <mark>administra su propio '
    'concurso y su propia carrera</mark>: no la CNSC. Antes de responder, mira siempre de qué entidad '
    'habla el caso.</div>\n'
)


def base(ruta, extra=None, aviso=True):
    SEC = secciones_mapeadas(ruta)
    if aviso:
        SEC[2] = AVISO_CARRERA + SEC[2]
    if extra:
        SEC[2] = SEC[2] + extra
    SEC = aplicar_todas(SEC, IDENTIDAD, estricto=False)
    SEC = aplicar_todas(SEC, limpieza_rol(CARGO, PLURAL), estricto=False)
    return SEC


def meta(**kw):
    """META con los datos fijos del curso ya puestos."""
    d = dict(cargo='Técnico en Criminalística 4TC-17 (Nivel Técnico)', conv='285-2026',
             badges=['⏱ 100-120 min', '👥 Talento humano', '📖 Específico'])
    d.update(kw)
    return d
