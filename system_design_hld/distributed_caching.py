"""
1. WHAT IS DISTRIBUTED CACHING?
    ------------------------------------------------------------
    Distributed Cache =
    A shared cache used by multiple application servers.

    App 1 ─┐
    App 2 ─┼──→ Redis ──→ DB
    App 3 ─┘

    Benefits:
    - Faster reads
    - Reduces DB load
    - Shared across servers


============================================================
2. CACHE-ASIDE
============================================================

    Application manages the cache.

    READ:
    App → Cache
          ↓ MISS
         DB → Cache

    Example:
    Redis MISS → read user from DB → store in Redis.

    Best for:
    - General read-heavy systems

    Memory:
    "App handles cache miss."


============================================================
3. READ-THROUGH
============================================================

    Cache manages the DB read on a miss.

    READ:

    App → Cache
           ↓ MISS
          DB
           ↓
        Cache
           ↓
          App

    Difference:

    Cache-Aside:
    App handles DB lookup.

    Read-Through:
    Cache handles DB lookup.

    Memory:
    "Cache handles miss."


============================================================
4. WRITE-AROUND
============================================================

    Writes bypass cache.

    WRITE:

    App → DB

    Cache is not updated.

    Later:
    READ → Cache MISS → DB → Cache

    Best for:
    - Data written frequently but rarely read
    - Avoiding cache pollution

    Memory:
    "Write around the cache."


============================================================
5. WRITE-THROUGH
============================================================

    Cache + DB are updated synchronously.

    WRITE:

    App → Cache → DB

    Example:
    Update price:
    Redis = ₹120
    DB = ₹120

    Advantage:
    - Cache stays fresh

    Disadvantage:
    - Higher write latency

    Memory:
    "Write THROUGH cache to DB."


============================================================
6. WRITE-BACK / WRITE-BEHIND
============================================================

    Cache is updated first.
    DB is updated asynchronously.

    WRITE:

    App → Cache
           ↓
       Async Queue
           ↓
          DB

    Advantage:
    - Very fast writes
    - Good for high write volume

    Risk:
    - DB temporarily stale
    - Possible data loss if async pipeline is not durable

    Memory:
    "Write cache now, DB later."


============================================================
7. MOST IMPORTANT COMPARISON
============================================================

    Strategy       Main Idea                  Best For
    ------------------------------------------------------------
    Cache-Aside    App handles cache miss     Read-heavy
    Read-Through   Cache handles cache miss   Simpler read abstraction
    Write-Around   Write directly to DB       Avoid cache pollution
    Write-Through  Cache → DB synchronously   Fresh cache
    Write-Back     Cache → DB asynchronously  Fast/high-volume writes


============================================================
MEMORY TRICK
============================================================

    READ:

    CACHE-ASIDE
    → App handles miss

    READ-THROUGH
    → Cache handles miss


    WRITE:

    WRITE-AROUND
    → Skip cache

    WRITE-THROUGH
    → Cache + DB now

    WRITE-BACK
    → Cache now, DB later


ONE-LINE:
    "Cache-aside and read-through describe how reads handle misses;
    write-around, write-through and write-back describe how writes
    interact with the cache and database."

"""