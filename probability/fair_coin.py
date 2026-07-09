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

   HH, TT
   HT, TH

 Now, count of HH = 1
 so probability of you wining the game is = 1/4
 even your friend has same probability of winning the game as TH counts only 1 out of four sets.


"""