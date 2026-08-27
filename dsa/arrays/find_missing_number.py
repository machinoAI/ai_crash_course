

nums = [0,1,2,3,4]
output = 5


def find_missing_number(nums):
    nums.sort()

    for i, num in enumerate(nums, start=0):
        if num != i:
            return i

    return len(nums)

print(find_missing_number(nums))


def find_missing_number(arr):
    n = len(arr) + 1

    xor_all = 0
    xor_arr = 0

    for i in range(1, n + 1):
        xor_all ^= i

    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr


arr = [8, 2, 4, 5, 3, 7, 1]

print(find_missing_number(arr))