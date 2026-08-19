"""
1. What is Microservices Architecture?

- Microservices = an architectural style where one application is built as a suite of small, independently deployable services.
- Each service:
  - Runs in its own process.
  - Communicates through lightweight mechanisms, commonly HTTP APIs.
  - Is organized around a business capability.
  - Can be deployed independently.
  - Can potentially use a different language, framework, or database.

  User
    │
    ▼
  ┌─────────────────────────────────────────────┐
  │              Microservices                  │
  │                                             │
  │  User ──► Order Service ──► Payment       │
  │                    │                        │
  │                    └──────► Inventory      │
  │                                             │
  └─────────────────────────────────────────────┘


2. What is the most important characteristic of a Microservice?

- Business Capability = a meaningful business responsibility that the organization performs.

- Services should be organized around business capabilities, NOT technical layers.

  Bad:

  UI Service
  Database Service
  Business Logic Service

  Better:

  Order Service
  Payment Service
  Inventory Service
  Shipping Service

- This creates stronger boundaries around business functionality.


3. What is Componentization via Services?

- Componentization = breaking a system into independently replaceable and deployable components.
- In microservices, the service itself becomes the architectural component.

- Important difference:

  Traditional application:
  Components → libraries/modules → one deployment

  Microservices:
  Components → independent services → independent deployment

- A service therefore provides a stronger boundary than an ordinary in-process module.


4. Why is independent deployment important?

- Independent Deployment = a service can be changed and released without rebuilding/redeploying the entire application.

  Before:

  Change Payment
       ↓
  Rebuild entire application
       ↓
  Deploy everything

  Microservices:

  Change Payment
       ↓
  Build Payment Service
       ↓
  Deploy Payment Service only

- Benefits:
  - Faster release cycles.
  - Smaller deployment risk.
  - Teams can work independently.
  - Failures are more isolated.


5. What is the relationship between Microservices and teams?

- Microservices encourage autonomous, cross-functional teams.
- A team can own the complete lifecycle of its services.

- Cross-functional Team = team containing the skills needed to build and operate its service, rather than depending on separate centralized teams for every function.

  Team A → Order Service
  Team B → Payment Service
  Team C → Inventory Service

- Service boundaries and team boundaries can reinforce each other.


6. How big should a Microservice be?

- There is NO universal number of lines of code, endpoints, or servers that defines a microservice.
- The important question is the responsibility it encapsulates.
- "Micro" should NOT be interpreted as "as tiny as possible."

- Good rule:

  As small as possible
          +
  As large as necessary
          ↓
  To represent a meaningful business/domain capability

- Fowler emphasizes that service size is less important than having appropriate boundaries.


7. What is "Smart Endpoints and Dumb Pipes"?

- Smart Endpoint = service contains business logic and makes decisions.
- Dumb Pipe = communication mechanism mainly transports messages/data.

- Example:

  Order Service
      │
      │ HTTP/API/Event
      ▼
  Payment Service

- Business intelligence belongs inside the services rather than inside a centralized ESB/message layer.

- This favors:
  - Simple communication.
  - Autonomous services.
  - Decentralized logic.


8. What is Decentralized Governance?

- Decentralized Governance = teams have freedom to choose technologies and implementation approaches appropriate for their service.

- Different services may use:

  Order      → Java + PostgreSQL
  Payment    → Go + MySQL
  Analytics  → Python + MongoDB

- The goal is not "everyone uses a different technology."
- The goal is to avoid unnecessary centralized technology control.

- Standardization can still be used where it makes operational sense.


9. What is Decentralized Data Management?

- Decentralized Data Management = each service owns/manages the data associated with its business capability.

  Order Service
      ↓
  Order DB

  Payment Service
      ↓
  Payment DB

  Inventory Service
      ↓
  Inventory DB

- Important principle:

  Service owns its data.

- Other services should access the capability through the service API rather than directly accessing its database.


10. Why is decentralized data management difficult?

- In a monolith:

  One DB
    ↓
  One transaction
    ↓
  Strong consistency is relatively easy

- In microservices:

  Service A DB
       +
  Service B DB
       +
  Service C DB

  ↓

  Distributed state

- Maintaining strong consistency across services becomes much harder.
- This often leads to accepting/managing Eventual Consistency.

- Eventual Consistency = different services may temporarily observe different states, but the system converges toward a consistent state.


11. What is the biggest cost of Microservices?

- Distribution.

- Distribution = functionality is spread across processes/services connected through a network.

- In a monolith:

  Service A → Service B

  may be an in-process function call.

- In microservices:

  Service A → Network → Service B

- Network calls introduce:
  - Latency.
  - Network failures.
  - Timeouts.
  - Partial failures.
  - Serialization/deserialization.
  - Operational complexity.

- Therefore:

  Remote call ≠ local function call.


12. What does "Design for Failure" mean?

- Design for Failure = assume that individual services, machines, networks, or dependencies can fail.

- Example:

  Order Service
      ↓
  Payment Service
      ↓
  Payment unavailable

- The Order Service should not blindly wait forever.

- Common techniques:
  - Timeouts.
  - Retries.
  - Circuit breakers.
  - Fallbacks.
  - Idempotency.
  - Monitoring/alerting.

- Core principle:

  In a distributed system,
  failure is normal, not exceptional.


13. What is a Circuit Breaker?

- Circuit Breaker = mechanism that stops repeatedly calling a failing downstream service.

  Normal:
  A → B
      ✓

  Failure:
  A → B
      ✗
      ✗
      ✗

  Circuit opens:

  A ──X──► B

- Instead of continuously sending requests to a failing service, the caller fails fast or uses a fallback.

- This prevents cascading failures.


14. What is Infrastructure Automation?

- Infrastructure Automation = automatically provisioning, deploying, configuring and operating services/infrastructure instead of manually performing these tasks.

- Microservices require automation because there may be many independently deployed services.

  Code
    ↓
  Build
    ↓
  Test
    ↓
  Deploy
    ↓
  Monitor

- CI/CD becomes particularly important.


15. Why is operational complexity higher in Microservices?

- Monolith:

  1 application
      ↓
  1 deployment unit
      ↓
  relatively simple operations

- Microservices:

  50 services
      ↓
  50 deployments
  50 logs
  50 health checks
  many network dependencies
  many versions
  many failure points

- Therefore microservices require mature:
  - Deployment automation.
  - Monitoring.
  - Logging.
  - Alerting.
  - Service discovery.
  - Incident management.


16. What are the major benefits of Microservices?

- Strong Module Boundaries
  - Services reinforce separation between business capabilities.

- Independent Deployment
  - Services can be released independently.

- Independent Scaling
  - Scale only the service that needs additional capacity.

- Technology Diversity
  - Different services can use different technologies when justified.

- Team Autonomy
  - Teams can independently own services.

- Fault Isolation
  - A failure can potentially be contained to one service instead of bringing down the entire application.


17. What are the major disadvantages?

- Distribution
  - Network calls are slower and can fail.

- Eventual Consistency
  - Cross-service strong consistency is difficult.

- Operational Complexity
  - Many services must be deployed, monitored and maintained.

- Testing Complexity
  - Multiple independently deployable services create additional integration/testing challenges.

- Debugging Complexity
  - One user request may cross many services.

- Deployment Complexity
  - Many services have independent versions and dependencies.


18. Microservices vs Monolith — what is the important difference?

  Monolith

  ┌─────────────────────────────┐
  │ Order                       │
  │ Payment                     │
  │ Inventory                   │
  │ Shipping                    │
  │                             │
  │      One application        │
  └─────────────────────────────┘

  Microservices

  ┌─────────┐   ┌─────────┐
  │ Order   │   │ Payment │
  └─────────┘   └─────────┘
       │             │
  ┌─────────┐   ┌─────────┐
  │Inventory│   │Shipping │
  └─────────┘   └─────────┘

- Monolith:
  - Simpler distribution.
  - Easier local development.
  - Easier transactions.
  - Entire application often deployed together.
  - Scaling is generally at application level.

- Microservices:
  - Stronger service boundaries.
  - Independent deployment.
  - Independent scaling.
  - More operational/distributed-system complexity.


19. Does Microservices always mean better architecture?

- NO.

- Fowler explicitly emphasizes that microservices have trade-offs.
- Many systems may be better served by a well-structured monolith.

- Choose microservices when the benefits justify the additional complexity.

  Microservices
      ↓
  Benefits
      +
  Distribution Cost
      +
  Operational Cost
      ↓
  Evaluate against business context


20. What is the "Microservice Premium"?

- Microservice Premium = additional cost and risk introduced by adopting microservices.

- You pay for:
  - Distributed communication.
  - Deployment infrastructure.
  - Monitoring.
  - Service coordination.
  - Distributed data.
  - Operational complexity.

- Therefore:

  Microservices are NOT "free scalability."

  They exchange:

  Simpler modularity/deployment
          for
  Higher distributed-system complexity.


21. What does "Monolith First" mean?

- Monolith First = start with a well-structured monolith and extract services when there is a clear reason to do so.

- Fowler observed that many successful microservice systems evolved from monoliths that became too large.

- However, this is a recommendation/trade-off, NOT a universal law.

- Important interview answer:

  "I wouldn't blindly choose microservices. I would start with a modular architecture and extract services when independent deployment, scaling, ownership, or business boundaries justify the complexity."


22. How should you break a Monolith into Microservices?

- Don't split based purely on technical layers.

- Identify:
  - Business capabilities.
  - Important business boundaries.
  - Areas that change frequently.
  - Capabilities that can become independently owned.

- Migration approach:

  Monolith
      ↓
  Identify business capability
      ↓
  Extract relatively independent service
      ↓
  Minimize dependency back to monolith
      ↓
  Move data ownership
      ↓
  Independently deploy
      ↓
  Repeat


23. What does "Go Macro First, then Micro" mean?

- Go Macro First = initially extract reasonably large, cohesive services rather than immediately creating dozens of tiny services.

- Why?
  - Easier to understand.
  - Lower operational complexity.
  - Easier to identify correct boundaries.
  - Boundaries can be refined later.

- Avoid:

  Monolith
      ↓
  50 tiny services immediately

- Prefer:

  Monolith
      ↓
  Few meaningful business services
      ↓
  Refine boundaries over time


24. What is Evolutionary Design?

- Evolutionary Design = architecture evolves incrementally as understanding of the business and system improves.

- Instead of trying to design the perfect service boundaries upfront:

  Understand
      ↓
  Extract
      ↓
  Observe
      ↓
  Refine
      ↓
  Repeat

- Microservice boundaries should be allowed to evolve.


25. What is a key mistake when designing Microservices?

- Creating services around technical concepts rather than business capabilities.

- Bad:

  User Controller Service
  Database Service
  Authentication Utility Service
  Email Utility Service

- Better:

  Customer Service
  Order Service
  Payment Service
  Inventory Service

- The service should own a coherent business capability.


26. What does "Products not Projects" mean?

- Project mindset = team builds software and eventually hands it off.

- Product mindset = team owns the service continuously through its lifecycle.

  Build
    ↓
  Deploy
    ↓
  Operate
    ↓
  Monitor
    ↓
  Improve

- Teams are responsible for the long-term health of their services.


27. Why does testing become harder with Microservices?

- A monolith mostly uses in-process calls.

- Microservices introduce network boundaries.

  Service A
      ↓
    Network
      ↓
  Service B
      ↓
    Network
      ↓
  Service C

- Therefore you need to test:
  - Individual services.
  - Service contracts.
  - Integration behavior.
  - End-to-end workflows.

- More services = more interaction paths.


28. Why is "service size" a bad interview definition?

- Saying:

  "A microservice must have 100 lines of code."

  is incorrect.

- There is no universal size.
- What matters more:
  - Business responsibility.
  - Cohesion.
  - Independent deployability.
  - Team ownership.
  - Data ownership.
  - Operational maturity.

- Interview phrase:

  "I optimize for the right business boundary, not an arbitrary number of lines of code."


29. What are the most important Microservices characteristics to remember?

- Componentization via Services
- Organized around Business Capabilities
- Products, not Projects
- Smart Endpoints, Dumb Pipes
- Decentralized Governance
- Decentralized Data Management
- Infrastructure Automation
- Design for Failure
- Evolutionary Design


30. What is the best interview answer to "Why Microservices?"

- I would choose microservices when the system has clear business boundaries and the organization benefits from independent ownership, deployment and scaling.
- The major benefits are strong module boundaries, independent deployment, independent scaling and technology/team autonomy.
- But microservices introduce distributed-system and operational complexity, including network failures, eventual consistency and more difficult testing/observability.
- Therefore, I would not choose microservices by default; I would choose them when their benefits justify the operational and distributed-system costs.


31. What are the 5 things I should remember for an interview?

- 1. Business Capability
      → Services should represent meaningful business boundaries.

- 2. Independent Deployment
      → One service can be changed and deployed independently.

- 3. Decentralized Data
      → Service owns its data; cross-service consistency becomes harder.

- 4. Design for Failure
      → Network calls fail; use timeouts, retries, circuit breakers, etc.

- 5. Trade-offs
      → Microservices improve modularity/autonomy but add distributed and operational complexity.


32. Final mental model

  Business Capability
          ↓
  Autonomous Service
          ↓
  Own Data
          ↓
  Independent Deployment
          ↓
  Independent Scaling
          ↓
  Network Communication
          ↓
  Distributed-System Failures
          ↓
  Automation + Observability + Resilience

- Core principle:

  "Microservices are not about making services tiny.
   They are about creating autonomous boundaries around
   business capabilities and allowing those services to
   evolve, deploy and scale independently."


"""