import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # time: O(N log N) for sorting and min heap
        # space: O(N) using a heap
        # method: heap
        intervals.sort()
        result = 0
        running = []
        for start, end in intervals:
            while running and running[0] <= start:
                heapq.heappop(running)
            heapq.heappush(running, end)
            result = max(result, len(running))
        return result