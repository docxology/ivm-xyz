"""
Tests for Vector and Qvector classes.
"""

import unittest
from math import sqrt
from ivm_xyz.core.vectors import Vector, Qvector


class TestVector(unittest.TestCase):
    """Test cases for Vector class."""
    
    def test_vector_creation(self):
        """Test vector initialization."""
        v = Vector((1, 2, 3))
        self.assertEqual(v.x, 1.0)
        self.assertEqual(v.y, 2.0)
        self.assertEqual(v.z, 3.0)
    
    def test_vector_length(self):
        """Test vector length calculation."""
        v = Vector((3, 4, 0))
        self.assertAlmostEqual(v.length(), 5.0, places=5)
    
    def test_vector_addition(self):
        """Test vector addition."""
        v1 = Vector((1, 2, 3))
        v2 = Vector((4, 5, 6))
        v3 = v1 + v2
        self.assertEqual(v3.x, 5.0)
        self.assertEqual(v3.y, 7.0)
        self.assertEqual(v3.z, 9.0)
    
    def test_vector_subtraction(self):
        """Test vector subtraction."""
        v1 = Vector((5, 5, 5))
        v2 = Vector((2, 3, 4))
        v3 = v1 - v2
        self.assertEqual(v3.x, 3.0)
        self.assertEqual(v3.y, 2.0)
        self.assertEqual(v3.z, 1.0)
    
    def test_vector_scalar_multiplication(self):
        """Test scalar multiplication."""
        v = Vector((1, 2, 3))
        v2 = v * 2
        self.assertEqual(v2.x, 2.0)
        self.assertEqual(v2.y, 4.0)
        self.assertEqual(v2.z, 6.0)
    
    def test_vector_dot_product(self):
        """Test dot product."""
        v1 = Vector((1, 2, 3))
        v2 = Vector((4, 5, 6))
        dot = v1.dot(v2)
        self.assertEqual(dot, 32.0)  # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
    
    def test_vector_cross_product(self):
        """Test cross product."""
        v1 = Vector((1, 0, 0))
        v2 = Vector((0, 1, 0))
        cross = v1.cross(v2)
        self.assertEqual(cross.x, 0.0)
        self.assertEqual(cross.y, 0.0)
        self.assertEqual(cross.z, 1.0)
    
    def test_vector_quadray_conversion(self):
        """Test conversion to quadray."""
        v = Vector((1, 0, 0))
        q = v.quadray()
        self.assertIsInstance(q, Qvector)


class TestQvector(unittest.TestCase):
    """Test cases for Qvector class."""
    
    def test_qvector_creation(self):
        """Test quadray vector initialization."""
        q = Qvector((1, 2, 3, 4))
        self.assertEqual(q.a, 0.0)  # Normalized (min subtracted)
        self.assertGreaterEqual(q.a, 0)
        self.assertGreaterEqual(q.b, 0)
        self.assertGreaterEqual(q.c, 0)
        self.assertGreaterEqual(q.d, 0)
    
    def test_qvector_length(self):
        """Test quadray vector length."""
        q = Qvector((1, 0, 0, 0))
        self.assertGreater(q.length(), 0)
    
    def test_qvector_addition(self):
        """Test quadray vector addition."""
        q1 = Qvector((1, 0, 0, 0))
        q2 = Qvector((0, 1, 0, 0))
        q3 = q1 + q2
        self.assertIsInstance(q3, Qvector)
    
    def test_qvector_xyz_conversion(self):
        """Test conversion to XYZ."""
        q = Qvector((1, 0, 0, 0))
        v = q.xyz()
        self.assertIsInstance(v, Vector)
        self.assertAlmostEqual(v.x, 0.5/sqrt(2), places=5)
    
    def test_qvector_equality(self):
        """Test quadray vector equality."""
        q1 = Qvector((1, 1, 1, 1))
        q2 = Qvector((2, 2, 2, 2))
        # After normalization, they should be equal
        self.assertEqual(q1, q2)


class TestVectorConversions(unittest.TestCase):
    """Test bidirectional conversions between Vector and Qvector."""
    
    def test_xyz_to_quadray_and_back(self):
        """Test round-trip conversion."""
        original = Vector((1, 1, 1))
        quadray = original.quadray()
        back = quadray.xyz()
        # Should be approximately equal (within floating point precision)
        self.assertAlmostEqual(original.x, back.x, places=5)
        self.assertAlmostEqual(original.y, back.y, places=5)
        self.assertAlmostEqual(original.z, back.z, places=5)


if __name__ == '__main__':
    unittest.main()

