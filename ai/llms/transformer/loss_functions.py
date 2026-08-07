"""
1. Why do we need a loss?
    - A loss function is a mathematical function that measures how far the model's prediction is
        from the correct answer. Lower loss means better predictions.

2. What is Cross-Entropy Formula ?

    - If the correct token has probability p,
            then
                Loss= −log(p)

    Notice:
        - Cross-Entropy only cares about the probability assigned to the correct token.

    Example:
            −log(0.9)=0.105

3. Why use the logarithm?
    | Probability | Loss = 1-p | Loss = -log(p) |
    | ----------- | ---------: | -------------: |
    | 0.9         |        0.1 |          0.105 |
    | 0.5         |        0.5 |          0.693 |
    | 0.1         |        0.9 |          2.303 |
    | 0.01        |       0.99 |          4.605 |


    - When the model is very wrong, Cross-Entropy penalizes it much more strongly than a simple linear loss.
    - This produces larger gradients, helping the model correct large mistakes more aggressively.

4. What is Cross-Entropy Loss?
    - Cross-Entropy Loss measures how different the model's predicted probability distribution is from the true distribution.
    - For the correct class, the loss is simply −log(p), where p is the predicted probability of the correct token.

5. Why don't we use MSE instead of Cross-Entropy?
    - MSE is designed for regression tasks and measures the squared error between continuous values.
    - Next-token prediction is a classification problem, where the model must assign probabilities over the vocabulary.
    - Cross-Entropy directly optimizes these probability distributions, penalizes confident wrong predictions
        much more strongly, and provides more informative gradients for training.

"""