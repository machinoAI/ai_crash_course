
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



# Op