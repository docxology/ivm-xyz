"""
Tests for Triangle class.
"""

import unittest
from math import sqrt
from ivm_xyz.core.triangle import Triangle, make_tri
from ivm_xyz.core.vectors import Vector
from ivm_xyz.core.constants import D, S3


class TestTriangle(unittest.TestCase):
    """Test cases for Triangle class."""
    
    def test_equilateral_triangle(self):
        """Test equilateral triangle area calculation."""
        tri = Triangle(D, D, D)
        ivm_area = tri.ivm_area()
        xyz_area = tri.xyz_area()
        
        # Area should be positive
        self.assertGreater(ivm_area, 0)
        self.assertGreater(xyz_area, 0)
        
        # XYZ area should be smaller (divided by S3)
        self.assertLess(xyz_area, ivm_area)
    
    def test_triangle_area_relationship(self):
        """Test relationship between IVM and XYZ areas."""
        tri = Triangle(1, 1, 1)
        ivm_area = tri.ivm_area()
        xyz_area = tri.xyz_area()
        
        # xyz_area = ivm_area / S3
        expected_xyz = ivm_area / S3
        self.assertAlmostEqual(xyz_area, expected_xyz, places=5)
    
    def test_make_tri_from_vectors(self):
        """Test making triangle from two vectors."""
        v0 = Vector((1, 0, 0))
        v1 = Vector((0, 1, 0))
        ivm_area, xyz_area = make_tri(v0, v1)
        
        self.assertGreater(ivm_area, 0)
        self.assertGreater(xyz_area, 0)
        self.assertAlmostEqual(xyz_area, ivm_area / S3, places=5)
    
    def test_triangle_herons_formula(self):
        """Test Heron's formula implementation."""
        # For a 3-4-5 right triangle
        tri = Triangle(3, 4, 5)
        area = tri.ivm_area()
        # Using Heron's formula: s = 6, area = sqrt(6*3*2*1) = sqrt(36) = 6
        self.assertAlmostEqual(area, 6.0, places=5)


if __name__ == '__main__':
    unittest.main()

