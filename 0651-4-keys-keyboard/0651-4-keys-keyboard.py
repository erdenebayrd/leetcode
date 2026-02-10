class Solution:
    def maxA(self, n: int) -> int:
        dp = [countA + 1 for countA in range(n)]
        for i in range(1, n):
            dp[i] = max(dp[i], dp[i - 1] + 1)
            for j in range(i - 6, i - 2):
                if j > 0:
                    dp[i] = max(dp[i], dp[j] * (i - j - 1))
            # dp[i] = max(dp[i - 3] * 2, dp[i - 4] * 3 + dp[i - 5] * 4 + dp[i - 6] * 5)
        return dp[n - 1]