from functools import lru_cache
from math import sqrt

class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        k = int(sqrt(n))
        if k * k == n:
            return True
        result = False
        for i in range(1, k + 1):
            result |= (not self.winnerSquareGame(n - i * i))
        return result