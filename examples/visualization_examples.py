"""
Visualization examples for the IVM-XYZ package.

Writes PNG (and optionally GIF) under the default plot directory (v0.2.0+:
``outputs/plots`` relative to the current working directory). Override with
``PolyhedronPlotter(output_folder=...)`` or set process CWD before running.
"""

import os

from ivm_xyz.visualization import DEFAULT_PLOT_OUTPUT_DIR, PolyhedronPlotter


def example_tetrahedron_plot():
    """Plot a simple tetrahedron."""
    print("Creating tetrahedron plot...")

    plotter = PolyhedronPlotter()

    vertices = [
        (0, 0, 0),
        (1, 0, 0),
        (0.5, 0.866, 0),
        (0.5, 0.289, 0.816),
    ]

    faces = [
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 3),
        (1, 2, 3),
    ]

    plotter.plot_polyhedron(
        vertices,
        faces,
        title="Regular Tetrahedron",
        save=True,
        file_name="tetrahedron.png",
    )
    out = os.path.join(plotter.output_folder, "tetrahedron.png")
    print(f"Saved to {out}")


def example_cube_plot():
    """Plot a cube."""
    print("Creating cube plot...")

    plotter = PolyhedronPlotter()

    vertices = [
        (-1, -1, -1),
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, 1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, 1, 1),
    ]

    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (2, 6, 7, 3),
        (0, 3, 7, 4),
        (1, 5, 6, 2),
    ]

    plotter.plot_polyhedron(
        vertices,
        faces,
        title="Cube",
        save=True,
        file_name="cube.png",
    )
    out = os.path.join(plotter.output_folder, "cube.png")
    print(f"Saved to {out}")


def example_animation():
    """Create animated GIF of multiple polyhedra."""
    print("Creating animations...")

    plotter = PolyhedronPlotter()

    tet_vertices = [
        (0, 0, 0),
        (1, 0, 0),
        (0.5, 0.866, 0),
        (0.5, 0.289, 0.816),
    ]
    tet_faces = [
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 3),
        (1, 2, 3),
    ]
    plotter.add_polyhedron(
        tet_vertices,
        tet_faces,
        "Tetrahedron",
        "tetrahedron.gif",
    )

    cube_vertices = [
        (-1, -1, -1),
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, 1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, 1, 1),
    ]
    cube_faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (2, 6, 7, 3),
        (0, 3, 7, 4),
        (1, 5, 6, 2),
    ]
    plotter.add_polyhedron(
        cube_vertices,
        cube_faces,
        "Cube",
        "cube.gif",
    )

    try:
        plotter.animate_polyhedron(save=True)
        print(f"Saved animations under {plotter.output_folder}/")
    except ImportError:
        print("Error: imageio is required for animations.")
        print("Install with: pip install imageio")


if __name__ == "__main__":
    os.makedirs(DEFAULT_PLOT_OUTPUT_DIR, exist_ok=True)

    example_tetrahedron_plot()
    example_cube_plot()

    # Uncomment to create animations (requires imageio)
    # example_animation()
