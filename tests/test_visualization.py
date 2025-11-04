"""
Tests for visualization module.
"""

import unittest
import os
import tempfile
import shutil
from ivm_xyz.visualization.plotter import PolyhedronPlotter


class TestPolyhedronPlotter(unittest.TestCase):
    """Test cases for PolyhedronPlotter class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.plotter = PolyhedronPlotter(output_folder=self.temp_dir)
    
    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_plotter_initialization(self):
        """Test plotter initialization."""
        self.assertEqual(self.plotter.output_folder, self.temp_dir)
        self.assertEqual(len(self.plotter.polyhedrons), 0)
        self.assertTrue(os.path.exists(self.temp_dir))
    
    def test_add_polyhedron(self):
        """Test adding polyhedron to plotter."""
        vertices = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        
        self.plotter.add_polyhedron(vertices, faces, "Test Tetrahedron", "test.png")
        self.assertEqual(len(self.plotter.polyhedrons), 1)
        self.assertEqual(self.plotter.polyhedrons[0]["title"], "Test Tetrahedron")
    
    def test_plot_polyhedron(self):
        """Test plotting a polyhedron."""
        vertices = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        
        # Should not raise an exception
        self.plotter.plot_polyhedron(
            vertices, faces, "Test", save=True, file_name="test_plot.png"
        )
        
        # Check file was created
        file_path = os.path.join(self.temp_dir, "test_plot.png")
        self.assertTrue(os.path.exists(file_path))


if __name__ == '__main__':
    unittest.main()

