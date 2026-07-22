"""
Coordinate conversion functions between XYZ (Cartesian) and IVM (Quadray) systems.

These functions provide direct conversion between 3D Cartesian coordinates
and 4D Quadray (IVM) coordinates without requiring Vector/Qvector objects.
"""

from __future__ import annotations

from math import sqrt
from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from ivm_xyz.core.vectors import Qvector, Vector

root2 = sqrt(2.0)


def xyz_to_ivm(x: float, y: float, z: float) -> Tuple[float, float, float, float]:
    """
    Convert XYZ 3D geometric coordinates to IVM 4D tetrahedral coordinates (quadray).

    Args:
        x (float): X coordinate
        y (float): Y coordinate
        z (float): Z coordinate

    Returns:
        tuple: A tuple of IVM (quadray) coordinates (a, b, c, d)
    """
    k = 2 / root2
    a = k * ((x >= 0) * (x) + (y >= 0) * (y) + (z >= 0) * (z))
    b = k * ((x < 0) * (-x) + (y < 0) * (-y) + (z >= 0) * (z))
    c = k * ((x < 0) * (-x) + (y >= 0) * (y) + (z < 0) * (-z))
    d = k * ((x >= 0) * (x) + (y < 0) * (-y) + (z < 0) * (-z))

    # Normalize to ensure all non-negative (as per Qvector normalization)
    min_val = min(a, b, c, d)
    return (a - min_val, b - min_val, c - min_val, d - min_val)


def ivm_to_xyz(a: float, b: float, c: float, d: float) -> Tuple[float, float, float]:
    """
    Convert IVM 4D tetrahedral (quadray) coordinates back to XYZ 3D geometric coordinates.

    Args:
        a, b, c, d (float): IVM (quadray) coordinates

    Returns:
        tuple: A tuple of XYZ coordinates (x, y, z)
    """
    k = 0.5 / root2
    x = k * (a - b - c + d)
    y = k * (a - b + c - d)
    z = k * (a + b - c - d)

    return (x, y, z)


def vector_to_qvector(vector: Vector) -> Qvector:
    """
    Convert a Vector object to a Qvector object.

    Args:
        vector: Vector object (XYZ coordinates)

    Returns:
        Qvector: Quadray representation of the vector
    """
    return vector.quadray()


def qvector_to_vector(qvector: Qvector) -> Vector:
    """
    Convert a Qvector object to a Vector object.

    Args:
        qvector: Qvector object (IVM coordinates)

    Returns:
        Vector: XYZ representation of the quadray vector
    """
    return qvector.xyz()
