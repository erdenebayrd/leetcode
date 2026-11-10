class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        inf = float('inf')
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = min(dp[i], dp[i - 1] + 1 + costs[i - 1])
            if i - 2 >= 0:
                dp[i] = min(dp[i], dp[i - 2] + 4 + costs[i - 1])
            if i - 3 >= 0:
                dp[i] = min(dp[i], dp[i - 3] + 9 + costs[i - 1])

        return dp[n]
            