
"""
R² measures how much of the variance in the target variable is explained by the model.

    R²  =  variance explained / total variance

    or

    R² = 1 - (Residual sum squares (Unexplained Variance)/ Total sum squares (total variance))

y actual    = [3,4,5,6,7]
y predicted = [2,3.5, 5 , 5.5, 6]
y mean = 25/5 = 5

Residual sum = sum((actual1 - predicted1)^2)+ ....)
Total sum = sum((actual1 - mean)^2+ ....)

The model explains 92% of the variability (variance) in the target variable.
The remaining 8% of the variability is due to factors not captured by the model or prediction errors.
"""

from sklearn.metrics import r2_score

y_true = [3, 5, 7, 9]
y_pred = [2.5, 5, 6, 8.5]

r2 = r2_score(y_true, y_pred)
print(r2)


import torch

y_true = torch.tensor([3., 5., 7., 9.])
y_pred = torch.tensor([2.5, 5., 6., 8.5])

ss_res = torch.sum((y_true - y_pred) ** 2)
ss_tot = torch.sum((y_true - torch.mean(y_true)) ** 2)

r2 = 1 - (ss_res / ss_tot)

print(r2.item())

