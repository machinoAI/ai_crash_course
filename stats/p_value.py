"""
A p-value is used in hypothesis testing to determine whether a feature is statistically significant.

A p-value is the probability of observing the estimated coefficient assuming the null hypothesis is true.
It helps us determine whether the observed relationship between a feature and the target is likely
 to be real or simply due to random sampling.

Exampl 1:
If the true relationship between Area and House Price were actually zero (β = 0),
then there is only a 1% chance of observing an estimated coefficient of 250 (or more extreme)
 purely because of random sampling.

 Example 2:
If payment mode actually had no effect on refunds (β = 0), there is only a 3% chance of observing
an estimated coefficient of 0.60 (or more extreme) purely due to random sampling.

Flow:

Train Regression Model
        ↓
Estimate coefficient (β̂)
        ↓
Compute Standard Error (SE)
        ↓
Compute t-statistic = β̂ / SE
        ↓
Use t-distribution
        ↓
Obtain p-value
        ↓
If p < 0.05
    Reject H₀
Else
    Fail to reject H₀
"""
import statsmodels.api as sm
import pandas as pd

X = pd.DataFrame({
    "Area": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800] })

y = [50, 60, 75, 90, 100, 110, 125, 140]

X = sm.add_constant(X)

print(X)
model = sm.OLS(y, X).fit()    # OLS = Ordinary Least Squares equivalent to LinearRegression in sk learn

print(model.summary())



# List of methods of model:

"""
| Method / Attribute     | Purpose                        |
| ---------------------- | ------------------------------ |
| `model.summary()`      | Complete regression report     |
| `model.conf_int()`     | Confidence intervals           |
| `model.predict(X_new)` | Predict new values             |
| `model.params`         | Regression coefficients        |
| `model.pvalues`        | p-values of coefficients       |
| `model.rsquared`       | R²                             |
| `model.rsquared_adj`   | Adjusted R²                    |
| `model.fvalue`         | F-statistic                    |
| `model.f_pvalue`       | p-value of F-statistic         |
| `model.resid`          | Residuals (Actual − Predicted) |
| `model.fittedvalues`   | Predicted values               |

"""