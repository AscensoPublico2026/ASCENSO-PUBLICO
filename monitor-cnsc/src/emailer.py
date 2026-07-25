"""Módulo de envío de alertas por email.

Envía un resumen de novedades detectadas en la CNSC
al email configurado (ascensopublico@gmail.com).
"""
import logging
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .config import ALERT_EMAIL, SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT

logger = logging.getLogger(__name__)


def build_email_html(new_links, new_pdfs, pdf_analyses):
    """
    Construye el cuerpo del email en HTML con las novedades.
    
    Args:
        new_links: [(url, texto, fuente)]
        new_pdfs: [(url, texto, fuente)]
        pdf_analyses: [dict con análisis de cada PDF]
        
    Returns:
        str HTML del email
    """
    now = datetime.now().strftime("%d/%m/%Y %H:%M")

    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 700px; margin: 0 auto; }}
            .header {{ background: #1a3a5c; color: white; padding: 20px; border-radius: 8px 8px 0 0; }}
            .header h1 {{ margin: 0; font-size: 22px; }}
            .header p {{ margin: 5px 0 0; opacity: 0.8; font-size: 13px; }}
            .content {{ padding: 20px; background: #f9f9f9; }}
            .section {{ background: white; padding: 15px; margin-bottom: 15px; border-radius: 6px; border-left: 4px solid #3366cc; }}
            .section h2 {{ margin-top: 0; color: #1a3a5c; font-size: 16px; }}
            .link-item {{ margin: 8px 0; padding: 8px; background: #f0f4ff; border-radius: 4px; }}
            .link-item a {{ color: #3366cc; text-decoration: none; font-weight: bold; }}
            .link-item .source {{ font-size: 11px; color: #888; }}
            .keyword-badge {{ display: inline-block; background: #ff6b35; color: white; padding: 2px 8px; border-radius: 12px; font-size: 11px; margin: 2px; }}
            .date-found {{ background: #e8f5e9; padding: 8px; border-radius: 4px; margin: 5px 0; border-left: 3px solid #4caf50; }}
            .date-found strong {{ color: #2e7d32; }}
            .context {{ font-size: 12px; color: #666; font-style: italic; margin-top: 4px; }}
            .footer {{ padding: 15px; text-align: center; font-size: 11px; color: #888; }}
            .alert-badge {{ background: #ff4444; color: white; padding: 3px 10px; border-radius: 12px; font-size: 12px; }}
            .no-news {{ text-align: center; padding: 30px; color: #888; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🔔 Monitor CNSC - Ascenso Público</h1>
            <p>Reporte automático | {now}</p>
        </div>
        <div class="content">
    """

    has_content = False

    # Sección: Nuevos enlaces (noticias, resoluciones, etc.)
    if new_links:
        has_content = True
        html += f"""
            <div class="section">
                <h2>📰 Nuevas publicaciones detectadas ({len(new_links)})</h2>
        """
        for url, text, source in new_links:
            html += f"""
                <div class="link-item">
                    <a href="{url}" target="_blank">{text}</a>
                    <div class="source">Fuente: {source}</div>
                </div>
            """
        html += "</div>"

    # Sección: Nuevos PDFs
    if new_pdfs:
        has_content = True
        html += f"""
            <div class="section">
                <h2>📄 Nuevos documentos PDF detectados ({len(new_pdfs)})</h2>
        """
        for url, text, source in new_pdfs:
            html += f"""
                <div class="link-item">
                    <a href="{url}" target="_blank">{text}</a>
                    <div class="source">Fuente: {source}</div>
                </div>
            """
        html += "</div>"

    # Sección: Análisis de PDFs (keywords y fechas)
    if pdf_analyses:
        for analysis in pdf_analyses:
            if not analysis:
                continue
            if not analysis.get("keywords_found") and not analysis.get("dates_found"):
                continue

            has_content = True
            html += f"""
                <div class="section">
                    <h2>🔍 Análisis del documento: {analysis.get('name', 'Sin nombre')}</h2>
                    <p style="font-size: 12px; color: #666;">
                        Páginas: {analysis.get('total_pages', '?')} | 
                        <a href="{analysis.get('url', '#')}" target="_blank">Ver PDF</a>
                    </p>
            """

            # Keywords encontradas
            if analysis.get("keywords_found"):
                html += "<h3 style='font-size: 14px; color: #ff6b35;'>⚡ Palabras clave encontradas:</h3>"
                for kw_result in analysis["keywords_found"]:
                    html += f"""
                        <div style="margin: 5px 0;">
                            <span class="keyword-badge">{kw_result['keyword']}</span>
                            <div class="context">{kw_result['context']}</div>
                        </div>
                    """

            # Fechas encontradas
            if analysis.get("dates_found"):
                html += "<h3 style='font-size: 14px; color: #2e7d32;'>📅 Fechas detectadas:</h3>"
                for date_result in analysis["dates_found"][:10]:  # Max 10 fechas
                    html += f"""
                        <div class="date-found">
                            <strong>{date_result['date']}</strong>
                            <div class="context">{date_result['context']}</div>
                        </div>
                    """

            html += "</div>"

    if not has_content:
        html += """
            <div class="no-news">
                <p>✅ No se detectaron novedades en esta revisión.</p>
                <p>El monitor sigue activo y te avisará cuando haya cambios.</p>
            </div>
        """

    html += """
        </div>
        <div class="footer">
            <p>Este es un reporte automático generado por el Monitor CNSC de Ascenso Público.</p>
            <p>El monitor revisa periódicamente la web de la CNSC para detectar novedades.</p>
        </div>
    </body>
    </html>
    """

    return html


def send_alert_email(new_links, new_pdfs, pdf_analyses):
    """
    Envía el email de alerta con las novedades detectadas.
    
    Args:
        new_links: Lista de nuevos enlaces encontrados
        new_pdfs: Lista de nuevos PDFs encontrados
        pdf_analyses: Lista de análisis de PDFs
        
    Returns:
        True si se envió correctamente, False si falló
    """
    if not SMTP_EMAIL or not SMTP_PASSWORD:
        logger.error(
            "No se configuraron las credenciales SMTP. "
            "Configura SMTP_EMAIL y SMTP_PASSWORD en el archivo .env"
        )
        return False

    # Construir el email
    msg = MIMEMultipart("alternative")

    # Determinar asunto según contenido
    total_news = len(new_links) + len(new_pdfs)
    has_important = any(
        a and (a.get("keywords_found") or a.get("dates_found"))
        for a in pdf_analyses
    )

    if has_important:
        subject = f"🚨 CNSC: Información importante detectada ({total_news} novedades)"
    elif total_news > 0:
        subject = f"🔔 CNSC: {total_news} novedades detectadas"
    else:
        # No enviar email si no hay nada nuevo
        logger.info("Sin novedades. No se envía email.")
        return True

    msg["Subject"] = subject
    msg["From"] = SMTP_EMAIL
    msg["To"] = ALERT_EMAIL

    # Cuerpo del email
    html_body = build_email_html(new_links, new_pdfs, pdf_analyses)
    msg.attach(MIMEText(html_body, "html"))

    # Enviar
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.send_message(msg)

        logger.info(f"Email enviado a {ALERT_EMAIL}: {subject}")
        return True

    except smtplib.SMTPAuthenticationError:
        logger.error(
            "Error de autenticación SMTP. Verifica que el email y la "
            "App Password sean correctos. Para Gmail necesitas una App Password."
        )
        return False
    except Exception as e:
        logger.error(f"Error enviando email: {e}")
        return False


def send_test_email():
    """Envía un email de prueba para verificar la configuración."""
    if not SMTP_EMAIL or not SMTP_PASSWORD:
        logger.error("Configura SMTP_EMAIL y SMTP_PASSWORD en .env primero.")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "✅ Monitor CNSC - Prueba de conexión exitosa"
    msg["From"] = SMTP_EMAIL
    msg["To"] = ALERT_EMAIL

    html = """
    <html>
    <body style="font-family: Arial, sans-serif; text-align: center; padding: 40px;">
        <h1 style="color: #1a3a5c;">✅ Monitor CNSC Activo</h1>
        <p style="font-size: 16px; color: #333;">
            La configuración de email funciona correctamente.
        </p>
        <p style="color: #666;">
            A partir de ahora recibirás alertas automáticas cuando se detecten
            novedades en la página de la CNSC.
        </p>
        <hr style="margin: 30px 0; border: none; border-top: 1px solid #ddd;">
        <p style="font-size: 12px; color: #888;">
            Monitor CNSC - Ascenso Público
        </p>
    </body>
    </html>
    """
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.send_message(msg)

        logger.info(f"Email de prueba enviado a {ALERT_EMAIL}")
        return True
    except Exception as e:
        logger.error(f"Error enviando email de prueba: {e}")
        return False
