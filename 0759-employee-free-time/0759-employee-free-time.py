from collections import defaultdict

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # time: O(N log N)
        # space: O(N)
        # method: dict
        schedules = defaultdict(int)
        for interval in schedule:
            for obj in interval:
                schedules[obj.start] += 1
                schedules[obj.end] -= 1
        intervals = []
        for key in schedules:
            value = schedules[key]
            intervals.append([key, value])
        intervals.sort()
        for i in range(1, len(intervals)):
            intervals[i][1] += intervals[i - 1][1]
        result = []
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] == 0:
                start = intervals[i - 1][0]
                end = intervals[i][0]
                result.append(Interval(start, end))
        return result