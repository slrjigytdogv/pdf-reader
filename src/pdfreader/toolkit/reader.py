"""ReaderSession — owns the open document handle and page state."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF


@dataclass
class ReaderSession:
    path: Path
    document: fitz.Document
    current_page: int = 0
    config: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def open(cls, path: str | Path, config: dict[str, Any]) -> "ReaderSession":
        doc = fitz.open(str(path))
        return cls(path=Path(path), document=doc, config=config)

    @property
    def page_count(self) -> int:
        return self.document.page_count

    def goto(self, page: int) -> int:
        self.current_page = max(0, min(page, self.page_count - 1))
        return self.current_page

    def close(self) -> None:
        if not self.document.is_closed:
            self.document.close()