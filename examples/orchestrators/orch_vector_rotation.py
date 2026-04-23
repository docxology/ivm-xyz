"""
Vector.rotz / roty on a simple direction; unit() length check.

Run from repo root: uv run python examples/orchestrators/orch_vector_rotation.py
"""

from ivm_xyz import Vector


def main() -> None:
    v = Vector((1.0, 0.0, 0.0))
    print("=== Start ===")
    print(f"  v = ({v.x}, {v.y}, {v.z})")

    rz = v.rotz(90.0)
    print("\n=== After rotz(90) ===")
    print(f"  v = ({rz.x:.6f}, {rz.y:.6f}, {rz.z:.6f})")

    ry = v.roty(90.0)
    print("\n=== After roty(90) (from original) ===")
    print(f"  v = ({ry.x:.6f}, {ry.y:.6f}, {ry.z:.6f})")

    u = v.unit()
    print("\n=== unit() ===")
    print(f"  length before: {v.length():.6f}, unit length: {u.length():.6f}")


if __name__ == "__main__":
    main()
