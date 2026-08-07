"""
1. Why don't we directly apply Softmax to the 4 × 512 hidden state?
    Why do we first project it to 4 × 50000 using the LM Head?

    - The hidden state (4 × 512) is a contextual representation, not a prediction.
    - To predict the next token, the model must assign a score to every token in the vocabulary.
    - The LM Head projects the 512-dimensional hidden state into a 50,000-dimensional logit vector,
      where each value represents the score of one vocabulary token.
    - Softmax then converts these scores into probabilities, and the token with the highest probability is selected.


2. What is Logit ?

    - A logit is the raw score assigned by the model to each vocabulary token before Softmax.
    - Softmax later converts scores into probabilities.

    - Analogy: You are judging a candidate , you give a score not probability. Logit is score not probability.
        - It can be negative. Which indicates less preferred.

    - Logits can be:
        -∞ to +∞

    - Logits = H×W_LM = 512 x 50K (vocabulary counts)


3. Why not put Softmax inside the model?

    - Because Cross-Entropy Loss in frameworks like PyTorch expects raw logits.
    - CrossEntropyLoss() already has
        LogSoftmax + Negative Log Likelihood

    This is similar to doing : Softmax ->> Cross entropy

    - But it is more numerical
    - faster
    - Avoids overflow when logits are very large.


    So during training:
            Model

            ↓

            Logits

            ↓

            CrossEntropyLoss

    No explicit Softmax is needed.

    - But at the inference time we need softmax.
    - If we had moved softmax inside the model it would have double softmax for training.

    - Another reason:
        - Researchers often wants access to logits for
            - Temperature Scaling
            - Calibration
            - Distillation
            - RLHF
            - DPO
            - Log Probability Computation



"""