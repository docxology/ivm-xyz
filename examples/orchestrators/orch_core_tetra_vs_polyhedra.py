"""
Contrast core.Tetrahedron (six edge lengths) vs polyhedra.PolyTetrahedron (Concentric Hierarchy solid).

Run from repo root: uv run python examples/orchestrators/orch_core_tetra_vs_polyhedra.py
"""

from ivm_xyz import Tetrahedron as EdgeTet
from ivm_xyz.polyhedra import PolyTetrahedron


def main() -> None:
    print("=== core.Tetrahedron (volume from six edge lengths) ===")
    t = EdgeTet(1, 1, 1, 1, 1, 1)
    print(
        f"  regular edges 1,1,1,1,1,1 -> ivm_volume()={t.ivm_volume():.6f} xyz_volume()={t.xyz_volume():.6f}"
    )

    print("\n=== polyhedra.PolyTetrahedron (Concentric Hierarchy polyhedron) ===")
    p = PolyTetrahedron()
    print(f"  {p.name}: volume (model)={p.volume}, vertices={len(p.vertexes)}")


if __name__ == "__main__":
    main()
