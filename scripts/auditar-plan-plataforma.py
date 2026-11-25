#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audita cómo se VERÁ un plan en la plataforma, no solo el contenido de las guías.

`auditar-pgn.py` revisa el interior de cada guía. Este script revisa lo otro:
que la guía quede en el módulo correcto, en el orden correcto y con el día
correcto cuando el estudiante abre su ruta de estudio.

Comprueba, para cada plan:
  1. MÓDULO   El campo `biblioteca` de biblioteca.json es el que la plataforma
              traduce al enum `tipo_guia` (plataforma/lib/catalogoGuias.ts,
              mapTipoDB). Solo reconoce «Funcional», «Por Nivel», «Bonus» y
              «Simulacro Final»; cualquier otro valor cae en «general». Un
              valor como «Comportamental» o «Simulacro» manda la guía al
              módulo equivocado sin avisar.
  2. ORDEN    La plataforma ordena dentro de cada módulo por `orden ?? dia`
              (plataforma/lib/desbloqueo.ts, ordenDentro). Si el plan de
              autocargarGuias.ts pone `orden: 1` a una guía del día 4, esa
              guía se sube al principio del módulo.
  3. DÍA      El número de día del plan coincide con la insignia «📅 Día N de
              21», con el botón «Finalizar Día N» y con el kicker del HTML.
  4. ARCHIVO  Cada código del plan existe en la biblioteca, está «publicada»,
              su HTML existe en el repositorio y está sincronizado en
              plataforma/public/seed-guias/.
  5. ÚNICOS   No hay códigos repetidos ni posiciones de orden empatadas.

Uso:
    python3 scripts/auditar-plan-plataforma.py                 # todos los planes
    python3 scripts/auditar-plan-plataforma.py <plan-id> [...] # solo esos
    python3 scripts/auditar-plan-plataforma.py --arreglar <plan-id>
        corrige en biblioteca.json el campo `biblioteca` y en
        autocargarGuias.ts el `orden`, y deja el resto para revisión manual.
"""
import json, os, re, sys, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
BIB = 'biblioteca/biblioteca.json'
PLANES_TS = 'plataforma/lib/autocargarGuias.ts'
SEED = 'plataforma/public/seed-guias'

# plataforma/lib/catalogoGuias.ts · mapTipoDB()
MAPA_BIBLIOTECA = {
    'Funcional': 'funcional',
    'Simulacro Final': 'simulacro',
    'Bonus': 'bonus',
    'Por Nivel': 'nivel',
}
# qué valor de `biblioteca` corresponde a cada `tipo` que usamos al registrar
CORRECCION = {
    'comportamental': 'Por Nivel',
    'nivel': 'Por Nivel',
    'simulacro': 'Simulacro Final',
    'funcional': 'Funcional',
    'bonus': 'Bonus',
    'bienvenida': 'Introducción',
    'entidad': 'Introducción',
    'general': 'General',
}
# plataforma/lib/desbloqueo.ts · moduloKey()
ETIQUETA = {'introduccion': 'Introducción', 'generales': 'Conocimiento general',
            'nivel': 'Competencias / Por nivel', 'funcional': 'Funciones del Cargo',
            'bonus': 'Bonus', 'simulacro': 'Simulacro Final'}


def modulo_key(tipo_db, archivo, dia):
    if tipo_db == 'simulacro': return 'simulacro'
    if tipo_db == 'bonus': return 'bonus'
    if tipo_db == 'funcional': return 'funcional'
    if tipo_db == 'nivel': return 'nivel'
    if re.search(r'(^|/)(INTRO|ENT)-', archivo or '', re.I) or dia == 1: return 'introduccion'
    return 'generales'


def leer_planes():
    """Extrae de autocargarGuias.ts: {plan_id: [(codigo, dia, orden|None), ...]}."""
    s = open(PLANES_TS, encoding='utf-8').read()
    planes = {}
    for m in re.finditer(r'"([a-z0-9\-]+)":\s*\{\s*\n\s*id:\s*"\1",(.*?)\n  \},\n', s, re.S):
        pid, cuerpo = m.group(1), m.group(2)
        items = []
        for it in re.finditer(r'\{\s*codigo:\s*"([^"]+)",\s*dia:\s*(\d+|null)\s*(?:,\s*orden:\s*(\d+)\s*)?\}', cuerpo):
            cod = it.group(1)
            dia = None if it.group(2) == 'null' else int(it.group(2))
            orden = int(it.group(3)) if it.group(3) else None
            items.append((cod, dia, orden))
        if items:
            planes[pid] = items
    return planes


def dias_en_html(path):
    """Devuelve (dia_insignia, dia_boton, dia_kicker) leídos del HTML."""
    try:
        s = open(path, encoding='utf-8').read()
    except OSError:
        return (None, None, None)
    ins = re.search(r'📅\s*Día\s*(\d+)\s*de\s*21', s)
    bot = re.search(r'Finalizar\s+Día\s+(\d+)', s)
    kic = re.search(r'<div class="kicker">\s*Día\s*(\d+)', s)
    f = lambda m: int(m.group(1)) if m else None
    return (f(ins), f(bot), f(kic))


def auditar(plan_id, items, catalogo, hallazgos):
    por_cod = {g['codigo']: g for g in catalogo}
    vistos = collections.Counter(c for c, _, _ in items)
    for cod, n in vistos.items():
        if n > 1:
            hallazgos.append(('ALTO', plan_id, cod, f'el código aparece {n} veces en el plan'))

    filas = []
    for cod, dia, orden in items:
        g = por_cod.get(cod)
        if not g:
            hallazgos.append(('CRITICO', plan_id, cod, 'el código no existe en biblioteca.json'))
            continue
        bib = g.get('biblioteca')
        tipo_reg = (g.get('tipo') or '').lower()
        tipo_db = MAPA_BIBLIOTECA.get(bib, 'general')
        arch = g.get('archivo') or ''
        mod = modulo_key(tipo_db, arch, g.get('dia'))

        # 1. módulo
        esperado = CORRECCION.get(tipo_reg)
        mod_esperado = modulo_key(MAPA_BIBLIOTECA.get(esperado, 'general'), arch, g.get('dia')) if esperado else mod
        if bib not in MAPA_BIBLIOTECA and bib not in ('Introducción', 'General', 'Por Entidad'):
            # solo es crítico si además termina en un módulo distinto del que le toca
            sev = 'CRITICO' if mod != mod_esperado else 'MEDIO'
            detalle = (f' → cae en «{ETIQUETA[mod]}» y debería estar en «{ETIQUETA[mod_esperado]}»'
                       if mod != mod_esperado else f' (por suerte queda en «{ETIQUETA[mod]}», que es el correcto)')
            hallazgos.append((sev, plan_id, cod,
                f'«biblioteca»={bib!r} no lo reconoce la plataforma{detalle}'
                + (f'; usar {esperado!r}' if esperado and esperado != bib else '')))
        elif esperado and esperado != bib and tipo_reg not in ('bienvenida', 'entidad', 'general', 'funcional'):
            hallazgos.append(('ALTO', plan_id, cod,
                f'«biblioteca»={bib!r} no corresponde al tipo registrado {tipo_reg!r}'))

        # 4. estado y archivo
        if g.get('estado') != 'publicada':
            hallazgos.append(('CRITICO', plan_id, cod, f'estado={g.get("estado")!r}, la plataforma la omite'))
        if not arch or not os.path.exists(arch):
            hallazgos.append(('CRITICO', plan_id, cod, f'no existe el archivo {arch!r}'))
        elif not os.path.exists(os.path.join(SEED, os.path.basename(arch))):
            hallazgos.append(('ALTO', plan_id, cod,
                'el HTML no está en plataforma/public/seed-guias (falta sync-biblioteca.sh)'))

        # 3. día
        if dia is not None:
            if g.get('dia') != dia:
                hallazgos.append(('ALTO', plan_id, cod,
                    f'día del plan ({dia}) distinto del de la biblioteca ({g.get("dia")})'))
            ins, bot, kic = dias_en_html(arch) if arch else (None, None, None)
            for nombre, val in (('insignia 📅', ins), ('botón Finalizar', bot), ('kicker', kic)):
                if val is not None and val != dia:
                    hallazgos.append(('ALTO', plan_id, cod,
                        f'el HTML dice Día {val} en el {nombre} pero el plan lo pone en el día {dia}'))

        filas.append((mod, orden if orden is not None else (dia or 0), dia, cod))

    # 2. orden dentro de cada módulo
    for mod in sorted(set(f[0] for f in filas)):
        grupo = [f for f in filas if f[0] == mod]
        ordenados = sorted(grupo, key=lambda f: f[1])
        dias = [f[2] for f in ordenados if f[2] is not None]
        if dias != sorted(dias):
            secuencia = ' → '.join(f'd{f[2]}' for f in ordenados)
            hallazgos.append(('CRITICO', plan_id, ETIQUETA[mod],
                f'los días se muestran desordenados: {secuencia}'))
        empates = collections.defaultdict(list)
        for f in grupo:
            empates[f[1]].append(f)
        for v, gs in empates.items():
            if len(gs) < 2:
                continue
            dias_emp = sorted(set(f[2] for f in gs if f[2] is not None))
            if len(dias_emp) > 1:
                # el desempate lo decide la base de datos: los días salen en cualquier orden
                hallazgos.append(('CRITICO', plan_id, ETIQUETA[mod],
                    f'las guías de los días {", ".join(str(d) for d in dias_emp)} comparten la posición '
                    f'de orden {v}: la plataforma las muestra en orden arbitrario'))
            else:
                hallazgos.append(('MEDIO', plan_id, ETIQUETA[mod],
                    f'{len(gs)} guías del día {dias_emp[0] if dias_emp else "?"} comparten la posición {v}'))
    return filas


def arreglar(plan_id, items, catalogo):
    """Corrige el campo `biblioteca` y reescribe el `orden` del plan."""
    cambios = []
    por_cod = {g['codigo']: g for g in catalogo}
    for cod, _, _ in items:
        g = por_cod.get(cod)
        if not g: continue
        esperado = CORRECCION.get((g.get('tipo') or '').lower())
        if esperado and g.get('biblioteca') != esperado and g.get('biblioteca') not in MAPA_BIBLIOTECA \
           and g.get('biblioteca') not in ('Introducción', 'General', 'Por Entidad'):
            cambios.append(f'  {cod}: biblioteca {g["biblioteca"]!r} → {esperado!r}')
            g['biblioteca'] = esperado
    if cambios:
        d = json.load(open(BIB, encoding='utf-8'))
        idx = {g['codigo']: g for g in d['guias']}
        for g in catalogo:
            if g['codigo'] in idx and 'biblioteca' in g:
                idx[g['codigo']]['biblioteca'] = g['biblioteca']
        json.dump(d, open(BIB, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # orden explícito: día×10 (+1, +2… para varias guías del mismo día)
    s = open(PLANES_TS, encoding='utf-8').read()
    m = re.search(r'("%s":\s*\{\s*\n\s*id:\s*"%s",.*?\n  \},\n)' % (plan_id, plan_id), s, re.S)
    if m:
        bloque = m.group(1)
        sub = collections.Counter()
        nuevo = bloque
        for cod, dia, _ in items:
            if dia is None: continue
            k = dia * 10 + sub[dia]; sub[dia] += 1
            viejo = re.search(r'\{\s*codigo:\s*"%s",\s*dia:\s*%d\s*(?:,\s*orden:\s*\d+\s*)?\}' % (re.escape(cod), dia), nuevo)
            if viejo:
                nuevo = nuevo.replace(viejo.group(0), '{ codigo: "%s", dia: %d, orden: %d }' % (cod, dia, k), 1)
        if nuevo != bloque:
            open(PLANES_TS, 'w', encoding='utf-8').write(s.replace(bloque, nuevo, 1))
            cambios.append(f'  orden explícito (día×10) para las {len(items)} guías del plan')
    return cambios


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    modo_arreglo = '--arreglar' in sys.argv
    catalogo = json.load(open(BIB, encoding='utf-8'))['guias']
    planes = leer_planes()
    objetivo = args or sorted(planes)
    faltan = [p for p in objetivo if p not in planes]
    for p in faltan:
        print(f'⚠️  no se encontró el plan {p!r} en {PLANES_TS}')
    objetivo = [p for p in objetivo if p in planes]

    if modo_arreglo:
        for p in objetivo:
            cambios = arreglar(p, planes[p], catalogo)
            print(f'== {p}: {len(cambios)} corrección(es)')
            for c in cambios: print(c)
        print('\nVuelve a ejecutar sin --arreglar para verificar, y corre scripts/sync-biblioteca.sh')
        return 0

    hallazgos = []
    for p in objetivo:
        auditar(p, planes[p], catalogo, hallazgos)
    sev = collections.Counter(h[0] for h in hallazgos)
    print(f'Planes auditados: {len(objetivo)} · CRITICO {sev["CRITICO"]} · ALTO {sev["ALTO"]} · MEDIO {sev["MEDIO"]}')
    for s in ('CRITICO', 'ALTO', 'MEDIO'):
        for h in [x for x in hallazgos if x[0] == s]:
            print(f'  [{h[0]}] {h[1]} · {h[2]}: {h[3]}')
    return 1 if sev['CRITICO'] else 0


if __name__ == '__main__':
    sys.exit(main())
