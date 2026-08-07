"""
1. What is positional Embeddings ?

    - Since self attention is permutation invariant, position encoding is added to token embeddings
        to inject sequence order information

    - The original transformer uses sinusoidal functions to encode positions.

2. Why do we need positional encoding ?

    - Transformer process all tokens in parallel, so sentence
        "Dog bites man"
        "man bites dog"

    Embeddings alone can not tell who is first.

    - Attention is order agnostic, So we must inject position information.

3. What is position encoding ?
    - It is vector added to token embedding.
    - To tell model:
        "This word is at position1 and this at position2..."


    Formula:

        Final Input = Token embeddings + Position encoding

4. What is Sinusoidal Position Encoding (SPE) ?

    - For position Pos and dimension i,

    PE (pos, 2i) = Sin(pos/ 10000^(2i/d_model)

    PE(pos, 2i+1) = cos(pos/ 10000^(2i/d_model)

    where:
        pos = token position (0, 1, 2, ...)
        i = embedding dimension index
        d_model = embedding dimension (e.g., 512, 768, 4096)


5. How does positional encoding works ?
    - Say we have embeddings e1, e2, e3 ...e512.
    - And positional encoding we calculated
        p1, p2,p3,....p512.

    Then we simply add these two:
        e1+p1, e2+p2, e3+p3, ... , e512+p512


6. What is Rotary Positional Encoding or RoPE ?

    -  Instead of adding Positional vectors like Sinusoidal PE,
        RoPE rotates the Q and K vectors in vector space based on position

    So, position is encoded via angle rotation.

 Core Idea:
    Each token vector  = Arrow in 2D plane
    Position  =  Rotation angle

    So,
        Token at position1 ->> Small rotation
        Token at position2 ->>  Bigger rotation

    Thus,
        Relative distance becomes naturally encoded.


How it works ?
    - Instead of Q = XWq
                K = XWk

    we do:
        Q' = Rotate(Q, position)
        K' = Rotate(K, position)

    Then Attention
        = SOftmax((Q'K'^T)sqrt(d_k) x V


7. Why RoPE is powerful ?

    - Encodes relative position naturally
        - Long Context understanding
        - Better generalization
    - Works well for very long sequence
    - No extra parameter

    Analogy:
        - Embedding ->>Car direction
        - Position ->> Steering angle
        RoPE ->> Turn steering wheel slightly at each token.


    So Model know, How far I have travelled in sentence.


8. What is learned PE ?
    - Sinusoidal PE is fixed
    - Learned Positional Embeddings use a trainable embedding matrix where each position has its own learnable vector.
    - These vectors are added to token embeddings.
    - Unlike sinusoidal encodings, they are optimized during training but cannot naturally generalize to positions beyond the training context length.

9. What is Relative Positional Encoding ?
    - Relative Positional Encoding represents the relative distance between tokens rather than their absolute positions.
    - This helps the model focus on relationships such as 'previous token' or 'next token' and improves generalization to longer sequences.
    - Example:
        "Curiosity skilled the cat"

            Do you really care "cat" is coming at last or  "cat" is coming after the "skilled" ?

    Advantages:
        - Better for long sequences.
        - Captures relative relationships naturally.
        - Generalizes better.

10. What are limitations of RoPE ?
    - Very Long context (1M) , The rotation angle become less effective.
        - Attention quality degrades.

    - Originally trained on 4096 tokens running at 128k requires scaling tricks.
        - Example: LongRoPE, NTK Scaling, YaRN

    - Still quadratic attention.
        - Attention complexity still O(T^2)


11. Difference:
    - Sinusoidal Positional Encoding uses sin and cos to create a positional vector that is added to the embeddings.

    -RoPE uses the same sine and cosine functions, but instead of adding a vector, it rotates the Q and K vectors.



"""