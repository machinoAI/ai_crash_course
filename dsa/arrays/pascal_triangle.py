"""
Input: N = 5, r = 5, c = 3
Output: Element at position (r, c): 6
N-th row of Pascal’s triangle: 1 4 6 4 1
First n rows of Pascal’s triangle:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
Explanation: Pascal triangle for first 5 rows is shown above.
Input: N = 1, r = 1, c = 1
Output: Element at position (r, c): 1
N-th row of Pascal’s triangle: 1
First n rows of Pascal’s triangle:
1
Explanation: N = 1 is the base case fof a pascal's triangle.

"""

def generate(n):

    triangle = []

    for i in range(n):
        row = [1] * (i+1)

        for j in range(1, i):
            row[j] = triangle[i-1][j-1]+triangle[i-1][j]


        triangle.append(row)

    return  triangle


list1 = generate(5)
for item in list1:
    print(item)