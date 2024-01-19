import numpy as np
import pyvista as pv


def count_neighbours(cloud):
    """
    computes the number of neighbours of each point in the cloud
    cloud is assumed to be of shape (N,N,N)
    """
    cloud = cloud.astype(np.int8)
    N = cloud.shape[0]
    neighbours = np.zeros_like(cloud, dtype=np.int8)
    neighbours += np.concatenate(
        [np.zeros((1, N, N), dtype=np.int8), cloud[:-1, :, :]], axis=0
    )
    neighbours += np.concatenate(
        [cloud[1:, :, :], np.zeros((1, N, N), dtype=np.int8)], axis=0
    )
    neighbours += np.concatenate(
        [np.zeros((N, 1, N), dtype=np.int8), cloud[:, :-1, :]], axis=1
    )
    neighbours += np.concatenate(
        [cloud[:, 1:, :], np.zeros((N, 1, N), dtype=np.int8)], axis=1
    )
    neighbours += np.concatenate(
        [np.zeros((N, N, 1), dtype=np.int8), cloud[:, :, :-1]], axis=2
    )
    neighbours += np.concatenate(
        [cloud[:, :, 1:], np.zeros((N, N, 1), dtype=np.int8)], axis=2
    )
    return neighbours


def get_surface_points(cloud):
    """
    From a point cloud of shape (N,N,N), returns cloud w/o points inside, meaning ones with 6 neighbours
    """
    surface = cloud.copy()
    neighbours = count_neighbours(cloud)
    surface[neighbours == 6] = False
    return surface


def get_mesh(cloud, space):
    """
    From a point cloud of shape (N,N,N) and a space of shape (N,N,N,3), returns a mesh
    """
    points_inside = cloud.flatten()
    x = space[points_inside][:, 0]
    y = space[points_inside][:, 1]
    z = space[points_inside][:, 2]
    points = np.array([x, y, z]).T
    point_cloud = pv.PolyData(points)
    mesh = point_cloud.reconstruct_surface(progress_bar=True, nbr_sz=10)

    vertices = mesh.points
    faces = mesh.faces.reshape(-1, 4)[:, 1:]

    return vertices, faces


def point_cloud_to_mesh(cloud, space):
    """
    From a point cloud of shape (N,N,N) and a space of shape (N,N,N,3), returns a mesh
    """
    surface = get_surface_points(cloud)
    vertices, faces = get_mesh(surface, space)
    return vertices, faces
