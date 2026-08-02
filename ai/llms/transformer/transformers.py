"""
1. What is transformer ?
- Transformer is a deep learning architecture designed to process data sequentially with attention mechanism
    instead recurrence or convolution.

    Existing Issues:
        - Slow training
        - Long range dependencies
        - Gradient issues

    Transformer solved this problem by:
        - Parallel processing
        - Global context learning (attention)
        - Better scalability

2.  How does attention solve long range dependencies ?

    - Attention mechanism looks at entire sequence at once and decide which word is important

    -Example:
        Say you are reading a novel and at the page #5 something happened
        which is related to page #100, RNN & CNN trouble remembering that far.


3. Why does self-attention solve this problem?
    - Self-attention allows every token to attend to every other token in the sequence without relying on
        previous hidden states.

    - Since all attention scores are computed using matrix operations(Q,K, V), all tokens can be processed
        in parallel, making training significantly faster while also capturing long-range dependencies effectively.

4. Full Architecture of transformer has :
    - Encoders -->> Embeddings
    - Decoders -->> Generate tokens

    Blocks:
        - Multi-head attention
        - Feed Forward Neural Network
        - Residual Connections
        - Layer Normalization


5. What is the overall architecture of a Transformer?
    - Transformer Architecture:
        - Input tokens -->> Embeddings -->> Positional Encoding/RoPE ->>
            -->>Transformer Block
                - Multi-head Attention
                - Add & LayerNorm
                - FFN
                - Add & LayerNorm
            -->> Language Model Head -->> SoftMax

    or complete:
            Input Text
              │
              ▼
        Tokenizer
              │
              ▼
        Token IDs
              │
              ▼
        Embedding
              │
              ▼
        Transformer Block 1
              │
              ▼
        Transformer Block 2
              │
              ▼
        ...
              │
              ▼
        Transformer Block 32
              │
              ▼
        Final Hidden State
              │
              ▼
        LM Head ⭐
              │
              ▼
        Vocabulary Logits
              │
              ▼
        Softmax
              │
              ▼
        Next Token


6. What is Encoder ?

    - The encoder transforms input tokens into contextual embeddings that captures the meaning of
        each token based on the entire input sequence.


    - Input tokens ->> Embedding + Positional Encoding -->> Multiple Encoder Layers -->> Output (Hidden States)

    - Each hidden state is a vector representing a token after considering the full context.

7. What does an encoder do ?

    1. Converts token IDs → embeddings.
    2. Adds positional information.
    3. Applies bidirectional self-attention (every token attends to every other token).
    4. Passes through Feed Forward Networks (MLP)
    5. Produces contextual representations for every input token.

Examples:
        - BERT
        - RoBERTa
        - DistilBERT



"""