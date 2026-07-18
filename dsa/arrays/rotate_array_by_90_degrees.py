"""
Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.
The rotation must be done in place, meaning the input 2D matrix must be modified directly.
Input :matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Details: https://takeuforward.org/data-structure/rotate-image-by-90-degree

"""
# Brute force:

def rotate_array(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    rotated = [[0]*rows for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            rotated[j][rows-1-i] = matrix[i][j]

    return  rotated


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(rotate_array(matrix))


# Optimised: Transpose and reverse: Reduce the space complexity from O(n^2) to O(1)

def rotate_array(matrix):

    #Transpose the matrix:

    n =len(matrix)

    for i in range(n):
        for j in range(i+1, n):
             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        matrix[i].reverse()


    return  matrix

    # Reverse the transposed Matrix:



print(rotate_array(matrix))
