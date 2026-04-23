# `tests/` — agent reference

## Layout

- `test_*.py` — discovered by `unittest` / `pytest` (see [pyproject.toml](../pyproject.toml) `[tool.pytest.ini_options]`).
- `_support/` — not a test package prefix; contains `optional_deps` (matplotlib probe) and `fixtures` (shared geometry).

## Skips

- Any test importing `ivm_xyz.visualization` must run only when `HAS_MATPLOTLIB` is true, or it will fail at import time (matplotlib loaded by `plotter.py`).

## Composability

- Prefer importing shared vertex/face lists from `tests._support.fixtures` when writing new plot or volume checks.
