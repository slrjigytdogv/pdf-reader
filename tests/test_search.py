from pathlib import Path

import fitz

from pdfreader.toolkit.search import DocumentSearch


def test_search_finds_phrase(tmp_path: Path) -> None:
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), "portable document format")
    pdf = tmp_path / "doc.pdf"
    doc.save(str(pdf))
    doc.close()

    opened = fitz.open(str(pdf))
    hits = DocumentSearch(opened).query("portable")
    assert hits and hits[0].page == 0
    opened.close()
</｜｜DSML｜｜ parameter>
</｜｜DSML｜｜ invoke>
</｜｜DSML｜｜ calls>