"""
1. How masking works in mask-attention ?

    - Before Softmax:
        - We modify the attention scores
        - Future positions set to -∞.

    Analogy: Think exam hall :-
        - You can see only previous answers
        - Future answer sheet is covered.

        Mask: Invigilator

    Types of Masking:
        - Padding Masking: Used when sentences has different lengths.
        - Causal Mask: Prevents information leakage by blocking attention to future token in autoregressive decoding.


"""