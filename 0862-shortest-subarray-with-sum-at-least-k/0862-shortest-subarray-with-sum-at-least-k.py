from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(N)
        n = len(nums)
        cumulativeSum = 0
        monotonicIncreasingWithIndex = deque()
        result = float('inf')
        for i in range(n):
            cumulativeSum += nums[i]
            if cumulativeSum >= k:
                result = min(result, i + 1)
            
            while monotonicIncreasingWithIndex and cumulativeSum - monotonicIncreasingWithIndex[0][0] >= k:
                _, index = monotonicIncreasingWithIndex.popleft()
                result = min(result, i - index)

            while monotonicIncreasingWithIndex and monotonicIncreasingWithIndex[-1][0] >= cumulativeSum:
                monotonicIncreasingWithIndex.pop()
            
            monotonicIncreasingWithIndex.append([cumulativeSum, i])
        
        if result == float('inf'):
            result = -1
        return result