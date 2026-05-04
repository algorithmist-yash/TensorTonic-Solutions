import numpy as np

def sigmoid(z):
    """
    Vectorized sigmoid function.
    """
    z=np.array(z)
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))