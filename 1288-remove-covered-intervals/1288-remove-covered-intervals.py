class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: sorting
        intervals.sort(key=lambda x: (x[0], -x[1])) # sorting intervals by "left" value
        n = len(intervals)
        count = n
        current_max_right = 0
        for i in range(n):
            _, right = intervals[i]
            if right <= current_max_right:
                count -= 1
                continue
            current_max_right = max(current_max_right, right)
        return count