#Q4. Given an array, find the smallest missing positive integer in O(n) time and O(1) extra space.


nums1=[7, 8, 9, 11, 12] #output= 1     Smallest positive integer 1 is missing.
nums2=[3, 4, -1, 1]     #output= 2     Smallest positive integer 1 is missing.
nums3=[1, 2, 0]         #output= 3     Smallest positive integer 1 is missing.
nums4=[3, 4, -1, 1]     #output= 2    Smallest positive integer 1 is missing.

# time: n(log n)
# space: O(1) #ignoring Python sort's auxiliary space


def smallest_missing_positive(nums):
   smallest = 1
   nums.sort()

   for num in nums:
       if num==smallest:
           smallest+=1

   return smallest


print(smallest_missing_positive(nums4))


# Method 2: Optimal solution:

def smallest_missing_positive(nums):

    n = len(nums)

    i = 0

    while i < n:

        correct = nums[i] - 1

        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


nums = [3, 4, -1, 1] # Swap the element position based on index ; after processing: [1,-1,3,4] Answer : 2 is missing

print(smallest_missing_positive(nums))