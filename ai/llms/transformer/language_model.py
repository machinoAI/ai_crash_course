"""
1. What is Language Model ?

    - A model that predicts the probability of the next token given the previous tokens.

2. What is the LM Head?

    - The transformer ends at the hidden state and the hidden state is not a word but vectors.
    - Humans can not read this, it must convert this vector into vocabulary.
    - That conversion layer is called the LM head.

3. What is inside the LM Head?
    - It is just One Linear Layer.
    - Mathematically: Hidden state ->> Linear ->> Vocabulary scores.
    - If hidden = 512 and vocabulary = 50k

    Then LM Head = 512 x 50,000

    - There is nothing more, No attention, No MLP, No layerNorm just one matrix multiplication.

4. Why is it called "Head"?
    - Because it's the last layer attached to the model.
    - Many neural networks have different heads:
        - Classification Head
        - Segmentation Head
        - Detection Head
        - Language Modeling Head

    - The Transformer is the shared backbone. The "head" is the task-specific output layer.



"""