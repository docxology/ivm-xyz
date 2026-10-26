# `ivm_xyz.visualization`

## API

- [`PolyhedronPlotter`](plotter.py) — exported by `__init__.py` alongside `DEFAULT_PLOT_OUTPUT_DIR`; matplotlib imported at module load in `plotter.py`.

## Tests

- `tests/test_visualization.py`, `tests/test_visualization_comprehensive.py` — **skipped** when matplotlib is not installed (`tests/_support/optional_deps.py`).
- `tests/test_integration_comprehensive.py` — visualization workflow skipped without matplotlib.
- `tests/test_imports_comprehensive.py` — visualization import checks skipped without matplotlib.

## Runtime

Uses matplotlib `Agg` backend for headless file output.
