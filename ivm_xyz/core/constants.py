"""
Mathematical constants used throughout the IVM-XYZ package.
"""

from math import sqrt

# Volume calculation constants
S3 = sqrt(9/8)  # Conversion factor between IVM and XYZ volumes

# Square roots
ROOT2 = sqrt(2)
ROOT3 = sqrt(3)
ROOT5 = sqrt(5)

# Golden ratio
PHI = (1 + ROOT5) / 2.0

# Geometric constants
R = 0.5  # Radius
D = 1.0  # Diameter

__all__ = [
    "S3",
    "ROOT2",
    "ROOT3",
    "ROOT5",
    "PHI",
    "R",
    "D",
]

