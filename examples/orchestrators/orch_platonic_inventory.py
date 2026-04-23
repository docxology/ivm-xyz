"""
Instantiate each exported Platonic-type solid and print volume and vertex count.

Run from repo root: uv run python examples/orchestrators/orch_platonic_inventory.py
"""

from ivm_xyz.polyhedra import (
    PolyTetrahedron,
    Cube,
    Octahedron,
    Icosahedron,
    Cuboctahedron,
)


def main() -> None:
    solids = [
        PolyTetrahedron(),
        Cube(),
        Octahedron(),
        Icosahedron(),
        Cuboctahedron(),
    ]
    print("=== Platonic inventory (polyhedra package) ===")
    for p in solids:
        print(f"  {p.name}: volume={p.volume}, vertices={len(p.vertexes)}, faces={len(p.faces)}")


if __name__ == "__main__":
    main()
