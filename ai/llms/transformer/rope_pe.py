import numpy as np

def rope_rotate(x, position):
    """
    x: even-dimensional vector
    position: token position
    """

    d = len(x)
    out = np.zeros_like(x, dtype=float)

    for i in range(0, d, 2):

        theta = position / (10000 ** (i / d))

        cos = np.cos(theta)
        sin = np.sin(theta)

        x1 = x[i]
        x2 = x[i+1]

        out[i]   = x1*cos - x2*sin
        out[i+1] = x1*sin + x2*cos

    return out


q = np.array([2,3,4,5],dtype=float)

print(rope_rotate(q, position=1))

#
# import torch
#
# def rotate_half(x):
#     x1 = x[..., ::2]
#     x2 = x[..., 1::2]
#
#     return torch.stack((-x2, x1), dim=-1).flatten(-2)
#
#
# def apply_rope(q, cos, sin):
#     return q * cos + rotate_half(q) * sin