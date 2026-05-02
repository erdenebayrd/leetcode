import heapq 

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: sorting

        maximumHeight.sort() # this requires O(N) spaces in builtin sort function
        n = len(maximumHeight)
        lastTaken = float('inf')
        result = 0
        for i in range(n - 1, -1, -1):
            height = maximumHeight[i]
            if lastTaken <= height:
                height = lastTaken - 1
            if height <= 0:
                return -1
            result += height
            lastTaken = height
        return result