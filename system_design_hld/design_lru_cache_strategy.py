"""
============================================================
SYSTEM DESIGN / LLD: LRU CACHE WITH THREAD SAFETY
============================================================

1. REQUIREMENTS
------------------------------------------------------------

Operations:

get(key)
→ return value if present
→ mark key as MOST RECENTLY USED

put(key, value)
→ insert/update value
→ mark key as MOST RECENTLY USED
→ if capacity exceeded, remove LEAST RECENTLY USED key


Example:

Capacity = 3

A, B, C

Access A:

B ← C ← A
            ↑
          MRU

A = Most Recently Used
B = Least Recently Used

Add D:

C, A, D
B is evicted.


============================================================
2. DATA STRUCTURE
------------------------------------------------------------

We need:

1. HashMap
   → O(1) lookup

2. Doubly Linked List
   → O(1) insert/remove/move

Why Doubly Linked List?

We need to move a recently accessed node to the front
and remove the least recently used node from the end.

Architecture:

HashMap
  key
   ↓
  Node
   ↓
Doubly Linked List

HEAD                         TAIL
 ↓                             ↓
[MRU] ↔ [Node] ↔ [Node] ↔ [LRU]

HEAD = Most Recently Used
TAIL = Least Recently Used


============================================================
3. GET(key)
------------------------------------------------------------

get(A)

1. Lookup A in HashMap → O(1)
2. If absent → return MISS
3. Remove A from current position
4. Move A to HEAD
5. Return value

Example:

Before:

A ↔ B ↔ C

get(B)

After:

B ↔ A ↔ C


Because B is now most recently used.


============================================================
4. PUT(key, value)
------------------------------------------------------------

Case 1: Key already exists

put(B, newValue)

→ update value
→ move B to HEAD


Case 2: Key does not exist

put(D, value)

→ create Node D
→ insert D at HEAD
→ add D to HashMap


If capacity exceeded:

→ remove TAIL
→ delete its key from HashMap


Example:

Capacity = 3

A ↔ B ↔ C

put(D)

D ↔ A ↔ B

C is evicted.


============================================================
5. WHY BOTH HASHMAP + LINKED LIST?
------------------------------------------------------------

HashMap alone:

GET → O(1)

But:
Find/remove LRU → O(N)

Linked List alone:

Find key → O(N)

Therefore combine:

HashMap
→ O(1) lookup

Doubly Linked List
→ O(1) reorder + eviction

Final:

GET  → O(1)
PUT  → O(1)


============================================================
6. THREAD SAFETY
------------------------------------------------------------

The critical issue:

get() is NOT actually read-only.

Why?

Because:

get(A)
→ moves A to HEAD

Therefore get() modifies the linked list.

Example:

Thread 1:
get(A)

Thread 2:
get(B)

Both modify:
HEAD ↔ nodes ↔ TAIL

Without synchronization:

❌ Race condition
❌ Corrupted pointers
❌ Incorrect ordering
❌ Possible lost updates


============================================================
7. SIMPLE THREAD-SAFE DESIGN
------------------------------------------------------------

Protect the entire cache operation using a lock.

For example:

Lock
  ↓
get()
put()
  ↓
Unlock


Java-style:

synchronized get()
synchronized put()


This guarantees only one thread modifies the cache
at a time.

Trade-off:

✅ Simple
✅ Correct

❌ Lower concurrency


============================================================
8. BETTER APPROACH FOR HIGH CONCURRENCY
------------------------------------------------------------

Use a ReentrantReadWriteLock?

BUT:

get() modifies the LRU order.

Therefore get() requires a WRITE LOCK,
not a READ LOCK.

So a normal ReadWriteLock provides less benefit
than people often expect here.

Alternative:

Use segmented/sharded LRU caches.

Example:

             Cache
          /    |    \
       Shard1 Shard2 Shard3

Each shard has its own lock.

This reduces lock contention.

However, a globally perfect LRU order becomes more complex.

For an interview, start with:

ONE LOCK + HashMap + Doubly Linked List.


============================================================
9. THREAD-SAFE ARCHITECTURE
------------------------------------------------------------

              ┌──────────────┐
Thread 1 ───→ │              │
Thread 2 ───→ │   LRU Cache  │
Thread 3 ───→ │              │
              └──────┬───────┘
                     │
                  LOCK
                     │
             ┌───────┴───────┐
             │               │
          HashMap       Doubly List
             │               │
          O(1) lookup    O(1) reorder


============================================================
10. EDGE CASES
------------------------------------------------------------

Capacity = 0
→ reject/handle put

get(non-existing)
→ return MISS

put(existing key)
→ update value + move to HEAD

Capacity exceeded
→ evict TAIL

Concurrent get/put
→ protected by lock


============================================================
11. COMPLEXITY
------------------------------------------------------------

Operation       Time
----------------------
get             O(1)
put             O(1)
eviction        O(1)
remove          O(1)

Space:
O(capacity)


Summary:

    I'd implement the LRU cache using a HashMap plus a doubly
    linked list. The HashMap gives O(1) lookup, while the linked
    list maintains recency: the head is most recently used and the
    tail is least recently used. On every get or put, I move the
    node to the head; when capacity is exceeded, I remove the tail.

    For thread safety, I'd protect get and put with a lock because
    get is also a write operation to the linked-list ordering.
    For higher concurrency, I could shared the cache and use
    per-shard locks, but I'd start with a single lock for correctness
    and simplicity.


============================================================
MEMORY TRICK
============================================================

HASHMAP
→ Find node FAST

DOUBLY LINKED LIST
→ Move / remove FAST

HEAD
→ MRU

TAIL
→ LRU

LOCK
→ Thread safety

RESULT:
O(1) GET + O(1) PUT

"""