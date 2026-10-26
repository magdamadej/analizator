import logging
from pathlib import Path


def konfiguruj_logowanie():
    folder = Path("logs")
    folder.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=folder / "app.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8"
    )