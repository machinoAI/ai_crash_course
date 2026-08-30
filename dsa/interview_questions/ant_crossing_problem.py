"""
You have two groups of ants on a pole/string:

    R1 = number of ants in the first group
    R2 = number of ants in the second group
    group1 = characters representing ants in group 1
    group2 = characters representing ants in group 2
    T = amount of time

The two groups move in opposite directions. When ants from the two groups meet, they cross each other, changing their relative order.

You need to determine the order of all ants after T seconds.

Example:

    R1 = 3
    R2 = 3

    Group 1 = CDE
    Group 2 = FGH

    T = 1

Expected output: EDFCGH

"""
"""
Pattern: Two ordered groups move toward each other, and when members meet, their relative positions are exchanged.


"""