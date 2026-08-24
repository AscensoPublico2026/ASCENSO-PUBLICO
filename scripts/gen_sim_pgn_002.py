#!/usr/bin/env python3
"""Genera simulacro/SIM-PGN-002.html reusando el shell (head+CSS+body+render JS)
de SIM-PGN-001.html y sustituyendo: (1) el array preguntas por 50 preguntas
NIVEL PROFESIONAL (Procurador Judicial II, sin 'Sustanciador'), y (2) los textos
del header/meta. Formato CNSC robusto: ctx extenso, dilema, 4 opciones largas."""
import json, re

SRC = 'simulacro/SIM-PGN-001.html'
DST = 'simulacro/SIM-PGN-002.html'

h = open(SRC, encoding='utf-8').read()

# --- localizar el array preguntas ---
# El array 'const preguntas=[...]' termina en '];' inmediatamente seguido de
# '\n\nlet respuestas={}' en la plantilla SIM-PGN-001. Cortamos por ese marcador
# para NO invadir las funciones helper (barajar, etc.) que vienen después.
i = h.find('const preguntas=[')
marker = h.find('];', i)  # primer '];' tras el inicio del array = cierre del array
assert marker != -1, 'no se encontró el cierre del array'
arr_end = marker + 2
pre = h[:i]
post = h[arr_end:]
# sanity: el POST debe comenzar con las funciones helper del simulacro
assert 'let respuestas' in post[:200] or 'let respuestas' in post[:400], \
    'CORTE INCORRECTO: el POST no arranca con los helpers (let respuestas...)'

# --- ajustes de textos en el shell (header, intro, meta, contadores) ---
pre = pre.replace('SIM-PGN-001', 'SIM-PGN-002')
post = post.replace('SIM-PGN-001', 'SIM-PGN-002')
pre = pre.replace('Sustanciador 4SU-08', 'Procurador Judicial II (3PJ-EC)')
pre = pre.replace('🎓 Nivel Técnico', '🎓 Nivel Profesional')
pre = pre.replace('33 preguntas', '50 preguntas')
pre = pre.replace('las 33 preguntas', 'las 50 preguntas')
pre = pre.replace('0 de 33 respondidas', '0 de 50 respondidas')
pre = pre.replace('>0/33<', '>0/50<')
# título del hero
pre = pre.replace(
  'Concurso Mérito Construyendo Excelencia',
  'Convocatoria 89-2026 · Simulacro Integral Final')
# meta del footer
post = post.replace('Sustanciador 4SU-08 — Procuraduría General de la Nación · 33 preguntas',
                    'Procurador Judicial II (3PJ-EC) — Procuraduría General de la Nación · 50 preguntas · Nivel Profesional')

with open('scripts/sim_pgn_002_preguntas.json', encoding='utf-8') as f:
    preguntas = json.load(f)

assert len(preguntas) == 50, f'Se esperaban 50 preguntas, hay {len(preguntas)}'
# validar que ninguna use 'Sustanciador'
blob = json.dumps(preguntas, ensure_ascii=False)
assert 'ustanciador' not in blob, 'FUGA: aparece Sustanciador en las preguntas'
for idx, p in enumerate(preguntas):
    for key in ('nivel', 'tema', 'ctx', 'q', 'ops', 'correcta', 'expl', 'ref', 'refT'):
        assert key in p, f'Pregunta {idx+1} sin campo {key}'
    assert len(p['ops']) == 4 and len(p['expl']) == 4, f'Pregunta {idx+1} debe tener 4 ops y 4 expl'
    assert 0 <= p['correcta'] <= 3, f'Pregunta {idx+1} correcta fuera de rango'

arr = 'const preguntas=' + json.dumps(preguntas, ensure_ascii=False) + ';'

out = pre + arr + post
open(DST, 'w', encoding='utf-8').write(out)
print('OK escrito', DST, 'con', len(preguntas), 'preguntas ·', len(out), 'bytes')
