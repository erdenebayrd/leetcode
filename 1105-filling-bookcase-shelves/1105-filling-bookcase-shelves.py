from functools import cache

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # time: O(N ^ 2)
        # space: O(N)
        # method: bottom-up DP
        n = len(books)
        dp = [float('inf')] * n
        dp[0] = books[0][1]
        for i in range(1, n):
            currentWidth, currentHeight = 0, 0
            for j in range(i, -1, -1):
                currentWidth += books[j][0]
                currentHeight = max(currentHeight, books[j][1])
                if currentWidth > shelfWidth:
                    break
                if j - 1 >= 0:
                    dp[i] = min(dp[i], currentHeight + dp[j - 1])
                else:
                    dp[i] = min(dp[i], currentHeight)
        return dp[n - 1]