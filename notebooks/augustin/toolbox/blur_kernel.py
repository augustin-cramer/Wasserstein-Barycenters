from scipy.ndimage import convolve
import numpy as np

def imgaussian(I, sigma, siz=None):
    if siz is None:
        siz = int(sigma * 6)
    # make a 1D Gaussian kernel
    x = np.arange(-np.ceil(siz/2), np.ceil(siz/2) + 1)
    H = np.exp(-(x**2 / (2 * sigma**2)))
    H = H / np.sum(H)
    
    # Filter each dimension with the 1D Gaussian kernels
    Hx = H.reshape((len(H), 1, 1))
    Hy = H.reshape((1, len(H), 1))
    Hz = H.reshape((1, 1, len(H)))
    I = convolve(
            convolve(
                convolve(I, Hx, mode='constant', cval=0.0),
            Hy, mode='constant', cval=0.0),
        Hz, mode='constant', cval=0.0)
    return I