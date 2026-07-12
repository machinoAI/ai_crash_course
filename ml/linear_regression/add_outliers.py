"""
 What happens when we add an outliers ?

 - Adding outliers significantly affect the LR
 - MSE:
    = 1/n ∑(y−y^)2

    - Squaring the error amplifies large deviations.
    - LR: Highly sensitive; The regression line shift towards the outlier.
    - Ridge(L2):Still sensitive and coefficients are shrunk
    - Lasso(L1):sensitive too ,coefficient may become zero
    - MAE : More robust because error are not squared.

"""