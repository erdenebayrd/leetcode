class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        to find min number of deletions from both string to make them equal
        means, to find longest common substring of them. Then add absolute diff between them.
        formally
        min_distance = len(word1) - lcs + len(word2) - lcs = len(word1) + len(word2) - 2 * lcs
        to find lcs, we can use 2 dimension DP
        """
        # time: O(n * m)
        # space: O(n * m)
        # method: DP LCS
        n = len(word1)
        m = len(word2)
        dp = [[0] * m for _ in range(n)]
        lcs = 0
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
                if word1[i] == word2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
            lcs = max(lcs, dp[i][j])
        return len(word1) + len(word2) - 2 * lcs