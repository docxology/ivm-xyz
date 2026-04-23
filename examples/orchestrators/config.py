"""
Paths for example scripts: base output directory and subfolders.

Environment: ``IVM_XYZ_OUTPUT_ROOT`` — path relative to the repository root, or
absolute. Default ``outputs`` (see /outputs/README.md at repo root).
"""

from __future__ import annotations

import os
from pathlib import Path

# examples/orchestrators/config.py -> parents[2] == repository root
_REPO_ROOT = Path(__file__).resolve().parents[2]


def repo_root() -> Path:
    """Absolute path to the ivm-xyz repository root."""
    return _REPO_ROOT


def output_root() -> Path:
    """Resolved base directory for generated example artifacts."""
    raw = os.environ.get("IVM_XYZ_OUTPUT_ROOT", "outputs").strip() or "outputs"
    p = Path(raw)
    if not p.is_absolute():
        p = _REPO_ROOT / p
    return p.resolve()


def plots_orchestrators_dir() -> Path:
    """Default folder for ``orch_plot_polyhedron`` PNGs: ``<root>/plots/orchestrators``."""
    d = output_root() / "plots" / "orchestrators"
    d.mkdir(parents=True, exist_ok=True)
    return d
