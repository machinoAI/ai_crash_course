"""
You are given an integer array height of length n.

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that, together with the x-axis, form a container that holds the maximum amount of water.

Return the maximum amount of water the container can store.

width = right_index - left_index
height = min(height[left_index], height[right_index])
area = width * height

"""

height = [1,8,6,2,5,4,8,3,7]

# output: 49

# Brute force: O(n) & O(1)
def most_water_container(height):
    max_area =0

    for i in range(len(height)):
        for j in range(i+1, len(height)):
            width = j - i
            min_height=min(height[i], height[j])
            area = width*min_height
            if area>max_area:
                max_area=area
    return  max_area


print("Max Area: ", most_water_container(height))


# Optimized solution:
height = [1,8,6,2,5,4,8,3,7]

def most_water_container(height):
    left = 0
    right = len(height)-1
    max_area= 0

    while left < right:
        width = right-left
        min_height = min(height[left], height[right])
        area = width * min_height

        max_area = max(max_area, area)

        if height[left] < height[right]:
            left +=1
        else:
            right -=1

    return  max_area

print("Optimised solution- Max Area: ", most_water_container(height))