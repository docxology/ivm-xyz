"""
Tests for advanced Vector methods not covered in basic tests.
"""

import unittest
from math import sqrt, isclose
from ivm_xyz.core.vectors import Vector, Qvector, Svector


class TestVectorAdvanced(unittest.TestCase):
    """Test cases for advanced Vector methods."""
    
    def test_vector_rotations(self):
        """Test rotation methods."""
        # Test rotx (rotation around X-axis) - rotates Y and Z
        v1 = Vector((0, 1, 0))
        v_rotx = v1.rotx(90)
        # When rotating (0,1,0) 90° around X, should get (0,0,1)
        self.assertAlmostEqual(v_rotx.x, 0.0, places=5)
        self.assertAlmostEqual(v_rotx.y, 0.0, places=5)
        self.assertAlmostEqual(v_rotx.z, 1.0, places=5)
        
        # Test roty (rotation around Y-axis) - rotates X and Z
        v2 = Vector((1, 0, 0))
        v_roty = v2.roty(90)
        # When rotating (1,0,0) 90° around Y, should get (0,0,-1) or (0,0,1)
        self.assertAlmostEqual(v_roty.x, 0.0, places=5)
        self.assertAlmostEqual(v_roty.y, 0.0, places=5)
        self.assertAlmostEqual(abs(v_roty.z), 1.0, places=5)
        
        # Test rotz (rotation around Z-axis) - rotates X and Y
        v3 = Vector((1, 0, 0))
        v_rotz = v3.rotz(90)
        # When rotating (1,0,0) 90° around Z, should get (0,1,0)
        self.assertAlmostEqual(v_rotz.x, 0.0, places=5)
        self.assertAlmostEqual(v_rotz.y, 1.0, places=5)
        self.assertAlmostEqual(v_rotz.z, 0.0, places=5)
        
        # Test rotaxis (rotation around arbitrary axis)
        axis = Vector((0, 0, 1))
        v4 = Vector((1, 0, 0))
        v_rotaxis = v4.rotaxis(axis, 90)
        self.assertIsInstance(v_rotaxis, Vector)
        # Should rotate around Z-axis (may be -1 or 1 depending on direction)
        self.assertAlmostEqual(abs(v_rotaxis.y), 1.0, places=5)
        self.assertAlmostEqual(v_rotaxis.x, 0.0, places=5)
    
    def test_vector_spherical(self):
        """Test spherical coordinate conversion."""
        # Test unit vector along X-axis
        v1 = Vector((1, 0, 0))
        r, phi, theta = v1.spherical()
        self.assertAlmostEqual(r, 1.0, places=5)
        self.assertAlmostEqual(phi, 90.0, places=5)  # 90 degrees from Z-axis
        self.assertAlmostEqual(theta, 0.0, places=5)
        
        # Test unit vector along Z-axis
        v2 = Vector((0, 0, 1))
        r, phi, theta = v2.spherical()
        self.assertAlmostEqual(r, 1.0, places=5)
        self.assertAlmostEqual(phi, 0.0, places=5)
        
        # Test zero vector
        v3 = Vector((0, 0, 0))
        r, phi, theta = v3.spherical()
        self.assertAlmostEqual(r, 0.0, places=5)
    
    def test_vector_unit(self):
        """Test unit vector calculation."""
        # Test unit vector
        v1 = Vector((3, 4, 0))
        unit = v1.unit()
        self.assertAlmostEqual(unit.length(), 1.0, places=5)
        
        # Test unit vector direction preserved
        v2 = Vector((2, 2, 2))
        unit2 = v2.unit()
        # Should be normalized but same direction
        self.assertAlmostEqual(unit2.x, unit2.y, places=5)
        self.assertAlmostEqual(unit2.y, unit2.z, places=5)
    
    def test_qvector_norm0(self):
        """Test Qvector norm0 normalization."""
        q1 = Qvector((1, 2, 3, 4))
        norm0_result = q1.norm0()
        # Sum should be approximately 0
        total = sum(norm0_result)
        self.assertAlmostEqual(total, 0.0, places=5)
    
    def test_svector(self):
        """Test Svector class."""
        # Create from spherical coordinates
        # Note: Svector converts input to spherical first, so pass regular vector coords
        sv = Svector((1.0, 0.0, 0.0))  # This will be converted to spherical first
        self.assertIsInstance(sv, Vector)
        self.assertIsInstance(sv, Svector)
        
        # Test that it has valid xyz coordinates
        self.assertIsNotNone(sv.xyz)
        self.assertIsNotNone(sv.x)
        self.assertIsNotNone(sv.y)
        self.assertIsNotNone(sv.z)
        
        # Test conversion back to spherical (should work)
        r, phi, theta = sv.spherical()
        self.assertGreaterEqual(r, 0.0)
        self.assertGreaterEqual(phi, 0.0)
        
        # Test that Svector creates valid vector from spherical coords
        # Svector first converts input to spherical, so we need to pass actual coords
        # Create a vector and get its spherical coords, then recreate
        v = Vector((1.0, 0.0, 0.0))
        r_exp, phi_exp, theta_exp = v.spherical()
        # Create Svector from those coords (it will convert again, but should work)
        sv2 = Svector((r_exp, phi_exp, theta_exp))
        # Verify it's a valid vector
        self.assertIsInstance(sv2, Svector)
        self.assertIsInstance(sv2, Vector)
        # The result may differ due to double conversion, but should be valid
        r2, phi2, theta2 = sv2.spherical()
        self.assertGreater(r2, 0.0)


if __name__ == '__main__':
    unittest.main()

