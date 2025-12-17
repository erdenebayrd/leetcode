class Solution:
    def maximumProfit(self, prices: List[int], m: int) -> int:
        # time: O(k * n)
        # space: O(k * n)
        
        # m pairs, which need to choose at most without any intersection between them
        n = len(prices)
        dp = [[0] * n for _ in range(m + 1)]
        for i in range(1, m + 1):
            maxLong = -prices[0]   # k=-1 case: dp[i-1][-1]=0, buy at index 0
            maxShort = prices[0]   # k=-1 case: dp[i-1][-1]=0, short at index 0
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1]

                # end transaction at j
                dp[i][j] = max(dp[i][j], prices[j] + maxLong)    # sell long
                dp[i][j] = max(dp[i][j], maxShort - prices[j])   # cover short
                # for k in range(j - 1):
                #     dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(prices[k + 1] - prices[j]))
                # # The `abs(prices[k+1] - prices[j])` can be split into two cases:
                # # - **Long (buy then sell):** `prices[j] - prices[k+1]`
                # # - **Short (sell then buy):** `prices[k+1] - prices[j]`

                # if i == 1:
                #     dp[i][j] = max(dp[i][j], abs(prices[0] - prices[j]))
                # at most, not exactly M, can be lower than M and can be exactly M
                dp[i][j] = max(dp[i][j], dp[i - 1][j])

                # update running max for next j
                # k = j-1: can start new transaction at index j
                maxLong = max(maxLong, dp[i - 1][j - 1] - prices[j])
                maxShort = max(maxShort, dp[i - 1][j - 1] + prices[j])

        return dp[m][n - 1]