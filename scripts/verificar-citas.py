#!/usr/bin/env python3
"""Verificador de CITAS NORMATIVAS: para cada cita "art. N" de la Constitución, el CGD (Ley 1952)
o el CPACA (Ley 1437), comprueba que el texto que la rodea hable del tema que ese artículo regula.
Si no aparece ninguna palabra clave del tema, la marca para revisión (posible artículo equivocado).
Uso: python3 scripts/verificar-citas.py [archivos...]   (sin argumentos: todas las guías PGN auditadas)
"""
import re, html, json, sys, os, collections
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def txt(x): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x)))
K = {'CP': {
 1:'estado social|república|unitari|descentraliz|democr|dignidad|pluralis|trabajo|solidaridad|interés general', 2:'fines|servir a la comunidad|prosperidad|autoridades|garantizar|efectividad',
 3:'soberan|pueblo', 4:'norma de normas|suprema|prevalec|inconstitucional|excepción', 6:'respons|particular|servidor|omisi|extralimit|infracci',
 13:'igualdad|discrimin', 15:'intimidad|habeas|datos|buen nombre', 23:'petici', 29:'debido proceso|defensa|inocen|prueba|nulidad|favorab|non bis|legalidad|juez natural|contradic|impugn',
 74:'acceso|documentos', 82:'espacio público|plusval', 83:'buena fe', 86:'tutela', 88:'popular|grupo|colectiv', 93:'tratados|derechos humanos|bloque',
 95:'deber|ciudadan|persona|obligacion', 103:'participaci|plebiscito|referendo|consulta|cabildo|iniciativa|revocatoria|voto', 113:'rama|órgano|autónom|independ|armónica|separaci',
 116:'justicia|jurisdiccional', 117:'control|Ministerio Público|Contralor', 118:'Ministerio Público|Procurador|Defensor|personer', 120:'electoral|Registradur|Consejo Nacional Electoral',
 123:'servidor|particular|empleados|trabajadores|miembros de corporaciones', 125:'carrera|mérito|concurso|libre nombramiento', 130:'Comisión Nacional del Servicio Civil|CNSC|carrera',
 150:'Congreso|ley', 151:'orgánic', 152:'estatutari', 153:'estatutari|mayoría absoluta|Corte', 158:'unidad de materia|materia', 189:'Presidente|Jefe de Estado|Gobierno',
 211:'delega', 212:'Fuerza Pública|militar', 224:'tratado', 230:'imperio de la ley|fuente|jurisprudencia|doctrina|equidad|auxiliar|principios generales',
 241:'Corte Constitucional|guarda|constitucionalidad', 242:'Corte|acción pública|proceso|demanda', 258:'voto|sufragio', 264:'Consejo Nacional Electoral|CNE|magistrad', 265:'Consejo Nacional Electoral|CNE|electoral',
 267:'Contralor|fiscal', 269:'control interno', 270:'participaci|vigil|gestión|veedur|ciudadan', 275:'Procurador|director|Ministerio Público', 276:'elegi|Senado|terna|Procurador',
 277:'Procurador|función|funciones|vigilanc|preferente|intervenir|derechos|patrimonio|disciplinari|prevenc|cumplimiento', 278:'Procurador|directamente|desvincul|Congreso|proyectos de ley|conceptos',
 279:'estructura|ley determinar|Procuradur|organizaci', 286:'territorial|departamento|municipio|distrito|indígena', 287:'autonom', 288:'ordenamiento|coordinaci|concurrencia|subsidiariedad|orgánica',
 298:'departamento', 300:'asamblea', 305:'gobernador', 311:'municipio', 313:'concejo', 315:'alcalde', 338:'tribut|impuest|contribuci|tasa|asamblea|concejo|Congreso',
 339:'plan|desarrollo', 345:'presupuest|gasto|contribuci|percibir', 346:'presupuest', 354:'Contador|contabilidad', 375:'proyecto|acto legislativo|reforma'},
 'CGD': {2:'titular|potestad|preferente|control interno|Procuradur|competen|jurisdiccional', 10:'culpabilidad|dolo|culpa|objetiva', 25:'destinatari|disciplinable|servidor|particular', 38:'deber'},
 'CPACA': {3:'principio', 5:'derecho', 7:'deber|atención', 9:'prohibi', 13:'petici', 14:'término|días|plazo', 17:'incomplet|desist|requer', 21:'competen|remit|traslad', 23:'Procuradur|Defensor|personer|deber',
  24:'reserva', 42:'decisi|contenido|motiva', 44:'discrecional|proporcional', 47:'sancionatori|procedimiento', 56:'electrónic|notificaci', 69:'aviso|notificaci', 74:'recurso|reposición|apelación|queja',
  83:'silencio', 87:'firmeza|firmes|ejecutori', 93:'revocaci|revocatoria', 137:'nulidad', 161:'requisito|demanda|conciliaci'}}
LAW = {'CP': r'(?:de la |la )?(?:Constituci[oó]n(?: Política)?|C\.\s?P\.?|CP)\b', 'CGD': r'(?:del |de la )?(?:CGD|Código General Disciplinario|Ley 1952(?: de 2019)?)', 'CPACA': r'(?:del |de la )?(?:CPACA|Ley 1437(?: de 2011)?)'}
def revisar(path):
    s = txt(open(path, encoding='utf-8').read()); out = []
    for law, pat in LAW.items():
        for m in re.finditer(r'\b[Aa]rt(?:ículo|s?\.)\s*(\d{1,3})(?:[\s,]*(?:num(?:eral|\.)\s*\d+|inc(?:iso|\.)\s*\d+|parágrafo))?\s*' + pat, s):
            a = int(m.group(1)); kw = K[law].get(a)
            if not kw: continue
            ctx = s[max(0, m.start()-220):m.end()+160]
            if not re.search(kw, ctx, re.I): out.append((law, a, s[max(0, m.start()-130):m.end()+70]))
    return out
if __name__ == '__main__':
    files = sys.argv[1:] or [r['archivo'] for r in json.load(open('referencias/pgn/AUDITORIA.json', encoding='utf-8'))]
    tot = 0
    for f in files:
        for law, a, frag in revisar(f):
            tot += 1; print(f"{f} | {law} art. {a} | …{frag}…")
    print('TOTAL a revisar:', tot, file=sys.stderr)
