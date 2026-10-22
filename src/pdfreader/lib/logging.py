"""Logging setup for the desktop app."""
from __future__ import annotations

import logging
from pathlib import Path

LOG_DIR = Path.home() / ".pdf-reader" / "logs"


def configure_logging(theme: str = "dark") -> logging.Logger:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("pdfreader")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(f"%(asctime)s [{theme}] %(levelname)s %(name)s: %(message)s")
    fh = logging.FileHandler(LOG_DIR / "reader.log", encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger