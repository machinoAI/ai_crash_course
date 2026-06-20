# Find second largest item of a given list

nums = [41, 90, 11, 40, 98, 55, 89, 39]
# Method:1
nums.sort()

print("Sorted List:", nums)
print("Second Largest element:", nums[-2])


# Method 2:

max_num = nums[0]
sec_max_num = 0
for ele in nums:
    if ele > max_num:
        max_num = ele

print("Largest element: ",max_num)
for i in range(len(nums)):
    if nums[i] > sec_max_num and (nums[i] != max_num):
        sec_max_num = nums[i]

print("Second Largest element:",sec_max_num)