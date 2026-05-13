from typing import Tuple
from functools import lru_cache

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # time: O(N ^ 2)
        # space: O(N ^ 2)
        # method: DP

        n = len(stones)
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] += prefix[i - 1] + stones[i]

        def score(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == 0:
                return prefix[right]
            return prefix[right] - prefix[left - 1]

        @lru_cache(None)
        def solve(left: int, right: int, alice_turn: bool) -> Tuple[int, int]:
            if left > right:
                return (0, 0)
            
            alice = bob = 0
            take_left_score = score(left + 1, right)
            take_left_alice, take_left_bob = solve(left + 1, right, not alice_turn)

            take_right_score = score(left, right - 1)
            take_right_alice, take_right_bob = solve(left, right - 1, not alice_turn)
            if alice_turn:
                if take_left_score + take_left_alice - take_left_bob > take_right_score + take_right_alice - take_right_bob:
                    alice, bob = take_left_score + take_left_alice, take_left_bob
                else:
                    alice, bob = take_right_score + take_right_alice, take_right_bob
            else:
                if take_left_alice - (take_left_score + take_left_bob) < take_right_alice - (take_right_score + take_right_bob):
                    alice, bob = take_left_alice, take_left_score + take_left_bob
                else:
                    alice, bob = take_right_alice, take_right_score + take_right_bob
            return (alice, bob)
        
        alice, bob = solve(0, n - 1, True)
        solve.cache_clear()
        return alice - bob
