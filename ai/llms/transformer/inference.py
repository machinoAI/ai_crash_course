"""
1. What is Prefill ?
    - Prefill is the first inference stage where the model processes the entire input prompt in parallel
        to compute the initial hidden states and populate the KV Cache.

    Example:
            "Curiosity kill the cat" --> 4 tokens

        - During prefill all the tokens processed parallely
        - The model computes Q,K, V, Hidden states Most importantly K & B and stored in KV cache.

        At the end of prefill:
            Prompt

            ↓

            Hidden States

            ↓

            KV Cache

            ↓

            Predict Next Token

    - Prefill = Process the whole prompt once and build the KV Cache.


2. What is Decode ?
    -

"""