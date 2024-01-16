import numpy as np

def rescale(array: np.ndarray, inf: float, sup: float) -> np.ndarray:
    """Rescale an array to a given interval.

    Args:
        array (np.ndarray): array to rescale
        inf (float): lower bound of the interval
        sup (float): upper bound of the interval

    Returns:
        np.ndarray: rescaled array
    """
    a = np.min(array)
    b = np.max(array)
    return (array - a) / (b - a) * (sup - inf) + inf