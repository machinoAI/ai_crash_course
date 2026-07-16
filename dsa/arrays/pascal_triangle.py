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
            row[j] = triangle[i-1][j-1]+triangle[i-1][j]  # Current element = upper-left + upper-right


        triangle.append(row)

    return  triangle


# list1 = generate(5)
# print(list1)
# for item in list1:
#     print(item)


# Optimised : Time complexity: O(min(c,r−c)) and space complexity:O(1)
"""
Pascal Triangle row n  ↔  coefficients of (a+b)^n
nCr = n! / (r!(n-r)!) 
Element=(n−1)C(r−1) = (n-1)! / (n-1)!(n-r)!
"""

def find_pascal_element(n,r):

    m = n-1
    n = r-1
    result =1

    for i in range(n):
        result *=(m-i)
        result //=(i+1)

    return result

print(find_pascal_element(5,5))


def generate_pascal_triangle(n):

    triangle = []

    for row in range(1, n + 1):

        current_row = []

        for col in range(1, row + 1):
            current_row.append(
                find_pascal_element(row, col)
            )

        triangle.append(current_row)

    return triangle


triangle = generate_pascal_triangle(5)

for row in triangle:
    print(row)