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








"""