from pathlib import Path

import fitz
import pytest

from pdfreader.toolkit.render import PageRenderer


@pytest.fixture()
def sample_pdf(tmp_path: Path) -> Path:
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), "PDF Reader sample page")
    target = tmp_path / "sample.pdf"
    doc.save(str(target))
    doc.close()
    return target


def test_render_page_size(sample_pdf: Path) -> None:
    doc = fitz.open(str(sample_pdf))
    renderer = PageRenderer(dpi=72)
    image = renderer.render_page(doc, 0)
    assert image.width > 0
    assert image.height > 0
    doc.close()


def test_render_cache_returns_same_object(sample_pdf: Path) -> None:
    doc = fitz.open(str(sample_pdf))
    renderer = PageRenderer(dpi=72)
    a = renderer.render_page(doc, 0)
    b = renderer.render_page(doc, 0)
    assert a is b
    doc.close()