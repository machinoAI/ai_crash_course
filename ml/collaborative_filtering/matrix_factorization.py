"""
Implement matrix factorization (similar to SVD) for collaborative filtering.
Given a sparse user-item rating matrix, decompose it into user and item latent factor matrices.


"""

import numpy as np

def matrix_factorization(
    R,
    k=2,
    learning_rate=0.01,
    regularization=0.02,
    epochs=200
):
    """
    Matrix Factorization using Gradient Descent.

    R:
        User-item rating matrix.
        0 means the rating is missing.

    k:
        Number of latent factors.

    learning_rate:
        Step size for gradient descent.

    regularization:
        L2 regularization strength.

    epochs:
        Number of training iterations.

    Returns:
        P: User-factor matrix
        Q: Item-factor matrix
    """

    num_users, num_items = R.shape

    P = np.random.normal(
        scale=1.0 / k,
        size=(num_users, k)
    )

    Q = np.random.normal(
        scale=1.0 / k,
        size=(num_items, k)
    )

    observed = np.argwhere(R > 0)

    # --------------------------------------------------
    #  Gradient Descent
    # --------------------------------------------------

    for epoch in range(epochs):

        total_error = 0

        for u, i in observed:

            prediction = np.dot(P[u], Q[i])

            error = R[u, i] - prediction
            total_error += error ** 2


            P_u = P[u].copy()
            Q_i = Q[i].copy()

            # ------------------------------------------
            # Update user vector P[u] & Q[i]
            # ------------------------------------------

            P[u] += learning_rate * (
                error * Q_i
                - regularization * P_u
            )

            Q[i] += learning_rate * (
                error * P_u
                - regularization * Q_i
            )


        if epoch % 500 == 0:
            print(
                f"Epoch {epoch}, "
                f"Error = {total_error:.4f}"
            )

    return P, Q


R = np.array([
    [5, 3, 0],
    [4, 0, 2],
    [0, 5, 4]
], dtype=float)

k = 2

P, Q = matrix_factorization(
    R,
    k=k,
    learning_rate=0.01,
    regularization=0.02,
    epochs=5000
)


# ======================================================
# Reconstruct the rating matrix
# ======================================================

R_predicted = P @ Q.T

print("\nUser-factor matrix P:")
print(P)

print("\nItem-factor matrix Q:")
print(Q)

print("\nPredicted rating matrix:")
print(R_predicted)

print("\nOriginal rating matrix:")
print(R)