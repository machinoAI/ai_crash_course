"""
STEP 1 — CLARIFY REQUIREMENTS
------------------------------------------------------------
    Functional:
    1. Create a short URL from a long URL.
    2. Redirect short URL to the original URL.
    3. Optional: expiration and analytics.

    Non-functional:
    - Very low redirect latency
    - Highly available
    - Durable URL mappings
    - Must scale to high read traffic."


============================================================
STEP 2 — ESTIMATE SCALE
============================================================

    "Let's assume:

    100M URLs created/month
    and 10B redirects/month.

    So redirects are much higher than writes.

    Therefore this is a READ-HEAVY system.

    I'd optimize the redirect path."


============================================================
STEP 3 — DEFINE APIs
============================================================

    POST /shorten

    Request:
    {
      "url": "https://example.com/very/long/url"
    }

    Response:
    {
      "short_url": "https://tiny.com/aB72xK"
    }


    GET /aB72xK

    → HTTP 302/307 redirect
    → original URL


============================================================
STEP 4 — HIGH-LEVEL ARCHITECTURE
============================================================

                 Client
                   ↓
              Load Balancer
                   ↓
             URL Service
              /        \
             ↓          ↓
          Redis        DB
             ↑
             └── Cache


        CREATE:
            Client
             ↓
            URL Service
             ↓
            Generate ID
             ↓
            Base62
             ↓
            DB


        REDIRECT:
            Client
             ↓
            URL Service
             ↓
            Redis
             ↓ MISS
            DB
             ↓
            Redis
             ↓
            Redirect


============================================================
STEP 5 — HOW DO WE GENERATE SHORT CODES?
============================================================

        "I need a unique short key.

        I'd generate a unique numeric ID using something like
        a distributed ID generator, then encode it using Base62."

        Example:

        123456789
            ↓
         Base62
            ↓
        "aB72xK"

        Base62 uses:
            0-9 + a-z + A-Z
            = 62 characters

        Advantages:
            - Short
            - URL-safe
            - Efficient


        DB should enforce:

        UNIQUE(short_code)


============================================================
STEP 6 — HANDLE THE REDIRECT PATH
============================================================

    "This is the critical path because reads are much higher."

    GET /aB72xK

            ↓
          Redis
         /     \
       HIT     MISS
        ↓        ↓
     return      DB
                 ↓
               Redis
                 ↓
               return

    This gives us low latency and protects the DB.


============================================================
STEP 7 — SCALE THE SYSTEM
============================================================

    Application:

    Load Balancer
          ↓
    App 1
    App 2
    App 3
    ...
    App N

    Stateless application servers
    → horizontally scalable.

    Redis:
    → Redis Cluster / replication

    Database:
    → primary + replicas initially

    At very large scale:
    → shard by short_code/hash


============================================================
STEP 8 — IMPORTANT FAILURE/EDGE CASES
============================================================

    1. Cache failure

        Redis unavailable
        → fallback to DB

    But protect DB with:
    - rate limiting
    - circuit breaker
    - connection limits


    2. Hot URL

    One URL receives millions of requests.

    Solutions:
        - Cache aggressively
        - Local cache
        - Replicate hot entries


    3. Expiration

        Store:

        expires_at

        If expired:
        → return 404/410


    4. Analytics

        Don't write analytics synchronously during redirect.

        Instead:

        Redirect
           ↓
        Kafka / Queue
           ↓
        Analytics service


    5. Security

        - URL validation
        - Rate limiting
        - Abuse/phishing detection


============================================================
STEP 9 — TRADE-OFFS
============================================================

    "I'd choose Base62 over random strings because it avoids
    unnecessary collision checking.

    I'd use Redis because redirects are read-heavy.

    I'd keep analytics asynchronous because it should not increase
    redirect latency.

    I'd start with a relational DB because the mapping is simple
    and needs uniqueness/durability, then shard when scale requires it."


============================================================
30-SECOND CLOSING ANSWER
============================================================

    "The system is a read-heavy URL mapping service.

    For creation, I generate a unique distributed ID, encode it
    with Base62, and store the short_code → long_url mapping in
    a database with a unique constraint.

    For redirects, I put Redis in front of the DB using cache-aside:
    check Redis first, fall back to DB on a miss, populate the cache,
    and return a 302/307 redirect.

    The application tier is stateless and horizontally scalable.
    At larger scale I'd use Redis clustering and database sharding/
    replication. I'd also handle hot keys, expiration, rate limiting,
    security, and send analytics asynchronously through Kafka or
    another queue."

Final Architecture:
                     ┌─────────────────────┐
                 │      LONG URL       │
                 │ https://linkedin... │
                 └──────────┬──────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │ URL Service  │
                    └──────┬───────┘
                           │
                  Generate Unique ID
                           │
                           ▼
                    ┌──────────────┐
                    │  ZooKeeper   │
                    │ Coordination │
                    └──────┬───────┘
                           │
                        Unique ID
                           │
                           ▼
                    ┌──────────────┐
                    │   Base62     │
                    │   Encoding   │
                    └──────┬───────┘
                           │
                     Short Code
                     e.g. aB72xK
                           │
                           ▼
                    ┌──────────────┐
                    │   Database   │
                    │              │
                    │ aB72xK ──────┼──→ Long URL
                    └──────┬───────┘
                           │
                           ▼
                  https://lnkd.in/aB72xK


Redirect path:
      USER
       │
       │ GET /aB72xK
       ▼
┌───────────────┐
│  URL Service  │
└───────┬───────┘
        │
        ▼
   ┌─────────┐
   │  Redis  │
   └────┬────┘
        │
    ┌───┴────┐
    │        │
   HIT      MISS
    │        │
    │        ▼
    │    ┌─────────┐
    │    │   DB    │
    │    └────┬────┘
    │         │
    │         ▼
    │      Store in
    │       Redis
    │         │
    └────┬────┘
         ▼
    Original URL
         │
         ▼
      302 / 307
      Redirect


"""