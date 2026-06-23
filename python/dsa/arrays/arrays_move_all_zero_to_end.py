#Q1: Move all zeros to the end while preserving the order of non-zero elements.

nums = [0,2,6,0,7,1,0]

# output = [2,6,7,1,0,0,0]


def move_zero_end(nums):
    for ele in nums:
        if ele==0:
            nums.remove(ele)
            nums.append(ele)
    return nums


print(move_zero_end(nums))
