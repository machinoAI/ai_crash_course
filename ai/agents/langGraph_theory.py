"""
1. Why would you choose LangGraph over LangChain? What problems does it solve?
    - LangChain is designed for sequential (linear) LLM workflows.
    - Best suited for RAG, prompt chaining, simple tool calling.
    - LangGraph is designed for stateful, agentic workflows.
    - Uses a graph architecture instead of a linear chain.
    - Supports shared state management across nodes.
    - Enables loops (cyclic workflows).
    - Supports conditional routing.
    - Supports parallel execution.
    - Enables multi-agent collaboration.
    - Supports checkpointing and resumability.
    - Supports Human-in-the-Loop.
    - Preferred for production-grade AI agents.

    One-liner:
    Use LangChain for simple sequential pipelines and LangGraph for complex, stateful, multi-agent workflows.

2. Explain the architecture of LangGraph. What are State, Nodes, Edges and Conditional Edges?

    - State: Core of LangGraph. Shared data object passed across nodes.
    - Contains:
        - Messages
        - User query
        - Retrieved documents
        - Tool outputs
        - Intermediate reasoning
        - Agent decisions

    - Every node reads and updates the state.
    - Nodes: Individual computation units. Can be:
        - LLM
        - Tool
        - Retriever
        - Python function
        - Agent
        - Another graph
        - Edges
    - Define execution flow. Fixed transition between nodes.
        - Conditional Edges
        - Dynamic routing: Decide next node based on current state.
    - Checkpointer:
        - Persists execution state.
        - Resume after failure.
        - Supports Human-in-the-Loop.
        - Enables long-running workflows.

    One-liner: LangGraph consists of State, Nodes, Edges, Conditional Edges, and Checkpointing, enabling stateful workflow orchestration.

3. How does state management work in LangGraph?

    - State is the shared data object.
    - Passed to every node.
    - Nodes never communicate directly.
    - Nodes read from state.
    - Nodes update state.
    - Updated state is passed to next node.
    - Makes workflows modular.
    - Easy to extend.
    - Supports multi-agent communication.
    - Example State:
        {
          "messages":[],
          "documents":[],
          "tool_output":"",
          "next_agent":"planner"
        }

    One-liner: Nodes communicate through the shared state, not directly with each other.

4. How do you build a multi-agent workflow using LangGraph?

    - Every agent becomes a node.
    - Supervisor routes work.
    - Shared state connects all agents.
    - Conditional edges decide routing.
    - Agents may execute:
        - Sequentially
        - In parallel
    - Each agent has one responsibility.
    - Easy to maintain.
    - Easy to scale.
    - Example:
        - Planner Agent
        - Search Agent
        - SQL Agent
        - Coding Agent
        - Response Agent

    One-liner: Multi-agent systems are built by connecting specialized agents through a shared state and orchestrating them with conditional routing.

5. How does LangGraph support loops, retries and iterative reasoning?

    - Supports cyclic graphs.
    - Can revisit previous nodes.
    - Agent can:
        - Think
        - Call Tool
        - Evaluate
        - Retry
        - Think Again
    - Retry failed APIs.
    - Retry failed validation.
    - Continue until goal achieved.
    - Doesn't require restarting workflow.

    One-liner: LangGraph supports iterative reasoning through loops, retries, and cyclic execution.

6. What are Checkpointers? Explain InMemorySaver, SQLite and PostgreSQL.

    - Checkpointer:
        - Saves execution state.
        - Enables resume.
        - Enables recovery.
        - Supports Human-in-the-Loop.
        - Supports long-running agents.
    - InMemorySaver:
        - RAM only.
        - Lost after restart.
        - Development only.
    - SQLite:
        - Local persistence.
        - Good for testing.
        - Survives restart.
    - PostgreSQL:
        - Persistent storage.
        - Production ready.
        - Concurrent users.
        - Scalable.

    One-liner: Checkpointing persists graph execution so workflows can pause, resume, and recover from failures.

7. How do you implement Human-in-the-Loop?

    - Agent performs reasoning.
    - Workflow pauses.
    - Checkpoint saved.
    - Human reviews output.
    - Human approves/rejects.
    - Workflow resumes from checkpoint.
    - Used for critical operations.
    - Examples:
        - Delete database
        - Refund money
        - Merge PR
        - Deploy production
        - Send legal email

    One-liner: Human-in-the-Loop pauses execution, waits for approval, and resumes from the saved checkpoint.

8. How do you make LangGraph production ready?

    - Include:
        - Checkpointing
        - Retry mechanism
        - Timeouts
        - Validation
        - Guardrails
        - Human approval
        - Logging
        - Monitoring
        - Observability
        - Parallel execution
        - Persistent database
        - Error handling
        - Security
        - RBAC
        - Token monitoring
        - Cost monitoring
        - Latency monitoring
    - Tools:
        - LangSmith
        - OpenTelemetry
        - MLflow
        - Signoz

    One-liner: Production-ready LangGraph systems require reliability, observability, fault tolerance, validation, and scalable persistence.

9. How do parallel execution and branching work?

    - Branching:
        - Uses conditional edges.
        - Route based on state.
        - Dynamic execution.
        - Example:
            Customer Query
            ↓
            Billing Agent  or  Technical Agent
    - Parallel Execution:
        - Independent nodes execute together.
        - Example:
            Search Docs
            Search Web
            Search SQL
        - Run simultaneously.
        - Merge outputs.
        - Pass merged state.
    - Benefits:
        - Lower latency
        - Better throughput
        - Faster response

    One-liner: Conditional edges enable branching, while parallel execution reduces latency by running independent tasks simultaneously.

10. Design a production-grade AI system using LangGraph.

    - Architecture:
        User
        ↓
        API
        ↓
        Supervisor
        ↓
        Planner
        ↓
        Specialized Agents
        ↓
        Validator
        ↓
        Human Approval
        ↓
        Response
    - Components:
        - Supervisor Agent
        - Shared State
        - Planner
        - Specialized Agents
        - Tool Calling
        - Validation
        - Human Approval
        - Response Generator
        - Checkpointer
        - Logging
        - Monitoring
        - Database
    - Production Features:
        - Shared state
        - Parallel execution
        - Retry
        - Timeout
        - Validation
        - Guardrails
        - Human-in-the-Loop
        - PostgreSQL
        - Observability
        - Security
        - Scalability
        - Fault tolerance

    One-liner: Design LangGraph around a supervisor-worker architecture with shared state, checkpointing, validation, and production-grade observability.

10-Second Revision Sheet

    | Question       | Remember                                                 |
    |----------------|----------------------------------------------------------|
    | Why LangGraph? | Stateful multi-agent orchestration                       |
    | Architecture   | State → Nodes → Edges → Conditional Edges → Checkpointing |
    | State          | Shared object passed between nodes                       |
    | Multi-Agent    | Supervisor + Shared State                                |
    | Loops          | Cyclic execution, retries, reasoning                     |
    | Checkpointer   | Save → Resume → Recover                                  |
    | Human Loop     | Pause → Approve → Resume                                  |
    | Production     | Retry, Validation, Monitoring, Security                  |
    | Parallel       | Run independent nodes together                           |
    | System Design  | Supervisor + Agents + State + Checkpoints + Observability |
"""