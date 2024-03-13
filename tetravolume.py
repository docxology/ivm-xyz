"""
Euler volume, modified by Gerald de Jong
http://www.grunch.net/synergetics/quadvols.html
Kirby Urner (c) MIT License

See:
http://mathforum.org/kb/thread.jspa?threadID=2836546
for explanation of quadrays, used for some unit tests

3-13-2024 - Copied from https://github.com/4dsolutions/MartianMath/blob/master/tetravolume.py 

"""

from math import sqrt as rt2
from qrays import Qvector, Vector
import sys

S3    = pow(9/8, 0.5)
root2 = rt2(2)
root5 = rt2(5)

# Introduce class Triangle

class Triangle:
    """
    Represents a triangle, allowing calculation of areas in both IVM and XYZ systems.
    Assumes equilateral triangle for simplicity.
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ivm_area(self):
        # Placeholder for IVM area calculation. Adjust formula as needed.
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

    def xyz_area(self):
        # Placeholder for XYZ area calculation. Adjust formula as needed.
        return self.ivm_area() / S3  # S3 used from Tetrahedron class for consistency

# Add make_tri method
        
def make_tri(v0,v1):
    """
    three edges from any corner, remaining three edges computed
    """
    tri = Triangle(v0.length(), v1.length(), (v1-v0).length())
    return tri.ivm_area(), tri.xyz_area()

class Tetrahedron:
    """
    Takes six edges of tetrahedron with faces
    (a,b,d)(b,c,e)(c,a,f)(d,e,f) -- returns volume
    if ivm and xyz
    """

    def __init__(self, a, b, c, d, e, f):
        # a,b,c,d,e,f = [Decimal(i) for i in (a,b,c,d,e,f)]
        self.a, self.a2 = a, a**2
        self.b, self.b2 = b, b**2
        self.c, self.c2 = c, c**2
        self.d, self.d2 = d, d**2
        self.e, self.e2 = e, e**2
        self.f, self.f2 = f, f**2
        print(f"Initialized Tetrahedron with edges: {a}, {b}, {c}, {d}, {e}, {f}")

    def ivm_volume(self):
        ivmvol = ((self._addopen() 
                    - self._addclosed() 
                    - self._addopposite())/2) ** 0.5
        print(f"IVM Volume: {ivmvol}")
        return ivmvol

    def xyz_volume(self):
        xyzvol = 1/S3 * self.ivm_volume()
        print(f"XYZ Volume: {xyzvol}")
        return xyzvol

    def _addopen(self):
        a2,b2,c2,d2,e2,f2 = self.a2, self.b2, self.c2, self.d2, self.e2, self.f2
        sumval = f2*a2*b2
        sumval +=  d2 * a2 * c2
        sumval +=  a2 * b2 * e2
        sumval +=  c2 * b2 * d2
        sumval +=  e2 * c2 * a2
        sumval +=  f2 * c2 * b2
        sumval +=  e2 * d2 * a2
        sumval +=  b2 * d2 * f2
        sumval +=  b2 * e2 * f2
        sumval +=  d2 * e2 * c2
        sumval +=  a2 * f2 * e2
        sumval +=  d2 * f2 * c2
        print(f"Sum of open products: {sumval}")
        return sumval

    def _addclosed(self):
        a2,b2,c2,d2,e2,f2 = self.a2, self.b2, self.c2, self.d2, self.e2, self.f2
        sumval =   a2 * b2 * d2
        sumval +=  d2 * e2 * f2
        sumval +=  b2 * c2 * e2
        sumval +=  a2 * c2 * f2
        print(f"Sum of closed products: {sumval}")
        return sumval

    def _addopposite(self):
        a2,b2,c2,d2,e2,f2 = self.a2, self.b2, self.c2, self.d2, self.e2, self.f2
        sumval =  a2 * e2 * (a2 + e2)
        sumval += b2 * f2 * (b2 + f2)
        sumval += c2 * d2 * (c2 + d2)
        print(f"Sum of opposite products: {sumval}")
        return sumval

def make_tet(v0,v1,v2):
    """
    three edges from any corner, remaining three edges computed
    """
    tet = Tetrahedron(v0.length(), v1.length(), v2.length(), 
                      (v0-v1).length(), (v1-v2).length(), (v2-v0).length())
    print(f"Making tetrahedron with vertices: {v0}, {v1}, {v2}")
    return tet.ivm_volume(), tet.xyz_volume()

PHI = (1 + root5)/2.0

R = 0.5
D = 1.0
root3 = pow(3, .5)
root2 = pow(2, .5)

import unittest
class Test_Tetrahedron(unittest.TestCase):

    def test_unit_volume(self):
        tet = Tetrahedron(D, D, D, D, D, D)
        self.assertEqual(tet.ivm_volume(), 1, "Volume not 1")

    def test_e_module(self):
        e0 = D
        e1 = rt2(3) * PHI**-1
        e2 = rt2((5 - root5)/2)
        e3 = (3 - root5)/2
        e4 = rt2(5 - 2*root5)
        e5 = 1/PHI
        tet = Tetrahedron(e0, e1, e2, e3, e4, e5)
        self.assertTrue(1/23 > tet.ivm_volume()/8 > 1/24, "Wrong E-mod")
        
    def test_unit_volume2(self):
        tet = Tetrahedron(R, R, R, R, R, R)
        self.assertAlmostEqual(float(tet.xyz_volume()), 0.117851130)

    def test_phi_edge_tetra(self):
        tet = Tetrahedron(D, D, D, D, D, PHI)
        self.assertAlmostEqual(float(tet.ivm_volume()), 0.70710678)

    def test_right_tetra(self):
        e = pow((root3/2)**2 + (root3/2)**2, 0.5)  # right tetrahedron
        tet = Tetrahedron(D, D, D, D, D, e)
        self.assertAlmostEqual(tet.xyz_volume(), 1)

    def test_quadrant(self):
        qA = Qvector((1,0,0,0))
        qB = Qvector((0,1,0,0))
        qC = Qvector((0,0,1,0))
        tet = make_tet(qA, qB, qC) 
        self.assertAlmostEqual(tet[0], 0.25) 

    def test_octant(self):
        x = Vector((0.5, 0,   0))
        y = Vector((0  , 0.5, 0))
        z = Vector((0  , 0  , 0.5))
        tet = make_tet(x,y,z)
        self.assertAlmostEqual(tet[1], 1/6, 5) # good to 5 places

    def test_quarter_octahedron(self):
        a = Vector((1,0,0))
        b = Vector((0,1,0))
        c = Vector((0.5,0.5,root2/2))
        tet = make_tet(a, b, c)
        self.assertAlmostEqual(tet[0], 1, 5) # good to 5 places  

    def test_xyz_cube(self):
        a = Vector((0.5, 0.0, 0.0))
        b = Vector((0.0, 0.5, 0.0))
        c = Vector((0.0, 0.0, 0.5))
        R_octa = make_tet(a,b,c) 
        self.assertAlmostEqual(6 * R_octa[1], 1, 4) # good to 4 places  

    def test_s3(self):
        D_tet = Tetrahedron(D, D, D, D, D, D)
        a = Vector((0.5, 0.0, 0.0))
        b = Vector((0.0, 0.5, 0.0))
        c = Vector((0.0, 0.0, 0.5))
        R_cube = 6 * make_tet(a,b,c)[1]
        self.assertAlmostEqual(D_tet.xyz_volume() * S3, R_cube, 4)
    def test_martian(self):
        """Test Martian tetrahedron volume calculation."""
        p = Qvector((2,1,0,1))
        q = Qvector((2,1,1,0))
        r = Qvector((2,0,1,1))
        result = make_tet(5*q, 2*p, 2*r)
        self.assertAlmostEqual(result[0], 20, 7, "Martian tetrahedron volume calculation failed.")

def command_line():
    """Process command-line arguments to calculate tetrahedron volumes."""
    args = sys.argv[1:]
    if len(args) == 6:
        try:
            args = [float(x) for x in args]  # Convert arguments to floats
            t = Tetrahedron(*args)
            print(f"IVM Volume (from command line): {t.ivm_volume():.6f}")
            print(f"XYZ Volume (from command line): {t.xyz_volume():.6f}")
        except ValueError:
            print("Error: All arguments must be numbers.")
    else:
        print("Usage: python tetravolume.py <a> <b> <c> <d> <e> <f>")
        print("Where <a>, <b>, <c>, <d>, <e>, <f> are the edges of the tetrahedron.")

def run_all_tests_and_demos():
    """Run all tests and demonstrations from tetravolume.py."""
    print("=== Running all tests and demonstrations ===\n")

    # Tetrahedron examples
    print("Tetrahedron Examples:")
    tet = Tetrahedron(D, D, D, D, D, D)
    print(f"Unit Tetrahedron IVM Volume: {tet.ivm_volume():.6f}")
    print(f"Unit Tetrahedron XYZ Volume: {tet.xyz_volume():.6f}\n")

    # Triangle examples
    print("Triangle Examples:")
    tri = Triangle(D, D, D)
    print(f"Unit Triangle IVM Area: {tri.ivm_area():.6f}")
    print(f"Unit Triangle XYZ Area: {tri.xyz_area():.6f}\n")

    # Additional examples
    print("Additional Examples:")
    v0 = Vector((R, 0, 0))
    v1 = Vector((0, R, 0))
    v2 = Vector((0, 0, R))
    ivm_vol, xyz_vol = make_tet(v0, v1, v2)
    print(f"Made Tetrahedron IVM Volume: {ivm_vol:.6f}, XYZ Volume: {xyz_vol:.6f}\n")

    v0_tri = Vector((D, 0, 0))
    v1_tri = Vector((0, D, 0))
    ivm_area, xyz_area = make_tri(v0_tri, v1_tri)
    print(f"Made Triangle IVM Area: {ivm_area:.6f}, XYZ Area: {xyz_area:.6f}\n")

    # Running unit tests
    print("Running Unit Tests:")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

if __name__ == "__main__":
    command_line()
    run_all_tests_and_demos()