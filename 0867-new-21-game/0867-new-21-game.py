class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1): # to i'th point
            le = max(0, i - maxPts)
            ri = min(i - 1, k - 1)
            # print(le, ri)
            if le > ri:
                break
            if le == 0:
                dp[i] += dp[ri] / maxPts
            else:
                dp[i] += (dp[ri] - dp[le - 1]) / maxPts
            dp[i] += dp[i - 1]
        return dp[n] - dp[k - 1]