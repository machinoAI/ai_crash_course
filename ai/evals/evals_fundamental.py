"""
Topic 1: LLM Evaluation vs Agent Evaluation

Q1. What is LLM evaluation?

    - LLM evaluation is the process of measuring how well a language model performs a
    given task based primarily on its generated output.

    We may evaluate:
    - Correctness
    - Relevance
    - Factuality
    - Helpfulness
    - Code correctness
    - Instruction following
    - Safety

    Example:
    Question:
        "What is the capital of India?"
    LLM:
    "New Delhi"

    Expected:
        "New Delhi"
    → PASS

    For code generation:

    Prompt:
    "Write a Python function to calculate Fibonacci numbers."

    LLM:
    Generates Python code

    Evaluation:
    Run the generated code against test cases.

    → PASS if the implementation behaves correctly.

Q2. What is an AI Agent?

    - An AI agent is a system in which an LLM can reason/plan, use tools, access
        memory or knowledge, interact with an environment, observe results, and take
        multiple actions to accomplish a goal.`

    - A simplified agent looks like:

        User Goal
           ↓
        Agent / LLM
           ↓
        Planning
           ↓
        Tool Selection
           ↓
        Tool Execution
           ↓
        Observation
           ↓
        Next Action
           ↓
        ...
           ↓
        Final Outcome

Q3. What is Agent Evaluation?

    - Agent evaluation is the process of measuring whether an agent successfully
        achieves its goal and whether it follows an effective, reliable, efficient,
        and safe process to achieve that goal.

    Therefore, Agent Evaluation evaluates BOTH:

    1. Outcome
    2. Process / trajectory

    High-level view:

                     AGENT EVALUATION
                           |
                  +--------+--------+
                  |                 |
               OUTCOME           PROCESS
                  |                 |
            Did it achieve     How did it
            the goal?          achieve it?
                  |                 |
            Correctness        Planning
            Task success      Tool selection
            Goal completion   Tool arguments
                               Trajectory
                               Efficiency
                               Safety

Q4. What is the key difference between LLM Evaluation and Agent Evaluation?

    - LLM Evaluation primarily evaluates the model's output/capability on a task.

    Agent Evaluation evaluates both:
    1. The final outcome
    2. The sequence of actions/behavior used to achieve that outcome.

    Simple memory trick:

    LLM:
    "What did you say?"

    Agent:
    "What did you do, and did you achieve the goal?"

Q5. Why can't we simply evaluate an agent using its final answer?

    - Because the final answer does not reveal how the agent reached that answer.

    An agent could produce the correct final answer while:

    - Selecting the wrong tool initially
    - Making unnecessary tool calls
    - Using incorrect arguments and recovering later
    - Taking an inefficient trajectory
    - Spending excessive tokens
    - Increasing latency and cost
    - Violating a policy
    - Accessing unauthorized information
    - Performing unsafe actions

    Therefore:

        Final answer = Outcome evaluation
        Agent trajectory = Process evaluation
        Both may be required.

    Example:
        User: "Refund order #123."

        Agent A:

            Lookup order
                ↓
            Check refund eligibility
                ↓
            Call refund API(order_id=123)
                ↓
            Refund successful
                ↓
            "Your refund has been processed."

        Agent B:

            Lookup order
                ↓
            Call wrong API
                ↓
            Failure
                ↓
            Retry
                ↓
            Call another API
                ↓
            Retry again
                ↓
            Call refund API
                ↓
            Refund successful
                ↓
            "Your refund has been processed."

        Final answer:
                A = PASS
                B = PASS

        But process:

                A = Efficient
                B = Inefficient

        Therefore, evaluating only the final answer would hide an important
        difference between the two agents.

Q6. What is the difference between Outcome Evaluation and Process Evaluation?

        Outcome Evaluation asks: "Did the agent accomplish the goal?"

        Process Evaluation asks: "Did the agent use a correct, efficient, reliable, and safe process to
        accomplish the goal?"

Q7. What is a trajectory in Agent Evaluation?

    - A trajectory is the sequence of actions, tool calls, observations, and
        decisions made by an agent while attempting to accomplish a task.

        Example:

            User Goal
               ↓
            Agent
               ↓
            Action 1: Search customer
               ↓
            Observation
               ↓
            Action 2: Check order
               ↓
            Observation
               ↓
            Action 3: Call refund API
               ↓
            Observation
               ↓
            Final Answer

            The complete sequence is the agent's trajectory.

Q8. What is a trace?

    - A trace is a recorded execution of an agent, usually containing structured
        information about what happened during the execution.

    -A trace can contain:
        - LLM calls
        - Tool calls
        - Tool arguments
        - Tool responses
        - Retriever calls
        - Memory access
        - Latency
        - Token usage
        - Errors
        - Sub-agent calls
        - Final output

    Example:

        Trace
         |
         +-- LLM call
         |
         +-- Tool: search_customer
         |      |
         |      +-- arguments: customer_id=123
         |
         +-- Tool: get_order
         |
         +-- Tool: refund_order
         |
         +-- Final response

Q9. Trajectory vs Trace:
    - Trajectory: The sequence of actions/steps taken by the agent.

    - Trace: The recorded telemetry/log of the execution.

    - Memory trick:
        Trajectory = WHAT happened

        Trace = RECORDED evidence of what happened

Q10. What are the different levels at which an agent can be evaluated?

    - There are four useful levels:

        1. Component-level evaluation
        2. Tool-level evaluation
        3. Trajectory/process evaluation
        4. End-to-end evaluation

        Example:

                            AGENT
                              |
                +-------------+-------------+
                |             |             |
              Router         RAG          Tools
                |             |             |
              Eval           Eval          Eval
                +-------------+-------------+
                              |
                         Trajectory
                            Eval
                              |
                        End-to-End
                            Eval

Q11. What is component-level evaluation?

    - Component-level evaluation evaluates an individual component of an agent
        system rather than the complete agent.

    Examples:

        Router:
        "Did the router select the correct skill?"

        RAG:
        "Did retrieval return relevant documents?"

        Memory:
        "Did the agent retrieve the correct previous information?"

        Planner:
        "Did the planner generate an appropriate plan?"

        This is useful for diagnosing where the agent is failing.

Q12. What is tool evaluation?

    - Tool evaluation measures whether the agent correctly interacts with its
        available tools.

    We can evaluate:

    1. Tool selection
    2. Tool-call correctness
    3. Tool arguments
    4. Tool-call sequence
    5. Unnecessary tool calls
    6. Correct handling of tool responses

    Example:

    Available tools:

    search_customer()
    get_order()
    refund_order()

    User:
    "Refund order #123."

    Expected:

    get_order(order_id=123)
           ↓
    refund_order(order_id=123)

    If the agent calls:

    delete_customer(customer_id=123)

    → Tool selection failure
    → Potentially a safety failure

Q13. What is end-to-end Agent Evaluation?

    - End-to-end evaluation evaluates the agent on the complete user task rather
        than evaluating individual components separately.

    Example:

    Task:
    "Find order #123, check whether it is eligible for a refund, and process
    the refund if eligible."

    We provide the task to the complete agent.

    Then evaluate:

    - Did it complete the task?
    - Was the final result correct?
    - Did it use the correct tools?
    - Were arguments correct?
    - Was the trajectory acceptable?
    - Was the action safe?
    - How much did it cost?
    - How long did it take?

    This gives us the overall agent performance.

Q14. Why do we need both component-level and end-to-end evaluation?

    - Because they answer different questions.

        Component-level evaluation: "Which component is failing?"

        End-to-end evaluation: "Does the complete agent actually work?"

    Example:
        Router accuracy = 98%
        RAG accuracy = 95%
        Tool accuracy = 97%

        But:

        End-to-end task success = 80%

    This tells us that good individual components do not necessarily guarantee
    good overall agent performance.

    Conversely, if end-to-end performance is poor, component-level evaluations
    help us identify where the problem is.

Q15. What are the major dimensions of Agent Evaluation?

    - Agent evaluation is multidimensional.

        1. Outcome
           - Task success
           - Correctness
           - Goal completion

        2. Process
           - Planning
           - Tool selection
           - Tool arguments
           - Trajectory
           - Step efficiency

        3. Reliability
           - Failure rate
           - Retry rate
           - Recovery rate
           - Consistency

        4. Efficiency
           - Latency
           - Token usage
           - Number of steps
           - Cost

        5. Safety
           - Policy compliance
           - Unauthorized actions
           - Data leakage
           - Prompt injection resistance

        6. Robustness
           - Missing information
           - Tool failures
           - Unexpected inputs
           - Environment changes


Important Terminologies:

1. What is a benchmark?
    - A benchmark is a standardized collection of tasks/environments used to compare the performance of agents.
    - Example:
        SWE-bench → benchmark for software engineering agents.
        WebArena → benchmark for web agents.
        GAIA → benchmark for general AI assistants.


2. What is a dataset?

    - A dataset is a collection of evaluation examples/tasks used to test an agent or model.

    - Example:
        Dataset:
        Task 1 → Refund order
        Task 2 → Cancel order
        Task 3 → Update address
        Task 4 → Track shipment
3. What is a metric?
    - A metric is a quantitative measurement used to evaluate performance.
    - Examples:

        Task Success Rate
        Tool-call Accuracy
        Cost per Task
        Average Latency
        Recovery Rate

4. What is an evaluator?
    -An evaluator is the mechanism that determines whether an agent's behavior
        or output satisfies a particular evaluation criterion.

    - Examples:
        - Rule-based evaluator
        - Human evaluator
        - LLM-as-a-Judge
        - Code-based evaluator

5. What is an evaluation method?
    - An evaluation method describes HOW we determine whether the agent performed correctly.
    - Examples:
        - Exact match
        - Rule-based evaluation
        - Human evaluation
        - LLM-as-a-Judge
        - Pairwise evaluation
        - Trajectory evaluation

6. What is an evaluation framework?
    - An evaluation framework provides infrastructure for creating datasets,
        running agents, collecting traces, executing evaluators, calculating
        metrics, and comparing experiments.

    - Examples:
        - DeepEval
        - LangSmith
        - Arize Phoenix
        - Ragas
        - OpenAI Evals
        - Inspect AI

7. Final Mental Model:

                             AGENT EVALUATION
                                |
             +------------------+------------------+
             |                  |                  |
          OUTCOME             PROCESS            SYSTEM
             |                  |                  |
       Task Success          Planning           Cost
       Correctness           Tool Use           Latency
       Goal Completion       Arguments          Reliability
                             Trajectory         Scalability
                             Efficiency
                             Recovery
                                |
                                |
                              SAFETY
                                |
                    +-----------+-----------+
                    |                       |
              Policy Compliance       Robustness
              Unauthorized Actions    Prompt Injection
              Data Leakage           Tool Failures


                     EVALUATION LEVELS
                            |
          +-----------------+------------------+
          |                 |                  |
      COMPONENT          TRAJECTORY       END-TO-END
          |                 |                  |
      Router             Actions            Goal
      RAG                Tools              Outcome
      Memory             Decisions          Overall Agent
      Planner            Observations
      Tools              Steps


"""