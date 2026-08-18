"""
Link: https://www.youtube.com/watch?v=oVZtzZVe9Dg

1. What is a Message Queue?

    - A message queue is an asynchronous communication mechanism where
        a producer sends messages to a queue and a consumer processes them
        later.

    -Basic flow:

        Producer
           |
           | Message
           v
        +---------+
        |  Queue  |
        +---------+
           |
           | Message
           v
        Consumer


2. Why Do We Need a Message Queue?

    - Without Queue: Producer ---> Consumer
    - Producer and Consumer are tightly coupled.

    - With Queue: Producer ---> Queue ---> Consumer
    - Benefits:
        - Decouples producer and consumer
        - Handles traffic spikes
        - Enables asynchronous processing
        - Provides buffering
        - Allows independent scaling


3. What is Producer ?
    A producer is a component that creates and publishes messages
    to the messaging system.

    Example:
        API Server
            |
            | OrderCreated
            v
         Message Queue


4. What is Consumer ?
    - A consumer is a component that reads messages from the queue
        and processes them.

    - Example:
        Message Queue
             |
             v
        Order Worker
             |
             v
        Database


5. Why Distributed?

    - A single queue/server becomes a bottleneck or single point
        of failure.

    - Distributed architecture:
                     +----------+
        Producer --->| Broker 1 |
                     +----------+
                          |
                     +----------+
                     | Broker 2 |
                     +----------+
                          |
                     +----------+
                     | Broker 3 |
                     +----------+
                          |
                       Consumers

    Goals:
        - High availability
        - Horizontal scalability
        - Fault tolerance
        - Higher throughput


6. What are the Key Concepts in distributed messaging queue ?

    1. Message: Unit of data sent through the messaging system.

    2.Broker: Server responsible for receiving, storing and delivering messages.

    3. Topic / Queue: Logical destination where messages are published/stored.

    4. Producer: Creates messages.

    5. Consumer: Processes messages.

    6. (Commited) Offset : Position of a message within an ordered log.

    7. Partition: A subdivision of a topic used for parallelism and scalability.
`

7. What is Consumer Groups ?

                 Topic
                   |
        +----------+----------+
        |          |          |
     Part-0     Part-1     Part-2
        |          |          |
        v          v          v
       C1         C2         C3

    - Consumers belonging to the same consumer group divide the
        partitions among themselves.

    - Purpose:
        - Parallel processing
        - Horizontal scaling


8. Important Interview Idea

    More consumers ≠ unlimited throughput.

    If:
        Partitions = 3
        Consumers  = 5

        Only 3 consumers can actively consume partitions simultaneously.

    Therefore:
        Maximum active consumers per consumer group
        ≈ Number of partitions


9. Message Processing Flow

    Producer
       |
       v
    Broker
       |
       v
    Partition
       |
       v
    Consumer Group
       |
       v
    Consumer
       |
       v
    Business Logic


10. Failure Handling

    Consumer processes message
            |
            v
       Processing fails
            |
            v
         Retry
            |
            +------> Success
            |
            +------> Failure
                        |
                        v
                   Dead Letter Queue


    DLQ = Dead Letter Queue
    - A separate destination used to store messages that repeatedly
        fail processing.

    Purpose:
    - Prevent poison messages from blocking processing
    - Enable debugging
    - Allow later reprocessing


11. Delivery Semantics

    At-most-once: Message is delivered zero or one time.
    Possible result: Message may be lost.

    At-least-once: Message is delivered one or more times.
    Possible result: Duplicate processing.

    Exactly-once: Message is processed exactly once from the application's logical perspective.

    Important:
    Exactly-once is difficult in distributed systems and often
    requires additional coordination/idempotency mechanisms.


12. Idempotency
    - An operation is idempotent if executing it multiple times
        produces the same final result as executing it once.

    Example:
    Message: PaymentProcessed(order_id=123)
    Consumer receives it twice.

    Use:
    processed_orders[123] = true
    Before processing:
    if order already processed:
        skip

    This prevents duplicate side effects.


13. Backpressure

    Problem: Producer rate > Consumer processing rate

    Producer
      |
      | 10,000 msg/sec
      v
    Queue
      |
      | 1,000 msg/sec
      v
    Consumer

    Queue starts growing.

    Backpressure = mechanism to prevent the producer/consumer system from becoming overwhelmed.
    Possible solutions:
        - Scale consumers
        - Rate-limit producers
        - Increase partitions
        - Batch processing
        - Apply admission control


14. Core Trade-off

    Messaging systems generally trade:

        Latency
           vs
        Throughput
           vs
        Reliability
           vs
        Consistency

    System design requires choosing the appropriate balance.



"""