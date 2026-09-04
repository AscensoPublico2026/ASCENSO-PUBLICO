import re, os

guias = [
 (1,"guias/INTRO-00-PGN-PU-presentacion-curso.html","intro"),
 (1,"guias/ENT-PGN-PU-01-conoce-entidad-pgn.html","ent"),
 (2,"guias/GEN-01-PGN-estado-funcion-publica.html","gen"),
 (3,"guias/GEN-02-PGN-relacion-estado-ciudadano.html","gen"),
 (4,"guias/GEN-03-PGN-marco-institucional.html","gen"),
 (5,"guias/PU-PRO-COM-01-responsabilidad-organizacion-trabajo.html","com"),
 (6,"guias/PU-PRO-COM-02-orientacion-resultados-cumplimiento-parametros.html","com"),
 (7,"guias/PU-PRO-COM-03-investigacion-pensamiento-conceptual.html","com"),
 (8,"guias/PU-PRO-COM-04-alcance-cargo-profesional-evaluacion.html","com"),
 (9,"guias/FUN-MP-01-PU-ministerio-publico-estructura-pgn.html","fun"),
 (10,"guias/FUN-CONST-01-derecho-constitucional-control-disciplinario.html","fun"),
 (11,"guias/FUN-DIS-01-PU-derecho-disciplinario-fundamentos.html","fun"),
 (12,"guias/FUN-DIS-02-PU-procedimiento-instruccion-juzgamiento.html","fun"),
 (13,"guias/FUN-PROB-01-PU-derecho-probatorio-valoracion.html","fun"),
 (14,"guias/FUN-DIS-03-PU-recursos-segunda-instancia-siri.html","fun"),
 (15,"guias/FUN-PREV-01-PU-funcion-preventiva-control-gestion.html","fun"),
 (16,"guias/FUN-PEN-01-PU-derecho-penal-administracion-publica.html","fun"),
 (17,"guias/FUN-PEN-02-PU-derecho-penal-procesal-penal.html","fun"),
 (18,"guias/FUN-JUR-01-PU-derecho-administrativo-cpaca.html","fun"),
 (19,"guias/FUN-CONT-01-PU-contratacion-estatal-anticorrupcion.html","fun"),
 (20,"guias/FUN-GDOC-01-PU-gestion-documental-atencion-sistemas.html","fun"),
]
FUGAS=["Procurador Judicial II","3PJ-EC","3PJ","89-2026","Sustanciador","Gina","Valentina","Nathaly","Andrés Guillermo","INDERVALLE","Gestor I","DIAN","MUISCA","198368"]

print(f"{'Día':<4}{'Archivo':<44}{'Desar':>6}{'Pg':>3}{'CP':>3}{'Tb':>3}{'Fj':>3}{'Ej':>3}{'Mk':>4}{'HTML':>5} Fugas")
print("-"*112)
issues=[]
for dia,f,tipo in guias:
    if not os.path.exists(f):
        print(f"{dia:<4}{os.path.basename(f):<44} ❌ NO EXISTE"); issues.append((dia,os.path.basename(f),"no existe")); continue
    h=open(f,encoding="utf-8").read()
    m=re.search(r'<section[^>]*data-sec="2".*?</section>',h,re.S)
    dev=len(re.sub(r'<[^>]+>',' ',m.group(0)).split()) if m else 0
    preg=len(re.findall(r'class="pregunta"',h))
    cp=len(re.findall(r'class="checkpoint"',h))
    tab=len(re.findall(r'<table',h))
    flj=len(re.findall(r'class="flujo"',h))
    ej=len(re.findall(r'Ejercicio práctico',h))
    mk=len(re.findall(r'<mark>',h))
    html_ok = h.count('</html>')==1 and h.count('</body>')==1 and h.count('<script>')==h.count('</script>')
    fug=[t for t in FUGAS if re.search(r'\b'+re.escape(t)+r'\b',h)]
    print(f"{dia:<4}{os.path.basename(f)[:42]:<44}{dev:>6}{preg:>3}{cp:>3}{tab:>3}{flj:>3}{ej:>3}{mk:>4}{('OK' if html_ok else 'BAD'):>5} {fug if fug else '—'}")
    if tipo in ("fun","com") and dev<10000: issues.append((dia,os.path.basename(f),f"Desarrollo {dev}<10000"))
    if tipo in ("fun","com") and preg<15: issues.append((dia,os.path.basename(f),f"preguntas {preg}<15"))
    if tipo in ("fun",) and cp<3: issues.append((dia,os.path.basename(f),f"checkpoints {cp}<3"))
    if tipo in ("fun",) and tab<3: issues.append((dia,os.path.basename(f),f"tablas {tab}<3"))
    if not html_ok: issues.append((dia,os.path.basename(f),"HTML desbalanceado"))
    if fug: issues.append((dia,os.path.basename(f),f"fugas {fug}"))
print("\n=== INCIDENCIAS (criterios funcionales/comportamentales) ===")
if issues:
    for i in issues: print("⚠️",i)
else:
    print("✅ Ninguna incidencia en los criterios automáticos")
