"""
Polyhedron definitions and geometric structures.
"""

from ivm_xyz.polyhedra.base import Polyhedron, Edge
from ivm_xyz.polyhedra.platonic import (
    Tetrahedron as PolyTetrahedron,
    Cube,
    Octahedron,
    Icosahedron,
    Cuboctahedron,
)
from ivm_xyz.polyhedra.edge_counting import (
    tet_edges,
    half_oct_edges,
    oct_edges,
    cubocta_edges,
    cubocta_layer,
)

__all__ = [
    "Polyhedron",
    "Edge",
    "PolyTetrahedron",
    "Cube",
    "Octahedron",
    "Icosahedron",
    "Cuboctahedron",
    "tet_edges",
    "half_oct_edges",
    "oct_edges",
    "cubocta_edges",
    "cubocta_layer",
]

# Note: PolyTetrahedron is renamed to avoid conflict with core.Tetrahedron

