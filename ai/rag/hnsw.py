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

2. What does "Small World" mean?
    - Think of social networks:
        - Your friend knows someone in another city.
        - That person knows someone in another country.
        - Even though millions of people exist, you can reach almost anyone through a few connections.

        - HNSW applies the same idea to vectors.
        - Instead of checking every vector, it hops through neighboring vectors to quickly reach the target.

"""