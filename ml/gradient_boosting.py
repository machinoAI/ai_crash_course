import numpy as np
from sklearn.tree import DecisionTreeRegressor


def one_gradient_boosting_iteration(
    X,
    y,
    current_prediction,
    learning_rate=0.1,
    loss="squared_error"
):
    """
    Perform ONE iteration of Gradient Boosting.

    X                  : Features
    y                  : Actual target
    current_prediction : Current model predictions
    learning_rate      : Shrinkage parameter

    Returns:
        tree
        updated_prediction
    """

    # --------------------------------------------------
    # 1. Calculate negative gradient
    # --------------------------------------------------

    if loss == "squared_error":

        # Loss = 1/2 * (y - prediction)^2
        #
        # Negative gradient = y - prediction
        residual = y - current_prediction

    else:
        raise ValueError(
            "Only squared_error is implemented"
        )

    # --------------------------------------------------
    # 2. Fit a decision tree to the residuals
    # --------------------------------------------------

    tree = DecisionTreeRegressor(
        max_depth=2,
        random_state=42
    )

    tree.fit(X, residual)

    # --------------------------------------------------
    # 3. Tree predicts the residual correction
    # --------------------------------------------------

    correction = tree.predict(X)

    # --------------------------------------------------
    # 4. Update current prediction
    # --------------------------------------------------

    updated_prediction = (
        current_prediction
        + learning_rate * correction
    )

    return tree, updated_prediction


X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

y = np.array([
    2,
    4,
    6,
    8,
    10
], dtype=float)


# Initial prediction
current_prediction = np.zeros(len(y))


tree, new_prediction = one_gradient_boosting_iteration(
    X,
    y,
    current_prediction,
    learning_rate=0.1
)

print("Actual:", y)

print("Initial prediction:")
print(current_prediction)

print("Updated prediction:")
print(new_prediction)