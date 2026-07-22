"""
Visualization tools for polyhedra using matplotlib.

This module provides functionality to plot and animate polyhedral structures.
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend
import os  # noqa: E402
from concurrent.futures import ThreadPoolExecutor  # noqa: E402
from typing import Any, Dict, List, Optional, Sequence, Tuple  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402

# Maximum number of threads for parallel processing
MAX_THREADS = 8

# Frames per second for generated animations.
ANIMATION_FPS = 20

# Default save directory (relative to process working directory) — v0.2.0+
DEFAULT_PLOT_OUTPUT_DIR = "outputs/plots"

# Type aliases for readability.
Vertex = Tuple[float, float, float]
Vertices = Sequence[Vertex]
Faces = Sequence[Sequence[int]]


class PolyhedronPlotter:
    """
    Class for plotting and animating polyhedra.

    Supports both static plots and animated GIFs of 3D polyhedral structures.
    """

    def __init__(self, output_folder: Optional[str] = None) -> None:
        """
        Initialize the plotter.

        Args:
            output_folder: Directory to save output images/animations. Defaults to
                :data:`DEFAULT_PLOT_OUTPUT_DIR` (``"outputs/plots"``), relative to the
                current working directory.
        """
        if output_folder is None:
            output_folder = DEFAULT_PLOT_OUTPUT_DIR
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        self.polyhedrons: List[Dict[str, Any]] = []  # List to store polyhedron dictionaries

    def add_polyhedron(self, vertices: Vertices, faces: Faces, title: str, file_name: str) -> None:
        """
        Add a polyhedron to the list for animation.

        Args:
            vertices: List of tuples, each representing (x, y, z) coordinates
            faces: List of tuples, each representing vertex indices forming a face
            title: Title of the polyhedron
            file_name: Name of the file to save the animation as
        """
        polyhedron = {"vertices": vertices, "faces": faces, "title": title, "file_name": file_name}
        self.polyhedrons.append(polyhedron)

    def plot_polyhedron(
        self,
        vertices: Vertices,
        faces: Faces,
        title: str = "Polyhedron Visualization",
        save: bool = False,
        file_name: str = "polyhedron.png",
    ) -> None:
        """
        Plot a polyhedron given its vertices and faces.

        Args:
            vertices: List of tuples, each representing (x, y, z) coordinates
            faces: List of tuples, each representing vertex indices forming a face
            title: Title of the plot
            save: Boolean indicating whether to save the plot
            file_name: Name of the file to save the plot as
        """
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection="3d")

        vtx = [[vertices[i] for i in face] for face in faces]

        poly = Poly3DCollection(
            vtx, facecolors="skyblue", linewidths=0.5, edgecolors="darkblue", alpha=0.5
        )
        ax.add_collection3d(poly)

        for i, (x, y, z) in enumerate(vertices):
            ax.scatter(x, y, z, color="darkred", s=100, edgecolors="black", zorder=5)
            ax.text(x, y, z, f"  V{i+1} ({x}, {y}, {z})", color="black")

        ax.set_xlabel("X Axis", fontsize=12)
        ax.set_ylabel("Y Axis", fontsize=12)
        ax.set_zlabel("Z Axis", fontsize=12)

        ax.set_xlim([min(v[0] for v in vertices) - 1, max(v[0] for v in vertices) + 1])
        ax.set_ylim([min(v[1] for v in vertices) - 1, max(v[1] for v in vertices) + 1])
        ax.set_zlim([min(v[2] for v in vertices) - 1, max(v[2] for v in vertices) + 1])

        plt.title(title, fontsize=14, fontweight="bold")
        plt.tight_layout()

        if save:
            os.makedirs(self.output_folder, exist_ok=True)
            plt.savefig(os.path.join(self.output_folder, file_name))
        else:  # pragma: no cover - interactive display, not exercised headlessly
            plt.show()
        plt.close(fig)

    @staticmethod
    def _render_frame(fig: "plt.Figure") -> "np.ndarray":
        """
        Render a drawn matplotlib figure to an ``(H, W, 3)`` uint8 RGB array.

        Uses ``buffer_rgba`` (the RGB ``tostring_rgb`` API was removed in
        matplotlib 3.10) and drops the alpha channel. The result is copied so it
        stays valid after the figure is closed.
        """
        fig.canvas.draw()
        # buffer_rgba() is provided by the Agg backend canvas selected above; the
        # base canvas type used for static typing does not declare it.
        rgba = np.asarray(fig.canvas.buffer_rgba())  # type: ignore[attr-defined]
        return rgba[..., :3].copy()

    def animate_polyhedron(self, save: bool = False) -> None:
        """
        Create animated GIFs of polyhedra in the list.

        Uses parallel processing across multiple CPU threads (up to MAX_THREADS).

        Args:
            save: Boolean indicating whether to save the animations
        """
        try:
            import imageio
        except ImportError:
            raise ImportError(
                "imageio is required for animation. Install with: pip install imageio"
            )

        num_threads = min(len(self.polyhedrons), MAX_THREADS)

        def plot_and_save(polyhedron: Dict[str, Any]) -> None:
            vertices = polyhedron["vertices"]
            faces = polyhedron["faces"]
            title = polyhedron["title"]
            file_name = polyhedron["file_name"]

            images: List[Any] = []
            for angle in range(0, 360, 2):
                fig = plt.figure(figsize=(10, 8))
                ax = fig.add_subplot(111, projection="3d")

                vtx = [[vertices[i] for i in face] for face in faces]

                poly = Poly3DCollection(
                    vtx, facecolors="skyblue", linewidths=0.5, edgecolors="darkblue", alpha=0.5
                )
                ax.add_collection3d(poly)

                for i, (x, y, z) in enumerate(vertices):
                    ax.scatter(x, y, z, color="darkred", s=100, edgecolors="black", zorder=5)
                    ax.text(x, y, z, f"V{i+1} ({x}, {y}, {z})", color="black")

                ax.set_xlabel("X Axis", fontsize=12)
                ax.set_ylabel("Y Axis", fontsize=12)
                ax.set_zlabel("Z Axis", fontsize=12)

                ax.set_xlim([min(v[0] for v in vertices) - 1, max(v[0] for v in vertices) + 1])
                ax.set_ylim([min(v[1] for v in vertices) - 1, max(v[1] for v in vertices) + 1])
                ax.set_zlim([min(v[2] for v in vertices) - 1, max(v[2] for v in vertices) + 1])

                ax.view_init(30, angle)
                plt.title(title, fontsize=14, fontweight="bold")
                plt.tight_layout()

                images.append(self._render_frame(fig))
                plt.close(fig)

            # Duration is milliseconds per frame; `fps` was deprecated by imageio.
            imageio.mimsave(
                os.path.join(self.output_folder, file_name),
                images,
                duration=1000 / ANIMATION_FPS,
            )

        if save:
            with ThreadPoolExecutor(max_workers=num_threads) as executor:
                # Consume the iterator so exceptions raised inside worker threads
                # propagate instead of being silently swallowed.
                list(executor.map(plot_and_save, self.polyhedrons))
