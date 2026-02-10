class Solution:
    def maxA(self, n: int) -> int:
        # time: O(N)
        # space: O(N)
        dp = [countA + 1 for countA in range(n)]
        for i in range(1, n):
            dp[i] = max(dp[i], dp[i - 1] + 1)
            for j in range(3, 7):
                if i - j < 0:
                    continue
                dp[i] = max(dp[i], dp[i - j] * (j - 1))
            # dp[i] = max(, dp[i - 3] * 2, dp[i - 4] * 3 + dp[i - 5] * 4 + dp[i - 6] * 5)
        return dp[n - 1]