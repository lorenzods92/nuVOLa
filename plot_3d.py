'''Modulo per plottare in 3d la superficie'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.spatial import Delaunay


def plot_points(x: list, y: list, z: list, tri):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    print("Chiudere le figure per continuare il calcolo del volume...")

    # The triangles in parameter space determine which x, y, z points are
    # connected by an edge
    #ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
    ax.plot_trisurf(x, y, z, triangles=tri.simplices, cmap=plt.cm.coolwarm)
    ax.set_box_aspect([1,1,1])
    set_axes_equal(ax)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # displaying the title
    plt.title("3D")
    
    fig = plt.figure()
    plt.triplot(x, y, tri.simplices)
    plt.plot(x,  y, 'o')
    plt.xlabel('X') 
    plt.ylabel('Y') 
    plt.title("2D")
    plt.show()

    plt.show()


def set_axes_equal(ax: plt.Axes):
    """Set 3D plot axes to equal scale.

    Make axes of 3D plot have equal scale so that spheres appear as
    spheres and cubes as cubes.  Required since `ax.axis('equal')`
    and `ax.set_aspect('equal')` don't work on 3D.
    """
    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius)

def _set_axes_radius(ax, origin, radius):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])
