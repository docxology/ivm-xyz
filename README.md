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

### From Source

```bash
git clone https://github.com/docxology/ivm-xyz.git
cd ivm-xyz
pip install -e .
```

### Dependencies

- Python 3.8+
- numpy
- matplotlib (optional, for visualization)
- imageio (optional, for animations)

Install dependencies:
```bash
pip install -r requirements.txt
```

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

plotter = PolyhedronPlotter(output_folder="images")

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

Run the test suite:

```bash
# Standard unittest
python -m unittest discover tests

# Using pytest
python -m pytest tests/

# Using test runner with detailed logging
python scripts/test_runner.py

# Generate comprehensive test report
python scripts/generate_comprehensive_report.py

# Verify documentation
python scripts/verify_documentation.py
```

The test suite includes:
- 6 unit test files covering all core functionality
- 4 comprehensive test files for integration and verification
- 78+ tests ensuring reliability and accuracy

## Mathematical Background

This package implements:

- **Euler Volume Formula**: For tetrahedron volume calculation
- **Heron's Formula**: For triangle area calculation  
- **Quadray Coordinates**: 4D coordinate system for IVM
- **Concentric Hierarchy**: Buckminster Fuller's geometric system

The IVM (Isotropic Vector Matrix) coordinate system provides a tetrahedral coordination geometry that offers advantages in certain geometric calculations and spatial analysis.

## Examples

See the `examples/` directory for more usage examples:
- `basic_usage.py`: Basic operations
- `visualization_examples.py`: Visualization examples

## Contributing

Contributions are welcome! Please ensure:

- Code follows PEP 8 style guidelines
- All new code has corresponding tests
- Documentation is updated
- Tests pass before submitting

## License

See [LICENSE](LICENSE) for details.

## References

- Buckminster Fuller, R. "Synergetics: Explorations in the Geometry of Thinking"
- [Martian Math](https://github.com/4dsolutions/MartianMath) - Original inspiration

## Acknowledgments

- Kirby Urner (4D Solutions) for foundational work
- Gerald de Jong for Euler volume formula modifications
