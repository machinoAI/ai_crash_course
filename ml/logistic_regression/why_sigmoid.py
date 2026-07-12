"""
Logistic Regression uses sigmoid activation why not ReLU ?
    - Logistic predicts  probability as output and sigmoid function predicts the probability between (0,1).
    - which can be interpreted as p(y=1/x)

ReLU(x) = max(0, x)  --> [0,∞)
 - ReLU outputs are not probabilities because:
        - Values can exceed 1.
        - They do not sum to 1.
        - Negative inputs collapse to 0.


"""