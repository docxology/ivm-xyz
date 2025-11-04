"""
Vector classes for XYZ and IVM (Quadray) coordinate systems.

This module provides Vector (XYZ Cartesian) and Qvector (IVM Quadray) classes
for geometric calculations in both coordinate systems.
"""

from math import radians, degrees, cos, sin, acos
import math
from operator import add, sub, mul, neg
from collections import namedtuple

XYZ = namedtuple("xyz_vector", "x y z")
IVM = namedtuple("ivm_vector", "a b c d")

root2 = 2.0**0.5


class Vector:
    """
    Represents a 3D vector in XYZ (Cartesian) coordinate system.
    
    Attributes:
        xyz: Named tuple containing (x, y, z) coordinates
    """
    
    def __init__(self, arg):
        """Initialize a vector at an (x,y,z)"""
        self.xyz = XYZ(*map(float, arg))

    def __repr__(self):
        return repr(self.xyz)
    
    @property
    def x(self):
        return self.xyz.x

    @property
    def y(self):
        return self.xyz.y

    @property
    def z(self):
        return self.xyz.z
        
    def __mul__(self, scalar):
        """Return vector (self) * scalar."""
        newcoords = [scalar * dim for dim in self.xyz]
        return type(self)(newcoords)

    __rmul__ = __mul__  # allow scalar * vector

    def __truediv__(self, scalar):
        """Return vector (self) * 1/scalar"""        
        return self.__mul__(1.0/scalar)
    
    def __add__(self, v1):
        """Add a vector to this vector, return a vector""" 
        newcoords = map(add, v1.xyz, self.xyz)
        return type(self)(newcoords)
        
    def __sub__(self, v1):
        """Subtract vector from this vector, return a vector"""
        return self.__add__(-v1)
    
    def __neg__(self):      
        """Return a vector, the negative of this one."""
        return type(self)(tuple(map(neg, self.xyz)))

    def unit(self):
        """Return unit vector in same direction."""
        return self.__mul__(1.0/self.length())

    def dot(self, v1):
        """Return scalar dot product of this with another vector."""
        return sum(map(mul, v1.xyz, self.xyz))

    def cross(self, v1):
        """Return the vector cross product of this with another vector"""
        newcoords = (self.y * v1.z - self.z * v1.y, 
                     self.z * v1.x - self.x * v1.z,
                     self.x * v1.y - self.y * v1.x)
        return type(self)(newcoords)
    
    def length(self):
        """Return this vector's length"""
        return self.dot(self) ** 0.5

    def angle(self, v1):
        """Return angle between self and v1, in decimal degrees"""
        costheta = round(self.dot(v1)/(self.length() * v1.length()), 10)
        theta = degrees(acos(costheta))
        return round(theta, 10)

    def rotaxis(self, vAxis, deg):
        """
        Rotate around vAxis by deg degrees.
        Realign rotation axis with Z-axis, realign self accordingly,
        rotate by deg (counterclockwise) around Z, resume original
        orientation (undo realignment).
        """
        r, phi, theta = vAxis.spherical()
        newv = self.rotz(-theta).roty(phi)
        newv = newv.rotz(-deg)
        newv = newv.roty(-phi).rotz(theta)
        return type(self)(newv.xyz)        

    def rotx(self, deg):
        """Rotate around X-axis by deg degrees."""
        rad = radians(deg)
        newy = cos(rad) * self.y - sin(rad) * self.z
        newz = sin(rad) * self.y + cos(rad) * self.z
        newxyz = [round(p, 8) for p in (self.x, newy, newz)]
        return type(self)(newxyz)
   
    def roty(self, deg):
        """Rotate around Y-axis by deg degrees."""
        rad = radians(deg)
        newx = cos(rad) * self.x - sin(rad) * self.z
        newz = sin(rad) * self.x + cos(rad) * self.z
        newxyz = [round(p, 8) for p in (newx, self.y, newz)]
        return type(self)(newxyz)

    def rotz(self, deg):
        """Rotate around Z-axis by deg degrees."""
        rad = radians(deg)
        newx = cos(rad) * self.x - sin(rad) * self.y
        newy = sin(rad) * self.x + cos(rad) * self.y
        newxyz = [round(p, 8) for p in (newx, newy, self.z)]
        return type(self)(newxyz)
    
    def spherical(self):
        """
        Return (r, phi, theta) spherical coordinates based 
        on current (x, y, z).
        
        Returns:
            tuple: (r, phi, theta) where r is radius, phi and theta are angles in degrees
        """
        r = self.length()

        if self.x == 0:
            if self.y == 0:
                theta = 0.0
            elif self.y < 0:
                theta = -90.0
            else:
                theta = 90.0
        else:  
            theta = degrees(math.atan(self.y/self.x))
            if self.x < 0 and self.y == 0:
                theta = 180
            elif self.x < 0 and self.y < 0:
                theta = 180 - theta
            elif self.x < 0 and self.y > 0:
                theta = -(180 + theta)

        if r == 0: 
            phi = 0.0
        else: 
            phi = degrees(acos(self.z/r))
        
        return (r, phi, theta)

    def quadray(self):
        """
        Return (a, b, c, d) quadray coordinates based on current (x, y, z).
        
        Returns:
            Qvector: Quadray representation of this vector
        """
        x, y, z = self.xyz
        k = 2/root2
        a = k * ((x >= 0) * (x) + (y >= 0) * (y) + (z >= 0) * (z))
        b = k * ((x < 0) * (-x) + (y < 0) * (-y) + (z >= 0) * (z))
        c = k * ((x < 0) * (-x) + (y >= 0) * (y) + (z < 0) * (-z))
        d = k * ((x >= 0) * (x) + (y < 0) * (-y) + (z < 0) * (-z))
        return Qvector((a, b, c, d))

        
class Qvector:
    """
    Represents a vector in IVM (Quadray) coordinate system.
    
    Quadray coordinates use 4 components (a, b, c, d) normalized such
    that all components are non-negative.
    
    Attributes:
        coords: Named tuple containing (a, b, c, d) coordinates
    """
    
    def __init__(self, arg):
        """Initialize a quadray vector from (a, b, c, d) tuple."""
        self.coords = self.norm(arg)

    def __repr__(self):
        return repr(self.coords)

    def norm(self, arg):
        """Normalize such that 4-tuple all non-negative members."""
        return IVM(*tuple(map(sub, arg, [min(arg)] * 4))) 
    
    def norm0(self):
        """Normalize such that sum of 4-tuple members = 0"""
        q = self.coords
        return IVM(*tuple(map(sub, q, [sum(q)/4.0] * 4))) 

    @property
    def a(self):
        return self.coords.a

    @property
    def b(self):
        return self.coords.b

    @property
    def c(self):
        return self.coords.c

    @property
    def d(self):
        return self.coords.d
    
    def __eq__(self, other):
        return self.coords == other.coords
        
    def __lt__(self, other):
        return self.coords < other.coords

    def __gt__(self, other):
        return self.coords > other.coords
    
    def __hash__(self):
        return hash(self.coords)
    
    def __mul__(self, scalar):
        """Return vector (self) * scalar."""
        newcoords = [scalar * dim for dim in self.coords]
        return Qvector(newcoords)

    __rmul__ = __mul__  # allow scalar * vector

    def __truediv__(self, scalar):
        """Return vector (self) * 1/scalar"""        
        return self.__mul__(1.0/scalar)
    
    def __add__(self, v1):
        """Add a vector to this vector, return a vector""" 
        newcoords = tuple(map(add, v1.coords, self.coords))
        return Qvector(newcoords)
        
    def __sub__(self, v1):
        """Subtract vector from this vector, return a vector"""
        return self.__add__(-v1)
    
    def __neg__(self):      
        """Return a vector, the negative of this one."""
        return Qvector(tuple(map(neg, self.coords)))
                  
    def dot(self, v1):
        """
        Return the dot product of self with another vector.
        
        Returns:
            float: Scalar dot product
        """
        return 0.5 * sum(map(mul, self.norm0(), v1.norm0()))

    def length(self):
        """Return this vector's length"""
        return self.dot(self) ** 0.5
        
    def cross(self, v1):
        """
        Return the cross product of self with another vector.
        
        Returns:
            Qvector: Cross product vector
        """
        A = Qvector((1, 0, 0, 0))
        B = Qvector((0, 1, 0, 0))
        C = Qvector((0, 0, 1, 0))
        D = Qvector((0, 0, 0, 1))
        a1, b1, c1, d1 = v1.coords
        a2, b2, c2, d2 = self.coords
        k = (2.0**0.5)/4.0
        sum_result = (A*c1*d2 - A*d1*c2 - A*b1*d2 + A*b1*c2
                      + A*b2*d1 - A*b2*c1 - B*c1*d2 + B*d1*c2 
                      + b1*C*d2 - b1*D*c2 - b2*C*d1 + b2*D*c1 
                      + a1*B*d2 - a1*B*c2 - a1*C*d2 + a1*D*c2
                      + a1*b2*C - a1*b2*D - a2*B*d1 + a2*B*c1 
                      + a2*C*d1 - a2*D*c1 - a2*b1*C + a2*b1*D)
        return k * sum_result

    def angle(self, v1):
        """Return angle between self and v1 in degrees."""
        return self.xyz().angle(v1.xyz())
        
    def xyz(self):
        """
        Convert quadray coordinates to XYZ (Cartesian) coordinates.
        
        Returns:
            Vector: XYZ representation of this quadray vector
        """
        a, b, c, d = self.coords
        k = 0.5/root2
        xyz = (k * (a - b - c + d),
               k * (a - b + c - d),
               k * (a + b - c - d))
        return Vector(xyz)


class Svector(Vector):
    """Subclass of Vector that takes spherical coordinate arguments."""
    
    def __init__(self, arg):
        # if returning from Vector calc method, spherical is true
        arg = Vector(arg).spherical()
            
        # initialize a vector at an (r, phi, theta) tuple (= arg)
        r = arg[0]
        phi = radians(arg[1])
        theta = radians(arg[2])
        coords = tuple(map(lambda x: round(x, 15),
                      (r * cos(theta) * sin(phi),
                       r * sin(theta) * sin(phi),
                       r * cos(phi))))
        self.xyz = XYZ(*coords)

    def __repr__(self):
        return "Svector " + str(self.spherical())


# Module-level convenience functions
def dot(a, b):
    """Return dot product of two vectors."""
    return a.dot(b)

def cross(a, b):
    """Return cross product of two vectors."""
    return a.cross(b)

def angle(a, b):
    """Return angle between two vectors in degrees."""
    return a.angle(b)

def length(a):
    """Return length of a vector."""
    return a.length()

