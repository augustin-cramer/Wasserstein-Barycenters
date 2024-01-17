import numpy as np
from .utils import gaussian_blur_kernel


def convolutional_barycenter_3d(
    initial_shapes: np.ndarray,
    alpha: np.ndarray,
    n_iter: int = 100,
    tol: float = 1e-5,
    sigma=1,
) -> np.ndarray:
    """Compute the convolutional barycenter of a set of shapes with given weights.

    Args:
        initial_shapes (np.ndarray): set of shapes
        alpha (np.ndarray): weight of each shape in the result
        n_iter (int, optional): maximum number of iterations. Defaults to 100.
        tol (float, optional): minimum change required for the iterations to keep on. Defaults to 1e-5.

    Returns:
        np.ndarray: the convolutional barycenter of the shapes with the given weights
    """
    n_shapes = initial_shapes.shape[0]
    shapes_shape = initial_shapes.shape[1:]

    # make sure that the weights sum to 1
    alpha = alpha / sum(alpha)

    area_weights = np.ones(shapes_shape, dtype=np.float64)
    kernel = lambda x: gaussian_blur_kernel(x, sigma=sigma, size=50 * sigma)

    v = np.ones(initial_shapes.shape, dtype=np.float64)
    w = np.ones(initial_shapes.shape, dtype=np.float64)
    d = np.full(initial_shapes.shape, 1e-100, dtype=np.float64)

    barycenter = np.ones(shapes_shape, dtype=np.float64)
    log_barycenter = np.log(barycenter)

    for _ in range(n_iter):

        # save the current barycenter to measure the change
        previous_barycenter = barycenter
        barycenter = np.ones(shapes_shape, dtype=np.float64)
        log_barycenter = np.log(barycenter)

        # compute the new barycenter
        for i in range(n_shapes):
            w[i] = initial_shapes[i] / kernel(area_weights * v[i])
            d[i] = v[i] * kernel(area_weights * w[i])
            d[d < 1e-100] = 1e-100
            log_barycenter += alpha[i] * np.log(d[i])
        barycenter = np.exp(log_barycenter)

        for i in range(n_shapes):
            v[i] = v[i] * barycenter / d[i]

        # measure the change
        change = np.sum(np.abs(previous_barycenter - barycenter))

        if change < tol or np.isnan(change):
            return barycenter

    return barycenter
