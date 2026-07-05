# cosine similarity = (A.B)/ ||A|| X ||B||
# WHere ||A|| = sqrt(sum(a**2)) in A  and similarly ||B|| = sqrt(sum(b**2)) in B


import math

def cosine_similarity(vec1, vec2):

    dot_product = sum(a*b for a, b in zip(vec1, vec2))
    magnitude_vec1 = math.sqrt(sum(a**2 for a in vec1))
    magnitude_vec2 = math.sqrt(sum(b**2 for b in vec2))

    cosine_sim = dot_product/(magnitude_vec1* magnitude_vec2)
    return  cosine_sim

x = [1,2,3]
y = [5,6,7]

cosine_sim = cosine_similarity(x,y)
print(cosine_sim)

# Numpy:

import numpy as np

def cosine_similarity(vec1, vec2):

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )

cosine_similarity(x,y)
print("Using Numpy:", cosine_sim)