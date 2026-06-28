"""
You are given an array of intervals where:

intervals[i] = [start, end]

Merge all overlapping intervals and return a new array containing only the merged intervals.
"""

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,10],[2,6]]
#Output: [[1,6],[8,10],[15,18]]

def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for start, end in intervals:
        if start <= merged[-1][1]:
            merged[-1][1]= max( merged[-1][1], end)
        else:
            merged.append([start,end])

    return merged


print(merge_intervals(intervals))