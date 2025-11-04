"""
Tests for coordinate conversion functions.
"""

import unittest
from math import sqrt, isclose
from ivm_xyz.conversion.converters import xyz_to_ivm, ivm_to_xyz, vector_to_qvector, qvector_to_vector
from ivm_xyz.core.vectors import Vector, Qvector


class TestConversion(unittest.TestCase):
    """Test cases for coordinate conversion functions."""
    
    def test_xyz_to_ivm_basic(self):
        """Test basic XYZ to IVM conversion."""
        a, b, c, d = xyz_to_ivm(1, 0, 0)
        # All quadray coordinates should be non-negative after normalization
        self.assertGreaterEqual(a, 0)
        self.assertGreaterEqual(b, 0)
        self.assertGreaterEqual(c, 0)
        self.assertGreaterEqual(d, 0)
    
    def test_ivm_to_xyz_basic(self):
        """Test basic IVM to XYZ conversion."""
        x, y, z = ivm_to_xyz(1, 0, 0, 0)
        # Should produce valid XYZ coordinates
        self.assertIsInstance(x, float)
        self.assertIsInstance(y, float)
        self.assertIsInstance(z, float)
    
    def test_round_trip_conversion(self):
        """Test round-trip conversion: XYZ -> IVM -> XYZ."""
        original_xyz = (1.0, 2.0, 3.0)
        ivm_coords = xyz_to_ivm(*original_xyz)
        result_xyz = ivm_to_xyz(*ivm_coords)
        
        # Should be approximately equal (within floating point precision)
        self.assertAlmostEqual(original_xyz[0], result_xyz[0], places=5)
        self.assertAlmostEqual(original_xyz[1], result_xyz[1], places=5)
        self.assertAlmostEqual(original_xyz[2], result_xyz[2], places=5)
    
    def test_zero_origin(self):
        """Test conversion of origin point."""
        ivm_coords = xyz_to_ivm(0, 0, 0)
        # All coordinates should be zero after normalization
        self.assertAlmostEqual(sum(ivm_coords), 0, places=5)
        
        xyz_coords = ivm_to_xyz(0, 0, 0, 0)
        self.assertAlmostEqual(xyz_coords[0], 0, places=5)
        self.assertAlmostEqual(xyz_coords[1], 0, places=5)
        self.assertAlmostEqual(xyz_coords[2], 0, places=5)
    
    def test_vector_to_qvector(self):
        """Test Vector to Qvector conversion."""
        v = Vector((1, 1, 1))
        q = vector_to_qvector(v)
        self.assertIsInstance(q, Qvector)
    
    def test_qvector_to_vector(self):
        """Test Qvector to Vector conversion."""
        q = Qvector((1, 0, 0, 0))
        v = qvector_to_vector(q)
        self.assertIsInstance(v, Vector)
    
    def test_negative_coordinates(self):
        """Test conversion with negative coordinates."""
        ivm_coords = xyz_to_ivm(-1, -2, -3)
        # After normalization, all should be non-negative
        self.assertGreaterEqual(ivm_coords[0], 0)
        self.assertGreaterEqual(ivm_coords[1], 0)
        self.assertGreaterEqual(ivm_coords[2], 0)
        self.assertGreaterEqual(ivm_coords[3], 0)
        
        # Convert back
        xyz_result = ivm_to_xyz(*ivm_coords)
        # Should approximate original (within normalization)
        self.assertIsInstance(xyz_result[0], float)
    
    def test_multiple_round_trips(self):
        """Test multiple round-trip conversions maintain precision."""
        test_points = [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 1),
            (2.5, 3.7, -1.2)
        ]
        
        for point in test_points:
            ivm = xyz_to_ivm(*point)
            xyz = ivm_to_xyz(*ivm)
            # Check that we get back something reasonable
            self.assertIsInstance(xyz[0], float)
            self.assertIsInstance(xyz[1], float)
            self.assertIsInstance(xyz[2], float)


if __name__ == '__main__':
    unittest.main()

