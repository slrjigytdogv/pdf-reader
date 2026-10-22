"""Application entry point: wires the toolkit modules into a runnable app."""
from __future__ import annotations

import click

from pdfreader.lib.config import load_config
from pdfreader.lib.logging import configure_logging
from pdfreader.toolkit.reader import ReaderSession
from pdfreader.toolkit.render import PageRenderer
from pdfreader.toolkit.search import DocumentSearch
from pdfreader.toolkit.toc import OutlineExtractor


@click.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
@click.option("--dpi", default=None, type=int, help="Override render DPI.")
def main(path: str, dpi: int | None) -> int:
    cfg = load_config()
    configure_logging(cfg.get("app", {}).get("theme", "dark"))

    session = ReaderSession.open(path, cfg)
    renderer = PageRenderer(dpi=dpi or cfg["render"]["dpi"])
    outline = OutlineExtractor(session.document).build()
    search = DocumentSearch(session.document)

    click.echo(f"Opened {path} ({session.page_count} pages, {len(outline)} bookmarks)")
    first = renderer.render_page(session.document, 0)
    click.echo(f"Rendered page 1 at {first.width}x{first.height}px")
    _ = search  # kept alive for interactive frontends
    session.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())