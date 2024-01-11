import numpy as np

def convolutional_barycenter(mus, alphas, area_weights, kernel, kernel_transpose, entropy_limit):
    n_iter = 1500
    tol = 1e-4
    v = np.ones(mus.shape)
    alphas = alphas / sum(alphas)
    if area_weights is None:
        area_weights = np.ones(mus.shape[1])
    if kernel_transpose is None:
        kernel_transpose = kernel
    barycenter = np.ones(mus.shape[1])
    for i in range(n_iter):
        old_barycenter = barycenter
        w = mus / (kernel_transpose(v * area_weights))
        d = v * kernel(w * area_weights)
        d[d<1e-100] = 1e-100
        barycenter = np.exp(np.sum(alphas.reshape(-1, 1) * np.log(d), axis=0))
        #entropy = -np.sum(area_weights*(barycenter*np.log(barycenter)))
        v = v*barycenter/d
        change = np.sum(np.abs(old_barycenter-barycenter) * area_weights)
        if i > 2 and change < tol :
            return barycenter
    return barycenter