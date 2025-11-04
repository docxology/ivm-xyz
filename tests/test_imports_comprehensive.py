"""
Comprehensive import verification testing.
"""

import unittest
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ImportVerificationTests(unittest.TestCase):
    """Comprehensive import verification tests."""
    
    def test_package_level_imports(self):
        """Test all package-level imports."""
        logger.info("Testing package-level imports...")
        
        # Main package imports
        import ivm_xyz
        self.assertTrue(hasattr(ivm_xyz, '__version__'))
        logger.info(f"  Package version: {ivm_xyz.__version__}")
        
        # Core imports
        from ivm_xyz import Vector, Qvector
        self.assertIsNotNone(Vector)
        self.assertIsNotNone(Qvector)
        logger.info("  ✓ Vector, Qvector imported")
        
        from ivm_xyz import Tetrahedron, make_tet
        self.assertIsNotNone(Tetrahedron)
        self.assertIsNotNone(make_tet)
        logger.info("  ✓ Tetrahedron, make_tet imported")
        
        from ivm_xyz import Triangle, make_tri
        self.assertIsNotNone(Triangle)
        self.assertIsNotNone(make_tri)
        logger.info("  ✓ Triangle, make_tri imported")
        
        from ivm_xyz import xyz_to_ivm, ivm_to_xyz
        self.assertIsNotNone(xyz_to_ivm)
        self.assertIsNotNone(ivm_to_xyz)
        logger.info("  ✓ xyz_to_ivm, ivm_to_xyz imported")
        
        logger.info("✓ All package-level imports successful")
    
    def test_core_module_imports(self):
        """Test core module imports."""
        logger.info("Testing core module imports...")
        
        from ivm_xyz.core import Vector, Qvector, Tetrahedron, make_tet, Triangle, make_tri
        self.assertIsNotNone(Vector)
        self.assertIsNotNone(Qvector)
        self.assertIsNotNone(Tetrahedron)
        self.assertIsNotNone(make_tet)
        self.assertIsNotNone(Triangle)
        self.assertIsNotNone(make_tri)
        logger.info("  ✓ Core module imports successful")
        
        from ivm_xyz.core.vectors import Vector, Qvector
        from ivm_xyz.core.tetrahedron import Tetrahedron, make_tet
        from ivm_xyz.core.triangle import Triangle, make_tri
        from ivm_xyz.core.constants import S3, PHI, ROOT2, ROOT3, ROOT5
        logger.info("  ✓ Submodule imports successful")
        logger.info(f"  Constants: S3={S3:.6f}, PHI={PHI:.6f}")
    
    def test_conversion_module_imports(self):
        """Test conversion module imports."""
        logger.info("Testing conversion module imports...")
        
        from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz
        self.assertIsNotNone(xyz_to_ivm)
        self.assertIsNotNone(ivm_to_xyz)
        logger.info("  ✓ Conversion module imports successful")
        
        from ivm_xyz.conversion.converters import xyz_to_ivm, ivm_to_xyz, vector_to_qvector, qvector_to_vector
        self.assertIsNotNone(vector_to_qvector)
        self.assertIsNotNone(qvector_to_vector)
        logger.info("  ✓ Converter function imports successful")
    
    def test_polyhedra_module_imports(self):
        """Test polyhedra module imports."""
        logger.info("Testing polyhedra module imports...")
        
        from ivm_xyz.polyhedra import (
            Polyhedron, Edge, Cube, Octahedron, Icosahedron, Cuboctahedron,
            tet_edges, half_oct_edges, oct_edges, cubocta_edges, cubocta_layer
        )
        self.assertIsNotNone(Polyhedron)
        self.assertIsNotNone(Edge)
        self.assertIsNotNone(Cube)
        self.assertIsNotNone(Octahedron)
        self.assertIsNotNone(Icosahedron)
        self.assertIsNotNone(Cuboctahedron)
        self.assertIsNotNone(tet_edges)
        logger.info("  ✓ Polyhedra module imports successful")
        
        from ivm_xyz.polyhedra.base import Polyhedron, Edge
        from ivm_xyz.polyhedra.platonic import Cube, Octahedron, Icosahedron, Cuboctahedron
        from ivm_xyz.polyhedra.edge_counting import tet_edges, half_oct_edges
        logger.info("  ✓ Polyhedra submodule imports successful")
    
    def test_visualization_module_imports(self):
        """Test visualization module imports."""
        logger.info("Testing visualization module imports...")
        
        from ivm_xyz.visualization import PolyhedronPlotter
        self.assertIsNotNone(PolyhedronPlotter)
        logger.info("  ✓ Visualization module imports successful")
        
        from ivm_xyz.visualization.plotter import PolyhedronPlotter
        logger.info("  ✓ Plotter submodule imports successful")
    
    def test_circular_import_prevention(self):
        """Test that circular imports are prevented."""
        logger.info("Testing circular import prevention...")
        
        # Try importing in different orders
        import ivm_xyz
        from ivm_xyz.core import Vector
        from ivm_xyz.conversion import xyz_to_ivm
        from ivm_xyz.polyhedra import Cube
        from ivm_xyz.visualization import PolyhedronPlotter
        
        # Verify no circular import issues
        self.assertTrue(True)
        logger.info("  ✓ No circular import issues detected")
    
    def test_all_exports_in_init(self):
        """Test that all __init__.py exports work."""
        logger.info("Testing __init__.py exports...")
        
        import ivm_xyz
        expected_exports = [
            'Vector', 'Qvector', 'Tetrahedron', 'make_tet',
            'Triangle', 'make_tri', 'xyz_to_ivm', 'ivm_to_xyz', '__version__'
        ]
        
        for export in expected_exports:
            self.assertTrue(
                hasattr(ivm_xyz, export),
                f"Missing export: {export}"
            )
        logger.info(f"  ✓ All {len(expected_exports)} exports present")
    
    def test_import_usage(self):
        """Test that imported modules can be used."""
        logger.info("Testing import usage...")
        
        from ivm_xyz import Vector, Tetrahedron, xyz_to_ivm
        
        # Test Vector usage
        v = Vector((1, 2, 3))
        self.assertEqual(v.x, 1.0)
        logger.info("  ✓ Vector usage works")
        
        # Test Tetrahedron usage
        tet = Tetrahedron(1, 1, 1, 1, 1, 1)
        vol = tet.ivm_volume()
        self.assertGreater(vol, 0)
        logger.info("  ✓ Tetrahedron usage works")
        
        # Test conversion usage
        quadray = xyz_to_ivm(1.0, 2.0, 3.0)
        self.assertEqual(len(quadray), 4)
        logger.info("  ✓ Conversion usage works")
        
        logger.info("✓ All imports are functional")


if __name__ == '__main__':
    unittest.main(verbosity=2)

