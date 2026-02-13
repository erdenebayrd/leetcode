import heapq

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # time: O(N Log N)
        # space: O(N)
        n = len(nums)
        minValueWithIndex = []
        heapq.heappush(minValueWithIndex, [0, -1])
        result = float('inf')
        cumulativeSum = 0
        for i in range(n):
            cumulativeSum += nums[i]
            while minValueWithIndex and cumulativeSum - minValueWithIndex[0][0] >= k:
                _, index = heapq.heappop(minValueWithIndex)
                result = min(result, i - index)
            heapq.heappush(minValueWithIndex, [cumulativeSum, i])

        if result == float('inf'):
            result = -1
        return result