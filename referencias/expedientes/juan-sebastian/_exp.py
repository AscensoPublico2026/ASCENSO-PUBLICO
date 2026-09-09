from datetime import date

GRADO = date(2016, 8, 26)  # título de Abogado

# Intervalos laborales (inicio, fin, etiqueta, es_juridica_posgrado_relevante)
periodos = [
    (date(2013,11,15), date(2013,11,15), "Práctica jurídica ad honorem - T. Admin Nariño (estudiante)", False),
    (date(2015,1,16),  date(2015,6,2),   "Auxiliar Judicial Ad Honorem - T. Superior Pasto (1)", False),
    (date(2015,7,6),   date(2015,12,11),  "Auxiliar Judicial Ad Honorem - T. Superior Pasto (2)", False),
    (date(2016,1,16),  date(2019,2,4),   "Jefe Talento Humano / Control Interno Disciplinario - Protegemos", True),
    (date(2020,1,22),  date(2020,9,2),   "ICBF Regional Narino - Grupo Juridico (contrato 098/2020)", True),
    (date(2020,2,4),   date(2020,12,18), "ARN contrato 1011/2020", True),
    (date(2021,1,19),  date(2021,12,31), "ARN contrato 838/2021", True),
    (date(2022,1,19),  date(2022,12,16), "ARN contrato 709/2022", True),
    (date(2023,7,19),  date(2023,12,31), "ARN contrato 1867/2023 (y 866/2023)", True),
    (date(2024,6,18),  date(2024,12,31), "MinTrabajo contrato 406/2024", True),
    (date(2025,2,5),   date(2025,12,4),  "MinTrabajo contrato 228/2025", True),
]

def recortar_desde_grado(ini, fin):
    ini2 = max(ini, GRADO)
    if fin < ini2:
        return None
    return (ini2, fin)

def unir(intervalos):
    ints = sorted(intervalos)
    merged = []
    for ini, fin in ints:
        if merged and ini <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], fin))
        else:
            merged.append((ini, fin))
    return merged

def dias_meses(intervalos):
    total = sum((fin-ini).days + 1 for ini,fin in intervalos)
    return total, total/30.0

print("=== PERIODOS (recortados desde el grado 2016-08-26) ===")
validos = []
for ini,fin,lbl,rel in periodos:
    r = recortar_desde_grado(ini,fin)
    if r is None:
        print(f"  DESCARTADO (antes del grado): {lbl}  [{ini} a {fin}]")
    else:
        print(f"  CUENTA: {lbl}  [{r[0]} a {r[1]}]")
        validos.append(r)

print("\n=== UNION DE INTERVALOS (sin doble conteo) ===")
merged = unir(validos)
for ini,fin in merged:
    print(f"  {ini}  ->  {fin}   ({(fin-ini).days+1} dias)")

d, m = dias_meses(merged)
print(f"\nTOTAL experiencia profesional post-titulo (union): {d} dias = {m:.1f} meses = {m/12:.2f} anos")

# Toda la experiencia post-titulo es juridica (abogado litigante + asesor juridico + judicatura)
print("\n(Toda la experiencia post-titulo corresponde a ejercicio profesional del derecho / juridica-administrativa.)")
