#!/usr/bin/env python3
"""Registra en biblioteca/biblioteca.json las guías del curso Procurador Judicial II (PGN):
las 13 nuevas + los reutilizables PGN que faltaban. Idempotente: no duplica por 'codigo'.
Actualiza también 'actualizado'. No toca las entradas ya existentes salvo que se indique.
"""
import json, datetime

PATH = 'biblioteca/biblioteca.json'
d = json.load(open(PATH, encoding='utf-8'))
guias = d['guias']
by_cod = {e.get('codigo'): e for e in guias}

# (codigo, titulo, biblioteca, nivel, tipo, archivo, reutilizable, simulacro, temas)
NUEVAS = [
 ("PGN-PRO-COM-01","Responsabilidad con la Organización y Organización del Trabajo (Nivel Profesional)","Por Nivel","Profesional","comportamental",
  "guias/PGN-PRO-COM-01-responsabilidad-organizacion-trabajo.html",False,False,
  ["Responsabilidad con la Organización (Nivel B)","Organización del Trabajo (Nivel B)","Diccionario de competencias comportamentales","Niveles A/B/C","Lealtad institucional y autonomía técnica"]),
 ("PGN-PRO-COM-02","Orientación a Resultados (C) e Impacto e Influencia (A) (Nivel Profesional)","Por Nivel","Profesional","comportamental",
  "guias/PGN-PRO-COM-02-orientacion-resultados-impacto-influencia.html",False,False,
  ["Orientación a Resultados (Nivel C)","Impacto e Influencia (Nivel A)","Influencia legítima vs. presión indebida","Anatomía del concepto persuasivo","Resultado del Ministerio Público"]),
 ("PGN-PRO-COM-03","Investigación (B), Pensamiento Conceptual (A) y Analítico (B) (Nivel Profesional)","Por Nivel","Profesional","comportamental",
  "guias/PGN-PRO-COM-03-investigacion-pensamiento-conceptual-analitico.html",False,False,
  ["Investigación (Nivel B)","Pensamiento Conceptual (Nivel A)","Pensamiento Analítico (Nivel B)","Sesgos del razonamiento","Subsunción y ponderación"]),
 ("PGN-PRO-COM-04","Alcance del Cargo Profesional y Evaluación por Niveles A/B/C (Nivel Profesional)","Por Nivel","Profesional","comportamental",
  "guias/PGN-PRO-COM-04-alcance-cargo-profesional-evaluacion-niveles.html",False,False,
  ["Alcance del cargo Procurador Judicial II","Autonomía técnica y sus límites","Sistema de evaluación por niveles A/B/C","Perfil comportamental completo","Cómo se evalúa en la prueba"]),
 ("FUN-INT-01","Intervención Judicial: Técnica, Conceptos y Argumentación Jurídica","Funcional","Profesional","funcional",
  "guias/FUN-INT-01-intervencion-judicial-tecnica-conceptos-argumentacion.html",True,False,
  ["Fundamento constitucional de la intervención (art. 277-7)","Sujeto procesal especial","Intervención obligatoria vs. facultativa","Anatomía del concepto","Subsunción, ponderación y precedente"]),
 ("FUN-INT-02","Intervención en lo Constitucional: Tutela, Acciones Constitucionales y Populares","Funcional","Profesional","funcional",
  "guias/FUN-INT-02-intervencion-constitucional-tutela-acciones.html",True,False,
  ["Acción de tutela y subsidiariedad","Tutela contra providencia (C-590/2005)","Acción de cumplimiento","Acciones populares y de grupo","Concepto ante la Corte Constitucional"]),
 ("FUN-INT-03","Intervención en lo Penal y Procesal Penal (Ley 906/2004)","Funcional","Profesional","funcional",
  "guias/FUN-INT-03-intervencion-penal-procesal-penal.html",True,False,
  ["Sistema penal acusatorio","Roles (garantías, conocimiento, Fiscalía, defensa, MP, víctima)","Etapas del proceso","Principio de objetividad y duda razonable","Independencia del Ministerio Público"]),
 ("FUN-INT-04","Intervención en lo Civil, Laboral, de Familia y Contencioso-Administrativo","Funcional","Profesional","funcional",
  "guias/FUN-INT-04-intervencion-civil-laboral-familia-contencioso.html",True,False,
  ["CGP e intervención en lo civil","Intervención obligatoria con menores","Procesos laborales","Medios de control del CPACA","Responsabilidad del Estado (art. 90 CP)"]),
 ("FUN-CONC-01","Conciliación, MASC y Comités de Conciliación","Funcional","Profesional","funcional",
  "guias/FUN-CONC-01-conciliacion-masc-comites.html",True,False,
  ["MASC: conciliación, arbitraje, amigable composición","Conciliación en derecho y en equidad","Materias conciliables y no conciliables","Requisito de procedibilidad","Comités de conciliación y defensa del patrimonio público"]),
 ("FUN-PREV-01","Función Preventiva y de Control de Gestión del Ministerio Público","Funcional","Profesional","funcional",
  "guias/FUN-PREV-01-funcion-preventiva-control-gestion.html",True,False,
  ["Función preventiva (art. 277)","Vigilancia superior de la conducta oficial","Requerimientos y advertencias","Poder preferente","Distinción entre preventiva, disciplinaria e intervención"]),
 ("FUN-DDHH-01","Derechos Humanos, DIH y Justicia Transicional (Ley 1448/2011)","Funcional","Profesional","funcional",
  "guias/FUN-DDHH-01-derechos-humanos-dih-justicia-transicional.html",True,False,
  ["Bloque de constitucionalidad (art. 93 CP)","Derechos humanos y DIH","Justicia transicional: verdad, justicia, reparación, no repetición","Ley 1448/2011 y restitución de tierras","Consulta previa (Convenio 169 OIT)"]),
 ("FUN-PROB-01","Derecho Probatorio, Valoración de la Prueba y Trámite Procesal","Funcional","Profesional","funcional",
  "guias/FUN-PROB-01-derecho-probatorio-valoracion-prueba.html",True,False,
  ["Medios de prueba","Principios probatorios","Carga de la prueba y carga dinámica","Sana crítica y estándares probatorios","Regla de exclusión (art. 29 CP) y cadena de custodia"]),
 ("SIM-PGN-002","Simulacro Integral Final — Procurador Judicial II (50 preguntas, Nivel Profesional)","Simulacro Final","Profesional","evaluacion",
  "simulacro/SIM-PGN-002.html",False,True,
  ["50 preguntas de juicio situacional nivel profesional","Cubre todo el curso PGN Procurador Judicial II","Intervención judicial, constitucional, penal y contencioso","Conciliación, preventiva, DDHH y probatorio","Competencias comportamentales del perfil"]),
]

# Reutilizables PGN que faltaban por registrar (los archivos ya existen)
REUTILIZABLES = [
 ("GEN-01-PGN","Estado y Función Pública (versión PGN)","General",None,"conocimiento",
  "guias/GEN-01-PGN-estado-funcion-publica.html",True,False,
  ["Estado y función pública","Estructura del Estado colombiano","Servidor público","Principios de la función administrativa"]),
 ("GEN-02-PGN","Relación Estado-Ciudadano (versión PGN)","General",None,"conocimiento",
  "guias/GEN-02-PGN-relacion-estado-ciudadano.html",True,False,
  ["Relación Estado-ciudadano","Derechos y deberes","Atención al ciudadano","Participación"]),
 ("GEN-03-PGN","Marco Institucional (versión PGN)","General",None,"conocimiento",
  "guias/GEN-03-PGN-marco-institucional.html",True,False,
  ["Marco institucional del Estado","Organización del Estado","Ramas del poder y órganos de control"]),
 ("FUN-MP-01","El Ministerio Público: Estructura y Funciones de la PGN","Funcional",None,"funcional",
  "guias/FUN-MP-01-ministerio-publico-estructura-pgn.html",True,False,
  ["Estructura de la Procuraduría General de la Nación","Ministerio Público (art. 118 CP)","Funciones misionales","Organización territorial"]),
 ("FUN-MP-02","Función de Intervención del Ministerio Público","Funcional",None,"funcional",
  "guias/FUN-MP-02-funcion-intervencion-ministerio-publico.html",True,False,
  ["Función de intervención (art. 277-7)","Sujeto procesal especial","Procesos donde interviene","Instrumentos de la intervención"]),
 ("FUN-OFI-02","Documentos de Oficina, Informes y Sistemas de Información","Funcional",None,"funcional",
  "guias/FUN-OFI-02-documentos-oficina-informes-sistemas.html",True,False,
  ["Documentos de oficina","Informes","Sistemas de información","Gestión documental de apoyo"]),
]

def entry(cod, titulo, bib, nivel, tipo, archivo, reutil, sim, temas):
    return {
        "codigo": cod, "dia": None, "titulo": titulo, "biblioteca": bib,
        "nivel": nivel, "tipo": tipo, "estado": "publicada", "archivo": archivo,
        "reutilizable": reutil, "simulacro": sim, "temas": temas,
    }

agregadas = []
for spec in NUEVAS + REUTILIZABLES:
    cod = spec[0]
    if cod in by_cod:
        continue  # idempotente: ya está
    e = entry(*spec)
    guias.append(e)
    by_cod[cod] = e
    agregadas.append(cod)

d['actualizado'] = datetime.date.today().isoformat()
json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('Agregadas', len(agregadas), 'entradas:', ', '.join(agregadas) if agregadas else '(ninguna, ya estaban)')
print('Total guías en biblioteca:', len(guias))
