#!/usr/bin/env python3
"""Compatibility wrapper for the relocated ContextLedger CLI."""

from __future__ import annotations

import sys
from pathlib import Path


def _prepare_path() -> None:
    """Ensure the editable package is importable when run as a script."""

    repo_root = Path(__file__).resolve().parents[1]
    src_dir = repo_root / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))


_prepare_path()

from contextledger.cli import main


if __name__ == "__main__":
    main()
