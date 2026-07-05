

def find_duplicate(nums):
    seen = set()
    duplicate = set()

    for item in nums:
        if item in seen:
            duplicate.add(item)
        else:
            seen.add(item)
    return duplicate

print(find_duplicate([1,2,3,2,4,5,6,4,2,6,7]))