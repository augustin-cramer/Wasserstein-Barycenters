from scipy.ndimage import convolve
import numpy as np


def gaussian_blur_kernel(distribution, sigma, size):
    # make a 1D Gaussian kernel
    x = np.arange(-np.ceil(size / 2), np.ceil(size / 2) + 1)
    gaussian_kernel = np.exp(-(x**2 / (2 * sigma**2)))
    gaussian_kernel = gaussian_kernel / np.sum(gaussian_kernel)

    # Filter each dimension with the 1D Gaussian kernels
    gaussian_kernel_x = gaussian_kernel.reshape((len(gaussian_kernel), 1, 1))
    gaussian_kernel_y = gaussian_kernel.reshape((1, len(gaussian_kernel), 1))
    gaussian_kernel_z = gaussian_kernel.reshape((1, 1, len(gaussian_kernel)))
    blurred_distribution = convolve(
        convolve(
            convolve(
                distribution, gaussian_kernel_x, mode="constant", cval=0.0
            ),
            gaussian_kernel_y,
            mode="constant",
            cval=0.0,
        ),
        gaussian_kernel_z,
        mode="constant",
        cval=0.0,
    )
    return blurred_distribution
