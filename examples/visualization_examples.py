"""
Visualization examples for the IVM-XYZ package.
"""

from ivm_xyz.visualization import PolyhedronPlotter


def example_tetrahedron_plot():
    """Plot a simple tetrahedron."""
    print("Creating tetrahedron plot...")
    
    plotter = PolyhedronPlotter(output_folder="images")
    
    # Tetrahedron vertices
    vertices = [
        (0, 0, 0),
        (1, 0, 0),
        (0.5, 0.866, 0),
        (0.5, 0.289, 0.816)
    ]
    
    # Tetrahedron faces
    faces = [
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 3),
        (1, 2, 3)
    ]
    
    plotter.plot_polyhedron(
        vertices, faces,
        title="Regular Tetrahedron",
        save=True,
        file_name="tetrahedron.png"
    )
    print("Saved to images/tetrahedron.png")


def example_cube_plot():
    """Plot a cube."""
    print("Creating cube plot...")
    
    plotter = PolyhedronPlotter(output_folder="images")
    
    # Cube vertices
    vertices = [
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
    ]
    
    # Cube faces
    faces = [
        (0, 1, 2, 3),  # bottom
        (4, 7, 6, 5),  # top
        (0, 4, 5, 1),  # front
        (2, 6, 7, 3),  # back
        (0, 3, 7, 4),  # left
        (1, 5, 6, 2)   # right
    ]
    
    plotter.plot_polyhedron(
        vertices, faces,
        title="Cube",
        save=True,
        file_name="cube.png"
    )
    print("Saved to images/cube.png")


def example_animation():
    """Create animated GIF of multiple polyhedra."""
    print("Creating animations...")
    
    plotter = PolyhedronPlotter(output_folder="images")
    
    # Tetrahedron
    tet_vertices = [
        (0, 0, 0), (1, 0, 0), (0.5, 0.866, 0), (0.5, 0.289, 0.816)
    ]
    tet_faces = [
        (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)
    ]
    plotter.add_polyhedron(
        tet_vertices, tet_faces,
        "Tetrahedron",
        "tetrahedron.gif"
    )
    
    # Cube
    cube_vertices = [
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
    ]
    cube_faces = [
        (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
        (2, 6, 7, 3), (0, 3, 7, 4), (1, 5, 6, 2)
    ]
    plotter.add_polyhedron(
        cube_vertices, cube_faces,
        "Cube",
        "cube.gif"
    )
    
    try:
        plotter.animate_polyhedron(save=True)
        print("Saved animations to images/")
    except ImportError:
        print("Error: imageio is required for animations.")
        print("Install with: pip install imageio")


if __name__ == "__main__":
    import os
    os.makedirs("images", exist_ok=True)
    
    example_tetrahedron_plot()
    example_cube_plot()
    
    # Uncomment to create animations (requires imageio)
    # example_animation()

