"""
1. What is a Transformer Block?
    - A Transformer block is the fundamental building block of a Transformer model.
    - A Transformer consists of multiple identical Transformer blocks stacked sequentially.
    - Each block contains Multi-Head Self-Attention, residual (Add) connections, Layer Normalization, and a Feed-Forward Network (MLP).
    - Every block refines the token representations before passing them to the next block.

2. Why do we stack multiple Transformer Blocks?
    - Each Transformer block progressively refines the hidden representations learned by previous blocks.
    - Early blocks often capture local lexical and syntactic information, while deeper blocks
        tend to capture higher-level semantic, contextual, and reasoning patterns.

    - Stacking many blocks allows the model to build increasingly rich representations of the input.


3. What components are inside one Transformer Block?

    For GPT: Decoder only:

        Input

        ↓

        LayerNorm

        ↓

        Masked Multi-Head Attention

        ↓

        Residual Add

        ↓

        LayerNorm

        ↓

        MLP

        ↓

        Residual Add

        ↓

        Output


4. How does information flow through multiple blocks?

    Embedding

        ↓

        Transformer Block 1

        ↓

        Transformer Block 2

        ↓

        ...

        ↓

        Transformer Block N

        ↓

        LM Head

        ↓

        Vocabulary Logits


    - The input embeddings enter the first Transformer block.
    - Each block applies attention, residual connections, normalization, and an MLP to produce updated hidden states.
    - These hidden states become the input to the next block.
    - This process repeats until the final block produces contextual representations that are passed to the LM head for next-token prediction.

5. What is the Hidden State?
    - A hidden state is the contextual vector representation of a token at a particular layer of the Transformer.
    - Each Transformer block updates the hidden states by incorporating information from other tokens, producing
        progressively richer contextual representations.

6. What is hidden layers ?
    - A hidden layer in a Transformer is a Transformer block, and each Transformer block takes a hidden state
        as input and produces a new hidden state as output.

    Embedding
        │
        ▼
    Hidden State 0
        │
    Transformer Block 1 (Hidden Layer 1)
        │
        ▼
    Hidden State 1
        │
    Transformer Block 2 (Hidden Layer 2)
        │
        ▼
    Hidden State 2
        │
    ...
        │
    Transformer Block N (Hidden Layer N)
        │
        ▼
    Final Hidden State

7.  Why does the hidden state change after every block?

    - Because every Transformer block updates the token representation using:
        - Self-Attention (gathers context from other tokens)
        - MLP (non-linear transformation)
        - Residual connections and LayerNorm

8. Does each Transformer block process different tokens?
    No; Every Transformer block processes the entire input sequence.

9. What exactly is learned in one Transformer block?
    - A block learns:
        - Attention patterns (which tokens should attend to which)
        - Feature transformations (MLP)
        - How to combine attention heads (Wₒ)
        - Normalization parameters

"""