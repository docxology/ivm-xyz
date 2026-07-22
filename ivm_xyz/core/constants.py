"""
Mathematical constants used throughout the IVM-XYZ package.
"""

from math import sqrt

# Volume calculation constants
S3: float = sqrt(9 / 8)  # Conversion factor between IVM and XYZ volumes

# Square roots
ROOT2: float = sqrt(2)
ROOT3: float = sqrt(3)
ROOT5: float = sqrt(5)

# Golden ratio
PHI: float = (1 + ROOT5) / 2.0

# Geometric constants
R: float = 0.5  # Radius
D: float = 1.0  # Diameter

__all__ = [
    "S3",
    "ROOT2",
    "ROOT3",
    "ROOT5",
    "PHI",
    "R",
    "D",
]
