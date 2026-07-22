"""
Scalar and object conversion: XYZ <-> quadray (IVM), with optional round-trip checks.

Run from repo root:
  uv run python examples/orchestrators/orch_conversion_roundtrip.py
  uv run python examples/orchestrators/orch_conversion_roundtrip.py --check
"""

from __future__ import annotations

import argparse
import math
import sys
from typing import List, Optional, Tuple

from ivm_xyz import Vector
from ivm_xyz.conversion import ivm_to_xyz, xyz_to_ivm
from ivm_xyz.conversion.converters import qvector_to_vector, vector_to_qvector

DEFAULT_RTOl = 1e-9
DEFAULT_ATOL = 1e-12


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--check",
        action="store_true",
        help="Exit with status 1 if a round-trip is outside rtol/atol (math.isclose per component)",
    )
    p.add_argument("--rtol", type=float, default=DEFAULT_RTOl)
    p.add_argument("--atol", type=float, default=DEFAULT_ATOL)
    args = p.parse_args(argv)
    rtol, atol = args.rtol, args.atol

    points: List[Tuple[float, float, float]] = [
        (1.0, 2.0, 3.0),
        (-1.0, 0.0, 2.5),
        (0.0, 0.0, 0.0),
    ]
    print("=== Scalar round-trip (xyz_to_ivm / ivm_to_xyz) ===")
    for x, y, z in points:
        q = xyz_to_ivm(x, y, z)
        bx, by, bz = ivm_to_xyz(*q)
        print(
            f"  in ({x}, {y}, {z}) out ({bx:.6f}, {by:.6f}, {bz:.6f}) quadray={tuple(round(t, 6) for t in q)}"
        )
        if args.check:
            for a, b in ((x, bx), (y, by), (z, bz)):
                if not math.isclose(a, b, rel_tol=rtol, abs_tol=atol):
                    print(
                        f"  FAIL: not close: {a!r} vs {b!r} (rtol={rtol} atol={atol})",
                        file=sys.stderr,
                    )
                    return 1

    print("\n=== Vector <-> Qvector (vector_to_qvector / qvector_to_vector) ===")
    v = Vector((2.0, -0.5, 1.0))
    v_back = qvector_to_vector(vector_to_qvector(v))
    print(f"  in  ({v.x}, {v.y}, {v.z}) out ({v_back.x:.6f}, {v_back.y:.6f}, {v_back.z:.6f})")
    if args.check:
        for a, b in ((v.x, v_back.x), (v.y, v_back.y), (v.z, v_back.z)):
            if not math.isclose(a, b, rel_tol=rtol, abs_tol=atol):
                print(f"  FAIL: vector component {a!r} vs {b!r}", file=sys.stderr)
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
