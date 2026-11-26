#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprueba, guía por guía, que los DATOS DUROS del cargo sean los de su convocatoria.

Por qué existe: las guías se construyen reutilizando guías de otros cargos. Los
reemplazos de identidad cambian el nombre del empleo y el número de la
convocatoria, pero NO las cifras que viven dentro de las frases: el número de
plazas, la asignación básica, los requisitos de estudio. Así fue como una guía
de este curso terminó diciendo «39 plazas» y «$3.120.457», que son del curso de
Citador, y otra «9 plazas» y «$6.889.867», que son del Técnico Investigador.

La fuente de verdad es referencias/pgn/fichas-cargo.json, que se llena
copiando el formato de convocatoria ANTES de escribir la primera guía.

Revisa en cada guía del plan:
  · toda cifra de dinero         → debe ser la asignación básica de la ficha
  · todo «N plazas/cargos»       → debe coincidir con el número de cargos
  · todo código de empleo        → debe ser el código del cargo (4TC-17, …)
  · todo número de convocatoria  → debe ser el de la ficha
  · nombres de OTROS cargos de la PGN y de otras entidades del catálogo
  · requisitos de estudio de otro cargo («educación básica secundaria», …)
  · el proceso y la dependencia

Uso:
    python3 scripts/auditar-ficha-cargo.py <plan-id> [...]
    python3 scripts/auditar-ficha-cargo.py            # todos los que tengan ficha
"""
import json, os, re, sys, glob, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
FICHAS = 'referencias/pgn/fichas-cargo.json'
BIB = 'biblioteca/biblioteca.json'

# denominaciones de empleo que aparecen en el catálogo de cursos
OTROS_CARGOS = [
    'Citador', 'Sustanciador', 'Secretario Procuraduría', 'Secretaria Procuraduría',
    'Auxiliar Administrativo', 'Técnico Investigador', 'Técnico Administrativo',
    'Profesional Universitario', 'Asesor de Despacho', 'Gestor I', 'Gestor II',
    'Gestor III', 'Analista I', 'Analista II', 'Analista IV', 'Facilitador II',
]
OTRAS_ENTIDADES = ['DIAN', 'Dirección de Impuestos y Aduanas']
# requisitos que delatan otro cargo
REQ_AJENOS = [
    'educación básica secundaria', 'bachiller', 'título profesional universitario',
    'tarjeta profesional', 'posgrado en la modalidad',
]


def texto_visible(html):
    s = re.sub(r'<script[\s\S]*?</script>', ' ', html)
    s = re.sub(r'<style[\s\S]*?</style>', ' ', s)
    return re.sub(r'<[^>]+>', ' ', s)


def guias_del_plan(plan_id):
    d = json.load(open(BIB, encoding='utf-8'))['guias']
    return [g for g in d if g.get('plan') == plan_id and g.get('archivo')]


def auditar(plan_id, ficha, hallazgos):
    cod = ficha['codigo']
    conv = ficha['convocatoria']
    salario = ficha.get('asignacion_basica')
    cargos = ficha.get('numero_cargos')
    denom = ficha.get('denominacion', '')
    guias = guias_del_plan(plan_id)
    if not guias:
        hallazgos.append(('ALTO', plan_id, '(plan)', 'no hay guías registradas con este plan en biblioteca.json'))
        return
    for g in guias:
        arch = g['archivo']
        nombre = os.path.basename(arch)
        if not os.path.exists(arch):
            hallazgos.append(('CRITICO', plan_id, nombre, 'el archivo no existe'))
            continue
        html = open(arch, encoding='utf-8').read()
        txt = texto_visible(html)

        # 1. dinero
        if salario:
            for m in set(re.findall(r'\$\s?([0-9]{1,3}(?:[.,][0-9]{3})+)', txt)):
                if m.replace(',', '.') != salario:
                    hallazgos.append(('CRITICO', plan_id, nombre,
                        f'cifra de dinero ${m} — la asignación básica del cargo es ${salario}'))
        # 2. plazas
        if cargos is not None:
            for m in set(re.findall(r'\b(\d{1,3})\s+(plazas?|cargos ofertados?|vacantes?)\b', txt, re.I)):
                if int(m[0]) != cargos:
                    hallazgos.append(('CRITICO', plan_id, nombre,
                        f'«{m[0]} {m[1]}» — la convocatoria ofrece {cargos}'))
            for pal in ('nueve plazas', 'tres plazas', 'dos plazas', 'cuatro plazas', 'cinco plazas'):
                if pal in txt.lower() and cargos != {'nueve': 9, 'tres': 3, 'dos': 2, 'cuatro': 4, 'cinco': 5}[pal.split()[0]]:
                    hallazgos.append(('CRITICO', plan_id, nombre, f'«{pal}» — la convocatoria ofrece {cargos}'))
        # 3. códigos de empleo
        for m in set(re.findall(r'\b([0-9][A-Z]{2}-?[0-9]{2})\b', txt)):
            if m.replace('-', '') != cod.replace('-', ''):
                hallazgos.append(('CRITICO', plan_id, nombre,
                    f'código de empleo ajeno «{m}» — el cargo es {cod}'))
        # 4. convocatorias
        for m in set(re.findall(r'\bConvocatoria\s+(?:N\.?o?\.?\s*)?(\d{2,3}-20\d\d)\b', txt, re.I)):
            if m != conv:
                hallazgos.append(('CRITICO', plan_id, nombre,
                    f'convocatoria ajena «{m}» — la del curso es {conv}'))
        # 5. otros cargos y entidades
        for c in OTROS_CARGOS:
            if c.lower() in denom.lower():
                continue
            n = len(re.findall(r'\b' + re.escape(c) + r'\b', txt))
            if n:
                hallazgos.append(('CRITICO', plan_id, nombre, f'menciona el cargo ajeno «{c}» ({n} vez/veces)'))
        for e in OTRAS_ENTIDADES:
            n = len(re.findall(r'\b' + re.escape(e) + r'\b', txt))
            if n:
                hallazgos.append(('ALTO', plan_id, nombre, f'menciona la entidad ajena «{e}» ({n} vez/veces)'))
        # 6. requisitos de otro cargo
        for r in REQ_AJENOS:
            if r in txt.lower() and r not in (ficha.get('estudio', '') + ficha.get('experiencia', '')).lower():
                hallazgos.append(('ALTO', plan_id, nombre, f'requisito ajeno al cargo: «{r}»'))
        # 7. dependencia y proceso
        dep = ficha.get('dependencia')
        if dep and 'DNIE' in txt and 'no ' not in txt[max(0, txt.find('DNIE') - 60):txt.find('DNIE')].lower():
            pass  # mencionar la DNIE para contrastarla es legítimo; se revisa a mano
        proc = ficha.get('proceso')
        if proc:
            for m in re.finditer(r'vinculad[ao]s? al (?:proceso )?<?[a-z]*>?\s*([A-Za-zÁÉÍÓÚáéíóúñ ]{3,30})', txt):
                if proc.lower() not in m.group(1).lower():
                    hallazgos.append(('ALTO', plan_id, nombre,
                        f'dice que el cargo está vinculado a «{m.group(1).strip()}» — el proceso es {proc}'))


def main():
    fichas = json.load(open(FICHAS, encoding='utf-8'))
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    planes = args or [k for k in fichas if not k.startswith('_')]
    hallazgos = []
    for p in planes:
        f = fichas.get(p)
        if not f:
            print(f'⚠️  no hay ficha para {p!r} en {FICHAS}')
            continue
        auditar(p, f, hallazgos)
    sev = collections.Counter(h[0] for h in hallazgos)
    print(f'Planes con ficha auditados: {len(planes)} · CRITICO {sev["CRITICO"]} · ALTO {sev["ALTO"]}')
    for s in ('CRITICO', 'ALTO'):
        for h in [x for x in hallazgos if x[0] == s]:
            print(f'  [{h[0]}] {h[2]}: {h[3]}')
    return 1 if sev['CRITICO'] else 0


if __name__ == '__main__':
    sys.exit(main())
