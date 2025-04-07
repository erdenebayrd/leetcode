class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # time: O(N * M), M is sum(nums)
        # space: O(N * M), M is sum(nums)
        # method: bottom up DP
        n = len(nums)
        m = sum(nums)
        if (m // 2) * 2 != m:
            return False
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if j - nums[i - 1] >= 0:
                    dp[i][j] |= dp[i - 1][j - nums[i - 1]]
        return dp[n][m // 2]