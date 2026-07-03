import numpy as np

# x: List of float
# x_shifted = x-max(x)
# exp = np.exp(x_shifted)
# probs = exp/sum(exp)


def softmax(x):
    x = np.asarray(x, dtype=np.float64)
    x_shifted = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x_shifted)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


scores = np.array([2.0, 1.0, 0.1])
print("Scores:", scores)

probs = softmax(scores)
print("probs:", probs)
print("Sum of probs:",probs.sum())

# Batch input
batch = np.array([[1.0, 2.0, 3.0],
                   [1.0, 1.0, 1.0]])
print("Batch:",softmax(batch))


import math

def softmax(x):
    m = max(x)
    exps = [math.exp(i - m) for i in x]
    total = sum(exps)
    return [e / total for e in exps]