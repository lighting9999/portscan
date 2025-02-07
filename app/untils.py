import secrets
import logging
from datetime import datetime

logging.basicConfig(filename="scanner.log", level=logging.INFO)

def generate_api_key():
    return secrets.token_urlsafe(32)
def log_scan_result(host, result):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"[{timestamp}] Host:{host}, Result: {result}")
