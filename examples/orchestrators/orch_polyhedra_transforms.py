"""
Scale and translate a Platonic solid (Cube) in quadray space.

Run from repo root: uv run python examples/orchestrators/orch_polyhedra_transforms.py
"""

from ivm_xyz.polyhedra import Cube
from ivm_xyz.core.vectors import Qvector


def main() -> None:
    c0 = Cube()
    print(f"=== {c0.name} (initial) ===")
    print(f"  volume: {c0.volume}")
    print(f"  vertices: {len(c0.vertexes)}")

    c1 = c0.scale(2.0)
    print(f"\n=== After scale(2.0) ===")
    print(f"  volume: {c1.volume}")

    # Asymmetric quadray so normalization does not collapse to the origin.
    shift = Qvector((1.0, 0.0, 0.25, 0.0))
    c2 = c1.translate(shift)
    k0 = sorted(c1.vertexes.keys())[0]
    print(f"\n=== After translate(shift) ===")
    print(f"  shift (quadray): {shift}")
    print(f"  vertex {k0} before: {c1.vertexes[k0]}")
    print(f"  vertex {k0} after:  {c2.vertexes[k0]}")
    print("  (Polyhedron.translate updates vertex positions; .volume is not recomputed here.)")


if __name__ == "__main__":
    main()
