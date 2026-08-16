"""
1. How do you create a tree in decision tree ?

    - A decision tree is built recursively.
    - At each node, we evaluate candidate splits across features and thresholds.
    - For classification, we calculate an impurity measure such as Gini or entropy before and after each split.
    - We then choose the feature and threshold that produces the largest reduction in weighted impurity, i.e. the highest information gain.
    - We recursively repeat this process on the child nodes until a stopping criterion such as maximum depth or minimum samples is reached.

            At every node:
                1. Look at available features
                        ↓
                2. Try candidate thresholds
                        ↓
                3. Calculate child impurity
                        ↓
                4. Calculate impurity reduction / information gain
                        ↓
                5. Choose BEST feature + threshold
                        ↓
                6. Split the data
                        ↓
                7. Repeat for each child

    - Example:

            | Lead | Webinar Count | Duration % | Converted |
            | ---- | ------------: | ---------: | --------: |
            | A    |             1 |         20 |         0 |
            | B    |             1 |         60 |         0 |
            | C    |             2 |         40 |         0 |
            | D    |             2 |         90 |         0 |
            | E    |             3 |         50 |         1 |
            | F    |             3 |         80 |         1 |
            | G    |             4 |         30 |         0 |
            | H    |             4 |         70 |         1 |
            | I    |            5+ |         60 |         1 |
            | J    |            5+ |         90 |         1 |

        We want the tree to predict: Target=Converted∈{0,1}

        Step 1: Start with one root
            Initially, all 10 leads are in one node.
                             ROOT
                        [10 leads: 6 No, 4 Yes]

            Gini = 1−(P0^2+P1^2)
                = 1−(0.6^2+0.4^2)
                = 0.48

            So the root has impurity 0.48.

        Step 2: What can the tree split on?
            We have two features:
                Webinar Count
                Duration %

        - The tree asks, "Which feature + threshold gives me the cleanest separation between converted and non-converted leads?"

        Step 3: Try Webinar Count
            Possible values: 1, 2, 3, 4, 5+
            The tree can try thresholds such as:
                Webinar ≤ 1.5
                Webinar ≤ 2.5
                Webinar ≤ 3.5
                Webinar ≤ 4.5

        Split: Webinar ≤ 2.5
        Left: A B C D
            Targets: 0 0 0 0

            Gini_left=0

        Right: E F G H I J
        Targets: 1 1 0 1 1 1

        = 5 Yes and 1 No

        So,
            Gini_right =1−(5/6)^2 −(1/6)^2
                    =0.278

        Step 4: Calculate weighted impurity
                Weighted Gini= 4/10(0) +6/10(0.278) = 0.167

        So the impurity reduction is:
            Gain=0.48−0.167 = 0.313

        Step 5: But the tree doesn't stop there
            "What if I split using Duration instead?
            For example:
                Duration ≤ 45%
                The tree calculates the resulting child Ginis and information gain.

                             Candidate splits
                                       ↓
                           ┌───────────┴───────────┐
                           ↓                       ↓
                     Webinar ≤ 2.5          Duration ≤ 45
                     Gain = 0.313            Gain = 0.214


        *** The tree chooses:
            Webinar Count ≤ 2.5
            because it gives the largest impurity reduction.


        Step 6: Now we have our first branch
                    Webinar ≤ 2.5?
                    /            \
                  YES             NO
                  /                \
             A B C D             E F G H I J
             0 0 0 0             1 1 0 1 1 1

        The left node is pure: No conversion
        But the right node isn't pure:

        Step 7: Split the right node again
                    Webinar ≤ 2.5?
                    /            \
                  YES             NO
                  /                \
              Predict 0       Duration ≤ 60?
                              /            \
                            ...            ...

"""