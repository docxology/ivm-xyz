"""
Base Polyhedron class and Edge class for geometric structures.

This module provides the foundation for defining polyhedra with vertices,
faces, and edges.
"""

from ivm_xyz.core.vectors import Vector, Qvector


class Polyhedron:
    """
    Base class for polyhedra. Designed to be subclassed, not used directly.
    
    Provides methods for scaling, translating, and extracting edges from faces.
    """
    
    def scale(self, scalefactor):
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
            newme.volume = self.volume * (scalefactor ** 3)
        if hasattr(self, "center"):
            newme.center = self.center
        if hasattr(self, "name"):
            newme.name = self.name
        newme.edges = newme._distill()
        return newme

    __mul__ = __rmul__ = scale

    def translate(self, vector):
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
        if hasattr(self, "suppress"):
            newme.suppress = self.suppress
            if newme.suppress:
                newme.faces = newme._suppress()
        newme.edges = newme._distill()
        return newme

    __add__ = __radd__ = translate
    
    def _distill(self):
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
            edges.append(Edge(self.vertexes[edge[0]],
                             self.vertexes[edge[1]]))
        
        return edges


class Edge:
    """
    Represents an edge connecting two vertices.
    
    Attributes:
        v0: First vertex (Vector or Qvector)
        v1: Second vertex (Vector or Qvector)
    """
    
    def __init__(self, v0, v1):
        """
        Initialize edge with two vertices.
        
        Args:
            v0: First vertex
            v1: Second vertex
        """
        self.v0 = v0
        self.v1 = v1
             
    def __repr__(self):
        return 'Edge from %s to %s' % (self.v0, self.v1)

