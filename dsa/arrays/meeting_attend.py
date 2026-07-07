
"""
You need to check whether a person able to attend all the scheduled meetings.
"""

intervals = [
    [7, 10],
    [2, 4],
    [4, 5]
]


def can_attend_meetings(intervals):
    intervals.sort(key = lambda x:x[0])
    print(intervals)

    for i in range(1, len(intervals)):
        prev = intervals[i-1]
        current = intervals[i]

        if current[0] < prev[1] :
            return False

    return True


print(can_attend_meetings(intervals))
