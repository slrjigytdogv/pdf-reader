"""OutlineExtractor — flattens the PDF bookmark tree into a navigable TOC."""
from __future__ import annotations

from dataclasses import dataclass

import fitz


@dataclass
class TocEntry:
    title: str
    page: int
    level: int


class OutlineExtractor:
    def __init__(self, document: fitz.Document) -> None:
        self.document = document

    def build(self) -> list[TocEntry]:
        raw = self.document.get_toc(simple=True)
        entries: list[TocEntry] = []
        for level, title, page in raw:
            entries.append(TocEntry(title=title.strip(), page=max(page - 1, 0), level=level))
        return entries

    def find(self, title: str) -> TocEntry | None:
        return next((e for e in self.build() if e.title.lower() == title.lower()), None)