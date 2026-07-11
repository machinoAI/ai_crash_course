from sympy import false

Input = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
target = 8

Output: True


def search_in_matrix(nums, target):


    for item in nums:
        for num in item:

            if num == target:
                return True

    return False

print(search_in_matrix(Input, target))