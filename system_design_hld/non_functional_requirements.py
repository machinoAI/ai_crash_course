"""
1. What is a Non-Functional Requirement (NFR)?

    - NFR = a system-level quality/constraint that describes HOW the system should behave, rather than WHAT functionality it provides.
    - Examples:
      - Performance
      - Scalability
      - Reliability
      - Security
      - Usability
      - Maintainability
      - Portability
      - Capacity
      - Regulatory compliance
      - Localization

    - Key idea:

      Functional Requirement  → What the system DOES
      NFR                    → HOW WELL / UNDER WHAT CONSTRAINTS it does it


2. What is the difference between Functional and Non-Functional Requirements?

  Functional Requirement
  - Describes system behavior/features.
  - Usually tied to a specific use case or component.
  - Example:
      "When a user registers, create the account and send an email."

  Non-Functional Requirement
  - Describes system-level quality or constraint.
  - Applies across the system rather than one feature.
  - Example:
      "95% of requests must complete within 3 seconds."

- Important:
  - Functional requirements are generally easier to trace to code/modules.
  - NFRs are often system-wide and harder to trace to a single code location.


3. Why are NFRs important?

    - A system can satisfy all functional requirements and still fail in production.

      Example:

      Feature works ✓
          ↓
      But:
      - 10-second response time
      - crashes under high traffic
      - poor mobile experience
      - difficult to use
          ↓
      System fails from user's perspective

    - NFRs strongly influence:
      - Architecture
      - Infrastructure
      - Design patterns
      - Testing strategy
      - Scalability decisions
      - Long-term maintainability


4. What are the major types of NFRs mentioned in the article?

    - Capacity = how much data the system can store/handle.

    - Regulatory = laws/regulations the system must comply with.

    - Portability = ability to work across different browsers, operating systems or platforms.

    - Reliability = ability to remain available and recover from failures.

    - Performance = how quickly requests are processed and how much traffic the system can handle.

    - Localization = ability to adapt to region-specific concepts such as timezone, measurements, etc.


5. What is the difference between Performance, Scalability and Capacity?

    - Performance = how fast the system responds or processes work.
      - Example: 95% of requests complete within 3 seconds.

    - Scalability = how well the system handles increasing load.
      - Example: system continues to perform acceptably as users increase from 10K to 100K.

    - Capacity = maximum amount of data/work the system can hold or handle.
      - Example: system must support 10 TB of stored data.

    - Easy memory:

      Performance → How FAST?
      Scalability → How well does it grow?
      Capacity → How MUCH?


6. What is Reliability?

    - Reliability = ability of the system to remain usable and recover correctly when failures occur.
    - Important questions:
      - How often can the system fail?
      - What happens when a component fails?
      - How quickly can the system recover?

    - Reliability is therefore broader than simply "the server is up."


7. What is an important difference between Availability and Reliability?

    - Availability = whether the system is accessible/usable at a particular time.
    - Reliability = ability to operate correctly and handle/recover from failures over time.

    - Memory:

      Availability → "Is it available now?"
      Reliability  → "Can it keep working correctly and recover from failures?"


8. How should an NFR be written?

    - Avoid vague requirements such as:

        "The system should be fast."

    - Make them measurable:

        "95% of requests should complete within 3 seconds."

    - Good NFRs should ideally contain:
      - Metric
      - Target
      - Conditions/load
      - Time window when relevant

    - Example:

        "The website should process each request
         within 4 seconds or less 99% of the time."


9. What are execution qualities and evolution qualities?

    - Execution Qualities = properties observable while the system is running.

      Examples:
      - Security
      - Usability
      - Efficiency
      - Performance
      - Speed

    - Evolution Qualities = properties related to how easily the system can change and evolve over time.

      Examples:
      - Maintainability
      - Testability
      - Flexibility
      - Scalability


10. How do NFRs influence architecture?

    - NFRs are not merely documentation requirements.
    - They can directly determine architectural components and patterns.

    - Example:

      Requirement:
      "User should continue using the website
       while a large video is being uploaded."

           ↓
      Synchronous upload blocks user
           ↓
      Need to decouple user request from processing
           ↓
      Event-based architecture
           +
      Job/Task Queue
           ↓
      Background processing


11. What is Decoupling?

    - Decoupling = separating components so one component does not have to wait for another component to finish its work.

    - Example:

      User
       ↓
      Upload API
       ↓
      Queue
       ↓
      Background Worker
       ↓
      Video Processing

    - User receives a quick response instead of waiting for video encoding/processing.


12. Why should NFRs be discovered early?

    - NFRs can fundamentally change the architecture.
    - If discovered late, architectural changes can become expensive.

    - Good sequence:

      Functional Requirements
              ↓
      Ask NFR questions
              ↓
      Define measurable constraints
              ↓
      Choose architecture
              ↓
      Implement


13. What questions should we ask to uncover NFRs?

    - How fast should it be?
    - How many users/requests should it support?
    - What happens when traffic increases?
    - What happens when a component fails?
    - How much data will be stored?
    - Are there auditing requirements?
    - What security constraints exist?
    - How easy should the system be to change?
    - Which platforms/browsers must be supported?
    - What regulations must be followed?



14. What are examples of measurable NFRs?

    - Performance:

        "99% of requests must complete within 4 seconds."

    - Load/Scalability:

        "The website should load within 5 seconds
         with more than 50,000 simultaneous users."

    - Security/Audit:

        "Every unauthorized request must be logged
         and retained for 5 years."

    - Key idea:
      - NFRs can span multiple quality attributes at the same time.


15. What is the relationship between NFRs and testing?

    - Functional requirements are commonly tested through:
      - Unit tests
      - Integration tests
      - Acceptance tests
      - End-to-end tests

    - NFRs require specialized testing such as:
      - Performance testing
      - Stress testing
      - Security testing
      - Usability testing

    - Therefore:

      Functional → "Does it work?"
      NFR        → "Does it work well enough under the required conditions?"


16. Why do NFRs often determine architectural choices?

    - Different NFRs create different architectural needs.

      High Performance
          → Caching / efficient processing

      High Scalability
          → Horizontal scaling / queues / distributed architecture

      High Reliability
          → Redundancy / failover / recovery mechanisms

      Async User Experience
          → Event-driven architecture / task queue

      Maintainability
          → Separation of concerns / patterns / testability

    - Architecture exists to satisfy BOTH functional and non-functional requirements.


17. What is the most important interview distinction?

    - Functional Requirements:

        WHAT does the system do?

    - Non-Functional Requirements:

        HOW should the system behave?

    - But NFRs are more than "performance."

      They describe system-level qualities such as:

        Performance
        Scalability
        Reliability
        Security
        Usability
        Capacity
        Portability
        Maintainability
        Regulatory constraints


"""