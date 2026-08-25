"""
1. GET, PUT, DELETE are already idempotent as they don't duplicate the DB.

2. POST and PATCH are not idempotent.

3. How do you make POST idempotent ?

- Idempotency = Repeating the same request produces the same final effect as processing it once.

1. SEQUENTIAL IDEMPOTENCY
    - Requests are processed one after another, so keep a record of processed request_id/idempotency_key
        and skip the same key if it already succeeded.
    - Example: POST /payment with key P123 → process → store P123 → retry P123 → return previous result.


2. PARALLEL IDEMPOTENCY
    - Multiple identical requests can arrive simultaneously, so use an atomic UNIQUE constraint / atomic
        insert on the idempotency key so only one request succeeds.
    - Example: 5 threads send P123 → one inserts P123 successfully;
        the others detect duplicate and reuse the stored result.


3. DISTRIBUTED IDEMPOTENCY
    - Requests can reach different servers/workers, so store idempotency state in a shared durable store
        such as PostgreSQL/Redis and use atomic operations/unique constraints.
    - Example: Server A and Server B receive P123 → shared DB UNIQUE(idempotency_key) ensures
        only one transaction is processed.


4. PRACTICAL PATTERN
    - Request → check/claim idempotency key atomically → process business operation ->
        → store result/status → retries return the stored result.


5. IMPORTANT
    - GET/PUT/DELETE are HTTP-idempotent by semantics, but POST/PATCH may require an explicit idempotency key
        when duplicate processing would be harmful.
    - Idempotency prevents duplicate EFFECTS; it does not mean the request is never executed twice internally.


6. Idempotency Key
    - Unique client/request ID used to identify the same logical operation.
    - from uuid import uuid4

7. Atomic Claim
    - Store the key using an atomic INSERT/SETNX/UNIQUE constraint so concurrent requests cannot both process it.

8. Idempotency State
    - Track PENDING / SUCCESS / FAILED so retries know what happened.

9. Store the Result
    - Save the original response/result so a retry can return the same result instead of re-executing.

10. TTL / Cleanup
    - Idempotency records don't need to live forever; expire them according to business requirements.

11. Concurrent Requests
    - The important case: multiple servers receive the same request simultaneously → shared atomic storage is required.

12. Crash During Processing
    - If the worker crashes after the business operation but before marking SUCCESS,
        you need transactional handling/outbox or equivalent design to avoid duplicate effects.

13. Scope
    - Idempotency should be scoped correctly, e.g. tenant_id + idempotency_key,
        if different tenants may generate the same key.

14. Exactly-once vs Idempotency
    - Distributed systems usually provide at-least-once processing + idempotent business operations
        rather than true exactly-once execution.

15. Flow:
    Request
    → Idempotency Key
    → Atomic Claim
    → Execute
    → Store Result
    → Retry returns stored Result


"""