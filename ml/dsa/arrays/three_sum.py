"""
Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:

i != j
i != k
j != k

and

nums[i] + nums[j] + nums[k] = 0

The solution set must not contain duplicate triplets.

"""
#Brute force:

def three_sum(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if (nums[i]+ nums[j] +nums[k])==target:
                    return i,j,k


nums=[1,2,3,4,5,6,7,8,9]
target=12
print("Three sum:", three_sum(nums, target))


# Optimised:

def three_sum(nums, target):
    results =[]

    for i in range(len(nums)):
        seen = {}

        for j in range(i+1, len(nums)):
            temp = target - (nums[i]+nums[j])

            if temp in seen and i!=j:

                results.append((i, seen[temp], j))

                # return i,seen[temp], j
            else:
                seen[nums[j]]= j
    return results

nums=[1,2,3,4,5,6,7,8,9]
target=12
print("Three sum optimized:", three_sum(nums, target))