"""Annotation store for highlights, notes, and bookmarks per document."""
from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, asdict
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS annotations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_key TEXT NOT NULL,
    page INTEGER NOT NULL,
    kind TEXT NOT NULL,
    payload TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_doc ON annotations(doc_key);
"""


@dataclass
class Annotation:
    page: int
    kind: str
    payload: dict


class AnnotationStore:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(db_path))
        self._conn.executescript(SCHEMA)

    def add(self, doc_key: str, annotation: Annotation) -> int:
        cur = self._conn.execute(
            "INSERT INTO annotations (doc_key, page, kind, payload) VALUES (?, ?, ?, ?)",
            (doc_key, annotation.page, annotation.kind, json.dumps(annotation.payload)),
        )
        self._conn.commit()
        return cur.lastrowid or -1

    def list_for(self, doc_key: str) -> list[Annotation]:
        rows = self._conn.execute(
            "SELECT page, kind, payload FROM annotations WHERE doc_key=? ORDER BY page",
            (doc_key,),
        ).fetchall()
        return [Annotation(page=p, kind=k, payload=json.loads(pl)) for p, k, pl in rows]

    def close(self) -> None:
        self._conn.close()