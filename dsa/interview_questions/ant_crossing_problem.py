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
def ants_crossing(r1, r2, group1, group2, t):
    g1_reversed = group1[::-1]

    r1 = list(range(r1))
    r2 = list(range(r1[-1] + 1, r1[-1] + 1 + len(group2)))

    # Update positions for both groups after t seconds
    g1_moved = [(pos + t, name) for pos, name in zip(r1, g1_reversed)]
    g2_moved = [(pos - t, name) for pos, name in zip(r2, group2)]

    # Combine both groups and sort left-to-right by position
    all_ants = sorted(g1_moved + g2_moved, key=lambda x: x[0])

    #Extract and return the final string
    return "".join(name for pos, name in all_ants)



r1 = 3
r2 = 3

group1 = "CDE"
group2 = "FGH"
t = 1

print(ants_crossing(r1, r2, group1, group2, t))