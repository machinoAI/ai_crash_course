"""
You have 10 million rows and 100 features. How would you train linear regression efficiently?
- Don't use the Normal Equation:
    Because: Matrix inversion is computationally expensive O(n*n*n)
    w = (X^T * X)^-1 X^T*y

- Use gradient descent:
    - options:
        - Batch Gradient
        - Mini-batch Gradient descent
        - Stochastic Gradient descent

- update rule:
    w = w − η(∂L/∂w)

- Scale the features:
    - Standardization
    - Min-max scaling

- Use distributed Training:
    For very large datasets:
        - Spark MLib
        - XGBoost Distributed
        - Dask
        - GPUs
- Use sparse metrics if possible:
    - For Text or one-hot- encoding avoid storing zeros .


"""