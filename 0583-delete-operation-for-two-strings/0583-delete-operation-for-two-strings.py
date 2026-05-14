from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # time: O(N * M)
        # space: O(N * M)
        # method: DP
        
        n = len(word1)
        m = len(word2)
        
        dp = [[0] * m for _ in range(n)]
        
        lcs = 0
        for i in range(n):
            for j in range(m):
                if j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
                if i - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if word1[i] == word2[j]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                    else:
                        dp[i][j] = 1
                lcs = max(lcs, dp[i][j])
        # print(dp)
        # print(lcs)
        result = n + m - 2 * lcs
        return result