class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # time: O(N * 3)
        # space: O(N * 3)
        # method: DP
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        for color in range(3):
            dp[0][color] = costs[0][color]
        for house in range(1, n):
            dp[house][0] = costs[house][0] + min(dp[house - 1][1], dp[house - 1][2])
            dp[house][1] = costs[house][1] + min(dp[house - 1][0], dp[house - 1][2])
            dp[house][2] = costs[house][2] + min(dp[house - 1][0], dp[house - 1][1])
        return min(dp[n - 1])