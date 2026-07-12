"""
When does logistic regression fail?
- Non-linear decision boundary
- Logistic Regression assumes: If the actual boundary is curved or complex, logistic regression underfits.
    log(p/1−p)=wx+b

- Highly correlated features: Multicollinearity makes coefficients unstable and difficult to interpret.
- Too many outliers: Outliers can significantly shift the decision boundary.
- Severe class imbalance: For example, 99:1 fraud detection. The model may predict only the majority class unless we use weighted loss or sampling.
- Complex feature interactions: Logistic regression cannot automatically learn feature interactions like XGBoost or deep neural networks.


-Logistic regression fails when the data is highly non-linear, heavily imbalanced, or contains
complex feature interactions because it assumes a linear relationship between features and log-odds.
"""