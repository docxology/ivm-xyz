"""
Triangle class for calculating areas in IVM and XYZ coordinate systems.
"""

from __future__ import annotations

from math import sqrt
from typing import TYPE_CHECKING, Tuple

from ivm_xyz.core.constants import S3

if TYPE_CHECKING:
    from ivm_xyz.core.vectors import Vector


class Triangle:
    """
    Represents a triangle, facilitating the calculation of areas
    in both IVM and XYZ coordinate systems.

    Assumes an equilateral triangle for simplification.

    Attributes:
        a, b, c: Edge lengths of the triangle
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initialize triangle with three edge lengths.

        Args:
            a: First edge length
            b: Second edge length
            c: Third edge length
        """
        self.a = a
        self.b = b
        self.c = c

    def ivm_area(self) -> float:
        """
        Calculate area using the IVM system.

        Uses Heron's formula for area calculation.

        Returns:
            float: Area in IVM units
        """
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def xyz_area(self) -> float:
        """
        Calculate area using the XYZ system.

        Returns:
            float: Area in XYZ units (converted from IVM)
        """
        return self.ivm_area() / S3


def make_tri(v0: Vector, v1: Vector) -> Tuple[float, float]:
    """
    Generate a triangle from two vectors and calculate its areas.

    Args:
        v0: First vector (must have length() method)
        v1: Second vector (must have length() method)

    Returns:
        tuple: (ivm_area, xyz_area)
    """
    tri = Triangle(v0.length(), v1.length(), (v1 - v0).length())
    return tri.ivm_area(), tri.xyz_area()
