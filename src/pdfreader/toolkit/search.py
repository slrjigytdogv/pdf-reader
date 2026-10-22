"""Full-document text search across rendered PDF pages."""
from __future__ import annotations

from dataclasses import dataclass

import fitz


@dataclass(frozen=True)
class SearchHit:
    page: int
    text: str
    rect: tuple[float, float, float, float]


class DocumentSearch:
    def __init__(self, document: fitz.Document, max_results: int = 500) -> None:
        self.document = document
        self.max_results = max_results

    def query(self, needle: str, case_sensitive: bool = False) -> list[SearchHit]:
        hits: list[SearchHit] = []
        for page_index in range(self.document.page_count):
            page = self.document.load_page(page_index)
            for rect in page.search_for(needle, quads=False):
                hits.append(
                    SearchHit(
                        page=page_index,
                        text=needle,
                        rect=(rect.x0, rect.y0, rect.x1, rect.y1),
                    )
                )
                if len(hits) >= self.max_results:
                    return hits
        if not case_sensitive:
            return hits
        return [h for h in hits if needle in h.text]