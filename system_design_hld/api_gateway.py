"""
1. What is an API Gateway?

- API Gateway = a single logical entry point between clients and backend microservices.
- It receives client requests, determines the target service, and routes the request.
- It can also provide cross-cutting concerns such as:
  - Authentication/Authorization
  - Rate limiting
  - API composition
  - Service discovery
  - Request/response transformation
  - Caching
  - Logging/monitoring

  Client
     │
     ▼
  API Gateway
     │
     ├────► Order Service
     ├────► Payment Service
     ├────► Invoice Service
     └────► Sales Service


2. Is an API Gateway physically a single server?

- No.
- "Single entry point" is a logical concept, not necessarily one physical machine.
- Multiple gateway instances can run across regions and availability zones.

  Client
    │
    ▼
  Global DNS / Traffic Manager
    │
    ├────► Region 1 → API Gateway instances
    │
    └────► Region 2 → API Gateway instances

- This provides scalability and removes the gateway as a physical Single Point of Failure.


3. What is the difference between an API Gateway and a Load Balancer?

- Load Balancer = distributes traffic across multiple instances of the same service.
- API Gateway = understands API-level routes and decides which microservice should handle the request.

  Client
     │
     ▼
  API Gateway
     │
     ├── /order   ──► Order Service
     ├── /payment ──► Payment Service
     └── /invoice ──► Invoice Service
                         │
                         ▼
                   Load Balancer
                    /    |    \
                  MS1   MS2   MS3

- Example:
  - /api/order → Order Service
  - /api/invoice → Invoice Service

- The Load Balancer then distributes the Order request among Order Service instances.

- Memory trick:

  API Gateway → WHICH service?
  Load Balancer → WHICH instance?


4. What is API Composition?

- API Composition = API Gateway combines data from multiple backend services and returns one response to the client.

- Without composition:

  Client
    ├──► Product Service
    ├──► Invoice Service
    ├──► Rating Service
    └──► Recommendation Service

- With API Composition:

  Client
      │
      ▼
  API Gateway
      │
      ├──► Product
      ├──► Invoice
      ├──► Rating
      └──► Recommendation
              │
              ▼
        Aggregate Response
              │
              ▼
            Client

- Benefits:
  - Fewer client-side API calls.
  - Lower client complexity.
  - Gateway can make downstream calls in parallel.
  - Useful when different clients need different amounts of data.


5. Why is API Composition useful for different clients?

- Different clients may need different data.

- Mobile:
  - Product details
  - Invoice details

- Desktop:
  - Product
  - Invoice
  - Ratings
  - Recommendations

- Instead of making clients understand all backend services, the gateway provides a client-friendly API.

- This reduces client-side network round trips and complexity.


6. How does an API Gateway handle Authentication and Authorization?

- Authentication = verifying WHO the client/user is.
- Authorization = verifying WHAT the authenticated user is allowed to access.

- Typical OAuth 2.0 flow:

  Client
    │
    ├──► Authorization Server
    │        │
    │        └──► Access Token
    │
    ▼
  API Gateway
    │
    ├── Validate token
    │
    ├── Invalid → Reject
    │
    └── Valid → Route request
                 │
                 ▼
             Microservice

- Token validation can happen by:
  - Calling the Authorization Server.
  - Locally verifying a cryptographic signature.

- Benefit:
  - Authentication logic does not need to be duplicated in every microservice.


7. What is Rate Limiting?

- Rate Limiting = restricting how many requests a client can make within a specified period.

- Example:

  User → /api/invoice
       → maximum 10 requests/minute

  Request 1 ✓
  Request 2 ✓
  ...
  Request 10 ✓
  Request 11 → HTTP 429

- HTTP 429 = Too Many Requests.


8. What is Throttling?

- Throttling = controlling request traffic when it exceeds the allowed processing rate.

- It can be applied based on:
  - User
  - Application/client
  - IP
  - API endpoint

- Example:

  /api/invoice
      ↓
  10 requests/min/user

- Rate limiting and throttling are closely related:
  - Rate limiting defines/limits allowed request rate.
  - Throttling controls traffic when that rate is exceeded.


9. What is a Burst Limit?

- Burst Limit = maximum amount of traffic that can be accepted during a sudden traffic spike.

- Example:

  Burst capacity = 500 requests

  Normal traffic
       ↓
  Sudden spike
       ↓
  First 500 accepted
       ↓
  Additional traffic
       ↓
  429 / queue depending on configuration


10. How can an API Gateway protect against a traffic spike?

- It can use:
  - Rate limiting
  - Burst limits
  - Throttling
  - Queuing
  - IP blocking

- Queue = temporary waiting area where excess requests are held instead of being immediately rejected.

  Traffic Spike
       ↓
  API Gateway
       ↓
  ┌───────────────┐
  │ Request Queue │
  └───────────────┘
       ↓
  Backend processes gradually

- This can help protect downstream services from sudden traffic surges.


11. What is Service Discovery?

- Service Discovery = mechanism that allows services to find the current network location of other services.

- Problem:
  - Microservices scale dynamically.
  - Instances may be created/destroyed.
  - IP addresses and ports can change.

- Example:

  Order Service
     Instance 1 → 10.0.1.5:8080
     Instance 2 → 10.0.2.7:8080

  Service Discovery Registry
            ▲
            │
       API Gateway

- Examples mentioned:
  - Netflix Eureka
  - HashiCorp Consul


12. How does Service Discovery work with an API Gateway?

- 1. Service starts.
- 2. Service registers its IP/port with the registry.
- 3. Registry tracks service health.
- 4. Failed instances are removed.
- 5. API Gateway discovers healthy instances.
- 6. Gateway routes traffic to an available instance.

  Service starts
      ↓
  Register with Registry
      ↓
  Health checks
      ↓
  Healthy instances
      ↓
  API Gateway
      ↓
  Backend Service


13. What is Request/Response Transformation?

- Request Transformation = modifying an incoming request before sending it downstream.
- Response Transformation = modifying a backend response before returning it to the client.

- Gateway may modify:
  - Headers
  - Query parameters
  - Request body
  - Response format

- Purpose:
  - Hide backend implementation details.
  - Adapt different backend APIs to a consistent client-facing API.


14. What is API Gateway Caching?

- Gateway Cache = storing frequently requested responses at the gateway/edge so the request does not need to reach backend services.

  Client
    │
    ▼
  API Gateway
    │
    ├── Cache HIT ──► Return response
    │
    └── Cache MISS ─► Backend Service
                         │
                         ▼
                       Response
                         │
                         ▼
                       Cache

- Benefits:
  - Lower latency.
  - Reduced backend load.
  - Fewer downstream requests.

- Most useful for static or slowly changing data.


15. Why is an API Gateway useful for Logging and Monitoring?

- The gateway is a central point through which client requests pass.
- It can collect:
  - Request logs
  - Latency
  - Request counts
  - Error rates
  - Access information

- This provides a centralized view of API traffic across services.


16. How does an API Gateway handle millions of requests?

- The gateway itself must be horizontally scalable.

- Horizontal Scaling = adding more instances rather than making one server bigger.

  Global DNS / Traffic Manager
             │
       ┌─────┴─────┐
       ▼           ▼
   Region 1     Region 2
       │           │
   Gateway ×N   Gateway ×N
       │           │
     Load         Load
   Balancer     Balancer
       │           │
   Services     Services

- Multiple gateway instances distribute traffic.
- Multiple regions provide geographic redundancy.
- Multiple Availability Zones protect against data-center/AZ failures.


17. What is an Availability Zone (AZ)?

- Availability Zone = isolated physical data-center infrastructure within a cloud region, designed to provide failure isolation.

- Example:

  Region
  ├── AZ1
  ├── AZ2
  └── AZ3

- If AZ1 fails, traffic can be served from healthy AZs.


18. What is a Region?

- Region = geographical cloud location containing multiple Availability Zones.

- Example:

  Region 1
    ├── AZ1
    ├── AZ2
    └── AZ3

  Region 2
    ├── AZ1
    ├── AZ2
    └── AZ3

- Multiple regions provide protection against an entire regional outage.


19. What is the complete highly available API Gateway architecture?

  Client
     │
     ▼
  Global DNS / Traffic Manager
     │
     ├──────────────────┐
     ▼                  ▼
  Region 1            Region 2
     │                  │
  API Gateway ×N      API Gateway ×N
     │                  │
  Load Balancer       Load Balancer
     │                  │
  ┌──┴──┐             ┌──┴──┐
  MS1  MS2            MS1  MS2
     │                  │
     ▼                  ▼
  Service Discovery + Health Checks

- Global DNS chooses a healthy/appropriate region.
- Multiple gateway instances provide horizontal scaling.
- Regional load balancers distribute traffic across service instances.
- Service discovery identifies healthy backend instances.


20. What happens when a Microservice instance fails?

- Health checks identify the unhealthy instance.
- Load Balancer stops routing traffic to it.
- Other healthy instances continue serving requests.

  MS1 ✓
  MS2 ✗
  MS3 ✓

  Load Balancer
      │
      ├──► MS1 ✓
      └──► MS3 ✓

- MS2 receives no new traffic until it becomes healthy again.


21. What happens when an Availability Zone fails?

- Gateway/load-balancing infrastructure detects the failure.
- Traffic is shifted to healthy instances in another AZ.

  AZ1 ✗
      ↓
  Traffic → AZ2 ✓
          → AZ3 ✓

- This provides AZ-level fault tolerance.


22. What happens when an entire Region fails?

- Global DNS/traffic management detects regional health failure.
- Requests are redirected to another healthy region.

  Client
    │
    ▼
  Global DNS
    │
    ├── Region 1 ✗
    │
    └── Region 2 ✓
            ↓
       API Gateway

- This provides regional disaster recovery/failover.


23. Is DNS a Single Point of Failure?

- No, DNS itself is a distributed and highly redundant system.

- DNS hierarchy:

  Local Resolver
       ↓
  Root DNS
       ↓
  TLD Server
       ↓
  Authoritative DNS
       ↓
  IP / Endpoint

- DNS responses are heavily cached at different levels.
- Authoritative DNS providers operate redundant infrastructure.
- Therefore, a single DNS server failure does not imply global DNS failure.


24. What are the most important API Gateway responsibilities?

- Request Routing
  → Decide which backend service should handle the request.

- API Composition
  → Combine responses from multiple services.

- Authentication/Authorization
  → Validate identity and access at the edge.

- Rate Limiting/Throttling
  → Control traffic and protect backend services.

- Service Discovery
  → Find healthy dynamic service instances.

- Transformation
  → Adapt requests/responses between clients and services.

- Caching
  → Return frequently requested data without calling backend services.

- Logging/Monitoring
  → Centralize API-level observability.


25. What is the most important difference between API Gateway and Load Balancer?

- API Gateway:

  "Which SERVICE should receive this request?"

- Load Balancer:

  "Which INSTANCE of that service should receive this request?"

- Typical flow:

  Client
    ↓
  API Gateway
    ↓
  Order Service Load Balancer
    ↓
  Order Instance 1 / 2 / 3


26. What are the key interview takeaways?

- API Gateway = intelligent entry point for microservices.
- It is a logical single entry point, not necessarily a single physical server.
- API Gateway performs application/API-level routing.
- Load Balancer distributes traffic among instances of a service.
- API Composition reduces client-side calls and complexity.
- Authentication can be centralized at the gateway.
- Rate limiting protects downstream services from abuse and traffic spikes.
- Service Discovery handles dynamically changing service instances.
- Caching reduces latency and backend load.
- Multiple gateway instances + multiple AZs/regions provide high availability.
- DNS/traffic management can route users to healthy regions.
- API Gateway adds functionality but also becomes an important infrastructure component that must itself be highly available and scalable.


27. What is the one-line mental model?

- API Gateway = "The intelligent front door of a microservices system."

  Client
     ↓
  API Gateway
     ↓
  ┌───────────────┬───────────────┬───────────────┐
  │ Authentication│ Rate Limiting │ Composition   │
  │ Routing       │ Caching       │ Transformation│
  │ Discovery     │ Logging       │               │
  └───────────────┴───────────────┴───────────────┘
     ↓
  Microservices
"""