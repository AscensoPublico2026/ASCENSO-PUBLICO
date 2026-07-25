"""Monitor CNSC - Script principal.

Revisa periódicamente la web de la CNSC, detecta novedades
(noticias, resoluciones, PDFs con ejes temáticos, cronogramas, etc.)
y envía alertas por email a ascensopublico@gmail.com.

Uso:
    python main.py              → Ejecuta una revisión y sale
    python main.py --loop       → Ejecuta en bucle (cada hora)
    python main.py --test-email → Envía un email de prueba
"""
import argparse
import logging
import sys
import time
from datetime import datetime

import schedule

from src.config import CHECK_INTERVAL_MINUTES, LOGS_DIR
from src.scraper import check_for_updates
from src.pdf_reader import analyze_pdf
from src.emailer import send_alert_email, send_test_email

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(
            f"{LOGS_DIR}/monitor_{datetime.now().strftime('%Y%m%d')}.log",
            encoding="utf-8"
        ),
    ]
)
logger = logging.getLogger("monitor-cnsc")


def run_check():
    """Ejecuta una revisión completa de la CNSC."""
    logger.info("=" * 60)
    logger.info("Iniciando revisión de la CNSC...")
    logger.info("=" * 60)

    try:
        # 1. Scraper: detectar contenido nuevo
        results = check_for_updates()
        new_links = results["new_links"]
        new_pdfs = results["new_pdfs"]

        logger.info(f"Resultados: {len(new_links)} enlaces nuevos, {len(new_pdfs)} PDFs nuevos")

        # 2. Analizar PDFs nuevos (buscar keywords y fechas dentro)
        # Limitamos a 15 PDFs por ejecución para no sobrecargar
        MAX_PDFS_PER_RUN = 15
        pdf_analyses = []
        for pdf_url, pdf_text, pdf_source in new_pdfs[:MAX_PDFS_PER_RUN]:
            analysis = analyze_pdf(pdf_url, pdf_name=pdf_text)
            if analysis:
                pdf_analyses.append(analysis)

        if len(new_pdfs) > MAX_PDFS_PER_RUN:
            logger.info(
                f"Se encontraron {len(new_pdfs)} PDFs nuevos, "
                f"se analizaron los primeros {MAX_PDFS_PER_RUN}. "
                f"Los restantes se reportarán en el email sin análisis profundo."
            )

        # 3. Enviar email si hay novedades
        if new_links or new_pdfs:
            success = send_alert_email(new_links, new_pdfs, pdf_analyses)
            if success:
                logger.info("Alerta enviada por email correctamente.")
            else:
                logger.warning("No se pudo enviar el email de alerta.")
        else:
            logger.info("Sin novedades. No se envía email.")

        logger.info("Revisión completada.")
        return True

    except Exception as e:
        logger.error(f"Error durante la revisión: {e}", exc_info=True)
        return False


def run_loop():
    """Ejecuta el monitor en bucle según el intervalo configurado."""
    logger.info(f"Monitor CNSC iniciado en modo bucle (cada {CHECK_INTERVAL_MINUTES} minutos)")
    logger.info(f"Alertas se enviarán a: ascensopublico@gmail.com")

    # Primera ejecución inmediata
    run_check()

    # Programar ejecuciones periódicas
    schedule.every(CHECK_INTERVAL_MINUTES).minutes.do(run_check)

    while True:
        schedule.run_pending()
        time.sleep(30)


def main():
    parser = argparse.ArgumentParser(
        description="Monitor CNSC - Detecta novedades y envía alertas por email"
    )
    parser.add_argument(
        "--loop",
        action="store_true",
        help="Ejecutar en bucle continuo (revisa cada hora)"
    )
    parser.add_argument(
        "--test-email",
        action="store_true",
        help="Enviar un email de prueba para verificar la configuración"
    )

    args = parser.parse_args()

    if args.test_email:
        logger.info("Enviando email de prueba...")
        success = send_test_email()
        if success:
            print("\n✅ Email de prueba enviado correctamente a ascensopublico@gmail.com")
        else:
            print("\n❌ Error: No se pudo enviar el email. Revisa las credenciales en .env")
        sys.exit(0 if success else 1)

    if args.loop:
        run_loop()
    else:
        success = run_check()
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
