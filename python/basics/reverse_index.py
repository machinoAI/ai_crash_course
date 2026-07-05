
def reverse_index(nums, index):

    if index < 0 and index >len(nums):
        return nums

    return nums[:index]+nums[index:][::-1]



print(reverse_index([1,2,3,4,5,6], 3))