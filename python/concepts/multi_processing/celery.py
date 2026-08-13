"""
1. What is celery ?

    - Celery is a distributed task queue for executing work asynchronously outside your web/API process.

    Typical architecture:
                 ┌──────────────┐
HTTP Request ───>│   FastAPI    │
                 └──────┬───────┘
                        │
                  enqueue task
                        │
                        ▼
                 ┌──────────────┐
                 │ Redis/Rabbit │
                 │    Broker    │
                 └──────┬───────┘
                        │
                        ▼
              ┌──────────────────┐
              │  Celery Workers  │
              │                  │
              │  Worker 1        │
              │  Worker 2        │
              │  Worker 3        │
              └───────┬──────────┘
                      │
                      ▼
                DB / API / S3

    - FastAPI handles the request. Celery handles background/distributed work.

2. What is celery core components ?
    - Producer: Usually FastAPI application.
        -  generate_report.delay()

    - Broker: Stores/queues messages.
        - Common choices:
            - Redis
            - RabbitMQ

    - Worker: Executes tasks.
        - celery -A app worker --loglevel=info

    - Result backend: Stores task state/result if you need it.

    Architecture:
                  ┌────────────┐
                 │  FastAPI   │
                 └─────┬──────┘
                       │
                       ▼
                 ┌────────────┐
                 │   Broker   │
                 │Redis/Rabbit│
                 └─────┬──────┘
                       │
                       ▼
                 ┌────────────┐
                 │  Worker    │
                 └─────┬──────┘
                       │
                       ▼
                 ┌────────────┐
                 │   Result   │
                 │   Backend  │
                 └────────────┘

3. What is the difference between Celery and asyncio ?

    asyncio : Good for i/o concurrency within an application process

    Celery: Good for
        - distributed background processing
        - long-running jobs
        - CPU-heavy workloads
        - reliable task execution
        - horizontal scaling

Example:

    async def get_dashboard():

    user = await get_user()
    orders = await get_orders()
    recommendations = await get_recommendations()

    return {
        "user": user,
        "orders": orders,
        "recommendations": recommendations
    }

    First optimizations:
        user, orders, recommendations = await asyncio.gather(
            get_user(),
            get_orders(),
            get_recommendations()
        )

    What happens when recommendation fails, so adding timeout policy:
    import asyncio

    async def get_recommendations_safe():
        try:
            async with asyncio.timeout(2):
                return await get_recommendations()

        except TimeoutError:
            return []

4. What is Circuit Breaker ?
    - Circuit breaker protects your service from repeatedly calling an unhealthy dependency.

    - If something is repeatedly failing: Stop sending electricity through it temporarily.
    - Example:
        import pybreaker

        breaker = pybreaker.CircuitBreaker(
            fail_max=5,
            reset_timeout=30
        )


5. Timeout + Retry + Circuit Breaker

    | Mechanism       | Purpose                                |
    | --------------- | -------------------------------------- |
    | Timeout         | Don't wait forever                     |
    | Retry           | Recover from transient failure         |
    | Circuit breaker | Stop calling unhealthy dependency      |
    | Fallback        | Maintain degraded functionality        |
    | Rate limit      | Protect service from excessive traffic |
    | Bulkhead        | Isolate failures/resources             |
    |Exponential backoff| wait more time than last wait and retry

6. Celery retry:

    @celery.task(bind=True, max_retries=3)
    def generate_recommendations(self, user_id):

        try:
            return call_recommendation_service(user_id)

        except TemporaryServiceError as exc:

            raise self.retry(
                exc=exc,
                countdown=2 ** self.request.retries
            )

    - Timeout → Retry → Backoff → Circuit Breaker → Fallback → Idempotency

7. What is idempotency ?
    - Performing the same operation multiple times produces the same final result as performing it once.
    - Idempotency means designing an operation so that executing it multiple times has the same business effect
        as executing it once, which is critical when retries or at-least-once message delivery can cause duplicate execution.


"""