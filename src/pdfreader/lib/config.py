"""Configuration loading from TOML plus user overrides."""
from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

DEFAULT_CONFIG = Path(__file__).resolve().parents[3] / "config" / "default.toml"


def load_config(override: Path | None = None) -> dict[str, Any]:
    path = override or DEFAULT_CONFIG
    with path.open("rb") as fh:
        data = tomllib.load(fh)
    user_cfg = Path.home() / ".pdf-reader" / "config.toml"
    if user_cfg.exists():
        with user_cfg.open("rb") as fh:
            _deep_merge(data, tomllib.load(fh))
    return data


def _deep_merge(base: dict[str, Any], overlay: dict[str, Any]) -> None:
    for key, value in overlay.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value