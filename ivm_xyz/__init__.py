"""
IVM-XYZ: A Python package for computational geometry with IVM and XYZ coordinate systems.

This package provides tools for:
- Converting between XYZ (Cartesian) and IVM (Isotropic Vector Matrix) coordinate systems
- Calculating volumes and areas of tetrahedra and triangles
- Working with polyhedra and geometric transformations
- Visualizing geometric structures
"""

__version__ = "0.1.0"

from ivm_xyz.core.vectors import Vector, Qvector
from ivm_xyz.core.tetrahedron import Tetrahedron, make_tet
from ivm_xyz.core.triangle import Triangle, make_tri
from ivm_xyz.conversion.converters import xyz_to_ivm, ivm_to_xyz

__all__ = [
    "Vector",
    "Qvector",
    "Tetrahedron",
    "make_tet",
    "Triangle",
    "make_tri",
    "xyz_to_ivm",
    "ivm_to_xyz",
    "__version__",
]

