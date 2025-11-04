"""
Platonic solids and geometric structures defined using IVM coordinates.

These classes provide canonical definitions of polyhedra following
R. Buckminster Fuller's Concentric Hierarchy.
"""

import math
from ivm_xyz.polyhedra.base import Polyhedron
from ivm_xyz.core.vectors import Qvector, Vector
from ivm_xyz.core.constants import PHI

ORIGIN = Qvector((0, 0, 0, 0))
A = Qvector((1, 0, 0, 0))
B = Qvector((0, 1, 0, 0))
C = Qvector((0, 0, 1, 0))
D = Qvector((0, 0, 0, 1))

E, F, G, H = B + C + D, A + C + D, A + B + D, A + B + C
I, J, K, L, M, N = A + B, A + C, A + D, B + C, B + D, C + D
O, P, Q, R, S, T = I + J, I + K, I + L, I + M, N + J, N + K
U, V, W, X, Y, Z = N + L, N + M, J + L, L + M, M + K, K + J

# Icosahedron vertex calculations
control = (Z - T).length()
midface = (Z + Y)
gold = 0.5 * PHI * midface / midface.length()
Zi = gold + J / J.length() * control / 2
Yi = gold + M / M.length() * control / 2

midface = (W + X)
gold = 0.5 * PHI * midface / midface.length()
Wi = gold + J / J.length() * control / 2
Xi = gold + M / M.length() * control / 2

midface = (R + V)
gold = 0.5 * PHI * midface / midface.length()
Ri = gold + I / I.length() * control / 2
Vi = gold + N / N.length() * control / 2

midface = (O + S)
gold = 0.5 * PHI * midface / midface.length()
Oi = gold + I / I.length() * control / 2
Si = gold + N / N.length() * control / 2

midface = (T + U)
gold = 0.5 * PHI * midface / midface.length()
Ti = gold + K / K.length() * control / 2
Ui = gold + L / L.length() * control / 2

midface = (P + Q)
gold = 0.5 * PHI * midface / midface.length()
Pi = gold + K / K.length() * control / 2
Qi = gold + L / L.length() * control / 2


class Tetrahedron(Polyhedron):
    """
    Regular Tetrahedron.
    
    Volume: 1 (per Concentric Hierarchy)
    """
    
    def __init__(self):
        verts = dict(
            a=Qvector((1, 0, 0, 0)),  # A
            b=Qvector((0, 1, 0, 0)),  # B
            c=Qvector((0, 0, 1, 0)),  # C
            d=Qvector((0, 0, 0, 1))   # D
        )
        
        self.name = "Tetrahedron"
        self.volume = 1
        self.center = ORIGIN
        self.vertexes = verts
        self.faces = (
            ('a', 'b', 'c'),
            ('a', 'c', 'd'),
            ('a', 'd', 'b'),
            ('b', 'd', 'c')
        )
        self.edges = self._distill()


class Cube(Polyhedron):
    """
    Cube.
    
    Volume: 3 (per Concentric Hierarchy)
    """
    
    def __init__(self):
        verts = {
            'a': A, 'b': B, 'c': C, 'd': D,
            'e': E, 'f': F, 'g': G, 'h': H
        }
        
        self.name = "Cube"
        self.volume = 3
        self.center = ORIGIN
        self.vertexes = verts
        self.faces = (
            ('a', 'f', 'c', 'h'),
            ('h', 'c', 'e', 'b'),
            ('b', 'e', 'd', 'g'),
            ('g', 'd', 'f', 'a'),
            ('c', 'f', 'd', 'e'),
            ('a', 'h', 'b', 'g')
        )
        self.edges = self._distill()


class Octahedron(Polyhedron):
    """
    Regular Octahedron.
    
    Volume: 4 (per Concentric Hierarchy)
    """
    
    def __init__(self):
        verts = {
            'i': I, 'j': J, 'k': K, 'l': L,
            'm': M, 'n': N
        }
        
        self.name = "Octahedron"
        self.volume = 4
        self.center = ORIGIN
        self.vertexes = verts
        self.faces = (
            ('j', 'k', 'i'),
            ('j', 'i', 'l'),
            ('j', 'l', 'n'),
            ('j', 'n', 'k'),
            ('m', 'k', 'i'),
            ('m', 'i', 'l'),
            ('m', 'l', 'n'),
            ('m', 'n', 'k')
        )
        self.edges = self._distill()


class Icosahedron(Polyhedron):
    """
    Regular Icosahedron.
    
    Volume: ~18.51 (per Concentric Hierarchy)
    """
    
    def __init__(self):
        self.vertexes = dict(
            o=Oi, p=Pi, q=Qi, r=Ri,
            s=Si, t=Ti, u=Ui, v=Vi,
            w=Wi, x=Xi, y=Yi, z=Zi
        )
        
        self.name = "Icosahedron"
        self.volume = 18.51
        self.center = ORIGIN
        self.faces = (
            ('o', 'w', 's'), ('o', 'z', 's'),
            ('z', 'p', 'y'), ('z', 't', 'y'),
            ('t', 'v', 'u'), ('t', 's', 'u'),
            ('w', 'q', 'x'), ('w', 'u', 'x'),
            ('p', 'o', 'q'), ('p', 'r', 'q'),
            ('r', 'y', 'v'), ('r', 'x', 'v'),
            ('z', 's', 't'), ('t', 'y', 'v'),
            ('y', 'p', 'r'), ('r', 'q', 'x'),
            ('x', 'u', 'v'), ('u', 's', 'w'),
            ('w', 'q', 'o'), ('o', 'z', 'p')
        )
        self.edges = self._distill()


class Cuboctahedron(Polyhedron):
    """
    Cuboctahedron.
    
    Volume: 20 (per Concentric Hierarchy)
    """
    
    def __init__(self):
        self.vertexes = dict(
            o=O, p=P, q=Q, r=R,
            s=S, t=T, u=U, v=V,
            w=W, x=X, y=Y, z=Z
        )
        
        self.name = "Cuboctahedron"
        self.volume = 20
        self.center = ORIGIN
        self.faces = (
            ('o', 'w', 's', 'z'),
            ('z', 'p', 'y', 't'),
            ('t', 'v', 'u', 's'),
            ('w', 'q', 'x', 'u'),
            ('o', 'p', 'r', 'q'),
            ('r', 'y', 'v', 'x'),
            ('z', 's', 't'),
            ('t', 'y', 'v'),
            ('y', 'p', 'r'),
            ('r', 'q', 'x'),
            ('x', 'u', 'v'),
            ('u', 's', 'w'),
            ('w', 'q', 'o'),
            ('o', 'z', 'p')
        )
        self.edges = self._distill()

