"""
1. What is self-attention ?
    - Each token attends to all others tokens in the same sequence

    Q, K, V -> From same input.

    Q = XWq
    K = XWk
    V = XWv

    Attention(x) = SoftMax(QK^T)/sqrt(dk)*V

    where dk is dimension of key vector
    K^T  = K transpose.

2. What is Q,K & V ?

    - Q, K, V projection matrices are trainable linear layers initialized randomly and optimized through
        gradient descent to learn task specific attention.

    self.wq = nn.Linear(d_model, d_k)
    self.wk = nn.Linear(d_model, d_k)
    self.wv = nn.Linear(d_model, d_k)

    where:
        d_model = dimension of embedding layer or Hidden size of transformer
        d_k = dimension of key vector

        d_k = d_model / num_heads = 512 / 8 = 64


    Why Smaller dimension ?

    -   Reduce computation O(n^2)
    - Enables multi-head attention
    - Different heads learns different attentions.
    - Stablizes dot product values

3. Why we divide by sqrt(d_k) in attention ?

    - To prevent dot product values from becoming too large,
    - Which would push softmax into extreme regions and cause very small gradients ->> unstable training
    This causes:
        - Almost no gradients->> Vanishing gradient problem
        - Model stops learning properly
        - Training Unstable

4. Why softmax in attention ?
    - Convert scores to probabilities.
    - Softmax sharpens attention because -- exponential scaling magnifies score differences
        loading to sparse probability distribution.

5. Why do we transpose K in attention ?

    Attention = Softmax(( Q x K^T) / sqrt(d_k)) x V

    - Say we have input tokens:
        "Curiosity skill the cat"

        total token counts = 4 --> input sequence length = T
        Lets say embedding dimension is = d =768

        So  Q  => T x d
            K  => T x d
            V  => T x d

        So in order to calculate attention first we need to do  matrix multiplication of
         Q and K

         which have T rows and d columns

         Matrix multiplication is not possible because the columns of Q (d) must equal the rows of K (T), and
         generally d not equal T.

            - Columns of the first matrix (d)
            - Rows of the second matrix (T)

            so,
                Clearly d is not equal to T

        So we need to transpose the K,  so its rows become columns and columns become rows.

        K  => T x d

        and

        K^T => d x T

        Now we would be able to do matrix multiplication.
            (QxK^T) = (T x d) x (d x T)  => (T x T)

        Next step we divide it by sqrt(d_k) and compute the Softmax

        Few things to note here,
            - The sum of each row is 1
            - Even after computing the attention we still have same dimension: (T x T)

        - In the last step we multiply the results with V = (T x d)

        Softmax((QxK^T)/sqrt(d_k)) x V
        = (T x T) x (T x d) =>> T x d (back to original dimension)


6. What are types of attentions ?

    1. Self-attention : Every token attends to every other tokens
        - GPT, BERT

    2. Cross-Attention: One sequence attends to another sequence
        - Machine translation, T5 , BART

    3. Masked (causal) Self-attention: A special type of self-attention where future tokens are hidden
        Example:  GPT


    4. Single Head Attention: Only one attention mechanism
    5. Multi-Head attention: Many attentions head where each head learns new relationship.

    6. Multi-Query Attention: Each head has different query but shared key and shared value.
        - Much smaller KV Cache
        - Faster Inference
        - Used in PaLM

    7. Grouped Query Attention: Multiple query heads share the same key and value heads within a group,
            instead of each query head having its own key and value.

        - This reduces the number of Key and Value tensors that must be stored and retrieved, significantly lowering
            KV cache memory and improving inference speed, while maintaining accuracy close to Multi-Head Attention (MHA).
            - Llama-2, Llama-3 , Mistral , Gemma etc

    8. Dense Attention: Every token attends to every token
        - All <--> All
        - Complexity O(T^2)
        - Standard Transformer

    9. Sparse Attention: Attend only to selected attention
        - LongFormer
        - BigBird

    10. Sliding Window Attention: Only nearby tokens.
        - Window => [5 previous] => Current [ 5 next ]
        - Used By Mistral

    11. Linear Attention: Avoids building the T×T matrix.
        - Complexity : O(T)
        - Good for very long sequences.

    12. Flash Attention: FlashAttention computes the same attention as standard Transformers but
        processes it in memory-efficient tiles, avoiding storage of the full attention matrix and
        significantly accelerating training and inference on GPUs.

        - Standard Attention:
            Q × Kᵀ
              ↓
        Attention Scores (T × T)
              ↓
        Store in GPU Memory
              ↓
            Softmax
              ↓
            Store Again
              ↓
        Multiply with V
              ↓
            Output


    - The large T×T matrix is written to and read from GPU memory multiple times.
    - This data movement is expensive.

    But in Flash Attention:
        - Instead of computing the entire matrix at once, FlashAttention processes it in small tiles.
        - Imagine splitting the matrix into blocks:
            +-----+-----+-----+
            | A11 | A12 | A13 |
            +-----+-----+-----+
            | A21 | A22 | A23 |
            +-----+-----+-----+
            | A31 | A32 | A33 |
            +-----+-----+-----+

        - It computes one block, immediately applies the necessary operations (including softmax),
            updates the output, and then discards the block.

        - The full attention matrix is never stored in GPU memory.

    Why is Flash Attention faster?

        - FlashAttention minimizes slow accesses to GPU high-bandwidth memory (HBM) by keeping intermediate computations in the much faster on-chip shared memory (SRAM).
        This leads to:
            - Less memory traffic.
            - Better GPU utilization.
            - Higher throughput.

7. What types of attention being used in the modern LLMs ?
    - Causal Attention + GQA + Flash Attention.

    Example:
            def attention(x):

                Q = project_query(x)      # 8 heads
                K = project_key(x)        # 4 heads (GQA)
                V = project_value(x)      # 4 heads (GQA)

                K = repeat_groups(K)
                V = repeat_groups(V)

                output = flash_attention(
                    Q,
                    K,
                    V,
                    causal=True
                )

                return output


Note:
- With 8 heads and a model dimension of 512, the model projects the input into eight independent 64-dimensional
    Q, K, and V representations ( 1 x 8 x 64). Each head computes attention in parallel on its own 64-dimensional subspace.
    Their outputs are concatenated, projected back to 512 dimensions, and all projection matrices are updated
    during backpropagation.

Question:
    - In multi-head attention each of the heads process: ( 1 x 8 x 64)
    - And it learns different values of Q,K, V across the attention.
    - And at the end we merge them all to get the final weights.

  Why not keep a single attention ?
    - Answer is more empirical than theoretical, single attention exist but that not perform as good as multi-head attention.
    - How single head attention is different than multi-head attention ?


8. What is weight tying ?
    - Weight tying shares the input embedding matrix with the output LM head by using its transpose during output prediction.
    - This reduces parameters and aligns the input and output token representations in the same embedding space.

9. What is Wₒ ?
    - Wₒ is a trainable weight matrix.
    - It is randomly initialized and learned during training through backpropagation.

10. Why do we need the Output Projection (Wₒ)?
    - The output projection (Wₒ) is a learned linear layer applied after concatenating all attention heads.
    - It combines information from different heads into a single unified representation and maps it back
        to the model dimension.

    Example:
            Head1 ... 1x64
            Head2 ... 1x64
            ...
            ...
            Head8 ... 1x64

            concatenate(H1,H2,h3,...,Head8) = 1x512
            since 4 tokens(Curiosity kill the cat) = 4x512

            Now Wₒ = 512x512

        So final attention gets calculated = (4x512)x (512 x 512) =>> 4x512
"""