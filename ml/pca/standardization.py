"""
Why do we standardize features in PCA ?
- PCA is based on variance.
- If features have two different scales, features with larger value dominates the covariance matrix.

- Let's say we have two features:
    - Salary -> 10k to 100k
    - Age- 18 to 100 years

    - Without standardization PCA will focus mostly only on salary and ignore age.
    - Standardization:
        x std = (x-μ)/σ

    where μ = mean = 0
    and σ = variance = 1


"""