"""
- Transformer Architecture:
    - Input tokens -->> Embeddings -->> Positional Encoding/RoPE ->>
        -->>Transformer Block
            - Multi-head Attention
            - Add & LayerNorm
            - FFN
            - Add & LayerNorm
        -->> Language Model Head -->> SoftMax



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






"""