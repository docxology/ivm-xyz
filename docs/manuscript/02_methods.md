# Methods

The conversion fixture contains a point in each Cartesian octant, the
origin, and a point on a coordinate plane. The replay computes each point's
Quadray coordinates, checks their normalization, converts back to Cartesian
coordinates, and repeats the projection after a common coefficient shift.

The regular tetrahedron comes from the package's four basis vertices.
The replay projects those vertices, measures the edge lengths, and
computes the centroid and determinant volume independently of the
edge-length volume API. Applying that API at two scales checks cubic
scaling under the package's volume convention. The same vertices and
faces feed the native visualization.
