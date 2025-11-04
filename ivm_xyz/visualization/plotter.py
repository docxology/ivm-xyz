"""
Visualization tools for polyhedra using matplotlib.

This module provides functionality to plot and animate polyhedral structures.
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import os
from concurrent.futures import ThreadPoolExecutor

# Maximum number of threads for parallel processing
MAX_THREADS = 8


class PolyhedronPlotter:
    """
    Class for plotting and animating polyhedra.
    
    Supports both static plots and animated GIFs of 3D polyhedral structures.
    """
    
    def __init__(self, output_folder="images"):
        """
        Initialize the plotter.
        
        Args:
            output_folder: Directory to save output images/animations
        """
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        self.polyhedrons = []  # List to store polyhedron dictionaries

    def add_polyhedron(self, vertices, faces, title, file_name):
        """
        Add a polyhedron to the list for animation.
        
        Args:
            vertices: List of tuples, each representing (x, y, z) coordinates
            faces: List of tuples, each representing vertex indices forming a face
            title: Title of the polyhedron
            file_name: Name of the file to save the animation as
        """
        polyhedron = {
            "vertices": vertices,
            "faces": faces,
            "title": title,
            "file_name": file_name
        }
        self.polyhedrons.append(polyhedron)

    def plot_polyhedron(self, vertices, faces, title="Polyhedron Visualization",
                       save=False, file_name="polyhedron.png"):
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
        ax = fig.add_subplot(111, projection='3d')

        vtx = [[vertices[i] for i in face] for face in faces]

        poly = Poly3DCollection(vtx, facecolors='skyblue', linewidths=0.5,
                               edgecolors='darkblue', alpha=0.5)
        ax.add_collection3d(poly)

        for i, (x, y, z) in enumerate(vertices):
            ax.scatter(x, y, z, color="darkred", s=100, edgecolors='black', zorder=5)
            ax.text(x, y, z, f'  V{i+1} ({x}, {y}, {z})', color='black')

        ax.set_xlabel('X Axis', fontsize=12)
        ax.set_ylabel('Y Axis', fontsize=12)
        ax.set_zlabel('Z Axis', fontsize=12)

        ax.set_xlim([min(v[0] for v in vertices) - 1, max(v[0] for v in vertices) + 1])
        ax.set_ylim([min(v[1] for v in vertices) - 1, max(v[1] for v in vertices) + 1])
        ax.set_zlim([min(v[2] for v in vertices) - 1, max(v[2] for v in vertices) + 1])

        plt.title(title, fontsize=14, fontweight='bold')
        plt.tight_layout()

        if save:
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)
            plt.savefig(os.path.join(self.output_folder, file_name))
        else:
            plt.show()
        plt.close(fig)

    def animate_polyhedron(self, save=False):
        """
        Create animated GIFs of polyhedra in the list.
        
        Uses parallel processing across multiple CPU threads (up to MAX_THREADS).
        
        Args:
            save: Boolean indicating whether to save the animations
        """
        try:
            import imageio
        except ImportError:
            raise ImportError("imageio is required for animation. Install with: pip install imageio")
        
        num_threads = min(len(self.polyhedrons), MAX_THREADS)

        def plot_and_save(polyhedron):
            vertices = polyhedron["vertices"]
            faces = polyhedron["faces"]
            title = polyhedron["title"]
            file_name = polyhedron["file_name"]

            images = []
            for angle in range(0, 360, 2):
                fig = plt.figure(figsize=(10, 8))
                ax = fig.add_subplot(111, projection='3d')

                vtx = [[vertices[i] for i in face] for face in faces]

                poly = Poly3DCollection(vtx, facecolors='skyblue', linewidths=0.5,
                                      edgecolors='darkblue', alpha=0.5)
                ax.add_collection3d(poly)

                for i, (x, y, z) in enumerate(vertices):
                    ax.scatter(x, y, z, color="darkred", s=100, edgecolors='black', zorder=5)
                    ax.text(x, y, z, f'V{i+1} ({x}, {y}, {z})', color='black')

                ax.set_xlabel('X Axis', fontsize=12)
                ax.set_ylabel('Y Axis', fontsize=12)
                ax.set_zlabel('Z Axis', fontsize=12)

                ax.set_xlim([min(v[0] for v in vertices) - 1, max(v[0] for v in vertices) + 1])
                ax.set_ylim([min(v[1] for v in vertices) - 1, max(v[1] for v in vertices) + 1])
                ax.set_zlim([min(v[2] for v in vertices) - 1, max(v[2] for v in vertices) + 1])

                ax.view_init(30, angle)
                plt.title(title, fontsize=14, fontweight='bold')
                plt.tight_layout()

                # Convert plot to image array
                fig.canvas.draw()
                buf = fig.canvas.tostring_rgb()
                image = np.frombuffer(buf, dtype='uint8')
                image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

                images.append(image)
                plt.close(fig)

            imageio.mimsave(os.path.join(self.output_folder, file_name), images, fps=20)

        if save:
            with ThreadPoolExecutor(max_workers=num_threads) as executor:
                executor.map(plot_and_save, self.polyhedrons)

