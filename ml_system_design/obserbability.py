"""
1. What is observability?
    - Observability is the ability to understand the internal state and behavior of a system from
        its external outputs, primarily using logs, metrics and traces.

2. Logs vs metrics vs traces?
    - Logs tell me what happened, metrics tell me how much/how often,
        and traces tell me where a request spent time or failed across distributed services.

3. How would you debug a slow API?

    1. Check latency metrics
    2. Look at P95/P99
    3. Check distributed trace
    4. Identify slow dependency
    5. Check logs for errors/timeouts
    6. Check DB/cache metrics
    7. Check CPU/memory/resource saturation

4. What would you monitor for an AI/RAG application?
    API latency
    LLM latency
    TTFT
    Token consumption
    LLM errors
    Embedding latency
    Retrieval latency
    Vector DB errors
    Cache hit rate
    RAG retrieval quality
    Model output errors
    CPU/GPU utilization

    retrieval Recall@K
    context relevance
    answer correctness


5. How would you detect that a downstream service is failing?
    Multiple signals:
        - Error rate ↑
        - Latency ↑
        - Timeouts ↑
        - Circuit breaker OPEN
        - Health checks failing


"""