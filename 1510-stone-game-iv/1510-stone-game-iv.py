from functools import cache
from math import sqrt

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # time: O(N * sqrt(N))
        # space: O(N)
        # method: DP

        @cache
        def solve(stones: int, alice_turn: bool) -> bool:
            limit = int(sqrt(stones))
            for stone in range(1, limit + 1):
                if alice_turn:
                    if solve(stones - stone * stone, not alice_turn):
                        return True
                else:
                    if not solve(stones - stone * stone, not alice_turn):
                        return False
            return not alice_turn

        return solve(n, True)