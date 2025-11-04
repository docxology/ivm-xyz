"""
Comprehensive visualization testing with detailed logging.
"""

import unittest
import os
import tempfile
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ComprehensiveVisualizationTests(unittest.TestCase):
    """Comprehensive tests for visualization functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        logger.info(f"Created temp directory: {self.temp_dir}")
    
    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
        logger.info(f"Removed temp directory: {self.temp_dir}")
    
    def test_plotter_initialization(self):
        """Test PolyhedronPlotter initialization."""
        logger.info("Testing plotter initialization...")
        from ivm_xyz.visualization import PolyhedronPlotter
        
        plotter = PolyhedronPlotter(output_folder=self.temp_dir)
        self.assertEqual(plotter.output_folder, self.temp_dir)
        self.assertEqual(len(plotter.polyhedrons), 0)
        self.assertTrue(os.path.exists(self.temp_dir))
        logger.info("✓ Plotter initialization successful")
    
    def test_static_plot_tetrahedron(self):
        """Test static plot generation for tetrahedron."""
        logger.info("Testing tetrahedron static plot...")
        from ivm_xyz.visualization import PolyhedronPlotter
        
        plotter = PolyhedronPlotter(output_folder=self.temp_dir)
        vertices = [(0, 0, 0), (1, 0, 0), (0.5, 0.866, 0), (0.5, 0.289, 0.816)]
        faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        
        plotter.plot_polyhedron(
            vertices, faces, "Test Tetrahedron", save=True, file_name="tet_test.png"
        )
        
        file_path = os.path.join(self.temp_dir, "tet_test.png")
        self.assertTrue(os.path.exists(file_path), f"File not created: {file_path}")
        logger.info(f"✓ Tetrahedron plot created: {file_path}")
    
    def test_static_plot_cube(self):
        """Test static plot generation for cube."""
        logger.info("Testing cube static plot...")
        from ivm_xyz.visualization import PolyhedronPlotter
        
        plotter = PolyhedronPlotter(output_folder=self.temp_dir)
        vertices = [
            (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
        ]
        faces = [
            (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
            (2, 6, 7, 3), (0, 3, 7, 4), (1, 5, 6, 2)
        ]
        
        plotter.plot_polyhedron(
            vertices, faces, "Test Cube", save=True, file_name="cube_test.png"
        )
        
        file_path = os.path.join(self.temp_dir, "cube_test.png")
        self.assertTrue(os.path.exists(file_path))
        logger.info(f"✓ Cube plot created: {file_path}")
    
    def test_static_plot_octahedron(self):
        """Test static plot generation for octahedron."""
        logger.info("Testing octahedron static plot...")
        from ivm_xyz.visualization import PolyhedronPlotter
        
        plotter = PolyhedronPlotter(output_folder=self.temp_dir)
        vertices = [
            (0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0),
            (1, 0, 0), (-1, 0, 0)
        ]
        faces = [
            (0, 1, 4), (0, 4, 2), (0, 2, 5), (0, 5, 1),
            (3, 1, 4), (3, 4, 2), (3, 2, 5), (3, 5, 1)
        ]
        
        plotter.plot_polyhedron(
            vertices, faces, "Test Octahedron", save=True, file_name="octa_test.png"
        )
        
        file_path = os.path.join(self.temp_dir, "octa_test.png")
        self.assertTrue(os.path.exists(file_path))
        logger.info(f"✓ Octahedron plot created: {file_path}")
    
    def test_add_polyhedron(self):
        """Test adding polyhedron to plotter."""
        logger.info("Testing add_polyhedron method...")
        from ivm_xyz.visualization import PolyhedronPlotter
        
        plotter = PolyhedronPlotter(output_folder=self.temp_dir)
        vertices = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        
        plotter.add_polyhedron(vertices, faces, "Test", "test.gif")
        self.assertEqual(len(plotter.polyhedrons), 1)
        logger.info("✓ Polyhedron added successfully")
    
    def test_animation_error_handling(self):
        """Test error handling for missing imageio."""
        logger.info("Testing animation error handling...")
        from ivm_xyz.visualization import PolyhedronPlotter
        
        plotter = PolyhedronPlotter(output_folder=self.temp_dir)
        vertices = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        plotter.add_polyhedron(vertices, faces, "Test", "test.gif")
        
        # Try to animate - should raise ImportError if imageio not available
        try:
            plotter.animate_polyhedron(save=True)
            logger.info("✓ Animation attempted (imageio may be available)")
        except ImportError as e:
            logger.info(f"✓ Expected ImportError caught: {e}")
            self.assertIn("imageio", str(e))
    
    def test_multiple_polyhedra(self):
        """Test plotting multiple polyhedra."""
        logger.info("Testing multiple polyhedra...")
        from ivm_xyz.visualization import PolyhedronPlotter
        
        plotter = PolyhedronPlotter(output_folder=self.temp_dir)
        
        # Add multiple polyhedra
        tet_vertices = [(0, 0, 0), (1, 0, 0), (0.5, 0.866, 0), (0.5, 0.289, 0.816)]
        tet_faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        plotter.add_polyhedron(tet_vertices, tet_faces, "Tetrahedron", "tet.gif")
        
        cube_vertices = [
            (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
        ]
        cube_faces = [
            (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
            (2, 6, 7, 3), (0, 3, 7, 4), (1, 5, 6, 2)
        ]
        plotter.add_polyhedron(cube_vertices, cube_faces, "Cube", "cube.gif")
        
        self.assertEqual(len(plotter.polyhedrons), 2)
        logger.info("✓ Multiple polyhedra added successfully")


if __name__ == '__main__':
    unittest.main(verbosity=2)

