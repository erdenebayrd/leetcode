from functools import lru_cache
from math import sqrt

class Solution:
    # time: O(N * sqrt(N))
    # space: O(N)
    # method: DP

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[1] = True
        for i in range(2, n + 1):
            k = int(sqrt(i))
            if k * k == i:
                dp[i] = True
            else:
                for j in range(1, k + 1):
                    dp[i] |= (not dp[i - j * j])
        return dp[n]