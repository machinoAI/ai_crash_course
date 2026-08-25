"""
Sort the given list
nums = [8,3,55,33,1,99,833,0,-1]
output=[-1,0,1,3,8,33,55,99,833]
"""


# Bubble sort: Repeatedly compare adjacent elements and swap them if they are in the wrong order.
# TC: O(n^2)
# SC: O(1)

def sort_numbers(nums):

    n = len(nums)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):

            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                swapped = True
                # print(i,j)

        if not swapped:
            break

    return nums

nums = [-8,3,55,33,1,99,833,0,-1]
# nums = [1,2,3]
print("Bubble Sort: ", sort_numbers(nums))

# Selection sort: Find the minimum element from the unsorted portion and put it at the beginning.
# TC: O(n^2)
# SC: O(1)


def sort_numbers(nums):

    n = len(nums)

    for i in range(n):

        min_idx = i

        for j in range(i+1, n):

            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx],  nums[i]


    return nums


print("Selection Sort: ", sort_numbers(nums))

# Merge sort: Keep dividing the array into smaller halves until each piece has one element, then merge those pieces back in sorted order.
# TC: O(n log n)
# SC: O(n)


def merge_sort(nums):

    if len(nums) == 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i +=1

        else:
            result.append(right[j])
            j +=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print("Merge Sort: ", merge_sort(nums))


# Heap sort: Build a Max Heap → repeatedly remove the maximum → put it at the end.
# TC: O(n log n)
# SC: O(1)

def heap_sort(nums):
    n = len(nums)

    # Heapify subtree rooted at i
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[left] > nums[largest]:
            largest = left

        if right < n and nums[right] > nums[largest]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(n, largest)

    # 1. Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # 2. Move maximum to the end
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]

        # 3. Restore Max Heap
        heapify(i, 0)

    return nums

print("Heap Sort: ", heap_sort(nums))



# Quick sort: Choose a pivot → partition the array around the pivot → recursively sort the left and right parts.
# TC: O(n^2)
# SC: O(n)

def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]

    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)