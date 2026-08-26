"""
 ORDER MANAGEMENT SYSTEM

1. REQUIREMENT CLARIFICATION

    Functional:
    - Create order
    - Get order
    - Add/remove order items
    - Update order status
    - Cancel order
    - View user's order history
    - Support payment and shipment lifecycle

    Clarify:
    - Can one order have multiple payment attempts?
    - Can an order be partially cancelled/refunded?
    - Do we need order history/audit?
    - Expected traffic and retention?
    - Is inventory reservation part of the workflow?


2. UNDERSTANDING BUSINESS WORKFLOW

    Create Order
        → Add Items
        → Validate Inventory
        → Payment
        → CONFIRMED
        → SHIPPED
        → DELIVERED

        Failure:
        → CANCELLED

    Important:
    - Order has a lifecycle/state machine.
    - Don't overwrite history if auditability is required.
    - Payment and inventory may be separate services.


3. IDENTIFY ENTITIES / TABLES / FIELDS

`    USER
        - user_id
        - name
        - email
        - created_at

    ORDER
        - order_id
        - user_id
        - status
        - total_amount_paise
        - currency
        - created_at
        - updated_at

    ORDER_ITEM
        - order_item_id
        - order_id
        - product_id
        - quantity
        - unit_price_paise

    PRODUCT
        - product_id
        - name
        - current_price

    PAYMENT
        - payment_id
        - order_id
        - status
        - amount_paise
        - idempotency_key

    SHIPMENT
        - shipment_id
        - order_id
        - status
        - tracking_number
    `

4. IDENTIFY QUERIES / ACCESS PATTERNS

    - Get order by order_id
    - Get all orders for user_id
    - Get order items for order_id
    - Get orders by status
    - Get orders by date
    - Find payment for order
    - Find shipment for order

    Example:

    SELECT *
    FROM orders
    WHERE user_id = ?
    ORDER BY created_at DESC;


5. DESIGN SCHEMA

    USER
        user_id PK
        name
        email
        created_at

    ORDER
        order_id PK
        user_id FK
        status
        total_amount_paise
        currency
        created_at
        updated_at

    ORDER_ITEM
        order_item_id PK
        order_id FK
        product_id FK
        quantity
        unit_price_paise

    PAYMENT
        payment_id PK
        order_id FK
        status
        amount_paise
        idempotency_key UNIQUE

    SHIPMENT
        shipment_id PK
        order_id FK
        status
        tracking_number


6. RELATIONSHIPS & CONSTRAINTS

    User 1:N Order
    Order 1:N OrderItem
    Product 1:N OrderItem
    Order 1:N Payment Attempt
    Order 1:1 or 1:N Shipment depending on business workflow

    PK:
        - user_id
        - order_id
        - order_item_id
        - payment_id
        - shipment_id

    FK:
        - order.user_id → user.user_id
        - order_item.order_id → order.order_id
        - order_item.product_id → product.product_id
        - payment.order_id → order.order_id
        - shipment.order_id → order.order_id

    Constraints:
        - quantity > 0
        - unit_price_paise > 0
        - total_amount_paise >= 0
        - idempotency_key UNIQUE


7. INDEXING

    Main queries:

        WHERE user_id = ?
        ORDER BY created_at DESC

        → INDEX(user_id, created_at)

        WHERE order_id = ?

        → PRIMARY KEY(order_id)

        WHERE order_id = ?  -- order items

        → INDEX(order_id)

        WHERE status = ?

        → INDEX(status) only if the query/selectivity justifies it

        For payment:
        → UNIQUE(idempotency_key)


8. EDGE CASES

    - Same order request arrives twice
    → Idempotency key

    - Two requests try to cancel order simultaneously
    → Atomic state transition

    - Product price changes after order creation
    → Store unit_price_paise in ORDER_ITEM; don't depend on current product price.

    - Payment succeeds but order update fails
    → Reconciliation / retry

    - Order cancellation after shipment
    → Validate state transition

    - User retries after timeout
    → Return existing order using idempotency key

    - Product deleted after order creation
    → Historical ORDER_ITEM should remain valid.


9. ARCHITECTURE CHOICES
    Database:
    → PostgreSQL for relationships, constraints and transactions.

    Normalization:
    → Keep User, Order, Product, Payment separate.

    Important denormalization:
    → Store unit_price_paise inside ORDER_ITEM.
    Why?
    → Historical order price must not change when Product.current_price changes.

    Order state:
    CREATED
    → PAYMENT_PENDING
    → CONFIRMED
    → SHIPPED
    → DELIVERED

    Failure states:
    → CANCELLED
    → PAYMENT_FAILED

    Concurrency:
    → Atomic state transition / row-level locking where required.

    SAGA:
    → Relevant if Order + Payment + Inventory + Shipping are separate services.

    Kafka/Queue:
    → Async notifications, events, analytics, inventory/shipping workflows.

    Redis:
    → Optional cache for product/order reads; not the source of truth.


10. NON-FUNCTIONAL REQUIREMENTS

    Scaling:
    - Stateless Order Service
    - Read replicas for order-history queries
    - Partition very large order tables if required
    - Queue async work

    Caching:
    - Product/catalog data can be cached.
    - Order/payment state should come from DB when correctness matters.

    Observability:
    - Order creation latency
    - Payment failures
    - State-transition failures
    - Duplicate requests
    - DB latency/locks
    - Queue lag

    Reliability:
    - Idempotent APIs
    - Retries with backoff
    - Reconciliation for payment/inventory mismatches


    CORE DESIGN

    Client
      ↓
    API Gateway
      ↓
    Order Service
      ├──→ PostgreSQL
      │      ├── User
      │      ├── Order
      │      ├── OrderItem
      │      ├── Payment
      │      └── Shipment
      │
      └──→ Kafka/Queue
              ├── Notification
              ├── Inventory
              └── Analytics


Notes:

    I'd model User, Order and OrderItem separately, with Payment and
    Shipment linked to the Order. The order would use an explicit state
    machine, and I'd store the purchased unit price in OrderItem so
    historical orders are not affected by later product-price changes.

    I'd use PostgreSQL because we need relational integrity and
    transactions. The main access patterns drive indexes such as
    (user_id, created_at) for order history. APIs would be idempotent,
    and concurrent state changes would use atomic updates or row-level
    locking.

    If payment, inventory and shipping are separate services, I'd use
    a Saga/event-driven workflow, while keeping PostgreSQL as the
    authoritative order state.

"""