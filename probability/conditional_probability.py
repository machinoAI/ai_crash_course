"""
A bag contains red and blue balls. Draw two balls without replacement. Compute conditional probabilities.
Explanation:
    - With replacement: After drawing the first ball, you put it back into the bag before drawing the second ball.
    - With replacement: After drawing the first ball, you do not put it back.

    - Conditional probability formula:
        P(A∣B) = P(A∩B)/ P(B)


    where:
    P(A∣B): Probability of A given B has happened.
    P(A∩B): Probability that both A and B happen.
    P(B): Probability that B happens.


    Examples:
        A bag contains:

        3 red balls (R)
        2 blue balls (B)

        Two balls are drawn without replacement.

        Find:

        P(Second ball is red∣First ball is red)

        Let:

        A: Second ball is red.
        B: First ball is red.

        After drawing one red ball:

        Remaining red balls = 2
        Remaining total balls = 4

        Hence,
            P(A∣B) = 2/4 = 1/2

"""