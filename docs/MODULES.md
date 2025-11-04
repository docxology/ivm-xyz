# IVM-XYZ Module Documentation

Comprehensive documentation for all modules in the IVM-XYZ package.

## Table of Contents

1. [Core Modules](#core-modules)
   - [vectors.py](#vectorspy)
   - [tetrahedron.py](#tetrahedronpy)
   - [triangle.py](#trianglepy)
   - [constants.py](#constantspy)
2. [Conversion Module](#conversion-module)
   - [converters.py](#converterspy)
3. [Polyhedra Modules](#polyhedra-modules)
   - [base.py](#basepy)
   - [platonic.py](#platonicpy)
   - [edge_counting.py](#edge_countingpy)
4. [Visualization Module](#visualization-module)
   - [plotter.py](#plotterpy)

---

## Core Modules

### vectors.py

**Purpose**: Vector classes for XYZ (Cartesian) and IVM (Quadray) coordinate systems.

**Location**: `ivm_xyz/core/vectors.py`

#### Classes

##### `Vector`

3D vector in XYZ (Cartesian) coordinate system.

**Attributes**:
- `xyz`: Named tuple containing (x, y, z) coordinates
- `x`, `y`, `z`: Properties accessing individual coordinates

**Methods**:

- `__init__(arg)`: Initialize from (x, y, z) tuple or iterable
- `__repr__()`: String representation
- `__mul__(scalar)`: Multiply by scalar (returns new Vector)
- `__rmul__(scalar)`: Right multiplication by scalar
- `__truediv__(scalar)`: Divide by scalar
- `__add__(v1)`: Add another vector
- `__sub__(v1)`: Subtract another vector
- `__neg__()`: Negate vector
- `unit()`: Return unit vector in same direction
- `dot(v1)`: Dot product with another vector
- `cross(v1)`: Cross product with another vector
- `length()`: Return vector length (magnitude)
- `angle(v1)`: Angle between vectors in degrees
- `rotaxis(vAxis, deg)`: Rotate around arbitrary axis by degrees
- `rotx(deg)`: Rotate around X-axis by degrees
- `roty(deg)`: Rotate around Y-axis by degrees
- `rotz(deg)`: Rotate around Z-axis by degrees
- `spherical()`: Convert to spherical coordinates (r, phi, theta)
- `quadray()`: Convert to Qvector (Quadray coordinates)

**Example**:
```python
from ivm_xyz.core.vectors import Vector

v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))
v_sum = v1 + v2
dot_product = v1.dot(v2)
length = v1.length()
rotated = v1.rotx(45)  # Rotate 45 degrees around X-axis
```

##### `Qvector`

4D vector in IVM (Quadray) coordinate system.

**Attributes**:
- `coords`: Named tuple containing (a, b, c, d) coordinates
- `a`, `b`, `c`, `d`: Properties accessing individual coordinates

**Methods**:

- `__init__(arg)`: Initialize from (a, b, c, d) tuple
- `__repr__()`: String representation
- `__eq__(other)`: Equality comparison
- `__lt__(other)`, `__gt__(other)`: Comparison operators
- `__hash__()`: Hash for use in sets/dicts
- `__mul__(scalar)`: Multiply by scalar
- `__rmul__(scalar)`: Right multiplication
- `__truediv__(scalar)`: Divide by scalar
- `__add__(v1)`: Add another Qvector
- `__sub__(v1)`: Subtract another Qvector
- `__neg__()`: Negate Qvector
- `norm(arg)`: Normalize such that all components are non-negative
- `norm0()`: Normalize such that sum of components equals 0
- `dot(v1)`: Dot product with another Qvector
- `length()`: Return vector length
- `cross(v1)`: Cross product with another Qvector
- `angle(v1)`: Angle between Qvectors in degrees
- `xyz()`: Convert to Vector (XYZ coordinates)

**Example**:
```python
from ivm_xyz.core.vectors import Qvector

q1 = Qvector((1, 0, 0, 0))
q2 = Qvector((0, 1, 0, 0))
q_sum = q1 + q2
v = q1.xyz()  # Convert to XYZ
q_back = v.quadray()  # Convert back
```

##### `Svector`

Subclass of Vector that takes spherical coordinate arguments.

**Inheritance**: Inherits all methods from `Vector` class

**Methods**:
- `__init__(arg)`: Initialize from (r, phi, theta) tuple or regular vector coordinates
  - If input is a vector, converts to spherical first
  - Converts spherical coords (r, phi, theta) to XYZ using standard conversion
- `__repr__()`: String representation as spherical coordinates
- All Vector methods: Inherits all methods including rotations, dot product, etc.

**Technical Details**:
- Converts spherical coordinates to XYZ: `x = r * cos(theta) * sin(phi)`, `y = r * sin(theta) * sin(phi)`, `z = r * cos(phi)`
- Angles are in degrees: `phi` (0-180 from Z-axis), `theta` (-180 to 180 in XY plane)
- Coordinates are rounded to 15 decimal places for precision

**Example**:
```python
from ivm_xyz.core.vectors import Svector

# From spherical coordinates
sv = Svector((1.0, 45.0, 30.0))  # r=1, phi=45°, theta=30°

# From regular vector (converts to spherical first)
v = Vector((1, 0, 0))
sv2 = Svector((v.x, v.y, v.z))  # Converts to spherical, then back to XYZ
```

#### Module-Level Functions

##### `dot(a, b)`

Convenience function for dot product calculation.

**Signature**: `dot(a: Vector, b: Vector) -> float`

**Parameters**:
- `a` (Vector or Qvector): First vector
- `b` (Vector or Qvector): Second vector

**Returns**: `float` - Dot product scalar

**Implementation**: Calls `a.dot(b)`

**Example**:
```python
from ivm_xyz.core.vectors import Vector, dot

v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))
d = dot(v1, v2)  # 32.0
```

##### `cross(a, b)`

Convenience function for cross product calculation.

**Signature**: `cross(a: Vector, b: Vector) -> Vector`

**Parameters**:
- `a` (Vector or Qvector): First vector
- `b` (Vector or Qvector): Second vector

**Returns**: `Vector` or `Qvector` - Cross product vector

**Implementation**: Calls `a.cross(b)`

**Example**:
```python
from ivm_xyz.core.vectors import Vector, cross

v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
c = cross(v1, v2)  # Vector with (0, 0, 1)
```

##### `angle(a, b)`

Convenience function for angle calculation.

**Signature**: `angle(a: Vector, b: Vector) -> float`

**Parameters**:
- `a` (Vector or Qvector): First vector
- `b` (Vector or Qvector): Second vector

**Returns**: `float` - Angle in degrees (0-180)

**Implementation**: Calls `a.angle(b)`

**Example**:
```python
from ivm_xyz.core.vectors import Vector, angle

v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
a = angle(v1, v2)  # 90.0 degrees
```

##### `length(a)`

Convenience function for length calculation.

**Signature**: `length(a: Vector) -> float`

**Parameters**:
- `a` (Vector or Qvector): Vector

**Returns**: `float` - Vector length

**Implementation**: Calls `a.length()`

**Example**:
```python
from ivm_xyz.core.vectors import Vector, length

v = Vector((3, 4, 0))
l = length(v)  # 5.0
```

---

### tetrahedron.py

**Purpose**: Tetrahedron volume calculations in IVM and XYZ coordinate systems.

**Location**: `ivm_xyz/core/tetrahedron.py`

#### Classes

##### `Tetrahedron`

Represents a tetrahedron with six edge lengths.

**Edge Configuration**:
- Faces: (a,b,d), (b,c,e), (c,a,f), (d,e,f) - opposite face
- Edges a, b, c from one vertex; d, e, f are opposite edges

**Attributes**:
- `a`, `b`, `c`, `d`, `e`, `f`: Edge lengths
- `a2`, `b2`, `c2`, `d2`, `e2`, `f2`: Squared edge lengths

**Methods**:

- `__init__(a, b, c, d, e, f)`: Initialize with six edge lengths
- `ivm_volume()`: Calculate volume in IVM units using Euler's formula
- `xyz_volume()`: Calculate volume in XYZ units (converted from IVM)
- `_addopen()`: Internal: Sum of open products
- `_addclosed()`: Internal: Sum of closed products (face products)
- `_addopposite()`: Internal: Sum of opposite edge pair products

**Mathematical Background**:
Uses Euler's volume formula modified by Gerald de Jong. The volume is calculated as:
```
ivm_vol = sqrt((addopen - addclosed - addopposite) / 2)
xyz_vol = ivm_vol / S3
```

**Example**:
```python
from ivm_xyz.core.tetrahedron import Tetrahedron

# Unit tetrahedron (all edges equal)
tet = Tetrahedron(1, 1, 1, 1, 1, 1)
ivm_vol = tet.ivm_volume()
xyz_vol = tet.xyz_volume()
```

#### Functions

##### `make_tet(v0, v1, v2)`

Create tetrahedron from three vectors and calculate volumes.

**Parameters**:
- `v0`, `v1`, `v2`: Three vectors (must have `length()` method)

**Returns**:
- `tuple`: (ivm_volume, xyz_volume)

**Example**:
```python
from ivm_xyz.core.tetrahedron import make_tet
from ivm_xyz.core.vectors import Vector

v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
v3 = Vector((0, 0, 1))
ivm_vol, xyz_vol = make_tet(v1, v2, v3)
```

---

### triangle.py

**Purpose**: Triangle area calculations in IVM and XYZ coordinate systems.

**Location**: `ivm_xyz/core/triangle.py`

#### Classes

##### `Triangle`

Represents a triangle with three edge lengths.

**Attributes**:
- `a`, `b`, `c`: Edge lengths

**Methods**:

- `__init__(a, b, c)`: Initialize with three edge lengths
- `ivm_area()`: Calculate area in IVM units using Heron's formula
- `xyz_area()`: Calculate area in XYZ units (converted from IVM)

**Mathematical Background**:
Uses Heron's formula:
```
s = (a + b + c) / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))
xyz_area = ivm_area / S3
```

**Example**:
```python
from ivm_xyz.core.triangle import Triangle

# Equilateral triangle
tri = Triangle(1, 1, 1)
ivm_area = tri.ivm_area()
xyz_area = tri.xyz_area()
```

#### Functions

##### `make_tri(v0, v1)`

Create triangle from two vectors and calculate areas.

**Parameters**:
- `v0`, `v1`: Two vectors (must have `length()` method)

**Returns**:
- `tuple`: (ivm_area, xyz_area)

**Example**:
```python
from ivm_xyz.core.triangle import make_tri
from ivm_xyz.core.vectors import Vector

v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
ivm_area, xyz_area = make_tri(v1, v2)
```

---

### constants.py

**Purpose**: Mathematical constants used throughout the package.

**Location**: `ivm_xyz/core/constants.py`

#### Constants

- `S3`: Conversion factor between IVM and XYZ volumes = √(9/8) ≈ 1.06066
- `ROOT2`: Square root of 2 = √2 ≈ 1.41421
- `ROOT3`: Square root of 3 = √3 ≈ 1.73205
- `ROOT5`: Square root of 5 = √5 ≈ 2.23607
- `PHI`: Golden ratio = (1 + √5) / 2 ≈ 1.61803
- `R`: Radius constant = 0.5
- `D`: Diameter constant = 1.0

**Example**:
```python
from ivm_xyz.core.constants import S3, PHI, ROOT2

# Convert IVM volume to XYZ
ivm_vol = 1.0
xyz_vol = ivm_vol / S3
```

---

## Conversion Module

### converters.py

**Purpose**: Coordinate conversion functions between XYZ and IVM systems.

**Location**: `ivm_xyz/conversion/converters.py`

#### Functions

##### `xyz_to_ivm(x, y, z)`

Convert XYZ 3D coordinates to IVM 4D quadray coordinates.

**Parameters**:
- `x` (float): X coordinate
- `y` (float): Y coordinate
- `z` (float): Z coordinate

**Returns**:
- `tuple`: IVM (quadray) coordinates (a, b, c, d)

**Example**:
```python
from ivm_xyz.conversion import xyz_to_ivm

quadray = xyz_to_ivm(1.0, 2.0, 3.0)
print(quadray)  # (a, b, c, d)
```

##### `ivm_to_xyz(a, b, c, d)`

Convert IVM 4D quadray coordinates to XYZ 3D coordinates.

**Parameters**:
- `a`, `b`, `c`, `d` (float): IVM (quadray) coordinates

**Returns**:
- `tuple`: XYZ coordinates (x, y, z)

**Example**:
```python
from ivm_xyz.conversion import ivm_to_xyz

xyz = ivm_to_xyz(1.0, 0.0, 0.0, 0.0)
print(xyz)  # (x, y, z)
```

##### `vector_to_qvector(vector)`

Convert a Vector object to a Qvector object.

**Parameters**:
- `vector`: Vector object (XYZ coordinates)

**Returns**:
- `Qvector`: Quadray representation

**Example**:
```python
from ivm_xyz.conversion import vector_to_qvector
from ivm_xyz.core.vectors import Vector

v = Vector((1, 2, 3))
q = vector_to_qvector(v)
```

##### `qvector_to_vector(qvector)`

Convert a Qvector object to a Vector object.

**Parameters**:
- `qvector`: Qvector object (IVM coordinates)

**Returns**:
- `Vector`: XYZ representation

**Example**:
```python
from ivm_xyz.conversion import qvector_to_vector
from ivm_xyz.core.vectors import Qvector

q = Qvector((1, 0, 0, 0))
v = qvector_to_vector(q)
```

**Round-Trip Conversion**:
```python
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz

# Convert XYZ -> IVM -> XYZ
xyz_orig = (1.0, 2.0, 3.0)
quadray = xyz_to_ivm(*xyz_orig)
xyz_back = ivm_to_xyz(*quadray)
# Round-trip error should be minimal (within floating point precision)
```

---

## Polyhedra Modules

### base.py

**Purpose**: Base Polyhedron class and Edge class for geometric structures.

**Location**: `ivm_xyz/polyhedra/base.py`

#### Classes

##### `Polyhedron`

Base class for polyhedra. Designed to be subclassed, not used directly.

**Attributes** (expected in subclasses):
- `vertexes`: Dictionary mapping vertex names to Vector/Qvector objects
- `faces`: Tuple of face tuples, each containing vertex names
- `edges`: List of Edge objects (auto-generated from faces)
- `volume`: Volume of the polyhedron
- `center`: Center point of the polyhedron
- `name`: Name of the polyhedron

**Methods**:

- `scale(scalefactor)`: Scale polyhedron by factor
  - Returns new instance of same type
  - Scales vertices and volume
- `translate(vector)`: Translate polyhedron by vector
  - Returns new instance of same type
  - Translates vertices and center
- `_distill()`: Extract unique edges from faces
  - Returns list of Edge objects
  - Internal method, automatically called

**Operators**:
- `__mul__` / `__rmul__`: Alias for `scale()`
- `__add__` / `__radd__`: Alias for `translate()`

**Example**:
```python
from ivm_xyz.polyhedra.base import Polyhedron
from ivm_xyz.polyhedra import Cube
from ivm_xyz.core.vectors import Qvector

cube = Cube()
scaled = cube.scale(2.0)  # Double size
translated = cube.translate(Qvector((1, 0, 0, 0)))
```

##### `Edge`

Represents an edge connecting two vertices.

**Attributes**:
- `v0`: First vertex (Vector or Qvector)
- `v1`: Second vertex (Vector or Qvector)

**Methods**:

- `__init__(v0, v1)`: Initialize edge with two vertices
- `__repr__()`: String representation

**Example**:
```python
from ivm_xyz.polyhedra.base import Edge
from ivm_xyz.core.vectors import Vector

v1 = Vector((0, 0, 0))
v2 = Vector((1, 0, 0))
edge = Edge(v1, v2)
```

---

### platonic.py

**Purpose**: Platonic solids and geometric structures defined using IVM coordinates.

**Location**: `ivm_xyz/polyhedra/platonic.py`

#### Classes

All classes inherit from `Polyhedron` and follow Buckminster Fuller's Concentric Hierarchy.

##### `Tetrahedron` (PolyTetrahedron when imported)

Regular tetrahedron.

**Properties**:
- Volume: 1 (IVM units)
- Vertices: 4
- Faces: 4 triangles
- Edges: 6

**Example**:
```python
from ivm_xyz.polyhedra import PolyTetrahedron

tet = PolyTetrahedron()
print(f"{tet.name}: Volume = {tet.volume}")
```

##### `Cube`

Regular cube.

**Properties**:
- Volume: 3 (IVM units)
- Vertices: 8
- Faces: 6 squares
- Edges: 12

**Example**:
```python
from ivm_xyz.polyhedra import Cube

cube = Cube()
scaled = cube.scale(2.0)
```

##### `Octahedron`

Regular octahedron.

**Properties**:
- Volume: 4 (IVM units)
- Vertices: 6
- Faces: 8 triangles
- Edges: 12

**Example**:
```python
from ivm_xyz.polyhedra import Octahedron

octa = Octahedron()
```

##### `Icosahedron`

Regular icosahedron.

**Properties**:
- Volume: ~18.51 (IVM units)
- Vertices: 12
- Faces: 20 triangles
- Edges: 30

**Example**:
```python
from ivm_xyz.polyhedra import Icosahedron

icosa = Icosahedron()
```

##### `Cuboctahedron`

Cuboctahedron.

**Properties**:
- Volume: 20 (IVM units)
- Vertices: 12
- Faces: 14 (8 triangles, 6 squares)
- Edges: 24

**Example**:
```python
from ivm_xyz.polyhedra import Cuboctahedron

cubocta = Cuboctahedron()
```

**Note**: All polyhedra are defined using canonical IVM coordinates and follow Fuller's Concentric Hierarchy.

---

### edge_counting.py

**Purpose**: Edge counting functions for geometric structures.

**Location**: `ivm_xyz/polyhedra/edge_counting.py`

#### Functions

##### `tri(n)`

Calculate triangular number n.

**Parameters**:
- `n` (int): Number

**Returns**:
- `int`: n * (n + 1) / 2

##### `sqr(n)`

Calculate square number n.

**Parameters**:
- `n` (int): Number

**Returns**:
- `int`: n²

##### `tet_edges(f)`

Number of contact points (edges) between equal spheres arranged in a tetrahedron with frequency f.

**Parameters**:
- `f` (int): Frequency (number of intervals along each edge)

**Returns**:
- `int`: Total number of edges/contact points

**Formula**: Each layer of tri(N) balls spawns N tetrahedrons of 6 edges each.

**Example**:
```python
from ivm_xyz.polyhedra import tet_edges

for f in [1, 2, 3, 4, 5]:
    edges = tet_edges(f)
    print(f"Frequency {f}: {edges} edges")
```

##### `half_oct_edges(f)`

Number of contact points in a half octahedron with frequency f.

**Parameters**:
- `f` (int): Frequency

**Returns**:
- `int`: Total number of edges/contact points

##### `oct_edges(f)`

Number of contact points in an octahedron with frequency f.

**Parameters**:
- `f` (int): Frequency

**Returns**:
- `int`: Total number of edges/contact points

**Formula**: 2 * half_oct_edges(f) - (f + 1) * f * 2

##### `cubocta_edges(f)`

Number of contact points in a cuboctahedron with frequency f.

**Parameters**:
- `f` (int): Frequency

**Returns**:
- `int`: Total number of edges/contact points

**Formula**: 20 * (f + 1)³ - 48 * (f + 1)² + 40 * (f + 1) - 12

##### `cubocta_layer(f)`

Number of contact points in layer n of a cuboctahedron.

**Parameters**:
- `f` (int): Layer number (frequency)

**Returns**:
- `int`: Number of edges/contact points in this layer

**Formula**: 8 * (f - 1)³ + 36 * (f - 1)² + 52 * (f - 1) + 24

#### Alternative Closed-Form Functions

- `a007531(n)`: Tetrahedron edges (closed form) = n * (n + 1) * (n + 2)
- `a035006(n)`: Half octahedron edges (closed form) = n * 2 * (n + 1)²
- `a300758(n)`: Octahedron edges (closed form) = 2 * n * (n + 1) * (2 * n + 1)

**Example**:
```python
from ivm_xyz.polyhedra.edge_counting import tet_edges, oct_edges, cubocta_edges

f = 5
tet = tet_edges(f)
oct = oct_edges(f)
cubocta = cubocta_edges(f)
```

---

## Visualization Module

### plotter.py

**Purpose**: Visualization tools for polyhedra using matplotlib.

**Location**: `ivm_xyz/visualization/plotter.py`

#### Classes

##### `PolyhedronPlotter`

Class for plotting and animating polyhedra.

**Attributes**:
- `output_folder`: Directory to save output images/animations
- `polyhedrons`: List of polyhedron dictionaries for animation

**Methods**:

- `__init__(output_folder="images")`: Initialize plotter
  - Creates output folder if it doesn't exist
  
- `add_polyhedron(vertices, faces, title, file_name)`: Add polyhedron for animation
  - `vertices`: List of (x, y, z) tuples
  - `faces`: List of tuples, each representing vertex indices forming a face
  - `title`: Title of the polyhedron
  - `file_name`: Name of the file to save animation as
  
- `plot_polyhedron(vertices, faces, title, save, file_name)`: Plot single polyhedron
  - `vertices`: List of (x, y, z) tuples
  - `faces`: List of tuples, each representing vertex indices forming a face
  - `title`: Title of the plot (default: "Polyhedron Visualization")
  - `save`: Boolean, whether to save the plot (default: False)
  - `file_name`: Name of file to save (default: "polyhedron.png")
  - Creates 3D plot with vertices, edges, and faces
  
- `animate_polyhedron(save)`: Create animated GIFs of polyhedra
  - `save`: Boolean, whether to save animations
  - Uses parallel processing (up to MAX_THREADS = 8)
  - Requires `imageio` package
  - Rotates polyhedron 360 degrees with 2-degree increments

**Example**:
```python
from ivm_xyz.visualization import PolyhedronPlotter

plotter = PolyhedronPlotter(output_folder="images")

# Define tetrahedron
vertices = [
    (0, 0, 0),
    (1, 0, 0),
    (0.5, 0.866, 0),
    (0.5, 0.289, 0.816)
]
faces = [
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
]

# Static plot
plotter.plot_polyhedron(
    vertices, faces,
    title="Regular Tetrahedron",
    save=True,
    file_name="tetrahedron.png"
)

# Animation
plotter.add_polyhedron(
    vertices, faces,
    "Tetrahedron",
    "tetrahedron.gif"
)
plotter.animate_polyhedron(save=True)
```

**Dependencies**:
- `matplotlib`: Required for plotting
- `imageio`: Required for animations (optional)
- `numpy`: Required for image processing

---

## Module Import Structure

### Package-Level Imports

```python
from ivm_xyz import (
    Vector, Qvector,
    Tetrahedron, make_tet,
    Triangle, make_tri,
    xyz_to_ivm, ivm_to_xyz,
    __version__
)
```

### Module-Specific Imports

```python
# Core modules
from ivm_xyz.core import Vector, Qvector, Tetrahedron, make_tet, Triangle, make_tri
from ivm_xyz.core.vectors import Vector, Qvector, Svector
from ivm_xyz.core.tetrahedron import Tetrahedron, make_tet
from ivm_xyz.core.triangle import Triangle, make_tri
from ivm_xyz.core.constants import S3, PHI, ROOT2, ROOT3, ROOT5, R, D

# Conversion
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz
from ivm_xyz.conversion.converters import xyz_to_ivm, ivm_to_xyz, vector_to_qvector, qvector_to_vector

# Polyhedra
from ivm_xyz.polyhedra import (
    Polyhedron, Edge,
    PolyTetrahedron, Cube, Octahedron, Icosahedron, Cuboctahedron,
    tet_edges, half_oct_edges, oct_edges, cubocta_edges, cubocta_layer
)
from ivm_xyz.polyhedra.base import Polyhedron, Edge
from ivm_xyz.polyhedra.platonic import Tetrahedron, Cube, Octahedron, Icosahedron, Cuboctahedron
from ivm_xyz.polyhedra.edge_counting import tet_edges, half_oct_edges, oct_edges, cubocta_edges, cubocta_layer

# Visualization
from ivm_xyz.visualization import PolyhedronPlotter
from ivm_xyz.visualization.plotter import PolyhedronPlotter
```

---

## Mathematical Background

### Volume Calculations

- **Tetrahedron**: Uses Euler's formula modified by Gerald de Jong
- **Conversion**: IVM volume = XYZ volume × S3 (where S3 = √(9/8))

### Coordinate Systems

- **XYZ**: 3D Cartesian coordinates (x, y, z)
- **IVM/Quadray**: 4D tetrahedral coordinates (a, b, c, d) normalized to non-negative

### Concentric Hierarchy

All polyhedra follow R. Buckminster Fuller's Concentric Hierarchy:
- Tetrahedron: Volume 1
- Cube: Volume 3
- Octahedron: Volume 4
- Icosahedron: Volume ~18.51
- Cuboctahedron: Volume 20

---

## References

- Buckminster Fuller, R. "Synergetics: Explorations in the Geometry of Thinking"
- Euler Volume Formula: http://www.grunch.net/synergetics/quadvols.html
- Gerald de Jong's modifications to Euler formula
- OEIS sequences: A007531, A035006, A300758, A069074

