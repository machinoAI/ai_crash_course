"""
1. why agent evals?

- LLM responses are non-deterministic sometimes it works as expected sometimes it's not.
- We can't guarantee how the agent will behave in wild without measuring it at scale.
- Evals allows us to understand and improve how the models behave in the real world by defining what is good looks like.
- To build evals that actually scale they must be strict and measurable.


2. How to start with evals ?

- Intuition based evals can be good even if it is non-scalable
- Prompt tweaks can have large performance gains.
- Learns the failure patterns and hillclimb in a targeted way.
- Start early and small. Test the negatives.

3. How to do evals ?
- Clear rubric template with trusted examples.
- Human-human agreement should be strong.
- Get explanations along with verdict.
- Categorical input - pass/fail
- Multiple output:
    - Is it accurate?
    - Is it safe ?
- Explanations can be used to make the agents better.

4. Do you trust the LLM-judge ?

- Monitor disagreements: Where does the llm disagree with human?
- Go beyond pass/fail alignment: spot check reasoning etc.
- High quality expert labels: Reliable golden truth with expert labels to establish baseline.

Example:
    prompt: For the legal reasons, disclaimer can never be removed
    - Initial trace ( I can see the disclaimer)-->> Disclaimer
    - Output trace: I am going to remove disclaimer


- If you want to know what's wrong , look it its thinking.
    - Did it see the disclaimer ?
        - Yes
    - Did it understand the disclaimer ?
        - Yes
    - Did it follow the rule ?
        - No; it went rogue.

- Avoid Overfitting:
    - Agent fails to generalize : Optimizing for a narrow datasets can lead to failure on the edge cases /
        broader capabilities.

    - Maintain a strict hold -out (test) set: Use the test set sparingly and refresh it with production data.

5. Launch Readiness:
    - Understand regression
    - Focus on patterns vs isolated runs
    - Invest in online evals
6. What makes a good eval system ?
    - Representative of what would -- You want your product would be good at
        Ex: what user journeys to support and their breakdown by frequency
    - Important to kep this-- Evolving /learning from new user usage patterns
    - Build an -- expert - audited high quality golden set with edge cases.
    - Invest in -- comprehensive rather templates/rubric with clear examples with a broad set of cases.
    - Choose the right metrics for the launch readiness: P/R - Semantics scores


"""