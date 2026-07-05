
nums = [2,7,11,15,5,4]
target = 9


def sum_target(nums, target):

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target==(nums[i]+nums[j]):
                return i,j



print( sum_target(nums, target))