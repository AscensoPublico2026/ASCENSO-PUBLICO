"""Módulo de descarga y lectura de PDFs.

Descarga PDFs nuevos de la CNSC, extrae el texto y busca
palabras clave relevantes (fechas, ejes temáticos, cronogramas, etc.)
"""
import io
import logging
import os
import re
from datetime import datetime

import requests
from PyPDF2 import PdfReader

from .config import PDF_DIR, KEYWORDS
from .scraper import get_session

logger = logging.getLogger(__name__)


def download_pdf(url):
    """
    Descarga un PDF y retorna los bytes.
    
    Args:
        url: URL del PDF a descargar
        
    Returns:
        bytes del PDF o None si falla
    """
    session = get_session()
    try:
        response = session.get(url, timeout=60, verify=False)
        response.raise_for_status()

        if "application/pdf" in response.headers.get("Content-Type", "") or url.lower().endswith(".pdf"):
            return response.content
        else:
            logger.warning(f"La URL no devolvió un PDF: {url}")
            return None

    except Exception as e:
        logger.error(f"Error descargando PDF {url}: {e}")
        return None


def save_pdf(pdf_bytes, filename):
    """Guarda el PDF en disco para referencia."""
    # Limpiar nombre de archivo
    safe_name = re.sub(r'[^\w\-.]', '_', filename)
    if not safe_name.endswith(".pdf"):
        safe_name += ".pdf"

    filepath = os.path.join(PDF_DIR, safe_name)
    with open(filepath, "wb") as f:
        f.write(pdf_bytes)

    logger.info(f"PDF guardado: {filepath}")
    return filepath


def extract_text_from_pdf(pdf_bytes):
    """
    Extrae todo el texto de un PDF.
    
    Args:
        pdf_bytes: bytes del archivo PDF
        
    Returns:
        Texto completo del PDF
    """
    try:
        reader = PdfReader(io.BytesIO(pdf_bytes))
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        logger.error(f"Error extrayendo texto del PDF: {e}")
        return ""


def search_keywords_in_text(text, keywords=None):
    """
    Busca palabras clave en el texto extraído del PDF.
    
    Returns:
        Lista de diccionarios con la keyword y el contexto donde aparece.
    """
    if keywords is None:
        keywords = KEYWORDS

    results = []
    text_lower = text.lower()

    for kw in keywords:
        kw_lower = kw.lower()
        # Buscar todas las ocurrencias
        start = 0
        while True:
            idx = text_lower.find(kw_lower, start)
            if idx == -1:
                break

            # Extraer contexto (100 chars antes y después)
            context_start = max(0, idx - 100)
            context_end = min(len(text), idx + len(kw) + 100)
            context = text[context_start:context_end].strip()
            context = re.sub(r'\s+', ' ', context)

            results.append({
                "keyword": kw,
                "context": f"...{context}...",
            })

            start = idx + len(kw)
            # Solo guardar la primera ocurrencia de cada keyword
            break

    return results


def extract_dates_from_text(text):
    """
    Busca fechas relevantes mencionadas en el texto.
    Patrones: "16 de agosto de 2026", "agosto 16", etc.
    
    Returns:
        Lista de fechas encontradas con contexto.
    """
    date_patterns = [
        # "16 de agosto de 2026"
        r'\d{1,2}\s+de\s+(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\s+(?:de\s+)?\d{4}',
        # "agosto 16 de 2026"
        r'(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\s+\d{1,2}\s+(?:de\s+)?\d{4}',
        # "16/08/2026" o "16-08-2026"
        r'\d{1,2}[/\-]\d{1,2}[/\-]\d{4}',
        # "2026-08-16"
        r'\d{4}[/\-]\d{1,2}[/\-]\d{1,2}',
    ]

    dates_found = []
    for pattern in date_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            date_str = match.group()
            # Contexto alrededor de la fecha
            start = max(0, match.start() - 80)
            end = min(len(text), match.end() + 80)
            context = text[start:end].strip()
            context = re.sub(r'\s+', ' ', context)

            dates_found.append({
                "date": date_str,
                "context": f"...{context}...",
            })

    return dates_found


def analyze_pdf(url, pdf_name=""):
    """
    Proceso completo: descarga, extrae texto, busca keywords y fechas.
    
    Args:
        url: URL del PDF
        pdf_name: nombre descriptivo del PDF
        
    Returns:
        dict con resultados del análisis o None si falla
    """
    logger.info(f"Analizando PDF: {pdf_name or url}")

    # Descargar
    pdf_bytes = download_pdf(url)
    if not pdf_bytes:
        return None

    # Guardar copia local
    filename = pdf_name or url.split("/")[-1]
    save_pdf(pdf_bytes, filename)

    # Extraer texto
    text = extract_text_from_pdf(pdf_bytes)
    if not text:
        logger.warning(f"No se pudo extraer texto del PDF: {url}")
        return None

    # Buscar keywords
    keyword_results = search_keywords_in_text(text)

    # Buscar fechas
    date_results = extract_dates_from_text(text)

    # Resumen
    analysis = {
        "url": url,
        "name": pdf_name,
        "analyzed_at": datetime.now().isoformat(),
        "total_pages": len(PdfReader(io.BytesIO(pdf_bytes)).pages),
        "text_length": len(text),
        "keywords_found": keyword_results,
        "dates_found": date_results,
        "text_preview": text[:500],  # Primeros 500 chars para referencia
    }

    if keyword_results or date_results:
        logger.info(
            f"PDF '{pdf_name}': {len(keyword_results)} keywords, {len(date_results)} fechas encontradas"
        )
    else:
        logger.info(f"PDF '{pdf_name}': sin hallazgos relevantes")

    return analysis
