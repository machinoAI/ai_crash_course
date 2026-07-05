# d(A,B) = sqrt(sum((x_i-y_i)**2)) where i = 1 to n

import math

def euclidean_distance(vec1, vec2):

    square_distance = [ (a-b)**2 for a,b in zip(vec1,vec2) ]

    return math.sqrt(sum(square_distance))


A = [1,2,3]
B = [5,6,7]
distance = euclidean_distance(A, B)
print(distance)