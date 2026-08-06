import numpy as np

d_model = 8      # Embedding dimension
max_len = 5      # Number of token positions

PE = np.zeros((max_len, d_model))

for pos in range(max_len):
    for i in range(0, d_model, 2):
        angle = pos / (10000 ** (i / d_model))

        PE[pos, i] = np.sin(angle)

        if i + 1 < d_model:
            PE[pos, i + 1] = np.cos(angle)

print(PE)




#
# import torch
#
# d_model = 512
# max_len = 100
#
# position = torch.arange(max_len).unsqueeze(1)
#
# div_term = torch.exp(
#     torch.arange(0, d_model, 2) *
#     (-torch.log(torch.tensor(10000.0)) / d_model)
# )
#
# PE = torch.zeros(max_len, d_model)
#
# PE[:, 0::2] = torch.sin(position * div_term)
# PE[:, 1::2] = torch.cos(position * div_term)
#
# print(PE)