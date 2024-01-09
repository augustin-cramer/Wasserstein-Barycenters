import numpy as np
from scipy.sparse import coo_matrix

def is_point_inside_mesh(point, vertices, triangles):
    def ray_intersects_triangle(ray_origin, ray_direction, triangle_vertices):
        # Möller–Trumbore intersection algorithm
        v0, v1, v2 = triangle_vertices
        e1 = v1 - v0
        e2 = v2 - v0
        h = np.cross(ray_direction, e2)
        a = np.dot(e1, h)

        if a > -1e-6 and a < 1e-6:
            return False

        f = 1.0 / a
        s = ray_origin - v0
        u = f * np.dot(s, h)

        if u < 0.0 or u > 1.0:
            return False

        q = np.cross(s, e1)
        v = f * np.dot(ray_direction, q)

        if v < 0.0 or u + v > 1.0:
            return False

        t = f * np.dot(e2, q)

        return t > 1e-6

    # Check if the point is inside the mesh volume
    ray_origin = point
    ray_direction = np.array([1, 0, 0])  # Choose a ray direction (e.g., along the positive x-axis)

    inside_count = 0

    for triangle_indices in triangles:
        triangle_vertices = vertices[triangle_indices]
        if ray_intersects_triangle(ray_origin, ray_direction, triangle_vertices):
            inside_count += 1

    # If the number of intersections is odd, the point is inside the mesh volume
    return inside_count % 2 == 1


def calculate_mesh_volume(vertices, triangles):
    def signed_volume_of_triangle(v1, v2, v3):
        return np.dot(v1, np.cross(v2, v3)) / 6.0

    volume = 0.0

    for triangle_indices in triangles:
        triangle_vertices = vertices[triangle_indices]
        v1, v2, v3 = triangle_vertices
        volume += signed_volume_of_triangle(v1, v2, v3)

    return abs(volume)


def cotangent_laplacian(vertices, triangles):
    """
    Compute the cotangent Laplacian matrix for a closed triangular mesh.

    Parameters:
    - vertices: Numpy array with the coordinates of the vertices.
    - triangles: Numpy array with the triangles' edge indices.

    Returns:
    - Laplacian matrix.
    """
    num_vertices = vertices.shape[0]
    laplacian_data = []
    row_indices = []
    col_indices = []

    # Iterate over each triangle
    for triangle in triangles:
        # Extract vertex indices for the triangle
        i, j, k = triangle

        # Calculate edge vectors
        v1 = vertices[j] - vertices[i]
        v2 = vertices[k] - vertices[i]

        # Calculate cotangent of the angles
        cot_alpha = np.dot(-v1, v2) / np.linalg.norm(np.cross(v1, v2))
        cot_beta = np.dot(v1, -v2) / np.linalg.norm(np.cross(v1, v2))
        cot_gamma = np.dot(v2, -v1) / np.linalg.norm(np.cross(v1, v2))

        # Update Laplacian matrix entries
        laplacian_data.extend([-cot_alpha, -cot_beta, cot_alpha + cot_beta, -cot_alpha, cot_beta, cot_alpha])
        row_indices.extend([i, j, k, i, j, k])
        col_indices.extend([j, k, i, k, i, j])

    # Construct the Laplacian matrix in COO format
    laplacian_matrix = coo_matrix((laplacian_data, (row_indices, col_indices)), shape=(num_vertices, num_vertices))

    # Convert to CSR format for efficient computations
    laplacian_matrix = laplacian_matrix.tocsr()

    # Compute the diagonal matrix D
    diagonal_matrix = np.diag(np.array(laplacian_matrix.sum(axis=1)).flatten())

    # Compute the cotangent Laplacian matrix L = D - Laplacian
    cot_laplacian_matrix = diagonal_matrix - laplacian_matrix

    return cot_laplacian_matrix

def vertex_triangle_areas(vertices, triangles):
    """
    Calculate the sum of the areas of triangles for which each vertex is a part.

    Parameters:
    - vertices: Numpy array with the coordinates of the vertices.
    - triangles: Numpy array with the triangles' edge indices.

    Returns:
    - Numpy array containing the sum of the areas for each vertex.
    """
    num_vertices = vertices.shape[0]
    areas = np.zeros(num_vertices)

    # Iterate over each triangle
    for triangle in triangles:
        # Extract vertex indices for the triangle
        i, j, k = triangle

        # Calculate vectors representing two edges of the triangle
        v1 = vertices[j] - vertices[i]
        v2 = vertices[k] - vertices[i]

        # Calculate the area of the triangle using cross product
        area = 0.5 * np.linalg.norm(np.cross(v1, v2))

        # Accumulate the area for each vertex
        areas[i] += area
        areas[j] += area
        areas[k] += area

    return np.diag(areas)