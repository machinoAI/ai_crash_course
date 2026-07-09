"""
If you roll a die three times, what is the probability of getting two consecutive threes?

Explanation:
    A die has six sides = 6
    dice counts = 3

    Sets = power(6,3) = 216

    probability of getting All threes (3,3,3)=  1/6*1/6*1/6 = 1/216
    probability of getting two threes (X,3,3), (3,3,X), (3,X,3)= 3/216

    but (3,X,3) , 3's are not in consecutive so consider only (X,3,3), (3,3,X) = (1/6*1/6 )+(1/6*1/6 )= 2/36

    so probability = 1/216-2/36 = 12-1/216 = 11/216


"""

