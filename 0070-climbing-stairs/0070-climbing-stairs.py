class Solution:
    def climbStairs(self, n: int) -> int:
        # time: O(N)
        # space: O(N)
        if n <= 1:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for stair in range(2, n):
            dp[stair] = dp[stair - 1] + dp[stair - 2]
        return dp[n - 1]