"""
R² is not perfect because it always increases (or stays the same) when you add more features,
 even if those features are completely useless.

 Adjusted R² adds a penalty for including more predictors.

Adjusted R² = 1 - (1-R²)(n-1)/(n-p-1)
where:

n = number of observations (samples)
p = number of predictor variables (features)

As p increases, the penalty increases.

A new feature will increase Adjusted R² only if it improves the model enough to justify its complexity.

"""

from sklearn.metrics import r2_score
import numpy as np

X = np.array([
    [1.2, 3],
    [2.5, 4],
    [3.8, 5],
    [5.1, 6]
])
y_true = [3, 5, 7, 9]
y_pred = [2.5, 5, 6, 8.5]

r2 = r2_score(y_true, y_pred)

n = len(y_true)          # Number of samples
p = X.shape[1]           # Number of features

adjusted_r2 = 1 - ((1 - r2) * (n - 1) / (n - p - 1))

print(adjusted_r2)