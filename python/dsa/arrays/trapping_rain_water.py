
"""
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
output = 6

"""

def rain_water_trapping(heights):
    water = 0

    for i, num in enumerate(heights):

        max_left = max(heights[:i + 1])
        max_right = max(heights[i:])

        water += min(max_left,max_right) - heights[i]

    return water



heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rain_water_trapping(heights))



# Optimization:

def rain_water_trapping(heights):
    water = 0
    left=0
    right= len(heights)-1

    left_max=0
    right_max=0

    while left < right :

        if heights[left] < heights[right]:

            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water +=left_max-heights[left]
            left +=1

        else:
            if heights[right]>= right_max:
                right_max=heights[right]
            else:
                water +=right_max-heights[right]
            right -=1

    return water

print("Optimized: ",rain_water_trapping(heights))