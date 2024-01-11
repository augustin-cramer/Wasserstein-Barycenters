import numpy as np

def rescale(array, inf, sup):
    """
    Rescale an array to a given interval.
    """
    a = np.min(array)
    b = np.max(array)
    return (array - a) / (b - a) * (sup - inf) + inf