"""
1. What are different types of microservice design patterns ?

    1. API Gateway: Instead of clients directly calling every microservice:
        Client
          │
          ├──→ User Service
          ├──→ Order Service
          └──→ Recommendation Service

    use:
        Client
           ↓
        API Gateway
           ├──→ User Service
           ├──→ Order Service
           └──→ Recommendation Service


    Gateway can handle:
        - Authentication
        - Routing
        - Rate limiting
        - SSL termination
        - Request logging
        - Sometimes response aggregation


    - Don't put business logic into the gateway.

    2. Circuit Breaker:
        - Prevent cascading failures and fail fast when a dependency is unhealthy.
        - If a service is already failing, don't continuously call it.

            CLOSED
              ↓ failures
            OPEN
              ↓ timeout
            HALF-OPEN
              ↓ success
            CLOSED

    3. Saga Pattern:
        - Important when a business transaction spans multiple microservices.
        - Suppose an order requires:
            Order
             ↓
            Payment
             ↓
            Inventory
             ↓
            Shipping

        - There is no single database transaction across all services.
        - If any of these fails, you need compensate.

            Payment successful
                ↓
            Inventory fails
                   ↓
            Refund payment

    There are two common approaches:
        - Choreography: Services communicate through events:

                    Order Created
                        ↓
                    Payment Service
                        ↓ Payment Completed
                    Inventory Service
                        ↓ Inventory Reserved
                    Shipping Service

        - Orchestration: A central orchestrator controls the workflow:
                             Orchestrator
                          /       |        \
                         ↓        ↓         ↓
                      Payment  Inventory  Shipping

    4. Bulkhead pattern:Isolate failures and resource exhaustion.

    5. Strangler Pattern: Very useful for legacy migration.
        - You don't rewrite everything at once but gradually extract functionality:

    6. Database per Service:
        - Each microservice owns its data/database rather than sharing one DB.
        - This gives service autonomy but makes cross-service queries/transactions harder

    7. Service Discovery:
        - How one service finds the current location/instance of another service in a dynamic environment.

    8. CQRS — Command Query Responsibility Segregation:
        - Separate the write model from the read model, useful when read/write requirements differ significantly.

    9. API Composition:
        - One service/gateway calls multiple services and combines their responses.
        - Very relevant when building APIs over microservices.

    10. Transactional Outbox:
        - Ensures a database update and publishing an event happen reliably together—important
            when combining DB + Kafka/event-driven architecture

2. Why use microservices instead of a monolith?
    - Microservices allow independent deployment and scaling, clearer service ownership and isolation of failures.
    - But they introduce distributed-system complexity such as network failures, observability, data consistency
        and operational overhead, so I wouldn't split a system into microservices without a clear reason.

3. How would you prevent one failing service from bringing down the whole system?

    - Timeout
    - Retries
    - Circuit Breaker
    - Fallback
    - Rate Limiting

4. How do microservices communicate?
    Two broad approaches:
        - Synchronous: Use synchronous communication when you need an immediate response.
            - REST
            - gRPC
            - GraphQL

        - Asynchronous: Use asynchronous communication when the operation can happen independently or you want loose coupling.
            - Kafka
            - RabbitMQ

5. How do you handle transactions across microservices?

    - Avoid trying to use a traditional distributed database transaction where possible.
    - Use patterns such as Saga with compensating actions, and design operations to be idempotent.
    Example:
            Order
             ↓
            Payment
             ↓
            Inventory fails
             ↓
            Compensating action
             ↓
            Refund Payment

6. When would you NOT use microservices?
    - If the system is small, the team is small, requirements are changing rapidly,
        or there's no need for independent scaling/deployment, a modular monolith may be a better choice.
    - Microservices introduce significant operational and distributed-system complexity.

7. REST vs GraphQL vs gRPC:
    | Feature           | REST                                                           | GraphQL                                  | gRPC                              |
| ----------------- | -------------------------------------------------------------- | ---------------------------------------- | --------------------------------- |
| Full Form     | Representational State Transfer                                | Graph Query Language                     | gRPC Remote Procedure Call        |
| Data Format   | JSON, XML, HTML                                                | JSON                                     | Protocol Buffers (Binary)         |
| Protocol      | HTTP/1.1 or HTTP/2                                             | HTTP/1.1 or HTTP/2                       | HTTP/2 exclusively                |
| Data Fetching | Can over-fetch or under-fetch                                  | Client requests exact fields needed      | Predetermined by service contract |
| Streaming     | Primarily request-response; streaming possible with extensions | Subscriptions, typically over WebSockets | Full bidirectional streaming      |
| Main Use Case | Public APIs, web applications                                  | Mobile apps, complex data graphs         | Internal microservices, IoT       |


8. When to Choose REST, GraphQL, gRPC ?
    - Use REST when I need a simple, broadly compatible public API.
    - Choose GraphQL when clients need flexible access to complex or nested data and I want to avoid over-fetching.
    - Choose gRPC for internal service-to-service communication where performance, strongly typed contracts
        and streaming are important. The choice depends on client requirements, latency,
        data-fetching patterns, compatibility and operational complexity."

Notes:
        API Gateway
            ↓
        Routing / Auth / Rate limit

        Circuit Breaker
            ↓
        Protect against failing dependencies

        Bulkhead
            ↓
        Isolate resources/failures

        Saga
            ↓
        Distributed transactions

        Strangler
            ↓
        Incremental legacy migration


"""