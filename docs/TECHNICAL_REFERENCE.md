# Technical Reference Guide

Comprehensive technical reference for developers working with the IVM-XYZ package.

## Table of Contents

1. [Method Signatures](#method-signatures)
2. [Algorithm Details](#algorithm-details)
3. [Performance Considerations](#performance-considerations)
4. [Error Handling](#error-handling)
5. [Precision and Numerical Accuracy](#precision-and-numerical-accuracy)
6. [Implementation Details](#implementation-details)

---

## Method Signatures

### Vector Class Methods

#### Arithmetic Operations

```python
Vector.__init__(arg: Union[tuple, list, Iterable]) -> Vector
Vector.__add__(v1: Vector) -> Vector
Vector.__sub__(v1: Vector) -> Vector
Vector.__mul__(scalar: float) -> Vector
Vector.__rmul__(scalar: float) -> Vector
Vector.__truediv__(scalar: float) -> Vector
Vector.__neg__() -> Vector
```

#### Vector Operations

```python
Vector.length() -> float
Vector.unit() -> Vector
Vector.dot(v1: Vector) -> float
Vector.cross(v1: Vector) -> Vector
Vector.angle(v1: Vector) -> float
```

#### Rotations

```python
Vector.rotx(deg: float) -> Vector
Vector.roty(deg: float) -> Vector
Vector.rotz(deg: float) -> Vector
Vector.rotaxis(vAxis: Vector, deg: float) -> Vector
```

#### Coordinate Conversions

```python
Vector.spherical() -> Tuple[float, float, float]  # (r, phi, theta)
Vector.quadray() -> Qvector
```

### Qvector Class Methods

```python
Qvector.__init__(arg: Union[tuple, Iterable]) -> Qvector
Qvector.norm(arg: tuple) -> namedtuple
Qvector.norm0() -> namedtuple
Qvector.length() -> float
Qvector.dot(v1: Qvector) -> float
Qvector.cross(v1: Qvector) -> Qvector
Qvector.angle(v1: Qvector) -> float
Qvector.xyz() -> Vector
```

### Tetrahedron Class Methods

```python
Tetrahedron.__init__(a: float, b: float, c: float, d: float, e: float, f: float) -> Tetrahedron
Tetrahedron.ivm_volume() -> float
Tetrahedron.xyz_volume() -> float
```

### Triangle Class Methods

```python
Triangle.__init__(a: float, b: float, c: float) -> Triangle
Triangle.ivm_area() -> float
Triangle.xyz_area() -> float
```

### Conversion Functions

```python
xyz_to_ivm(x: float, y: float, z: float) -> Tuple[float, float, float, float]
ivm_to_xyz(a: float, b: float, c: float, d: float) -> Tuple[float, float, float]
vector_to_qvector(vector: Vector) -> Qvector
qvector_to_vector(qvector: Qvector) -> Vector
```

### Polyhedron Methods

```python
Polyhedron.scale(scalefactor: float) -> Polyhedron
Polyhedron.translate(vector: Union[Vector, Qvector]) -> Polyhedron
Polyhedron._distill() -> List[Edge]
```

### Visualization Methods

```python
PolyhedronPlotter.__init__(output_folder: str = "images") -> None
PolyhedronPlotter.add_polyhedron(vertices: List[Tuple], faces: List[Tuple], title: str, file_name: str) -> None
PolyhedronPlotter.plot_polyhedron(vertices: List[Tuple], faces: List[Tuple], title: str = "Polyhedron Visualization", save: bool = False, file_name: str = "polyhedron.png") -> None
PolyhedronPlotter.animate_polyhedron(save: bool = False) -> None
```

---

## Algorithm Details

### Euler Volume Formula (Modified)

The tetrahedron volume calculation uses Gerald de Jong's modification of Euler's formula:

```
ivm_vol = √((addopen - addclosed - addopposite) / 2)
```

**Components**:
- `addopen`: Sum of 12 open products (edge² × edge² × edge² where edges don't form a face)
- `addclosed`: Sum of 4 closed products (face products: edge² × edge² × edge² for each face)
- `addopposite`: Sum of 3 opposite edge pair products

**Edge Pairing**:
- Opposite pairs: (a, e), (b, f), (c, d)
- Each pair contributes: `edge1² × edge2² × (edge1² + edge2²)`

### Heron's Formula

Triangle area calculation:

```
s = (a + b + c) / 2
area = √(s × (s - a) × (s - b) × (s - c))
```

### Quadray Conversion

**XYZ to IVM**:
```
k = 2/√2
a = k × [max(0, x) + max(0, y) + max(0, z)]
b = k × [max(0, -x) + max(0, -y) + max(0, z)]
c = k × [max(0, -x) + max(0, y) + max(0, -z)]
d = k × [max(0, x) + max(0, -y) + max(0, -z)]
# Then normalize to non-negative
```

**IVM to XYZ**:
```
k = 0.5/√2
x = k × (a - b - c + d)
y = k × (a - b + c - d)
z = k × (a + b - c - d)
```

### Rotation Matrices

**X-axis rotation** (affects Y and Z):
```
[y']   [cos(θ)  -sin(θ)] [y]
[z'] = [sin(θ)   cos(θ)] [z]
```

**Y-axis rotation** (affects X and Z):
```
[x']   [cos(θ)  -sin(θ)] [x]
[z'] = [sin(θ)   cos(θ)] [z]
```

**Z-axis rotation** (affects X and Y):
```
[x']   [cos(θ)  -sin(θ)] [x]
[y'] = [sin(θ)   cos(θ)] [y]
```

**Arbitrary axis rotation**:
1. Realign axis to Z-axis
2. Rotate around Z by angle
3. Restore original orientation

### Spherical Coordinate Conversion

**To Spherical**:
```
r = √(x² + y² + z²)
phi = arccos(z/r)  [0-180 degrees]
theta = arctan2(y, x)  [-180 to 180 degrees, with quadrant correction]
```

**From Spherical**:
```
x = r × cos(theta) × sin(phi)
y = r × sin(theta) × sin(phi)
z = r × cos(phi)
```

---

## Performance Considerations

### Computational Complexity

- **Vector Operations**: O(1) for most operations
- **Tetrahedron Volume**: O(1) - fixed number of calculations
- **Triangle Area**: O(1) - fixed number of calculations
- **Coordinate Conversion**: O(1) - direct mathematical transformation
- **Polyhedron Scaling/Translation**: O(V) where V is number of vertices
- **Edge Extraction**: O(F×E) where F is faces, E is edges per face

### Memory Usage

- **Vector/Qvector**: Minimal (stores only coordinates)
- **Tetrahedron/Triangle**: Minimal (stores only edge lengths)
- **Polyhedron**: O(V) for vertices, O(F) for faces, O(E) for edges
- **Visualization**: O(F×V×180) for animations (180 frames)

### Optimization Tips

1. **Reuse Vector Objects**: Create once, use multiple times
2. **Batch Operations**: Use `add_polyhedron()` for multiple animations
3. **Parallel Processing**: Animation automatically uses parallel processing
4. **Edge Counting**: Use closed-form functions (`a007531`, etc.) for better performance

---

## Error Handling

### Common Exceptions

**ZeroDivisionError**:
- `Vector.unit()`: Raised when vector length is zero
- `Vector / scalar`: Raised when scalar is zero

**ImportError**:
- `PolyhedronPlotter.animate_polyhedron()`: Raised when `imageio` is not installed

**TypeError**:
- Vector operations: Raised when incompatible types are used
- Coordinate conversion: Raised when wrong number of arguments provided

### Input Validation

- **Vector initialization**: Accepts any iterable of 3 numbers
- **Qvector initialization**: Accepts any iterable of 4 numbers
- **Tetrahedron**: All edge lengths must be positive numbers
- **Triangle**: All edge lengths must be positive numbers (triangle inequality not enforced)

### Edge Cases

- **Zero Vector**: `Vector((0, 0, 0))` has length 0, cannot compute unit vector
- **Degenerate Tetrahedron**: May produce zero or negative volume if edges don't form valid tetrahedron
- **Degenerate Triangle**: May produce zero or negative area if edges don't form valid triangle
- **Spherical Coordinates**: `phi=0` or `phi=180` requires special handling for `theta`

---

## Precision and Numerical Accuracy

### Floating Point Precision

- **Default Precision**: Python float (typically 64-bit, ~15-17 decimal digits)
- **Rounding**: Rotation results rounded to 8 decimal places
- **Svector Conversion**: Coordinates rounded to 15 decimal places
- **Spherical Conversion**: Angle calculations rounded to 10 decimal places

### Conversion Accuracy

- **Round-Trip Error**: Typically < 1e-10 for coordinate conversions
- **Volume Calculations**: Accuracy depends on edge length precision
- **Area Calculations**: Accuracy depends on edge length precision

### Numerical Stability

- **Normalization**: Qvector normalization ensures mathematical consistency
- **Length Calculations**: Uses dot product for numerical stability
- **Angle Calculations**: Uses `acos` with rounding to prevent domain errors

---

## Implementation Details

### Data Structures

**Vector**:
- Uses `namedtuple` for coordinates: `xyz_vector(x, y, z)`
- Properties provide convenient access: `v.x`, `v.y`, `v.z`
- Immutable design (operations return new instances)

**Qvector**:
- Uses `namedtuple` for coordinates: `ivm_vector(a, b, c, d)`
- Properties provide convenient access: `q.a`, `q.b`, `q.c`, `q.d`
- Automatic normalization on initialization

**Polyhedron**:
- Uses dictionary for vertices: `{name: Vector/Qvector}`
- Uses tuple for faces: `((v1, v2, v3), ...)`
- Edges auto-generated from faces

### Internal Methods

**Tetrahedron**:
- `_addopen()`: Internal calculation for open products
- `_addclosed()`: Internal calculation for closed products
- `_addopposite()`: Internal calculation for opposite products

**Polyhedron**:
- `_distill()`: Internal method to extract unique edges from faces

### Threading and Parallelization

**Animation**:
- Uses `ThreadPoolExecutor` for parallel frame generation
- Maximum threads: `min(len(polyhedrons), MAX_THREADS)` where `MAX_THREADS = 8`
- Each animation runs in separate thread

### Backend Configuration

**Visualization**:
- Uses matplotlib 'Agg' backend (non-interactive)
- Allows headless operation (no display required)
- Suitable for server environments

---

## Mathematical Constants

### Conversion Factors

- **S3**: `√(9/8) ≈ 1.0606601717798212` - IVM to XYZ volume conversion
- **ROOT2**: `√2 ≈ 1.4142135623730951` - Used in Quadray conversions
- **Conversion Factor (XYZ to IVM)**: `k = 2/√2`
- **Conversion Factor (IVM to XYZ)**: `k = 0.5/√2`

### Geometric Constants

- **PHI**: Golden ratio `(1 + √5)/2 ≈ 1.618033988749895`
- **ROOT3**: `√3 ≈ 1.7320508075688772`
- **ROOT5**: `√5 ≈ 2.23606797749979`

---

## Testing Coverage

### Test Categories

1. **Unit Tests**: Test individual methods and classes
2. **Functional Tests**: Test complete operations and workflows
3. **Integration Tests**: Test module interactions
4. **Visualization Tests**: Test plotting and animation
5. **Import Tests**: Verify package structure and imports

### Test Statistics

- **Total Tests**: 83+
- **Coverage**: All public methods and classes
- **Edge Cases**: Zero vectors, degenerate shapes, boundary conditions
- **Precision Tests**: Round-trip conversions, mathematical accuracy

---

## References

- **Euler Volume Formula**: http://www.grunch.net/synergetics/quadvols.html
- **Gerald de Jong**: Modifications to Euler formula
- **OEIS Sequences**: A007531, A035006, A300758, A069074
- **Buckminster Fuller**: "Synergetics: Explorations in the Geometry of Thinking"

