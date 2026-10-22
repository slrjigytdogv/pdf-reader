# Contributing to pdf-reader

Thanks for your interest in improving PDF Reader. This is a hobbyist, community-maintained desktop PDF reader written in Python.

## Development setup

```bash
git clone https://github.com/<org>/pdf-reader.git
cd pdf-reader
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Project layout

- `src/pdfreader/` — application package
- `src/pdfreader/toolkit/` — feature modules (render, annotate, toc, search)
- `src/pdfreader/lib/` — shared helpers (paths, logging, config)
- `config/` — default settings and keybindings
- `tests/` — pytest suite

## Style

- Python 3.11+, type hints required for public functions.
- Keep modules under ~400 lines; split by feature.
- Run `pytest -q` before opening a PR.

## Pull requests

1. Fork, branch from `main` (`feat/toc-outline`, `fix/search-crash`, …).
2. Add a test if you fix a bug or add a feature.
3. Describe the change and include a sample PDF if it reproduces a rendering issue.

## Reporting bugs

Include the PDF Reader version, your OS, the PDF's page count, and a minimal reproduction if possible. Attach a redacted PDF when it does not contain private data.