class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        rides.sort(key=lambda x: x[1])
        rideIdx = 0
        for ri in range(1, n + 1):
            dp[ri] = max(dp[ri], dp[ri - 1])
            while rideIdx < len(rides) and ri == rides[rideIdx][1]:
                st, ed, tip = rides[rideIdx]
                dp[ri] = max(dp[ri], dp[st] + ed - st + tip)
                rideIdx += 1
        return dp[n]