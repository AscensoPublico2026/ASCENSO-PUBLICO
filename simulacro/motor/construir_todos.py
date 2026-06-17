#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construye TODOS los simulacros que tengan contenido en contenido/*.json.
Valida cada uno y reporta un resumen. Un solo comando = todos los simulacros.

Uso:
    python3 motor/construir_todos.py
"""
import os
import glob
from construir_simulacro import construir

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(BASE_DIR)


def main():
    archivos = sorted(glob.glob(os.path.join(SIM_DIR, 'contenido', '*.json')))
    # Ignorar plantillas y archivos auxiliares (empiezan con "_")
    archivos = [a for a in archivos if not os.path.basename(a).startswith('_')]
    if not archivos:
        print('No hay archivos de contenido en contenido/')
        return
    ok, fail = 0, 0
    for ruta in archivos:
        print('\n> %s' % os.path.basename(ruta))
        try:
            construir(ruta)
            ok += 1
        except SystemExit as e:
            print('  %s' % e)
            fail += 1
    print('\n=== Resumen: %d generados, %d con errores ===' % (ok, fail))


if __name__ == '__main__':
    main()
