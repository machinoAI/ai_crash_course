"""
1. Why would you choose FastAPI over Django?

    FastAPI:
        - Primarily requirement is building APIs.
        - Workload has significantly I/O concurrency
        - Native support of async programming.
        - Automatic openAPI documentation
        - Pydantic based validation

    Django:
        - When required full-featured application with:
            - Integrated ORM
            - Authentication
            - Admin
            - Middleware
            - Migrations and other batteries-included capabilities, Django
                can significantly reduce development effort.

2. Is FastAPI faster than Django?
    - Performance depends on the workload and implementation.
    - FastAPI has an efficient ASGI-based async architecture and can perform very well for I/O-heavy APIs,
    - but database queries, application logic, serialization and external dependencies
        often dominate real-world latency.

3. WSGI vs ASGI?
    WSGI (Web Server Gateway Interface): Traditional Python web-server interface:

        Request
           ↓
        WSGI application
           ↓
        Response


    ASGI (Asynchronous Server Gateway Interface): Designed for modern async applications:

        Request
           ↓
        ASGI application
           ↓
        async processing
           ↓
        Response


4. How would you handle authentication in FastAPI?

    Request
       ↓
    Authentication middleware/dependency
       ↓
    Validate JWT
       ↓
    Extract user identity
       ↓
    Authorization
       ↓
    Endpoint
5.  What is difference between Authentication and Authorization ?

    - Authentication = Who are you?
    - Authorization = What are you allowed to do?


6. How would you scale a FastAPI service?

                    Load Balancer
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          FastAPI     FastAPI     FastAPI
          worker      worker      worker
             │           │           │
             └───────────┼───────────┘
                         │
                     Redis/DB

    Then consider:
        - Horizontal scaling
        - Connection pooling
        - Redis caching
        - DB indexing
        - Async I/O
        - Rate limiting
        - CDN where appropriate
        - Kubernetes
        - Autoscaling
        - Observability


7. How would you design a production FastAPI service?

                Load Balancer
                      │
                      ▼
                 FastAPI
                      │
          ┌───────────┼────────────┐
          │           │            │
        Redis        DB       External APIs
          │           │            │
          └───────────┼────────────┘
                      │
                   Celery
                      │
                   Workers

    - Authentication
    - Authorization
    - Rate limiting
    - Timeouts
    - Retries
    - Circuit breakers
    - Caching
    - Logging
    - Metrics
    - Tracing
    - Health checks
    - CI/CD
    - Docker
    - Kubernetes

Note: Don't choose a framework based on benchmark speed.
    Choose based on workload, architecture, ecosystem, team expertise,
        scalability requirements and operational complexity.
"""