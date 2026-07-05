# ReLU (Rectified Linear Unit) is an activation function that keeps positive values and converts negative values to zero.
# ReLU(x)=max(0,x)  If x>0 → output = x  If x≤0 → output = 0


import torch
from torch.ao.nn.quantized.functional import leaky_relu

x = torch.tensor([3.0, -2.0, 5., 7., -9.0])
y = torch.relu(x)


print("ReLU:", y)



#Leaky ReLU: is a variant of ReLU that allows a small negative output instead of making all negative values zero.
# This prevents neurons from becoming permanently inactive.
# f(x) = { x if x> 0 , αx if x<=0, where α = small constant (typically 0.01)
import torch.nn as nn

leaky_relu1 = nn.LeakyReLU(negative_slope=0.01)

print("Leaky ReLU:", leaky_relu1(x))
