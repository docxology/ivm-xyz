# IVM-XYZ API Reference

Complete technical API documentation for all classes, methods, and functions in the IVM-XYZ package.

## Table of Contents

1. [Core Module](#core-module)
   - [Vector Class](#vector-class)
   - [Qvector Class](#qvector-class)
   - [Svector Class](#svector-class)
   - [Tetrahedron Class](#tetrahedron-class)
   - [Triangle Class](#triangle-class)
   - [Constants](#constants)
   - [Module-Level Functions](#module-level-functions)
2. [Conversion Module](#conversion-module)
3. [Polyhedra Module](#polyhedra-module)
4. [Visualization Module](#visualization-module)

---

## Core Module

### `ivm_xyz.core.vectors`

#### Vector Class

3D vector in XYZ (Cartesian) coordinate system.

**Class**: `Vector`

**Location**: `ivm_xyz.core.vectors.Vector`

##### Attributes

- **`xyz`** (`namedtuple`): Named tuple of type `xyz_vector` containing (x, y, z) coordinates
- **`x`** (`float`, property): X coordinate
- **`y`** (`float`, property): Y coordinate
- **`z`** (`float`, property): Z coordinate

##### Methods

###### `__init__(arg)`

Initialize a vector from coordinates.

**Parameters**:
- `arg` (tuple, list, or iterable): Coordinates as (x, y, z) or any iterable of 3 numbers

**Returns**: `Vector` instance

**Example**:
```python
v1 = Vector((1, 2, 3))
v2 = Vector([4, 5, 6])
v3 = Vector((0.5, 1.5, 2.5))
```

###### `__repr__()`

String representation of the vector.

**Returns**: `str` - Representation showing xyz_vector named tuple

**Example**:
```python
v = Vector((1, 2, 3))
print(v)  # xyz_vector(x=1.0, y=2.0, z=3.0)
```

###### `__mul__(scalar)`

Multiply vector by scalar (element-wise multiplication).

**Parameters**:
- `scalar` (float): Scalar multiplier

**Returns**: `Vector` - New vector with scaled coordinates

**Mathematical Operation**: `v' = (x*s, y*s, z*s)`

**Example**:
```python
v = Vector((1, 2, 3))
v_scaled = v * 2  # Vector with (2, 4, 6)
```

###### `__rmul__(scalar)`

Right multiplication by scalar (supports `scalar * vector` syntax).

**Parameters**:
- `scalar` (float): Scalar multiplier

**Returns**: `Vector` - New vector with scaled coordinates

**Example**:
```python
v = Vector((1, 2, 3))
v_scaled = 2 * v  # Same as v * 2
```

###### `__truediv__(scalar)`

Divide vector by scalar.

**Parameters**:
- `scalar` (float): Scalar divisor (must be non-zero)

**Returns**: `Vector` - New vector with divided coordinates

**Mathematical Operation**: `v' = (x/s, y/s, z/s)`

**Example**:
```python
v = Vector((2, 4, 6))
v_divided = v / 2  # Vector with (1, 2, 3)
```

###### `__add__(v1)`

Add another vector to this vector.

**Parameters**:
- `v1` (Vector): Vector to add

**Returns**: `Vector` - New vector with sum of coordinates

**Mathematical Operation**: `v' = (x+x1, y+y1, z+z1)`

**Example**:
```python
v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))
v_sum = v1 + v2  # Vector with (5, 7, 9)
```

###### `__sub__(v1)`

Subtract another vector from this vector.

**Parameters**:
- `v1` (Vector): Vector to subtract

**Returns**: `Vector` - New vector with difference of coordinates

**Mathematical Operation**: `v' = (x-x1, y-y1, z-z1)`

**Example**:
```python
v1 = Vector((5, 7, 9))
v2 = Vector((1, 2, 3))
v_diff = v1 - v2  # Vector with (4, 5, 6)
```

###### `__neg__()`

Negate vector (unary minus).

**Returns**: `Vector` - New vector with negated coordinates

**Mathematical Operation**: `v' = (-x, -y, -z)`

**Example**:
```python
v = Vector((1, 2, 3))
v_neg = -v  # Vector with (-1, -2, -3)
```

###### `unit()`

Return unit vector (normalized) in same direction.

**Returns**: `Vector` - Unit vector with length 1.0

**Mathematical Operation**: `v' = v / ||v||` where `||v||` is the length

**Raises**: 
- ZeroDivisionError if vector length is zero

**Example**:
```python
v = Vector((3, 4, 0))
unit_v = v.unit()  # Vector with length 1.0
print(unit_v.length())  # 1.0
```

###### `length()`

Calculate vector length (magnitude).

**Returns**: `float` - Euclidean length of the vector

**Mathematical Operation**: `||v|| = √(x² + y² + z²)`

**Example**:
```python
v = Vector((3, 4, 0))
len_v = v.length()  # 5.0
```

###### `dot(v1)`

Calculate dot product (scalar product) with another vector.

**Parameters**:
- `v1` (Vector): Another vector

**Returns**: `float` - Dot product scalar value

**Mathematical Operation**: `v · v1 = x*x1 + y*y1 + z*z1`

**Example**:
```python
v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))
dot_product = v1.dot(v2)  # 32.0 (1*4 + 2*5 + 3*6)
```

###### `cross(v1)`

Calculate cross product (vector product) with another vector.

**Parameters**:
- `v1` (Vector): Another vector

**Returns**: `Vector` - Cross product vector (perpendicular to both input vectors)

**Mathematical Operation**: 
```
v × v1 = (y*z1 - z*y1, z*x1 - x*z1, x*y1 - y*x1)
```

**Example**:
```python
v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
cross_product = v1.cross(v2)  # Vector with (0, 0, 1)
```

###### `angle(v1)`

Calculate angle between two vectors in degrees.

**Parameters**:
- `v1` (Vector): Another vector

**Returns**: `float` - Angle in degrees (0-180)

**Mathematical Operation**: `θ = arccos((v · v1) / (||v|| * ||v1||))`

**Example**:
```python
v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
angle_deg = v1.angle(v2)  # 90.0 degrees
```

###### `rotaxis(vAxis, deg)`

Rotate vector around an arbitrary axis by specified degrees.

**Parameters**:
- `vAxis` (Vector): Rotation axis vector
- `deg` (float): Rotation angle in degrees (positive = counterclockwise)

**Returns**: `Vector` - Rotated vector

**Algorithm**: 
1. Realign rotation axis with Z-axis
2. Realign vector accordingly
3. Rotate by `deg` degrees around Z-axis
4. Restore original orientation

**Example**:
```python
v = Vector((1, 0, 0))
axis = Vector((0, 0, 1))
v_rotated = v.rotaxis(axis, 90)  # Rotate 90° around Z-axis
```

###### `rotx(deg)`

Rotate vector around X-axis by specified degrees.

**Parameters**:
- `deg` (float): Rotation angle in degrees (positive = counterclockwise)

**Returns**: `Vector` - Rotated vector

**Rotation Matrix** (for Y and Z components):
```
[y']   [cos(θ)  -sin(θ)] [y]
[z'] = [sin(θ)   cos(θ)] [z]
```

**Example**:
```python
v = Vector((0, 1, 0))
v_rotated = v.rotx(90)  # Rotates to (0, 0, 1)
```

###### `roty(deg)`

Rotate vector around Y-axis by specified degrees.

**Parameters**:
- `deg` (float): Rotation angle in degrees (positive = counterclockwise)

**Returns**: `Vector` - Rotated vector

**Rotation Matrix** (for X and Z components):
```
[x']   [cos(θ)  -sin(θ)] [x]
[z'] = [sin(θ)   cos(θ)] [z]
```

**Example**:
```python
v = Vector((1, 0, 0))
v_rotated = v.roty(90)  # Rotates around Y-axis
```

###### `rotz(deg)`

Rotate vector around Z-axis by specified degrees.

**Parameters**:
- `deg` (float): Rotation angle in degrees (positive = counterclockwise)

**Returns**: `Vector` - Rotated vector

**Rotation Matrix** (for X and Y components):
```
[x']   [cos(θ)  -sin(θ)] [x]
[y'] = [sin(θ)   cos(θ)] [y]
```

**Example**:
```python
v = Vector((1, 0, 0))
v_rotated = v.rotz(90)  # Rotates to (0, 1, 0)
```

###### `spherical()`

Convert vector to spherical coordinates.

**Returns**: `tuple` - (r, phi, theta) where:
- `r` (float): Radial distance (radius) from origin
- `phi` (float): Polar angle from Z-axis in degrees (0-180)
- `theta` (float): Azimuthal angle in XY plane in degrees (-180 to 180)

**Mathematical Conversion**:
```
r = √(x² + y² + z²)
phi = arccos(z/r) [in degrees]
theta = arctan2(y, x) [in degrees, with quadrant correction]
```

**Example**:
```python
v = Vector((1, 0, 0))
r, phi, theta = v.spherical()  # (1.0, 90.0, 0.0)
```

###### `quadray()`

Convert vector to Qvector (Quadray/IVM coordinates).

**Returns**: `Qvector` - Quadray representation

**Mathematical Conversion**:
Uses conversion factor `k = 2/√2` and component-wise mapping based on sign of coordinates.

**Example**:
```python
v = Vector((1, 0, 0))
q = v.quadray()  # Returns Qvector
```

---

#### Qvector Class

4D vector in IVM (Quadray) coordinate system.

**Class**: `Qvector`

**Location**: `ivm_xyz.core.vectors.Qvector`

##### Attributes

- **`coords`** (`namedtuple`): Named tuple of type `ivm_vector` containing (a, b, c, d) coordinates
- **`a`** (`float`, property): First quadray coordinate
- **`b`** (`float`, property): Second quadray coordinate
- **`c`** (`float`, property): Third quadray coordinate
- **`d`** (`float`, property): Fourth quadray coordinate

##### Methods

###### `__init__(arg)`

Initialize a quadray vector from coordinates.

**Parameters**:
- `arg` (tuple or iterable): Quadray coordinates as (a, b, c, d)

**Returns**: `Qvector` instance

**Note**: Coordinates are automatically normalized using `norm()` to ensure all components are non-negative.

**Example**:
```python
q1 = Qvector((1, 0, 0, 0))
q2 = Qvector((1, 2, 3, 4))
```

###### `norm(arg)`

Normalize quadray coordinates such that all components are non-negative.

**Parameters**:
- `arg` (tuple): Quadray coordinates (a, b, c, d)

**Returns**: `namedtuple` - Normalized IVM coordinates

**Algorithm**: Subtracts the minimum value from all components

**Example**:
```python
q = Qvector((1, 2, 3, 4))
# After normalization, minimum is subtracted: (0, 1, 2, 3)
```

###### `norm0()`

Normalize quadray coordinates such that sum of components equals 0.

**Returns**: `namedtuple` - Normalized IVM coordinates with zero sum

**Algorithm**: Subtracts the average (sum/4) from all components

**Example**:
```python
q = Qvector((1, 2, 3, 4))
norm0_coords = q.norm0()
sum(norm0_coords)  # Approximately 0.0
```

###### `__eq__(other)`

Equality comparison between Qvectors.

**Parameters**:
- `other` (Qvector): Another Qvector

**Returns**: `bool` - True if coordinates are equal

**Example**:
```python
q1 = Qvector((1, 1, 1, 1))
q2 = Qvector((2, 2, 2, 2))
q1 == q2  # True (after normalization)
```

###### `__lt__(other)`, `__gt__(other)`

Comparison operators for Qvectors (lexicographic comparison).

**Parameters**:
- `other` (Qvector): Another Qvector

**Returns**: `bool` - Comparison result

###### `__hash__()`

Hash function for use in sets and dictionaries.

**Returns**: `int` - Hash value

**Example**:
```python
q = Qvector((1, 0, 0, 0))
hash(q)  # Hash value
```

###### `__mul__(scalar)`, `__rmul__(scalar)`, `__truediv__(scalar)`

Scalar multiplication and division (same as Vector class).

**Parameters**:
- `scalar` (float): Scalar value

**Returns**: `Qvector` - Scaled Qvector

###### `__add__(v1)`, `__sub__(v1)`, `__neg__()`

Vector addition, subtraction, and negation (same as Vector class).

**Parameters**:
- `v1` (Qvector): Another Qvector

**Returns**: `Qvector` - Result Qvector

###### `dot(v1)`

Calculate dot product with another Qvector.

**Parameters**:
- `v1` (Qvector): Another Qvector

**Returns**: `float` - Dot product

**Mathematical Operation**: Uses `norm0()` normalization: `0.5 * sum(norm0(q) * norm0(v1))`

**Example**:
```python
q1 = Qvector((1, 0, 0, 0))
q2 = Qvector((0, 1, 0, 0))
dot_product = q1.dot(q2)
```

###### `length()`

Calculate Qvector length (magnitude).

**Returns**: `float` - Length of the Qvector

**Mathematical Operation**: `||q|| = √(q · q)`

**Example**:
```python
q = Qvector((1, 0, 0, 0))
len_q = q.length()
```

###### `cross(v1)`

Calculate cross product with another Qvector.

**Parameters**:
- `v1` (Qvector): Another Qvector

**Returns**: `Qvector` - Cross product Qvector

**Algorithm**: Uses basis vectors and component-wise cross product calculation with conversion factor `k = √2/4`

**Example**:
```python
q1 = Qvector((1, 0, 0, 0))
q2 = Qvector((0, 1, 0, 0))
cross_product = q1.cross(q2)
```

###### `angle(v1)`

Calculate angle between two Qvectors in degrees.

**Parameters**:
- `v1` (Qvector): Another Qvector

**Returns**: `float` - Angle in degrees

**Implementation**: Converts to XYZ, calculates angle, returns result

**Example**:
```python
q1 = Qvector((1, 0, 0, 0))
q2 = Qvector((0, 1, 0, 0))
angle_deg = q1.angle(q2)
```

###### `xyz()`

Convert Qvector to Vector (XYZ coordinates).

**Returns**: `Vector` - XYZ representation

**Mathematical Conversion**:
```
k = 0.5/√2
x = k * (a - b - c + d)
y = k * (a - b + c - d)
z = k * (a + b - c - d)
```

**Example**:
```python
q = Qvector((1, 0, 0, 0))
v = q.xyz()  # Returns Vector
```

---

#### Svector Class

Subclass of Vector that takes spherical coordinate arguments.

**Class**: `Svector`

**Location**: `ivm_xyz.core.vectors.Svector`

**Inheritance**: Inherits from `Vector`

##### Methods

###### `__init__(arg)`

Initialize from spherical coordinates or regular vector coordinates.

**Parameters**:
- `arg` (tuple): If tuple is (r, phi, theta), interprets as spherical coordinates. Otherwise, converts input to spherical first.

**Returns**: `Svector` instance

**Algorithm**:
1. If input is not already spherical, converts to spherical using `Vector(arg).spherical()`
2. Converts spherical coordinates (r, phi, theta) to XYZ:
   - `x = r * cos(theta) * sin(phi)`
   - `y = r * sin(theta) * sin(phi)`
   - `z = r * cos(phi)`
3. Creates Vector with computed XYZ coordinates

**Example**:
```python
sv = Svector((1.0, 90.0, 0.0))  # r=1, phi=90°, theta=0°
```

###### `__repr__()`

String representation as spherical coordinates.

**Returns**: `str` - "Svector (r, phi, theta)"

**Example**:
```python
sv = Svector((1.0, 45.0, 30.0))
print(sv)  # "Svector (r, phi, theta)"
```

---

#### Module-Level Functions

##### `dot(a, b)`

Convenience function for dot product.

**Parameters**:
- `a` (Vector or Qvector): First vector
- `b` (Vector or Qvector): Second vector

**Returns**: `float` - Dot product

**Example**:
```python
from ivm_xyz.core.vectors import Vector, dot

v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))
result = dot(v1, v2)  # Same as v1.dot(v2)
```

##### `cross(a, b)`

Convenience function for cross product.

**Parameters**:
- `a` (Vector or Qvector): First vector
- `b` (Vector or Qvector): Second vector

**Returns**: `Vector` or `Qvector` - Cross product

**Example**:
```python
from ivm_xyz.core.vectors import Vector, cross

v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
result = cross(v1, v2)  # Same as v1.cross(v2)
```

##### `angle(a, b)`

Convenience function for angle calculation.

**Parameters**:
- `a` (Vector or Qvector): First vector
- `b` (Vector or Qvector): Second vector

**Returns**: `float` - Angle in degrees

**Example**:
```python
from ivm_xyz.core.vectors import Vector, angle

v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
result = angle(v1, v2)  # Same as v1.angle(v2)
```

##### `length(a)`

Convenience function for length calculation.

**Parameters**:
- `a` (Vector or Qvector): Vector

**Returns**: `float` - Length

**Example**:
```python
from ivm_xyz.core.vectors import Vector, length

v = Vector((3, 4, 0))
result = length(v)  # Same as v.length()
```

---

### `ivm_xyz.core.tetrahedron`

#### Tetrahedron Class

Represents a tetrahedron with six edge lengths.

**Class**: `Tetrahedron`

**Location**: `ivm_xyz.core.tetrahedron.Tetrahedron`

##### Edge Configuration

The tetrahedron has six edges arranged as follows:
- **Face 1**: (a, b, d) - edges a, b, d form first face
- **Face 2**: (b, c, e) - edges b, c, e form second face
- **Face 3**: (c, a, f) - edges c, a, f form third face
- **Face 4**: (d, e, f) - opposite face (edges d, e, f)

**Edge Relationships**:
- Edges `a`, `b`, `c` emanate from one vertex
- Edges `d`, `e`, `f` are opposite edges (not sharing a vertex with a, b, c)

##### Attributes

- **`a`, `b`, `c`, `d`, `e`, `f`** (`float`): Edge lengths
- **`a2`, `b2`, `c2`, `d2`, `e2`, `f2`** (`float`): Squared edge lengths (computed for efficiency)

##### Methods

###### `__init__(a, b, c, d, e, f)`

Initialize tetrahedron with six edge lengths.

**Parameters**:
- `a` (float): First edge length
- `b` (float): Second edge length
- `c` (float): Third edge length
- `d` (float): Fourth edge length
- `e` (float): Fifth edge length
- `f` (float): Sixth edge length

**Returns**: `Tetrahedron` instance

**Example**:
```python
tet = Tetrahedron(1, 1, 1, 1, 1, 1)  # Unit tetrahedron
```

###### `ivm_volume()`

Calculate volume in IVM units using Euler's formula (modified by Gerald de Jong).

**Returns**: `float` - Volume in IVM units

**Mathematical Formula**:
```
ivm_vol = √((addopen - addclosed - addopposite) / 2)
```

Where:
- `addopen`: Sum of open products (edges not forming closed triangles)
- `addclosed`: Sum of closed products (face products)
- `addopposite`: Sum of opposite edge pair products

**Example**:
```python
tet = Tetrahedron(1, 1, 1, 1, 1, 1)
ivm_vol = tet.ivm_volume()  # 1.0 for unit tetrahedron
```

###### `xyz_volume()`

Calculate volume in XYZ units (converted from IVM).

**Returns**: `float` - Volume in XYZ units

**Mathematical Formula**:
```
xyz_vol = ivm_vol / S3
```

Where `S3 = √(9/8) ≈ 1.06066` is the conversion factor.

**Example**:
```python
tet = Tetrahedron(1, 1, 1, 1, 1, 1)
xyz_vol = tet.xyz_volume()  # Approximately 0.942809
```

###### `_addopen()` (Internal Method)

Calculate the sum of open products for volume calculation.

**Returns**: `float` - Sum of products of three edges that don't form a closed triangle

**Algorithm**: Sums 12 terms of form `edge² * edge² * edge²` where edges don't form a face

###### `_addclosed()` (Internal Method)

Calculate the sum of closed products (face products).

**Returns**: `float` - Sum of products of three edges that form a closed triangle (face)

**Algorithm**: Sums 4 terms corresponding to the 4 faces

###### `_addopposite()` (Internal Method)

Calculate the sum of opposite products for volume calculation.

**Returns**: `float` - Sum of products of opposite edge pairs

**Algorithm**: Sums 3 terms of form `a² * e² * (a² + e²)` for opposite pairs

---

#### `make_tet(v0, v1, v2)`

Create tetrahedron from three vectors and calculate volumes.

**Function**: `make_tet`

**Location**: `ivm_xyz.core.tetrahedron.make_tet`

**Parameters**:
- `v0` (Vector or Qvector): First vector (must have `length()` method)
- `v1` (Vector or Qvector): Second vector (must have `length()` method)
- `v2` (Vector or Qvector): Third vector (must have `length()` method)

**Returns**: `tuple` - (ivm_volume, xyz_volume)

**Algorithm**:
1. Calculates six edge lengths:
   - `a = v0.length()`
   - `b = v1.length()`
   - `c = v2.length()`
   - `d = (v0 - v1).length()`
   - `e = (v1 - v2).length()`
   - `f = (v2 - v0).length()`
2. Creates Tetrahedron with these edges
3. Calculates and returns both volumes

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

### `ivm_xyz.core.triangle`

#### Triangle Class

Represents a triangle with three edge lengths.

**Class**: `Triangle`

**Location**: `ivm_xyz.core.triangle.Triangle`

##### Attributes

- **`a`, `b`, `c`** (`float`): Edge lengths of the triangle

##### Methods

###### `__init__(a, b, c)`

Initialize triangle with three edge lengths.

**Parameters**:
- `a` (float): First edge length
- `b` (float): Second edge length
- `c` (float): Third edge length

**Returns**: `Triangle` instance

**Example**:
```python
tri = Triangle(1, 1, 1)  # Equilateral triangle
```

###### `ivm_area()`

Calculate area in IVM units using Heron's formula.

**Returns**: `float` - Area in IVM units

**Mathematical Formula** (Heron's Formula):
```
s = (a + b + c) / 2
area = √(s * (s - a) * (s - b) * (s - c))
```

**Example**:
```python
tri = Triangle(1, 1, 1)
ivm_area = tri.ivm_area()
```

###### `xyz_area()`

Calculate area in XYZ units (converted from IVM).

**Returns**: `float` - Area in XYZ units

**Mathematical Formula**:
```
xyz_area = ivm_area / S3
```

**Example**:
```python
tri = Triangle(1, 1, 1)
xyz_area = tri.xyz_area()
```

---

#### `make_tri(v0, v1)`

Create triangle from two vectors and calculate areas.

**Function**: `make_tri`

**Location**: `ivm_xyz.core.triangle.make_tri`

**Parameters**:
- `v0` (Vector or Qvector): First vector (must have `length()` method)
- `v1` (Vector or Qvector): Second vector (must have `length()` method)

**Returns**: `tuple` - (ivm_area, xyz_area)

**Algorithm**:
1. Calculates three edge lengths:
   - `a = v0.length()`
   - `b = v1.length()`
   - `c = (v1 - v0).length()`
2. Creates Triangle with these edges
3. Calculates and returns both areas

**Example**:
```python
from ivm_xyz.core.triangle import make_tri
from ivm_xyz.core.vectors import Vector

v1 = Vector((1, 0, 0))
v2 = Vector((0, 1, 0))
ivm_area, xyz_area = make_tri(v1, v2)
```

---

### `ivm_xyz.core.constants`

Mathematical constants used throughout the package.

**Module**: `ivm_xyz.core.constants`

##### Constants

- **`S3`** (`float`): Conversion factor between IVM and XYZ volumes = √(9/8) ≈ 1.0606601717798212
- **`ROOT2`** (`float`): Square root of 2 = √2 ≈ 1.4142135623730951
- **`ROOT3`** (`float`): Square root of 3 = √3 ≈ 1.7320508075688772
- **`ROOT5`** (`float`): Square root of 5 = √5 ≈ 2.23606797749979
- **`PHI`** (`float`): Golden ratio = (1 + √5) / 2 ≈ 1.618033988749895
- **`R`** (`float`): Radius constant = 0.5
- **`D`** (`float`): Diameter constant = 1.0

**Example**:
```python
from ivm_xyz.core.constants import S3, PHI, ROOT2

# Convert IVM volume to XYZ
ivm_vol = 1.0
xyz_vol = ivm_vol / S3
```

---

## Conversion Module

### `ivm_xyz.conversion.converters`

#### `xyz_to_ivm(x, y, z)`

Convert XYZ 3D coordinates to IVM 4D quadray coordinates.

**Function**: `xyz_to_ivm`

**Location**: `ivm_xyz.conversion.converters.xyz_to_ivm`

**Parameters**:
- `x` (float): X coordinate in Cartesian system
- `y` (float): Y coordinate in Cartesian system
- `z` (float): Z coordinate in Cartesian system

**Returns**: `tuple` - IVM (quadray) coordinates (a, b, c, d)

**Algorithm**:
1. Uses conversion factor `k = 2/√2`
2. Maps coordinates based on sign:
   - `a = k * ((x≥0)*x + (y≥0)*y + (z≥0)*z)`
   - `b = k * ((x<0)*(-x) + (y<0)*(-y) + (z≥0)*z)`
   - `c = k * ((x<0)*(-x) + (y≥0)*y + (z<0)*(-z))`
   - `d = k * ((x≥0)*x + (y<0)*(-y) + (z<0)*(-z))`
3. Normalizes to ensure all components are non-negative

**Example**:
```python
from ivm_xyz.conversion import xyz_to_ivm

quadray = xyz_to_ivm(1.0, 2.0, 3.0)
print(quadray)  # (a, b, c, d) tuple
```

#### `ivm_to_xyz(a, b, c, d)`

Convert IVM 4D quadray coordinates to XYZ 3D coordinates.

**Function**: `ivm_to_xyz`

**Location**: `ivm_xyz.conversion.converters.ivm_to_xyz`

**Parameters**:
- `a` (float): First quadray coordinate
- `b` (float): Second quadray coordinate
- `c` (float): Third quadray coordinate
- `d` (float): Fourth quadray coordinate

**Returns**: `tuple` - XYZ coordinates (x, y, z)

**Algorithm**:
Uses conversion factor `k = 0.5/√2`:
```
x = k * (a - b - c + d)
y = k * (a - b + c - d)
z = k * (a + b - c - d)
```

**Example**:
```python
from ivm_xyz.conversion import ivm_to_xyz

xyz = ivm_to_xyz(1.0, 0.0, 0.0, 0.0)
print(xyz)  # (x, y, z) tuple
```

#### `vector_to_qvector(vector)`

Convert a Vector object to a Qvector object.

**Function**: `vector_to_qvector`

**Location**: `ivm_xyz.conversion.converters.vector_to_qvector`

**Parameters**:
- `vector` (Vector): Vector object with XYZ coordinates

**Returns**: `Qvector` - Quadray representation

**Implementation**: Calls `vector.quadray()` method

**Example**:
```python
from ivm_xyz.conversion import vector_to_qvector
from ivm_xyz.core.vectors import Vector

v = Vector((1, 2, 3))
q = vector_to_qvector(v)
```

#### `qvector_to_vector(qvector)`

Convert a Qvector object to a Vector object.

**Function**: `qvector_to_vector`

**Location**: `ivm_xyz.conversion.converters.qvector_to_vector`

**Parameters**:
- `qvector` (Qvector): Qvector object with IVM coordinates

**Returns**: `Vector` - XYZ representation

**Implementation**: Calls `qvector.xyz()` method

**Example**:
```python
from ivm_xyz.conversion import qvector_to_vector
from ivm_xyz.core.vectors import Qvector

q = Qvector((1, 0, 0, 0))
v = qvector_to_vector(q)
```

---

## Polyhedra Module

### `ivm_xyz.polyhedra.base`

#### Polyhedron Class

Base class for polyhedra. Designed to be subclassed, not used directly.

**Class**: `Polyhedron`

**Location**: `ivm_xyz.polyhedra.base.Polyhedron`

##### Attributes (Expected in Subclasses)

- **`vertexes`** (`dict`): Dictionary mapping vertex names (strings) to Vector/Qvector objects
- **`faces`** (`tuple`): Tuple of face tuples, each containing vertex names (strings)
- **`edges`** (`list`): List of Edge objects (auto-generated from faces via `_distill()`)
- **`volume`** (`float`): Volume of the polyhedron in IVM units
- **`center`** (`Vector` or `Qvector`): Center point of the polyhedron
- **`name`** (`str`): Name of the polyhedron

##### Methods

###### `scale(scalefactor)`

Scale polyhedron by a factor.

**Parameters**:
- `scalefactor` (float): Scaling factor (multiplier)

**Returns**: New instance of same polyhedron type (scaled)

**Algorithm**:
1. Scales all vertices: `new_vertex = old_vertex * scalefactor`
2. Scales volume: `new_volume = old_volume * scalefactor³`
3. Preserves center
4. Regenerates edges

**Operators**: Can also use `*` or `scalefactor * polyhedron`

**Example**:
```python
from ivm_xyz.polyhedra import Cube

cube = Cube()
scaled = cube.scale(2.0)  # Double size
# Or: scaled = cube * 2.0
# Or: scaled = 2.0 * cube
```

###### `translate(vector)`

Translate polyhedron by a vector.

**Parameters**:
- `vector` (Vector or Qvector): Translation vector

**Returns**: New instance of same polyhedron type (translated)

**Algorithm**:
1. Translates all vertices: `new_vertex = old_vertex + vector`
2. Translates center: `new_center = old_center + vector`
3. Preserves volume
4. Regenerates edges

**Operators**: Can also use `+` or `polyhedron + vector`

**Example**:
```python
from ivm_xyz.polyhedra import Cube
from ivm_xyz.core.vectors import Qvector

cube = Cube()
translation = Qvector((1, 0, 0, 0))
translated = cube.translate(translation)
# Or: translated = cube + translation
```

###### `_distill()` (Internal Method)

Extract unique edges from faces.

**Returns**: `list` - List of Edge objects

**Algorithm**:
1. Iterates through all faces
2. For each face, creates edge pairs from adjacent vertices (including wrap-around)
3. Removes duplicates by sorting vertex pairs
4. Creates Edge objects for each unique pair

**Note**: Automatically called during initialization

---

#### Edge Class

Represents an edge connecting two vertices.

**Class**: `Edge`

**Location**: `ivm_xyz.polyhedra.base.Edge`

##### Attributes

- **`v0`** (`Vector` or `Qvector`): First vertex
- **`v1`** (`Vector` or `Qvector`): Second vertex

##### Methods

###### `__init__(v0, v1)`

Initialize edge with two vertices.

**Parameters**:
- `v0` (Vector or Qvector): First vertex
- `v1` (Vector or Qvector): Second vertex

**Returns**: `Edge` instance

**Example**:
```python
from ivm_xyz.polyhedra.base import Edge
from ivm_xyz.core.vectors import Vector

edge = Edge(Vector((0, 0, 0)), Vector((1, 0, 0)))
```

###### `__repr__()`

String representation of the edge.

**Returns**: `str` - "Edge from <v0> to <v1>"

---

### `ivm_xyz.polyhedra.platonic`

Platonic solids classes (all inherit from `Polyhedron`):

#### Tetrahedron (PolyTetrahedron when imported)

Regular tetrahedron following Buckminster Fuller's Concentric Hierarchy.

**Class**: `Tetrahedron` (imported as `PolyTetrahedron`)

**Location**: `ivm_xyz.polyhedra.platonic.Tetrahedron`

**Properties**:
- **Volume**: 1 (IVM units)
- **Vertices**: 4
- **Faces**: 4 triangles
- **Edges**: 6

**Vertices**: Defined using canonical IVM quadray coordinates:
- `a = Qvector((1, 0, 0, 0))`
- `b = Qvector((0, 1, 0, 0))`
- `c = Qvector((0, 0, 1, 0))`
- `d = Qvector((0, 0, 0, 1))`

**Example**:
```python
from ivm_xyz.polyhedra import PolyTetrahedron

tet = PolyTetrahedron()
print(f"{tet.name}: Volume = {tet.volume}")
```

#### Cube

Regular cube.

**Class**: `Cube`

**Location**: `ivm_xyz.polyhedra.platonic.Cube`

**Properties**:
- **Volume**: 3 (IVM units)
- **Vertices**: 8
- **Faces**: 6 squares
- **Edges**: 12

**Example**:
```python
from ivm_xyz.polyhedra import Cube

cube = Cube()
scaled = cube.scale(2.0)
```

#### Octahedron

Regular octahedron.

**Class**: `Octahedron`

**Location**: `ivm_xyz.polyhedra.platonic.Octahedron`

**Properties**:
- **Volume**: 4 (IVM units)
- **Vertices**: 6
- **Faces**: 8 triangles
- **Edges**: 12

**Example**:
```python
from ivm_xyz.polyhedra import Octahedron

octa = Octahedron()
```

#### Icosahedron

Regular icosahedron.

**Class**: `Icosahedron`

**Location**: `ivm_xyz.polyhedra.platonic.Icosahedron`

**Properties**:
- **Volume**: ~18.51 (IVM units)
- **Vertices**: 12
- **Faces**: 20 triangles
- **Edges**: 30

**Note**: Uses golden ratio (PHI) in vertex calculations

**Example**:
```python
from ivm_xyz.polyhedra import Icosahedron

icosa = Icosahedron()
```

#### Cuboctahedron

Cuboctahedron (Archimedean solid).

**Class**: `Cuboctahedron`

**Location**: `ivm_xyz.polyhedra.platonic.Cuboctahedron`

**Properties**:
- **Volume**: 20 (IVM units)
- **Vertices**: 12
- **Faces**: 14 (8 triangles, 6 squares)
- **Edges**: 24

**Example**:
```python
from ivm_xyz.polyhedra import Cuboctahedron

cubocta = Cuboctahedron()
```

**Note**: All polyhedra are defined using canonical IVM coordinates and follow Fuller's Concentric Hierarchy.

---

### `ivm_xyz.polyhedra.edge_counting`

Functions for counting edges (contact points) in geometric structures:

#### `tri(n)`

Calculate triangular number n.

**Function**: `tri`

**Location**: `ivm_xyz.polyhedra.edge_counting.tri`

**Parameters**:
- `n` (int): Number

**Returns**: `int` - Triangular number: `n * (n + 1) // 2`

**Example**:
```python
from ivm_xyz.polyhedra.edge_counting import tri

result = tri(5)  # 15
```

#### `sqr(n)`

Calculate square number n.

**Function**: `sqr`

**Location**: `ivm_xyz.polyhedra.edge_counting.sqr`

**Parameters**:
- `n` (int): Number

**Returns**: `int` - Square number: `n²`

**Example**:
```python
from ivm_xyz.polyhedra.edge_counting import sqr

result = sqr(5)  # 25
```

#### `tet_edges(f)`

Number of contact points between equal spheres arranged in a tetrahedron with frequency f.

**Function**: `tet_edges`

**Location**: `ivm_xyz.polyhedra.edge_counting.tet_edges`

**Parameters**:
- `f` (int): Frequency (number of intervals along each edge)

**Returns**: `int` - Total number of edges/contact points

**Formula**: 
- Layer 1: 6 edges
- Layer N (N>1): `previous + tri(N) * 6`

**Mathematical Background**: Each layer of `tri(N)` balls spawns N tetrahedrons of 6 edges each.

**OEIS Reference**: A007531

**Example**:
```python
from ivm_xyz.polyhedra import tet_edges

for f in [1, 2, 3, 4, 5]:
    edges = tet_edges(f)
    print(f"Frequency {f}: {edges} edges")
```

#### `half_oct_edges(f)`

Number of contact points in a half octahedron with frequency f.

**Function**: `half_oct_edges`

**Location**: `ivm_xyz.polyhedra.edge_counting.half_oct_edges`

**Parameters**:
- `f` (int): Frequency (number of intervals along each edge)

**Returns**: `int` - Total number of edges/contact points

**Formula**:
- Layer 1: 8 edges
- Layer N (N>1): `previous + sqr(N) * 4 + (N + 1) * N * 2`

**OEIS Reference**: A035006

**Example**:
```python
from ivm_xyz.polyhedra import half_oct_edges

edges = half_oct_edges(5)
```

#### `oct_edges(f)`

Number of contact points in an octahedron with frequency f.

**Function**: `oct_edges`

**Location**: `ivm_xyz.polyhedra.edge_counting.oct_edges`

**Parameters**:
- `f` (int): Frequency (number of intervals along each edge)

**Returns**: `int` - Total number of edges/contact points

**Formula**: `2 * half_oct_edges(f) - (f + 1) * f * 2`

**Mathematical Background**: Two half-octahedrons minus the layer they have in common.

**OEIS Reference**: A300758

**Example**:
```python
from ivm_xyz.polyhedra import oct_edges

edges = oct_edges(5)
```

#### `cubocta_edges(f)`

Number of contact points in a cuboctahedron with frequency f.

**Function**: `cubocta_edges`

**Location**: `ivm_xyz.polyhedra.edge_counting.cubocta_edges`

**Parameters**:
- `f` (int): Frequency (number of intervals along each edge)

**Returns**: `int` - Total number of edges/contact points

**Formula**: `20 * (f + 1)³ - 48 * (f + 1)² + 40 * (f + 1) - 12`

**Example**:
```python
from ivm_xyz.polyhedra import cubocta_edges

edges = cubocta_edges(5)
```

#### `cubocta_layer(f)`

Number of contact points in layer n of a cuboctahedron.

**Function**: `cubocta_layer`

**Location**: `ivm_xyz.polyhedra.edge_counting.cubocta_layer`

**Parameters**:
- `f` (int): Layer number (frequency)

**Returns**: `int` - Number of edges/contact points in this layer

**Formula**: `8 * (f - 1)³ + 36 * (f - 1)² + 52 * (f - 1) + 24`

**OEIS Reference**: A069074

**Example**:
```python
from ivm_xyz.polyhedra import cubocta_layer

edges = cubocta_layer(5)
```

#### Alternative Closed-Form Functions

##### `a007531(n)`

Tetrahedron edges (closed form).

**Function**: `a007531`

**Location**: `ivm_xyz.polyhedra.edge_counting.a007531`

**Parameters**:
- `n` (int): Frequency

**Returns**: `int` - `n * (n + 1) * (n + 2)`

**OEIS Reference**: A007531

##### `a035006(n)`

Half octahedron edges (closed form).

**Function**: `a035006`

**Location**: `ivm_xyz.polyhedra.edge_counting.a035006`

**Parameters**:
- `n` (int): Frequency

**Returns**: `int` - `n * 2 * (n + 1)²`

**OEIS Reference**: A035006

##### `a300758(n)`

Octahedron edges (closed form).

**Function**: `a300758`

**Location**: `ivm_xyz.polyhedra.edge_counting.a300758`

**Parameters**:
- `n` (int): Frequency

**Returns**: `int` - `2 * n * (n + 1) * (2 * n + 1)`

**OEIS Reference**: A300758

---

## Visualization Module

### `ivm_xyz.visualization.plotter`

#### PolyhedronPlotter Class

Class for plotting and animating polyhedra.

**Class**: `PolyhedronPlotter`

**Location**: `ivm_xyz.visualization.plotter.PolyhedronPlotter`

##### Attributes

- **`output_folder`** (`str`): Directory path to save output images/animations
- **`polyhedrons`** (`list`): List of polyhedron dictionaries for batch animation

##### Constants

- **`MAX_THREADS`** (`int`): Maximum number of threads for parallel processing (default: 8)

##### Methods

###### `__init__(output_folder="images")`

Initialize the plotter.

**Parameters**:
- `output_folder` (str, optional): Directory to save output images/animations. Default: "images"

**Behavior**: 
- Creates output folder if it doesn't exist
- Initializes empty `polyhedrons` list

**Example**:
```python
from ivm_xyz.visualization import PolyhedronPlotter

plotter = PolyhedronPlotter(output_folder="my_images")
```

###### `add_polyhedron(vertices, faces, title, file_name)`

Add a polyhedron to the list for batch animation.

**Parameters**:
- `vertices` (list): List of tuples, each representing (x, y, z) coordinates
- `faces` (list): List of tuples, each representing vertex indices forming a face
- `title` (str): Title of the polyhedron (used in plot title)
- `file_name` (str): Name of the file to save the animation as (e.g., "tetrahedron.gif")

**Returns**: `None` (modifies `self.polyhedrons` list)

**Example**:
```python
vertices = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
plotter.add_polyhedron(vertices, faces, "Tetrahedron", "tetrahedron.gif")
```

###### `plot_polyhedron(vertices, faces, title="Polyhedron Visualization", save=False, file_name="polyhedron.png")`

Plot a single polyhedron as a static 3D visualization.

**Parameters**:
- `vertices` (list): List of tuples, each representing (x, y, z) coordinates
- `faces` (list): List of tuples, each representing vertex indices forming a face
- `title` (str, optional): Title of the plot. Default: "Polyhedron Visualization"
- `save` (bool, optional): Whether to save the plot. Default: False
- `file_name` (str, optional): Name of file to save. Default: "polyhedron.png"

**Returns**: `None`

**Behavior**:
1. Creates 3D matplotlib figure with axes
2. Plots faces as Poly3DCollection with semi-transparent blue color
3. Plots vertices as red scatter points with labels
4. Sets axis labels and limits
5. If `save=True`, saves to `output_folder/file_name`
6. Closes figure after plotting/saving

**Visualization Details**:
- Face color: Sky blue with 50% opacity
- Edge color: Dark blue
- Vertex color: Dark red with black edges
- Vertex labels: Show vertex index and coordinates

**Example**:
```python
vertices = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
plotter.plot_polyhedron(
    vertices, faces,
    title="Regular Tetrahedron",
    save=True,
    file_name="tetrahedron.png"
)
```

###### `animate_polyhedron(save=False)`

Create animated GIFs of all polyhedra in the `polyhedrons` list.

**Parameters**:
- `save` (bool, optional): Whether to save animations. Default: False

**Returns**: `None`

**Behavior**:
1. Uses parallel processing (ThreadPoolExecutor) with up to `MAX_THREADS` threads
2. For each polyhedron in the list:
   - Creates 180 frames (360 degrees / 2 degrees per frame)
   - Rotates view angle from 0 to 360 degrees
   - Converts each frame to image array
   - Saves as animated GIF using imageio
3. Uses 20 FPS for animation speed

**Requirements**:
- Requires `imageio` package (raises ImportError if not available)

**Parallel Processing**:
- Uses `concurrent.futures.ThreadPoolExecutor`
- Maximum threads: `min(len(polyhedrons), MAX_THREADS)`

**Raises**:
- `ImportError`: If `imageio` package is not installed

**Example**:
```python
# Add multiple polyhedra
plotter.add_polyhedron(vertices1, faces1, "Tetrahedron", "tetrahedron.gif")
plotter.add_polyhedron(vertices2, faces2, "Cube", "cube.gif")

# Create animations for all
plotter.animate_polyhedron(save=True)
```

**Dependencies**:
- `matplotlib`: Required for plotting (uses non-interactive 'Agg' backend)
- `numpy`: Required for image processing
- `imageio`: Required for animations (raises error if missing)
- `concurrent.futures`: For parallel processing (standard library)

---

## Package-Level Imports

The main package provides convenient imports:

```python
from ivm_xyz import (
    Vector, Qvector,
    Tetrahedron, make_tet,
    Triangle, make_tri,
    xyz_to_ivm, ivm_to_xyz,
    __version__
)
```

## Module-Level Imports

### Core Module Functions

```python
from ivm_xyz.core.vectors import dot, cross, angle, length

# Convenience functions for vector operations
d = dot(v1, v2)
c = cross(v1, v2)
a = angle(v1, v2)
l = length(v1)
```

### Additional Classes

```python
from ivm_xyz.core.vectors import Svector

# Spherical vector (initialized from spherical coordinates)
sv = Svector((r, phi, theta))
```

---

## Technical Notes

### Coordinate System Conversions

**XYZ to IVM Conversion**:
- Uses sign-based mapping with conversion factor `k = 2/√2`
- Results are normalized to ensure non-negative components

**IVM to XYZ Conversion**:
- Uses linear combination with conversion factor `k = 0.5/√2`
- Round-trip conversion maintains precision (error typically < 1e-10)

### Volume Calculations

**Tetrahedron Volume**:
- Uses Euler's formula modified by Gerald de Jong
- Requires 6 edge lengths
- Volume scales as cube of edge length

**Triangle Area**:
- Uses Heron's formula
- Requires 3 edge lengths
- Area scales as square of edge length

### Rotation Operations

**Axis Rotations**:
- Positive angles rotate counterclockwise when viewing from positive axis
- Rotations use standard rotation matrices
- Precision: Results rounded to 8 decimal places

**Arbitrary Axis Rotation**:
- Uses axis alignment algorithm
- Maintains relative orientation

### Performance Considerations

- Vector operations are optimized for small-scale geometric calculations
- Polyhedron operations create new instances (immutable design)
- Visualization uses parallel processing for multiple animations
- Edge counting functions use iterative algorithms (can be optimized with closed-form formulas)

---

## References

- Buckminster Fuller, R. "Synergetics: Explorations in the Geometry of Thinking"
- Euler Volume Formula: http://www.grunch.net/synergetics/quadvols.html
- Gerald de Jong's modifications to Euler formula
- OEIS sequences: A007531, A035006, A300758, A069074
