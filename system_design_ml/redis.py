"""
1. What is caching ?
    Caching means storing frequently accessed data in a faster storage layer so
        we don't repeatedly access the slower source.

2. What is Cache-Aside pattern ?

    Example:
        def get_user(user_id):

            key = f"user:{user_id}"

            # 1. Check cache
            cached = redis.get(key)

            if cached:
                return deserialize(cached)

            # 2. Cache miss → DB
            user = db.get_user(user_id)

            # 3. Populate cache
            redis.setex(
                key,
                300,
                serialize(user)
            )

            return user

        Flow:

            Request
                ↓
              Redis
             /     \
          HIT       MISS
           ↓          ↓
        Return       DB
                     ↓
                   Redis
                     ↓
                   Return


3. What is Redis and why would you use it?

    - Redis is an in-memory data store commonly used for low-latency caching, sessions, counters, rate limiting and other fast-access state.
    - For caching, it reduces database load and latency.

3. Why Redis ?

    - Redis is an in-memory data store commonly used for:
        - Caching
        - Sessions
        - Rate limiting
        - Distributed locks
        - Counters
        - Queues/streams in some architectures
        - Temporary state

    - Its primary attraction for caching is very low latency compared with going to a database for every request.

    Think of :
        -> In-memory key-value store
        → low latency
        → caching
        → sessions
        → distributed locks
        → counters
        → rate limiting

4 . Should we use Redis?
    - I'd use Redis if repeated reads justify the additional cache complexity.
    - I'd need to define TTL, invalidation strategy, consistency expectations and behavior
        when Redis is unavailable.


5. What is TTL ?

    - Time To Live:
        redis.setex(
            "user:123",
            300,
            data
        )

    The value expires after 300 seconds.


6. Three common caching strategies:
    - Cache-Aside: Application manages cache.
    - Write-through: Application writes to cache, and cache synchronously writes to DB.
    - Write-Behind / Write-Back: Application writes cache first, and DB update happens asynchronously.

7. What happens if Redis goes down?
    - Redis unavailable ->> fallback to DB

8. What is Cache stampede or cache thundering herd ?

    - Suppose a popular key expires at exactly the same time your DB gets hammered.
    - Solutions include:
        - Locking
        - Request coalescing
        - TTL jitter
        - Early refresh
        - Background refresh

9. What is Cache penetration ?
    - Suppose attackers repeatedly request /user/999999999, which doesn't exist.
    - For every request, DB keep getting hit.
    - A solution is negative caching:
            "user:999999999" → NOT_FOUND
            with a short TTL.

10. What is Cache eviction ?
    - Redis has limited memory, so what happens when memory fills?
    - So Redis has eviction policy:
        - allkeys-lru
        - volatile-lru
        - allkeys-lfu
        - volatile-ttl
        - noeviction

11. What are LRU and LFU ?
    - LRU → Least Recently Used
    - LFU → Least Frequently Used


12. Redis vs CDN?
    - CDN caches content at geographically distributed edge locations close to users, while
    - Redis is generally an application-side distributed cache used for dynamic data and fast application access.

"""