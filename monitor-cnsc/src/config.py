"""Configuración del monitor CNSC."""
import os
from dotenv import load_dotenv

load_dotenv()

# Email
ALERT_EMAIL = os.getenv("ALERT_EMAIL", "ascensopublico@gmail.com")
SMTP_EMAIL = os.getenv("SMTP_EMAIL", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

# Intervalo de chequeo
CHECK_INTERVAL_MINUTES = int(os.getenv("CHECK_INTERVAL_MINUTES", "60"))

# Palabras clave para buscar en PDFs y contenido
KEYWORDS = [
    k.strip()
    for k in os.getenv(
        "KEYWORDS",
        "fecha de aplicación,pruebas escritas,cronograma,ejes temáticos,citación,convocatoria,resolución,inscripción,OPEC,manual de funciones,Corpomojana,DIAN,Territorial"
    ).split(",")
]

# URLs a monitorear
URLS_TO_MONITOR = {
    "noticias_2026": "https://www.cnsc.gov.co/cnsc-noticias-por-a-os/2026",
    "convocatorias_en_desarrollo": "https://www.cnsc.gov.co/convocatorias/en-desarrollo",
    "entidades_orden_nacional_corpomojana": "https://www.cnsc.gov.co/convocatorias/entidades-del-orden-nacional-y-corpomojana?field_tipo_de_contenido_convocat_target_id=65",
    "entidades_orden_nacional_2026": "https://www.cnsc.gov.co/convocatorias/entidades-del-orden-nacional-2026?field_tipo_de_contenido_convocat_target_id=65",
    "territorial_12": "https://www.cnsc.gov.co/convocatorias/territorial-12?field_tipo_de_contenido_convocat_target_id=65",
    "dian_2022": "https://www.cnsc.gov.co/convocatorias/dian-2022?field_tipo_de_contenido_convocat_target_id=65",
    "empresas_sociales_estado_2": "https://www.cnsc.gov.co/convocatorias/empresas-sociales-del-estado-2?field_tipo_de_contenido_convocat_target_id=65",
}

# Directorios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
PDF_DIR = os.path.join(DATA_DIR, "pdfs")

# Crear directorios si no existen
for d in [DATA_DIR, LOGS_DIR, PDF_DIR]:
    os.makedirs(d, exist_ok=True)

# Archivo de estado (para recordar qué ya se detectó)
STATE_FILE = os.path.join(DATA_DIR, "state.json")
