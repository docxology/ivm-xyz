"""
Basic usage examples for the IVM-XYZ package.
"""

from ivm_xyz import Vector, Qvector, Tetrahedron, make_tet, Triangle, make_tri
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz
from ivm_xyz.core.constants import D, R, PHI


def example_vectors():
    """Demonstrate vector operations."""
    print("=== Vector Examples ===")
    
    # Create vectors
    v1 = Vector((1, 0, 0))
    v2 = Vector((0, 1, 0))
    v3 = Vector((0, 0, 1))
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print(f"Vector 3: {v3}")
    
    # Vector operations
    v_sum = v1 + v2
    print(f"Sum: {v_sum}")
    
    dot = v1.dot(v2)
    print(f"Dot product: {dot}")
    
    cross = v1.cross(v2)
    print(f"Cross product: {cross}")
    
    print(f"Length of v1: {v1.length():.6f}")
    print()


def example_quadrays():
    """Demonstrate quadray vectors."""
    print("=== Quadray Examples ===")
    
    # Create quadray vectors
    q1 = Qvector((1, 0, 0, 0))
    q2 = Qvector((0, 1, 0, 0))
    
    print(f"Quadray 1: {q1}")
    print(f"Quadray 2: {q2}")
    
    # Convert to XYZ
    v1 = q1.xyz()
    print(f"Quadray 1 as XYZ: {v1}")
    
    # Convert back
    q1_back = v1.quadray()
    print(f"Round trip: {q1_back}")
    print()


def example_tetrahedron():
    """Demonstrate tetrahedron calculations."""
    print("=== Tetrahedron Examples ===")
    
    # Unit tetrahedron
    tet = Tetrahedron(D, D, D, D, D, D)
    ivm_vol = tet.ivm_volume()
    xyz_vol = tet.xyz_volume()
    
    print(f"Unit tetrahedron:")
    print(f"  IVM Volume: {ivm_vol:.6f}")
    print(f"  XYZ Volume: {xyz_vol:.6f}")
    
    # From vectors
    v1 = Vector((0.5, 0, 0))
    v2 = Vector((0, 0.5, 0))
    v3 = Vector((0, 0, 0.5))
    ivm_vol2, xyz_vol2 = make_tet(v1, v2, v3)
    
    print(f"\nTetrahedron from vectors:")
    print(f"  IVM Volume: {ivm_vol2:.6f}")
    print(f"  XYZ Volume: {xyz_vol2:.6f}")
    print(f"  Expected XYZ: {1/6:.6f}")
    print()


def example_triangle():
    """Demonstrate triangle calculations."""
    print("=== Triangle Examples ===")
    
    # Equilateral triangle
    tri = Triangle(1, 1, 1)
    ivm_area = tri.ivm_area()
    xyz_area = tri.xyz_area()
    
    print(f"Equilateral triangle (side=1):")
    print(f"  IVM Area: {ivm_area:.6f}")
    print(f"  XYZ Area: {xyz_area:.6f}")
    
    # From vectors
    v1 = Vector((1, 0, 0))
    v2 = Vector((0, 1, 0))
    ivm_area2, xyz_area2 = make_tri(v1, v2)
    
    print(f"\nTriangle from vectors:")
    print(f"  IVM Area: {ivm_area2:.6f}")
    print(f"  XYZ Area: {xyz_area2:.6f}")
    print()


def example_conversion():
    """Demonstrate coordinate conversion."""
    print("=== Conversion Examples ===")
    
    # Convert XYZ to IVM
    xyz_point = (1.0, 2.0, 3.0)
    quadray = xyz_to_ivm(*xyz_point)
    print(f"XYZ {xyz_point} -> Quadray {quadray}")
    
    # Convert back
    xyz_back = ivm_to_xyz(*quadray)
    print(f"Quadray {quadray} -> XYZ {xyz_back}")
    print(f"Round trip error: {abs(xyz_point[0] - xyz_back[0]):.10f}")
    print()


def example_polyhedra():
    """Demonstrate polyhedra."""
    print("=== Polyhedra Examples ===")
    
    from ivm_xyz.polyhedra import Cube, Octahedron, tet_edges
    
    # Create polyhedra
    cube = Cube()
    octa = Octahedron()
    
    print(f"{cube.name}:")
    print(f"  Volume: {cube.volume}")
    print(f"  Vertices: {len(cube.vertexes)}")
    print(f"  Faces: {len(cube.faces)}")
    
    print(f"\n{octa.name}:")
    print(f"  Volume: {octa.volume}")
    print(f"  Vertices: {len(octa.vertexes)}")
    print(f"  Faces: {len(octa.faces)}")
    
    # Edge counting
    print(f"\nEdge counting:")
    for f in [1, 2, 3, 4, 5]:
        edges = tet_edges(f)
        print(f"  Frequency {f}: {edges} edges")
    print()


if __name__ == "__main__":
    example_vectors()
    example_quadrays()
    example_tetrahedron()
    example_triangle()
    example_conversion()
    example_polyhedra()

