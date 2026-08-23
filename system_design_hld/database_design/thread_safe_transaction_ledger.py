""""
THREAD-SAFE TRANSACTION LEDGER


1. REQUIREMENT CLARIFICATION
    Functional:
    - Create account
    - Deposit money
    - Withdraw money
    - Transfer money
    - Get account transactions
    - Query transactions by time range

    Clarify:
    - Is negative balance allowed?
    - Do we need transaction history/audit?
    - Can requests be retried?
    - What is the expected traffic/data volume?
    - Single-region or multi-region?


2. UNDERSTANDING BUSINESS WORKFLOW
    Deposit:
    Request → Validate → Update balance → Record transaction → Commit

    Withdraw:
    Request → Validate balance → Update balance → Record transaction → Commit

    Transfer:
    Debit A + Credit B + Record transaction must happen atomically.

    If any step fails:
    → Rollback everything.


3. IDENTIFY ENTITIES / TABLES / FIELDS
    Account:
    - account_id
    - balance_paise
    - created_at

    Transaction:
    - transaction_id
    - account_id / from_account_id / to_account_id
    - type
    - amount_paise
    - timestamp
    - idempotency_key

    Money:
    - Store as integer paise/cents, not float.


4. IDENTIFY QUERIES / ACCESS PATTERNS
    - Get balance by account_id
    - Get transactions by account_id
    - Get transactions by account_id + timestamp range
    - Check idempotency_key

    Example:
    SELECT *
    FROM transaction
    WHERE account_id = ?
    AND timestamp BETWEEN ? AND ?
    ORDER BY timestamp;


5. DESIGN SCHEMA
    ACCOUNT:
    - account_id BIGINT PRIMARY KEY
    - balance_paise BIGINT NOT NULL
    - created_at TIMESTAMP NOT NULL

    TRANSACTION:
    - transaction_id BIGINT PRIMARY KEY
    - account_id BIGINT NOT NULL
    - type VARCHAR NOT NULL
    - amount_paise BIGINT NOT NULL
    - timestamp TIMESTAMP NOT NULL
    - idempotency_key VARCHAR NOT NULL

    For transfer, use from_account_id + to_account_id or two immutable ledger entries.


6. RELATIONSHIPS & CONSTRAINTS
    Relationship:
    - Account 1:N Transaction

    Constraints:
    - PK: account_id, transaction_id
    - FK: transaction.account_id → account.account_id
    - UNIQUE: idempotency_key
    - NOT NULL: amount, timestamp, account_id
    - CHECK: amount_paise > 0
    - CHECK: from_account_id <> to_account_id

    Transaction history should be immutable.


7. INDEXING
    Main query:
    WHERE account_id = ?
    ORDER BY timestamp DESC

    Use:
    INDEX(account_id, timestamp)

    Why:
    - account_id filters first
    - timestamp supports ordering/range retrieval

    Idempotency:
    UNIQUE INDEX(idempotency_key)

    PostgreSQL manages the B+ tree/index pages internally.


8. EDGE CASES
    Concurrent withdrawals:
    - Use row-level locking or optimistic concurrency.

    Concurrent transfers:
    - Lock both accounts in deterministic order to avoid deadlock.

    Duplicate request:
    - Idempotency key + UNIQUE constraint.

    Partial transfer:
    - Use one DB transaction so debit + credit commit/rollback together.

    Insufficient balance:
    - Reject before update.


9. ARCHITECTURE CHOICES
    Use PostgreSQL because we need ACID transactions and relational consistency.

    Concurrency:
    - Pessimistic: SELECT ... FOR UPDATE
    - Optimistic: version + conditional UPDATE

    Deadlock:
    - Always lock accounts in a fixed order:
      min(accountA, accountB) → max(accountA, accountB)

    SAGA:
    - Not needed inside one PostgreSQL transaction.
    - Consider it only when the workflow spans multiple services.

    Normalization:
    - Keep Account and Transaction separate.
    - Denormalize only when a measured read-performance problem requires it.

    CAP:
    - Not central for a single PostgreSQL database.


10. NON-FUNCTIONAL REQUIREMENTS
    Scaling:
    - Stateless application servers
    - PostgreSQL primary + read replicas for read scaling
    - Partition large transaction tables
    - Sharding/distributed SQL only when required

    Caching:
    - Redis can accelerate non-authoritative reads.
    - PostgreSQL remains the source of truth for balances.

    Observability:
    - Transaction success/failure
    - Latency
    - Lock waits
    - Deadlocks
    - Duplicate requests
    - DB connections
    - Replica lag


    FINAL ARCHITECTURE
    Answer:

    API / Celery Workers
            ↓
    Transaction Service
            ↓
       PostgreSQL
        /       \
    Accounts   Transactions
        ↓
    Read Replicas
        ↓
    Analytics


    CRITICAL TRANSFER FLOW
    Answer:

    BEGIN
      ↓
    Lock A + B in fixed order
      ↓
    Check balance
      ↓
    Debit A
      ↓
    Credit B
      ↓
    Insert transaction record(s)
      ↓
    COMMIT

    Failure at any step:
    → ROLLBACK



"""