# IVM-XYZ Package Structure

## Repository layout

```
ivm-xyz/
├── ivm_xyz/                 # Installable package (see per-subfolder README / AGENTS)
│   ├── core/
│   ├── conversion/
│   ├── polyhedra/
│   └── visualization/
├── tests/                   # unittest / pytest; _support/ for optional deps + fixtures
├── scripts/                 # Dev tools (run from repo root)
├── examples/                # Runnable examples; examples/orchestrators/ (thin CLIs, config)
├── docs/                    # API, MODULES, AGENTS, this file, etc.
├── archive/                 # Legacy reference only (not imported by ivm_xyz)
├── outputs/                 # Default generated logs / reports / plots (see outputs/README.md)
├── images/                  # Optional legacy path if output_folder="images" (v0.1)
├── working/                 # Local scratch — gitignored; forked_from_SoT/ reference files are tracked
├── README.md
├── AGENTS.md                # Short index; full agent doc is docs/AGENTS.md
├── pyproject.toml
├── requirements.txt
└── LICENSE
```

There is no `FINAL_AUDIT_REPORT.md` or root `TESTING_SUMMARY.md`; testing notes live under **[TESTING_SUMMARY.md](TESTING_SUMMARY.md)** in this directory.

## Module responsibilities

### Core (`ivm_xyz.core`)

- **vectors.py**: `Vector` (XYZ), `Qvector` (quadray)
- **tetrahedron.py**: `Tetrahedron`, `make_tet`
- **triangle.py**: `Triangle`, `make_tri`
- **constants.py**: `S3`, `PHI`, `ROOT2`, etc.

### Conversion (`ivm_xyz.conversion`)

- **converters.py**: `xyz_to_ivm`, `ivm_to_xyz`, `vector_to_qvector`, `qvector_to_vector`

### Polyhedra (`ivm_xyz.polyhedra`)

- **base.py**: `Polyhedron`, `Edge`
- **platonic.py**: Platonic solids; tetrahedron class exported as `PolyTetrahedron` in `__init__.py` to avoid clashing with `core.Tetrahedron`
- **edge_counting.py**: `tet_edges`, `half_oct_edges`, `oct_edges`, `cubocta_edges`, `cubocta_layer`

### Visualization (`ivm_xyz.visualization`)

- **plotter.py**: `PolyhedronPlotter` (requires **matplotlib** at import time); default save directory is **`outputs/plots`** (v0.2+); re-exported **`DEFAULT_PLOT_OUTPUT_DIR`**

## Import structure

### Package entry

```python
from ivm_xyz import (
    Vector, Qvector,
    Tetrahedron, make_tet, Triangle, make_tri,
    xyz_to_ivm, ivm_to_xyz,
)
```

### Submodules

```python
from ivm_xyz.core import Vector, Qvector, Tetrahedron, make_tet, Triangle, make_tri
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz
from ivm_xyz.polyhedra import Cube, Octahedron, tet_edges
from ivm_xyz.visualization import PolyhedronPlotter, DEFAULT_PLOT_OUTPUT_DIR  # needs matplotlib
```

## Testing

Run from the **repository root** (see [TESTING_SUMMARY.md](TESTING_SUMMARY.md)):

```bash
uv sync --all-extras
uv run python -m unittest discover tests
# or
uv run pytest tests/
# or
uv run python scripts/test_runner.py
```

Visualization tests are **skipped** when `matplotlib` is not installed.

## Documentation map

- **[README.md](../README.md)**: User-facing overview
- **[AGENTS.md](../AGENTS.md)**: Repository index for agents
- **[docs/AGENTS.md](AGENTS.md)**: Full developer / agent guide
- **[docs/DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md)**: Topic index
- **[docs/MODULES.md](MODULES.md)**: Module-by-module reference

## Additional directories

- **archive/**: Old scripts; not wired into the package
- **outputs/**: Default `outputs/plots`, `outputs/logs`, `outputs/reports` (see [outputs/README.md](../outputs/README.md))
- **images/**: Optional explicit path; v0.1 default was here
- **working/**: Gitignored local experiments (documented in root AGENTS / README); the `forked_from_SoT/` reference forks are the only tracked entries
