"""
1. What is FFN ?
    - Feed forward Network, is a small neural network that applied independently to every token.

    Inside FFN:
        - input (512) ->> Linear (512 ->> 2048) -->> GeLU ->> Linear (2048  ->> 512) ->> output.

    Mathematically:
        FFN(x) = W2( GeLU( W1x + b1 )) + b2

    Notice:
        Linear ->> Activation ->> Linear


2. What does Activation function do ?
    - Activation introduces non-Linearity to attention.
    - The activation function (GeLU, ReLU, SwiGLU) is a component inside the FFN.

3. Why is FFN called "Position-wise"?
    - The same FFN is applied independently to every token.
    - Tokens do not interact inside the FFN; interaction happens only in the attention layer.


4. Why is the MLP usually 4× the model dimension?
    - The MLP first expands the hidden dimension (typically 4×) to create a larger feature space for learning
        complex representations, then projects it back to the original model dimension.
        The 4× ratio is an empirically successful design choice that balances model capacity and computational cost.

5. Why do we need an MLP after Attention?
    - Attention gathers relevant information from other tokens, while the MLP transforms that information
        into richer, non-linear features. Without the MLP, the model would mostly mix information but
        have limited ability to learn complex patterns.


6. Why do modern models use SwiGLU instead of GeLU?
    Benefits:
    - Better quality
    - Better parameter efficiency


7. Why expand first and compress later?
    - Because learning in a higher-dimensional feature space allows the model to represent more
        complex feature interactions before projecting back to the model dimension.

"""