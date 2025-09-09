class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        dp[0] = 1
        mod = int(1e9 + 7)
        # dp[i] = dp[i - forget] + dp[i - forget + 1] ... + dp[i - delay]
        # dp[i] = sum(dp[j]) j value would be from i - forget to i - delay
        for i in range(1, n):
            for j in range(max(i - forget + 1, 0), max(i - delay + 1, 0), 1):
                dp[i] = (dp[i] + dp[j]) % mod
        return sum(dp[n - forget: n + 1]) % mod