"""
- For a RAG system with around 10 million documents,
    I would first design an offline ingestion pipeline. I would extract text from PDFs and use recursive chunking,
    where the text is split based on chapters, topics, subtopics, and paragraphs so that the semantic context is preserved.
    I would also keep a hard limit of around 800 tokens per chunk, and if a section exceeds that limit,
    I would split it further with an overlap of about 50 tokens to preserve continuity across chunks.
    After chunking, I would clean and normalize the text before generating embeddings.

- For embeddings, I would benchmark a few state-of-the-art models such as OpenAI's text-embedding-3-large,
    Voyage, or BGE, and choose the one that gives the best balance of retrieval quality, latency, and
    cost for my enterprise documents. Assuming text-embedding-3-large performs best during evaluation,
    I would use that to generate the embeddings.

- Assuming each document produces around five chunks on average, 10 million documents would result in roughly 50 million vectors.
    At this scale, I would use FAISS as my ANN indexing engine because it provides multiple indexing algorithms such
    as HNSW, IVFFlat, and IVFPQ. Since memory efficiency becomes important with tens of millions of vectors,
    I would choose IVF-PQ, which clusters the vectors and compresses them using Product Quantization.
    This significantly reduces memory usage while maintaining good retrieval performance for large-scale deployments.

- Once the index is built, I would create the online retrieval pipeline. The user query would first be converted
    into an embedding, and I would perform hybrid retrieval by combining dense semantic search with BM25 keyword search.
    I would also apply metadata filtering whenever applicable, such as filtering by department, document version,
    project, or user permissions, to reduce the search space and improve relevance.

- Instead of using a fixed Top-K, I would use Dynamic Top-K because the number of relevant documents depends on the complexity of the user's question.
    Simple factual questions may only require three to five documents, whereas more complex reasoning questions may require ten to fifteen documents.
    However, I would cap the maximum at around twenty documents to control latency and context size.

- Since not every retrieved document is equally useful, I would use a cross-encoder reranker to re-rank the
    retrieved results and keep only the most relevant documents before constructing the final prompt.
    Those documents, along with the system prompt and user query, would then be sent to the LLM for answer generation.

- To evaluate the retrieval quality, I would use metrics such as Recall@K, Precision@K, MRR, and nDCG.
    For generation quality, I would evaluate groundedness, faithfulness, and answer relevance to ensure the model
    generates answers that are both accurate and supported by the retrieved context.

- One reason I would not choose HNSW in this particular design is that, while it offers excellent recall and low-latency
    search, it stores full vectors and therefore requires significantly more memory.
    With around 50 million vectors, IVF-PQ provides a better trade-off between memory consumption, scalability, and retrieval quality.

- I would also avoid ChromaDB for this use case because it abstracts away the indexing strategy and primarily uses HNSW internally.
    - For very large production deployments, I would prefer a solution where I have explicit control over the
    ANN indexing algorithm and its tuning parameters. Similarly, I would not choose pgvector because,
    although it supports HNSW and IVFFlat, it does not currently support IVF-PQ compression, making it less memory-efficient for this scale.

- Finally, this would only be the initial system design. Before production deployment,
    I would benchmark the entire pipeline by measuring embedding latency, retrieval latency, reranking latency,
    LLM inference latency, and end-to-end response time. I would also optimize the system using embedding caching,
    retrieval caching, prompt caching, and response caching. From a production perspective,
    I would implement PII masking, authentication and authorization, multi-tenant isolation, observability,
    and continuous monitoring to ensure the system remains secure, scalable, and reliable.

"""