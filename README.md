# IVM-XYZ

A powerful Python package for computational geometry, providing tools for working with both XYZ (Cartesian) and IVM (Isotropic Vector Matrix / Quadray) coordinate systems. Inspired by R. Buckminster Fuller's Synergetics.

## Features

- **Robust Coordinate Conversion**: Precise and efficient transformations between XYZ and IVM coordinate systems
- **High-Precision Calculations**: Accurate volume and area calculations for scientific and engineering applications
- **Geometric Structures**: Predefined polyhedra following Buckminster Fuller's Concentric Hierarchy
- **Visualization Tools**: Plot and animate 3D geometric structures
- **Comprehensive Testing**: Extensive test suite ensuring reliability
- **Well-Documented**: Clear API documentation and usage examples

## Installation

### From source (uv)

```bash
git clone https://github.com/docxology/ivm-xyz.git
cd ivm-xyz
uv sync --all-extras
```

`uv sync` uses **`uv.lock`** when present for pinned dependency resolution.

### From source (pip)

```bash
git clone https://github.com/docxology/ivm-xyz.git
cd ivm-xyz
pip install -e ".[dev,visualization]"
```

### Dependencies

- Python 3.8+
- `numpy` (required)
- `matplotlib` (optional, for visualization; required to run visualization tests)
- `imageio` (optional, for GIF animation in visualization)

Minimal install (core math only):

```bash
pip install -r requirements.txt
```

## Repository layout

- **[AGENTS.md](AGENTS.md)** — Short index for tools and contributors (full detail: [docs/AGENTS.md](docs/AGENTS.md)).
- **[outputs/](outputs/)** — Default generated plots, logs, and reports (v0.2+; see [outputs/README.md](outputs/README.md)). **`images/`** is optional for explicit `output_folder="images"` (legacy v0.1 default).
- **`working/`** is listed in `.gitignore` for local scratch work; it is not part of the published tree.

## Quick Start

### Basic Usage

```python
from ivm_xyz import Vector, Tetrahedron, make_tet

# Create vectors
v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
v3 = Vector((0, 0, 1))

# Calculate tetrahedron volume
ivm_vol, xyz_vol = make_tet(v1, v2, v3)
print(f"IVM Volume: {ivm_vol:.6f}")
print(f"XYZ Volume: {xyz_vol:.6f}")

# Or create from edge lengths
tet = Tetrahedron(1, 1, 1, 1, 1, 1)
print(f"Unit tetrahedron IVM volume: {tet.ivm_volume():.6f}")
```

### Coordinate Conversion

```python
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz

# Convert Cartesian to Quadray
quadray = xyz_to_ivm(1.0, 2.0, 3.0)
print(f"Quadray coordinates: {quadray}")

# Convert back to Cartesian
xyz = ivm_to_xyz(*quadray)
print(f"XYZ coordinates: {xyz}")
```

### Working with Polyhedra

```python
from ivm_xyz.polyhedra import Cube, Octahedron
from ivm_xyz.core.vectors import Qvector

# Create polyhedra
cube = Cube()
octa = Octahedron()

# Transform polyhedra
scaled_cube = cube.scale(2.0)
translated_cube = cube.translate(Qvector((1, 0, 0, 0)))
```

### Visualization

```python
from ivm_xyz.visualization import PolyhedronPlotter

plotter = PolyhedronPlotter()  # default: outputs/plots/ (v0.2+); override with output_folder=...

# Add polyhedron
vertices = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

plotter.add_polyhedron(vertices, faces, "Tetrahedron", "tetrahedron.gif")
plotter.animate_polyhedron(save=True)
```

## Package Structure

```
ivm_xyz/
├── core/              # Core geometric calculations
│   ├── vectors.py     # Vector and Qvector classes
│   ├── tetrahedron.py # Tetrahedron volume calculations
│   ├── triangle.py    # Triangle area calculations
│   └── constants.py   # Mathematical constants
├── conversion/        # Coordinate conversion
│   └── converters.py  # XYZ <-> IVM conversion functions
├── polyhedra/         # Polyhedron definitions
│   ├── base.py        # Base Polyhedron class
│   ├── platonic.py    # Platonic solids
│   └── edge_counting.py # Edge counting functions
└── visualization/     # Visualization tools
    └── plotter.py     # PolyhedronPlotter class
```

## Documentation

- **Per-directory signposts**: Each of `ivm_xyz/`, `tests/`, `scripts/`, `docs/`, etc. has a `README.md` and `AGENTS.md` (see [AGENTS.md](AGENTS.md) for the map).
- **API Reference**: See [docs/API.md](docs/API.md) - Complete technical API with all method signatures and examples
- **Module Documentation**: See [docs/MODULES.md](docs/MODULES.md) - Comprehensive module-by-module documentation
- **Technical Reference**: See [docs/TECHNICAL_REFERENCE.md](docs/TECHNICAL_REFERENCE.md) - Deep technical details for developers
- **Documentation Index**: See [docs/DOCUMENTATION_INDEX.md](docs/DOCUMENTATION_INDEX.md) - Complete documentation guide and navigation
- **Agent Documentation**: See [docs/AGENTS.md](docs/AGENTS.md) - Development workflows and agent guidance
- **Background**: See [docs/BACKGROUND.md](docs/BACKGROUND.md) - Mathematical background and theory
- **Package Structure**: See [docs/STRUCTURE.md](docs/STRUCTURE.md) - Package organization and structure
- **Testing Summary**: See [docs/TESTING_SUMMARY.md](docs/TESTING_SUMMARY.md) - Testing overview and results

## Utility Scripts

The `scripts/` directory contains utility scripts for development:

- **`scripts/test_runner.py`**: Run tests with detailed logging and reporting
- **`scripts/generate_comprehensive_report.py`**: Generate comprehensive test reports
- **`scripts/verify_documentation.py`**: Verify documentation matches implementation

For more information, see [docs/AGENTS.md](docs/AGENTS.md#utility-scripts).

## Testing

From the **repository root**:

```bash
# Recommended (uv, all extras for visualization tests)
uv sync --all-extras
uv run python -m unittest discover tests
# or
uv run python -m pytest tests/

# Test runner (writes under outputs/logs/ and outputs/reports/)
uv run python scripts/test_runner.py

# Reports / doc verification
uv run python scripts/generate_comprehensive_report.py
uv run python scripts/verify_documentation.py
```

With **pip** only, install at least `pytest` and `matplotlib` to match CI-style runs, or expect visualization-related tests to be **skipped**.

The suite includes unit modules (`test_vectors.py`, `test_tetrahedron.py`, …) and comprehensive modules (`test_*_comprehensive.py`); see [docs/TESTING_SUMMARY.md](docs/TESTING_SUMMARY.md).

## Mathematical Background

This package implements:

- **Euler Volume Formula**: For tetrahedron volume calculation
- **Heron's Formula**: For triangle area calculation  
- **Quadray Coordinates**: 4D coordinate system for IVM
- **Concentric Hierarchy**: Buckminster Fuller's geometric system

The IVM (Isotropic Vector Matrix) coordinate system provides a tetrahedral coordination geometry that offers advantages in certain geometric calculations and spatial analysis.

## Examples

See [examples/README.md](examples/README.md) for how to run scripts with `uv run`.

- [examples/basic_usage.py](examples/basic_usage.py) — end-to-end slice of the API
- [examples/visualization_examples.py](examples/visualization_examples.py) — `PolyhedronPlotter` and optional GIF output
- [examples/orchestrators/](examples/orchestrators/) — many thin, single-purpose workflows ([index](examples/orchestrators/README.md))

## Contributing

Contributions are welcome! Please ensure:

- Code follows PEP 8 style guidelines
- All new code has corresponding tests
- Documentation is updated
- Tests pass before submitting

## License

MIT — see [LICENSE](LICENSE).

## References

- Buckminster Fuller, R. "Synergetics: Explorations in the Geometry of Thinking"
- [Martian Math](https://github.com/4dsolutions/MartianMath) - Original inspiration

## Acknowledgments

- Kirby Urner (4D Solutions) for foundational work
- Gerald de Jong for Euler volume formula modifications
