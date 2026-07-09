"""
Q1: You and your friend are playing a game with a fair coin. The two of you will continue to toss the coin until
the sequence HH or TH shows up. If HH shows up first, you win, and if TH shows up first your friend wins.
 What is the probability of you winning the game?

 Explanations:

 A fair coin has two side = 2
 How many coins (two friend) = 2

   =  power(number of sides, number of coins)
   = power(2,2) = 4
   or

   HH,
   TT
   HT,
   TH

case1: When first toss is H (1/2)-> Only 50% chances that the next toss would also be H = 1/2*1/2 = 1/4 (only scenario you win)
When next toss is T = you lost the game. or your friend win = (1/2*1/2) = 1/4

case 2: When first toss is T -> you lost the game doesn't matter. TH or TT (1/2)

 so 1/4+1/2 = 3/4 = 75% chances that your friend win but only 25% you may win.


"""


