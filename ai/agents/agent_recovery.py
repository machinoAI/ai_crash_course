"""
1. What are different types of failures of AI Agents on production ?
    - Prompt issues
    - Tools issues
    - Model Issues
    - Planning issues

2. How do agents recover from failures ?
    Production systems fails all the time:
        - Tool timeout
        - Hallucination
        - API failure
        - Rate limits
        - Invalid output

    - Retry Strategy
        Try 1 ->> fail ->> Retry with backoff ->> fail ->> Fallback-->> Human

    Common Techniques:
        - Exponential Backoff
        - Checkpointing
                {
                    "step": 5,
                    "state": ...
                }
            resumes from step 5.

        - Fallback Model
             Claude ->> fail -->> GPT->> fail-->> Gemini
        - Human Escalation:
            Confidence < threshold


3. What are the different types of memory ?
- There are three types of memory in context:
    - Episodic Memory:
        What happen previously ?

    - Semantic Memory:
        What facts do I know ?

    - Procedural Memory:
        How should I act ?


4. How do agents decide the next action?
    - Rule-based routing
    - LLM planning
        - Available tools:
            1. Search
            2. SQL
            3. Calculator
            Choose next action.
            LLM decides.

    - ReAct pattern
        Thought:
        Need customer information.

        Action:
        Query database.

        Observation:
        Customer premium.

        Thought:
        Offer premium support.

    - Planning approaches

5. How do you prevent infinite loops?
    - Maximum iteration limit
    - Duplicate action detection
        - prevent: Search() ->>  Search() -->>  Search()-->>  Search()
    - Cost budget:
        max_tokens = 50000
    - Time budget
        max_time = 30 seconds
    - Confidence threshold
        confidence < 0.6
    - 

"""