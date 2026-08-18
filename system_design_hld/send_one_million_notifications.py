"""
1. How would you send 1 million notifications without overwhelming your servers?


STEP 1 — Define the problem and estimate scale
    ------------------------------------------------
    Goal: Send notifications to 1M users without:

    - Overloading application servers
    - Overloading DB
    - Hitting FCM/APNs rate limits
    - Losing notifications
    - Creating duplicates

    Example:
    1,000,000 notifications

    If processed in 1 hour:

    1,000,000 / 3,600
    ≈ 278 notifications/sec

    So the system must support controlled throughput rather than
    trying to send 1M notifications instantly.


    STEP 2 — Decouple request creation from notification delivery
    --------------------------------------------------------------
    DO NOT:

    API → DB → Send 1M notifications synchronously

    Instead:

    Campaign Service
          ↓
    Message Queue
    (Kafka / SQS)
          ↓
    Worker Pool
          ↓
    FCM / APNs / Email / SMS Provider

    Why?

    The queue absorbs traffic spikes.

    Producer can create jobs quickly.
    Consumers process them at a controlled rate.

    This is the most important design decision.


    STEP 3 — Fan-out notification jobs into the queue
    --------------------------------------------------
    When the campaign starts:

    Campaign Service
          ↓
    Fetch eligible users
          ↓
    Create notification jobs
          ↓
    Kafka / SQS

    Example message:

    {
      "notification_id": "N123",
      "user_id": "U456",
      "channel": "push",
      "template_id": "T10",
      "payload": {...}
    }

    For 1M users, we create 1M logical jobs/events.

    IMPORTANT:
    Do not load all 1M users into application memory.

    Process recipients in pages/batches from the database.


    STEP 4 — Scale consumers horizontally
    --------------------------------------
    Use multiple workers:

                 Kafka / SQS
                      ↓
           ┌──────────┼──────────┐
           ↓          ↓          ↓
        Worker 1   Worker 2   Worker N
           ↓          ↓          ↓
         FCM        FCM        FCM

    More workers
    → higher throughput

    But:

    MORE WORKERS ≠ unlimited sending

    Because downstream providers have rate limits.

    Therefore consumer scaling must be combined
    with rate limiting.


    STEP 5 — Use batching + rate limiting
    --------------------------------------
    Each worker pulls a batch:

    Example:
    500 notifications

    Then:

    rateLimiter.acquire(500)
            ↓
    FCM batch API
            ↓
    success
            ↓
    ACK queue messages

    Why batching?

    - Fewer network calls
    - Better throughput
    - Lower overhead

    Why rate limiting?

    Because FCM/APNs/provider APIs have limits.

    Use:
    - Token Bucket
    OR
    - Leaky Bucket

    Example:

    Allowed rate = 1,000 notifications/sec

    Workers collectively must stay below this limit.

    Important:
    Rate limiting should usually be GLOBAL / DISTRIBUTED,
    not an independent limit inside every worker.

    Otherwise:

    10 workers × 1,000/sec
    = 10,000/sec

    and the provider may throttle or reject requests.


    STEP 6 — Handle failures safely
    -------------------------------
    Never assume every notification succeeds.

    Failure types:

    1. Temporary failure
       → retry

    2. Permanent failure
       → do not retry forever

    3. Provider throttling
       → exponential backoff

    4. Worker crash
       → message becomes available again

    5. Poison message
       → move to DLQ

    Architecture:

                     Queue
                       ↓
                    Worker
                       ↓
                  Provider
                  ↙       ↘
             Success      Failure
                ↓            ↓
              ACK          Retry
                             ↓
                      Max retries?
                        ↙      ↘
                      NO       YES
                      ↓         ↓
                   Queue       DLQ

    Use:
    - Exponential backoff
    - Maximum retry count
    - Dead Letter Queue


    STEP 7 — Make delivery reliable, observable and idempotent
    -----------------------------------------------------------
    The biggest distributed-system problem:

    What if notification is sent successfully,
    but the worker crashes BEFORE acknowledging the message?

    The queue may deliver the message again.

    Therefore:

    Same notification may be sent twice.

    Solution:
    Use idempotency.

    Example:

    notification_id = "N123"

    Before sending/completing:

    Check notification status:

    N123 → SENT

    If already SENT:
        skip

    Otherwise:
        send
        mark SENT

    IMPORTANT:
    True exactly-once delivery is difficult in distributed systems.

    Usually design for:

    AT-LEAST-ONCE processing
    +
    IDEMPOTENT consumers

    rather than assuming exactly-once delivery.

    Observability:
    Track:

    - queued notifications
    - processing rate
    - success rate
    - failure rate
    - retry count
    - DLQ count
    - provider throttling
    - delivery latency
    - queue lag

    For marketing/product use cases, also store:

    notification_id
    user_id
    campaign_id
    status
    created_at
    sent_at
    delivered_at
    failed_at

    This allows delivery tracking and reporting.


    ========================================================
    FINAL ARCHITECTURE
    ========================================================

                     Campaign API
                          ↓
                    Campaign Service
                          ↓
                   User/Recipient DB
                          ↓
                    Kafka / SQS
                          ↓
              ┌───────────┼───────────┐
              ↓           ↓           ↓
           Worker 1    Worker 2    Worker N
              └───────────┼───────────┘
                          ↓
               Distributed Rate Limiter
                          ↓
                 FCM / APNs / Email
                          ↓
                 Success / Failure
                     ↙         ↘
                  ACK         Retry
                                 ↓
                                DLQ
                                 ↓
                           Alert / Replay


    ========================================================
    KEY INTERVIEW CONCEPTS TO MENTION
    ========================================================

    1. Producer/Consumer decoupling
    2. Kafka/SQS as buffer
    3. Horizontal consumer scaling
    4. Batch processing
    5. Distributed rate limiting
    6. Exponential backoff
    7. Dead Letter Queue
    8. At-least-once processing
    9. Idempotency
    10. Queue lag monitoring
    11. Backpressure
    12. Delivery-status tracking


    ========================================================
    Explanation:

    I would never send 1 million notifications synchronously.
    I would decouple campaign creation from delivery using Kafka or
    SQS. The campaign service publishes notification jobs, and a
    horizontally scaled worker pool consumes them in batches.

    Workers use a distributed token-bucket rate limiter so the total
    throughput stays within FCM/APNs limits. Temporary failures are
    retried with exponential backoff, while permanently failing
    messages go to a DLQ.

    Because queue processing is typically at-least-once, every
    notification needs an idempotency key to prevent duplicate sends.
    Finally, I would monitor queue lag, throughput, latency, failures,
    retries, provider throttling and DLQ size."


    MEMORY TRICK
    ========================================================

    "QUEUE → BATCH → LIMIT → RETRY → DLQ → IDEMPOTENCY → MONITOR"

    Queue       = absorb spike
    Batch       = improve throughput
    Limit       = protect provider
    Retry       = recover transient failures
    DLQ         = isolate permanent failures
    Idempotency  = prevent duplicates
    Monitor     = know what's happening

"""