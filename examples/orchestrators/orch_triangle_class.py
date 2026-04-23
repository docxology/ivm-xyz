"""
Triangle class from three edge lengths: IVM and XYZ areas (Heron-style path in package).

Run from repo root: uv run python examples/orchestrators/orch_triangle_class.py
"""

from ivm_xyz import Triangle


def main() -> None:
    print("=== Equilateral side 1 ===")
    t = Triangle(1, 1, 1)
    print(f"  ivm_area: {t.ivm_area():.6f}")
    print(f"  xyz_area: {t.xyz_area():.6f}")

    print("\n=== 3-4-5 triangle ===")
    t = Triangle(3, 4, 5)
    print(f"  ivm_area: {t.ivm_area():.6f}")
    print(f"  xyz_area: {t.xyz_area():.6f}")


if __name__ == "__main__":
    main()
