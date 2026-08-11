"""
RAG:
- RAG has two pipeline
    - Ingestion pipeline: Docs ->> Chunking ->> cleaning ->> embeddings->> vector indexing
    - Retrieval Pipeline: Query ->> Embeddings ->> semantic Search (ANN) ->> re-ranker ->> top@k match + prompts->> LLM->> Answer (grounded)

1. What is ANN?
- Approximate Nearest Neighbours is a technique to find the most relevant items in vector DB for the given query.

- what is HNSW Algorithm?
    - HNSW: Hierarchical Navigable Small World is a graph-based indexing algorithm used for Approximate Nearest Neighbor (ANN) search.
    - Instead of querying against every vector , It organizes vectors into multilayer graph, Allowing the search to
    quickly navigate to the nearest neighbors with high accuracy and low latency.


    Pros:
        - Very fast retrieval
        - Excellent Recall
        - No training phase

    Cons:
        - High Memory consumption
        - Index construction can be expensive

    HNSW Base Vector Database:
        - Weaviate
        - PgVector
        - Milvus


2. What does "Small World" mean?
    - Think of social networks:
        - Your friend knows someone in another city.
        - That person knows someone in another country.
        - Even though millions of people exist, you can reach almost anyone through a few connections.

        - HNSW applies the same idea to vectors.
        - Instead of checking every vector, it hops through neighboring vectors to quickly reach the target.

3. What is inverted File Index (IVF) ?

    IVF is the first cluster base algorithm , It partitions vector into clusters and searches only the nearest clauster.

                All vectors
                   |
       ┌───────────┼───────────┐
       ↓           ↓           ↓
    Cluster 1   Cluster 2   Cluster 3


    For a query, identify the closest clusters and search only those.

    nprobe : Higher nprobe ->> Better recall but slower search.


4. What is Product Quantization or PQ ?

    - Compresses vectors into smaller representations.
    - Useful when you have huge numbers of vectors and memory becomes a problem.

    You sacrifice some accuracy for:

        - Lower Memory
        - Faster Search
        - Lower Storage

5. what is IVF + PQ  ?

    - Very common for large-scale vector search.
    - This gives : partitioning + compression


                 Vectors
                    ↓
                  IVF
              /     |     \
          Cluster Cluster Cluster
             ↓
             PQ
             ↓
        compressed vectors



Note:   ------------------------------------------------------------------------------
        | Index      | Main idea          | Strength               | Weakness         |
        | ---------- | ------------------ | ---------------------- | ---------------- |
        | Flat   | Compare everything | Exact                  | Slow at scale    |
        | HNSW   | Graph traversal    | Excellent speed/recall | Memory heavy     |
        | IVF    | Cluster vectors    | Scales well            | Requires tuning  |
        | PQ     | Compress vectors   | Huge memory savings    | Some recall loss |
        | IVF-PQ | Cluster + compress | Very large datasets    | More complexity  |

"""