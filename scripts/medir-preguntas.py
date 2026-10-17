#!/usr/bin/env python3
"""Mide las preguntas del simulacro de una guía, tolerante a keys con o sin comillas.
Uso: medir-preguntas.py <archivo.html> [<archivo2.html> ...]"""
import re, sys

def grab_strings(segment):
    # captura 'texto' o "texto" respetando escapes
    return re.findall(r"'((?:[^'\\]|\\.)*)'|\"((?:[^\"\\]|\\.)*)\"", segment)

def medir(path):
    h = open(path, encoding='utf-8').read()
    m = re.search(r'const preguntas\s*=\s*(\[.*?\]);', h, re.S)
    if not m:
        print(f"{path}: SIN array const preguntas"); return
    blk = m.group(1)
    def field_lens(name):
        out=[]
        for mm in re.finditer(name+r"[\"']?\s*:\s*('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")", blk):
            out.append(len(mm.group(1))-2)
        return out
    ctxs = field_lens(r"[\"']?ctx")
    qs   = field_lens(r"[\"']?q")
    # ops y expl son arrays
    ops_arrays = re.findall(r"[\"']?ops[\"']?\s*:\s*\[(.*?)\]\s*,\s*[\"']?correcta", blk, re.S)
    expl_arrays= re.findall(r"[\"']?expl[\"']?\s*:\s*\[(.*?)\]\s*\}", blk, re.S)
    nops=[]; oplens=[]
    for o in ops_arrays:
        items=[ (a or b) for a,b in grab_strings(o)]
        nops.append(len(items)); oplens+=[len(i) for i in items]
    nexpl=[]
    for e in expl_arrays:
        items=[ (a or b) for a,b in grab_strings(e)]
        nexpl.append(len(items))
    correctas=[int(x) for x in re.findall(r"[\"']?correcta[\"']?\s*:\s*(\d+)", blk)]
    n=blk.count('ctx')
    print(f"\n=== {path.split('/')[-1]} ===")
    print(f"  nº preguntas (por ctx): {len(ctxs)} | nops set: {set(nops)} | nexpl set: {set(nexpl)} | correcta set: {sorted(set(correctas))}")
    if ctxs: print(f"  ctx: min {min(ctxs)} | <550: {sum(c<550 for c in ctxs)}")
    if qs:   print(f"  q  : min {min(qs)} | <230: {sum(c<230 for c in qs)} | <110: {sum(c<110 for c in qs)}")
    if oplens: print(f"  op : min {min(oplens)} | <150: {sum(c<150 for c in oplens)}")
    bad=[]
    if set(nops)-{3}: bad.append("NOPS!=3")
    if set(nexpl)-{3}: bad.append("NEXPL!=3")
    if ctxs and min(ctxs)<550: bad.append("ctx<550")
    if qs and min(qs)<230: bad.append("q<230")
    if oplens and min(oplens)<150: bad.append("op<150")
    if 'barajar([0,1,2,3])' in h: bad.append("barajar4")
    print("  RESULTADO:", "OK ✓" if not bad else "*** "+", ".join(bad))

for p in sys.argv[1:]:
    medir(p)
