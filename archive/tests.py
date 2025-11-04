from tetravolume import Tetrahedron, Triangle, Vector, make_tet, make_tri
import unittest

def run_all_tests_and_demos():
    """Execute all tests and demonstrations from tetravolume module."""
    print("Executing all tests and demonstrations from tetravolume.py...\n")

    # Define sets of D, R pairs to explore the space
    DR_pairs = [(1, 2), (2, 3), (3, 4)]

    for D, R in DR_pairs:
        print(f"Testing with D={D}, R={R}:")

        # Demonstrate Tetrahedron calculations
        print("Tetrahedron Demonstrations:")
        tet = Tetrahedron(D, D, D, D, D, D)
        print(f"Unit Tetrahedron IVM Volume: {tet.ivm_volume():.6f}")
        print(f"Unit Tetrahedron XYZ Volume: {tet.xyz_volume():.6f}\n")

        # Demonstrate Triangle calculations
        print("Triangle Demonstrations:")
        tri = Triangle(D, D, D)
        print(f"Unit Triangle IVM Area: {tri.ivm_area():.6f}")
        print(f"Unit Triangle XYZ Area: {tri.xyz_area():.6f}\n")

        # Show additional examples
        print("Additional Demonstrations:")
        v0, v1, v2 = Vector((R, 0, 0)), Vector((0, R, 0)), Vector((0, 0, R))
        ivm_vol, xyz_vol = make_tet(v0, v1, v2)
        print(f"Constructed Tetrahedron IVM Volume: {ivm_vol:.6f}, XYZ Volume: {xyz_vol:.6f}")

        v0_tri, v1_tri = Vector((D, 0, 0)), Vector((0, D, 0))
        ivm_area, xyz_area = make_tri(v0_tri, v1_tri)
        print(f"Constructed Triangle IVM Area: {ivm_area:.6f}, XYZ Area: {xyz_area:.6f}\n")

    # Execute unit tests
    print("Executing Unit Tests:")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

if __name__ == "__main__":
    run_all_tests_and_demos()