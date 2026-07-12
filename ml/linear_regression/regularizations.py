"""
Ridge(L2):
    - Penalizes loss with λ∑wi^2
    - L2 penalty is smooth
    - L2 doesn't produce sparsity:coefficients shrinks towards zero but never makes them exactly zero

Lasso:
    - Penalizes loss with λ∑∣wi|
    - L1 penalty has sharp corners at 0:
    - L1 produce sparsity: During optimization, many coefficients hit exactly zero, effectively selecting features.

Elastic Net:
    - Lasso struggles when features are highly correlated:
        - Age in years.
        - Age in months.

    - Lasso may arbitrarily keep one and discard the other.

        = λ1∑∣wi∣ + λ2∑wi^2

    - combines feature selection (L1) with coefficient stability (L2).

- A data sets with multicollinearity uses elastic net.
"""