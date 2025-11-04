"""
Tests for polyhedra classes.
"""

import unittest
from ivm_xyz.polyhedra.base import Polyhedron, Edge
from ivm_xyz.polyhedra.platonic import Tetrahedron, Cube, Octahedron, Icosahedron, Cuboctahedron
from ivm_xyz.polyhedra.edge_counting import (
    tet_edges, half_oct_edges, oct_edges, cubocta_edges, cubocta_layer
)


class TestPolyhedron(unittest.TestCase):
    """Test cases for base Polyhedron class."""
    
    def test_tetrahedron_creation(self):
        """Test tetrahedron polyhedron creation."""
        tet = Tetrahedron()
        self.assertEqual(tet.name, "Tetrahedron")
        self.assertEqual(tet.volume, 1)
        self.assertEqual(len(tet.vertexes), 4)
        self.assertEqual(len(tet.faces), 4)
    
    def test_cube_creation(self):
        """Test cube polyhedron creation."""
        cube = Cube()
        self.assertEqual(cube.name, "Cube")
        self.assertEqual(cube.volume, 3)
        self.assertEqual(len(cube.vertexes), 8)
        self.assertEqual(len(cube.faces), 6)
    
    def test_octahedron_creation(self):
        """Test octahedron polyhedron creation."""
        octa = Octahedron()
        self.assertEqual(octa.name, "Octahedron")
        self.assertEqual(octa.volume, 4)
        self.assertEqual(len(octa.vertexes), 6)
        self.assertEqual(len(octa.faces), 8)
    
    def test_icosahedron_creation(self):
        """Test icosahedron polyhedron creation."""
        ico = Icosahedron()
        self.assertEqual(ico.name, "Icosahedron")
        self.assertAlmostEqual(ico.volume, 18.51, places=2)
        self.assertEqual(len(ico.vertexes), 12)
        self.assertEqual(len(ico.faces), 20)
    
    def test_cuboctahedron_creation(self):
        """Test cuboctahedron polyhedron creation."""
        cubocta = Cuboctahedron()
        self.assertEqual(cubocta.name, "Cuboctahedron")
        self.assertEqual(cubocta.volume, 20)
        self.assertEqual(len(cubocta.vertexes), 12)
    
    def test_polyhedron_scaling(self):
        """Test polyhedron scaling."""
        tet = Tetrahedron()
        scaled = tet.scale(2.0)
        self.assertIsInstance(scaled, Tetrahedron)
        self.assertEqual(scaled.volume, 8.0)  # 2^3 = 8
    
    def test_polyhedron_translation(self):
        """Test polyhedron translation."""
        tet = Tetrahedron()
        from ivm_xyz.core.vectors import Qvector
        translation = Qvector((1, 0, 0, 0))
        translated = tet.translate(translation)
        self.assertIsInstance(translated, Tetrahedron)


class TestEdgeCounting(unittest.TestCase):
    """Test cases for edge counting functions."""
    
    def test_tet_edges(self):
        """Test tetrahedron edge counting."""
        self.assertEqual(tet_edges(1), 6)
        self.assertEqual(tet_edges(2), 24)
        self.assertEqual(tet_edges(3), 60)
    
    def test_half_oct_edges(self):
        """Test half octahedron edge counting."""
        self.assertEqual(half_oct_edges(1), 8)
        self.assertGreater(half_oct_edges(2), 8)
    
    def test_oct_edges(self):
        """Test octahedron edge counting."""
        edges_1 = oct_edges(1)
        self.assertGreater(edges_1, 0)
        edges_2 = oct_edges(2)
        self.assertGreater(edges_2, edges_1)
    
    def test_cubocta_edges(self):
        """Test cuboctahedron edge counting."""
        edges_1 = cubocta_edges(1)
        self.assertGreater(edges_1, 0)
        edges_2 = cubocta_edges(2)
        self.assertGreater(edges_2, edges_1)
    
    def test_cubocta_layer(self):
        """Test cuboctahedron layer edge counting."""
        layer_1 = cubocta_layer(1)
        self.assertGreater(layer_1, 0)
        layer_2 = cubocta_layer(2)
        self.assertGreater(layer_2, layer_1)


if __name__ == '__main__':
    unittest.main()

