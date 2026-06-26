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

def most_water_container(height):
    max_area =0

    for i in range(len(height)):
        for j in range(i, len(height)):
            width = j - i
            min_height=min(height[i], height[j])
            area = width*min_height
            if area>max_area:
                max_area=area
    return  max_area


print(most_water_container(height))
