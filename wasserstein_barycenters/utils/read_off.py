import numpy as np


def read_off(filename: str) -> (np.ndarray, np.ndarray):
    """Reads an OFF file.

    Args:
        filename (str): file name

    Returns:
        (np.ndarray, np.ndarray): vertices, faces
    """
    with open(filename) as f:
        if "OFF" != f.readline().strip():
            raise ("Not a valid OFF header")
        n_verts, n_faces, _ = tuple(
            [int(s) for s in " ".join(f.readline().split()).strip().split(" ")]
        )
        vertices = [
            [
                float(s)
                for s in " ".join(f.readline().split()).strip().split(" ")
            ]
            for _ in range(n_verts)
        ]
        faces = [
            [
                int(s)
                for s in " ".join(f.readline().split()).strip().split(" ")
            ][1:]
            for _ in range(n_faces)
        ]
    return np.array(vertices), np.array(faces)
