"""
Tests for Tetrahedron class.
"""

import unittest
from math import sqrt
from ivm_xyz.core.tetrahedron import Tetrahedron, make_tet
from ivm_xyz.core.vectors import Vector, Qvector
from ivm_xyz.core.constants import D, R, PHI, ROOT2, ROOT3


class TestTetrahedron(unittest.TestCase):
    """Test cases for Tetrahedron class."""
    
    def test_unit_volume(self):
        """Test unit tetrahedron volume calculation."""
        tet = Tetrahedron(D, D, D, D, D, D)
        self.assertAlmostEqual(tet.ivm_volume(), 1.0, places=5)
    
    def test_xyz_volume(self):
        """Test XYZ volume calculation."""
        tet = Tetrahedron(R, R, R, R, R, R)
        xyz_vol = tet.xyz_volume()
        self.assertAlmostEqual(xyz_vol, 0.117851130, places=5)
    
    def test_phi_edge_tetra(self):
        """Test tetrahedron with phi edge."""
        tet = Tetrahedron(D, D, D, D, D, PHI)
        ivm_vol = tet.ivm_volume()
        self.assertAlmostEqual(ivm_vol, 0.70710678, places=5)
    
    def test_right_tetra(self):
        """Test right tetrahedron."""
        e = sqrt((ROOT3/2)**2 + (ROOT3/2)**2)
        tet = Tetrahedron(D, D, D, D, D, e)
        xyz_vol = tet.xyz_volume()
        self.assertAlmostEqual(xyz_vol, 1.0, places=4)
    
    def test_make_tet_from_vectors(self):
        """Test making tetrahedron from vectors."""
        v0 = Vector((0.5, 0, 0))
        v1 = Vector((0, 0.5, 0))
        v2 = Vector((0, 0, 0.5))
        ivm_vol, xyz_vol = make_tet(v0, v1, v2)
        self.assertGreater(ivm_vol, 0)
        self.assertGreater(xyz_vol, 0)
        self.assertAlmostEqual(xyz_vol, 1/6, places=5)
    
    def test_make_tet_from_quadrays(self):
        """Test making tetrahedron from quadray vectors."""
        qA = Qvector((1, 0, 0, 0))
        qB = Qvector((0, 1, 0, 0))
        qC = Qvector((0, 0, 1, 0))
        ivm_vol, xyz_vol = make_tet(qA, qB, qC)
        self.assertAlmostEqual(ivm_vol, 0.25, places=5)
    
    def test_quarter_octahedron(self):
        """Test quarter octahedron volume."""
        a = Vector((1, 0, 0))
        b = Vector((0, 1, 0))
        c = Vector((0.5, 0.5, ROOT2/2))
        ivm_vol, xyz_vol = make_tet(a, b, c)
        self.assertAlmostEqual(ivm_vol, 1.0, places=5)
    
    def test_xyz_cube(self):
        """Test XYZ cube volume."""
        a = Vector((0.5, 0.0, 0.0))
        b = Vector((0.0, 0.5, 0.0))
        c = Vector((0.0, 0.0, 0.5))
        ivm_vol, xyz_vol = make_tet(a, b, c)
        self.assertAlmostEqual(6 * xyz_vol, 1.0, places=4)
    
    def test_s3_relationship(self):
        """Test S3 relationship between IVM and XYZ volumes."""
        D_tet = Tetrahedron(D, D, D, D, D, D)
        a = Vector((0.5, 0.0, 0.0))
        b = Vector((0.0, 0.5, 0.0))
        c = Vector((0.0, 0.0, 0.5))
        R_cube = 6 * make_tet(a, b, c)[1]
        from ivm_xyz.core.constants import S3
        self.assertAlmostEqual(D_tet.xyz_volume() * S3, R_cube, places=4)
    
    def test_martian_tetrahedron(self):
        """Test Martian tetrahedron volume calculation."""
        p = Qvector((2, 1, 0, 1))
        q = Qvector((2, 1, 1, 0))
        r = Qvector((2, 0, 1, 1))
        ivm_vol, xyz_vol = make_tet(5*q, 2*p, 2*r)
        self.assertAlmostEqual(ivm_vol, 20.0, places=7)


if __name__ == '__main__':
    unittest.main()

