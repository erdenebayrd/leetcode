class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        n = len(rides)
        dp = [0] * (n + 1)
        rides.append([0, 0, 0])
        rides.sort(key=lambda x: x[1])
        for i in range(1, n + 1):
            st, ed, tip = rides[i]
            profit = tip + ed - st
            lo, hi = 0, i
            while lo + 1 < hi:
                md = (lo + hi) // 2
                if rides[md][1] <= st:
                    lo = md
                else:
                    hi = md
            dp[i] = max(dp[i - 1], dp[lo] + profit)
        return dp[n]