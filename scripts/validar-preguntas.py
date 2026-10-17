#!/usr/bin/env python3
"""Valida el estandar de preguntas de juicio situacional de una guia/simulacro.
Extrae `const preguntas=[...]` (claves JS sin comillas) y mide ctx, q, ops.
Uso: validar-preguntas.py ARCHIVO.html [--sim]
Umbrales: 0 ctx<550, 0 q<110, 0 ops<150. Con --sim exige mas intensidad.
"""
import sys, re, json, statistics

def js_array_to_json(s):
    # añade comillas a las claves tipo  nivel:  tema:  ctx:  q:  ops:  correcta:  expl:  ref:  refT:
    s = re.sub(r'([{,]\s*)([a-zA-Z_][a-zA-Z0-9_]*)\s*:', r'\1"\2":', s)
    return s

def main():
    if len(sys.argv) < 2:
        print("uso: validar-preguntas.py ARCHIVO [--sim]"); sys.exit(2)
    f = sys.argv[1]
    sim = '--sim' in sys.argv
    h = open(f, encoding='utf-8').read()
    m = re.search(r'const\s+preguntas\s*=\s*(\[.*?\])\s*;', h, re.S)
    if not m:
        print("FAIL: no se encontro `const preguntas=[...]`"); sys.exit(1)
    raw = m.group(1)
    try:
        arr = json.loads(js_array_to_json(raw))
    except Exception as e:
        print("FAIL: no se pudo parsear el array:", e); sys.exit(1)
    ctx = [len(p.get('ctx','')) for p in arr]
    q   = [len(p.get('q','')) for p in arr]
    ops = [len(o) for p in arr for o in p.get('ops',[])]
    nops= set(len(p.get('ops',[])) for p in arr)
    corr= [p.get('correcta') for p in arr]
    bad_ctx = sum(1 for c in ctx if c < 550)
    bad_q   = sum(1 for x in q if x < 110)
    bad_ops = sum(1 for o in ops if o < 150)
    # aperturas variadas
    aperturas = [p.get('ctx','')[:22].lower() for p in arr]
    rep = len(aperturas) - len(set(aperturas))
    print(f"ARCHIVO: {f}  {'[SIMULACRO]' if sim else ''}")
    print(f"  N={len(arr)}  nops={nops}  correctas distrib={ {i:corr.count(i) for i in sorted(set(corr))} }")
    print(f"  ctx  min={min(ctx)} prom={int(statistics.mean(ctx))} max={max(ctx)}  (<550: {bad_ctx})")
    print(f"  q    min={min(q)} prom={int(statistics.mean(q))} max={max(q)}  (<110: {bad_q})")
    print(f"  ops  min={min(ops)} prom={int(statistics.mean(ops))} max={max(ops)}  (<150: {bad_ops})")
    print(f"  aperturas repetidas (primeros 22 car): {rep}")
    ok = (bad_ctx==0 and bad_q==0 and bad_ops==0 and nops=={3})
    if sim:
        # simulacro: exigir mas (contexto prom >=640, q prom >=300)
        if statistics.mean(ctx) < 620 or statistics.mean(q) < 290:
            print("  WARN sim: contexto/enunciado promedio por debajo del nivel del simulacro final")
    print("RESULTADO:", "OK" if ok else "FALLA (hay preguntas bajo umbral)")
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
