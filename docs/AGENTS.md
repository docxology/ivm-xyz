# IVM-XYZ Package Agent Documentation

## Package Overview

The `ivm_xyz` package provides tools for computational geometry working with both XYZ (Cartesian) and IVM (Isotropic Vector Matrix / Quadray) coordinate systems, inspired by R. Buckminster Fuller's Synergetics.

## Module Structure

For comprehensive module-by-module documentation, see [MODULES.md](MODULES.md).

### Core Module (`ivm_xyz.core`)

**Purpose**: Fundamental geometric calculations and data structures.

**Key Components**:
- `vectors.py`: Vector (XYZ) and Qvector (IVM Quadray) classes
- `tetrahedron.py`: Tetrahedron volume calculations
- `triangle.py`: Triangle area calculations
- `constants.py`: Mathematical constants (S3, PHI, ROOT2, etc.)

**See [MODULES.md](MODULES.md#core-modules) for detailed documentation.**

**Usage Pattern**:
```python
from ivm_xyz.core import Vector, Qvector, Tetrahedron, make_tet

# Create vectors
v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
v3 = Vector((0, 0, 1))

# Calculate tetrahedron volume
ivm_vol, xyz_vol = make_tet(v1, v2, v3)
```

### Conversion Module (`ivm_xyz.conversion`)

**Purpose**: Convert between XYZ and IVM coordinate systems.

**Key Functions**:
- `xyz_to_ivm(x, y, z)`: Convert Cartesian to Quadray
- `ivm_to_xyz(a, b, c, d)`: Convert Quadray to Cartesian
- `vector_to_qvector(vector)`: Convert Vector to Qvector
- `qvector_to_vector(qvector)`: Convert Qvector to Vector

**See [MODULES.md](MODULES.md#conversion-module) for detailed documentation.**

**Usage Pattern**:
```python
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz

# Convert coordinates
quadray = xyz_to_ivm(1.0, 2.0, 3.0)
xyz = ivm_to_xyz(*quadray)
```

### Polyhedra Module (`ivm_xyz.polyhedra`)

**Purpose**: Define and work with polyhedral structures.

**Key Components**:
- `base.py`: Base Polyhedron class and Edge class
- `platonic.py`: Platonic solids (Tetrahedron, Cube, Octahedron, Icosahedron, Cuboctahedron)
- `edge_counting.py`: Functions for counting edges in geometric structures

**See [MODULES.md](MODULES.md#polyhedra-modules) for detailed documentation.**

**Usage Pattern**:
```python
from ivm_xyz.polyhedra import Cube, Octahedron, tet_edges

# Create polyhedra
cube = Cube()
octa = Octahedron()

# Count edges
edges = tet_edges(5)  # Edges for frequency 5 tetrahedron
```

### Visualization Module (`ivm_xyz.visualization`)

**Purpose**: Visualize geometric structures.

**Key Components**:
- `plotter.py`: PolyhedronPlotter class for static plots and animations

**See [MODULES.md](MODULES.md#visualization-module) for detailed documentation.**

**Usage Pattern**:
```python
from ivm_xyz.visualization import PolyhedronPlotter

plotter = PolyhedronPlotter(output_folder="images")
plotter.add_polyhedron(vertices, faces, "Title", "output.gif")
plotter.animate_polyhedron(save=True)
```

## Common Workflows

### 1. Calculate Tetrahedron Volume

```python
from ivm_xyz import Vector, Tetrahedron

# Method 1: From edge lengths
tet = Tetrahedron(1, 1, 1, 1, 1, 1)
ivm_vol = tet.ivm_volume()
xyz_vol = tet.xyz_volume()

# Method 2: From vectors
from ivm_xyz import make_tet
v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
v3 = Vector((0, 0, 1))
ivm_vol, xyz_vol = make_tet(v1, v2, v3)
```

### 2. Convert Between Coordinate Systems

```python
from ivm_xyz import Vector, Qvector
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz

# Using functions
quadray = xyz_to_ivm(1.0, 2.0, 3.0)
xyz = ivm_to_xyz(*quadray)

# Using classes
v = Vector((1, 2, 3))
q = v.quadray()  # Convert to Quadray
v2 = q.xyz()     # Convert back to XYZ
```

### 3. Work with Polyhedra

```python
from ivm_xyz.polyhedra import Cube, Octahedron

# Create and transform
cube = Cube()
scaled = cube.scale(2.0)
from ivm_xyz.core.vectors import Qvector
translated = cube.translate(Qvector((1, 0, 0, 0)))
```

## Testing

### Test Files

All modules have corresponding test files in `tests/`:

**Unit Tests:**
- `test_vectors.py`: Basic Vector and Qvector tests (13 tests)
- `test_vector_advanced.py`: Advanced Vector methods - rotations, spherical coordinates, unit vectors, norm0, Svector (5 tests)
- `test_tetrahedron.py`: Tetrahedron calculation tests (11 tests)
- `test_triangle.py`: Triangle calculation tests (4 tests)
- `test_conversion.py`: Coordinate conversion tests (8 tests)
- `test_polyhedra.py`: Polyhedron tests (11 tests)
- `test_visualization.py`: Basic visualization tests (3 tests)

**Comprehensive Tests:**
- `test_functional_comprehensive.py`: Comprehensive functional verification
- `test_imports_comprehensive.py`: Import verification and module structure
- `test_integration_comprehensive.py`: End-to-end integration testing
- `test_visualization_comprehensive.py`: Comprehensive visualization testing

### Test Execution

Run all tests:
```bash
python -m unittest discover tests
# or
python -m pytest tests/
# or using the test runner script
python scripts/test_runner.py
```

Generate comprehensive test report:
```bash
python scripts/generate_comprehensive_report.py
```

Verify documentation:
```bash
python scripts/verify_documentation.py
```

## Utility Scripts

The `scripts/` directory contains utility scripts for development and maintenance:

### `scripts/test_runner.py`
Comprehensive test runner with detailed logging and reporting. Generates test reports with timing, success/failure counts, and detailed output.

**Usage:**
```bash
python scripts/test_runner.py
```

### `scripts/generate_comprehensive_report.py`
Generates comprehensive test reports including:
- Main test suite results
- Comprehensive test module results
- Documentation verification
- Module structure verification
- Test coverage summary

**Usage:**
```bash
python scripts/generate_comprehensive_report.py
```

### `scripts/verify_documentation.py`
Verifies that documentation matches implementation:
- Checks API documentation completeness
- Verifies all documented functions exist
- Validates module structure
- Checks README examples

**Usage:**
```bash
python scripts/verify_documentation.py
```

### `scripts/clone_4dsolutions.py`
Utility script for cloning reference code (development use only).

## Mathematical Background

The package implements:
- **Euler Volume Formula**: For tetrahedron volume calculation
- **Heron's Formula**: For triangle area calculation
- **Quadray Coordinates**: 4D coordinate system for IVM
- **Concentric Hierarchy**: Buckminster Fuller's geometric system

## Dependencies

- `numpy`: Numerical operations
- `matplotlib`: Visualization (optional)
- `imageio`: Animation (optional, for visualization)

## Extension Points

1. **New Polyhedra**: Subclass `Polyhedron` in `polyhedra/base.py`
2. **New Calculations**: Add to appropriate core module
3. **New Visualizations**: Extend `PolyhedronPlotter` or create new plotter classes

## Development Workflow

### Running Tests

1. **Quick test run:**
   ```bash
   python -m unittest discover tests
   ```

2. **Comprehensive test with logging:**
   ```bash
   python scripts/test_runner.py
   ```

3. **Generate full test report:**
   ```bash
   python scripts/generate_comprehensive_report.py
   ```

### Verifying Changes

1. **Run tests:**
   ```bash
   python scripts/test_runner.py
   ```

2. **Verify documentation:**
   ```bash
   python scripts/verify_documentation.py
   ```

3. **Check imports:**
   ```bash
   python tests/test_imports_comprehensive.py
   ```

### Project Structure

- **Package code**: `ivm_xyz/` - Main package modules
- **Tests**: `tests/` - All test files
- **Scripts**: `scripts/` - Utility scripts
- **Examples**: `examples/` - Usage examples
- **Documentation**: `docs/` - Documentation files
- **Archive**: `archive/` - Legacy files (reference only, not imported)
- **Working**: `working/` - Development workspace
