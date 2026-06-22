# Q2: Rotate an array to the right by k positions in-place.

#Example:
"""
    nums = [10,20,30,40,50,60]
    k = 2
    output: [40,50,10,20,30]

"""

nums=eval(input("Enter an array:"))
k =int(input("Enter an position number:"))

def rotate_array(nums):

    return nums[k+1:]+nums[0:k+1]

print("Entered array:", nums)
print("Given position:", k)
print(f"Rotated Array by {k}th position: {rotate_array(nums)}")