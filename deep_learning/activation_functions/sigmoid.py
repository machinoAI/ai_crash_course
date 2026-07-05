import torch

def sigmoid(x):
    return torch.sigmoid(x)

x = torch.tensor([3., -2., 5., 7., -9.])

print(sigmoid(x))


import numpy as np

def sigmoid(x):
    """
    Sigmoid activation: f(x) = 1 / (1 + e^-x)
    """
    return 1 / (1 + np.exp(-x))

x = torch.tensor([3., -2., 5., 7., -9.])

print(sigmoid(x))