"""
Print shared geometric constants from ivm_xyz.core.constants.

Run from repo root: uv run python examples/orchestrators/orch_constants.py
"""

from ivm_xyz.core.constants import D, R, PHI, ROOT2, ROOT3, ROOT5, S3


def main() -> None:
    print("=== ivm_xyz.core.constants ===")
    for name, val in [
        ("D", D),
        ("R", R),
        ("PHI", PHI),
        ("ROOT2", ROOT2),
        ("ROOT3", ROOT3),
        ("ROOT5", ROOT5),
        ("S3", S3),
    ]:
        print(f"  {name} = {val:.12f}")


if __name__ == "__main__":
    main()
