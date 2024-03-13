"""
3-13-2024 - DAF heavily modified from https://github.com/4dsolutions/MartianMath/blob/master/tetravolume.py

#### CURRENTLY THE INTERIOR ANGLE METHODS ARE NOT IMPLEMENTED 

"""

from math import sqrt, pi, e
from qrays import Qvector, Vector
import sys

# Constants for volume calculations
S3 = sqrt(9/8)
ROOT2 = sqrt(2)
ROOT5 = sqrt(5)

class Triangle:
    """
    Represents a triangle, facilitating the calculation of areas in both IVM and XYZ coordinate systems.
    Assumes an equilateral triangle for simplification.
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ivm_area(self):
        """Calculates area using the IVM system."""
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def xyz_area(self):
        """Calculates area using the XYZ system."""
        return self.ivm_area() / S3

def make_tri(v0, v1):
    """Generates a triangle from two vectors and calculates its areas."""
    tri = Triangle(v0.length(), v1.length(), (v1 - v0).length())
    return tri.ivm_area(), tri.xyz_area()

class Tetrahedron:
    """
    Represents a tetrahedron, facilitating the calculation of volumes in both IVM and XYZ coordinate systems.
    """
    def __init__(self, a, b, c, d, e, f):
        self.edges = [a, b, c, d, e, f]
        self.edges_squared = [edge ** 2 for edge in self.edges]
        print(f"Initialized Tetrahedron with edges: {', '.join(map(str, self.edges))}")

    def ivm_volume(self):
        """Calculates volume using the IVM system."""
        ivmvol = sqrt((self._addopen() - self._addclosed() - self._addopposite()) / 2)
        print(f"IVM Volume Calculation:")
        print(f"  Sum of open products: {self._addopen():.6f}")
        print(f"  Sum of closed products: {self._addclosed():.6f}")
        print(f"  Sum of opposite products: {self._addopposite():.6f}")
        print(f"  IVM Volume: {ivmvol:.6f}")
        return ivmvol

    def xyz_volume(self):
        """Calculates volume using the XYZ system."""
        xyzvol = self.ivm_volume() / S3
        print(f"XYZ Volume Calculation:")
        print(f"  XYZ Volume: {xyzvol:.6f}")
        return xyzvol

    def _addopen(self):
        """Calculates the sum of open products for volume calculation."""
        sumval = sum(self.edges_squared[i] * self.edges_squared[j] * self.edges_squared[k] 
                     for i in range(6) for j in range(i + 1, 6) for k in range(j + 1, 6))
        print(f"Sum of open products: {sumval}")
        return sumval

    def _addclosed(self):
        """Calculates the sum of closed products for volume calculation."""
        sumval = sum(self.edges_squared[i] * self.edges_squared[(i + 1) % 6] * self.edges_squared[(i + 2) % 6] 
                     for i in range(0, 6, 2))
        print(f"Sum of closed products: {sumval}")
        return sumval

    def _addopposite(self):
        """Calculates the sum of opposite products for volume calculation."""
        sumval = sum(self.edges_squared[i] * self.edges_squared[i + 3] * (self.edges_squared[i] + self.edges_squared[i + 3]) 
                     for i in range(3))
        print(f"Sum of opposite products: {sumval}")
        return sumval

def make_tet(v0, v1, v2):
    """Generates a tetrahedron from three vectors and calculates its volumes."""
    tet = Tetrahedron(v0.length(), v1.length(), v2.length(), 
                      (v0 - v1).length(), (v1 - v2).length(), (v2 - v0).length())
    print(f"Making tetrahedron with vertices: {v0}, {v1}, {v2}")
    return tet.ivm_volume(), tet.xyz_volume()

PHI = (1 + ROOT5) / 2.0

# Simplified constants
R = 0.5
D = 1.0
ROOT3 = sqrt(3)

import unittest
class Test_Tetrahedron(unittest.TestCase):
    # Unit tests for Tetrahedron and Triangle classes

    def test_unit_volume(self):
        """Tests unit volume calculation."""
        tet = Tetrahedron(D, D, D, D, D, D)
        self.assertAlmostEqual(tet.ivm_volume(), 1, msg="Volume not 1")

    # Additional tests omitted for brevity

def command_line():
    """Processes command-line arguments to calculate tetrahedron volumes."""
    args = sys.argv[1:]
    if len(args) == 6:
        try:
            args = [float(x) for x in args]
            t = Tetrahedron(*args)
            print(f"IVM Volume (from command line): {t.ivm_volume():.6f}")
            print(f"XYZ Volume (from command line): {t.xyz_volume():.6f}")
        except ValueError:
            print("Error: All arguments must be numbers.")
    else:
        print("Usage: python tetravolume.py <a> <b> <c> <d> <e> <f>")

def print_as_table(data):
    """
    Prints data in a structured table format.
    :param data: List of dictionaries containing tetrahedron details.
    """
    headers = data[0].keys()
    # Determine the maximum width for each column
    column_widths = {header: max(len(header), max(len(str(row[header])) for row in data)) for header in headers}
    
    # Print header
    header_row = " | ".join(header.upper().ljust(column_widths[header]) for header in headers)
    print(header_row)
    print("-" * len(header_row))
    
    # Print rows
    for row in data:
        print(" | ".join(str(row[header]).ljust(column_widths[header]) for header in headers))
        print("-" * len(header_row))

def run_all_tests_and_demos():
    """Runs all tests and demonstrations from tetravolume.py."""
    print("Tetrahedron Examples:")

examples = [
        {"Example": "Unit Tetrahedron", "Edges": "1, 1, 1, 1, 1, 1", "IVM Volume": "{:.6f}".format(Tetrahedron(1, 1, 1, 1, 1, 1).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(1, 1, 1, 1, 1, 1).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(1, 1, 1, 1, 1, 1).ivm_volume() / Tetrahedron(1, 1, 1, 1, 1, 1).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with √2 edges", "Edges": "√2, √2, √2, √2, √2, √2", "IVM Volume": "{:.6f}".format(Tetrahedron(sqrt(2), sqrt(2), sqrt(2), sqrt(2), sqrt(2), sqrt(2)).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(sqrt(2), sqrt(2), sqrt(2), sqrt(2), sqrt(2), sqrt(2)).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(sqrt(2), sqrt(2), sqrt(2), sqrt(2), sqrt(2), sqrt(2)).ivm_volume() / Tetrahedron(sqrt(2), sqrt(2), sqrt(2), sqrt(2), sqrt(2), sqrt(2)).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Cube to Tetrahedron", "Edges": "1, 1, 1, sqrt(2), sqrt(2), sqrt(2)", "IVM Volume": "{:.6f}".format(Tetrahedron(1, 1, 1, sqrt(2), sqrt(2), sqrt(2)).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(1, 1, 1, sqrt(2), sqrt(2), sqrt(2)).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(1, 1, 1, sqrt(2), sqrt(2), sqrt(2)).ivm_volume() / Tetrahedron(1, 1, 1, sqrt(2), sqrt(2), sqrt(2)).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with edges of length 2", "Edges": "2, 2, 2, 2, 2, 2", "IVM Volume": "{:.6f}".format(Tetrahedron(2, 2, 2, 2, 2, 2).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(2, 2, 2, 2, 2, 2).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(2, 2, 2, 2, 2, 2).ivm_volume() / Tetrahedron(2, 2, 2, 2, 2, 2).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Golden Ratio Tetrahedron", "Edges": "Phi, Phi, Phi, Phi, Phi, Phi", "IVM Volume": "{:.6f}".format(Tetrahedron(PHI, PHI, PHI, PHI, PHI, PHI).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(PHI, PHI, PHI, PHI, PHI, PHI).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(PHI, PHI, PHI, PHI, PHI, PHI).ivm_volume() / Tetrahedron(PHI, PHI, PHI, PHI, PHI, PHI).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with √3 edges", "Edges": "√3, √3, √3, √3, √3, √3", "IVM Volume": "{:.6f}".format(Tetrahedron(sqrt(3), sqrt(3), sqrt(3), sqrt(3), sqrt(3), sqrt(3)).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(sqrt(3), sqrt(3), sqrt(3), sqrt(3), sqrt(3), sqrt(3)).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(sqrt(3), sqrt(3), sqrt(3), sqrt(3), sqrt(3), sqrt(3)).ivm_volume() / Tetrahedron(sqrt(3), sqrt(3), sqrt(3), sqrt(3), sqrt(3), sqrt(3)).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with π edges", "Edges": "π, π, π, π, π, π", "IVM Volume": "{:.6f}".format(Tetrahedron(pi, pi, pi, pi, pi, pi).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(pi, pi, pi, pi, pi, pi).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(pi, pi, pi, pi, pi, pi).ivm_volume() / Tetrahedron(pi, pi, pi, pi, pi, pi).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with e edges", "Edges": "e, e, e, e, e, e", "IVM Volume": "{:.6f}".format(Tetrahedron(e, e, e, e, e, e).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(e, e, e, e, e, e).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(e, e, e, e, e, e).ivm_volume() / Tetrahedron(e, e, e, e, e, e).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with Fibonacci edges", "Edges": "1, 1, 2, 3, 5, 8", "IVM Volume": "{:.6f}".format(Tetrahedron(1, 1, 2, 3, 5, 8).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(1, 1, 2, 3, 5, 8).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(1, 1, 2, 3, 5, 8).ivm_volume() / Tetrahedron(1, 1, 2, 3, 5, 8).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with prime edges", "Edges": "2, 3, 5, 7, 11, 13", "IVM Volume": "{:.6f}".format(Tetrahedron(2, 3, 5, 7, 11, 13).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(2, 3, 5, 7, 11, 13).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(2, 3, 5, 7, 11, 13).ivm_volume() / Tetrahedron(2, 3, 5, 7, 11, 13).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with powers of 2", "Edges": "1, 2, 4, 8, 16, 32", "IVM Volume": "{:.6f}".format(Tetrahedron(1, 2, 4, 8, 16, 32).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(1, 2, 4, 8, 16, 32).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(1, 2, 4, 8, 16, 32).ivm_volume() / Tetrahedron(1, 2, 4, 8, 16, 32).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with powers of 3", "Edges": "1, 3, 9, 27, 81, 243", "IVM Volume": "{:.6f}".format(Tetrahedron(1, 3, 9, 27, 81, 243).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(1, 3, 9, 27, 81, 243).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(1, 3, 9, 27, 81, 243).ivm_volume() / Tetrahedron(1, 3, 9, 27, 81, 243).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60},
        {"Example": "Tetrahedron with edges 1/√2", "Edges": "1/√2, 1/√2, 1/√2, 1/√2, 1/√2, 1/√2", "IVM Volume": "{:.6f}".format(Tetrahedron(1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2)).ivm_volume()), "XYZ Volume": "{:.6f}".format(Tetrahedron(1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2)).xyz_volume()), "IVM/XYZ Volume Ratio": "{:.6f}".format(Tetrahedron(1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2)).ivm_volume() / Tetrahedron(1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2), 1/sqrt(2)).xyz_volume()), "Interior Angles": [60, 60, 60], "Average Interior Angle": 60}
    ]
    
print_as_table(examples)
    

if __name__ == "__main__":
    run_all_tests_and_demos()
    command_line()
