# -*- coding: utf-8 -*-
import openpyxl, re, unicodedata

RUTA = "/projects/sandbox/ASCENSO-PUBLICO/Convocatorias_Procuraduria.xlsx"
wb = openpyxl.load_workbook(RUTA, read_only=True, data_only=True)
ws = wb["Convocatorias"]
rows = list(ws.iter_rows(values_only=True))
H = rows[0]
data = rows[1:]

def col(name):
    for i,h in enumerate(H):
        if h == name: return i
    raise KeyError(name)

C = {h:i for i,h in enumerate(H)}
i_cod=C["Código"]; i_cargo=C["Cargo"]; i_niv=C["Nivel"]; i_grado=C["Grado"]
i_plz=C["N° de plazas"]; i_sal=C["Salario mensual"]; i_dep=C["Departamentos"]
i_mun=C["Municipios"]; i_proc=C["Proceso"]; i_estudio=C["Requisito de estudio"]
i_exp=C["Requisito de experiencia"]; i_dep2=C["Dependencia"]

def norm(s):
    s = str(s or "")
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode()
    return s.lower()

CIUDADES = ["pasto","ipiales","popayan","mocoa","puerto asis","cartagena"]
DEPTOS = ["narino","cauca","putumayo","caldas","antioquia","bolivar"]

print(f"Total vacantes: {len(data)}")
print("Salario objetivo aspirante: 8.000.000 - 9.000.000 (con margen mostramos 7M-11M)\n")

# 1) Requisito de estudio acepta Derecho
def acepta_derecho(txt):
    t = norm(txt)
    return "derecho" in t

# 2) ubicacion coincide
def ubica(deps, muns):
    dn, mn = norm(deps), norm(muns)
    hit_c = [c for c in CIUDADES if c in mn]
    hit_d = [d for d in DEPTOS if d in dn]
    return hit_c, hit_d

resultados = []
for r in data:
    est = r[i_estudio]
    if not acepta_derecho(est):
        continue
    hit_c, hit_d = ubica(r[i_dep], r[i_mun])
    if not (hit_c or hit_d):
        continue
    sal = r[i_sal] or 0
    try: sal = int(float(sal))
    except: sal = 0
    resultados.append({
        "cod": r[i_cod], "cargo": r[i_cargo], "nivel": r[i_niv], "grado": r[i_grado],
        "plz": r[i_plz], "sal": sal, "proc": r[i_proc], "dep": r[i_dep2],
        "ciudades": hit_c, "deptos": hit_d,
        "estudio": str(est)[:220], "exp": str(r[i_exp])[:120]
    })

# ordenar por cercania a 8.5M
resultados.sort(key=lambda x: abs(x["sal"]-8500000))
print(f"Vacantes que ACEPTAN DERECHO y coinciden en ciudad/depto: {len(resultados)}\n")
for x in resultados:
    print("="*80)
    print(f"[{x['cod']}] {x['cargo']}  | Nivel: {x['nivel']} | Grado: {x['grado']}")
    print(f"  Salario: ${x['sal']:,}  | Plazas: {x['plz']}  | Proceso: {x['proc']}")
    print(f"  Dependencia: {x['dep']}")
    print(f"  Ciudades match: {x['ciudades']}  | Deptos match: {x['deptos']}")
    print(f"  Estudio: {x['estudio']}")
    print(f"  Experiencia: {x['exp']}")
