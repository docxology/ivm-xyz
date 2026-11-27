"""Reproduce coordinate measurements and the IVM-XYZ manuscript plot."""

from itertools import combinations, product
import json
from math import dist, isclose, sqrt
from pathlib import Path

import numpy as np

from ivm_xyz import Tetrahedron, ivm_to_xyz, xyz_to_ivm
from ivm_xyz.polyhedra import PolyTetrahedron
from ivm_xyz.visualization import PolyhedronPlotter


ROOT = Path(__file__).resolve().parents[1]
TOLERANCE = 1e-12


def main() -> None:
    points = [(x, 2 * y, 3 * z) for x, y, z in product((-1.0, 1.0), repeat=3)]
    points.extend(((0.0, 0.0, 0.0), (0.0, 1.25, -2.5)))
    roundtrips = []
    for point in points:
        quadray = xyz_to_ivm(*point)
        restored = ivm_to_xyz(*quadray)
        shifted = ivm_to_xyz(*(coefficient + 5 for coefficient in quadray))
        error = dist(point, restored)
        shift_error = dist(restored, shifted)
        if min(quadray) != 0 or max(error, shift_error) > TOLERANCE:
            raise ValueError(f"Coordinate conversion failed for {point}.")
        roundtrips.append({
            "cartesian": point, "quadray": quadray, "round_trip_error": error,
            "common_shift_projection_error": shift_error,
        })

    tetrahedron = PolyTetrahedron()
    vertices = {name: tuple(vector.xyz().xyz) for name, vector in tetrahedron.vertexes.items()}
    coordinates = np.array(list(vertices.values()))
    lengths = [dist(vertices[a], vertices[b]) for a, b in combinations(vertices, 2)]
    centroid = coordinates.mean(axis=0)
    determinant_volume = abs(float(np.linalg.det(coordinates[1:] - coordinates[0]))) / 6
    if not np.allclose(lengths, 1, rtol=0, atol=TOLERANCE) or not np.allclose(
        centroid, 0, rtol=0, atol=TOLERANCE
    ):
        raise ValueError("The projected tetrahedron is not regular and centered at the origin.")
    if not isclose(determinant_volume, sqrt(2) / 12, rel_tol=0, abs_tol=TOLERANCE):
        raise ValueError("Determinant volume differs from the analytic unit tetrahedron volume.")

    unit = Tetrahedron(*([1.0] * 6))
    doubled = Tetrahedron(*([2.0] * 6))
    scaling = doubled.ivm_volume() / unit.ivm_volume()
    if not isclose(scaling, 8, rel_tol=0, abs_tol=TOLERANCE):
        raise ValueError("The normalized tetrahedron volume did not scale cubically.")

    figure_dir = ROOT / "output" / "figures"
    data_dir = ROOT / "output" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    vertex_indices = {name: index for index, name in enumerate(vertices)}
    faces = [[vertex_indices[name] for name in face] for face in tetrahedron.faces]
    plotted = [tuple(round(value, 4) for value in point) for point in vertices.values()]
    PolyhedronPlotter(str(figure_dir)).plot_polyhedron(
        plotted, faces, title="Regular tetrahedron in Cartesian coordinates",
        save=True, file_name="ivm-tetrahedron.png",
    )
    measurements = {
        "case_count": len(roundtrips), "tolerance": TOLERANCE, "coordinate_checks": roundtrips,
        "tetrahedron": {
            "vertices": len(vertices), "edges": len(lengths), "edge_lengths": lengths,
            "centroid": centroid.tolist(), "ivm_volume": unit.ivm_volume(),
            "package_xyz_volume": unit.xyz_volume(), "determinant_volume": determinant_volume,
            "determinant_volume_rounded": round(determinant_volume, 6),
            "package_xyz_volume_rounded": round(unit.xyz_volume(), 6), "scale_factor": scaling,
        },
    }
    (data_dir / "ivm-coordinate-evidence.json").write_text(json.dumps(measurements, indent=2) + "\n")
    registry = {"figures": [{
        "label": "fig:ivm-tetrahedron", "filename": "ivm-tetrahedron.png",
        "caption": "Regular tetrahedron from the package's visualization routine.",
        "alt_text": "Four vertices and shaded faces form a regular tetrahedron around the origin.",
        "generated_by": "python -m docs.reproduce_geometry",
    }]}
    (figure_dir / "figure_registry.json").write_text(json.dumps(registry, indent=2) + "\n")
    print("Verified ten coordinate cases, six unit edges, and the two volume conventions.")


if __name__ == "__main__":
    main()
