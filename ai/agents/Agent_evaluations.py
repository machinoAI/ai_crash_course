"""
AI Evaluation Metrics: Put into two buckets

1. Business Metrics: Most import for PMs , CIOs.
  - Goal Completion metrics:    Which tells actually the agents were able to complete the objectives or not (Binary)?
  - Progress Rate:              How fard did agent move towards the goal: Agent failing at 2nd step is different than 9th step.

2. Technical metrics:
  - Tool correctness:           How exactly agent was able to predict the tool.
  - Tool argument accuracy:     How many parameters were correct including their values.
  - LLM-as-judge: Agent comes with an answer instead of tool call. Such cases need to compute answer correctness using semantic similarity and LLM-as judge.
  - Measure the reasoning quality:  by measuring the plan quality and plan adherence.

"""