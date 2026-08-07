"""
1. What is Softmax?
    - Softmax converts raw logits into a probability distribution by exponentiating
        each logit and normalizing by the sum of all exponentiated logits.

    Softmax for token i is:
        P_i = e^zi/∑ e^zi j=1 to V

        Where:
            - zi = logit of token i
            - V = vocabulary size

    Example:
            P(cat)= e^8/(e^8 + e^4 + e^1 + e^−2)

2. Why exponential ?

    - Always positive: e^x >0
    - Preserves ordering: 8>4>1>-2 ->>  e⁸>e⁴>e¹>e⁻² =>>> Ranking doesn't change.
    - Magnifies confidence.

3. Why subtract the maximum logit?
    - To prevent numerical overflow while producing exactly the same probability distribution.


"""