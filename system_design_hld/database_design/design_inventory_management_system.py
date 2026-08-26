"""
INVENTORY MANAGEMENT SYSTEM

1. REQUIREMENT CLARIFICATION

    - Add/update product inventory
    - Get current stock
    - Reserve stock
    - Release stock
    - Deduct stock after successful order
    - Maintain inventory history

    Clarify:
    - Multiple warehouses?
    - Can stock go negative?
    - Do we need real-time availability?
    - Expected read/write volume?
    - Do we need inventory history/audit?


2. UNDERSTANDING BUSINESS WORKFLOW

    Stock Received
        → AVAILABLE

    Order Created
        → RESERVE stock

    Payment Success
        → DEDUCT / COMMIT stock

    Order Cancelled / Payment Failed
        → RELEASE reservation

    Important:
        AVAILABLE stock and RESERVED stock should be tracked separately.


3. IDENTIFY ENTITIES / TABLES / FIELDS

    PRODUCT
    - product_id
    - name

    WAREHOUSE
        - warehouse_id
        - location

    INVENTORY
        - product_id
        - warehouse_id
        - available_qty
        - reserved_qty
        - updated_at

    INVENTORY_EVENT
        - event_id
        - product_id
        - warehouse_id
        - event_type
        - quantity
        - reference_id
        - created_at


4. IDENTIFY QUERIES / ACCESS PATTERNS

    - Get stock for product + warehouse
    - Find available stock across warehouses
    - Reserve stock
    - Release stock
    - Get inventory history

    Example:
        SELECT available_qty
        FROM inventory
        WHERE product_id = ?
        AND warehouse_id = ?;


5. DESIGN SCHEMA

    INVENTORY
        - product_id
        - warehouse_id
        - available_qty
        - reserved_qty
        - updated_at

    Primary key:
    (product_id, warehouse_id)

    INVENTORY_EVENT
        - event_id PK
        - product_id
        - warehouse_id
        - event_type
        - quantity
        - reference_id
        - created_at


6. RELATIONSHIPS & CONSTRAINTS

    - Product 1:N Inventory
    - Warehouse 1:N Inventory
    - Inventory 1:N InventoryEvent

    Constraints:
        - PK(product_id, warehouse_id)
        - available_qty >= 0
        - reserved_qty >= 0
        - quantity > 0
        - UNIQUE(reference_id, event_type) where needed for idempotency


7. INDEXING

    Main query:

    WHERE product_id = ?
    AND warehouse_id = ?

    → PRIMARY KEY(product_id, warehouse_id)

    History:

    WHERE product_id = ?
    AND warehouse_id = ?
    ORDER BY created_at DESC

    → INDEX(product_id, warehouse_id, created_at)

    If searching by order/reference:

    → UNIQUE(reference_id, event_type)


8. EDGE CASES

    Concurrent orders:
    → Two users try to reserve the last 1 item.

    Use atomic update:

    UPDATE inventory
    SET available_qty = available_qty - 1,
        reserved_qty = reserved_qty + 1
    WHERE product_id = ?
    AND warehouse_id = ?
    AND available_qty >= 1;

    affected_rows = 1
    → reservation succeeded

    affected_rows = 0
    → insufficient stock / another request won

    Other cases:
    - Duplicate reservation request → idempotency
    - Payment fails → release reservation
    - Order cancelled → release reservation
    - Warehouse failure → choose another warehouse
    - Product deleted → preserve historical inventory events


9. ARCHITECTURE CHOICES

    PostgreSQL:
    → Good for strong consistency, transactions and constraints.

    Concurrency:
    → Prefer atomic conditional UPDATE for simple stock changes.
    → Row-level locking for more complex multi-step operations.

    Inventory events:
    → Append-only history for auditability.

    Redis:
    → Optional for fast stock reads, but DB remains source of truth.

    Kafka / Queue:
    → Useful for asynchronous inventory events, notifications,
    analytics and downstream processing.

    SAGA:
    → Relevant if inventory participates in Order → Payment →
    Shipping across separate services.


10. NON-FUNCTIONAL REQUIREMENTS

Scaling:
- Stateless Inventory Service
- Read replicas for read-heavy queries
- Partition inventory events when very large
- Queue asynchronous downstream processing

Caching:
- Cache product/availability reads if necessary.
- Never trust stale cache for final stock reservation.

Observability:
- Reservation success/failure
- Oversell attempts
- Stock mismatch
- Lock wait time
- DB latency
- Queue lag
- Reconciliation failures


CORE INVENTORY FLOW

Order
  ↓
Reserve Stock
  ↓
Atomic DB Update
  ↓
Payment
  ↓
SUCCESS → Deduct/commit
FAILURE → Release


Notes:
    I'd model Inventory by product and warehouse using
    (product_id, warehouse_id) as the primary key, with available
    and reserved quantities tracked separately. Stock history would
    be append-only through inventory events.

    The critical concurrency problem is two orders trying to reserve
    the same stock, so I'd use an atomic conditional update such as
    'update only if available_qty >= requested_qty'. An affected-row
    count of zero means another request won or there isn't enough
    stock.

    PostgreSQL would be the source of truth. Redis can optimize reads,
    while Kafka or a queue can handle asynchronous events. If the
    workflow spans Order, Payment and Inventory services, I'd consider
    a Saga.

"""