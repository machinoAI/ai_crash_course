"""
Database Design Pattern:

    1. Requirement clarification
    2. Understanding Business workflow
    3. Identify Entities
    4. Identify queries  ->> [ Select * from TXN where timestamp between d1 and d2 ]
    5. Design Schema
    6. Relationship and Constraints: -->> [ PK, FK, UNIQUE, NOT NULL, CHECK]
    7. Indexing based on query retrieval: [Index on individual keys and composite keys to retrieve faster] [ B+ Tree, Hash indexes, Data pages]
    8. Discussing of Edge cases:
    9. Architecture Choices: ACID, SAGA, CAP Theorem, Normalization, De-normalization
    10. Discussing NFRs: Scaling, Caching, Observability,



1. Requirement clarification:
    1. How much data/transactions, user/traffic we are expecting?
        100 RPS ->> PostgresSQL
        1 M RPS -> Need Caching, Partitioning/ Sharding, Replicas or specialized infrastructure

    SQL
        - PostgresSQL: High Consistency. Ideal for transactions, banking, finance etc.
            - PostgresSQL can also be scaled horizontally by deploying replicas at multi-region
            - Ideal for complex queries

        - Distributed SQL - CockroachDB: It automatically manages distribution storage,
            sharding, replications, node failure, and multi-region distributions.

    - NoSQL:
        - MongoDB: Flexible schema, document based storage, Read document as whole.
        - Cassandra: High throughput, high availability, Access based indexing and massive scale.

    - Sharding/Partition: Carefully choose the shard keys, it must be based on the access else querying can be expensive.
        - Example: Shard based on user_id. Time based sharding usually used for archival.

    2. Is the system read-heavy or write heavy ?

        Ready heavy -> Caching becomes important
            - Redis (key-value storage)
                - LRU
                - MRU
                - LFU

        Write heavy -> Kafka, Casandra etc. May become relevant depending on the use case.

    3. Do we need real-time ?

        Real-time means: How quickly must a change become visible?

        Example: If real-time:
            → WebSocket/SSE
            → streaming
            → low-latency cache
            → immediate event propagation

        if not real-time:
            → async processing --> Kafka, RabbitMQ
            → queues
            → eventual consistency

    4. What is the consistency requirement ?

        Strong consistency:
            Account A sending amount XXX to account B ->> Immediately should deduct from A and reflect in B.

        Eventual consistency:
            Like Count increase, Send Notifications, Watch count increase, Recommendations


2. WHY DO THESE QUESTIONS MATTER?

        Because your answers determine the architecture.

            REAL-TIME?
               ↓
            Streaming / WebSocket / low-latency processing


            STRONG CONSISTENCY?
               ↓
            Transactions / locking / coordination


            READ-HEAVY?
               ↓
            Cache / read replicas


            WRITE-HEAVY?
               ↓
            Partitioning / batching / write-optimized DB


            COMPLEX RELATIONSHIPS?
               ↓
            Relational DB


            DOCUMENT-LIKE DATA?
               ↓
            MongoDB


            MASSIVE TIME-SERIES?
               ↓
            Time-series DB


            MASSIVE WRITES + KNOWN QUERY PATTERNS?
               ↓
            Cassandra






"""