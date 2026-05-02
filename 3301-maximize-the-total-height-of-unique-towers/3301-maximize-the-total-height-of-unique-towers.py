import heapq 

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: max heap

        lastTaken = float('inf')
        arr = [-height for height in maximumHeight]
        heapq.heapify(arr)
        result = 0
        while arr:
            height = -arr[0]
            if lastTaken <= height:
                height = lastTaken - 1
                if height <= 0:
                    return -1
            result += height
            lastTaken = height
            heapq.heappop(arr)
        return result