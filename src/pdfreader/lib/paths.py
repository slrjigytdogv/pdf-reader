"""Path helpers for the PDF Reader cache and annotation store."""
from __future__ import annotations

import hashlib
from pathlib import Path

CACHE_ROOT = Path.home() / ".pdf-reader" / "cache"


def cache_key(pdf_path: Path) -> str:
    stat = pdf_path.stat()
    digest = hashlib.sha1(f"{pdf_path}:{stat.st_size}:{stat.st_mtime}".encode()).hexdigest()
    return digest[:16]


def page_cache_dir(pdf_path: Path) -> Path:
    target = CACHE_ROOT / cache_key(pdf_path)
    target.mkdir(parents=True, exist_ok=True)
    return target