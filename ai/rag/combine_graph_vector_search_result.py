"""
1. How do you combine the results of vector and graph search ?

                 User Query
                 │
        ┌────────┴─────────┐
        ↓                  ↓
   Vector Search       Graph Search
        ↓                  ↓
   Candidates A        Candidates B
        └────────┬─────────┘
                 ↓
              Merge
                 ↓
              Rerank
                 ↓
            Top K chunks
                 ↓
                LLM

    - RRF: Reciprocal Rank Fusion:

        RRF(chunk) = 1 / (k + rank_vector) + 1 / (k + rank_graph)
                    = RRF score = Σ 1 / (K + rank)

        rank = position of the document in a retrieval list
        K = a smoothing constant
        Commonly K = 60
        K prevents the top-ranked result from dominating too aggressively.


    Example:
        Query = "Customer ABC pricing discussion"

        Vector Search          Graph Search
        -------------          ------------
        Chunk A → Rank 1       Chunk C → Rank 1
        Chunk B → Rank 2       Chunk A → Rank 2
        Chunk C → Rank 3       Chunk D → Rank 3
        Chunk D → Rank 4       Chunk B → Rank 4


        K = 60

        Chunk A:
            Vector Rank = 1
            Graph Rank  = 2

            RRF(A) = 1/(60+1) + 1/(60+2)
                   = 1/61 + 1/62
                   = 0.03252


        Chunk B:
            Vector Rank = 2
            Graph Rank  = 4

            RRF(B) = 1/62 + 1/64
                   = 0.03176


        Chunk C:
            Vector Rank = 3
            Graph Rank  = 1

            RRF(C) = 1/63 + 1/61
                   = 0.03226


        Chunk D:
            Vector Rank = 4
            Graph Rank  = 3

            RRF(D) = 1/64 + 1/63
                   = 0.03150


        Final Ranking:
            1. Chunk A → 0.03252
            2. Chunk C → 0.03226
            3. Chunk B → 0.03176
            4. Chunk D → 0.03150


        Meaning of K:
            Small K → rank position has more impact
            Large K → rank position has less impact

            K = 60 → commonly used starting point
            K should ultimately be tuned using retrieval evaluation.

2. What are the different technique to combine results from different sources ?

    Common Retrieval Fusion Methods

    1. RRF (Reciprocal Rank Fusion)
       - Combines based on rank
       - Does NOT require scores from different retrievers to be comparable
       - Simple + robust
       - Very common baseline

    2. Weighted Score Fusion
       - Combines normalized scores

       Final Score =
           α × Vector Score
         + β × Keyword Score
         + γ × Graph Score

       Example:
           0.6 × Vector
         + 0.2 × Keyword
         + 0.2 × Graph

       - Useful when you know the importance of each signal
       - Scores must be normalized/calibrated

    3. Relative Score Fusion
       - Normalize each retriever's scores first
       - Then combine them

       Example:
           normalized_vector_score
           normalized_keyword_score
           normalized_graph_score

       - Better than directly adding raw scores
       - Useful when score ranges differ

    4. Rank-Based Weighted Fusion
       - Similar to RRF
       - But different retrievers can have different weights

       Example:
           0.7 × Vector Rank Contribution
           0.3 × Graph Rank Contribution

       - Useful when one retriever is more reliable

    5. Learned Fusion / Learning-to-Rank
       - Train a model to combine retrieval signals

       Features:
           vector_score
           BM25_score
           graph_score
           recency
           entity_match
           metadata_match
           source_quality

       ↓

       Ranking Model

       ↓

       Final ranking

       - More sophisticated
       - Requires labeled/evaluation data

    6. Cross-Encoder Reranking
       - Retrieve candidates from multiple sources first
       - Give Query + Candidate to a cross-encoder
       - Model directly predicts relevance

       Query + Chunk
            ↓
       Cross Encoder
            ↓
       Relevance Score
            ↓
       Final Ranking

       - Usually much better for final ranking
       - More computationally expensive





3.  End-to-End Architecture:

                         USER QUERY
                              │
                              ↓
                    Query Understanding
                              │
                ┌─────────────┴─────────────┐
                ↓                           ↓
        Tenant / Entity                Query Embedding
        Identification                       │
                │                            ↓
                │                      PGVector HNSW
                │                            │
                │                       Vector Results
                │                            │
                ↓                            │
       Identifier Table                      │
                │                            │
                ↓                            │
          Entity Resolution                  │
                │                            │
                ↓                            │
       Relationship Table                    │
                │                            │
                ↓                            │
         Graph Expansion                    │
                │                            │
                └──────────────┬─────────────┘
                               ↓
                            MERGE
                               ↓
                         DEDUPLICATE
                               ↓
                            RERANK
                               ↓
                      Context Construction
                               ↓
                              LLM
                               ↓
                           RESPONSE


"""