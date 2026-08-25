"""
Rate Limiter: It limits the sudden jump in traffic on applications:

1. Rate Limiter Algorithms:

    1. Token Bucket → Allows requests by consuming tokens that refill at a fixed rate, permitting controlled bursts.

    2. Leaking Bucket → Processes requests at a fixed rate, smoothing bursts by making excess requests wait or get dropped.

    3. Fixed Window Counter → Counts requests within fixed time intervals and rejects requests after the limit is reached.

    4. Sliding Window Log → Stores timestamps of requests and allows a request only if the number of recent requests within the sliding window is below the limit.

    5. Sliding Window Counter → Combines adjacent fixed-window counts to estimate the request count in the current sliding window more accurately.


2. Where to implement Rate Limiter ?
        - API Gateway: → Usually the first place to enforce rate limiting for incoming client requests.

        - Redis: → Used when the rate limiter needs shared state across multiple API servers.

        Typical distributed design:

            Client
              ↓
            API Gateway
              ↓
            Redis (shared rate-limit state)
              ↓
            Backend services


        So in a distributed system, commonly:
            - API Gateway = enforcement point
            - Redis = shared counter/token state

        For a single server, Redis may not be necessary.

3. Important notes:

    1. Rate-limit key → user_id / API key / IP / endpoint, depending on the requirement.
    2. HTTP response → return 429 Too Many Requests when the limit is exceeded.
    3. Distributed state → Redis/shared store; local memory is not enough across servers.
    4. Atomicity → Redis INCR/Lua script or equivalent atomic operation to avoid race conditions.
    5. Burst handling → Token Bucket is commonly preferred when bursts should be allowed.
    6. Fairness → Consider separate limits per user/tenant/API endpoint.
    7. Failure policy → Decide fail-open (allow traffic) vs fail-closed (reject traffic) if Redis is unavailable.
    8. Headers → Optionally return limit/remaining/reset information to clients.
    9. Hierarchical limits → e.g. 1000/user/min + 100/endpoint/min.
    10. Backpressure → Rate limiting protects downstream services from overload.

4. What is Backpressure ?

    - A mechanism where a faster producer is slowed down or limited when the consumer
        cannot process data fast enough, preventing overload.

     - Backpressure → Control the incoming rate when downstream capacity is lower.

    Common implementations:
    1. Queue → Buffer requests until consumers catch up.
    2. Rate Limiter → Limit producer/request rate.
    3. Bounded Queue → When full, block/reject new work.
    4. Worker Pool → Limit concurrent processing.
    5. Retry + Exponential Backoff → Slow retries after failures.
    6. Load Shedding → Drop low-priority requests when overloaded.

    Example:
    Producer: 10,000 req/s
    Consumer: 2,000 req/s

    API → Rate Limit → Bounded Queue → Workers → DB

    If queue is full:
    → reject with 429/503 OR apply backoff.

    Notes:
    - Implement backpressure using a bounded queue, controlled worker concurrency, rate limiting,
        and rejection/backoff when downstream capacity is exhausted.

"""