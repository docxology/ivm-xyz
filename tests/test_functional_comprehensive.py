"""
Comprehensive functional verification testing.
"""

import unittest
import logging
from math import sqrt, isclose

from ivm_xyz import Vector, Qvector, Tetrahedron, make_tet, Triangle, make_tri
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz
from ivm_xyz.core.constants import D, R, PHI, ROOT2, ROOT3, S3
from ivm_xyz.polyhedra import Cube, Octahedron, tet_edges

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FunctionalVerificationTests(unittest.TestCase):
    """Comprehensive functional verification tests."""
    
    def test_vector_operations_comprehensive(self):
        """Test all Vector operations with various inputs."""
        logger.info("Testing Vector operations...")
        
        # Basic operations
        v1 = Vector((1, 0, 0))
        v2 = Vector((0, 1, 0))
        v3 = Vector((0, 0, 1))
        
        # Addition
        v_sum = v1 + v2
        self.assertEqual(v_sum.x, 1.0)
        self.assertEqual(v_sum.y, 1.0)
        logger.info("  ✓ Vector addition")
        
        # Subtraction
        v_diff = v1 - v2
        self.assertEqual(v_diff.x, 1.0)
        self.assertEqual(v_diff.y, -1.0)
        logger.info("  ✓ Vector subtraction")
        
        # Scalar multiplication
        v_scaled = v1 * 2
        self.assertEqual(v_scaled.x, 2.0)
        logger.info("  ✓ Scalar multiplication")
        
        # Dot product
        dot = v1.dot(v2)
        self.assertEqual(dot, 0.0)
        logger.info("  ✓ Dot product")
        
        # Cross product
        cross = v1.cross(v2)
        self.assertEqual(cross.z, 1.0)
        logger.info("  ✓ Cross product")
        
        # Length
        length = Vector((3, 4, 0)).length()
        self.assertAlmostEqual(length, 5.0, places=5)
        logger.info("  ✓ Length calculation")
        
        # Unit vector
        unit = Vector((3, 4, 0)).unit()
        self.assertAlmostEqual(unit.length(), 1.0, places=5)
        logger.info("  ✓ Unit vector")
        
        # Rotation
        v_rot = v1.rotz(90)
        self.assertAlmostEqual(v_rot.y, 1.0, places=5)
        logger.info("  ✓ Rotation")
        
        logger.info("✓ All Vector operations verified")
    
    def test_qvector_operations_comprehensive(self):
        """Test all Qvector operations."""
        logger.info("Testing Qvector operations...")
        
        # Basic operations
        q1 = Qvector((1, 0, 0, 0))
        q2 = Qvector((0, 1, 0, 0))
        
        # Addition
        q_sum = q1 + q2
        self.assertIsInstance(q_sum, Qvector)
        logger.info("  ✓ Qvector addition")
        
        # Subtraction
        q_diff = q1 - q2
        self.assertIsInstance(q_diff, Qvector)
        logger.info("  ✓ Qvector subtraction")
        
        # Scalar multiplication
        q_scaled = q1 * 2
        self.assertIsInstance(q_scaled, Qvector)
        logger.info("  ✓ Qvector scalar multiplication")
        
        # Length
        length = q1.length()
        self.assertGreater(length, 0)
        logger.info("  ✓ Qvector length")
        
        # Dot product
        dot = q1.dot(q2)
        self.assertIsInstance(dot, (int, float))
        logger.info("  ✓ Qvector dot product")
        
        # Cross product
        cross = q1.cross(q2)
        self.assertIsInstance(cross, Qvector)
        logger.info("  ✓ Qvector cross product")
        
        # Conversion to XYZ
        v = q1.xyz()
        self.assertIsInstance(v, Vector)
        logger.info("  ✓ Qvector to Vector conversion")
        
        logger.info("✓ All Qvector operations verified")
    
    def test_tetrahedron_calculations_edge_cases(self):
        """Test tetrahedron calculations with edge cases."""
        logger.info("Testing tetrahedron edge cases...")
        
        # Unit tetrahedron
        tet1 = Tetrahedron(D, D, D, D, D, D)
        vol1 = tet1.ivm_volume()
        self.assertAlmostEqual(vol1, 1.0, places=5)
        logger.info(f"  ✓ Unit tetrahedron: {vol1:.6f}")
        
        # Different edge lengths
        tet2 = Tetrahedron(1, 1, 1, ROOT2, ROOT2, ROOT2)
        vol2 = tet2.ivm_volume()
        self.assertGreater(vol2, 0)
        logger.info(f"  ✓ Different edges: {vol2:.6f}")
        
        # Large values
        tet3 = Tetrahedron(10, 10, 10, 10, 10, 10)
        vol3 = tet3.ivm_volume()
        expected = 1000.0  # 10^3
        self.assertAlmostEqual(vol3, expected, places=2)
        logger.info(f"  ✓ Large values: {vol3:.6f}")
        
        # Small values
        tet4 = Tetrahedron(0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
        vol4 = tet4.ivm_volume()
        self.assertGreater(vol4, 0)
        logger.info(f"  ✓ Small values: {vol4:.6f}")
        
        # XYZ volume conversion
        xyz_vol = tet1.xyz_volume()
        self.assertAlmostEqual(xyz_vol, 1.0 / S3, places=5)
        logger.info(f"  ✓ XYZ volume: {xyz_vol:.6f}")
        
        logger.info("✓ All tetrahedron edge cases verified")
    
    def test_triangle_calculations(self):
        """Test triangle calculations."""
        logger.info("Testing triangle calculations...")
        
        # Equilateral triangle
        tri1 = Triangle(1, 1, 1)
        area1 = tri1.ivm_area()
        self.assertGreater(area1, 0)
        logger.info(f"  ✓ Equilateral triangle IVM area: {area1:.6f}")
        
        # Right triangle
        tri2 = Triangle(3, 4, 5)
        area2 = tri2.ivm_area()
        self.assertAlmostEqual(area2, 6.0, places=5)
        logger.info(f"  ✓ Right triangle area: {area2:.6f}")
        
        # XYZ area conversion
        xyz_area = tri1.xyz_area()
        self.assertAlmostEqual(xyz_area, area1 / S3, places=5)
        logger.info(f"  ✓ XYZ area conversion: {xyz_area:.6f}")
        
        logger.info("✓ All triangle calculations verified")
    
    def test_coordinate_conversions_round_trip(self):
        """Test coordinate conversions with round-trip accuracy."""
        logger.info("Testing coordinate conversions...")
        
        test_points = [
            (0, 0, 0),
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 1),
            (2.5, 3.7, -1.2),
            (-1, -2, -3),
            (10, 20, 30),
        ]
        
        max_error = 0.0
        for point in test_points:
            x, y, z = point
            quadray = xyz_to_ivm(x, y, z)
            xyz_back = ivm_to_xyz(*quadray)
            
            error_x = abs(x - xyz_back[0])
            error_y = abs(y - xyz_back[1])
            error_z = abs(z - xyz_back[2])
            max_point_error = max(error_x, error_y, error_z)
            max_error = max(max_error, max_point_error)
            
            self.assertAlmostEqual(x, xyz_back[0], places=5, msg=f"Point {point}")
            self.assertAlmostEqual(y, xyz_back[1], places=5, msg=f"Point {point}")
            self.assertAlmostEqual(z, xyz_back[2], places=5, msg=f"Point {point}")
        
        logger.info(f"  ✓ Round-trip conversion tested with {len(test_points)} points")
        logger.info(f"  ✓ Maximum error: {max_error:.10f}")
        logger.info("✓ All coordinate conversions verified")
    
    def test_polyhedra_creation_and_transformations(self):
        """Test polyhedra creation and transformations."""
        logger.info("Testing polyhedra operations...")
        
        # Create polyhedra
        cube = Cube()
        self.assertEqual(cube.volume, 3)
        self.assertEqual(len(cube.vertexes), 8)
        logger.info("  ✓ Cube creation")
        
        octa = Octahedron()
        self.assertEqual(octa.volume, 4)
        self.assertEqual(len(octa.vertexes), 6)
        logger.info("  ✓ Octahedron creation")
        
        # Scaling
        scaled_cube = cube.scale(2.0)
        self.assertEqual(scaled_cube.volume, 24.0)  # 3 * 2^3
        logger.info("  ✓ Polyhedron scaling")
        
        # Translation
        from ivm_xyz.core.vectors import Qvector
        translation = Qvector((1, 0, 0, 0))
        translated_cube = cube.translate(translation)
        self.assertIsInstance(translated_cube, Cube)
        logger.info("  ✓ Polyhedron translation")
        
        logger.info("✓ All polyhedra operations verified")
    
    def test_edge_counting_functions(self):
        """Test edge counting functions."""
        logger.info("Testing edge counting functions...")
        
        # Tetrahedron edges
        edges1 = tet_edges(1)
        self.assertEqual(edges1, 6)
        logger.info(f"  ✓ tet_edges(1) = {edges1}")
        
        edges2 = tet_edges(2)
        self.assertEqual(edges2, 24)
        logger.info(f"  ✓ tet_edges(2) = {edges2}")
        
        edges3 = tet_edges(3)
        self.assertEqual(edges3, 60)
        logger.info(f"  ✓ tet_edges(3) = {edges3}")
        
        # Test multiple frequencies
        for f in range(1, 6):
            edges = tet_edges(f)
            self.assertGreater(edges, 0)
        logger.info("  ✓ Multiple frequencies tested")
        
        logger.info("✓ All edge counting functions verified")


if __name__ == '__main__':
    unittest.main(verbosity=2)

