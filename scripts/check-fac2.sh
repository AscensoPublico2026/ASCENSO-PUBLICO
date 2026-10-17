#!/usr/bin/env bash
# Validación rápida de una guía del curso Facilitador II DIAN.
# Uso: bash scripts/check-fac2.sh <archivo.html> "Día N" [--intro]
cd "$(dirname "$0")/.." || exit 1
F="$1"; DIA="$2"; INTRO="$3"
NODE=$(ls ~/.nvm/versions/node/*/bin/node 2>/dev/null | tail -1)
PY=.venv/bin/python3
[ -f "$F" ] || { echo "NO EXISTE: $F"; exit 1; }
"$PY" - "$F" "$INTRO" <<'PYEOF'
import re,sys,statistics
f=sys.argv[1]; intro=(len(sys.argv)>2 and sys.argv[2]=='--intro')
h=open(f,encoding='utf-8').read()
scripts=re.findall(r'<script>(.*?)</script>',h,re.S)
open('/tmp/jcheck.js','w').write("\n".join(scripts))
do=len(re.findall(r'<div[ >]',h)); dc=h.count('</div>')
ok=True
print("div:",do,"/",dc, "OK" if do==dc else "*** MISMATCH ***"); ok&=do==dc
m=re.search(r'const preguntas=\s*(\[.*?\]);',h,re.S)
if m:
    blk=m.group(0); n=blk.count('nivel:')
    b3='barajar([0,1,2])' in h; b4='barajar([0,1,2,3])' in h
    ctxs=[len(x) for x in re.findall(r"ctx:'((?:[^'\\]|\\.)*)'",blk)]
    qq=[len(x) for x in re.findall(r"q:'((?:[^'\\]|\\.)*)'",blk)]
    ops=re.findall(r"ops:\[(.*?)\], ?correcta",blk,re.S)
    oplens=[]; nops=[]; expls=[]
    for o in ops:
        items=re.findall(r"'((?:[^'\\]|\\.)*)'",o); nops.append(len(items)); oplens+=[len(i) for i in items]
    for e in re.findall(r"expl:\[(.*?)\]\s*\}",blk,re.S):
        expls.append(len(re.findall(r"'((?:[^'\\]|\\.)*)'",e)))
    print(f"preguntas:{n} barajar3:{b3} barajar4:{b4} nops:{set(nops)} nexpl:{set(expls)}")
    if ctxs: print(f"  ctx min {min(ctxs)} (<550:{sum(1 for c in ctxs if c<550)}) | q min {min(qq)} (<230:{sum(1 for c in qq if c<230)}) | op min {min(oplens)} (<150:{sum(1 for c in oplens if c<150)})")
    if b4 or set(nops)-{3}: print("  *** OJO: no es formato 3-opciones DIAN")
else:
    print("preguntas: (sin array const preguntas)")
PYEOF
echo "--- node --check ---"; "$NODE" --check /tmp/jcheck.js && echo "JS OK" || echo "*** JS ERROR ***"
echo "--- fugas ---"; grep -icE "Citador|6CI-04|\bPGN\b|Procuradur.a General|90-2026|Resoluci.n 212|Auxiliar Administrativo|5AM-10|\bSustanciador\b|Analista I|nivel T.cnico|242-2026|\bSyndy\b" "$F"
echo "--- desarrollo/día ---"; "$PY" scripts/validar-guia.py "$F" "$DIA" 2>&1 | grep -E "OK:|Desarrollo|coherente"
