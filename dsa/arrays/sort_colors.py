"""
You are given an array containing only:

0 → Red
1 → White
2 → Blue

Sort the array in-place so that all 0s come first, then all 1s, then all 2s.

You must not use Python's built-in sort().

"""
colors = [2,0,2,1,1,0]

# Output: [0,0,1,1,2,2]
# Dutch National Flag Algorithm.

# BruteForce:

def sort_colors(colors):
    zeros_count = 0
    ones_count = 0
    twos_count = 0

    for color in colors:
        if color == 0 :
            zeros_count +=1
        elif color == 1:
            ones_count +=1
        else:
            twos_count +=1

    for zero in range(0, zeros_count):
        colors[zero] = 0


    for one in range(zeros_count, zeros_count+ones_count):
        colors[one] = 1

    for two in range(zeros_count+ones_count,  zeros_count+ones_count+twos_count):
        colors[two] = 2

    return colors


colors = [2,0,2,1,1,0]
print(sort_colors(colors))

# Dutch National Flag algorithm: Optimal solutions:

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]  # swap 0 to first range element ( 0th to low-1)
            low += 1      # An element has increased in first range so low will increase.
            mid += 1      # An element has reduced so moving to next element

        elif nums[mid] == 1:   # 2nd range: low to mid -1
            mid += 1            # nothing required to do as it is already with 1s. so moving to the next element

        else:
            nums[mid], nums[high] = nums[high], nums[mid] # 3rd range( high+1 to n-1) Swap 2 with high position
            high -= 1   # since a new element added to 3rd range , high will increase by 1.

    return nums

# colors = [2,0,2,1,1,0]
# print(sort_colors(colors))