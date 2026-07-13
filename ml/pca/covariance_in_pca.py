"""
Covariance tell us how two features varies together.

- For two features X and Y,

    Cov(X,Y)= 1/n∑(xi- xbar)(y-y bar)

 - +ve covariance → both increase together.
 - -ve covariance → one increases while the other decreases.
 - 0 covariance → no linear relationship.


- PCA wants to find the directions with maximum variance. The covariance matrix captures:
    - Variance along each feature (diagonal elements).
    - Relationship between features (off-diagonal elements).

Example: Assume height and weight increases together , so covariance is high.
    - PCA will find principal component in this direction.


- PCA computes the covariance matrix because it contains both the variance of individual features
    and the relationships between features. PCA then finds the directions that capture the maximum variance.

"""

"""
When can PCA hurt performance ?
- PCA keeps features with high variance and removes those with low variance.
- When important features have low variance.
    Example: Fraud detection: Fraud patterns may have low variance but high predictive power.
        PCA may remove them.
- When the relationship is non-linear
- When interpretability matters
- When you already have very few features
    

"""