from functools import cache

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # time: O(N ^ 2)
        # space: O(N)
        # method: DP
        
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for j in range(n):
            for i in range(j):
                # i -> j
                if -target <= nums[j] - nums[i] <= target and dp[i] > 0:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        result = dp[n - 1] - 1
        return result