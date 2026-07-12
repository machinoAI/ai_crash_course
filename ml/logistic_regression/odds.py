"""
What is odds?
- How many times event expected to happen compared to not happen.
- Odds = p/ 1-p
- Example: Suppose India has 80% chance of wining the cricket world cup.
 p = 0.8
 Then odds = 0.8/1-0.8 = 4 Means , India is 4 times more likely to win than lose.


Why Logistic regression uses odds instead of directly probability ?
    - Probability is limited from 0 <=p <= 1
    - odds range from 0 → ∞
    - And log-odds: log(p/1-p)  ranges from −∞ → +∞

- Probability answers: "What is the chance of winning?"
- Odds answer: "How many times is winning more likely than losing?

"""