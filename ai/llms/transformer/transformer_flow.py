"""
                    Sentence
                    ──────────────────────────────────────────────
                    Curiosity | killed | the | cat
                    (T = 4)

                                    │
                                    ▼
                    Tokenization
                    ──────────────────────────────────────────────
                    [101] [2054] [1996] [4937]

                                    │
                                    ▼
                    Embedding + Positional Encoding
                    ──────────────────────────────────────────────
                    X = (4 × 512)

                                    │
                                    ▼
                            Three Linear Projections
                    ──────────────────────────────────────────────

                    Q = XWq          K = XWk          V = XWv

                    Wq = 512×512     Wk = 512×512     Wv = 512×512

                    Q = 4×512        K = 4×512        V = 4×512

                                    │
                                    ▼
                    Reshape into 8 Heads
                    ──────────────────────────────────────────────

                    Q → 4×8×64
                    K → 4×8×64
                    V → 4×8×64

                                    │
                                    ▼

                            ┌──────────────────────────────┐
                    Head 1  │ Q1,K1,V1 : (4×64)            │
                            │ Attention(Q1,K1,V1)          │
                            │ Output → (4×64)              │
                            └──────────────────────────────┘

                            ┌──────────────────────────────┐
                    Head 2  │ Q2,K2,V2 : (4×64)            │
                            │ Attention(Q2,K2,V2)          │
                            │ Output → (4×64)              │
                            └──────────────────────────────┘

                                     ...

                            ┌──────────────────────────────┐
                    Head 8  │ Q8,K8,V8 : (4×64)            │
                            │ Attention(Q8,K8,V8)          │
                            │ Output → (4×64)              │
                            └──────────────────────────────┘

                    Each head computes:

                    Attention = Softmax(QKᵀ / √64) V

                                    │
                                    ▼
                    Concatenate Heads
                    ──────────────────────────────────────────────

                    Head1  (4×64)
                    Head2  (4×64)
                    ...
                    Head8  (4×64)

                    ↓

                    Concat

                    ↓

                    (4×512)

                                    │
                                    ▼
                    Output Projection
                    ──────────────────────────────────────────────

                    Wo = (512 × 512)

                    (4×512) × (512×512)

                    ↓

                    Output = (4×512)

                                    │
                                    ▼
                    Residual Add

                    Output + Original Input

                    ↓

                    (4×512)

                                    │
                                    ▼
                    LayerNorm

                    ↓

                    (4×512)

                                    │
                                    ▼
                    Feed Forward Network (MLP)

                    512 → 2048 → 512

                    ↓

                    (4×512)

                                    │
                                    ▼
                    Residual Add

                    ↓

                    LayerNorm

                    ↓

                    Final Output of Transformer Block

                    (4×512)
"""