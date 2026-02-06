import bisect

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # time: O(N * Log N)
        # space: O(1)
        # method: binary search + dp
        nums.sort()
        result = float('inf')
        n = len(nums)
        for i in range(n):
            maxLimit = k * nums[i]
            index = bisect.bisect_right(nums, maxLimit)
            currentCost = i
            if index < n:
                currentCost += n - index
            result = min(result, currentCost)
        return result