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
    - Decode is the inference stage where the model generates one new token at a time
        using the previously generated tokens and the KV Cache.

    - Decode = Generate one token, append it to the KV Cache, repeat.


3. Why is Decode Sequential?
    - Each generated token becomes part of the input for predicting the next token.
    - Since the next token is unknown until the current one is generated, decoding must proceed one token at a time.

4. What KV Cache does ?

    - KV Cache stores key (K) and value (v) tensors of the previously processed tokens during Autoregressive
        inference, So the model doesn't recompute them when generating the next token.

    - KV Cache trades GPU memory for computation, dramatically reducing redundant computation during autoregressive decoding.

    - Cache the past K and V; compute a new Q, K, V for the new token.

    - KV Cache trades GPU memory for computation.


5. Why don't we cache Q?
    - Because during autoregressive decoding, the old Q vectors aren't needed again.

    Q = What information do I need?
    K = What information do I represent?
    V = What information should I provide?

    From the attention , we just need all the previous K & V to predict and just current Q to predict next token

6. How much memory KV required ?
    Imagine a transformer with following configuration:

        - Layers = 32 -transformer block
        - Hidden dimension= 4096
        - Attention Heads = 32
        - Heads dimension = 128
        - Precision = FP16 = 2 bytes
        - Sequence length = 2048

        KV cache per layer:
            K : 2048×32×128 = V is the same

        KV = 2x 2048 x 32 x 128 = 16,777,216

        At FP16 = 2 x 16,777,216 = 33,554,432 bytes = 32 MB

        For 32 Layers =  32 x 32 MB =  1 GB

        So this model requires approximately 1 GB of KV cache for one sequence of 2048 tokens.


        KV Memory = 2 × L × T × H × D × Bytes

        Where:
            L =  Layers
            T = Sequence length
            H = Number of KV heads
            D = Head Dimension
            The first 2 is K+V

    So KV cache memory linearly with sequence length:
        | Context | KV Cache |
        | ------: | -------: |
        |      2K |    ~1 GB |
        |      4K |    ~2 GB |
        |      8K |    ~4 GB |
        |     16K |    ~8 GB |
        |     32K |   ~16 GB |
        |    128K |   ~64 GB |


7. What is difference in with and without KV cache ?

    |                  | Without KV Cache          | With KV Cache             |
    | ---------------- | ------------------------- | ------------------------- |
    | KV memory        | Low                       | High                      |
    | Recompute K/V    | Huge                      | Minimal                   |
    | Generation speed | Slow                      | Much faster               |
    | Sequence scaling | Computationally expensive | Memory becomes bottleneck |


8. How does the GQA save memory ?

    Normal attentions KV Memory:

        KV Memory = 2 × L × T × H × D × Bytes

    Where H is number of heads in transformer block(In standard) = KV heads

    KV =  32 in standard transformer

    But in GQA , Since we group KV fot multiple Query values

    Let's Say KV heads = 8

    Means for Q1, Q2, Q3, Q4 we will have same KV values = 32/8

    And Now KV Memory
        = 2 x 32 x 2048 x 8 x 128 x 2 = 268,435,456 approx 256 MB

    - With GQA it is 4 times cheaper.


"""