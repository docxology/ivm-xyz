"""
Tests for visualization module.
"""

import unittest
import os
import tempfile
import shutil

from tests._support.optional_deps import HAS_MATPLOTLIB
from tests._support.fixtures import SIMPLE_TET_VERTICES, SIMPLE_TET_FACES


@unittest.skipUnless(HAS_MATPLOTLIB, "matplotlib required for visualization tests")
class TestPolyhedronPlotter(unittest.TestCase):
    """Test cases for PolyhedronPlotter class."""

    def setUp(self):
        """Set up test fixtures."""
        from ivm_xyz.visualization.plotter import PolyhedronPlotter

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
        self.plotter.add_polyhedron(
            SIMPLE_TET_VERTICES, SIMPLE_TET_FACES, "Test Tetrahedron", "test.png"
        )
        self.assertEqual(len(self.plotter.polyhedrons), 1)
        self.assertEqual(self.plotter.polyhedrons[0]["title"], "Test Tetrahedron")

    def test_plot_polyhedron(self):
        """Test plotting a polyhedron."""
        self.plotter.plot_polyhedron(
            SIMPLE_TET_VERTICES, SIMPLE_TET_FACES, "Test", save=True, file_name="test_plot.png"
        )
        file_path = os.path.join(self.temp_dir, "test_plot.png")
        self.assertTrue(os.path.exists(file_path))


if __name__ == "__main__":
    unittest.main()
