"""
AI Evaluation Metrics: Put into four buckets

1. Task Success :
  - Goal Completion metrics:    Which tells actually the agents were able to complete the objectives or not (Binary)?
  - Progress Rate:              How far did agent move towards the goal: Agent failing at 2nd step is different-than  failing at 9th step.

2. Technical metrics:
  - Tool correctness:           How exactly agent was able to predict the tool.
  - Tool argument accuracy:     How many parameters were correct including their values.
  - LLM-as-judge: Agent comes with an answer instead of tool call. Such cases need to compute answer correctness using semantic similarity and LLM-as judge.
  - Measure the reasoning quality:  by measuring the plan quality and plan adherence.

2.1 Tool Metrics:
    - Tool accuracy
    - Tool latency
    - Tool failures
    - Retry count
2.2 Trajectory Evaluation
    Evaluate:
        - Thoughts ->> Actions -->> Evaluations

    Questions:
        - Was the plan optimal
        - Were tools correct
        - Were retries necessary ?
3. Productions Metrics:
    Track:
        - Success Rate
        - Cost per task
        - Average latency
        - Token Usage
        - Human intervention rate
4. Business Metrics:
    - Ticket resolution time
    - Customer Satisfaction
    - Developer Productivity
    - Revenue impact





"""