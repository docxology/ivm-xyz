"""
Comprehensive integration testing.
"""

import unittest
import logging
import sys
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IntegrationTests(unittest.TestCase):
    """Comprehensive integration tests."""
    
    def test_xyz_to_ivm_workflow(self):
        """Test complete XYZ -> IVM -> calculations workflow."""
        logger.info("Testing XYZ -> IVM workflow...")
        
        from ivm_xyz import Vector, xyz_to_ivm, make_tet
        
        # Start with XYZ coordinates
        x, y, z = 1.0, 2.0, 3.0
        
        # Convert to IVM
        quadray = xyz_to_ivm(x, y, z)
        self.assertEqual(len(quadray), 4)
        logger.info(f"  ✓ Converted to IVM: {quadray}")
        
        # Create vectors
        v1 = Vector((1, 0, 0))
        v2 = Vector((0, 1, 0))
        v3 = Vector((0, 0, 1))
        
        # Calculate volumes
        ivm_vol, xyz_vol = make_tet(v1, v2, v3)
        self.assertGreater(ivm_vol, 0)
        self.assertGreater(xyz_vol, 0)
        logger.info(f"  ✓ Calculated volumes: IVM={ivm_vol:.6f}, XYZ={xyz_vol:.6f}")
        
        logger.info("✓ XYZ -> IVM workflow verified")
    
    def test_polyhedra_to_visualization_workflow(self):
        """Test polyhedra creation to visualization workflow."""
        logger.info("Testing polyhedra -> visualization workflow...")
        
        from ivm_xyz.polyhedra import Cube
        from ivm_xyz.visualization import PolyhedronPlotter
        import tempfile
        import shutil
        
        # Create polyhedron
        cube = Cube()
        logger.info(f"  ✓ Created cube: {cube.name}, volume={cube.volume}")
        
        # Extract vertices for visualization
        vertices = []
        for key in sorted(cube.vertexes.keys()):
            v = cube.vertexes[key]
            # Convert Qvector to XYZ if needed
            if hasattr(v, 'xyz'):
                xyz = v.xyz()
                vertices.append((xyz.x, xyz.y, xyz.z))
            else:
                vertices.append((v.x, v.y, v.z))
        
        # Create faces (simplified - cube has 6 faces)
        faces = [
            (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
            (2, 6, 7, 3), (0, 3, 7, 4), (1, 5, 6, 2)
        ]
        
        # Create visualization
        temp_dir = tempfile.mkdtemp()
        try:
            plotter = PolyhedronPlotter(output_folder=temp_dir)
            plotter.plot_polyhedron(
                vertices, faces, "Cube Visualization", save=True, file_name="cube_integration.png"
            )
            
            file_path = os.path.join(temp_dir, "cube_integration.png")
            self.assertTrue(os.path.exists(file_path))
            logger.info(f"  ✓ Visualization created: {file_path}")
        finally:
            shutil.rmtree(temp_dir)
        
        logger.info("✓ Polyhedra -> visualization workflow verified")
    
    def test_example_scripts_execution(self):
        """Test that example scripts can be executed."""
        logger.info("Testing example scripts...")
        
        # Test basic_usage.py
        example_path = "examples/basic_usage.py"
        if os.path.exists(example_path):
            import subprocess
            result = subprocess.run(
                [sys.executable, example_path],
                capture_output=True,
                text=True,
                cwd=os.getcwd(),
                env={**os.environ, 'PYTHONPATH': '.'}
            )
            self.assertEqual(result.returncode, 0, f"Example script failed: {result.stderr}")
            logger.info("  ✓ basic_usage.py executed successfully")
        else:
            logger.warning(f"  ⚠ Example script not found: {example_path}")
        
        logger.info("✓ Example scripts verified")
    
    def test_package_installation_simulation(self):
        """Test that package can be imported as if installed."""
        logger.info("Testing package installation simulation...")
        
        # Try importing as if installed (using PYTHONPATH environment variable)
        # Note: sys.path manipulation removed - use PYTHONPATH=. when running tests
        try:
            import ivm_xyz
            from ivm_xyz import Vector, Tetrahedron
            from ivm_xyz.conversion import xyz_to_ivm
            from ivm_xyz.polyhedra import Cube
            from ivm_xyz.visualization import PolyhedronPlotter
            
            # Verify all imports work
            self.assertTrue(hasattr(ivm_xyz, '__version__'))
            self.assertIsNotNone(Vector)
            self.assertIsNotNone(Tetrahedron)
            self.assertIsNotNone(xyz_to_ivm)
            self.assertIsNotNone(Cube)
            self.assertIsNotNone(PolyhedronPlotter)
            
            logger.info("  ✓ Package imports work correctly")
            logger.info(f"  ✓ Package version: {ivm_xyz.__version__}")
        except Exception as e:
            self.fail(f"Package import failed: {e}")
        
        logger.info("✓ Package installation simulation verified")
    
    def test_end_to_end_workflow(self):
        """Test complete end-to-end workflow."""
        logger.info("Testing end-to-end workflow...")
        
        from ivm_xyz import Vector, Qvector, Tetrahedron, make_tet, xyz_to_ivm, ivm_to_xyz
        from ivm_xyz.polyhedra import Cube, tet_edges
        
        # 1. Coordinate conversion
        xyz_point = (1.0, 2.0, 3.0)
        quadray = xyz_to_ivm(*xyz_point)
        xyz_back = ivm_to_xyz(*quadray)
        self.assertAlmostEqual(xyz_point[0], xyz_back[0], places=5)
        logger.info("  ✓ Step 1: Coordinate conversion")
        
        # 2. Vector operations
        v1 = Vector((1, 0, 0))
        v2 = Vector((0, 1, 0))
        v3 = Vector((0, 0, 1))
        q1 = v1.quadray()
        v1_back = q1.xyz()
        self.assertAlmostEqual(v1.x, v1_back.x, places=5)
        logger.info("  ✓ Step 2: Vector operations")
        
        # 3. Volume calculations
        ivm_vol, xyz_vol = make_tet(v1, v2, v3)
        self.assertGreater(ivm_vol, 0)
        logger.info("  ✓ Step 3: Volume calculations")
        
        # 4. Polyhedra operations
        cube = Cube()
        scaled = cube.scale(2.0)
        self.assertEqual(scaled.volume, 24.0)
        logger.info("  ✓ Step 4: Polyhedra operations")
        
        # 5. Edge counting
        edges = tet_edges(5)
        self.assertGreater(edges, 0)
        logger.info("  ✓ Step 5: Edge counting")
        
        logger.info("✓ End-to-end workflow verified")


if __name__ == '__main__':
    unittest.main(verbosity=2)

