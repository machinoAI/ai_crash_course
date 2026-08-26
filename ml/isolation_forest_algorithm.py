import numpy as np


class IsolationTree:

    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.left = None
        self.right = None
        self.feature = None
        self.split_value = None
        self.size = 0

    def fit(self, X, depth=0):

        self.size = len(X)

        # Stop conditions
        if (
            depth >= self.max_depth
            or len(X) <= 1
            or np.all(X == X[0])
        ):
            return self

        n_features = X.shape[1]

        # Randomly select a feature
        self.feature = np.random.randint(n_features)

        feature_values = X[:, self.feature]

        min_value = feature_values.min()
        max_value = feature_values.max()

        # If all values are identical, cannot split
        if min_value == max_value:
            return self

        # Random split between min and max
        self.split_value = np.random.uniform(
            min_value,
            max_value
        )

        # Partition data
        left_mask = feature_values < self.split_value
        right_mask = ~left_mask

        X_left = X[left_mask]
        X_right = X[right_mask]

        # Avoid empty child
        if len(X_left) == 0 or len(X_right) == 0:
            return self

        # Recursively build tree
        self.left = IsolationTree(self.max_depth)
        self.left.fit(X_left, depth + 1)

        self.right = IsolationTree(self.max_depth)
        self.right.fit(X_right, depth + 1)

        return self

    def path_length(self, x, depth=0):

        # Leaf node
        if self.left is None or self.right is None:
            return depth + self._c(self.size)

        # Go left
        if x[self.feature] < self.split_value:
            return self.left.path_length(x, depth + 1)

        # Go right
        return self.right.path_length(x, depth + 1)

    @staticmethod
    def _c(n):

        """
        Average path length adjustment for
        unsuccessful search in a Binary Search Tree.
        """

        if n <= 1:
            return 0

        if n == 2:
            return 1

        # Harmonic number approximation
        return (
            2 * (
                np.log(n - 1)
                + 0.5772156649
            )
            - 2 * (n - 1) / n
        )


class IsolationForest:

    def __init__(
        self,
        n_trees=100,
        sample_size=256,
        contamination=0.1
    ):
        self.n_trees = n_trees
        self.sample_size = sample_size
        self.contamination = contamination

        self.trees = []
        self.threshold = None

    def fit(self, X):

        X = np.asarray(X)

        self.trees = []

        # Build multiple random trees
        for _ in range(self.n_trees):

            # Random subsample
            size = min(
                self.sample_size,
                len(X)
            )

            indices = np.random.choice(
                len(X),
                size=size,
                replace=False
            )

            X_sample = X[indices]

            # Build tree
            tree = IsolationTree(
                max_depth=int(
                    np.ceil(np.log2(size))
                )
            )

            tree.fit(X_sample)

            self.trees.append(tree)

        # Calculate anomaly scores
        scores = self.anomaly_score(X)

        # Lower score = more normal
        # Higher score = more anomalous
        self.threshold = np.percentile(
            scores,
            100 * (1 - self.contamination)
        )

        return self

    def anomaly_score(self, X):

        X = np.asarray(X)

        scores = []

        for x in X:

            # Average path length
            path_lengths = [
                tree.path_length(x)
                for tree in self.trees
            ]

            avg_path_length = np.mean(
                path_lengths
            )

            # Normalization factor
            sample_size = self.trees[0].size

            c = IsolationTree._c(sample_size)

            if c == 0:
                score = 0.5
            else:
                score = 2 ** (
                    -avg_path_length / c
                )

            scores.append(score)

        return np.array(scores)

    def predict(self, X):

        scores = self.anomaly_score(X)

        # 1 = anomaly
        # 0 = normal
        return (
            scores >= self.threshold
        ).astype(int)



np.random.seed(42)

# Normal observations
normal = np.random.normal(
    loc=0,
    scale=1,
    size=(100, 2)
)

# Anomalies
anomalies = np.array([
    [8, 8],
    [9, 9],
    [-8, -9]
])

X = np.vstack([
    normal,
    anomalies
])


# Train Isolation Forest
model = IsolationForest(
    n_trees=100,
    sample_size=64,
    contamination=0.03
)

model.fit(X)


# Scores
scores = model.anomaly_score(X)

# Predictions
predictions = model.predict(X)

print("Anomaly scores:")
print(scores)

print("\nPredictions:")
print(predictions)

print("\nLast 3 predictions:")
print(predictions[-3:])