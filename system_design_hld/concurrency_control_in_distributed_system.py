"""
CONCURRENCY CONTROL IN DISTRIBUTED SYSTEMS


CORE QUESTION
-------------
    How do we prevent multiple concurrent requests from incorrectly
    modifying the same shared resource?

Classic example:

          User 1 ──┐
          User 2 ──┼──> BOOK SEAT 10 ──> Database
          User 3 ──┘

    Seat 10 = FREE

    Without concurrency control:

    User 1 → reads FREE
    User 2 → reads FREE
    User 3 → reads FREE

    All three think:
    "Seat is available."

    Result:
    User 1 → BOOKED
    User 2 → BOOKED
    User 3 → BOOKED

    ❌ Same seat allocated to 3 users.

    This is a RACE CONDITION / CONCURRENCY BUG.

------------------------------------------------------------
1. CRITICAL SECTION
------------------------------------------------------------

Critical Section =
    Code that accesses/modifies a shared resource.

    Example:

    read seat
       ↓
    check if FREE
       ↓
    mark BOOKED
       ↓
    save

    The dangerous part is:

    IF seat == FREE:
        seat = BOOKED

    Because multiple requests may execute this logic simultaneously.

    Memory:
    "Shared resource + concurrent access = possible race condition."


============================================================
2. WHY `synchronized` IS NOT ENOUGH IN DISTRIBUTED SYSTEMS
============================================================

    On a SINGLE JVM:

    synchronized(bookSeat)
    {
        read seat
        if free:
            book seat
    }

    Only one thread enters at a time.

    But distributed system:

                     Load Balancer
                    /      |      \
                   ↓       ↓       ↓
               Server 1 Server 2 Server 3
                  JVM       JVM      JVM
                    \        |       /
                     Shared DB

    Server 1 has its own lock.
    Server 2 has its own lock.
    Server 3 has its own lock.

    Therefore:

    Server 1: synchronized()
    Server 2: synchronized()
    Server 3: synchronized()

    These locks do NOT coordinate with each other.

    IMPORTANT:
    Process-level/thread-level locks ≠ Distributed locks/concurrency control.

    The database or a distributed coordination mechanism
    must provide the shared coordination.


============================================================
3. THREE FOUNDATIONS
============================================================

    Before OCC/PCC understand:

    1. Transactions
    2. Locks
    3. Isolation Levels


============================================================
4. TRANSACTIONS
============================================================

    Transaction =
    A group of database operations treated as ONE logical unit.

    Goal:
    Either everything succeeds or everything fails.

    Example: Bank Transfer

    A = ₹100
    B = ₹50

    Transfer ₹20:

    A → ₹80
    B → ₹70

    Transaction:

    BEGIN

    A = A - 20
    B = B + 20

    COMMIT

    If second operation fails:

    ROLLBACK

    A returns to ₹100
    B remains ₹50

    Without transaction:

    A = ₹80
    B = ₹50

    ₹20 has effectively disappeared.

    Key idea:

    TRANSACTION = ATOMIC UNIT OF WORK


    ACID:
    A = Atomicity
    C = Consistency
    I = Isolation
    D = Durability


    For concurrency-control interviews,
    the most important one here is:

    I = Isolation


============================================================
5. DATABASE LOCKS
============================================================

    Two basic conceptual lock types:

    S = Shared Lock
    X = Exclusive Lock


    Shared Lock (S):
    Used when protecting/read-locking data for concurrent transactions.

    Multiple compatible S locks can coexist.

    Example:

    T1 → S-lock Row A
    T2 → S-lock Row A

    Allowed.

    Exclusive Lock (X):
    Used when modifying data.

    X-lock conflicts with other incompatible locks.

    Simplified compatibility:

              S       X
           ----------------
    S      | YES   |  NO
    X      | NO    |  NO

    Think:

    S = "I want to read/protect this row."

    X = "I want to modify this row."


IMPORTANT DATABASE NUANCE
-------------------------
    Do NOT blindly say:

    "Every SELECT gets an S-lock."

    That is too simplistic for modern databases.

    Systems such as PostgreSQL use MVCC, where ordinary reads can often
    proceed without blocking writers in the way a textbook S-lock model
    suggests. PostgreSQL explicitly documents row-level locking separately
    from ordinary reads. :contentReference[oaicite:2]{index=2}


============================================================
6. ISOLATION LEVELS
============================================================

    Isolation defines how much one transaction can observe
    the effects of concurrent transactions.

    Three classic anomalies:

------------------------------------------------------------
A. DIRTY READ
------------------------------------------------------------

    T1:
    seat = BOOKED
    but NOT COMMITTED

    T2:
    reads BOOKED

    T1:
    ROLLBACK

    Actual database value:
    FREE

    T2 read something that never committed.

    => DIRTY READ


------------------------------------------------------------
B. NON-REPEATABLE READ
------------------------------------------------------------

    T1:
    READ seat → FREE

    T2:
    UPDATE seat → BOOKED
    COMMIT

    T1:
    READ same seat again → BOOKED

    Same transaction
    Same row
    Different value.

    => NON-REPEATABLE READ


------------------------------------------------------------
C. PHANTOM READ
------------------------------------------------------------

    T1:
    SELECT seats WHERE price < 500

    Result:
    Seat 1
    Seat 3

    T2:
    INSERT Seat 2 with price 400
    COMMIT

    T1:
    runs same query again

    Result:
    Seat 1
    Seat 2
    Seat 3

    A new ROW appears in the result set.

    => PHANTOM READ


------------------------------------------------------------
STANDARD ISOLATION LEVELS
------------------------------------------------------------

                        Dirty   Non-repeatable   Phantom
                        Read       Read            Read

    READ UNCOMMITTED      ✓          ✓              ✓
    READ COMMITTED        ✗          ✓              ✓
    REPEATABLE READ       ✗          ✗              ✓*
    SERIALIZABLE          ✗          ✗              ✗

    *Standard minimum guarantee.

    Important:
    Actual database implementations can provide stronger behavior.

    Memory trick:

    READ UNCOMMITTED → trust nobody

    READ COMMITTED → don't see uncommitted data

    REPEATABLE READ → same row stays consistent

    SERIALIZABLE → behave as if transactions ran one-by-one


============================================================
7. OPTIMISTIC CONCURRENCY CONTROL (OCC)
============================================================

    PHILOSOPHY:
    - Conflicts are rare.
    - Let everyone work.
    - Check for conflict when writing."

    Instead of blocking readers:

    READ
     ↓
    COMPUTE
     ↓
    VALIDATE
     ↓
    WRITE

    Usually implemented using:

    version number

    Example:

    seat_id | status | version
    --------|--------|--------
    10      | FREE   | 1


    T1 reads:

    status = FREE
    version = 1

    T2 reads:

    status = FREE
    version = 1

    Both calculate:

    FREE → BOOKED


    T1 writes:

    UPDATE seats
    SET status = 'BOOKED',
        version = version + 1
    WHERE id = 10
    AND version = 1;


    T1 succeeds.

    DB:

    status = BOOKED
    version = 2


    T2 now tries:

    UPDATE seats
    SET status = 'BOOKED',
        version = version + 1
    WHERE id = 10
    AND version = 1;


    No row matches because:

    DB version = 2
    Expected version = 1

    Therefore:

    affected_rows = 0

    => CONFLICT DETECTED

    T2 must:

    ROLLBACK
       ↓
    RETRY / FAIL GRACEFULLY


    CORE OCC PATTERN:

    READ VERSION
         ↓
    DO WORK
         ↓
    CHECK VERSION
         ↓
    UPDATE IF UNCHANGED


    Memory:
    "OCC doesn't prevent conflict.
    It DETECTS conflict."


============================================================
8. PESSIMISTIC CONCURRENCY CONTROL (PCC)
============================================================

    PHILOSOPHY:
    - Conflicts are likely.
    - Lock the resource before modifying it.

    Instead of:

    READ → HOPE → VALIDATE

    we do:

    LOCK → READ → MODIFY → COMMIT


    Example:

    BEGIN;

    SELECT *
    FROM seats
    WHERE id = 10
    FOR UPDATE;

    UPDATE seats
    SET status = 'BOOKED'
    WHERE id = 10;

    COMMIT;


    T1:
    SELECT FOR UPDATE
    → gets lock

    T2:
    SELECT FOR UPDATE
    → BLOCKED

    T1:
    books seat

    T1:
    COMMIT

    Lock released

    T2:
    continues

    T2:
    reads BOOKED

    T2:
    fails to book


    CORE PCC PATTERN:

    LOCK
     ↓
    READ
     ↓
    VALIDATE
     ↓
    UPDATE
     ↓
    COMMIT
     ↓
    UNLOCK


    Memory: PCC prevents conflict by blocking.


============================================================
9. OCC vs PCC
============================================================

                     OCC                 PCC
    ------------------------------------------------------------
    Assumption       Conflicts rare      Conflicts likely

    Strategy         Detect conflict     Prevent conflict

    Read             Usually no long     Acquire/hold lock
                     lock

    Write            Validate version    Modify locked resource

    Conflict         Rollback/retry      Other transaction waits

    Concurrency      High                Lower under contention

    Best for         Low contention      High contention

    Main cost        Retry cost          Lock/wait cost

    Main risk        Many retries        Blocking/deadlocks


    Simple rule:

    LOW CONTENTION
    → OCC

    HIGH CONTENTION
    → PCC


============================================================
10. SEAT BOOKING EXAMPLE
============================================================

    Case A: OCC

    1000 users try to book different seats.

    Low conflict.

    Most transactions succeed.

    OCC is attractive.


    Case B: Flash-sale seat

    1000 users try to book:

    Seat #10

    Huge contention.

    OCC:

    1000 transactions
    → all read FREE
    → 999 eventually discover conflict
    → lots of rollback/retry

    Very wasteful.

    PCC:

    First transaction locks Seat #10.
    Others wait.

    Only one can modify it at a time.

    High contention:
    PCC may be better.


============================================================
11. DEADLOCK
============================================================

    Deadlock =
    Two or more transactions wait for each other forever.

    Classic example:

    T1:
    locks A
    tries to lock B

    T2:
    locks B
    tries to lock A


              T1
              |
          holds A
              |
          wants B
              |
              ↓
              T2
              |
          holds B
              |
          wants A
              |
              └──────────→ T1


    Circular wait.

    T1 waits for T2.
    T2 waits for T1.

    Nobody progresses.


============================================================
12. HOW DATABASES HANDLE DEADLOCKS
============================================================

    Database detects circular dependency.

    Then:

    T1 ← ABORT / ROLLBACK

    T2 continues.

    Application retries T1.

    Typical strategy:

    DETECT
      ↓
    ABORT ONE TRANSACTION
      ↓
    ROLLBACK
      ↓
    RETRY


    IMPORTANT:
    Deadlock is NOT the same as starvation.

    Deadlock:
    A waits for B
    B waits for A

    Starvation:
    A keeps getting delayed because other work keeps winning.


============================================================
13. HOW TO REDUCE DEADLOCKS
============================================================

    Best technique:

    Acquire locks in a CONSISTENT ORDER.

    Bad:

    T1: Lock A → Lock B
    T2: Lock B → Lock A

    Good:

    T1: Lock A → Lock B
    T2: Lock A → Lock B

    Then circular dependency is avoided.

    Other techniques:

    - Keep transactions short
    - Avoid unnecessary locks
    - Lock only required rows
    - Use appropriate lock ordering
    - Configure lock timeouts
    - Retry aborted transactions

============================================================
14. IMPORTANT CORRECTION ABOUT OCC
============================================================

    The lecture says OCC has "zero deadlock risk."

    Interview-safe explanation:

    "Pure version-validation OCC avoids the long lock-wait pattern normally
    associated with pessimistic locking, but the actual database operation
    still uses database concurrency mechanisms. If a transaction touches
    multiple resources/rows, implementation details can still matter."

    Therefore don't memorise:

    "OCC can NEVER deadlock."

    Better:

    "OCC greatly reduces/avoids deadlocks caused by holding locks during
    the read/compute phase."


============================================================
15. `SELECT FOR UPDATE`
============================================================

    Very important for interviews.

    Example:

    SELECT *
    FROM seats
    WHERE id = 10
    FOR UPDATE;


    Meaning:

    "Return this row and acquire a lock that protects it from conflicting
    concurrent modifications until the transaction ends."

    Example:

    BEGIN;

    SELECT * FROM seats
    WHERE id = 10
    FOR UPDATE;

    -- check status

    UPDATE seats
    SET status = 'BOOKED'
    WHERE id = 10;

    COMMIT;


    Other transaction trying to acquire a conflicting lock:

    → waits

    PostgreSQL documents that `FOR UPDATE` blocks conflicting updates,
    deletes and locking reads on the selected rows until the transaction
    ends. :contentReference[oaicite:6]{index=6}


============================================================
16. `NOWAIT` and `SKIP LOCKED`
============================================================

    Useful senior interview concepts.

    Instead of waiting:

    SELECT *
    FROM seats
    WHERE id = 10
    FOR UPDATE NOWAIT;


    If locked:

    FAIL IMMEDIATELY

    Useful when:
    you do NOT want request latency caused by lock waiting.


    `SKIP LOCKED`:

    SELECT *
    FROM jobs
    FOR UPDATE SKIP LOCKED
    LIMIT 10;


    Meaning:

    "Give me available rows; skip rows currently locked by another worker."

    Very useful for:

    DATABASE-BACKED JOB QUEUES

    PostgreSQL explicitly documents `SKIP LOCKED` as useful for
    multiple consumers accessing queue-like tables. :contentReference[oaicite:7]{index=7}


============================================================
17. INTERVIEW DECISION TREE
============================================================

    Ask:

    Q1. Is contention LOW?

    YES
     ↓
    Use OCC
     ↓
    Version column
     ↓
    Conditional UPDATE
     ↓
    Retry conflict


    Q2. Is contention HIGH?

    YES
     ↓
    Consider PCC
     ↓
    SELECT FOR UPDATE
     ↓
    Serialize access to hot resource


    Q3. Do I need very strong consistency?

    YES
     ↓
    Consider stronger isolation / SERIALIZABLE
    depending on workload and DB.


    Q4. Does the transaction touch multiple rows/resources?

    YES
     ↓
    Think about:
    - lock ordering
    - deadlocks
    - retry
    - transaction duration


============================================================
18. MOST IMPORTANT SQL PATTERNS
============================================================

    OCC:

    UPDATE seats
    SET status = 'BOOKED',
        version = version + 1
    WHERE id = 10
    AND version = 1;


    Success:
    affected_rows = 1

    Conflict:
    affected_rows = 0


    PCC:

    BEGIN;

    SELECT *
    FROM seats
    WHERE id = 10
    FOR UPDATE;

    UPDATE seats
    SET status = 'BOOKED'
    WHERE id = 10;

    COMMIT;


============================================================
19. REAL-WORLD EXAMPLES
============================================================

    OCC is useful for:

    - User profile editing
    - Document editing
    - Inventory with low contention
    - Collaborative records
    - APIs where conflicts are uncommon

    PCC is useful for:

    - Ticket/seat booking
    - Flash-sale inventory
    - Wallet/account balance updates
    - Resource allocation
    - Highly contested counters


============================================================
20. ONE-MINUTE INTERVIEW ANSWER
============================================================

    "Concurrency control prevents multiple concurrent requests from
    corrupting shared state. The two common strategies are optimistic
    and pessimistic concurrency control.

    With OCC, I assume conflicts are rare. Multiple transactions read
    without holding long-lived locks, and before updating I validate a
    version number using a conditional UPDATE. If no row is updated,
    another transaction changed the record, so I rollback and retry.

    With PCC, I assume conflicts are frequent. I explicitly lock the
    resource, for example with SELECT FOR UPDATE, perform the business
    operation, and commit. Other transactions wait for the lock.

    I'd choose OCC for low-contention workloads and PCC for highly
    contended resources such as seat booking or flash-sale inventory.

    I would also choose the isolation level based on consistency
    requirements, keep transactions short, acquire multiple locks in a
    consistent order, and handle deadlocks with rollback and retry."


============================================================
21. 10-SECOND MEMORY VERSION
============================================================

    Concurrency Control
            ↓
    Prevent race conditions
            ↓
       ┌─────────┐
       │   OCC   │
       └─────────┘
       "Detect"
       version check
       retry conflict

            VS

       ┌─────────┐
       │   PCC   │
       └─────────┘
       "Prevent"
       lock first
       others wait


    OCC → Low contention
    PCC → High contention

    Transaction → All or nothing
    Isolation → How concurrent transactions interact
    Lock → Controls conflicting access
    Deadlock → Circular waiting
    Version → Detects OCC conflict


============================================================
FINAL MEMORY TRICK
============================================================

    "TRANSACTION → ISOLATION → LOCK → OCC/PCC → DEADLOCK"

    Transaction:
    Make operations atomic.

    Isolation:
    Control visibility between transactions.

    Lock:
    Control conflicting access.

    OCC:
    Let them work → detect conflict → retry.

    PCC:
    Lock first → others wait.

    Deadlock:
    Detect → rollback one → retry.




22. Decision-Making Notes:

         LOW CONTENTION
             ↓
        OCC
             ↓
        Version check
             ↓
        Retry on conflict


        HIGH CONTENTION / HOT RESOURCE
             ↓
        PCC
             ↓
        SELECT FOR UPDATE
             ↓
        Serialize access


        MULTIPLE LOCKED RESOURCES
             ↓
        Consistent lock ordering
             ↓
        Avoid deadlock
"""