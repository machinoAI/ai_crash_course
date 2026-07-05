# Q3. Find the second largest element in one traversal without sorting.


nums = [41, 90, 11, 40, 98, 55, 89, 39]

largest=float("-inf")
second=float("-inf")

for ele in nums:
    if ele > largest:
        second=largest
        largest=ele
    elif largest>ele>second:
        second=ele

print("Largest:", largest)
print("Second Largest:", second)