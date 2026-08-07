"""
1. What is activations ?

    - An activation is simply the output of any layer during the forward pass.
    - Intermediate outputs produced during the forward pass (stored temporarily for backpropagation).

      Embedding
        ↓

        Activation 1

        ↓

        Attention
        ↓

        Activation 2

        ↓

        MLP
        ↓

        Activation 3

        ↓

        LM Head
        ↓

        Logits


2. What is activation functions ?

    - These are the functions which introduce non-linearity to attentions. Examples:
        - ReLU
        - GeLU
        - SiLU
        - SwiGLU
        - Tanh
        - Sigmoid

3. What is Hidden state ?
    - In Transformers, the most important activations are called hidden states.
    - Every hidden state is an activation.
    - But Not every activation is a hidden state.
    - Examples:
            Embeddings
            ↓

            Hidden State 0

            ↓

            Block 1

            ↓

            Hidden State 1

            ↓

            Block 2

            ↓

            Hidden State 2


4. What are weights ?

    - Weights are learned parameters. (not activations)
    - Example:
        - WQ
        - WK
        - WV
        - WO
        - WLM

    These are weights.
    - Activations are the values produced when the model processes an input.


"""