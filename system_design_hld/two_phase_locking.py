"""
# TWO-PHASE LOCKING (2PL)

1. What is Two-Phase Locking (2PL)?

- 2PL = a pessimistic concurrency-control protocol where a transaction follows two separate phases for acquiring and releasing locks.
- It is a type of pessimistic locking.
- The two phases are:
  - Growing Phase → acquire locks.
  - Shrinking Phase → release locks.

  Number of
  Locks Held
       │
       │        /\
       │       /  \
       │      /    \
       │     /      \
       │____/________\______ Time
          Growing   Shrinking


2. What is the Growing Phase?

- Growing Phase = the transaction can acquire new locks but cannot release any lock.
- Number of locks held can only increase.

  Lock A → Lock B → Lock C
     ↑
  Only acquire


3. What is the Shrinking Phase?

- Shrinking Phase = the transaction can release locks but cannot acquire any new locks.
- Once the first lock is released, the transaction has entered the shrinking phase.

  Unlock A → Unlock B → Unlock C
      ↑
  Only release


4. What is NOT 2PL?

- This is NOT allowed:

  Lock A
    ↓
  Unlock A
    ↓
  Lock B
    ↓
  Unlock B

- Why?
  - After Unlock A, the transaction entered the shrinking phase.
  - It cannot acquire Lock B afterward.

- Core rule:

  Growing  →  Shrinking
  Acquire      Release

  Never:

  Acquire → Release → Acquire


5. What are the main types of 2PL?

- Basic 2PL
- Conservative 2PL / Static 2PL
- Strong Strict 2PL / Rigorous 2PL


6. What are Shared and Exclusive locks?

- Shared Lock (S) = read lock; multiple transactions can usually hold shared locks simultaneously.
- Exclusive Lock (X) = write lock; prevents conflicting access by other transactions.

- Typical compatibility:

              Existing
              S       X
  Request S   ✓       ✗
  Request X   ✗       ✗


7. What is Basic 2PL?

- Basic 2PL = locks are acquired dynamically as needed during the growing phase.
- A transaction may release a lock at any point.
- Once it releases its first lock, it enters the shrinking phase and cannot acquire another lock.

  T1:
  Lock-X(A)
      ↓
  Lock-X(B)
      ↓
  Work
      ↓
  Unlock(A)  ← Shrinking starts
      ↓
  Unlock(B)
      ↓
  Commit

- Commit can also release all remaining locks simultaneously.
- Therefore, explicit unlocks are not always required before commit.


8. What are the two major problems with Basic 2PL?

- Deadlock = transactions wait for each other indefinitely.
- Cascading Abort = failure of one transaction forces dependent transactions to abort.


9. How does a deadlock occur?

- Deadlock = a circular waiting condition where transactions wait for locks held by one another.

Example:

  T1                    T2
   │                     │
  Lock-X(A)            Lock-X(B)
   │                     │
  Request B ────────────→│
   │                    holds B
   │                     │
  waits                  │
                          │
  Request A ←─────────────
          waits

- T1 waits for T2 to release B.
- T2 waits for T1 to release A.
- Neither can proceed.
- This creates a deadlock.


10. Can deadlock happen with only one data item?

- Yes.
- Lock Conversion = upgrading a lock from one type to another, typically S → X.

Example:

  T1                    T2
   │                     │
  Lock-S(A)             Lock-S(A)
   │                     │
   └── Both can read ────┘
          ↓
  Upgrade S → X
   │                     │
  T1 waits               T2 waits
   │                     │
   └────── Deadlock ─────┘

- Both transactions hold S(A).
- Both request X(A).
- Each waits for the other to release S(A).
- Neither can proceed.


11. How can deadlocks be handled?

- Main strategies:
  1. Timeout
  2. Wait-For Graph
  3. Conservative 2PL
  4. Timestamp-based schemes
     - Wait-Die
     - Wound-Wait


12. What is Timeout-based deadlock handling?

- Timeout = abort a transaction if it waits for a lock longer than a predefined limit.

  Waiting
     ↓
  Timeout exceeded
     ↓
  Abort transaction

- Advantage:
  - Simple.

- Disadvantage:
  - It may abort a transaction that was simply waiting for a long-running transaction, even when no deadlock existed.


13. What is a Wait-For Graph (WFG)?

- Wait-For Graph = directed graph representing which transaction is waiting for which other transaction.

- Node = transaction.
- Edge Ti → Tj = Ti is waiting for Tj.

Example:

  T1 → T2
  T2 → T3
  T3 → T1

- Cycle exists:

  T1 → T2 → T3 → T1

- Cycle = deadlock.


14. How is a deadlock resolved using a Wait-For Graph?

- Detect a cycle in the WFG.
- Select one transaction as the victim.
- Abort the victim.
- Release its locks.
- Other transactions can then continue.

- Victim Selection = choosing which transaction should be aborted to break the deadlock.

- Factors considered:
  - Work already completed.
  - How close it is to completion.
  - Rollback cost.
  - Number of deadlock cycles it participates in.


15. What is Conservative 2PL?

- Conservative 2PL = Static 2PL where a transaction obtains ALL required locks before it starts execution.

  Transaction starts
       ↓
  Request ALL locks
       ↓
  Can acquire all?
    /       \
  YES       NO
   ↓         ↓
 Execute    Wait
   ↓
 Release

- If even one required lock is unavailable:
  - No locks are granted.
  - Transaction waits without holding partial locks.

- Main benefit:
  - Deadlocks are prevented by design.

- Why?
  - A transaction never holds some locks while waiting for additional locks.

- Main disadvantages:
  - Lower concurrency.
  - Transaction must know all required data in advance.
  - Locks may be held longer.
  - Higher planning/management overhead.
  - Rarely used in practice.


16. What are timestamp-based deadlock schemes?

- Timestamp = unique ordering assigned to a transaction when it starts.
- Older transaction = lower timestamp.
- Newer transaction = higher timestamp.

- Two major schemes:
  - Wait-Die
  - Wound-Wait


17. What is Wait-Die?

- Wait-Die = non-preemptive timestamp-based deadlock prevention scheme.

- Older requests lock held by newer:
  - Older transaction → WAIT.

- Newer requests lock held by older:
  - Newer transaction → DIE/ABORT.

  Older → requests newer's lock → WAIT
  Newer → requests older's lock → ABORT


18. What is Wound-Wait?

- Wound-Wait = preemptive timestamp-based deadlock prevention scheme.

- Older requests lock held by newer:
  - Older transaction → WOUNDS newer → newer aborts.

- Newer requests lock held by older:
  - Newer transaction → WAIT.

  Older → requests newer's lock → ABORT newer
  Newer → requests older's lock → WAIT


19. What is a Cascading Abort?

- Cascading Abort = when one transaction aborts and forces other transactions that depended on its uncommitted data to abort.

Example:

  Initial:
  A = 10

  T1:
  Lock-X(A)
      ↓
  Update A = 11
      ↓
  Unlock(A)
      ↓
  T2 reads A = 11
      ↓
  T1 ABORTS
      ↓
  A rolls back to 10
      ↓
  T2's read was based on invalid data
      ↓
  T2 must ABORT

- Dirty Read = reading data written by another transaction before that transaction commits.
- If T2 has already influenced T3, then T3 may also need to abort.

  T1 aborts
      ↓
  T2 aborts
      ↓
  T3 aborts
      ↓
  T4 aborts
      ↓
  Cascading Abort


20. Why does Basic 2PL allow cascading aborts?

- Basic 2PL allows a transaction to release locks before Commit.
- Another transaction can then acquire the released lock and read uncommitted data.

  T1:
  Write A = 11
      ↓
  Unlock A
      ↓
  T2 reads A = 11
      ↓
  T1 aborts
      ↓
  T2 has read invalid data

- Therefore, Basic 2PL does NOT guarantee prevention of cascading aborts.


21. What is Strong Strict 2PL / Rigorous 2PL?

- Strong Strict 2PL = a stricter form of 2PL where a transaction keeps all its locks until Commit or Abort.
- It can acquire locks dynamically.
- It cannot release any lock before the transaction ends.

  Growing Phase
  Lock A
    ↓
  Lock B
    ↓
  Lock C
    ↓
  Commit / Abort
    ↓
  Release ALL locks


22. How does Strong Strict 2PL prevent cascading aborts?

- Because locks are held until Commit/Abort.
- Other transactions cannot read/write conflicting uncommitted data.

  T1:
  Write A
     ↓
  Hold X(A)
     ↓
  T2 requests S(A)
     ↓
  BLOCKED
     ↓
  T1 commits
     ↓
  T1 releases A
     ↓
  T2 reads committed A

- Therefore:
  - Dirty reads are prevented.
  - Cascading aborts are prevented.


23. Does Strong Strict 2PL prevent deadlocks?

- NO.
- Locks are still acquired dynamically.
- Two transactions can still acquire different locks and wait for each other.

- Therefore:
  - Cascading aborts → prevented.
  - Deadlocks → still possible.

- Deadlocks can be detected/resolved using mechanisms such as a Wait-For Graph.


24. What is the trade-off of Strong Strict 2PL?

- Advantage:
  - Prevents dirty reads.
  - Prevents cascading aborts.
  - Provides strong consistency.

- Disadvantage:
  - Locks are held longer.
  - Therefore concurrency is lower than Basic 2PL.
  - Deadlocks are still possible.


25. How do Basic, Conservative and Strong Strict 2PL differ?

  ┌──────────────────────┬────────────┬───────────────┬─────────────────┐
  │ Feature              │ Basic 2PL  │ Conservative  │ Strong Strict  │
  ├──────────────────────┼────────────┼───────────────┼─────────────────┤
  │ Lock acquisition     │ Dynamic    │ All at start  │ Dynamic         │
  │ Lock release         │ During/end │ After work    │ Only at end     │
  │ Deadlock             │ Possible   │ Prevented     │ Possible        │
  │ Cascading abort      │ Possible   │ Possible      │ Prevented       │
  │ Concurrency          │ High       │ Low           │ Medium          │
  │ Industry usage       │ Less       │ Rare          │ Common          │
  └──────────────────────┴────────────┴───────────────┴─────────────────┘


26. Why can Basic 2PL produce an inconsistent read?

- Consider a bank transfer:

  Initial:
  A = 100
  B = 100
  Total = 200

  T1 transfers 10 from A → B.

  T1:
  A = 90
      ↓
  Unlock A

  T2:
  Reads A = 90
      ↓
  Reads B = 100
      ↓
  Sum = 190

  T1:
  B = 110
      ↓
  Commit

- T2 observed the money "in flight":
  - A already decreased.
  - B had not yet increased.
- Therefore T2 calculated 190 instead of the correct total 200.


27. How does Conservative 2PL handle the same bank-transfer scenario?

- T1 obtains locks on BOTH A and B before modifying either.

  T1:
  Lock-X(A)
  Lock-X(B)
      ↓
  A = 90
  B = 110
      ↓
  Commit
      ↓
  Release locks

- T2 cannot acquire A and B while T1 holds them.
- After T1 commits:

  T2 reads:
  A = 90
  B = 110

  Total = 200

- The transaction also avoids deadlock because it does not hold partial locks while waiting for additional locks.


28. How does Strong Strict 2PL handle the bank-transfer scenario?

- T1 dynamically acquires locks:

  T1:
  Lock-X(A)
      ↓
  A = 90
      ↓
  Lock-X(B)
      ↓
  B = 110
      ↓
  Commit
      ↓
  Release A and B

- T2 requests S(A) while T1 holds X(A).
- T2 is blocked.
- After T1 commits, T2 gets the locks and reads:

  A = 90
  B = 110

  Total = 200

- T2 never sees T1's intermediate state.
- Therefore, the read is consistent and cascading aborts are prevented.


29. What is the most important difference between Basic and Strong Strict 2PL?

- Basic 2PL:

  Acquire → Release whenever needed → No more acquisition

- Strong Strict 2PL:

  Acquire → Acquire → Acquire → Commit/Abort → Release ALL

- The key difference:

  Basic 2PL can release locks before Commit.

  Strong Strict 2PL holds all locks until Commit/Abort.


30. What is the relationship between 2PL and pessimistic locking?

- Pessimistic Locking = assume conflicts may occur, so locks are acquired before accessing/modifying shared data.
- 2PL = a specific pessimistic locking protocol that controls WHEN locks can be acquired and released.
- Strong Strict 2PL is a stricter version commonly used in database systems.


31. What are the key interview takeaways?

- 2PL has two phases:
  - Growing → acquire only.
  - Shrinking → release only.

- Basic 2PL:
  - Dynamic locking.
  - Deadlocks possible.
  - Cascading aborts possible.

- Conservative 2PL:
  - Acquire all locks at the beginning.
  - Deadlocks prevented.
  - Lower concurrency.
  - Requires knowing all required locks in advance.

- Strong Strict 2PL:
  - Acquire locks dynamically.
  - Release ALL locks only at Commit/Abort.
  - Prevents dirty reads and cascading aborts.
  - Deadlocks still possible.

- Wait-For Graph:
  - Detects deadlocks through cycles.
  - One transaction is selected as the victim and aborted.

- Wait-Die:
  - Older waits.
  - Newer dies.

- Wound-Wait:
  - Older wounds newer.
  - Newer waits.

- Core memory trick:

  Basic:
  "Can release early."

  Conservative:
  "Take everything first."

  Strong Strict:
  "Hold everything till the end."

  Deadlock:
  "Who is waiting for whom?"

  WFG:
  "Cycle = Deadlock."

"""