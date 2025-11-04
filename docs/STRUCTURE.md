# IVM-XYZ Package Structure

## Complete Package Organization

```
ivm-xyz/
├── ivm_xyz/                    # Main package
│   ├── __init__.py            # Package exports
│   ├── core/                  # Core geometric calculations
│   │   ├── __init__.py
│   │   ├── vectors.py         # Vector, Qvector classes
│   │   ├── tetrahedron.py     # Tetrahedron volume calculations
│   │   ├── triangle.py        # Triangle area calculations
│   │   └── constants.py       # Mathematical constants
│   ├── conversion/            # Coordinate conversion
│   │   ├── __init__.py
│   │   └── converters.py     # xyz_to_ivm, ivm_to_xyz
│   ├── polyhedra/             # Polyhedron definitions
│   │   ├── __init__.py
│   │   ├── base.py           # Base Polyhedron class
│   │   ├── platonic.py       # Platonic solids
│   │   └── edge_counting.py   # Edge counting functions
│   └── visualization/        # Visualization tools
│       ├── __init__.py
│       └── plotter.py        # PolyhedronPlotter
├── tests/                     # Test suite
│   ├── __init__.py
│   ├── test_vectors.py        # Basic Vector and Qvector tests (13 tests)
│   ├── test_vector_advanced.py # Advanced Vector methods (rotations, spherical, Svector) (5 tests)
│   ├── test_tetrahedron.py    # Tetrahedron volume calculations (11 tests)
│   ├── test_triangle.py       # Triangle area calculations (4 tests)
│   ├── test_conversion.py     # Coordinate conversion tests (8 tests)
│   ├── test_polyhedra.py      # Polyhedra operations (11 tests)
│   ├── test_visualization.py # Basic visualization tests (3 tests)
│   ├── test_functional_comprehensive.py # Comprehensive functional verification (7 tests)
│   ├── test_imports_comprehensive.py # Import verification (8 tests)
│   ├── test_integration_comprehensive.py # Integration testing (5 tests)
│   └── test_visualization_comprehensive.py # Comprehensive visualization (7 tests)
├── scripts/                   # Utility scripts
│   ├── generate_comprehensive_report.py  # Generate test reports
│   ├── test_runner.py         # Test runner with logging
│   ├── verify_documentation.py  # Verify documentation accuracy
│   └── clone_4dsolutions.py  # Utility script
├── examples/                  # Example scripts
│   ├── basic_usage.py
│   └── visualization_examples.py
├── docs/                      # Documentation
│   ├── .cursorrules          # Development rules
│   ├── AGENTS.md             # Agent documentation
│   ├── API.md                # API reference
│   ├── BACKGROUND.md         # Background information
│   ├── STRUCTURE.md          # Package structure (this file)
│   └── TESTING_SUMMARY.md    # Testing summary
├── archive/                   # Legacy files (reference only)
│   ├── qrays.py
│   ├── tetravolume.py
│   ├── tetravolume_2.py
│   ├── tetravolume_3.py
│   ├── visualize.py
│   ├── visualize_2.py
│   └── tests.py
├── working/                   # Development workspace
│   └── forked_from_SoT/       # Forked code reference
│       ├── convert.py
│       ├── flextegrity.py
│       ├── ivm_tetra_edges.py
│       ├── polyhedra.py
│       └── verifications.py
├── images/                    # Generated visualization images
│   ├── cube.gif
│   ├── dodecahedron.gif
│   ├── octahedron.gif
│   ├── pyramid.gif
│   └── tetrahedron.gif
├── setup.py                  # Package installation
├── pyproject.toml            # Modern Python packaging
├── requirements.txt          # Dependencies
├── README.md                 # Main documentation
├── FINAL_AUDIT_REPORT.md     # Legacy code audit report
├── TESTING_SUMMARY.md        # Testing summary report
└── LICENSE                   # License file
```

## Module Responsibilities

### Core Module (`ivm_xyz.core`)
- **vectors.py**: Fundamental Vector (XYZ) and Qvector (IVM Quadray) classes
- **tetrahedron.py**: Tetrahedron volume calculations using Euler's formula
- **triangle.py**: Triangle area calculations using Heron's formula
- **constants.py**: Mathematical constants (S3, PHI, ROOT2, etc.)

### Conversion Module (`ivm_xyz.conversion`)
- **converters.py**: Bidirectional conversion between XYZ and IVM coordinate systems

### Polyhedra Module (`ivm_xyz.polyhedra`)
- **base.py**: Base Polyhedron class with scaling and translation
- **platonic.py**: Platonic solids (Tetrahedron, Cube, Octahedron, Icosahedron, Cuboctahedron)
- **edge_counting.py**: Functions for counting edges in geometric structures

### Visualization Module (`ivm_xyz.visualization`)
- **plotter.py**: PolyhedronPlotter for static plots and animated GIFs

## Package Statistics

- **14 Python modules** in the package
- **11 test files** (7 unit test files + 4 comprehensive test files)
- **83+ tests** total (all passing)
- **2 example scripts**
- **4 utility scripts** in `scripts/` directory
- **All tests passing** ✅

## Import Structure

### Main Package Imports
```python
from ivm_xyz import (
    Vector, Qvector,
    Tetrahedron, make_tet,
    Triangle, make_tri,
    xyz_to_ivm, ivm_to_xyz
)
```

### Module-Specific Imports
```python
from ivm_xyz.core import Vector, Qvector, Tetrahedron
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz
from ivm_xyz.polyhedra import Cube, Octahedron, tet_edges
from ivm_xyz.visualization import PolyhedronPlotter
```

## Testing

### Test Files

**Unit Tests:**
- `test_vectors.py` - Basic Vector and Qvector operations (13 tests)
- `test_vector_advanced.py` - Advanced Vector methods: rotations, spherical coordinates, unit vectors, norm0, Svector (5 tests)
- `test_tetrahedron.py` - Tetrahedron volume calculations (11 tests)
- `test_triangle.py` - Triangle area calculations (4 tests)
- `test_conversion.py` - Coordinate conversions (8 tests)
- `test_polyhedra.py` - Polyhedra operations (11 tests)
- `test_visualization.py` - Basic visualization tools (3 tests)

**Comprehensive Tests:**
- `test_functional_comprehensive.py` - Comprehensive functional verification
- `test_imports_comprehensive.py` - Import verification
- `test_integration_comprehensive.py` - Integration testing
- `test_visualization_comprehensive.py` - Comprehensive visualization testing

### Test Execution

Run all tests:
```bash
python -m unittest discover tests
# or
python scripts/test_runner.py
```

Generate comprehensive test report:
```bash
python scripts/generate_comprehensive_report.py
```

All tests pass with comprehensive coverage:
- ✅ Vector and Qvector operations
- ✅ Tetrahedron volume calculations
- ✅ Triangle area calculations
- ✅ Coordinate conversions
- ✅ Polyhedra operations
- ✅ Visualization tools
- ✅ Integration workflows
- ✅ Documentation verification

## Documentation

### Main Documentation Files

- **README.md**: Comprehensive usage guide and quick start
- **FINAL_AUDIT_REPORT.md**: Legacy code audit report (confirms no legacy code)
- **TESTING_SUMMARY.md**: Comprehensive testing summary

### Documentation Directory (`docs/`)

- **API.md**: Complete API reference with examples
- **MODULES.md**: Comprehensive module-by-module documentation
- **AGENTS.md**: Agent documentation and workflows
- **BACKGROUND.md**: Background information on IVM and Synergetics
- **STRUCTURE.md**: Package structure documentation (this file)
- **TESTING_SUMMARY.md**: Testing summary documentation
- **.cursorrules**: Development guidelines and rules

### Additional Directories

- **archive/**: Legacy files kept for reference only (not imported)
- **working/**: Development workspace with forked code reference
- **images/**: Generated visualization images (GIFs)
- **scripts/**: Utility scripts for testing and verification

