

nums = [0,1,2,3,4]
output = 5


def find_missing_number(nums):
    nums.sort()

    for i, num in enumerate(nums):
        if num != i:
            return i

    return len(nums)

print(find_missing_number(nums))
