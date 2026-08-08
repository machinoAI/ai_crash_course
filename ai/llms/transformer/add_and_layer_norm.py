"""
- Transformer Architecture:
    - Input tokens -->> Embeddings -->> Positional Encoding/RoPE ->>
        -->>Transformer Block
            - Multi-head Attention
            - Add & LayerNorm
            - FFN
            - Add & LayerNorm
        -->> Language Model Head -->> SoftMax


0. Where to apply to add & LayerNorm ?
    - After each sub-players we apply: Residual connections(Add) and LayerNorm.


1. What is Add  in 'add & LayerNorm' in transformer ?

    -The "Add" is simply a Residual Connection (Skip Connection).

    - suppose input embedding is: x
        After self attention:
            Attention output = A(x)

    Instead of using only the attention output , we add the original input back
        output = x+A(x)

        this is why it's called 'Add'


2. Why add the original input ?

    - Suppose a layer doesn't learn anything useful.
        Without residual:
            Output = Bad Output

        The information is lost.

        With residual:
            Output = Original + Small Change

    - It preserve the original input even there is loss of information in attention output.
    - Help gradient flow
    - Prevents vanishing gradient
    - Allows deeper model


            Original Chapter
                │
                ├──────────────┐
                │              │
        Rewrite              Original
                │              │
                └──── Add ─────┘


3. Why is it called a Skip Connection?

    - Because the input skips the computation and is added later.
    - The input bypasses the attention layer.

4. What is LayerNorm ?

    - Layer Normalization stablizes the values flowing through the network

    - It rescales the features for each token so they have a controlled distribution.

    For one token's hidden vector:
        [2, 10, -5, 100] -->>  [-0.4, 0.1, -1.2, 1.5]

5. Why do we need LayerNorm ?

    - Without LayerNorm , hidden values can grow or shrink unpredictably extremely large/ small across many layers.


6. How LayerNorm works ?
    - For each token independently:
        Hidden State

            [3, 5, 7, 9]

    - Compute the mean:
        Mean = 6

    - Subtract it:
        [-3, -1, 1, 3]

    - Compute the standard deviation and divide by it:
        Normalized = (x - μ) / (σ + ε)

        Normalized = [-1.34, -0.45, 0.45, 1.34]

    Where :
        - ε (epsilon) is a very small constant added to prevent division by zero.
        -

    - Then apply two learnable parameters: This stabilizes activations and improves training of deep Transformers.
        Output = γ × normalized + β

        where:
            γ learns the scale.
            β learns the shift.

            - These are trained with the rest of the model.

7. What are the different techniques used in LayerNorm ?

    1. LayerNorm: Normalizes the hidden/features of each token independently.

        y = γ ( x - μ)/ SQRT(σ^2+ϵ) + β

        Key: subtracts mean + divides by standard deviation.

    2. RMSNorm:
        Normalizes using the root-mean-square, without subtracting the mean.

         y = γ ( x ) / SQRT(1/d(x_i^2+ϵ) )

        Key: simpler than LayerNorm and widely used in modern LLMs.

    3. BatchNorm: Normalizes using statistics computed across the batch.

        Key: very common in CNNs, but generally not preferred for Transformers,
            partly because sequence lengths and batch composition make batch statistics less suitable.

    4. GroupNorm: Splits channels/features into groups and normalizes within each group.

        Key: common in computer vision; uncommon in standard LLMs.


8. What is difference between LayerNorm & BatchNorm:

    |                            | LayerNorm | RMSNorm         |
    | -------------------------- | --------- | --------------- |
    | Mean subtraction           | ✅         | ❌               |
    | Variance/std normalization | ✅         | ❌               |
    | RMS normalization          | ❌         | ✅               |
    | Learnable scale            | ✅         | ✅               |
    | Learnable bias             | Usually ✅ | Usually ❌       |
    | Modern LLM usage           | Common    | **Very common** |

LayerNorm = center + scale.
RMSNorm = scale only.


9. Where normalization is placed in a Transformer block?

    Post-LayerNorm:
        Attention -> Add -> LayerNorm

    Pre LayerNorm:
        LayerNorm -> Attention ->> Add

"""