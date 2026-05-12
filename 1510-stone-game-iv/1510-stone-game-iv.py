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
            k = 1
            while k * k <= i:
                if dp[i - k * k] is False:
                    dp[i] = True
                    break
                k += 1
        return dp[n]