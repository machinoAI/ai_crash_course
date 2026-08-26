"""
PAYMENT SYSTEM


1. REQUIREMENT CLARIFICATION

    Functional:
    - User creates a payment for an Order.
    - Support payment processing through an external PSP (Stripe/RazorPay).
    - Query payment status.
    - Support full/partial refunds.
    - Maintain immutable payment/ledger history.
    - Handle retries and duplicate requests.
    - Receive asynchronous PSP webhooks.

    Clarify:
    - One-time payment or recurring?
    - One currency or multi-currency?
    - Do we need payouts to merchants?
    - Full refund only or partial refund?
    - Expected TPS / transaction volume?
    - Single-region or multi-region?
    - How long must financial history be retained?


2. UNDERSTANDING BUSINESS WORKFLOW

    User
    → Create Order
    → Create Payment
    → PENDING
    → Send payment request to PSP
    → AUTHORIZED / CAPTURED / FAILED
    → Webhook confirms final PSP state
    → Update internal state
    → Record ledger entries

    Refund:
    CAPTURED
    → REFUND_PENDING
    → REFUNDED

    Important:
    A payment is a STATE MACHINE; don't model it as only
    `is_paid = true/false`.

3. IDENTIFY ENTITIES / TABLES / FIELDS

    USER
    - user_id PK
    - name
    - email
    - created_at

    ORDER
    - order_id PK
    - user_id FK
    - amount_paise
    - currency
    - status
    - created_at

    PAYMENT
    - payment_id PK
    - order_id FK
    - user_id FK
    - amount_paise
    - currency
    - status
    - idempotency_key
    - provider
    - provider_payment_id
    - created_at
    - updated_at

    PAYMENT_HISTORY
    - event_id PK
    - payment_id FK
    - old_status
    - new_status
    - event_type
    - created_at

    PAYMENT_METHOD
    - payment_method_id PK
    - user_id FK
    - provider_token
    - type
    - last4

    LEDGER_ENTRY
    - entry_id PK
    - payment_id FK
    - account_id
    - direction
    - amount_paise
    - currency
    - created_at

    WEBHOOK_EVENT
    - provider_event_id PK/UNIQUE
    - payment_id
    - event_type
    - payload/reference
    - received_at
    - processed_at

    OUTBOX_EVENT
    - outbox_id PK
    - aggregate_id
    - event_type
    - payload/reference
    - status
    - created_at


4. IDENTIFY QUERIES / ACCESS PATTERNS

    Q1:
    Get payment status

    SELECT *
    FROM payment
    WHERE payment_id = ?;


    Q2:
    Find payment by idempotency key

    SELECT *
    FROM payment
    WHERE idempotency_key = ?;


    Q3:
    Get payments for an order

    SELECT *
    FROM payment
    WHERE order_id = ?
    ORDER BY created_at DESC;


    Q4:
    Get user's payment history

    SELECT *
    FROM payment
    WHERE user_id = ?
    ORDER BY created_at DESC;


    Q5:
    Get payment history

    SELECT *
    FROM payment_history
    WHERE payment_id = ?
    ORDER BY created_at;


    Q6:
    Deduplicate webhook

    SELECT *
    FROM webhook_event
    WHERE provider_event_id = ?;


    These access patterns determine the indexes.


    5. DESIGN SCHEMA

    USER
    1 ─── N ORDER
    1 ─── N PAYMENT
    1 ─── N PAYMENT_METHOD

    ORDER
    1 ─── N PAYMENT

    PAYMENT
    1 ─── N PAYMENT_HISTORY

    PAYMENT
    1 ─── N LEDGER_ENTRY


    Money:
    - Store `amount_paise` as BIGINT.
    - Store currency separately, e.g. INR/USD.
    - Never use float for financial amounts.

    Payment history and ledger entries should be append-only/immutable.
    Current payment state can be stored separately for fast lookup.


6. RELATIONSHIPS & CONSTRAINTS

    PK:
    - user_id
    - order_id
    - payment_id
    - event_id
    - entry_id

    FK:
    - order.user_id → user.user_id
    - payment.user_id → user.user_id
    - payment.order_id → order.order_id
    - payment_history.payment_id → payment.payment_id
    - ledger_entry.payment_id → payment.payment_id

    UNIQUE:
    - payment.idempotency_key
    - webhook_event.provider_event_id
    - payment.provider_payment_id where appropriate

    NOT NULL:
    - amount
    - currency
    - status
    - timestamps
    - required foreign keys

    CHECK:
    - amount_paise > 0
    - currency valid
    - refund_amount <= captured_amount

    Important:
    State transitions should also be guarded:
    e.g. REFUNDED → CAPTURED should be rejected.


7. INDEXING

    Main indexes:

        UNIQUE(idempotency_key)

        INDEX(order_id, created_at)

        INDEX(user_id, created_at)

        INDEX(payment_id, created_at) on history

        UNIQUE(provider_event_id)

        UNIQUE(provider_payment_id) where applicable


    Why:
    Indexes must follow actual queries.

    Example:
    WHERE user_id = ?
    ORDER BY created_at DESC

    → INDEX(user_id, created_at)

    PostgreSQL manages the underlying B-tree/index pages;
    we choose the index based on access pattern.


8. EDGE CASES

    1. Same API request arrives twice
    → idempotency_key
    → process once
    → return original result.

    2. Two servers receive same request simultaneously
    → UNIQUE(idempotency_key) + atomic insert/claim.


    3. PSP succeeds but our request times out
    → Payment may be UNKNOWN/PENDING.
    → Do NOT blindly retry a new charge.
    → Query PSP using the provider idempotency key/reference or wait
      for webhook/reconciliation. This "unknown outcome" case is a
      key payment-system interview failure mode.


    4. PSP succeeds but our DB update fails
    → Reconciliation/webhook eventually repairs internal state.


    5. Webhook arrives twice
    → UNIQUE(provider_event_id)
    → process only once.


    6. Webhook arrives out of order
    → Validate allowed state transition.
    → Reject stale transition or reconcile with PSP authoritative state.
    Current guidance explicitly calls out duplicate and out-of-order
    webhooks. :contentReference[oaicite:4]{index=4}


    7. Refund request arrives twice
    → Separate idempotency key for refund operation.


    8. Payment succeeds but notification fails
    → Payment remains successful.
    → Notification is asynchronous and retried.


    9. Partial refund
    → Create a new refund operation/ledger entries.
    → Never mutate original payment history.


    10. Crash between DB write and message publish
    → Transactional Outbox.


9. ARCHITECTURE CHOICES

    DATABASE:
    → PostgreSQL initially.
    Reason:
    - ACID
    - relational integrity
    - strong consistency
    - financial transactions


    PAYMENT STATE:
    → Explicit state machine.

    Example:
    CREATED
    → PROCESSING
    → AUTHORIZED
    → CAPTURED
    → SETTLED

    Failure:
    PROCESSING → FAILED

    Refund:
    CAPTURED → REFUND_PENDING → REFUNDED


    IDEMPOTENCY:
    → client idempotency key
    → UNIQUE constraint
    → persist/claim before processing


    PSP:
    Payment Service
    → PSP Adapter
    → Stripe/Adyen/Bank

    Keep PSP-specific logic behind an interface.


    TRANSACTIONAL OUTBOX:
    Within the same DB transaction:

    Payment row
    +
    Outbox row

    COMMIT

    Then:
    Outbox Relay → Queue/Kafka → PSP Worker



    ASYNC PROCESSING:
    Use queue/Kafka for:
    - PSP worker jobs
    - Notifications
    - Reconciliation
    - Analytics

    Do not put non-critical work in the payment critical path.


    SAGA:
    Use only when payment participates in a multi-service workflow,
    e.g. Order + Inventory + Payment.

    Do NOT use Saga instead of the DB transaction for the internal
    payment/ledger operation.

    PAYMENT + LEDGER atomicity:
    The ledger debit/credit and corresponding payment state transition
    must commit together when money is recognized internally. :contentReference[oaicite:6]{index=6}


10. NON-FUNCTIONAL REQUIREMENTS

    Consistency:
    → Strong consistency for money movement.

    Availability:
    → High availability, but correctness wins over blindly accepting
      writes during a partition.

    Scalability:
    → Stateless payment API
    → Horizontal workers
    → Read replicas for non-critical reads
    → Partition/shard ledger by merchant/account/time when necessary.

    Caching:
    → Don't use Redis as the authoritative source for payment state.
    → Cache non-critical read data only.

    Observability:
    Track:
    - payment success/failure rate
    - latency
    - PSP latency
    - timeout/unknown payments
    - duplicate requests
    - webhook failures
    - reconciliation mismatches
    - refund failures
    - queue lag
    - DB latency/locks


    FINAL ARCHITECTURE:

    Client
      ↓
    API Gateway
      ↓
    Payment Service
      ↓
    PostgreSQL
      ├── Payment
      ├── Order
      ├── Payment History
      ├── Ledger Entries
      ├── Idempotency
      └── Outbox
            ↓
       Outbox Relay
            ↓
         Queue/Kafka
            ↓
        PSP Workers
            ↓
     Stripe / RazorPay
            ↓
       Webhook
            ↓
     Payment Service
            ↓
    PostgreSQL

                      ↓
              Reconciliation Job


    CRITICAL WRITE FLOW
    Answer:

    POST /payments
            ↓
    Validate request
            ↓
    Check/claim idempotency key
            ↓
    Create PAYMENT = PENDING
            ↓
    Create OUTBOX event
            ↓
    COMMIT
            ↓
    Worker calls PSP with same idempotency key
            ↓
    PSP response / timeout
            ↓
    Webhook / reconciliation
            ↓
    Update payment state
            ↓
    Write ledger entries atomically
            ↓
    Notify user asynchronously


MOST IMPORTANT INTERVIEW POINTS

    1. Idempotency → prevent double charge.
    2. Payment state machine → prevent invalid transitions.
    3. Integer money → avoid precision issues.
    4. Double-entry ledger → every movement is accounted for.
    5. Transactional outbox → solve DB + queue dual-write.
    6. Webhooks → PSP may confirm asynchronously.
    7. Reconciliation → resolve unknown/missing/mismatched states.
    8. Immutable history → don't rewrite financial history.
    9. PostgreSQL/ACID → strong consistency for money.
    10. Async workers → scale PSP calls without blocking API.


Notes:

    I'd model User, Order and Payment separately, with Payment treated
    as an explicit state machine and money stored as integer paise.
    Every payment API requires an idempotency key, enforced with a
    unique constraint so concurrent retries cannot create duplicate
    charges.

    I'd use PostgreSQL for the authoritative payment state and
    immutable ledger/history. The API transaction would create the
    payment intent and an outbox event atomically. A worker would then
    call the PSP using the same idempotency key. Because a PSP response
    can timeout or arrive asynchronously, I'd use webhooks and a
    reconciliation job to resolve unknown states.

    For refunds I'd use separate idempotent operations and append-only
    ledger entries. Kafka/queues would handle asynchronous PSP work,
    notifications and reconciliation, while the database remains the
    source of truth.



"""