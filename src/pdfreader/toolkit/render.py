"""PageRenderer — rasterizes PDF pages to PIL images with a small LRU cache."""
from __future__ import annotations

from collections import OrderedDict

import fitz
from PIL import Image


class PageRenderer:
    def __init__(self, dpi: int = 144, cache_pages: int = 12) -> None:
        self.dpi = dpi
        self.cache_pages = cache_pages
        self._cache: "OrderedDict[tuple[int, int], Image.Image]" = OrderedDict()

    def render_page(self, document: fitz.Document, page_index: int) -> Image.Image:
        key = (id(document), page_index)
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]

        page = document.load_page(page_index)
        zoom = self.dpi / 72.0
        matrix = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

        self._cache[key] = image
        if len(self._cache) > self.cache_pages:
            self._cache.popitem(last=False)
        return image

    def clear(self) -> None:
        self._cache.clear()