"""
    Linear Regression Assumes:
        y = wX + b + ϵ

    where ϵ is the noise/error.

    - We want to find w and b such that the error ϵ=y−y^ is as small as possible.
    - A natural choice is:
        MSE =1/n ∑ (yi−yi^)2

    - we square because:
        - positive errors don't cancel out
        - Large errors penalize more heavily
        - The function is smooth and differentiable
        - It leads to a convex optimization problem

    - MAE is not differentiable at 0:
        d|x| / dx  ; this makes optimization harder

    - MAE also convex
    - MAE is more robust to outliers



"""