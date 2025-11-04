"""
Edge counting functions for various geometric structures.

These functions calculate the number of contact points (edges) between
equal spheres arranged in various geometric configurations.
"""


def tri(n: int) -> int:
    """Triangular number n."""
    return n * (n + 1) // 2


def sqr(n: int) -> int:
    """Square number n."""
    return n ** 2


def tet_edges(f: int) -> int:
    """
    Number of contact points between equal spheres arranged in a tetrahedron
    with f intervals along each edge.
    
    Each layer of tri(N) balls spawns N tetrahedrons of 6 edges each,
    accumulating to give a next layer of tri(N+1) balls, and so on.
    
    Args:
        f: Frequency (number of intervals along each edge)
    
    Returns:
        int: Total number of edges/contact points
    
    References:
        https://oeis.org/A007531
    """
    cumm = 0
    for layer in range(1, f + 1):
        if layer == 1:
            cumm = 6
        else:
            cumm = cumm + tri(layer) * 6
    return cumm


def half_oct_edges(f: int) -> int:
    """
    Number of contact points between equal spheres arranged in a half octahedron
    with f intervals along each edge.
    
    Each layer of sqr(N) balls spawns N half-octahedrons, with 4*N edges
    to the next layer of N+1 balls per edge, plus (layer+1)*layer*2 layer edges.
    
    Args:
        f: Frequency (number of intervals along each edge)
    
    Returns:
        int: Total number of edges/contact points
    
    References:
        https://oeis.org/A035006
    """
    cumm = 0
    for layer in range(1, f + 1):
        if layer == 1:
            cumm = 8
        else:
            cumm = cumm + sqr(layer) * 4 + (layer + 1) * layer * 2
    return cumm


def oct_edges(f: int) -> int:
    """
    Number of contact points between equal spheres arranged in an octahedron
    with f intervals along each edge.
    
    Two half-octas minus the layer they have in common.
    
    Args:
        f: Frequency (number of intervals along each edge)
    
    Returns:
        int: Total number of edges/contact points
    
    References:
        https://oeis.org/A300758
    """
    return 2 * half_oct_edges(f) - (f + 1) * f * 2


def cubocta_edges(f: int) -> int:
    """
    Number of contact points between equal spheres arranged in a cuboctahedron
    with f intervals between balls along each edge.
    
    Args:
        f: Frequency (number of intervals along each edge)
    
    Returns:
        int: Total number of edges/contact points
    """
    x = f + 1
    return 20 * x ** 3 - 48 * x ** 2 + 40 * x - 12


def cubocta_layer(f: int) -> int:
    """
    Number of contact points between equal spheres arranged in layer n
    of a cuboctahedron with n intervals between balls along each edge.
    
    Args:
        f: Frequency (layer number)
    
    Returns:
        int: Number of edges/contact points in this layer
    
    References:
        https://oeis.org/A069074
    """
    x = f - 1
    return 8 * x ** 3 + 36 * x ** 2 + 52 * x + 24


# Alternative closed-form implementations
def a007531(n: int) -> int:
    """Tetrahedron edges (ball contacts) - closed form."""
    return n * (n + 1) * (n + 2)


def a035006(n: int) -> int:
    """Half octahedron edges (ball contacts) - closed form."""
    return n * 2 * (n + 1) ** 2


def a300758(n: int) -> int:
    """Octahedron edges (ball contacts) - closed form."""
    return 2 * n * (n + 1) * (2 * n + 1)

