"""
Build a Cube from polyhedra, extract XYZ mesh, write one PNG with PolyhedronPlotter.

Requires optional extra: ``pip install -e ".[visualization]"`` (matplotlib).

Default output: ``<IVM_XYZ_OUTPUT_ROOT>/plots/orchestrators/`` (see config.py; default
``outputs/plots/orchestrators`` under the repo root).

Run from repo root:
  uv run python examples/orchestrators/orch_plot_polyhedron.py
  uv run python examples/orchestrators/orch_plot_polyhedron.py --output-dir /tmp/plots
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import List, Optional, Tuple

from ivm_xyz.polyhedra import Cube

# Same directory as this script
sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as orch_config  # noqa: E402


def _cube_mesh(cube: Cube) -> Tuple[List[tuple], list]:
    vertices = []
    for key in sorted(cube.vertexes.keys()):
        v = cube.vertexes[key]
        if hasattr(v, "xyz"):
            xyz = v.xyz()
            vertices.append((xyz.x, xyz.y, xyz.z))
        else:
            vertices.append((v.x, v.y, v.z))
    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (2, 6, 7, 3),
        (0, 3, 7, 4),
        (1, 5, 6, 2),
    ]
    return vertices, faces


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Override output directory (default: from IVM_XYZ_OUTPUT_ROOT / plots / orchestrators)",
    )
    p.add_argument(
        "--file-name",
        default="orch_cube.png",
        help="File name within the output directory",
    )
    args = p.parse_args(argv)

    try:
        from ivm_xyz.visualization import PolyhedronPlotter
    except ImportError as err:
        print("matplotlib is required. Install with: uv sync --all-extras", file=sys.stderr)
        raise SystemExit(1) from err

    out_dir = args.output_dir
    if out_dir is None:
        out_dir = str(orch_config.plots_orchestrators_dir())
    else:
        os.makedirs(out_dir, exist_ok=True)

    cube = Cube()
    vertices, faces = _cube_mesh(cube)
    plotter = PolyhedronPlotter(output_folder=out_dir)
    plotter.plot_polyhedron(
        vertices,
        faces,
        title=f"{cube.name} from polyhedra",
        save=True,
        file_name=args.file_name,
    )
    print(f"Wrote {os.path.join(out_dir, args.file_name)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
