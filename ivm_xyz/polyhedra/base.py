"""
Base Polyhedron class and Edge class for geometric structures.

This module provides the foundation for defining polyhedra with vertices,
faces, and edges.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Tuple

if TYPE_CHECKING:
    from ivm_xyz.core.vectors import Qvector


class Polyhedron:
    """
    Base class for polyhedra. Designed to be subclassed, not used directly.

    Provides methods for scaling, translating, and extracting edges from faces.

    Subclasses are expected to populate the following attributes in ``__init__``:
    ``name``, ``volume``, ``center``, ``vertexes``, ``faces`` and ``edges``.
    """

    name: str
    volume: float
    center: "Qvector"
    vertexes: Dict[str, "Qvector"]
    faces: Tuple[Tuple[str, ...], ...]
    edges: List["Edge"]

    def scale(self, scalefactor: float) -> "Polyhedron":
        """
        Scale the polyhedron by a factor.

        Args:
            scalefactor: Scaling factor

        Returns:
            New instance of the same polyhedron type, scaled
        """
        newverts = {}
        for v in self.vertexes:
            newverts[v] = self.vertexes[v] * scalefactor
        newme = type(self)()
        newme.vertexes = newverts
        if hasattr(self, "volume"):
            newme.volume = self.volume * (scalefactor**3)
        if hasattr(self, "center"):
            newme.center = self.center
        if hasattr(self, "name"):
            newme.name = self.name
        newme.edges = newme._distill()
        return newme

    __mul__ = __rmul__ = scale

    def translate(self, vector: "Qvector") -> "Polyhedron":
        """
        Translate the polyhedron by a vector.

        Args:
            vector: Translation vector

        Returns:
            New instance of the same polyhedron type, translated
        """
        newverts = {}
        for v in self.vertexes:
            newverts[v] = self.vertexes[v] + vector
        newme = type(self)()
        newme.vertexes = newverts
        if hasattr(self, "center"):
            newme.center = self.center + vector
        newme.edges = newme._distill()
        return newme

    __add__ = __radd__ = translate

    def _distill(self) -> List["Edge"]:
        """
        Extract unique edges from faces.

        Returns:
            list: List of Edge objects
        """
        edges = []
        unique = set()

        for f in self.faces:
            for pair in zip(f, f[1:] + (f[0],)):
                unique.add(tuple(sorted(pair)))

        for edge in unique:
            edges.append(Edge(self.vertexes[edge[0]], self.vertexes[edge[1]]))

        return edges


class Edge:
    """
    Represents an edge connecting two vertices.

    Attributes:
        v0: First vertex (Vector or Qvector)
        v1: Second vertex (Vector or Qvector)
    """

    def __init__(self, v0: "Qvector", v1: "Qvector") -> None:
        """
        Initialize edge with two vertices.

        Args:
            v0: First vertex
            v1: Second vertex
        """
        self.v0 = v0
        self.v1 = v1

    def __repr__(self) -> str:
        return "Edge from %s to %s" % (self.v0, self.v1)
