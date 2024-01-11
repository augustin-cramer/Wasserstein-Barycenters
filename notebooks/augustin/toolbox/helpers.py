import numpy as np

N = 100

# Function to calculate minimum of array
mmin = lambda x: np.min(x)

# Function to calculate maximum of array
mmax = lambda x: np.max(x)

# Function to normalize array
normalize = lambda h: h / np.sum(h)

# Function to set figure name
def setfigname(name):
    import matplotlib.pyplot as plt
    plt.gcf().canvas.set_window_title(name)

# Function to display histograms
delta = 0.1 / N**2
dispHist = lambda x: -np.log(x + delta)

# Function to display histograms for a cell array
dispCell = lambda H: [dispHist(h) for h in H]

# Function to calculate entropy
def Entropy(x):
    return -np.sum(x[x > 0] * np.log(x[x > 0]))

# Note: Replace N with the appropriate value before using the code
