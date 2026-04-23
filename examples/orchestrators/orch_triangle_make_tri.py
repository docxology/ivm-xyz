"""
Two position vectors (from origin) -> make_tri -> IVM and XYZ triangle areas.

``make_tri`` uses edge lengths ``|v0|``, ``|v1|``, ``|v1-v0|`` (same as
:class:`ivm_xyz.core.triangle.Triangle`). With ``--check``, compares to
explicit Heron areas on those three lengths (not to ½|v0×v1| unless the two
constructions coincide).

Run from repo root:
  uv run python examples/orchestrators/orch_triangle_make_tri.py
  uv run python examples/orchestrators/orch_triangle_make_tri.py --check
"""

from __future__ import annotations

import argparse
import math
import sys
from typing import List, Optional, Tuple

from ivm_xyz import Triangle, Vector, make_tri

DEFAULT_RTOl = 1e-9
DEFAULT_ATOL = 1e-12


def _heron_pair(v1: Vector, v2: Vector) -> Tuple[float, float]:
    a, b, c = v1.length(), v2.length(), (v2 - v1).length()
    t = Triangle(a, b, c)
    return t.ivm_area(), t.xyz_area()


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if make_tri disagrees with Triangle(|v0|,|v1|,|v1-v0|) (Heron)",
    )
    p.add_argument("--rtol", type=float, default=DEFAULT_RTOl)
    p.add_argument("--atol", type=float, default=DEFAULT_ATOL)
    args = p.parse_args(argv)

    print("=== make_tri: canonical basis in XY ===")
    v1 = Vector((1.0, 0.0, 0.0))
    v2 = Vector((0.0, 1.0, 0.0))
    ivm_a, xyz_a = make_tri(v1, v2)
    h_ivm, h_xyz = _heron_pair(v1, v2)
    print(f"  IVM area: {ivm_a:.6f}  (Heron on |v0|,|v1|,|v0-v1|: {h_ivm:.6f})")
    print(f"  XYZ area: {xyz_a:.6f}  (Heron XYZ: {h_xyz:.6f})")
    if args.check:
        if not math.isclose(ivm_a, h_ivm, rel_tol=args.rtol, abs_tol=args.atol):
            print("  FAIL: IVM vs Heron", file=sys.stderr)
            return 1
        if not math.isclose(xyz_a, h_xyz, rel_tol=args.rtol, abs_tol=args.atol):
            print("  FAIL: XYZ vs Heron", file=sys.stderr)
            return 1

    print("\n=== make_tri: scaled legs (3 and 4 in XY, edge 5) ===")
    v1 = Vector((3.0, 0.0, 0.0))
    v2 = Vector((0.0, 4.0, 0.0))
    ivm_a, xyz_a = make_tri(v1, v2)
    h_ivm, h_xyz = _heron_pair(v1, v2)
    print(f"  IVM area: {ivm_a:.6f}  (Heron: {h_ivm:.6f})")
    print(f"  XYZ area: {xyz_a:.6f}  (Heron XYZ: {h_xyz:.6f})")
    if args.check:
        if not math.isclose(ivm_a, h_ivm, rel_tol=args.rtol, abs_tol=args.atol):
            print("  FAIL: IVM vs Heron", file=sys.stderr)
            return 1
        if not math.isclose(xyz_a, h_xyz, rel_tol=args.rtol, abs_tol=args.atol):
            print("  FAIL: XYZ vs Heron", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
