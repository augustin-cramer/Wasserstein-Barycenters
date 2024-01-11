import numpy as np

def apply_3d_func(f, x):
    
    if x.ndim==1:
        x = x.reshape(1, -1)
        
    N = int(np.round((x.shape[1])**(1/3)))
    P = x.shape[0]
    
    resh = lambda x: np.reshape(x, (N, N, N))
    flat = lambda x: x.flatten()

    y = np.zeros_like(x)
    for i in range(P):
        y[i, :] = flat(f(resh(x[i, :])))

    return y