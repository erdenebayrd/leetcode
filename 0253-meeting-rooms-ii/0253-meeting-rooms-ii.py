class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # time: O(N * Log N)
        # space: O(N)
        intervals.sort()
        _, ed = intervals[0]
        freeRooms = [ed]
        heapq.heapify(freeRooms)
        res = 1
        for i in range(1, len(intervals)):
            st, ed = intervals[i]
            if freeRooms[0] <= st:
                heapq.heappop(freeRooms)
            heapq.heappush(freeRooms, ed)
            res = max(res, len(freeRooms))
        return res