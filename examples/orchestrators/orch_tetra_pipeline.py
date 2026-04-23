"""
Three position vectors -> make_tet -> IVM and XYZ volumes.

Run from repo root: uv run python examples/orchestrators/orch_tetra_pipeline.py
"""

from ivm_xyz import Vector, make_tet


def main() -> None:
    v1 = Vector((1.0, 0.0, 0.0))
    v2 = Vector((0.0, 1.0, 0.0))
    v3 = Vector((0.0, 0.0, 1.0))
    ivm_v, xyz_v = make_tet(v1, v2, v3)
    print("=== make_tet from canonical basis ===")
    print(f"  IVM volume: {ivm_v:.6f}")
    print(f"  XYZ volume: {xyz_v:.6f}")

    v1 = Vector((0.5, 0.0, 0.0))
    v2 = Vector((0.0, 0.5, 0.0))
    v3 = Vector((0.0, 0.0, 0.5))
    ivm_v, xyz_v = make_tet(v1, v2, v3)
    print("\n=== make_tet from (0.5,0,0), (0,0.5,0), (0,0,0.5) ===")
    print(f"  IVM volume: {ivm_v:.6f}")
    print(f"  XYZ volume: {xyz_v:.6f}")


if __name__ == "__main__":
    main()
