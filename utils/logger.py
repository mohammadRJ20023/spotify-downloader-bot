import logging
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


LOG_FILE = LOG_DIR / "konar.log"

logger = logging.getLogger("Konar")

logger.setlevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler() 
console_handler.setFormatter(formatter)

if not logger.handlers :
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    