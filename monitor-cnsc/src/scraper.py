"""Scraper principal de la CNSC.

Revisa noticias, convocatorias y detecta nuevos enlaces y PDFs.
"""
import json
import logging
import os
import re
import ssl
from datetime import datetime
from html.parser import HTMLParser
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context

from .config import URLS_TO_MONITOR, STATE_FILE, DATA_DIR, KEYWORDS

logger = logging.getLogger(__name__)


# Adaptador SSL para manejar el certificado de la CNSC
class SSLAdapter(HTTPAdapter):
    """Adaptador HTTPS que no verifica certificado (CNSC tiene problemas de cert)."""
    def init_poolmanager(self, *args, **kwargs):
        ctx = create_urllib3_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        kwargs["ssl_context"] = ctx
        return super().init_poolmanager(*args, **kwargs)


def get_session():
    """Crea una sesión HTTP configurada."""
    session = requests.Session()
    session.mount("https://", SSLAdapter())
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    return session


class LinkExtractor(HTMLParser):
    """Extrae enlaces y sus textos del HTML de la CNSC."""

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []  # [(url, texto)]
        self.pdfs = []   # [(url, texto)]
        self._current_href = ""
        self._current_text = ""
        self._capturing = False

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attrs_dict = dict(attrs)
            href = attrs_dict.get("href", "")
            css_class = attrs_dict.get("class", "")

            # Ignorar links de navegación
            if "nav-item" in css_class or "nav-link" in css_class:
                return

            if href and (href.startswith("/") or href.startswith("http")):
                self._current_href = href
                self._current_text = ""
                self._capturing = True

    def handle_data(self, data):
        if self._capturing:
            self._current_text += data.strip()

    def handle_endtag(self, tag):
        if tag == "a" and self._capturing:
            self._capturing = False
            href = self._current_href
            text = self._current_text.strip()

            if not text or len(text) < 5:
                return

            # Construir URL completa
            if href.startswith("/"):
                full_url = urljoin(self.base_url, href)
            else:
                full_url = href

            # Clasificar como PDF o enlace normal
            if href.lower().endswith(".pdf"):
                self.pdfs.append((full_url, text))
            elif len(text) > 15:
                self.links.append((full_url, text))


def load_state():
    """Carga el estado previo (URLs ya detectadas)."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"known_links": [], "known_pdfs": [], "last_check": None}


def save_state(state):
    """Guarda el estado actual."""
    state["last_check"] = datetime.now().isoformat()
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def scrape_page(session, url):
    """Scrapea una página y extrae enlaces y PDFs."""
    try:
        response = session.get(url, timeout=30, verify=False)
        response.raise_for_status()

        parser = LinkExtractor(url)
        parser.feed(response.text)

        return parser.links, parser.pdfs

    except Exception as e:
        logger.error(f"Error scrapeando {url}: {e}")
        return [], []


def find_keywords_in_text(text, keywords=None):
    """Busca palabras clave en un texto y devuelve las encontradas."""
    if keywords is None:
        keywords = KEYWORDS

    found = []
    text_lower = text.lower()
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
    return found


def check_for_updates():
    """
    Revisa todas las URLs configuradas y detecta contenido nuevo.
    
    Returns:
        dict con:
            - new_links: [(url, texto, fuente)]
            - new_pdfs: [(url, texto, fuente)]
            - relevant_keywords: {url: [keywords encontradas]}
    """
    session = get_session()
    state = load_state()

    known_links = set(state.get("known_links", []))
    known_pdfs = set(state.get("known_pdfs", []))

    new_links = []
    new_pdfs = []
    relevant_keywords = {}

    for source_name, url in URLS_TO_MONITOR.items():
        logger.info(f"Revisando: {source_name} ({url})")
        links, pdfs = scrape_page(session, url)

        for link_url, link_text in links:
            if link_url not in known_links:
                new_links.append((link_url, link_text, source_name))
                known_links.add(link_url)

                # Buscar keywords en el título del enlace
                kws = find_keywords_in_text(link_text)
                if kws:
                    relevant_keywords[link_url] = kws

        for pdf_url, pdf_text in pdfs:
            if pdf_url not in known_pdfs:
                new_pdfs.append((pdf_url, pdf_text, source_name))
                known_pdfs.add(pdf_url)

                # Buscar keywords en el nombre del PDF
                kws = find_keywords_in_text(pdf_text)
                if kws:
                    relevant_keywords[pdf_url] = kws

    # Actualizar estado
    state["known_links"] = list(known_links)
    state["known_pdfs"] = list(known_pdfs)
    save_state(state)

    return {
        "new_links": new_links,
        "new_pdfs": new_pdfs,
        "relevant_keywords": relevant_keywords,
    }


def get_page_content(session, url):
    """Obtiene el contenido de texto de una página (para análisis profundo)."""
    try:
        response = session.get(url, timeout=30, verify=False)
        response.raise_for_status()
        # Extraer solo texto visible (sin tags)
        text = re.sub(r'<script[^>]*>.*?</script>', '', response.text, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', response.text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    except Exception as e:
        logger.error(f"Error obteniendo contenido de {url}: {e}")
        return ""
