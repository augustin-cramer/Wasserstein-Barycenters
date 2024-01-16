import numpy as np


def ray_intersects_triangle(
    ray_origin: np.ndarray,
    ray_direction: np.ndarray,
    triangle_vertices: np.ndarray,
) -> np.ndarray:
    """Implement the Möller-Trumbore intersection algorithm.

    Args:
        ray_origin (np.ndarray): origins of the rays
        ray_direction (np.ndarray): direction of the rays
        triangle_vertices (np.ndarray): vertices of the triangle

    Returns:
        np.ndarray: boolean array indicating if the rays intersect the triangle
    """
    v0, v1, v2 = triangle_vertices
    e1 = v1 - v0
    e2 = v2 - v0
    h = np.cross(ray_direction, e2)
    a = np.dot(e1, h)

    mask_a = (a > -1e-6) & (a < 1e-6)
    f = np.where(mask_a, np.inf, 1.0 / a)

    s = ray_origin - v0
    u = f * np.dot(s, h)

    mask_u = (u < 0.0) | (u > 1.0)
    f = np.where(mask_u, np.inf, f)

    q = np.cross(s, e1)
    v = f * np.dot(q, ray_direction)

    mask_v = (v < 0.0) | ((u + v) > 1.0)
    f = np.where(mask_v, np.inf, f)

    t = f * np.dot(q, e2)

    return (t > 1e-6) & (t != np.inf)


def mesh_to_point_cloud(
    points: np.ndarray, vertices: np.ndarray, triangles: np.ndarray
) -> np.ndarray:
    """Check if the points are inside the mesh volume.

    Args:
        points (np.ndarray): coordinates of the points to check if thet are inside the mesh volume
        vertices (np.ndarray): vertices of the mesh
        triangles (np.ndarray): triangles of the mesh

    Returns:
        np.ndarray: boolean array indicating if the points are inside the mesh volume
    """

    # Check if the points are inside the mesh volume
    ray_origin = points
    ray_direction = np.ones((3,))  # Choose a ray direction

    inside_count = 0

    for triangle_indices in triangles:
        triangle_vertices = vertices[triangle_indices]
        intersections = ray_intersects_triangle(
            ray_origin, ray_direction, triangle_vertices
        )
        inside_count += intersections

    # If the number of intersections is odd, the points are inside the mesh volume
    return (inside_count % 2) == 1
