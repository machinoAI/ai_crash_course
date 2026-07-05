"""
A confidence interval is a range of plausible values for an unknown population parameter
(such as a regression coefficient), calculated from sample data.

Example:
        In house prediction, lets we got area coefficient is 250.
        But this is not fix, if you analyze a different subsets of data it might be 265 or 240.

        So, instead of saying exact range we say a range like 230-270
        This is called confidence interval.

Example 2:
Coefficient = 250

95% Confidence Interval

[220, 280]

Meaning of 95%: If we repeatedly collected new samples and constructed a 95% confidence interval
 from each one, then about 95% of those intervals would contain the true parameter.

Note: The true parameter is fixed. It's the interval that changes from sample to sample.


Confidence Interval= β^ +_(critical value ) * SE


β^ = estimated coefficient
SE = standard error
"""

import statsmodels.api as sm
import pandas as pd

X = pd.DataFrame({
    "Area": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800] })

y = [50, 60, 75, 90, 100, 110, 125, 140]

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()    # OLS = Ordinary Least Squares equivalent to LinearRegression in sk learn

print(model.conf_int())
