"""Edita preguntas en formato de una línea JSON por pregunta (const preguntas=[ {..},\n {..} ])."""
import json
def editar_ops(f, O):
    L = open(f, encoding='utf-8').read().split('\n')
    idx = [i for i, l in enumerate(L) if l.strip().startswith('{') and '"ops"' in l]
    for n, cambios in O.items():
        i = idx[n - 1]; raw = L[i]; coma = raw.rstrip().endswith(',')
        pre = raw[:len(raw) - len(raw.lstrip())]
        q = json.loads(raw.strip().rstrip(','))
        for k, t in cambios.items(): q['ops'][k] = t
        L[i] = pre + json.dumps(q, ensure_ascii=False) + (',' if coma else '')
    open(f, 'w', encoding='utf-8').write('\n'.join(L))
