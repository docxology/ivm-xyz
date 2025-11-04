"""
Tetrahedron class for calculating volumes in IVM and XYZ coordinate systems.

Based on Euler volume formula, modified by Gerald de Jong.
See: http://www.grunch.net/synergetics/quadvols.html
"""

from math import sqrt
from ivm_xyz.core.constants import S3


class Tetrahedron:
    """
    Represents a tetrahedron, facilitating the calculation of volumes 
    in both IVM and XYZ coordinate systems.
    
    Takes six edges of tetrahedron with faces:
    - (a,b,d) - first face
    - (b,c,e) - second face  
    - (c,a,f) - third face
    - (d,e,f) - opposite face
    
    Attributes:
        a, b, c, d, e, f: Edge lengths of the tetrahedron
        a2, b2, c2, d2, e2, f2: Squared edge lengths
    """
    
    def __init__(self, a, b, c, d, e, f):
        """
        Initialize tetrahedron with six edge lengths.
        
        Args:
            a, b, c: Three edges from one vertex
            d, e, f: Remaining three edges (opposite face)
        """
        self.a, self.a2 = a, a**2
        self.b, self.b2 = b, b**2
        self.c, self.c2 = c, c**2
        self.d, self.d2 = d, d**2
        self.e, self.e2 = e, e**2
        self.f, self.f2 = f, f**2

    def ivm_volume(self):
        """
        Calculate volume using the IVM system.
        
        Uses Euler's formula for tetrahedron volume calculation.
        
        Returns:
            float: Volume in IVM units
        """
        ivmvol = ((self._addopen() 
                   - self._addclosed() 
                   - self._addopposite()) / 2) ** 0.5
        return ivmvol

    def xyz_volume(self):
        """
        Calculate volume using the XYZ system.
        
        Returns:
            float: Volume in XYZ units (converted from IVM)
        """
        xyzvol = self.ivm_volume() / S3
        return xyzvol

    def _addopen(self):
        """
        Calculate the sum of open products for volume calculation.
        
        This represents the sum of products of three edges that don't
        form a closed triangle.
        
        Returns:
            float: Sum of open products
        """
        a2, b2, c2, d2, e2, f2 = self.a2, self.b2, self.c2, self.d2, self.e2, self.f2
        sumval = f2 * a2 * b2
        sumval += d2 * a2 * c2
        sumval += a2 * b2 * e2
        sumval += c2 * b2 * d2
        sumval += e2 * c2 * a2
        sumval += f2 * c2 * b2
        sumval += e2 * d2 * a2
        sumval += b2 * d2 * f2
        sumval += b2 * e2 * f2
        sumval += d2 * e2 * c2
        sumval += a2 * f2 * e2
        sumval += d2 * f2 * c2
        return sumval

    def _addclosed(self):
        """
        Calculate the sum of closed products for volume calculation.
        
        This represents the sum of products of three edges that form
        a closed triangle (face).
        
        Returns:
            float: Sum of closed products
        """
        a2, b2, c2, d2, e2, f2 = self.a2, self.b2, self.c2, self.d2, self.e2, self.f2
        sumval = a2 * b2 * d2
        sumval += d2 * e2 * f2
        sumval += b2 * c2 * e2
        sumval += a2 * c2 * f2
        return sumval

    def _addopposite(self):
        """
        Calculate the sum of opposite products for volume calculation.
        
        This represents the sum of products of opposite edge pairs.
        
        Returns:
            float: Sum of opposite products
        """
        a2, b2, c2, d2, e2, f2 = self.a2, self.b2, self.c2, self.d2, self.e2, self.f2
        sumval = a2 * e2 * (a2 + e2)
        sumval += b2 * f2 * (b2 + f2)
        sumval += c2 * d2 * (c2 + d2)
        return sumval


def make_tet(v0, v1, v2):
    """
    Generate a tetrahedron from three vectors and calculate its volumes.
    
    The three vectors define three edges from one vertex. The remaining
    three edges are computed from the vector differences.
    
    Args:
        v0: First vector (must have length() method)
        v1: Second vector (must have length() method)
        v2: Third vector (must have length() method)
    
    Returns:
        tuple: (ivm_volume, xyz_volume)
    """
    tet = Tetrahedron(v0.length(), v1.length(), v2.length(), 
                      (v0 - v1).length(), (v1 - v2).length(), (v2 - v0).length())
    return tet.ivm_volume(), tet.xyz_volume()

