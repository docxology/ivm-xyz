import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import os
import sys
import imageio

class PolyhedronPlotter:
    def __init__(self, output_folder="images"):
        self.output_folder = output_folder

    def animate_polyhedron(self, vertices, faces, title="Polyhedron Animation", save=False, file_name="polyhedron.gif"):
        """
        Creates an animated GIF of a polyhedron given its vertices and faces by improving aesthetics and adding vertex labels.
        Optionally saves the animation as a GIF file.

        :param vertices: A list of tuples, each representing the x, y, z coordinates of a vertex.
        :param faces: A list of tuples, each representing indices of vertices that form a face.
        :param title: Title of the plot.
        :param save: Boolean indicating whether to save the plot as a GIF file.
        :param file_name: Name of the file to save the plot as. Defaults to 'polyhedron.gif'.
        """
        images = []
        for angle in range(0, 360, 2):
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')

            vtx = [[vertices[i] for i in face] for face in faces]

            poly = Poly3DCollection(vtx, facecolors='skyblue', linewidths=0.5, edgecolors='darkblue', alpha=0.5)
            ax.add_collection3d(poly)

            for i, (x, y, z) in enumerate(vertices):
                ax.scatter(x, y, z, color="darkred", s=100, edgecolors='black', zorder=5)
                ax.text(x, y, z, f'  V{i+1} ({x}, {y}, {z})', color='black')

            ax.set_xlabel('X Axis', fontsize=12)
            ax.set_ylabel('Y Axis', fontsize=12)
            ax.set_zlabel('Z Axis', fontsize=12)

            ax.set_xlim([min(v[0] for v in vertices)-1, max(v[0] for v in vertices)+1])
            ax.set_ylim([min(v[1] for v in vertices)-1, max(v[1] for v in vertices)+1])
            ax.set_zlim([min(v[2] for v in vertices)-1, max(v[2] for v in vertices)+1])

            ax.view_init(30, angle)
            plt.title(title, fontsize=14, fontweight='bold')
            plt.tight_layout()

            # Convert the plot to an image array
            fig.canvas.draw()
            image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
            image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

            images.append(image)

            plt.close(fig)

        kwargs_write = {'fps':1.0, 'quantizer':'nq'}
        imageio.mimsave(f"{self.output_folder}/{file_name}", images, fps=20)

if __name__ == "__main__":
    plotter = PolyhedronPlotter()
    polyhedron_list = [
        {
            "vertices": [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)],
            "faces": [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)],
            "title": "Tetrahedron 1",
            "file_name": "tetrahedron_1.gif"
        },
        {
            "vertices": [(0, 0, 0), (2, 0, 0), (0, 2, 0), (0, 0, 2)],
            "faces": [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)],
            "title": "Tetrahedron 2",
            "file_name": "tetrahedron_2.gif"
        }
    ]
    for polyhedron in polyhedron_list:
        plotter.animate_polyhedron(polyhedron["vertices"], polyhedron["faces"], title=polyhedron["title"], save=True, file_name=polyhedron["file_name"])
