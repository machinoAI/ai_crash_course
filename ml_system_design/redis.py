"""
1. What is Redis?

    Think of :
        -> In-memory key-value store
        → low latency
        → caching
        → sessions
        → distributed locks
        → counters
        → rate limiting

2. Should we use Redis?
    - I'd use Redis if repeated reads justify the additional cache complexity.
    - I'd need to define TTL, invalidation strategy, consistency expectations and behavior
        when Redis is unavailable.


3.
"""