#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construye TODAS las guías que tengan contenido en motor/contenido/*.json.
Valida cada una y reporta un resumen. Un solo comando = toda la biblioteca.

Uso:
    python3 motor/construir_todas.py
"""
import os, glob
from construir_guia import construir

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    archivos = sorted(glob.glob(os.path.join(BASE_DIR, 'contenido', '*.json')))
    if not archivos:
        print('No hay archivos de contenido en motor/contenido/')
        return
    ok, fail = 0, 0
    for ruta in archivos:
        print('\n▶ %s' % os.path.basename(ruta))
        try:
            construir(ruta)
            ok += 1
        except SystemExit as e:
            print('  %s' % e)
            fail += 1
    print('\n=== Resumen: %d generadas, %d con errores ===' % (ok, fail))

if __name__ == '__main__':
    main()
