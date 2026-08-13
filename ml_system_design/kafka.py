"""
1. What is Kafka and why would you use it?

    - Kafka is a distributed event-streaming platform used to reliably publish, store, and consume streams of events.

                    Service A
                        ↓
                     Kafka Topic
                        ↓
             ┌───────┬────────┬─────────┐
             ▼       ▼        ▼
            Service B Service C Analytics

2. Why Kafka?
    Architecture:
        Producer
           ↓
        Kafka Topic
           ↓
        Partitions
           ↓
        Consumer Group
           ↓
        Consumers
           ↓
        Processing
           ↓
        Commit Offset

        - Decouple services
        - Asynchronous processing
        - High throughput
        - Durable event storage
        - Multiple consumers
        - Replay events


3. What are the major components of Kafka ?

    - Topic: Logical stream of events.
    - Partition: A topic is divided into partitions for scalability.
    - Offset: Position of a message inside a partition.
    - Consumer Group: Multiple consumers working together.
    - Each partition is processed by one consumer within a consumer group at a time.
            Topic
          ┌────┼────┐
          ▼    ▼    ▼
       Part 0 Part1 Part2
          │    │    │
          ▼    ▼    ▼
        C1    C2    C3

4. What happens if a Kafka consumer fails?
    - Another consumer in the group can take over the partition.
    - Kafka provides fault tolerance and recovery without requiring the producer to resend the entire event stream.

5. What happens if processing an event fails?
    Suppose:
        Kafka
          ↓
        Consumer
          ↓
        LLM processing
          ↓
        ERROR

    - You have several options.
        - Retry
        - Dead Letter Queue / Topic

6. Kafka vs Celery — when would you use which?
        | Celery                   | Kafka                              |
        | ------------------------ | ---------------------------------- |
        | Task queue               | Event streaming                    |
        | Execute work             | Publish events                     |
        | Worker-oriented          | Consumer-oriented                  |
        | Task execution           | Event distribution                 |
        | Good for background jobs | Good for event-driven architecture |
        | Retry tasks              | Replay/process events              |


7.


"""