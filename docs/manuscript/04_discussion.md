# Discussion

The public volume API uses a normalized tetrahedral measure. Its XYZ value is
the normalized IVM volume divided by the package's conversion constant.
For coordinates measured along the plotted axes, the determinant gives
volume in cubic coordinate units. Both volume measures scale cubically
under uniform edge scaling.

The experiment covers a finite set of coordinates and a regular tetrahedron.
Its tolerance applies to those inputs. A larger stability study could vary
magnitude, degeneracy, and coordinate precision separately.
