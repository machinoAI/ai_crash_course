nums1 = [1,2,3,4,5]
nums2 = [2,3,4,4,5]

output = [1,2,3,4,5]

def find_union(nums1, nums2):
    seen = set()

    for num in nums1:
        if num not in seen:
            seen.add(num)

    for num in nums2:
        if num not in seen:
            seen.add(num)

    return list(seen)


print(find_union(nums1, nums2))

def find_union(nums1, nums2):

    return list(set(nums1)|set(nums2))

print(find_union(nums1, nums2))